"""Abstract document builder class."""

import pathlib
from dataclasses import dataclass, field

from custom_types import TreeBuilderAttributes


@dataclass
class StackItem:
    """An element currently being built, with the text seen within it so far."""

    tag: str
    attributes: TreeBuilderAttributes
    texts: list[str] = field(default_factory=list)

    def matches(self, tag: str, attributes: TreeBuilderAttributes | None = None) -> bool:
        """Return whether this item has the given tag and contains all the given attributes."""
        attributes = attributes or {}
        return self.tag == tag and attributes.items() <= self.attributes.items()


class Builder:
    """Abstract builder."""

    def __init__(self, filename: pathlib.Path) -> None:
        self.filename = filename
        self._stack: list[StackItem] = []

    def start_document(self) -> None:
        """Start the document."""

    def accept_element(self, tag: str, attributes: TreeBuilderAttributes) -> bool:
        """Return whether the builder accepts the element."""
        return True

    def get_element_attributes(self, tag: str) -> TreeBuilderAttributes | None:
        """Return the attributes of the element."""
        if matching_elements := [element for element in self._stack if element.matches(tag)]:
            return matching_elements[-1].attributes
        return None

    def in_element(self, tag: str, attributes: TreeBuilderAttributes | None = None) -> bool:
        """Return whether we are currently in an element with the specified tag and attributes."""
        return self.nr_elements(tag, attributes) > 0

    def nr_elements(self, tag: str, attributes: TreeBuilderAttributes | None = None) -> int:
        """Return how many elements with the specified tag and attributes are currently being built."""
        return len([element for element in self._stack if element.matches(tag, attributes)])

    def start_element(self, tag: str, attributes: TreeBuilderAttributes) -> None:
        """Start element."""
        self._stack.append(StackItem(tag, attributes))

    def text(self, tag: str, text: str, attributes: TreeBuilderAttributes) -> None:
        """Element text."""
        self._stack[-1].texts.append(text)

    def current_text(self) -> str:
        """Return the concatenated text buffered in the element currently being built."""
        return "".join(self._stack[-1].texts)

    def end_element(self, tag: str, attributes: TreeBuilderAttributes) -> None:
        """End element."""
        self._stack.pop()

    def tail(self, tag: str, tail: str, parent: str, attributes: TreeBuilderAttributes) -> None:
        """Element tail."""
        self.text(parent, tail, attributes)

    def end_document(self) -> None:
        """End the document."""
