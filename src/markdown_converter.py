"""Markdown converter."""

import contextlib
import pathlib
import re
from typing import cast, List, Optional, Set
from xml.etree.ElementTree import ElementTree, TreeBuilder

import markdown_syntax
import xmltags
from custom_types import Settings, TreeBuilderAttributes, Variables
from markdown_table import Table


class MarkdownConverter:
    """Convert Markdown to XML."""

    APPENDIX_HEADING = "Bijlagen"
    APPENDIX_LEVEL = 1

    def __init__(self, variables: Variables) -> None:
        self.builder = TreeBuilder()
        self.context: Set[str] = set()  # Current context, e.g. are we in a measure, or in the appendices
        self.current_section_level = 0
        self.current_list_tags: List[str] = []
        self.list_counter: List[int] = []  # List item counters per list level
        self.table: Optional[Table] = None
        self.variables = variables

    def convert(self, settings: Settings) -> ElementTree:
        """Convert the markdown to XML."""
        self._start_document(settings)
        self._convert_markdown_file(pathlib.Path(settings["InputFile"]), settings)
        self._end_document()
        return ElementTree(self.builder.close())

    def _convert_markdown_file(self, markdown_filename: pathlib.Path, settings: Settings) -> None:
        """Convert markdown file to XML."""
        with open(markdown_filename, encoding="utf-8") as markdown_file:
            for line in markdown_file.readlines():
                if line.startswith("#include"):
                    filename = line.split(" ", maxsplit=1)[1].strip().strip('"')
                    filename = filename.replace(
                        "{{DOCUMENT-FOLDER}}",
                        settings.get("DocumentFolder", "DocumentFolder missing in settings"),
                    )
                    self._convert_markdown_file(pathlib.Path(filename), settings)
                else:
                    self._process_line(line)

    def _start_document(self, settings: Settings) -> None:
        """Start the document."""
        document_attributes: TreeBuilderAttributes = {}
        for setting, tag in (
            ("Title", xmltags.DOCUMENT_TITLE),
            ("Version", xmltags.DOCUMENT_VERSION),
        ):
            document_attributes[tag] = str(settings[setting])
        self.builder.start(xmltags.DOCUMENT, document_attributes)
        self._create_frontpage(settings)
        self._create_header(settings)
        self._create_footer()
        if settings["IncludeTableOfContents"]:
            self._create_table_of_contents()

    def _create_frontpage(self, settings: Settings) -> None:
        """Create a front page."""
        if not settings.get("FrontPage"):
            return
        document_type = settings["DocumentType"]
        with self.element(xmltags.FRONTPAGE):
            if settings["FrontPage"] == "ICTU":
                self._add_element(
                    xmltags.IMAGE,
                    attributes={
                        xmltags.IMAGE_SRC: "ICTU.png",
                        xmltags.IMAGE_TITLE: "ICTU logo",
                        xmltags.IMAGE_WIDTH: "5",
                    },
                )
            with self.element(xmltags.TITLE):
                self._process_formatted_text(settings["Title"])
            if document_type == "Template":
                with self.element(xmltags.PARAGRAPH):
                    with self.element(xmltags.INSTRUCTION):
                        self._add_element(xmltags.BOLD, settings["Subtitle"])
                self._add_element(xmltags.PARAGRAPH)
                with self.element(xmltags.PARAGRAPH):
                    self._process_formatted_text("Rubriceringsniveau {Rubriceringsniveau}")
                with self.element(xmltags.PARAGRAPH):
                    self.builder.data("Versie ")
                    self._add_element(xmltags.INSTRUCTION, "{Versienummer}")
                    self.builder.data(", ")
                    self._add_element(xmltags.INSTRUCTION, "{Datum}")
                self._add_element(xmltags.PARAGRAPH)
            elif document_type == "Kwaliteitsaanpak":
                if settings.get("Subtitle"):
                    with self.element(xmltags.PARAGRAPH):
                        self._add_element(xmltags.BOLD, settings["Subtitle"])
                with self.element(xmltags.PARAGRAPH):
                    self.builder.data(f"Versie {settings['Version']}, {settings['Date']}")
            else:
                raise ValueError(f"Unknown document type '{document_type}' in the settings")
            if settings["FrontPage"] == "ICTU":
                self._add_element(
                    xmltags.IMAGE,
                    attributes={
                        xmltags.IMAGE_SRC: "word-cloud.png",
                        xmltags.IMAGE_TITLE: (
                            "Word cloud met woorden die veel voorkomen in het document zoals "
                            "Kwaliteitsaanpak, Realisatie, ICTU, Software en Overheid"
                        ),
                        xmltags.IMAGE_WIDTH: "15",
                    },
                )
            self._add_element(xmltags.PAGEBREAK)

    def _create_header(self, settings: Settings) -> None:
        """Create the page header."""
        title = settings["Title"]
        with self.element(xmltags.HEADER):
            if settings["DocumentType"] == "Template":
                self._process_formatted_text(f"{title} ")
                self._add_element(xmltags.INSTRUCTION, settings["Subtitle"])
            else:
                self.builder.data(title)

    def _create_footer(self) -> None:
        """Create the page footer."""
        self._add_element(xmltags.FOOTER)

    def _create_table_of_contents(self) -> None:
        """Create the table of contents placeholder. Actually creating a table of contents is the responsibility of the
        target format (e.g. docx)."""
        self._add_element(
            xmltags.TABLE_OF_CONTENTS,
            attributes={xmltags.TABLE_OF_CONTENTS_HEADING: "Inhoudsopgave"},
        )
        self._add_element(xmltags.PAGEBREAK)

    def _process_line(self, line: str) -> None:
        """Process a line of Markdown."""
        if not (stripped_line := line.strip()):
            self._end_lists()
            self._end_table()
            return  # Empty line, nothing further to do
        stripped_line = self._process_variables(stripped_line)
        if match := re.match(markdown_syntax.BEGIN_PATTERN, stripped_line):
            attributes: dict[bytes | str, bytes | str] = {}
            if attribute := match.group(2):
                key, value = attribute.split("=")
                attributes[key] = value
            self.builder.start(match.group(1), attributes)
        elif match := re.match(markdown_syntax.END_PATTERN, stripped_line):
            self.builder.end(match.group(1))
        elif match := re.match(markdown_syntax.HEADING_PATTERN, stripped_line):
            self._process_heading(heading=match.group(2), level=len(match.group(1)))
        elif re.match(markdown_syntax.BULLET_LIST_PATTERN, stripped_line):
            list_level = {"*": 1, "+": 2, "-": 3}[stripped_line[0]]
            self._process_list(stripped_line, xmltags.BULLET_LIST, list_level)
        elif re.match(markdown_syntax.NUMBERED_LIST_PATTERN, stripped_line):
            list_level = 1 if line[0].isdigit() else (3 if stripped_line[0].isdigit() else 2)
            self._process_list(stripped_line, xmltags.NUMBERED_LIST, list_level)
        elif stripped_line[0] == markdown_syntax.TABLE_MARKER:
            self._process_table_row(stripped_line)
        else:
            with self.element(xmltags.PARAGRAPH):
                self._process_formatted_text(stripped_line)

    def _process_variables(self, line: str) -> str:
        """Replace the variables with their values."""
        return re.sub(
            markdown_syntax.VARIABLE_USE_PATTERN,
            lambda variable: self.variables[variable.group(1)],
            line,
        )

    def _process_heading(self, heading: str, level: int) -> None:
        """Process a heading."""
        if level == self.APPENDIX_LEVEL and heading == self.APPENDIX_HEADING:
            self.context.add(self.APPENDIX_HEADING)
        is_appendix: TreeBuilderAttributes = (
            {xmltags.SECTION_IS_APPENDIX: "y"} if self.APPENDIX_HEADING in self.context else {}
        )
        if self.current_section_level >= level:
            while self.current_section_level >= level:
                self.builder.end(xmltags.SECTION)
                self.current_section_level -= 1
        elif self.current_section_level < level - 1:
            while self.current_section_level < level - 1:
                self.current_section_level += 1
                attributes: TreeBuilderAttributes = {
                    xmltags.SECTION_LEVEL: str(self.current_section_level),
                    **is_appendix,
                }
                self.builder.start(xmltags.SECTION, attributes)
        self.current_section_level = level
        self.builder.start(
            xmltags.SECTION,
            {**is_appendix, xmltags.SECTION_LEVEL: str(self.current_section_level)},
        )
        with self.element(xmltags.HEADING):
            self._process_formatted_text(heading)

    def _end_sections(self):
        """Close all sections."""
        while self.current_section_level > 0:
            self.builder.end(xmltags.SECTION)
            self.current_section_level -= 1

    def _process_list(self, line: str, tag: str, list_level: int) -> None:
        """Process a bullet or numbered list."""
        self._start_lists(tag, list_level)
        self._end_lists(list_level)
        self.list_counter[list_level - 1] += 1
        number = str(self.list_counter[list_level - 1])
        attributes: TreeBuilderAttributes = {xmltags.LIST_ITEM_NUMBER: number} if tag == xmltags.NUMBERED_LIST else {}
        with self.element(xmltags.LIST_ITEM, attributes):
            self._process_formatted_text(line.split(" ", maxsplit=1)[1])

    def _start_lists(self, tag: str, level: int) -> None:
        """Start (possibly nested) lists until the required level is reached."""
        while len(self.current_list_tags) < level:
            self.current_list_tags.append(tag)
            self.list_counter.append(0)
            self.builder.start(tag, {xmltags.LIST_LEVEL: str(len(self.current_list_tags))})

    def _end_lists(self, level: int = 0) -> None:
        """End (possibly nested) lists until the required level is reached."""
        while len(self.current_list_tags) > level:
            self.list_counter.pop()
            self.builder.end(self.current_list_tags.pop())

    def _process_table_row(self, line: str) -> None:
        """Process table row."""
        cells = Table.get_table_cells(line)
        if self.table is None:
            self.table = Table(cells)
        else:
            self.table.process_table_cells(cells)

    def _end_table(self) -> None:
        """Flush the table."""

        def table_row(tag: str, cells, row_index: int) -> None:
            assert self.table is not None
            with self.element(tag):
                for column_index, (cell, alignment, width) in enumerate(
                    zip(cells, self.table.column_alignment, self.table.column_widths)
                ):
                    attributes: TreeBuilderAttributes = {
                        xmltags.TABLE_CELL_ALIGNMENT: alignment,
                        xmltags.TABLE_CELL_COLUMN: str(column_index),
                        xmltags.TABLE_CELL_ROW: str(row_index),
                        xmltags.TABLE_CELL_WIDTH: str(width),
                    }
                    with self.element(xmltags.TABLE_CELL, attributes):
                        self._process_formatted_text(cell)

        if self.table is None:
            return
        table_attributes: TreeBuilderAttributes = {
            xmltags.TABLE_COLUMNS: str(len(self.table.header_cells)),
            xmltags.TABLE_ROWS: str(len(self.table.rows)),
        }
        with self.element(xmltags.TABLE, table_attributes):
            table_row(xmltags.TABLE_HEADER_ROW, self.table.header_cells, 0)
            for row_index, row in enumerate(self.table.rows):
                table_row(xmltags.TABLE_ROW, row, row_index + 1)
        self.table = None

    def _process_formatted_text(self, line: str) -> None:
        """Process formatted Markdown text."""
        seen = ""
        formats = [
            (markdown_syntax.BOLD_START, markdown_syntax.BOLD_END, xmltags.BOLD),
            (
                markdown_syntax.BOLD_ALTERNATIVE_START,
                markdown_syntax.BOLD_ALTERNATIVE_END,
                xmltags.BOLD,
            ),
            (
                markdown_syntax.INSTRUCTION_START,
                markdown_syntax.INSTRUCTION_END,
                xmltags.INSTRUCTION,
            ),
            (markdown_syntax.ITALIC_START, markdown_syntax.ITALIC_END, xmltags.ITALIC),
            (
                markdown_syntax.ITALIC_ALTERNATIVE_START,
                markdown_syntax.ITALIC_ALTERNATIVE_END,
                xmltags.ITALIC,
            ),
            (
                markdown_syntax.STRIKETROUGH_START,
                markdown_syntax.STRIKETROUGH_END,
                xmltags.STRIKETHROUGH,
            ),
        ]
        while line:
            format_found = False
            for md_start, md_end, xml_tag in formats:
                if line.startswith(md_start) and md_end in line[len(md_start) :]:
                    format_found = True
                    self._flush(seen)
                    seen = ""
                    with self.element(xml_tag):
                        if xml_tag == xmltags.INSTRUCTION:
                            self.builder.data(md_start)
                        formatted_text, line = line[len(md_start) :].split(md_end, maxsplit=1)
                        self._process_formatted_text(formatted_text)
                        if xml_tag == xmltags.INSTRUCTION:
                            self.builder.data(md_end)
                    break
            else:
                if match := re.match(markdown_syntax.LINK_PATTERN, line):
                    format_found = True
                    self._flush(seen)
                    seen = ""
                    match = cast(re.Match, match)
                    with self.element(xmltags.ANCHOR, {xmltags.ANCHOR_LINK: match.group(2)}):
                        self._process_formatted_text(match.group(1))
                    line = line[len(match.group(0)) :]
                elif match := re.match(markdown_syntax.IMAGE_PATTERN, line):
                    format_found = True
                    self._flush(seen)
                    seen = ""
                    match = cast(re.Match, match)
                    self._add_element(
                        xmltags.IMAGE,
                        attributes={
                            xmltags.IMAGE_ALT: match.group(1),
                            xmltags.IMAGE_SRC: match.group(2),
                            xmltags.IMAGE_TITLE: match.group(3),
                            xmltags.IMAGE_WIDTH: "15",
                        },
                    )
                    line = line[len(match.group(0)) :]

            if not format_found:
                seen += line[0] if line else ""
                line = line[1:]
        self._flush(seen)

    def _end_document(self) -> None:
        """End the document."""
        self._end_lists()
        self._end_table()
        self._end_sections()
        self.builder.end(xmltags.DOCUMENT)

    def _add_element(self, tag: str, text: str = "", attributes: TreeBuilderAttributes | None = None) -> None:
        """Add an element with text."""
        with self.element(tag, attributes):
            self._flush(text)

    @contextlib.contextmanager
    def element(self, tag: str, attributes: TreeBuilderAttributes | None = None):
        """Return a context manager."""
        element = self.builder.start(tag, attributes or {})
        try:
            yield element
        finally:
            self.builder.end(tag)

    def _flush(self, text: str) -> None:
        """Flush the text."""
        if text:
            self.builder.data(text)
