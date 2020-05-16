"""Utility functions."""


def slugify(text: str) -> str:
    """Slugify a text."""
    slug = ""
    for char in text:
        if char.isalnum():
            slug += char
        elif not slug.endswith("-"):
            slug += "-"
    return slug.strip("-").lower()
