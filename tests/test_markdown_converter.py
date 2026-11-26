"""Markdown converter unit tests."""

import unittest
from typing import cast
from unittest.mock import Mock, patch
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

    @patch(read_text, Mock(return_value="# Heading 1\n## Heading 2\n<!-- submeasures: 1, 3 -->\nText"))
    def test_submeasures(self):
        """Test that the section is marked as explanation of the submeasures."""
        section1 = self.find(xmltags.SECTION)
        self.assertNotIn(xmltags.SECTION_SUBMEASURES, section1.attrib)
        section2 = self.find(xmltags.SECTION, section1)
        self.assertEqual("1,3", section2.attrib[xmltags.SECTION_SUBMEASURES])
        self.assertEqual("Text", self.find(xmltags.PARAGRAPH, section2).text)

    @patch(
        read_text,
        Mock(
            return_value="**Bold** _Italic_ ~~Strike~~ {Instruction} [Anchor](link) `Code`"
            "[measure-title]Measure[/measure-title] [submeasure-title]Submeasure[/submeasure-title]"
        ),
    )
    def test_formatting(self):
        """Test formatting."""
        paragraph = self.find(xmltags.PARAGRAPH)
        self.assertEqual("Bold", self.find(xmltags.BOLD, paragraph).text)
        self.assertEqual("Code", self.find(xmltags.CODE, paragraph).text)
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

    @patch(read_text, Mock(return_value='![Anchor](image_(1).png "Figure 1 (cropped)")'))
    def test_image_with_brackets(self):
        """Test an image whose source and title contain brackets."""
        image = self.find(f".//{xmltags.IMAGE}")
        self.assertEqual("image_(1).png", image.attrib[xmltags.IMAGE_SRC])
        self.assertEqual("Figure 1 (cropped)", image.attrib[xmltags.IMAGE_TITLE])

    @patch(read_text, Mock(return_value='![Anchor](image (1).png "Figure 1")'))
    def test_image_with_whitespace_in_filename(self):
        """Test an image whose source path contains whitespace."""
        image = self.find(f".//{xmltags.IMAGE}")
        self.assertEqual("image (1).png", image.attrib[xmltags.IMAGE_SRC])
        self.assertEqual("Figure 1", image.attrib[xmltags.IMAGE_TITLE])

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

    @patch(read_text, Mock(return_value="```python\nprint('Hello world')\n```\n"))
    def test_code_blok(self):
        """Test that a code block can be included in the Markdown."""
        code_block = self.find(xmltags.CODE_BLOCK)
        self.assertEqual("print('Hello world')\n", code_block.text)

    @patch(read_text, Mock(return_value="```mermaid\nflowchart TD\n    A --> B\n```\nAfter\n"))
    def test_diagram(self):
        """Test that a Mermaid code block becomes a diagram with the Mermaid source."""
        self.assertEqual("flowchart TD\n    A --> B\n", self.find(xmltags.DIAGRAM).text)
        self.assertIsNone(self.xml().find(xmltags.CODE_BLOCK))
        self.assertEqual("After", self.find(xmltags.PARAGRAPH).text)

    @patch(read_text, Mock(return_value="See: [more info](https://more.info)\n"))
    def test_url(self):
        """Test a URL."""
        paragraph = self.find(xmltags.PARAGRAPH)
        anchor_link = self.find(xmltags.ANCHOR, paragraph).attrib[xmltags.ANCHOR_LINK]
        self.assertEqual("https://more.info", anchor_link)

    @patch(read_text, Mock(return_value="See: [more info](https://en.wikipedia.org/wiki/ZAP_(software))\n"))
    def test_url_with_brackets(self):
        """Test a URL with brackets."""
        paragraph = self.find(xmltags.PARAGRAPH)
        anchor_link = self.find(xmltags.ANCHOR, paragraph).attrib[xmltags.ANCHOR_LINK]
        self.assertEqual("https://en.wikipedia.org/wiki/ZAP_(software)", anchor_link)


