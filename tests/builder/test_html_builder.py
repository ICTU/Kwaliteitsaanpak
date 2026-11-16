"""HTML builder unit tests."""

import pathlib
import tempfile
import unittest
from xml.etree.ElementTree import Element, ElementTree, SubElement

from pygments.util import ClassNotFound

import xmltags
from builder.html_builder import HTMLBuilder
from converter import Converter


class CodeBlockTest(unittest.TestCase):
    """Unit tests for code blocks in the HTML builder."""

    def build(self, language: str, code: str) -> str:
        """Build an HTML document with a single code block and return its contents."""
        document = Element(xmltags.DOCUMENT, {"title": "Title", "version": "1"})
        SubElement(document, xmltags.FRONTPAGE)  # Starts the <main> element that the document end closes
        code_block = SubElement(document, xmltags.CODE_BLOCK, {xmltags.CODE_BLOCK_LANGUAGE: language})
        code_block.text = code
        with tempfile.TemporaryDirectory() as directory:
            filename = pathlib.Path(directory) / "output.html"
            Converter(ElementTree(document)).convert(HTMLBuilder(filename, pathlib.Path("style.css")))
            return filename.read_text(encoding="utf-8")

    def test_highlighting(self):
        """Test that the code is highlighted, e.g. keywords get the keyword token class."""
        html = self.build("python", "def f(x):\n    return 1\n")
        self.assertIn('<div class="highlight">', html)
        self.assertIn('class="k"', html)

    def test_indentation_preserved(self):
        """Test that the indentation of the code is preserved."""
        html = self.build("python", "def f():\n    return 1\n")
        self.assertIn("\n    <span", html)

    def test_special_characters_escaped(self):
        """Test that characters that are special in HTML are escaped rather than parsed as markup."""
        html = self.build("python", "# a < b & c\n")
        self.assertIn("a &lt; b &amp; c", html)

    def test_unknown_language(self):
        """Test that an unknown language raises an exception."""
        self.assertRaises(ClassNotFound, self.build, "nonexistent", "code\n")


class TextFormattingTest(unittest.TestCase):
    """Unit tests for fomatting text."""

    def build(self, xmltag: str) -> str:
        """Build an HTML document with a line."""
        document = Element(xmltags.DOCUMENT, {"title": "Title", "version": "1"})
        SubElement(document, xmltags.FRONTPAGE)  # Starts the <main> element that the document end closes
        paragraph = SubElement(document, xmltags.PARAGRAPH, {})
        formatted = SubElement(paragraph, xmltag)
        formatted.text = "formatted"
        with tempfile.TemporaryDirectory() as directory:
            filename = pathlib.Path(directory) / "output.html"
            Converter(ElementTree(document)).convert(HTMLBuilder(filename, pathlib.Path("style.css")))
            return filename.read_text(encoding="utf-8")

    def test_bold(self):
        """Test bold text."""
        html = self.build(xmltags.BOLD)
        self.assertIn("<strong>formatted</strong>", html)

    def test_italic(self):
        """Test italic text."""
        html = self.build(xmltags.ITALIC)
        self.assertIn("<em>formatted</em>", html)

    def test_strikethrough(self):
        """Test italic text."""
        html = self.build(xmltags.STRIKETHROUGH)
        self.assertIn("<s>formatted</s>", html)

    def test_code(self):
        """Test code text."""
        html = self.build(xmltags.CODE)
        self.assertIn("<code>formatted</code>", html)


class AbbreviationTest(unittest.TestCase):
    """Unit tests for abbreviations in the HTML builder."""

    def build(self, attributes: dict[str, str]) -> str:
        """Build an HTML document with an abbreviation."""
        document = Element(xmltags.DOCUMENT, {"title": "Title", "version": "1"})
        SubElement(document, xmltags.FRONTPAGE)  # Starts the <main> element that the document end closes
        paragraph = SubElement(document, xmltags.PARAGRAPH, {})
        paragraph.text = "De "
        abbreviation = SubElement(paragraph, xmltags.ABBREVIATION, attributes)
        abbreviation.text = "API"
        abbreviation.tail = " is gedocumenteerd."
        with tempfile.TemporaryDirectory() as directory:
            filename = pathlib.Path(directory) / "output.html"
            Converter(ElementTree(document)).convert(HTMLBuilder(filename, pathlib.Path("style.css")))
            return filename.read_text(encoding="utf-8")

    def test_abbreviation(self):
        """Test that an abbreviation is an abbr-element within a link to the definition of the abbreviation."""
        html = self.build({xmltags.ABBREVIATION_TITLE: "application programming interface"})
        self.assertIn(
            '<p>De <a class="afkorting" href="#afkorting-api">'
            '<abbr title="application programming interface">API</abbr></a> is gedocumenteerd.</p>',
            html,
        )

    def test_definition(self):
        """Test that the definition of an abbreviation is an abbr-element with an id, without title and link."""
        html = self.build(
            {xmltags.ABBREVIATION_TITLE: "application programming interface", xmltags.ABBREVIATION_IS_DEFINITION: "y"}
        )
        self.assertIn(
            '<p>De <abbr id="afkorting-api">API</abbr> is gedocumenteerd.</p>',
            html,
        )


