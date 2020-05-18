"""Main program to convert Markdown files to different possible output formats."""

import datetime
import io
import json
import logging
import pathlib
import pprint
import sys
from typing import cast, List
from xml.etree.ElementTree import ElementTree

from cli import parse_cli_arguments
from converter import Converter
from docx_builder import DocxBuilder
from html_builder import HTMLBuilder, HTMLCoverBuilder
from xlsx_builder import XlsxBuilder
from markdown_builder import MarkdownBuilder
from markdown_converter import MarkdownConverter
from custom_types import JSON, Settings, Variables


def read_json(json_filename: str) -> JSON:
    """Read JSON from the specified filename."""
    with open(json_filename) as json_file:
        return json.load(json_file)


def read_markdown(settings: Settings) -> List[str]:
    """Read the Markdown file and return the contents."""
    markdown_filename = pathlib.Path(settings["InputFile"])
    with open(markdown_filename) as markdown_file:
        return markdown_file.readlines()


def write_xml(xml: ElementTree, settings: Settings) -> None:
    """Write the XML to the file specified in the settings."""
    markdown_filename = pathlib.Path(settings["InputFile"])
    xml_filename = pathlib.Path(settings["BuildPath"]) / markdown_filename.with_suffix(".xml").name
    xml.write(xml_filename, encoding="utf-8")


def main(settings_filename: str, version: str) -> None:
    """Convert the input document to the specified output formats."""
    settings = cast(Settings, read_json(settings_filename))
    variables: Variables = {}
    for variable_file in settings["VariablesFiles"]:
        variables.update(cast(Variables, read_json(variable_file)))
    variables["VERSIE"] = settings["Version"] = version
    variables["DATUM"] = settings["Date"] = datetime.date.today().strftime('%d-%m-%Y')
    logging.info("Converting with settings:\n%s", pprint.pformat(settings))
    markdown = read_markdown(settings)
    xml = MarkdownConverter(variables).convert(markdown, settings)
    write_xml(xml, settings)
    converter = Converter(xml)
    if "md" in settings["OutputFormats"]:
        output_path = pathlib.Path(settings["OutputFormats"]["md"]["OutputPath"])
        markdown_output_filename = output_path / pathlib.Path(settings["InputFile"]).with_suffix(".md").name
        markdown_builder = MarkdownBuilder(markdown_output_filename)
        converter.convert(markdown_builder)
    if "docx" in settings["OutputFormats"]:
        output_path = pathlib.Path(settings["OutputFormats"]["docx"]["OutputPath"])
        docx_output_filename = output_path / pathlib.Path(settings["InputFile"]).with_suffix(".docx").name
        docx_builder = DocxBuilder(docx_output_filename, pathlib.Path(settings["DocxReferenceFile"]))
        converter.convert(docx_builder)
    if "html" in settings["OutputFormats"]:
        output_path = pathlib.Path(settings["OutputFormats"]["html"]["OutputPath"])
        html_filename = output_path / pathlib.Path(settings["InputFile"]).with_suffix(".html").name
        html_builder = HTMLBuilder(html_filename)
        converter.convert(html_builder)
        html_cover_filename = output_path / pathlib.Path(settings["InputFile"]).with_suffix(".cover.html").name
        html_cover_builder = HTMLCoverBuilder(html_cover_filename)
        converter.convert(html_cover_builder)
    if "xlsx" in settings["OutputFormats"]:
        output_path = pathlib.Path(settings["OutputFormats"]["xlsx"]["OutputPath"])
        xlsx_filename = output_path / pathlib.Path(settings["InputFile"]).with_suffix(".xlsx").name
        xlsx_builder = XlsxBuilder(xlsx_filename)
        converter.convert(xlsx_builder)


if __name__ == "__main__":
    args = parse_cli_arguments()
    logging.basicConfig(level=getattr(logging, args.log))
    main(args.settings, args.version)
