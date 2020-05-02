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
        self.paragraph = None
        self.current_list_style = []
        self.current_list_level = 0
        self.previous_list_item = []

    def start_element(self, tag: str, attributes: Attributes) -> None:
        if tag == xmltags.PARAGRAPH:
            self.paragraph = self.doc.add_paragraph()
        elif tag == xmltags.PAGEBREAK:
            self.doc.add_page_break()
        elif tag == xmltags.BULLET_LIST:
            self.current_list_style.append("Lijst opsom.teken1")
            self.previous_list_item.append(None)
            self.current_list_level += 1
        elif tag == xmltags.NUMBERED_LIST:
            self.current_list_style.append("Lijstnummering1")
            self.previous_list_item.append(None)
            self.current_list_level += 1
        elif tag == xmltags.LIST_ITEM:
            self.paragraph = self.doc.add_paragraph(style=self.current_list_style[-1])
            self.paragraph._p.get_or_add_pPr().get_or_add_numPr().get_or_add_ilvl().val = self.current_list_level - 1
            if "Lijstnummering1" == self.current_list_style[-1]:
                if self.previous_list_item[-1] is None:
                    num = self.doc.part.numbering_part.numbering_definitions._numbering.add_num("0")  # Abstract numId of Lijstnummering1
                    num.add_lvlOverride(ilvl=self.current_list_level - 1).add_startOverride(1)
                    num = num.numId
                else:
                    num = self.previous_list_item[-1]._p.pPr.numPr.numId.val
                self.paragraph._p.get_or_add_pPr().get_or_add_numPr().get_or_add_numId().val = num
            self.previous_list_item[-1] = self.paragraph

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

    def end_element(self, tag: str, attributes: Attributes) -> None:
        if tag in (xmltags.BULLET_LIST, xmltags.NUMBERED_LIST):
            self.current_list_style.pop()
            self.previous_list_item.pop()
            self.current_list_level -= 1

    def tail(self, tag: str, tail: str, parent: str) -> None:
        self.text(parent, tail)

    def end_document(self) -> None:
        self.doc.save(self.filename)