class ElementTest(unittest.TestCase):
    """Unit tests for tables, links, and images in the HTML builder."""

    def setUp(self):
        self.document = Element(xmltags.DOCUMENT, {"title": "Title", "version": "1"})
        SubElement(self.document, xmltags.FRONTPAGE)  # Starts the <main> element that the document end closes

    def build(self) -> str:
        """Build an HTML document."""
        with tempfile.TemporaryDirectory() as directory:
            filename = pathlib.Path(directory) / "output.html"
            Converter(ElementTree(self.document)).convert(HTMLBuilder(filename, pathlib.Path("style.css")))
            return filename.read_text(encoding="utf-8")

    def test_table(self):
        """Test that a table has a header with header cells and a body with aligned cells."""
        table = SubElement(self.document, xmltags.TABLE)
        for row_tag, cell_text, alignment in (
            (xmltags.TABLE_HEADER_ROW, "Kop", "left"),
            (xmltags.TABLE_ROW, "Cel", "right"),
        ):
            cell = SubElement(SubElement(table, row_tag), xmltags.TABLE_CELL, {xmltags.TABLE_CELL_ALIGNMENT: alignment})
            cell.text = cell_text
        self.assertIn(
            '<table><thead><tr><th style="text-align:left">Kop</th></tr></thead>'
            '<tbody><tr><td style="text-align:right">Cel</td></tr></tbody></table>',
            self.build(),
        )

    def test_link(self):
        """Test that a link is an anchor."""
        anchor = SubElement(
            SubElement(self.document, xmltags.PARAGRAPH), xmltags.ANCHOR, {xmltags.ANCHOR_LINK: "#bronnen"}
        )
        anchor.text = "Bronnen"
        self.assertIn('<p><a href="#bronnen">Bronnen</a></p>', self.build())

    def test_image(self):
        """Test that the alternative text of an image consists of the title and the alternative text."""
        SubElement(
            SubElement(self.document, xmltags.PARAGRAPH),
            xmltags.IMAGE,
            {xmltags.IMAGE_SRC: "plaatje.png", xmltags.IMAGE_TITLE: "Titel", xmltags.IMAGE_ALT: "Beschrijving"},
        )
        self.assertIn('<img style="max-width: 100%" src="plaatje.png" alt="Titel: Beschrijving">', self.build())


class HTMLEntitiesToXMLTest(unittest.TestCase):
    """Unit tests for converting named HTML entities to numeric character references."""

    def test_named_entity(self):
        """Test that a named HTML entity is turned into a numeric character reference."""
        self.assertEqual("a&#160;b", HTMLBuilder.html_entities_to_xml("a&nbsp;b"))

    def test_xml_entities_kept(self):
        """Test that the entities the XML parser already understands are left untouched."""
        self.assertEqual("&amp;&lt;&gt;&quot;&apos;", HTMLBuilder.html_entities_to_xml("&amp;&lt;&gt;&quot;&apos;"))

    def test_unknown_entity_kept(self):
        """Test that an unknown entity is left untouched."""
        self.assertEqual("&unknown;", HTMLBuilder.html_entities_to_xml("&unknown;"))


class AdmonitionTest(unittest.TestCase):
    """Unit tests for admonitions in the HTML builder."""

    def build(self, *, after_heading: bool = False) -> str:
        """Build an HTML document with an admonition that contains a paragraph and return its contents."""
        document = Element(xmltags.DOCUMENT, {"title": "Title", "version": "1"})
        SubElement(document, xmltags.FRONTPAGE)  # Starts the <main> element that the document end closes
        parent = document
        if after_heading:
            parent = SubElement(document, xmltags.SECTION, {xmltags.SECTION_LEVEL: "2"})
            SubElement(parent, xmltags.HEADING).text = "Heading"
        admonition = SubElement(
            parent, xmltags.ADMONITION, {xmltags.ADMONITION_TYPE: "warning", xmltags.ADMONITION_TITLE: "Waarschuwing"}
        )
        paragraph = SubElement(admonition, xmltags.PARAGRAPH)
        paragraph.text = "Some "
        SubElement(paragraph, xmltags.BOLD).text = "bold"
        with tempfile.TemporaryDirectory() as directory:
            filename = pathlib.Path(directory) / "output.html"
            Converter(ElementTree(document)).convert(HTMLBuilder(filename, pathlib.Path("style.css")))
            return filename.read_text(encoding="utf-8")

    def test_admonition(self):
        """Test that the admonition is an aside with a class per type, an icon, a title, and the contents."""
        html = self.build()
        self.assertIn('<aside class="admonition admonition-warning"><p class="admonition-title"><svg ', html)
        self.assertIn('class="admonition-icon"', html)
        self.assertIn("</svg>Waarschuwing</p><p>Some <strong>bold</strong></p></aside>", html)

    def test_admonition_after_heading(self):
        """Test that the heading is kept together with the whole admonition."""
        html = self.build(after_heading=True)
        self.assertIn('<div class="keep-together"><h2 id="heading">Heading</h2><aside ', html)
        self.assertIn("</aside></div>", html)
