"""Abstract document builder class."""

import pathlib

from custom_types import TreeBuilderAttributes


class Builder:
    """Abstract builder."""

    # pylint: disable=unused-argument

    def __init__(self, filename: pathlib.Path) -> None:
        self.filename = filename
        self._stack: list[tuple[str, TreeBuilderAttributes]] = []

    def start_document(self) -> None:
        """Start the document."""

    def accept_element(self, tag: str) -> bool:
        """Return whether the builder accepts the element."""
        return True

    def in_element(self, tag: str, attributes: TreeBuilderAttributes | None = None) -> bool:
        """Return whether we are currently in an element with the specified tag and attributes."""
        return self.nr_elements(tag, attributes) > 0

    def nr_elements(self, tag: str, attributes: TreeBuilderAttributes | None = None) -> int:
        """Return how many elements with the specified tag and attributes are currently being built."""
        attributes = attributes or {}
        return len(
            [element for element in self._stack if tag == element[0] and attributes.items() <= element[1].items()]
        )

    def start_element(self, tag: str, attributes: TreeBuilderAttributes) -> None:
        """Start element."""
        self._stack.append((tag, attributes))

    def text(self, tag: str, text: str, attributes: TreeBuilderAttributes) -> None:
        """Element text."""

    def end_element(self, tag: str, attributes: TreeBuilderAttributes) -> None:
        """End element."""
        self._stack.pop()

    def tail(self, tag: str, tail: str, parent: str, attributes: TreeBuilderAttributes) -> None:
        """Element tail."""
        self.text(parent, tail, attributes)

    def end_document(self) -> None:
        """End the document."""