@patch("markdown_converter.pathlib.Path.write_text", Mock())
class AdmonitionTest(MarkdownConverterTestCase):
    """Unit tests for admonitions in the Markdown converter."""

    def convert(self, markdown: str) -> Element:
        """Convert the Markdown and return the document element."""
        with patch("markdown_converter.pathlib.Path.read_text", Mock(return_value=markdown)):
            return cast(Element, self.xml().getroot())

    def admonition(self, markdown: str) -> Element:
        """Convert the Markdown and return the first admonition."""
        return cast(Element, self.convert(markdown).find(xmltags.ADMONITION))

    def test_admonition(self):
        """Test that an admonition has a type, a default title, and contents."""
        admonition = self.admonition("> [!NOTE]\n> Text\n")
        self.assertEqual({xmltags.ADMONITION_TYPE: "note", xmltags.ADMONITION_TITLE: "Opmerking"}, admonition.attrib)
        self.assertEqual("Text", self.find(xmltags.PARAGRAPH, admonition).text)

    def test_default_titles(self):
        """Test the default titles of the admonition types; the types are case-insensitive."""
        for marker, title in (
            ("NOTE", "Opmerking"),
            ("tip", "Tip"),
            ("Important", "Belangrijk"),
            ("WARNING", "Waarschuwing"),
            ("caution", "Let op"),
        ):
            with self.subTest(marker=marker):
                admonition = self.admonition(f"> [!{marker}]\n> Text\n")
                self.assertEqual(marker.lower(), admonition.attrib[xmltags.ADMONITION_TYPE])
                self.assertEqual(title, admonition.attrib[xmltags.ADMONITION_TITLE])

    def test_unknown_type(self):
        """Test that an unknown admonition type is not an admonition."""
        self.assertIsNone(self.admonition("> [!UNKNOWN]\n> Text\n"))

    def test_custom_title(self):
        """Test that a title after the marker replaces the default title and that variables are replaced."""
        admonition = self.admonition("> [!WARNING] Let op de $var$\n> Text\n")
        self.assertEqual("Let op de variable", admonition.attrib[xmltags.ADMONITION_TITLE])

    def test_formatted_text(self):
        """Test that the contents of the admonition are processed as Markdown."""
        paragraph = self.find(xmltags.PARAGRAPH, self.admonition("> [!TIP]\n> **Bold** [link](https://link) $var$\n"))
        self.assertEqual("Bold", self.find(xmltags.BOLD, paragraph).text)
        self.assertEqual("https://link", self.find(xmltags.ANCHOR, paragraph).attrib[xmltags.ANCHOR_LINK])
        self.assertEqual(" variable", self.find(xmltags.ANCHOR, paragraph).tail)

    def test_paragraphs(self):
        """Test that a line with only the quote marker separates paragraphs."""
        admonition = self.admonition("> [!NOTE]\n> Paragraph 1\n>\n> Paragraph 2\n")
        self.assertEqual(["Paragraph 1", "Paragraph 2"], [p.text for p in admonition.findall(xmltags.PARAGRAPH)])

    def test_nested_list(self):
        """Test that an admonition can contain a nested list."""
        admonition = self.admonition("> [!NOTE]\n> * Item\n> + Nested item\n")
        bullet_list = self.find(xmltags.BULLET_LIST, admonition)
        self.assertEqual("Item", self.find(xmltags.LIST_ITEM, bullet_list).text)
        self.assertEqual("Nested item", self.find(f"{xmltags.BULLET_LIST}/{xmltags.LIST_ITEM}", bullet_list).text)

    def test_table(self):
        """Test that an admonition can contain a table that ends with the admonition."""
        document = self.convert("> [!NOTE]\n> |col|\n> |---|\n> |cell|\nAfter\n")
        admonition = self.find(xmltags.ADMONITION, document)
        self.assertEqual(
            "cell", self.find(f"{xmltags.TABLE_ROW}/{xmltags.TABLE_CELL}", self.find(xmltags.TABLE, admonition)).text
        )
        self.assertEqual("After", self.find(xmltags.PARAGRAPH, document).text)

    def test_code_block(self):
        """Test that an admonition can contain a code block, even if it is not closed."""
        admonition = self.admonition("> [!NOTE]\n> ```python\n> print('Hello world')\n")
        self.assertEqual("print('Hello world')\n", self.find(xmltags.CODE_BLOCK, admonition).text)

    def test_diagram(self):
        """Test that an admonition can contain a diagram, even if it is not closed."""
        admonition = self.admonition("> [!NOTE]\n> ```mermaid\n> flowchart TD\n")
        self.assertEqual("flowchart TD\n", self.find(xmltags.DIAGRAM, admonition).text)

    def test_marker_in_code_block(self):
        """Test that a marker in a code block is not an admonition."""
        document = self.convert("```markdown\n> [!NOTE]\n```\n")
        self.assertIsNone(document.find(xmltags.ADMONITION))
        self.assertEqual("> [!NOTE]\n", self.find(xmltags.CODE_BLOCK, document).text)

    def test_end_at_line_without_quote_marker(self):
        """Test that the admonition ends at the first line that does not start with the quote marker."""
        document = self.convert("> [!NOTE]\n> * Item\nAfter\n")
        self.assertEqual("After", self.find(xmltags.PARAGRAPH, document).text)
        self.assertIsNone(self.find(xmltags.ADMONITION, document).find(xmltags.PARAGRAPH))

    def test_end_at_empty_line(self):
        """Test that the admonition ends at an empty line."""
        document = self.convert("> [!NOTE]\n> Inside\n\nAfter\n")
        self.assertEqual("After", self.find(xmltags.PARAGRAPH, document).text)

    def test_end_of_document(self):
        """Test that an admonition with a list at the end of the document is closed."""
        admonition = self.admonition("> [!NOTE]\n> 1. Item")
        self.assertEqual("Item", self.find(f"{xmltags.NUMBERED_LIST}/{xmltags.LIST_ITEM}", admonition).text)

    def test_consecutive_admonitions(self):
        """Test that a marker ends the previous admonition and any list before it."""
        document = self.convert("* Item\n> [!NOTE]\n> * Note\n> [!TIP]\n> Tip\n")
        self.assertEqual(
            ["note", "tip"], [a.attrib[xmltags.ADMONITION_TYPE] for a in document.iter(xmltags.ADMONITION)]
        )
        self.assertIsNone(self.find(xmltags.BULLET_LIST, document).find(xmltags.ADMONITION))

    def test_quote_without_marker(self):
        """Test that a quote without a marker is not an admonition."""
        document = self.convert("> Quote\n")
        self.assertIsNone(document.find(xmltags.ADMONITION))
        self.assertEqual("> Quote", self.find(xmltags.PARAGRAPH, document).text)

    def test_heading(self):
        """Test that headings are not allowed in admonitions."""
        self.assertRaises(ValueError, self.convert, "> [!NOTE]\n> # Heading\n")


