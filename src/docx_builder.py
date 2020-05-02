"""Docx builder."""

import pathlib
import shutil
from docx import Document
from docx.enum.text import WD_COLOR_INDEX
from typing import Dict

from builder import Attributes, Builder
import xmltags


class DocxBuilder(Builder):
    """Docx builder."""

    def __init__(self, filename: pathlib.Path, docx_reference_filename: pathlib.Path) -> None:
        super().__init__(filename)
        filename.unlink(missing_ok=True)
        shutil.copy(docx_reference_filename, filename)
        self.doc = Document(filename)
        self.paragraph = None  # The current paragraph
        self.current_list_style = []  # Stack of list styles
        self.previous_list_item = []  # Stack of previous list items

    def start_element(self, tag: str, attributes: Attributes) -> None:
        if tag == xmltags.PARAGRAPH:
            self.paragraph = self.doc.add_paragraph()
        elif tag == xmltags.PAGEBREAK:
            self.doc.add_page_break()
        elif tag == xmltags.BULLET_LIST:
            self.current_list_style.append("Lijst opsom.teken1")
            self.previous_list_item.append(None)
        elif tag == xmltags.NUMBERED_LIST:
            self.current_list_style.append("Lijstnummering1")
            self.previous_list_item.append(None)
        elif tag == xmltags.LIST_ITEM:
            self.paragraph = self.doc.add_paragraph(style=self.current_list_style[-1])
            level = len(self.current_list_style) - 1
            self.paragraph._p.get_or_add_pPr().get_or_add_numPr().get_or_add_ilvl().val = level
            if "Lijstnummering1" == self.current_list_style[-1]:
                if self.previous_list_item[-1] is None:
                    # Add a new concrete numbering for Lijstnummering1. "0" is the id of the abstract numbering of
                    # Lijstnummering1. This id can be found in the word/numbering.xml file (unzip reference.docx so
                    # see word/numbering.xml), look for the <w:abstractNum w:abstractNumId="0" ...> that has a
                    # child element <w:pStyle w:val="Lijstnummering1"/>
                    num = self.doc.part.numbering_part.numbering_definitions._numbering.add_num("0")
                    num.add_lvlOverride(ilvl=level).add_startOverride(1)  # Restart the numbering
                    num = num.numId
                else:
                    num = self.previous_list_item[-1]._p.pPr.numPr.numId.val
                self.paragraph._p.get_or_add_pPr().get_or_add_numPr().get_or_add_numId().val = num
            self.previous_list_item[-1] = self.paragraph
        elif tag == xmltags.SECTION:
            level = attributes["level"]
            style = f"Kop {level} Bijlage" if attributes.get("is-appendix") else f"heading {level}"
            self.paragraph = self.doc.add_paragraph(style=style)

    def text(self, tag: str, text: str) -> None:
        if tag == xmltags.PARAGRAPH:
            self.paragraph.add_run(text)
        elif tag == xmltags.INSTRUCTION:
            self.paragraph.add_run(text).font.highlight_color = WD_COLOR_INDEX.YELLOW
        elif tag == xmltags.BOLD:
            self.paragraph.add_run(text).font.bold = True
        elif tag == xmltags.ITALIC:
            self.paragraph.add_run(text).font.italic = True
        elif tag == xmltags.STRIKETHROUGH:
            self.paragraph.add_run(text).font.strike = True
        elif tag == xmltags.LIST_ITEM:
            self.paragraph.add_run(text)
        elif tag == xmltags.HEADING:
            self.paragraph.add_run(text)

    def end_element(self, tag: str, attributes: Attributes) -> None:
        if tag in (xmltags.BULLET_LIST, xmltags.NUMBERED_LIST):
            self.current_list_style.pop()
            self.previous_list_item.pop()

    def tail(self, tag: str, tail: str, parent: str) -> None:
        self.text(parent, tail)

    def end_document(self) -> None:
        self.doc.save(self.filename)
