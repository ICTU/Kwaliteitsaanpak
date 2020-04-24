"""Main program to convert Markdown files to different possible output formats."""

import io
import json
import logging
import pathlib
import pprint
import sys
from typing import List
from xml.dom.minidom import parseString
from xml.etree.ElementTree import ElementTree

from cli import parse_cli_arguments
from markdown_converter import MarkdownConverter
from custom_types import Settings


def read_settings(settings_filename: str) -> Settings:
    """Read the settings from the specified filename."""
    with open(settings_filename) as settings_file:
        return json.load(settings_file)


def read_markdown(settings: Settings) -> List[str]:
    """Read the Markdown file and return the contents."""
    markdown_filename = pathlib.Path(settings["InputFile"])
    with open(markdown_filename) as markdown_file:
        return markdown_file.readlines()


def write_xml(xml: ElementTree, settings: Settings) -> None:
    """Write the XML to the file specified in the settings."""
    markdown_filename = pathlib.Path(settings["InputFile"])
    #xml_filename = pathlib.Path(settings["BuildPath"]) / markdown_filename.with_suffix(".xml")
    xml_filename = markdown_filename.with_suffix(".xml")
    xml_string = io.StringIO()
    xml.write(xml_string, encoding="unicode")
    with open(xml_filename, "w") as xml_file:
        xml_file.write(parseString(xml_string.getvalue()).toprettyxml(indent="    "))


def main(settings_filename: str) -> None:
    """Convert the input document to the specified output formats."""
    settings = read_settings(settings_filename)
    logging.info("Converting with settings:\n%s", pprint.pformat(settings))
    markdown = read_markdown(settings)
    xml = MarkdownConverter().convert(markdown, settings)
    write_xml(xml, settings)


if __name__ == "__main__":
    args = parse_cli_arguments()
    logging.basicConfig(level=getattr(logging, args.log))
    main(args.settings)
