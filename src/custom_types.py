"""Types."""

from typing import Any, NewType


JSON = NewType("JSON", dict[str, Any])
Settings = NewType("Settings", dict[str, Any])
TreeBuilderAttributes = dict[bytes | str, bytes | str]
Variables = NewType("Variables", dict[str, Any])
