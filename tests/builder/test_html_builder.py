"""HTML builder unit tests."""

import pathlib
import tempfile
import unittest
from xml.etree.ElementTree import Element, ElementTree, SubElement

from pygments.util import ClassNotFound

import xmltags
from builder.html_builder import HTMLBuilder
from converter import Converter


class CodeBlockTest(unittest.TestCase):
    """Unit tests for code blocks in the HTML builder."""

    def build(self, language: str, code: str) -> str:
        """Build an HTML document with a single code block and return its contents."""
        document = Element(xmltags.DOCUMENT, {"title": "Title", "version": "1"})
        SubElement(document, xmltags.FRONTPAGE)  # Starts the <main> element that the document end closes
        code_block = SubElement(document, xmltags.CODE_BLOCK, {xmltags.CODE_BLOCK_LANGUAGE: language})
        code_block.text = code
        with tempfile.TemporaryDirectory() as directory:
            filename = pathlib.Path(directory) / "output.html"
            Converter(ElementTree(document)).convert(HTMLBuilder(filename, pathlib.Path("style.css")))
            return filename.read_text(encoding="utf-8")

    def test_highlighting(self):
        """Test that the code is highlighted, e.g. keywords get the keyword token class."""
        html = self.build("python", "def f(x):\n    return 1\n")
        self.assertIn("highlighttable", html)
        self.assertIn('class="k"', html)

    def test_indentation_preserved(self):
        """Test indentation; the formatter emits &nbsp; for it, which is not a valid XML entity."""
        html = self.build("python", "def f():\n    return 1\n")
        self.assertIn("\u00a0", html)

    def test_special_characters_escaped(self):
        """Test that characters that are special in HTML are escaped rather than parsed as markup."""
        html = self.build("python", "# a < b & c\n")
        self.assertIn("a &lt; b &amp; c", html)

    def test_unknown_language(self):
        """Test that an unknown language raises an exception."""
        self.assertRaises(ClassNotFound, self.build, "nonexistent", "code\n")


class HTMLEntitiesToXMLTest(unittest.TestCase):
    """Unit tests for converting named HTML entities to numeric character references."""

    def test_named_entity(self):
        """Test that a named HTML entity is turned into a numeric character reference."""
        self.assertEqual("a&#160;b", HTMLBuilder.html_entities_to_xml("a&nbsp;b"))

    def test_xml_entities_kept(self):
        """Test that the entities the XML parser already understands are left untouched."""
        self.assertEqual("&amp;&lt;&gt;&quot;&apos;", HTMLBuilder.html_entities_to_xml("&amp;&lt;&gt;&quot;&apos;"))

    def test_unknown_entity_kept(self):
        """Test that an unknown entity is left untouched."""
        self.assertEqual("&unknown;", HTMLBuilder.html_entities_to_xml("&unknown;"))
