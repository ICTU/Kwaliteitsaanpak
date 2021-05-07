"""Kwaliteitsaanpak PPTX-presentation builder."""

import pathlib

from pptx import Presentation

from .builder import Builder


class PptxBuilder(Builder):
    """Kwaliteitsaanpak presentation builder."""

    def __init__(self, filename: pathlib.Path) -> None:
        super().__init__(filename)
        filename.unlink(missing_ok=True)
        self.presentation = Presentation("../DocumentDefinitions/reference.pptx")

    def end_document(self) -> None:
        self.presentation.save(self.filename)