@patch("markdown_converter.pathlib.Path.write_text", Mock())
class LandscapeTest(MarkdownConverterTestCase):
    """Unit tests for landscape blocks in the Markdown converter."""

    def convert(self, markdown: str) -> Element:
        """Convert the Markdown and return the document element."""
        with patch("markdown_converter.pathlib.Path.read_text", Mock(return_value=markdown)):
            return cast(Element, self.xml().getroot())

    def orientations(self, document: Element) -> list[str]:
        """Return the page orientations in the document."""
        return [element.attrib[xmltags.PAGE_ORIENTATION_VALUE] for element in document.iter(xmltags.PAGE_ORIENTATION)]

    def test_landscape(self):
        """Test that a landscape block switches to landscape at the start and back to portrait at the end."""
        document = self.convert("<!-- begin: landscape -->\n# Heading 1\nText\n# Heading 2\n<!-- end: landscape -->\n")
        self.assertEqual(
            [xmltags.PAGE_ORIENTATION_LANDSCAPE, xmltags.PAGE_ORIENTATION_PORTRAIT], self.orientations(document)
        )
        self.assertEqual(2, len(list(document.iter(xmltags.SECTION))))

    def test_table(self):
        """Test that the end of a landscape block ends a table."""
        document = self.convert("<!-- begin: landscape -->\n| A |\n|:--|\n| a |\n<!-- end: landscape -->\n")
        self.assertIsNone(self.find(xmltags.TABLE, document).find(f".//{xmltags.PAGE_ORIENTATION}"))
        self.assertEqual(2, len(self.orientations(document)))

    def test_nested(self):
        """Test that landscape blocks can't be nested."""
        self.assertRaises(ValueError, self.convert, "<!-- begin: landscape -->\n<!-- begin: landscape -->\n")

    def test_end_without_begin(self):
        """Test that a landscape block can't end without beginning."""
        self.assertRaises(ValueError, self.convert, "<!-- end: landscape -->\n")

    def test_admonition(self):
        """Test that landscape blocks are not allowed in admonitions."""
        self.assertRaises(ValueError, self.convert, "> [!NOTE]\n> <!-- begin: landscape -->\n")


