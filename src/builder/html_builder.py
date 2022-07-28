"""HTML builder."""

import pathlib
from typing import List, Optional
from xml.etree.ElementTree import ElementTree, TreeBuilder

import xmltags
from custom_types import TreeBuilderAttributes
from . import html_tags
from .builder import Builder
from .utils import slugify


class HTMLBuilder(Builder):
    """HTML builder."""

    FORMAT = {
        xmltags.BOLD: html_tags.BOLD,
        xmltags.ITALIC: html_tags.ITALIC,
        xmltags.STRIKETHROUGH: html_tags.STRIKETROUGH,
    }
    LIST = {
        xmltags.BULLET_LIST: html_tags.UNORDERED_LIST,
        xmltags.NUMBERED_LIST: html_tags.ORDERED_LIST,
        xmltags.LIST_ITEM: html_tags.LIST_ITEM,
    }
    STYLESHEET = "ICTU-Kwaliteitsaanpak.css"

    def __init__(self, filename: pathlib.Path, stylesheet_path: pathlib.Path) -> None:
        super().__init__(filename)
        self.stylesheet_path = stylesheet_path
        self.builder = TreeBuilder()
        self.heading_class: List[str] = []  # Heading class stack
        self.heading_level: List[int] = []  # Heading level stack
        self.table_cell_html_tag: Optional[str] = None
        self.in_keep_together_div = False
        self.in_measure = False
        self.frontpage_done = False

    def start_element(self, tag: str, attributes: TreeBuilderAttributes) -> None:  # pylint:disable=too-many-branches
        if tag == xmltags.DOCUMENT:
            self.builder.start(html_tags.HTML, {html_tags.LANGUAGE: "nl"})
            self.builder.start(html_tags.HEAD, {})
            self.builder.start(html_tags.META, {html_tags.META_CHARSET: "UTF-8"})
            self.builder.end(html_tags.META)
            self.builder.start(html_tags.TITLE, {})
            self.builder.data(f"{attributes['title']} versie {attributes['version']}")
            self.builder.end(html_tags.TITLE)
            self.builder.start(
                html_tags.LINK,
                {html_tags.LINK_REL: "stylesheet", html_tags.LINK_HREF: self.STYLESHEET},
            )
            self.builder.end(html_tags.LINK)
            self.builder.end(html_tags.HEAD)
            self.builder.start(html_tags.BODY, {})
        elif tag == xmltags.PARAGRAPH:
            if not self.in_measure:
                self.builder.start(html_tags.PARAGRAPH, attributes)
        elif tag in self.LIST:
            self.builder.start(self.LIST[tag], {})
        elif tag in self.FORMAT:
            self.builder.start(self.FORMAT[tag], {})
        elif tag == xmltags.SECTION:
            self.heading_class.append("bijlage" if attributes.get(xmltags.SECTION_IS_APPENDIX) else "")
            self.heading_level.append(int(attributes[xmltags.SECTION_LEVEL]))
        elif tag == xmltags.TABLE:
            self.builder.start(html_tags.TABLE, {})
        elif tag == xmltags.TABLE_HEADER_ROW:
            self.table_cell_html_tag = html_tags.TABLE_HEAD_CELL
            self.builder.start(html_tags.TABLE_HEAD, {})
            self.builder.start(html_tags.TABLE_ROW, {})
        elif tag == xmltags.TABLE_ROW:
            self.table_cell_html_tag = html_tags.TABLE_BODY_CELL
            self.builder.start(html_tags.TABLE_ROW, {})
        elif tag == xmltags.TABLE_CELL:
            assert self.table_cell_html_tag
            alignment = str(attributes[xmltags.TABLE_CELL_ALIGNMENT])
            self.builder.start(self.table_cell_html_tag, {html_tags.STYLE: f"text-align:{alignment}"})
        elif tag == xmltags.ANCHOR:
            self.builder.start(
                html_tags.ANCHOR,
                {html_tags.ANCHOR_LINK: attributes[xmltags.ANCHOR_LINK]},
            )
        elif tag == xmltags.IMAGE:
            image_attributes = {
                html_tags.STYLE: "max-width: 100%",
                html_tags.IMAGE_SOURCE: attributes["src"],
            }
            title = attributes.get("title", "")
            alt = attributes.get("alt", "")
            image_attributes[html_tags.IMAGE_ALT] = f"{title}{': ' if title and alt else ''}{alt}"
            self.builder.start(html_tags.IMAGE, image_attributes)
            self.builder.end(html_tags.IMAGE)
        elif tag == xmltags.MEASURE:
            self.builder.start(html_tags.DIV, {html_tags.CLASS: "maatregel"})
            self.in_measure = True

    def text(self, tag: str, text: str, attributes: TreeBuilderAttributes) -> None:
        if tag == xmltags.TITLE:
            title = html_tags.PARAGRAPH
            self.builder.start(title, {html_tags.CLASS: "title"})
            self.builder.data(text)
            self.builder.end(title)
        if tag == xmltags.HEADING:
            if self.heading_level[-1] > 1 and not self.in_keep_together_div:
                self.builder.start(html_tags.DIV, {html_tags.CLASS: "keep-together"})
                self.in_keep_together_div = True
            heading_attributes: TreeBuilderAttributes = (
                {html_tags.CLASS: self.heading_class[-1]} if self.heading_class[-1] else {}
            )
            if self.heading_level[-1] <= 2:
                heading_attributes["id"] = slugify(text)
            self.builder.start(html_tags.HEADING + str(self.heading_level[-1]), heading_attributes)
        if tag not in (xmltags.IMAGE, xmltags.HEADER, xmltags.TITLE):
            self.builder.data(text)

    def end_element(self, tag: str, attributes: TreeBuilderAttributes) -> None:
        if tag == xmltags.DOCUMENT:
            self.builder.end(html_tags.BODY)
            self.builder.end(html_tags.HTML)
        elif tag == xmltags.FRONTPAGE:
            self.frontpage_done = True
        elif tag == xmltags.PARAGRAPH:
            self.end_paragraph()
        elif tag in self.LIST:
            self.end_list(tag)
        elif tag in self.FORMAT:
            self.builder.end(self.FORMAT[tag])
        elif tag == xmltags.SECTION:
            self.heading_class.pop()
            self.heading_level.pop()
        elif tag == xmltags.HEADING:
            self.builder.end(html_tags.HEADING + str(self.heading_level[-1]))
        elif tag == xmltags.TABLE:
            self.builder.end(html_tags.TABLE_BODY)
            self.builder.end(html_tags.TABLE)
        elif tag == xmltags.TABLE_HEADER_ROW:
            self.builder.end(html_tags.TABLE_ROW)
            self.builder.end(html_tags.TABLE_HEAD)
            self.builder.start(html_tags.TABLE_BODY, {})
        elif tag == xmltags.TABLE_ROW:
            self.builder.end(html_tags.TABLE_ROW)
        elif tag == xmltags.TABLE_CELL:
            assert self.table_cell_html_tag
            self.builder.end(self.table_cell_html_tag)
        elif tag == xmltags.ANCHOR:
            self.builder.end(html_tags.ANCHOR)
        elif tag == xmltags.MEASURE:
            self.builder.end(html_tags.DIV)
            self.in_measure = False

    def end_paragraph(self) -> None:
        """End the paragraph."""
        if self.in_measure:
            self.builder.start(html_tags.LINE_BREAK, {})
            self.builder.end(html_tags.LINE_BREAK)
        else:
            self.builder.end(html_tags.PARAGRAPH)
            if self.in_keep_together_div:
                self.in_keep_together_div = False
                self.builder.end(html_tags.DIV)

    def end_list(self, tag: str) -> None:
        """End the list."""
        self.builder.end(self.LIST[tag])
        if tag in (xmltags.NUMBERED_LIST, xmltags.BULLET_LIST) and self.in_keep_together_div:
            self.in_keep_together_div = False
            self.builder.end(html_tags.DIV)

    def end_document(self) -> None:
        tree = ElementTree(self.builder.close())
        with open(self.filename, mode="w", encoding="utf-8") as html_file:
            html_file.write("<!DOCTYPE html>\n")
            tree.write(html_file, "unicode", method="html")


class HTMLContentBuilder(HTMLBuilder):
    """HTML document content builder."""

    def accept_element(self, tag: str) -> bool:
        return tag != xmltags.FRONTPAGE


class HTMLCoverBuilder(HTMLBuilder):
    """HTML cover builder."""

    def accept_element(self, tag: str) -> bool:
        return not self.frontpage_done
