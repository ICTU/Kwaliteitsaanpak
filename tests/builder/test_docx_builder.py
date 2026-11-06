"""Docx builder unit tests."""

import pathlib
import tempfile
import unittest
from xml.etree.ElementTree import Element, ElementTree, SubElement

import docx
from docx.document import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Cm
from docx.text.paragraph import Paragraph
from pygments.util import ClassNotFound

import xmltags
from builder.docx_builder import DocxBuilder
from converter import Converter

REFERENCE_DOCX = pathlib.Path(__file__).parents[2] / "DocumentDefinitions" / "reference-neutral.docx"
BREAK = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}br"


class CodeBlockTest(unittest.TestCase):
    """Unit tests for code blocks in the docx builder."""

    def build(self, language: str, code: str) -> Document:
        """Build a docx with a single code block and return the resulting document."""
        document = Element(xmltags.DOCUMENT)
        code_block = SubElement(document, xmltags.CODE_BLOCK, {xmltags.CODE_BLOCK_LANGUAGE: language})
        code_block.text = code
        with tempfile.TemporaryDirectory() as directory:
            filename = pathlib.Path(directory) / "output.docx"
            Converter(ElementTree(document)).convert(DocxBuilder(filename, REFERENCE_DOCX, pathlib.Path(".")))
            return docx.Document(str(filename))

    def code_paragraph(self, document: Document) -> Paragraph:
        """Return the code block paragraph that was added (the last paragraph with the Code style)."""
        code_paragraphs = [
            paragraph
            for paragraph in document.paragraphs
            if paragraph.style is not None and paragraph.style.name == "Code"
        ]
        return code_paragraphs[-1]

    def test_code(self):
        """Test that the code is added verbatim, with line breaks between the lines."""
        paragraph = self.code_paragraph(self.build("python", "def f(x):\n    return x + 1\n"))
        self.assertEqual("def f(x):\n    return x + 1", paragraph.text)
        self.assertEqual(1, sum(len(run._r.findall(BREAK)) for run in paragraph.runs))

    def test_highlighting(self):
        """Test that tokens are highlighted, e.g. the keywords are green in the default style."""
        paragraph = self.code_paragraph(self.build("python", "def f(x):\n    return 1\n"))
        colors = {str(run.font.color.rgb) for run in paragraph.runs if run.font.color and run.font.color.rgb}
        self.assertIn("008000", colors)

    def test_yaml(self):
        """Test a YAML code block; the YAML lexer emits token types not styled in their own right."""
        paragraph = self.code_paragraph(self.build("yaml", "name: value\nlist:\n  - a\n"))
        self.assertEqual("name: value\nlist:\n  - a", paragraph.text)

    def test_unknown_language(self):
        """Test that an unknown language raises an exception."""
        self.assertRaises(ClassNotFound, self.build, "nonexistent", "code\n")


class TextFormattingTest(unittest.TestCase):
    """Unit tests for fomatting text."""

    def build(self, xmltag: str) -> Document:
        """Build an docx with a formatted paragraph."""
        document = Element(xmltags.DOCUMENT, {"title": "Title", "version": "1"})
        SubElement(document, xmltags.FRONTPAGE)  # Starts the <main> element that the document end closes
        paragraph = SubElement(document, xmltags.PARAGRAPH, {})
        formatted = SubElement(paragraph, xmltag)
        formatted.text = "formatted"
        with tempfile.TemporaryDirectory() as directory:
            filename = pathlib.Path(directory) / "output.docx"
            Converter(ElementTree(document)).convert(DocxBuilder(filename, REFERENCE_DOCX, pathlib.Path(".")))
            return docx.Document(str(filename))

    def test_bold(self):
        """Test bold text."""
        document = self.build(xmltags.BOLD)
        self.assertTrue(document.paragraphs[-1].runs[-1].bold)

    def test_italic(self):
        """Test italic text."""
        document = self.build(xmltags.ITALIC)
        self.assertTrue(document.paragraphs[-1].runs[-1].italic)

    def test_strikethrough(self):
        """Test strikethrough text."""
        document = self.build(xmltags.STRIKETHROUGH)
        self.assertTrue(document.paragraphs[-1].runs[-1].font.strike)

    def test_code(self):
        """Test code text."""
        document = self.build(xmltags.CODE)
        self.assertEqual("Fira code", document.paragraphs[-1].runs[-1].font.name)