@patch("markdown_converter.pathlib.Path.write_text", Mock())
class AbbreviationsTest(MarkdownConverterTestCase):
    """Unit tests for collecting the abbreviations in the Markdown converter."""

    def abbreviations(self, markdown: str) -> dict[str, str]:
        """Convert the Markdown and return the collected abbreviations."""
        converter = MarkdownConverter(Variables({"var": "variable"}))
        with patch("markdown_converter.pathlib.Path.read_text", Mock(return_value=markdown)):
            converter.convert(self.settings, "html")
        return converter.abbreviations

    def test_no_abbreviations_table(self):
        """Test that there are no abbreviations if the Markdown has no abbreviations table."""
        markdown = "| Term | Toelichting |\n|:-|:-|\n| **IPO** | intern projectoverleg |\n"
        self.assertEqual({}, self.abbreviations(markdown))

    def test_abbreviations_table(self):
        """Test that the abbreviations and their meanings are collected from the abbreviations table."""
        markdown = (
            "| Afkorting | Betekenis | Toelichting |\n"
            "|:----------|:----------|:------------|\n"
            "| **IPO** | intern projectoverleg | |\n"
            "| **IB-plan** | informatiebeveiligingsplan | Een plan |\n"
        )
        self.assertEqual(
            {"IPO": "intern projectoverleg", "IB-plan": "informatiebeveiligingsplan"}, self.abbreviations(markdown)
        )

    def test_formatting_is_removed(self):
        """Test that formatting is removed from the abbreviations and their meanings."""
        markdown = "| Afkorting | Betekenis |\n|:-|:-|\n| **ART** | automatische **regressietest** |\n"
        self.assertEqual({"ART": "automatische regressietest"}, self.abbreviations(markdown))

    def test_variables_are_replaced(self):
        """Test that variables in the meanings are replaced by their values."""
        markdown = "| Afkorting | Betekenis |\n|:-|:-|\n| **VAR** | $var$ |\n"
        self.assertEqual({"VAR": "variable"}, self.abbreviations(markdown))

    def test_other_tables_are_ignored(self):
        """Test that tables other than the abbreviations table are ignored."""
        markdown = (
            "| Afkorting | Betekenis |\n|:-|:-|\n| **IPO** | intern projectoverleg |\n\n"
            "| Term | Toelichting |\n|:-|:-|\n| **actor** | een persoon |\n"
        )
        self.assertEqual({"IPO": "intern projectoverleg"}, self.abbreviations(markdown))


