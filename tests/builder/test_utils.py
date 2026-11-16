"""Utility function unit tests."""

import unittest

from builder.utils import slugify


class SlugifyTest(unittest.TestCase):
    """Unit tests for the slugify function."""

    def test_text(self):
        """Test that the text is lowercased and that non-alphanumeric characters are replaced by a single dash."""
        self.assertEqual("terminologie-en-afkortingen", slugify("Terminologie en afkortingen"))

    def test_leading_and_trailing_dashes(self):
        """Test that leading and trailing non-alphanumeric characters are removed."""
        self.assertEqual("bronnen", slugify(" (Bronnen) "))

    def test_measure(self):
        """Test that the slug of a measure title is the measure id."""
        self.assertEqual("m01", slugify("M01: Het project ontvangt en levert in elke fase vastgestelde producten"))
