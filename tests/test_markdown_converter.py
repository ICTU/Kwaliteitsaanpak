"""Markdown converter unit tests."""

import unittest
from unittest.mock import patch, mock_open
from xml.etree.ElementTree import ElementTree

import xmltags
from custom_types import Settings, Variables
from markdown_converter import MarkdownConverter


class MarkdownConverterTestCase(unittest.TestCase):
    """Base class for Markdown converter tests."""

    def setUp(self):
        self.settings = Settings(
            {
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


@patch("markdown_converter.open", mock_open(read_data=""))
class EmptyMarkdownTest(MarkdownConverterTestCase):
    """Unit test for the Markdown converter with empty Markdown."""

    def test_title(self):
        """Test the document title."""
        self.assertEqual(self.settings["Title"], self.xml().getroot().attrib[xmltags.DOCUMENT_TITLE])

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
        self.assertEqual(
            self.settings["Title"],
            self.xml().find(xmltags.FRONTPAGE).find(xmltags.TITLE).text,
        )

    def test_toc(self):
        """Test the table of contents."""
        self.settings["OutputFormats"]["html"]["IncludeTableOfContents"] = True
        self.assertIsNotNone(self.xml().find(xmltags.TABLE_OF_CONTENTS))


class MarkdownTest(MarkdownConverterTestCase):
    """Unit test for the Markdown converter."""

    @patch("markdown_converter.open", mock_open(read_data="# Heading 1\n## Heading 2"))
    def test_headings(self):
        """Test nested headings."""
        section1 = self.xml().find(xmltags.SECTION)
        self.assertEqual("1", section1.attrib[xmltags.SECTION_LEVEL])
        self.assertEqual("Heading 1", section1.find(xmltags.HEADING).text)
        section2 = section1.find(xmltags.SECTION)
        self.assertEqual("2", section2.attrib[xmltags.SECTION_LEVEL])
        self.assertEqual("Heading 2", section2.find(xmltags.HEADING).text)

    @patch("markdown_converter.open", mock_open(read_data="# Bijlagen\n## Appendix"))
    def test_appendix_headings(self):
        """Test appendix headings."""
        appendices = self.xml().find(xmltags.SECTION)
        self.assertEqual("Bijlagen", appendices.find(xmltags.HEADING).text)
        self.assertEqual("1", appendices.attrib[xmltags.SECTION_LEVEL])
        self.assertEqual("y", appendices.attrib[xmltags.SECTION_IS_APPENDIX])
        appendix = appendices.find(xmltags.SECTION)
        self.assertEqual("Appendix", appendix.find(xmltags.HEADING).text)

    @patch("markdown_converter.open", mock_open(read_data="## Heading 2"))
    def test_open_implicit_sections(self):
        """Test start with a nested heading."""
        section1 = self.xml().find(xmltags.SECTION)
        self.assertEqual("1", section1.attrib[xmltags.SECTION_LEVEL])
        section2 = section1.find(xmltags.SECTION)
        self.assertEqual("2", section2.attrib[xmltags.SECTION_LEVEL])
        self.assertEqual("Heading 2", section2.find(xmltags.HEADING).text)

    @patch("markdown_converter.open", mock_open(read_data="## Heading 2\n# Heading 1"))
    def test_close_implicit_sections(self):
        """Test that a nested heading is closed properly."""
        section2 = self.xml().findall(xmltags.SECTION)[1]
        self.assertEqual("Heading 1", section2.find(xmltags.HEADING).text)

    @patch(
        "markdown_converter.open",
        mock_open(
            read_data="**Bold** _Italic_ ~~Strike~~ {Instruction} [Anchor](link) "
            "[measure-title]Measure[/measure-title] [submeasure-title]Submeasure[/submeasure-title]"
        ),
    )
    def test_formatting(self):
        """Test formatting."""
        paragraph = self.xml().find(xmltags.PARAGRAPH)
        self.assertEqual("Bold", paragraph.find(xmltags.BOLD).text)
        self.assertEqual("Italic", paragraph.find(xmltags.ITALIC).text)
        self.assertEqual("Strike", paragraph.find(xmltags.STRIKETHROUGH).text)
        self.assertEqual("{Instruction}", paragraph.find(xmltags.INSTRUCTION).text)
        self.assertEqual("Anchor", paragraph.find(xmltags.ANCHOR).text)
        self.assertEqual("link", paragraph.find(xmltags.ANCHOR).attrib[xmltags.ANCHOR_LINK])
        self.assertEqual("Measure", paragraph.find(xmltags.MEASURE_TITLE).text)
        self.assertEqual("Submeasure", paragraph.find(xmltags.SUBMEASURE_TITLE).text)
        self.assertEqual("1", paragraph.find(xmltags.SUBMEASURE_TITLE).attrib[xmltags.SUBMEASURE_TITLE_NUMBER])

    @patch("markdown_converter.open", mock_open(read_data='![Anchor](image.png "description")'))
    def test_image(self):
        """Test image."""
        image = self.xml().find(f".//{xmltags.IMAGE}")
        self.assertEqual("image.png", image.attrib[xmltags.IMAGE_SRC])
        self.assertEqual("description", image.attrib[xmltags.IMAGE_TITLE])

    @patch("markdown_converter.open", mock_open(read_data="* Bullet\n* list\n\n"))
    def test_bullet_list(self):
        """Test bullet list."""
        bullet_list = self.xml().find(xmltags.BULLET_LIST)
        self.assertEqual("Bullet", bullet_list.find(xmltags.LIST_ITEM).text)

    @patch("markdown_converter.open", mock_open(read_data="1. Numbered\n2. list\n\n"))
    def test_numbered_list(self):
        """Test bullet list."""
        numbered_list = self.xml().find(xmltags.NUMBERED_LIST)
        self.assertEqual("Numbered", numbered_list.find(xmltags.LIST_ITEM).text)
        self.assertEqual("1", numbered_list.find(xmltags.LIST_ITEM).attrib[xmltags.LIST_ITEM_NUMBER])

    @patch(
        "markdown_converter.open",
        mock_open(read_data="|col1|col2|col3|\n|:---:||:---|---:|\n|cell1|cell2|cell3|\n\n"),
    )
    def test_table(self):
        """Test table."""
        table = self.xml().find(xmltags.TABLE)
        self.assertEqual(
            ("1", "3"),
            (table.attrib[xmltags.TABLE_ROWS], table.attrib[xmltags.TABLE_COLUMNS]),
        )
        self.assertEqual("col1", table.find(xmltags.TABLE_HEADER_ROW).find(xmltags.TABLE_CELL).text)
        cell = table.find(xmltags.TABLE_ROW).find(xmltags.TABLE_CELL)
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

    @patch("markdown_converter.open", mock_open(read_data="|text\n\n"))
    def test_table_marker_without_columns(self):
        """Test an incomplete table."""
        table = self.xml().find(xmltags.TABLE)
        self.assertEqual(
            ("0", "1"),
            (table.attrib[xmltags.TABLE_ROWS], table.attrib[xmltags.TABLE_COLUMNS]),
        )
        self.assertEqual("text", table.find(xmltags.TABLE_HEADER_ROW).find(xmltags.TABLE_CELL).text)

    @patch("markdown_converter.open", mock_open(read_data="Replace $var$."))
    def test_variable(self):
        """Test that a variable is replaced with its value."""
        self.assertEqual("Replace variable.", self.xml().find(xmltags.PARAGRAPH).text)

    @patch(
        "markdown_converter.open",
        mock_open(read_data="Replace [anchor](https://$var$/).\n"),
    )
    def test_variable_in_url(self):
        """Test that a variable in a URL is replaced with its value."""
        anchor_link = self.xml().find(xmltags.PARAGRAPH).find(xmltags.ANCHOR).attrib[xmltags.ANCHOR_LINK]
        self.assertEqual("https://variable/", anchor_link)

    @patch(
        "markdown_converter.open",
        mock_open(read_data="<!-- begin: measure -->\nMeasure\n<!-- end: measure -->\n"),
    )
    def test_measure(self):
        """Test measure."""
        self.assertEqual("Measure", self.xml().find(xmltags.MEASURE).find(xmltags.PARAGRAPH).text)

    @patch("markdown_converter.open", new_callable=mock_open, read_data="#include 'file'")
    def test_include(self, mocked_open):
        """Test that Markdown files can be included."""
        mocked_open.side_effect = (
            mocked_open.return_value,
            mock_open(read_data="included\n").return_value,
        )
        self.assertEqual("included", self.xml().find(xmltags.PARAGRAPH).text)