@patch("markdown_converter.pathlib.Path.write_text", Mock())
class AbbreviationMarkingTest(MarkdownConverterTestCase):
    """Unit tests for marking the abbreviations in the Markdown converter."""

    ABBREVIATIONS_TABLE = (
        "| Afkorting | Betekenis |\n|:-|:-|\n"
        "| **API** | application programming interface |\n"
        "| **IB-plan** | informatiebeveiligingsplan |\n"
        "| **ISO** | International Organization for Standardization |\n"
        "| **VIR** | Voorschrift Informatiebeveiliging Rijksdienst |\n"
        "| **VIRBI** | Voorschrift Informatiebeveiliging Rijksdienst Bijzondere Informatie |\n"
    )

    def convert(self, markdown: str, abbreviations_table: str = ABBREVIATIONS_TABLE) -> Element:
        """Convert the Markdown, followed by the abbreviations table, and return the first content element."""
        with patch(
            "markdown_converter.pathlib.Path.read_text", Mock(return_value=f"{markdown}\n\n{abbreviations_table}")
        ):
            return cast(Element, self.xml().getroot())[2]  # Skip the header and footer

    def abbreviations(self, markdown: str, abbreviations_table: str = ABBREVIATIONS_TABLE) -> list[str]:
        """Convert the Markdown and return the marked abbreviations in the first element."""
        return [
            element.text or "" for element in self.convert(markdown, abbreviations_table).iter(xmltags.ABBREVIATION)
        ]

    def test_abbreviation(self):
        """Test that an abbreviation is marked, with its meaning as title."""
        paragraph = self.convert("De API is gedocumenteerd.")
        self.assertEqual("De ", paragraph.text)
        abbreviation = self.find(xmltags.ABBREVIATION, paragraph)
        self.assertEqual("API", abbreviation.text)
        self.assertEqual("application programming interface", abbreviation.attrib[xmltags.ABBREVIATION_TITLE])
        self.assertEqual(" is gedocumenteerd.", abbreviation.tail)

    def test_every_occurrence(self):
        """Test that every occurrence of an abbreviation is marked."""
        self.assertEqual(["API", "API"], self.abbreviations("API en nog eens API"))

    def test_whole_words(self):
        """Test that only whole words are marked."""
        self.assertEqual([], self.abbreviations("APIs, XAPI, API2, api"))

    def test_compounds(self):
        """Test that abbreviations are marked at the start of a compound, but not at the end."""
        self.assertEqual(["API", "IB-plan"], self.abbreviations("API-server, NEN-ISO/IEC, IB-plan"))

    def test_longest_abbreviation(self):
        """Test that the longest abbreviation is marked if abbreviations overlap."""
        self.assertEqual(["VIRBI", "VIR"], self.abbreviations("VIRBI en VIR"))

    def test_formatted_text(self):
        """Test that abbreviations in formatted text and instructions are marked."""
        self.assertEqual(["API", "ISO"], self.abbreviations("**API** en {ISO}"))

    def test_variables(self):
        """Test that abbreviations in variable values are marked."""
        abbreviations_table = self.ABBREVIATIONS_TABLE + "| **variable** | een waarde |\n"
        self.assertEqual(["variable"], self.abbreviations("Een $var$", abbreviations_table))

    def test_list_items_and_table_cells(self):
        """Test that abbreviations in list items and table cells are marked."""
        self.assertEqual(["API"], self.abbreviations("* De API"))
        self.assertEqual(["API", "ISO"], self.abbreviations("| API |\n|:-|\n| ISO |"))

    def test_not_in_headings(self):
        """Test that abbreviations in headings are not marked."""
        heading = self.find(xmltags.HEADING, self.convert("# De API"))
        self.assertEqual("De API", heading.text)
        self.assertEqual([], list(heading))

    def test_not_in_code(self):
        """Test that abbreviations in code and code blocks are not marked."""
        self.assertEqual([], self.abbreviations("De `API`"))
        self.assertEqual([], self.abbreviations("```python\napi = 'API'\n```"))

    def test_not_in_links(self):
        """Test that abbreviations in link texts are not marked."""
        self.assertEqual([], self.abbreviations("De [API](https://example.org)"))

    def test_not_in_measure_titles(self):
        """Test that abbreviations in measure and submeasure titles are not marked."""
        self.assertEqual([], self.abbreviations("**[measure-title]M01: De API[/measure-title]**"))
        self.assertEqual([], self.abbreviations("[submeasure-title]De API[/submeasure-title]"))

    def test_no_abbreviations_table(self):
        """Test that nothing is marked if the document has no abbreviations table."""
        self.assertEqual([], self.abbreviations("De API", abbreviations_table=""))

    def test_definitions(self):
        """Test that the abbreviations in the first column of the abbreviations table are marked as definitions."""
        with patch(
            "markdown_converter.pathlib.Path.read_text", Mock(return_value=f"De API\n\n{self.ABBREVIATIONS_TABLE}")
        ):
            root = cast(Element, self.xml().getroot())
        abbreviations = list(root.iter(xmltags.ABBREVIATION))
        self.assertNotIn(xmltags.ABBREVIATION_IS_DEFINITION, abbreviations[0].attrib)
        for abbreviation in abbreviations[1:]:
            self.assertEqual("y", abbreviation.attrib[xmltags.ABBREVIATION_IS_DEFINITION])

    def test_no_definitions_in_other_columns(self):
        """Test that abbreviations in the other columns of the abbreviations table are not marked as definitions."""
        abbreviations_table = self.ABBREVIATIONS_TABLE + "| **IPO** | intern projectoverleg, zie API |\n"
        with patch("markdown_converter.pathlib.Path.read_text", Mock(return_value=abbreviations_table)):
            root = cast(Element, self.xml().getroot())
        abbreviation = list(root.iter(xmltags.ABBREVIATION))[-1]
        self.assertEqual("API", abbreviation.text)
        self.assertNotIn(xmltags.ABBREVIATION_IS_DEFINITION, abbreviation.attrib)
