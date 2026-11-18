"""Pptx builder unit tests."""

import pathlib
import tempfile
import unittest
from xml.etree.ElementTree import Element, ElementTree, SubElement

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

import xmltags
from builder.pptx_builder import PptxBuilder
from converter import Converter

REFERENCE_PPTX = pathlib.Path(__file__).parents[2] / "DocumentDefinitions" / "reference-ictu.pptx"
DIAGRAM = "flowchart TD\n    accTitle: Title\n    accDescr: Description\n    A --> B\n"


class DiagramTest(unittest.TestCase):
    """Unit tests for diagrams in the pptx builder."""

    def setUp(self):
        self.document = Element(xmltags.DOCUMENT)

    def build(self):
        """Build a pptx from the XML document and return the pictures on the last slide."""
        with tempfile.TemporaryDirectory() as directory:
            filename = pathlib.Path(directory) / "output.pptx"
            Converter(ElementTree(self.document)).convert(PptxBuilder(filename, REFERENCE_PPTX))
            presentation = Presentation(str(filename))
        slides = list(presentation.slides)
        shapes = slides[-1].shapes if slides else []
        return [shape for shape in shapes if shape.shape_type == MSO_SHAPE_TYPE.PICTURE], presentation

    def test_diagram_on_slide(self):
        """Test that a diagram on a slide is added as picture that fits the content area, with title and description."""
        SubElement(SubElement(self.document, xmltags.SLIDE), xmltags.DIAGRAM).text = DIAGRAM
        pictures, presentation = self.build()
        picture = pictures[0]
        self.assertEqual("Title", picture._element._nvXxPr.cNvPr.get("title"))
        self.assertEqual("Description", picture._element._nvXxPr.cNvPr.get("descr"))
        self.assertLessEqual(picture.height, PptxBuilder.CONTENT_HEIGHT)
        self.assertLessEqual(picture.width, PptxBuilder.CONTENT_WIDTH)
        self.assertAlmostEqual(presentation.slide_width - picture.width, 2 * picture.left, delta=1)

    def test_diagram_outside_slide(self):
        """Test that a diagram outside slides and measures is not added to the presentation."""
        SubElement(self.document, xmltags.DIAGRAM).text = DIAGRAM
        pictures, _ = self.build()
        self.assertEqual([], pictures)


class SlideTitleTest(unittest.TestCase):
    """Unit tests for the titles of slides in the pptx builder."""

    def setUp(self):
        self.document = Element(xmltags.DOCUMENT)
        self.chapter = self.add_section(self.document, "1", "Chapter")

    @staticmethod
    def add_section(parent: Element, level: str, heading: str) -> Element:
        """Add a section with a heading to the parent."""
        section = SubElement(parent, xmltags.SECTION, {xmltags.SECTION_LEVEL: level})
        SubElement(section, xmltags.HEADING).text = heading
        return section

    def slide_title(self, parent: Element) -> str:
        """Add a slide to the parent, build the pptx, and return the title of the last slide."""
        SubElement(SubElement(parent, xmltags.SLIDE), xmltags.PARAGRAPH).text = "Text"
        with tempfile.TemporaryDirectory() as directory:
            filename = pathlib.Path(directory) / "output.pptx"
            Converter(ElementTree(self.document)).convert(PptxBuilder(filename, REFERENCE_PPTX))
            return str(list(Presentation(str(filename)).slides)[-1].shapes.title.text)

    def test_chapter_heading(self):
        """Test that a slide gets the chapter heading as title, even if it is in a section within the chapter."""
        self.assertEqual("Chapter", self.slide_title(self.add_section(self.chapter, "2", "Section")))

    def test_section_heading_after_measure(self):
        """Test that a slide gets the heading of its section if a measure already used the chapter heading."""
        measure = SubElement(self.add_section(self.chapter, "2", "M01"), xmltags.MEASURE)
        SubElement(SubElement(measure, xmltags.PARAGRAPH), xmltags.MEASURE_TITLE).text = "M01: Measure"
        self.assertEqual("Section", self.slide_title(self.add_section(self.chapter, "2", "Section")))
