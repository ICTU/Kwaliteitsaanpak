"""Types."""

from typing import Any, Literal, NewType


JSON = NewType("JSON", dict[str, Any])
Settings = NewType("Settings", dict[str, Any])
Variables = NewType("Variables", dict[str, Any])

type OutputFormat = Literal["docx", "html", "json", "pptx", "xlsx", "zip"]
type TreeBuilderAttributes = dict[str, str]
