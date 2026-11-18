"""Diagram unit tests."""

import pathlib
import tempfile
import unittest
from unittest.mock import patch

from diagram import DiagramError, render_mermaid

MERMAID = """flowchart TD
    accTitle: Title
    accDescr: Description
    A --> B
"""


class RenderMermaidTest(unittest.TestCase):
    """Unit tests for rendering Mermaid diagrams."""

    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.cache_folder = pathlib.Path(self.temporary_directory.name) / "diagrams"

    def tearDown(self):
        self.temporary_directory.cleanup()

    def test_render(self):
        """Test that the diagram is rendered as SVG and PNG."""
        diagram = render_mermaid(MERMAID, self.cache_folder)
        self.assertTrue(diagram.svg_path.read_text().startswith("<svg"))
        self.assertTrue(diagram.png_path.read_bytes().startswith(b"\x89PNG"))
        self.assertGreater(diagram.width_cm(), 0)

    def test_colors_resolved(self):
        """Test that CSS variables are replaced by colors, because resvg does not support CSS variables."""
        self.assertNotIn("var(", render_mermaid(MERMAID, self.cache_folder).svg_path.read_text())

    def test_title_and_description(self):
        """Test that the accessible title and description of the diagram are available."""
        diagram = render_mermaid(MERMAID, self.cache_folder)
        self.assertEqual("Title", diagram.title())
        self.assertEqual("Description", diagram.description())

    def test_missing_title_and_description(self):
        """Test that the title and description are empty if the diagram has none."""
        diagram = render_mermaid("flowchart TD\n    A --> B\n", self.cache_folder)
        self.assertEqual("", diagram.title())
        self.assertEqual("", diagram.description())

    def test_cache(self):
        """Test that a diagram that was rendered before is not rendered again."""
        diagram = render_mermaid(MERMAID, self.cache_folder)
        with patch("diagram.subprocess.run") as run:
            self.assertEqual(diagram, render_mermaid(MERMAID, self.cache_folder))
        run.assert_not_called()

    def test_changed_diagram(self):
        """Test that a changed diagram is rendered again."""
        diagram = render_mermaid(MERMAID, self.cache_folder)
        self.assertNotEqual(diagram, render_mermaid(MERMAID + "    B --> C\n", self.cache_folder))

    def test_invalid_diagram(self):
        """Test that an invalid diagram results in an error message that shows the diagram and the error."""
        with self.assertRaises(DiagramError) as context:
            render_mermaid("flowchart TD\n    A[[[ --\n", self.cache_folder)
        self.assertIn("A[[[ --", str(context.exception))
        self.assertIn("line 2", str(context.exception))
