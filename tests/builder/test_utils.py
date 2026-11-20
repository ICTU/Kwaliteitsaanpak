"""Builder utility unit tests."""

import unittest

from builder.utils import slugify


class SlugifyTest(unittest.TestCase):
    """Unit tests for slugify, used for the ids of headings that the table of contents links to."""

    def test_text(self):
        """Test that a text is lower cased and that spaces become dashes."""
        self.assertEqual("versie-5-5-0", slugify("Versie 5.5.0"))

    def test_consecutive_special_characters(self):
        """Test that consecutive special characters become one dash and that leading and trailing dashes are removed."""
        self.assertEqual("risico-s-en-maatregelen", slugify("(Risico's en maatregelen)"))

    def test_measure(self):
        """Test that the slug of a measure title is the measure number."""
        self.assertEqual("m26", slugify("M26: Het project laat de beveiliging van het ontwikkelde product beoordelen"))
