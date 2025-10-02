"""JSON Builders."""

import json
import pathlib
from uuid import uuid4

from custom_types import TreeBuilderAttributes
import xmltags

from .builder import Builder


class JSONBuilder(Builder):
    """Builder to create a Quality-time compliance report in JSON format."""

    def __init__(self, filename: pathlib.Path) -> None:
        super().__init__(filename)
        self.json: dict = {"subjects": {}}
        self.heading_level: list[int] = []  # Heading level stack
        self.section_has_measures = False
        self.current_measure = ""

    def accept_element(self, tag: str, attributes: TreeBuilderAttributes) -> bool:
        """Return whether the builder accepts the element."""
        return attributes.get(xmltags.SECTION_IS_APPENDIX) != "y"

    def start_element(self, tag: str, attributes: TreeBuilderAttributes) -> None:
        super().start_element(tag, attributes)
        match tag:
            case xmltags.DOCUMENT:
                version = attributes["version"]
                self.json["title"] = f"{attributes['title']} versie {version}"
                self.json["subtitle"] = "Checklist"
                self.json["report_uuid"] = f"ictu_ka_checklist_{version.replace('.', '_')}"
            case xmltags.SECTION:
                self.heading_level.append(int(attributes[xmltags.SECTION_LEVEL]))
                if self.heading_level[-1] == 1:
                    self.section_has_measures = False
            case xmltags.MEASURE:
                self.section_has_measures = True

    def text(self, tag: str, text: str, attributes: TreeBuilderAttributes) -> None:
        """Element text."""
        match tag:
            case xmltags.HEADING:
                if self.heading_level[-1] == 1:
                    self.add_subject(text)
            case xmltags.MEASURE_TITLE:
                self.current_measure = text
                if not self.in_element(xmltags.MEASURE, {"composite": "true"}):
                    self.add_metric(text)
            case xmltags.SUBMEASURE_TITLE:
                self.add_metric(self.current_measure, f"{attributes[xmltags.SUBMEASURE_TITLE_NUMBER]}. {text}")

    def add_subject(self, text: str) -> None:
        """Add a subject to the JSON."""
        self.subject_id = str(uuid4())
        self.json["subjects"][self.subject_id] = {"type": "software", "name": text, "metrics": {}}

    def add_metric(self, name: str, secondary_name: str = "") -> None:
        """Add a metric to the JSON."""
        self.json["subjects"][self.subject_id]["metrics"][str(uuid4())] = {
            "type": "compliance",
            "name": name,
            "secondary_name": secondary_name,
            "sources": {str(uuid4()): {"type": "manual_number", "parameters": {}}},
            "target": "100",
            "near_target": "80",
        }

    def end_element(self, tag: str, attributes: TreeBuilderAttributes) -> None:
        super().end_element(tag, attributes)
        match tag:
            case xmltags.SECTION:
                if self.heading_level[-1] == 1 and not self.section_has_measures:
                    del self.json["subjects"][self.subject_id]
                self.heading_level.pop()

    def end_document(self) -> None:
        """End the document and save it."""
        with open(self.filename, "w") as fd:
            json.dump(self.json, fd, indent=4)
