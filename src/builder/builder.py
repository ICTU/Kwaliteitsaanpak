"""Abstract document builder class."""

import pathlib
from typing import Dict


Attributes = Dict[str, str]


class Builder:
    """Abstract builder."""

    def __init__(self, filename: pathlib.Path) -> None:
        self.filename = filename
        self.tag_path = []

    def start_document(self) -> None:
        """Start the document."""

    def accept_element(self, tag: str) -> bool:
        """Return whether the builder accepts the element."""
        return True

    def start_element(self, tag: str, attributes: Attributes) -> None:
        """Start element."""
        self.tag_path.append(tag)

    def text(self, tag: str, text: str, attributes: Attributes) -> None:
        """Element text."""

    def end_element(self, tag: str, attributes: Attributes) -> None:
        """End element."""
        self.tag_path.pop()

    def tail(self, tag: str, tail: str, parent: str, attributes: Attributes) -> None:
        """Element tail."""
        self.text(parent, tail, attributes)

    def end_document(self) -> None:
        """End the document."""
