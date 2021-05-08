"""Kwaliteitsaanpak PPTX-presentation builder."""

import pathlib
import shutil

from pptx import Presentation
from pptx.util import Inches, Pt

import xmltags
from custom_types import TreeBuilderAttributes
from .builder import Builder


class PptxBuilder(Builder):
    """Kwaliteitsaanpak presentation builder."""

    # Slide layouts. These are specific for the reference file
    TITLE_SLIDE = 0
    MEASURE_SLIDE = 4
    CHAPTER_SLIDE = 16

    def __init__(self, filename: pathlib.Path, pptx_reference_filename: pathlib.Path) -> None:
        super().__init__(filename)
        filename.unlink(missing_ok=True)
        shutil.copy(pptx_reference_filename, filename)
        self.presentation = Presentation(filename)
        # Make the title placeholder on the measure slide wider
        measure_master_slide = self.presentation.slide_master.slide_layouts[self.MEASURE_SLIDE]
        measure_master_slide.placeholders[0].width = Inches(10)
        self.current_slide = None
        self.chapter_heading = None

    def text(self, tag: str, text: str, attributes: TreeBuilderAttributes) -> None:
        if tag == xmltags.TITLE:
            self.add_slide(self.TITLE_SLIDE, text)
            self.current_slide.shapes.title.text_frame.paragraphs[0].font.size = Pt(60)
        elif tag == xmltags.PARAGRAPH and self.in_element(xmltags.FRONTPAGE):
            self.current_slide.shapes[1].text = text
        elif self.in_element(xmltags.MEASURE) and not self.in_appendix():
            if self.chapter_heading:
                self.add_slide(self.CHAPTER_SLIDE, self.chapter_heading)
                self.chapter_heading = None
            if tag == xmltags.BOLD:
                self.add_slide(self.MEASURE_SLIDE, text)
                self.current_slide.shapes.title.text_frame.paragraphs[0].font.size = Pt(24)
            else:
                text_box = self.current_slide.shapes.add_textbox(Inches(0.7), Inches(1.6), Inches(12), Inches(6))
                text_box.text_frame.word_wrap = True
                text_box.text = text
        elif tag == xmltags.HEADING and self.in_element(xmltags.SECTION, dict(level="1")) and not self.in_element(xmltags.SECTION, dict(level="2")):
            self.chapter_heading = text

    def add_slide(self, slide_layout_index: int, title: str) -> None:
        slide_layout = self.presentation.slide_layouts[slide_layout_index]
        self.current_slide = self.presentation.slides.add_slide(slide_layout)
        self.current_slide.shapes.title.text = title

    def in_appendix(self) -> bool:
        """Return whether the current section is an appendix."""
        return self.in_element(xmltags.SECTION, {xmltags.SECTION_IS_APPENDIX: "y"})

    def end_document(self) -> None:
        """Override to save the presentation."""
        self.presentation.save(self.filename)
