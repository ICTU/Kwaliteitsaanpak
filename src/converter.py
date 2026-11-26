"""Converter."""

import copy
from collections.abc import Sequence
from xml.etree.ElementTree import Element, ElementTree

from builder.builder import Builder


class Converter:
    """Convert the XML to a destination format using a document builder."""

    def __init__(self, xml: ElementTree) -> None:
        self.root = xml.getroot()

    def convert(self, builder: Builder) -> None:
        """Convert the XML using the builder."""
        builder.start_document()
        if self.root is not None:
            self.convert_element(self.flatten(self.root, builder.FLATTEN_TAGS), builder)
        builder.end_document()

    @staticmethod
    def flatten(root: Element, tags: Sequence[str]) -> Element:
        """Return a copy of the tree in which the elements with the given tags are replaced by their text. Assumes
        that the elements with the given tags have no child elements."""
        if not tags:
            return root
        root = copy.deepcopy(root)
        for parent in list(root.iter()):
            previous_child: Element | None = None
            for child in list(parent):
                if child.tag not in tags:
                    previous_child = child
                    continue
                text = (child.text or "") + (child.tail or "")
                if previous_child is None:
                    parent.text = (parent.text or "") + text
                else:
                    previous_child.tail = (previous_child.tail or "") + text
                parent.remove(child)
        return root

    def convert_element(self, element: Element, builder: Builder, parent: Element | None = None) -> None:
        """Recursively convert the element using the builder."""
        attributes = element.attrib
        if not builder.accept_element(element.tag, attributes):
            return
        builder.start_element(element.tag, attributes)
        if element.text:
            builder.text(element.tag, element.text, attributes)
        for child_element in element:
            self.convert_element(child_element, builder, element)
        builder.end_element(element.tag, attributes)
        if element.tail:
            assert parent is not None
            builder.tail(element.tag, element.tail, parent.tag, attributes)
