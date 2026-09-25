"""XLSX builder unit tests."""

import pathlib
import tempfile
import unittest
import zipfile
from xml.etree.ElementTree import Element, ElementTree, SubElement, fromstring

import xmltags
from builder.xlsx_builder import SelfAssessmentXlsxBuilder
from converter import Converter

SPREADSHEET_NAMESPACE = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"


class SelfAssessmentXlsxBuilderTest(unittest.TestCase):
    """Unit tests for the self-assessment builder."""

    def setUp(self):
        """Create a document with a composite measure."""
        self.document = Element(xmltags.DOCUMENT, {xmltags.DOCUMENT_VERSION: "1"})
        chapter = self.add_section(self.document, "1", "Maatregelen")
        self.measure_section = self.add_section(chapter, "2", "M01")
        measure = SubElement(self.measure_section, xmltags.MEASURE, {"composite": "true"})
        measure_title = SubElement(SubElement(measure, xmltags.PARAGRAPH), xmltags.MEASURE_TITLE)
        measure_title.text = "M01: Measure"
        numbered_list = SubElement(self.measure_section, xmltags.NUMBERED_LIST, {xmltags.LIST_LEVEL: "1"})
        for number in ("1", "2"):
            item = SubElement(numbered_list, xmltags.LIST_ITEM, {xmltags.LIST_ITEM_NUMBER: number})
            submeasure_title = SubElement(item, xmltags.SUBMEASURE_TITLE, {xmltags.SUBMEASURE_TITLE_NUMBER: number})
            submeasure_title.text = f"Submeasure {number}"
        self.add_section(self.measure_section, "3", "Rationale", "Rationale text")

    @staticmethod
    def add_section(parent: Element, level: str, heading: str, text: str = "", submeasures: str = "") -> Element:
        """Add a section with heading and optional paragraph to the parent."""
        attributes = {xmltags.SECTION_LEVEL: level} | (
            {xmltags.SECTION_SUBMEASURES: submeasures} if submeasures else {}
        )
        section = SubElement(parent, xmltags.SECTION, attributes)
        SubElement(section, xmltags.HEADING).text = heading
        if text:
            SubElement(section, xmltags.PARAGRAPH).text = text
        return section

    def comments(self) -> dict[str, str]:
        """Build the spreadsheet and return the comments in the measure column by cell reference."""
        with tempfile.TemporaryDirectory() as directory:
            filename = pathlib.Path(directory) / "output.xlsx"
            Converter(ElementTree(self.document)).convert(SelfAssessmentXlsxBuilder(filename))
            comments_xml = fromstring(zipfile.ZipFile(filename).read("xl/comments1.xml"))
        return {
            comment.attrib["ref"]: "".join(text.text or "" for text in comment.iter(f"{SPREADSHEET_NAMESPACE}t"))
            for comment in comments_xml.iter(f"{SPREADSHEET_NAMESPACE}comment")
            if comment.attrib["ref"].startswith("B")
        }

    def test_measure_comment(self):
        """Test that the measure comment contains the complete measure text if no sections explain submeasures."""
        self.add_section(self.measure_section, "3", "Explanation", "Explanation text")
        comment = self.comments()["B7"]
        self.assertIn("M01: Measure", comment)
        self.assertIn("1. Submeasure 1", comment)
        self.assertIn("Explanation text", comment)
        self.assertIn("Rationale text", comment)

    def test_submeasure_comments(self):
        """Test that sections that explain submeasures are added to the submeasure comments."""
        self.add_section(self.measure_section, "3", "Explanation 1", "Explanation text 1", submeasures="1")
        self.add_section(self.measure_section, "3", "Explanation 2", "Explanation text 2", submeasures="1,2")
        comments = self.comments()
        self.assertNotIn("Explanation", comments["B7"])
        self.assertIn("Rationale text", comments["B7"])
        self.assertEqual("Explanation 1\n\nExplanation text 1\n\nExplanation 2\n\nExplanation text 2", comments["B8"])
        self.assertEqual("Explanation 2\n\nExplanation text 2", comments["B9"])

    def test_explanation_of_missing_submeasure(self):
        """Test that an explanation of a submeasure that does not exist is an error."""
        self.add_section(self.measure_section, "3", "Explanation", "Explanation text", submeasures="3")
        self.assertRaises(ValueError, self.comments)
