"""Markdown builder."""

import pathlib
from typing import Dict

import markdown_syntax
import xmltags


class Builder:
    """Abstract builder."""
    def __init__(self, filename: pathlib.Path) -> None:
        self.filename = filename

    def start_document(self) -> None:
        """Start the document."""

    def end_document(self) -> None:
        """End the document."""

    def start_element(self, tag: str) -> None:
        """Start element."""

    def text(self, tag: str, text: str) -> None:
        """Element text."""

    def end_element(self, tag: str) -> None:
        """Start element."""

    def tail(self, tag: str, tail: str) -> None:
        """Element tail."""


class MarkdownBuilder(Builder):
    """Markdown builder."""

    LIST_ITEMS = {xmltags.BULLET_LIST: ["*", "+", "-"], xmltags.NUMBERED_LIST: ["1.", "a.", "1."]}
    FORMAT_START = {
        xmltags.ITALIC: markdown_syntax.ITALIC_START,
        xmltags.BOLD: markdown_syntax.BOLD_START,
        xmltags.STRIKETHROUGH: markdown_syntax.STRIKETROUGH_START,
        xmltags.MEASURE: markdown_syntax.MEASURE_START}
    FORMAT_END = {
        xmltags.ITALIC: markdown_syntax.ITALIC_END,
        xmltags.BOLD: markdown_syntax.BOLD_END,
        xmltags.STRIKETHROUGH: markdown_syntax.STRIKETROUGH_END,
        xmltags.MEASURE: markdown_syntax.MEASURE_END}

    def __init__(self, filename: pathlib.Path) -> None:
        super().__init__(filename)
        self.markdown = ""  # lines of Markdown
        self.current_section_level = 0
        self.current_list_item = []
        self.table_alignments = ""

    def start_element(self, tag: str, attributes: Dict[str, str]) -> None:
        if tag in self.FORMAT_START:
            self.markdown += self.FORMAT_START[tag]
        elif tag == xmltags.SECTION:
            self.current_section_level += 1
        elif tag == xmltags.HEADING:
            self.markdown += "#" * self.current_section_level + " "
        elif tag in (xmltags.BULLET_LIST, xmltags.NUMBERED_LIST):
            level = int(attributes[xmltags.LIST_LEVEL]) - 1
            self.current_list_item.append("  " * level + self.LIST_ITEMS[tag][level] + " ")
        elif tag == xmltags.LIST_ITEM:
            self.markdown += self.current_list_item[-1]
        elif tag in (xmltags.TABLE_HEADER_ROW, xmltags.TABLE_ROW):
            self.table_alignments = ""
            self.markdown += "|"
        elif tag == xmltags.TABLE_CELL:
            alignment = attributes.get(xmltags.TABLE_CELL_ALIGNMENT, "left")
            self.table_alignments += dict(left="|:---", center="|:---:", right="|---:")[alignment]
            self.markdown += " "
        elif tag == xmltags.ANCHOR:
            self.markdown += "["

    def text(self, tag: str, text: str) -> None:
        if tag != xmltags.IMAGE:
            self.markdown += text

    def end_element(self, tag: str, attributes: Dict[str, str]) -> None:
        if tag in self.FORMAT_END:
            self.markdown += self.FORMAT_END[tag]
        elif tag == xmltags.PARAGRAPH:
            self.markdown += "\n\n"
        elif tag == xmltags.SECTION:
            self.current_section_level -= 1
        elif tag == xmltags.HEADING:
            self.markdown += "\n\n"
        elif tag in (xmltags.BULLET_LIST, xmltags.NUMBERED_LIST):
            self.current_list_item.pop()
            if not self.current_list_item:
                self.markdown += "\n"
        elif tag == xmltags.LIST_ITEM:
            self.markdown += "\n"
        elif tag == xmltags.TABLE:
            self.markdown += "\n"
        elif tag == xmltags.TABLE_CELL:
            self.markdown += " |"
        elif tag == xmltags.TABLE_HEADER_ROW:
            self.markdown += f"\n{self.table_alignments}|\n"
        elif tag == xmltags.TABLE_ROW:
            self.markdown += "\n"
        elif tag == xmltags.ANCHOR:
            self.markdown += f"]({attributes[xmltags.ANCHOR_LINK]})"

    def tail(self, tag: str, tail: str) -> None:
        self.markdown += tail

    def end_document(self) -> None:
        with open(self.filename, "w") as markdown_file:
            markdown_file.write(self.markdown)
