"""Markdown converter unit tests."""

import unittest
from unittest.mock import patch, Mock
from typing import cast
from xml.etree.ElementTree import Element, ElementTree

import xmltags
from custom_types import Settings, Variables
from markdown_converter import MarkdownConverter


class MarkdownConverterTestCase(unittest.TestCase):
    """Base class for Markdown converter tests."""

    def setUp(self):
        self.settings = Settings(
            {
                "BuildPath": ".",
                "FrontPage": "",
                "DocumentType": "Kwaliteitsaanpak",
                "Title": "Title",
                "Subtitle": "Subtitle",
                "Version": "x.y",
                "Date": "2020-20-20",
                "OutputFormats": {
                    "html": {
                        "IncludeTableOfContents": False,
                        "InputFile": "document.md",
                    }
                },
            }
        )

    def xml(self) -> ElementTree:
        """Create the XML."""
        return MarkdownConverter(Variables({"var": "variable"})).convert(self.settings, "html")

    def find(self, path: str, parent: Element | None = None) -> Element:
        """Find a path."""
        return cast(Element, self.xml().find(path) if parent is None else parent.find(path))


@patch("markdown_converter.pathlib.Path.read_text", Mock(return_value=""))
@patch("markdown_converter.pathlib.Path.write_text", Mock())
class EmptyMarkdownTest(MarkdownConverterTestCase):
    """Unit test for the Markdown converter with empty Markdown."""

    def test_title(self):
        """Test the document title."""
        self.assertEqual(self.settings["Title"], cast(Element, self.xml().getroot()).attrib[xmltags.DOCUMENT_TITLE])

    def test_frontpage_kwaliteitsaanpak(self):
        """Test the front page of the Kwaliteitsaanpak."""
        self.settings["FrontPage"] = "ICTU"
        self.assertIsNotNone(self.xml().find(xmltags.FRONTPAGE))

    def test_frontpage_template(self):
        """Test the front page of templates."""
        self.settings["DocumentType"] = "Template"
        self.settings["FrontPage"] = "ICTU"
        self.assertIsNotNone(self.xml().find(xmltags.FRONTPAGE))

    def test_frontpage_unknown_document_type(self):
        """Test that an unknown document type raises an exception."""
        self.settings["DocumentType"] = "Wrong type"
        self.settings["FrontPage"] = "ICTU"
        self.assertRaises(ValueError, MarkdownConverter(Variables({})).convert, self.settings, "html")

    def test_frontpage_title(self):
        """Test the front page title."""
        self.settings["FrontPage"] = "ICTU"
        frontpage = self.find(xmltags.FRONTPAGE)
        self.assertEqual(self.settings["Title"], self.find(xmltags.TITLE, frontpage).text)

    def test_toc(self):
        """Test the table of contents."""
        self.settings["OutputFormats"]["html"]["IncludeTableOfContents"] = True
        self.assertIsNotNone(self.xml().find(xmltags.TABLE_OF_CONTENTS))


