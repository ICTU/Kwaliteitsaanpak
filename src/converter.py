"""Converter."""

from xml.etree.ElementTree import Element, ElementTree

from markdown_builder import Builder
import xmltags


class Converter:
    """Converter."""
    def __init__(self, xml: ElementTree) -> None:
        self.root = xml.getroot()

    def convert(self, builder: Builder) -> None:
        """Convert the XML using the builder."""
        builder.start_document()
        self.convert_element(self.root, builder)
        builder.end_document()

    def convert_element(self, element: Element, builder: Builder) -> None:
        """Convert the element using the builder."""
        builder.start_element(element.tag, element.attrib)
        if element.text:
            builder.text(element.tag, element.text)
        for child_element in element:
            self.convert_element(child_element, builder)
        builder.end_element(element.tag, element.attrib)
        if element.tail:
            builder.tail(element.tag, element.tail)
