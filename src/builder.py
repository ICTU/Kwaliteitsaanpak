"""Abstract document builder class."""

import pathlib
from typing import Dict


class Builder:
    """Abstract builder."""
    def __init__(self, filename: pathlib.Path) -> None:
        self.filename = filename

    def start_document(self) -> None:
        """Start the document."""

    def start_element(self, tag: str, attributes: Dict[str, str]) -> None:
        """Start element."""

    def text(self, tag: str, text: str) -> None:
        """Element text."""

    def end_element(self, tag: str, attributes: Dict[str, str]) -> None:
        """End element."""

    def tail(self, tag: str, tail: str) -> None:
        """Element tail."""

    def end_document(self) -> None:
        """End the document."""