@patch("markdown_converter.pathlib.Path.write_text", Mock())
class MarkdownTest(MarkdownConverterTestCase):
    """Unit test for the Markdown converter."""

    read_text = "markdown_converter.pathlib.Path.read_text"

    @patch(read_text, Mock(return_value="# Heading 1\n## Heading 2"))
    def test_headings(self):
        """Test nested headings."""
        section1 = self.find(xmltags.SECTION)
        self.assertEqual("1", section1.attrib[xmltags.SECTION_LEVEL])
        self.assertEqual("Heading 1", self.find(xmltags.HEADING, section1).text)
        section2 = self.find(xmltags.SECTION, section1)
        self.assertEqual("2", section2.attrib[xmltags.SECTION_LEVEL])
        self.assertEqual("Heading 2", self.find(xmltags.HEADING, section2).text)

    @patch(read_text, Mock(return_value="# Bijlagen\n## Appendix"))
    def test_appendix_headings(self):
        """Test appendix headings."""
        appendices = self.find(xmltags.SECTION)
        self.assertEqual("Bijlagen", self.find(xmltags.HEADING, appendices).text)
        self.assertEqual("1", appendices.attrib[xmltags.SECTION_LEVEL])
        self.assertEqual("y", appendices.attrib[xmltags.SECTION_IS_APPENDIX])
        appendix = self.find(xmltags.SECTION, appendices)
        self.assertEqual("Appendix", self.find(xmltags.HEADING, appendix).text)

    @patch(read_text, Mock(return_value="## Heading 2"))
    def test_open_implicit_sections(self):
        """Test start with a nested heading."""
        section1 = self.find(xmltags.SECTION)
        self.assertEqual("1", section1.attrib[xmltags.SECTION_LEVEL])
        section2 = self.find(xmltags.SECTION, section1)
        self.assertEqual("2", section2.attrib[xmltags.SECTION_LEVEL])
        self.assertEqual("Heading 2", self.find(xmltags.HEADING, section2).text)

    @patch(read_text, Mock(return_value="## Heading 2\n# Heading 1"))
    def test_close_implicit_sections(self):
        """Test that a nested heading is closed properly."""
        section2 = self.xml().findall(xmltags.SECTION)[1]
        self.assertEqual("Heading 1", self.find(xmltags.HEADING, section2).text)

    @patch(
        read_text,
        Mock(
            return_value="**Bold** _Italic_ ~~Strike~~ {Instruction} [Anchor](link) "
            "[measure-title]Measure[/measure-title] [submeasure-title]Submeasure[/submeasure-title]"
        ),
    )
    def test_formatting(self):
        """Test formatting."""
        paragraph = self.find(xmltags.PARAGRAPH)
        self.assertEqual("Bold", self.find(xmltags.BOLD, paragraph).text)
        self.assertEqual("Italic", self.find(xmltags.ITALIC, paragraph).text)
        self.assertEqual("Strike", self.find(xmltags.STRIKETHROUGH, paragraph).text)
        self.assertEqual("{Instruction}", self.find(xmltags.INSTRUCTION, paragraph).text)
        self.assertEqual("Anchor", self.find(xmltags.ANCHOR, paragraph).text)
        self.assertEqual("link", self.find(xmltags.ANCHOR, paragraph).attrib[xmltags.ANCHOR_LINK])
        self.assertEqual("Measure", self.find(xmltags.MEASURE_TITLE, paragraph).text)
        self.assertEqual("Submeasure", self.find(xmltags.SUBMEASURE_TITLE, paragraph).text)
        self.assertEqual("1", self.find(xmltags.SUBMEASURE_TITLE, paragraph).attrib[xmltags.SUBMEASURE_TITLE_NUMBER])

    @patch(read_text, Mock(return_value='![Anchor](image.png "description")'))
    def test_image(self):
        """Test image."""
        image = self.find(f".//{xmltags.IMAGE}")
        self.assertEqual("image.png", image.attrib[xmltags.IMAGE_SRC])
        self.assertEqual("description", image.attrib[xmltags.IMAGE_TITLE])

    @patch(read_text, Mock(return_value="* Bullet\n* list\n\n"))
    def test_bullet_list(self):
        """Test bullet list."""
        bullet_list = self.find(xmltags.BULLET_LIST)
        self.assertEqual("Bullet", self.find(xmltags.LIST_ITEM, bullet_list).text)

    @patch(read_text, Mock(return_value="1. Numbered\n2. list\n\n"))
    def test_numbered_list(self):
        """Test bullet list."""
        numbered_list = self.find(xmltags.NUMBERED_LIST)
        self.assertEqual("Numbered", self.find(xmltags.LIST_ITEM, numbered_list).text)
        self.assertEqual("1", self.find(xmltags.LIST_ITEM, numbered_list).attrib[xmltags.LIST_ITEM_NUMBER])

    @patch(read_text, Mock(return_value="|col1|col2|col3|\n|:---:||:---|---:|\n|cell1|cell2|cell3|\n\n"))
    def test_table(self):
        """Test table."""
        table = self.find(xmltags.TABLE)
        self.assertEqual(
            ("1", "3"),
            (table.attrib[xmltags.TABLE_ROWS], table.attrib[xmltags.TABLE_COLUMNS]),
        )
        header_row = self.find(xmltags.TABLE_HEADER_ROW, table)
        self.assertEqual("col1", self.find(xmltags.TABLE_CELL, header_row).text)
        row = self.find(xmltags.TABLE_ROW, table)
        cell = self.find(xmltags.TABLE_CELL, row)
        self.assertEqual("cell1", cell.text)
        self.assertEqual(
            ("1", "0"),
            (
                cell.attrib[xmltags.TABLE_CELL_ROW],
                cell.attrib[xmltags.TABLE_CELL_COLUMN],
            ),
        )
        self.assertEqual("center", cell.attrib[xmltags.TABLE_CELL_ALIGNMENT])
        self.assertEqual(str(len("cell1")), cell.attrib[xmltags.TABLE_CELL_WIDTH])

    @patch(read_text, Mock(return_value="|text\n\n"))
    def test_table_marker_without_columns(self):
        """Test an incomplete table."""
        table = self.find(xmltags.TABLE)
        self.assertEqual(
            ("0", "1"),
            (table.attrib[xmltags.TABLE_ROWS], table.attrib[xmltags.TABLE_COLUMNS]),
        )
        header_row = self.find(xmltags.TABLE_HEADER_ROW, table)
        self.assertEqual("text", self.find(xmltags.TABLE_CELL, header_row).text)

    @patch(read_text, Mock(return_value="Replace $var$."))
    def test_variable(self):
        """Test that a variable is replaced with its value."""
        self.assertEqual("Replace variable.", self.find(xmltags.PARAGRAPH).text)

    @patch(read_text, Mock(return_value="Replace [anchor](https://$var$/).\n"))
    def test_variable_in_url(self):
        """Test that a variable in a URL is replaced with its value."""
        paragraph = self.find(xmltags.PARAGRAPH)
        anchor_link = self.find(xmltags.ANCHOR, paragraph).attrib[xmltags.ANCHOR_LINK]
        self.assertEqual("https://variable/", anchor_link)

    @patch(read_text, Mock(return_value="<!-- begin: measure -->\nMeasure\n<!-- end: measure -->\n"))
    def test_measure(self):
        """Test measure."""
        measure = self.find(xmltags.MEASURE)
        self.assertEqual("Measure", self.find(xmltags.PARAGRAPH, measure).text)

    @patch(read_text, Mock(return_value="<!-- begin: measure composite=true -->\nMeasure\n<!-- end: measure -->\n"))
    def test_measure_with_attribute(self):
        """Test measure with an attribute."""
        self.assertEqual("true", self.find(xmltags.MEASURE).attrib["composite"])

    @patch(read_text, Mock(side_effect=["#include 'file'", "included\n", "included\n"]))
    def test_include(self):
        """Test that Markdown files can be included."""
        self.assertEqual("included", self.find(xmltags.PARAGRAPH).text)
