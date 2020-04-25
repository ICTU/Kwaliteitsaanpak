"""Markdown converter."""

import contextlib
import logging
import re
from typing import Dict, List
from xml.etree.ElementTree import ElementTree, TreeBuilder

from custom_types import Settings
import markdown_syntax
from table import Table
import xmltags


class MarkdownConverter:
    """Convert Markdown to XML."""

    APPENDIX_HEADING = "Bijlagen"
    APPENDIX_LEVEL = 1

    def __init__(self) -> None:
        self.builder = TreeBuilder()
        self.in_appendices = False
        self.in_measure = False
        self.current_section_level = 0
        self.current_list_tags = []
        self.table = None

    def convert(self, markdown: List[str], settings: Settings) -> ElementTree:
        """Convert the markdown to XML."""
        self.start_document(settings)
        for line in markdown:
            self.process_line(line, settings)
        self.end_document()
        return ElementTree(self.builder.close())

    def start_document(self, settings: Settings) -> None:
        """Start the document."""
        title = settings.get("Title")
        title_attribute = {xmltags.DOCUMENT_TITLE: title} if title else {}
        self.builder.start(xmltags.DOCUMENT, title_attribute)
        if settings["IncludeFrontPage"]:
            self.create_frontpage(settings)
        self.create_header(settings)
        self.create_footer()

    def create_frontpage(self, settings: Settings) -> None:
        """Create a front page."""
        document_type = settings["DocumentType"]
        with self.element(xmltags.FRONTPAGE):
            if document_type in ("Kwaliteitsaanpak", "Template"):
                self.add_element(xmltags.IMAGE, "ICTU.png")
            self.add_element(xmltags.TITLE, settings["Title"])
            if document_type == "Template":
                with self.element(xmltags.PARAGRAPH):
                    with self.element(xmltags.INSTRUCTION):
                        self.add_element(xmltags.BOLD, settings["Subtitle"])
                self.add_element(xmltags.PARAGRAPH)
                with self.element(xmltags.PARAGRAPH):
                    self.builder.data("Versie ")
                    self.add_element(xmltags.INSTRUCTION, "{Versienummer}")
                with self.element(xmltags.PARAGRAPH):
                    self.builder.data("Datum ")
                    self.add_element(xmltags.INSTRUCTION, "{Datum}")
                self.add_element(xmltags.PARAGRAPH)
            if document_type in ("Kwaliteitsaanpak", "Template"):
                self.add_element(xmltags.IMAGE, "word-cloud.png")
            self.add_element(xmltags.PAGEBREAK)

    def create_header(self, settings: Settings) -> None:
        """Create the page header."""
        title = settings["Title"]
        with self.element(xmltags.HEADER):
            if settings["DocumentType"] == "Template":
                with self.element(xmltags.PARAGRAPH):
                    self.builder.data(f"{title} ")
                    self.add_element(xmltags.INSTRUCTION, settings["Subtitle"])
            else:
                self.add_element(xmltags.PARAGRAPH, title)

    def create_footer(self) -> None:
        """Create the page footer."""
        self.add_element(xmltags.FOOTER)

    def process_line(self, line: str, settings: Settings) -> None:
        """Process a line of Markdown."""
        if not (stripped_line := line.strip()):
            self.end_lists()
            self.end_table()
            return  # Empty line, nothing further to do
        ending_measure = False
        if stripped_line.startswith(markdown_syntax.MEASURE_START) and not self.in_measure:
            self.builder.start(xmltags.MEASURE)
            stripped_line = stripped_line[len(markdown_syntax.MEASURE_START):]
            self.in_measure = True
        if stripped_line.endswith(markdown_syntax.MEASURE_END) and self.in_measure:
            ending_measure = True
            stripped_line = stripped_line[:-len(markdown_syntax.MEASURE_END)]
        if match := re.match(markdown_syntax.HEADING_PATTERN, stripped_line):
            self.process_heading(heading=match.group(2), level=len(match.group(1)))
        elif match := re.match(markdown_syntax.BULLET_LIST_PATTERN, stripped_line):
            list_level = {"*": 1, "+": 2, "-": 3}[stripped_line[0]]
            self.process_list(stripped_line, xmltags.BULLET_LIST, list_level)
        elif match := re.match(markdown_syntax.NUMBERED_LIST_PATTERN, stripped_line):
            list_level = 1 if line[0].isdigit() else (3 if stripped_line[0].isdigit() else 2)
            self.process_list(stripped_line, xmltags.NUMBERED_LIST, list_level)
        elif stripped_line[0] == markdown_syntax.TABLE_MARKER:
            self.process_table_row(stripped_line)
        else:
            with self.element(xmltags.PARAGRAPH):
                self.process_formatted_text(stripped_line)
        if self.in_measure and ending_measure:
            self.in_measure = False
            self.builder.end(xmltags.MEASURE)

    def process_heading(self, heading: str, level: int) -> None:
        """Process a heading."""
        if level == self.APPENDIX_LEVEL and heading == self.APPENDIX_HEADING:
            self.in_appendices = True
        is_appendix = {xmltags.SECTION_IS_APPENDIX: "y"} if self.in_appendices else {}
        if self.current_section_level >= level:
            while self.current_section_level > level:
                self.current_section_level -= 1
                self.builder.end(xmltags.SECTION)
            self.builder.end(xmltags.SECTION)
            self.builder.start(xmltags.SECTION, {**is_appendix, xmltags.SECTION_LEVEL: str(self.current_section_level)})
        else:
            while self.current_section_level < level:
                self.current_section_level += 1
                self.builder.start(
                    xmltags.SECTION, {**is_appendix, xmltags.SECTION_LEVEL: str(self.current_section_level)})
        with self.element(xmltags.HEADING):
            self.process_formatted_text(heading)

    def process_list(self, line: str, tag: str, list_level: int) -> None:
        """Process a bullet or numbered list."""
        self.start_lists(tag, list_level)
        self.end_lists(list_level)
        with self.element(xmltags.LIST_ITEM):
            self.process_formatted_text(line.split(" ", maxsplit=1)[1])

    def start_lists(self, tag: str, level: int) -> None:
        """Start (possibly nested) lists until the required level is reached."""
        while len(self.current_list_tags) < level:
            self.current_list_tags.append(tag)
            self.builder.start(tag, {xmltags.LIST_LEVEL: str(len(self.current_list_tags))})

    def end_lists(self, level: int = 0) -> None:
        """End (possibly nested) lists until the required level is reached."""
        while len(self.current_list_tags) > level:
            self.builder.end(self.current_list_tags.pop())

    def process_table_row(self, line: str) -> None:
        """Process table row."""
        if cells := self.get_table_cells(line):
            if self.table is None:
                self.process_table_header(cells)
            else:
                self.process_table_cells(cells)

    def get_table_cells(self, line: str) -> List[str]:
        """Return the table cells."""
        line = line.strip(markdown_syntax.TABLE_MARKER + " " + "\t")
        return [cell.strip() for cell in line.split(markdown_syntax.TABLE_MARKER)]

    def process_table_cells(self, cells: List[str]) -> None:
        """Process the table cells."""
        if "---" in cells[0] and len(self.table.rows) == 0:
            self.process_table_alignment(cells)
        else:
            self.table.rows.append(cells)

    def process_table_alignment(self, cells: List[str]) -> None:
        """Process the alignment row of the Markdown table."""
        alignment_marker = markdown_syntax.CELL_ALIGNMENT_MARKER
        for cell in cells:
            if cell.startswith(alignment_marker) and cell.endswith(alignment_marker):
                alignment = "center"
            elif cell.endswith(alignment_marker):
                alignment = "right"
            else:
                alignment = "left"
            self.table.column_alignment.append(alignment)

    def process_table_header(self, cells: List[str]) -> None:
        """Process the table header."""
        logging.debug("process_table_header: %s", cells)
        self.table = Table(cells)

    def end_table(self) -> None:
        """Flush the table."""
        if self.table is None:
            return
        logging.debug("end_table: %s", self.table.header_cells)
        table_attributes = {
            xmltags.TABLE_COLUMNS: str(len(self.table.header_cells)), xmltags.TABLE_ROWS: str(len(self.table.rows))}
        with self.element(xmltags.TABLE, table_attributes):
            with self.element(xmltags.TABLE_HEADER_ROW):
                for cell, alignment in zip(self.table.header_cells, self.table.column_alignment):
                    with self.element(xmltags.TABLE_CELL, {xmltags.TABLE_CELL_ALIGNMENT: alignment}):
                        self.process_formatted_text(cell)
            for row in self.table.rows:
                with self.element(xmltags.TABLE_ROW):
                    for cell in row:
                        with self.element(xmltags.TABLE_CELL):
                            self.process_formatted_text(cell)
        self.table = None

    def process_formatted_text(self, line: str) -> None:
        """Process formatted Markdown text."""
        seen = ""
        formats = [
            (markdown_syntax.BOLD_START, markdown_syntax.BOLD_END, xmltags.BOLD),
            (markdown_syntax.BOLD_ALTERNATIVE_START, markdown_syntax.BOLD_ALTERNATIVE_END, xmltags.BOLD),
            (markdown_syntax.INSTRUCTION_START, markdown_syntax.INSTRUCTION_END, xmltags.INSTRUCTION),
            (markdown_syntax.ITALIC_START, markdown_syntax.ITALIC_END, xmltags.ITALIC),
            (markdown_syntax.ITALIC_ALTERNATIVE_START, markdown_syntax.ITALIC_ALTERNATIVE_END, xmltags.ITALIC),
            (markdown_syntax.STRIKETROUGH_START, markdown_syntax.STRIKETROUGH_END, xmltags.STRIKETHROUGH)]
        while line:
            format_found = False
            for md_start, md_end, xml_tag in formats:
                if line.startswith(md_start) and md_end in line[len(md_start):]:
                    format_found = True
                    self.flush(seen)
                    seen = ""
                    with self.element(xml_tag):
                        if xml_tag == xmltags.INSTRUCTION:
                            self.builder.data(md_start)
                        formatted_text, line = line[len(md_start):].split(md_end, maxsplit=1)
                        self.process_formatted_text(formatted_text)
                        if xml_tag == xmltags.INSTRUCTION:
                            self.builder.data(md_end)
                    break
            else:
                if match := re.match(markdown_syntax.LINK_PATTERN, line):
                    format_found = True
                    self.flush(seen)
                    seen = ""
                    self.add_element(xmltags.ANCHOR, match.group(1), {xmltags.ANCHOR_LINK: match.group(2)})
                    line = line[len(match.group(0)):]
            if not format_found:
                seen += line[0] if line else ""
                line = line[1:]
        self.flush(seen)

    def end_document(self) -> None:
        """End the document."""
        self.end_lists()
        self.end_table()
        self.builder.end(xmltags.DOCUMENT)

    def add_element(self, tag: str, text: str = "", attributes: Dict[str, str] = None) -> None:
        """Add an element with text."""
        with self.element(tag, attributes):
            self.flush(text)

    @contextlib.contextmanager
    def element(self, tag: str, attributes: Dict[str, str] = None):
        """Return a context manager."""
        element = self.builder.start(tag, attributes or {})
        try:
            yield element
        finally:
            self.builder.end(tag)

    def flush(self, text: str) -> None:
        """Flush the text."""
        if text:
            self.builder.data(text)