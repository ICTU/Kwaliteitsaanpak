"""Converter."""

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
            self.convert_element(self.root, builder)
        builder.end_document()

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
