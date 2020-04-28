"""Docx builder."""

import pathlib
import shutil
from typing import Dict

import markdown_syntax
import xmltags

from builder import Builder


class DocxBuilder(Builder):
    """Docx builder."""

    def __init__(self, filename: str, docx_reference_filename: str) -> None:
        super().__init__(filename)
        docx = pathlib.Path(filename)
        docx.unlink(missing_ok=True)
        shutil.copy(pathlib.Path(docx_reference_filename), docx)

    def start_document(self) -> None:
        pass