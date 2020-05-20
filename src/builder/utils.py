"""Utility functions."""

from typing import cast
import re


def slugify(text: str) -> str:
    """Slugify a text."""
    if match := re.match(r"(M\d+): ", text):
        match = cast(re.Match, match)
        return match.group(1).lower()
    slug = ""
    for char in text:
        if char.isalnum():
            slug += char
        elif not slug.endswith("-"):
            slug += "-"
    return slug.strip("-").lower()
