"""Converter unit tests."""

import unittest
import xml.etree.ElementTree
from unittest.mock import Mock

from converter import Converter
from builder.builder import Builder


class ConverterTestCase(unittest.TestCase):
    """Converter unit tests."""

    def setUp(self):
        self.builder = Mock(spec=Builder)

    def test_empty_document(self):
        """Test an empty document."""
        tree = xml.etree.ElementTree.ElementTree()
        Converter(tree).convert(self.builder)
        self.builder.start_document.assert_called_once()
        self.builder.accept_element.assert_not_called()
        self.builder.start_element.assert_not_called()
        self.builder.end_element.assert_not_called()
        self.builder.end_document.assert_called_once()

    def test_convert_element(self):
        """Test that the builder is called for each element."""
        tree = xml.etree.ElementTree.ElementTree(xml.etree.ElementTree.XML("<document/>"))
        Converter(tree).convert(self.builder)
        self.builder.start_document.assert_called_once()
        self.builder.accept_element.assert_called_once_with("document")
        self.builder.start_element.assert_called_once_with("document", {})
        self.builder.end_element.assert_called_once_with("document", {})
        self.builder.end_document.assert_called_once()

    def test_convert_text(self):
        """Test that the builder is called for text."""
        tree = xml.etree.ElementTree.ElementTree(xml.etree.ElementTree.XML("<document>Text</document>"))
        Converter(tree).convert(self.builder)
        self.builder.text.assert_called_once_with("document", "Text", {})

    def test_convert_tail(self):
        """Test that the builder is called for tail."""
        tree = xml.etree.ElementTree.ElementTree(xml.etree.ElementTree.XML("<document><b>Text</b>Tail</document>"))
        Converter(tree).convert(self.builder)
        self.builder.tail.assert_called_once_with("b", "Tail", "document", {})

    def test_skip_elements_not_accepted(self):
        """Test that the builder skips elements that are not accepted by the builder."""
        self.builder.accept_element.side_effect = [True, False]
        tree = xml.etree.ElementTree.ElementTree(xml.etree.ElementTree.XML("<document><skip>Text</skip></document>"))
        Converter(tree).convert(self.builder)
        self.builder.start_element.assert_called_once_with("document", {})
