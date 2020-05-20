"""Types."""

from typing import Any, Dict, NewType, Union


JSON = NewType("JSON", Dict[str, Any])
Settings = NewType("Settings", Dict[str, Any])
TreeBuilderAttributes = Dict[Union[bytes, str], Union[bytes, str]]
Variables = NewType("Variables", Dict[str, Any])
