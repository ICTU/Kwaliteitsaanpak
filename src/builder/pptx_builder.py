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
    MEASURE_SLIDE = 1

    def __init__(self, filename: pathlib.Path, pptx_reference_filename: pathlib.Path) -> None:
        super().__init__(filename)
        filename.unlink(missing_ok=True)
        shutil.copy(pptx_reference_filename, filename)
        self.presentation = Presentation(filename)
        # Make the title placeholder on the measure slide wider
        measure_master_slide = self.presentation.slide_master.slide_layouts[self.MEASURE_SLIDE]
        measure_master_slide.placeholders[0].width = Inches(10)
        self.current_slide = None

    def text(self, tag: str, text: str, attributes: TreeBuilderAttributes) -> None:
        if tag == xmltags.TITLE:
            slide_layout = self.presentation.slide_layouts[self.TITLE_SLIDE]
            self.current_slide = self.presentation.slides.add_slide(slide_layout)
            title_placeholder = self.current_slide.shapes.title
            title_placeholder.text = text
            title_placeholder.text_frame.paragraphs[0].font.size = Pt(60)
        elif tag == xmltags.PARAGRAPH and self.in_element(xmltags.FRONTPAGE):
            self.current_slide.shapes[1].text = text
        elif self.in_element(xmltags.MEASURE) and tag == xmltags.BOLD and not self.in_appendix():
            slide_layout = self.presentation.slide_layouts[self.MEASURE_SLIDE]
            self.current_slide = self.presentation.slides.add_slide(slide_layout)
            title = self.current_slide.shapes.title
            title.text = text
            title.text_frame.paragraphs[0].font.size = Pt(24)

    def in_appendix(self) -> bool:
        """Return whether the current section is an appendix."""
        return self.in_element(xmltags.SECTION, {xmltags.SECTION_IS_APPENDIX: "y"})

    def end_document(self) -> None:
        """Override to save the presentation."""
        self.presentation.save(self.filename)