class DocumentStructureTest(unittest.TestCase):
    """Unit tests for the document structure elements in the docx builder."""

    def setUp(self):
        self.document = Element(xmltags.DOCUMENT)

    def build(self) -> Document:
        """Build a docx from the XML document and return the resulting document."""
        images_folder = pathlib.Path(__file__).parents[2] / "Content" / "Images"
        with tempfile.TemporaryDirectory() as directory:
            filename = pathlib.Path(directory) / "output.docx"
            Converter(ElementTree(self.document)).convert(DocxBuilder(filename, REFERENCE_DOCX, images_folder))
            return docx.Document(str(filename))

    def add_list(self, parent: Element, tag: str, *items: str) -> Element:
        """Add a list with the items to the parent."""
        xml_list = SubElement(parent, tag)
        for item in items:
            SubElement(xml_list, xmltags.LIST_ITEM).text = item
        return xml_list

    def test_title(self):
        """Test that the title gets the title style."""
        SubElement(self.document, xmltags.TITLE).text = "Title"
        paragraph = self.build().paragraphs[-1]
        self.assertEqual("Title", paragraph.text)
        self.assertEqual("Title", paragraph.style.name)

    def test_heading(self):
        """Test that the heading style depends on the section level."""
        section = SubElement(self.document, xmltags.SECTION, {xmltags.SECTION_LEVEL: "1"})
        subsection = SubElement(section, xmltags.SECTION, {xmltags.SECTION_LEVEL: "2"})
        SubElement(subsection, xmltags.HEADING).text = "Heading"
        paragraph = self.build().paragraphs[-1]
        self.assertEqual("Heading", paragraph.text)
        self.assertEqual("Heading 2", paragraph.style.name)

    def test_appendix_heading(self):
        """Test that headings in appendices get the appendix heading style."""
        section = SubElement(
            self.document, xmltags.SECTION, {xmltags.SECTION_LEVEL: "1", xmltags.SECTION_IS_APPENDIX: "y"}
        )
        SubElement(section, xmltags.HEADING).text = "Appendix"
        self.assertEqual("Kop 1 Bijlage", self.build().paragraphs[-1].style.name)

    def test_bullet_list(self):
        """Test that bullet list items get the bullet list style."""
        self.add_list(self.document, xmltags.BULLET_LIST, "one", "two")
        paragraphs = self.build().paragraphs[-2:]
        self.assertEqual(["one", "two"], [paragraph.text for paragraph in paragraphs])
        self.assertEqual({"Lijst opsom.teken1"}, {paragraph.style.name for paragraph in paragraphs})

    def test_numbered_list(self):
        """Test that the items of a numbered list share a numbering and that a new list restarts the numbering."""
        self.add_list(self.document, xmltags.NUMBERED_LIST, "one", "two")
        self.add_list(self.document, xmltags.NUMBERED_LIST, "three")
        paragraphs = self.build().paragraphs[-3:]
        num_ids = [paragraph._p.pPr.numPr.numId.val for paragraph in paragraphs]
        self.assertEqual({"Lijstnummering1"}, {paragraph.style.name for paragraph in paragraphs})
        self.assertEqual(num_ids[0], num_ids[1])
        self.assertNotEqual(num_ids[1], num_ids[2])

    def test_nested_list(self):
        """Test that nested list items get a higher list level."""
        bullet_list = self.add_list(self.document, xmltags.BULLET_LIST, "one")
        self.add_list(bullet_list, xmltags.BULLET_LIST, "nested")
        paragraphs = self.build().paragraphs[-2:]
        self.assertEqual([0, 1], [paragraph._p.pPr.numPr.ilvl.val for paragraph in paragraphs])

    def test_table(self):
        """Test that a table is added with the table style, a full width, and the cell contents."""
        table = SubElement(self.document, xmltags.TABLE, {xmltags.TABLE_COLUMNS: "2", xmltags.TABLE_ROWS: "1"})
        for row_tag, texts in ((xmltags.TABLE_HEADER_ROW, ("A", "B")), (xmltags.TABLE_ROW, ("1", "2"))):
            row = SubElement(table, row_tag)
            for alignment, text in zip(("left", "right"), texts):
                SubElement(row, xmltags.TABLE_CELL, {xmltags.TABLE_CELL_ALIGNMENT: alignment}).text = text
        docx_table = self.build().tables[-1]
        self.assertEqual("Tabelraster1", docx_table.style.name)
        self.assertEqual("100%", docx_table._tbl.tblPr.xpath("./w:tblW")[0].get(f"{DocxBuilder.SCHEMA}w"))
        self.assertEqual([["A", "B"], ["1", "2"]], [[cell.text for cell in row.cells] for row in docx_table.rows])
        self.assertEqual(WD_PARAGRAPH_ALIGNMENT.RIGHT, docx_table.cell(1, 1).paragraphs[0].alignment)

    def test_image(self):
        """Test that an image is added with its title."""
        SubElement(
            self.document,
            xmltags.IMAGE,
            {xmltags.IMAGE_SRC: "ICTU.png", xmltags.IMAGE_TITLE: "ICTU logo", xmltags.IMAGE_WIDTH: "5"},
        )
        inline_shape = self.build().inline_shapes[-1]
        self.assertEqual("ICTU logo", inline_shape._inline.docPr.get("title"))
        self.assertEqual(Cm(5), inline_shape.width)
