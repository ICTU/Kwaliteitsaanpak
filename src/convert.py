#!/bin/env python

"""Main program to convert Markdown files to different possible output formats."""

import datetime
import json
import logging
import os
import pathlib
import pprint
import re
import shutil
from typing import cast, List
from xml.etree.ElementTree import ElementTree

from cli import parse_cli_arguments
from converter import Converter
from builder import xlsx_builder as xlsx_builder_module
from builder.docx_builder import DocxBuilder
from builder.html_builder import HTMLBuilder
from builder.pptx_builder import PptxBuilder
from markdown_converter import MarkdownConverter
from markdown_syntax import VARIABLE_USE_PATTERN
from custom_types import JSON, Settings, Variables


def convert(settings_filename: str, version: str) -> None:
    """Convert the input document to the specified output formats."""
    variables = read_variables(settings_filename, version)
    settings = read_settings(settings_filename, variables)
    logging.info("Converting with settings:\n%s", pprint.pformat(settings))
    get_build_path(settings)
    xml = MarkdownConverter(variables).convert(settings)
    write_xml(xml, settings)
    converter = Converter(xml)
    if "docx" in settings["OutputFormats"]:
        convert_docx(converter, settings)
    if "pptx" in settings["OutputFormats"]:
        convert_pptx(converter, settings)
    if "xlsx" in settings["OutputFormats"]:
        convert_xlsx(converter, settings)
    if "html" in settings["OutputFormats"]:
        copy_files(settings, "html")
        convert_html(converter, settings)


def read_variables(settings_filename: str, version: str) -> Variables:
    """Read the variables."""
    settings = cast(Settings, read_json(settings_filename))
    variables = cast(Variables, {})
    for variable_file in settings["VariablesFiles"]:
        variables.update(cast(Variables, read_json(variable_file)))
    variables["VERSIE"] = version if version == "wip" else f"v{version}"
    variables["VERSIE_ZONDER_V"] = version
    variables["DATUM"] = datetime.date.today().strftime("%d-%m-%Y")
    return variables


def read_settings(settings_filename: str, variables: Variables) -> Settings:
    """Read the settings."""
    settings = read_json(settings_filename, variables)
    settings["Version"] = variables["VERSIE"]
    settings["Date"] = variables["DATUM"]
    return cast(Settings, settings)


def read_json(json_filename: str, variables: Variables | None = None) -> JSON:
    """Read JSON from the specified filename."""
    variables = variables or cast(Variables, {})
    with open(json_filename, encoding="utf-8") as json_file:
        json_text = re.sub(
            VARIABLE_USE_PATTERN,
            lambda variable: variables.get(variable.group(1), variable.group(0)),
            json_file.read(),
        )
        return JSON(json.loads(json_text))


def write_xml(xml: ElementTree, settings: Settings) -> None:
    """Write the XML to the file specified in the settings."""
    markdown_filename = pathlib.Path(str(settings["InputFile"]))
    xml_filename = get_build_path(settings) / markdown_filename.with_suffix(".xml").name
    xml.write(str(xml_filename), encoding="utf-8")


def copy_files(settings: Settings, output_format: str) -> None:
    """Copy specified source files (e.g. CSS files) to the specified destinations."""
    for file_to_copy in settings["OutputFormats"][output_format].get("CopyFiles", []):
        source_path = pathlib.Path(file_to_copy["from"])
        destination_paths = [pathlib.Path(path) for path in file_to_copy["to"]]
        for destination_path in destination_paths:
            shutil.copy(source_path, destination_path)


def convert_html(converter, settings: Settings) -> None:
    """Convert the XML to HTML."""
    build_path = get_build_path(settings)
    html_build_filename = build_path / settings["OutputFormats"]["html"]["OutputFile"]
    html_builder = HTMLBuilder(html_build_filename, pathlib.Path(""))
    converter.convert(html_builder)
    copy_output(html_build_filename, settings, "html")


def convert_docx(converter, settings: Settings) -> None:
    """Convert the XML to docx."""
    build_path = get_build_path(settings)
    docx_build_filename = build_path / settings["OutputFormats"]["docx"]["OutputFile"]
    docx_builder = DocxBuilder(
        docx_build_filename,
        pathlib.Path(settings["OutputFormats"]["docx"]["ReferenceFile"]),
        pathlib.Path("Content/Images"),
    )
    converter.convert(docx_builder)
    copy_output(docx_build_filename, settings, "docx")


def convert_pptx(converter, settings: Settings) -> None:
    """Convert the XML to pptx."""
    build_path = get_build_path(settings)
    pptx_build_filename = build_path / settings["OutputFormats"]["pptx"]["OutputFile"]
    pptx_builder = PptxBuilder(
        pptx_build_filename,
        pathlib.Path(settings["OutputFormats"]["pptx"]["ReferenceFile"]),
    )
    converter.convert(pptx_builder)
    copy_output(pptx_build_filename, settings, "pptx")


def convert_xlsx(converter, settings: Settings) -> None:
    """Convert the XML to xlsx."""
    build_path = get_build_path(settings)
    xlsx_build_filename = build_path / settings["OutputFormats"]["xlsx"]["OutputFile"]
    xlsx_builder_class_name = settings["OutputFormats"]["xlsx"]["BuilderClass"]
    xlsx_builder = getattr(xlsx_builder_module, xlsx_builder_class_name)(xlsx_build_filename)
    converter.convert(xlsx_builder)
    copy_output(xlsx_build_filename, settings, "xlsx")


def copy_output(build_filename: pathlib.Path, settings: Settings, output_format: str):
    """Copy the build file to the output paths."""
    output_settings = settings["OutputFormats"][output_format]
    output_paths = [pathlib.Path(output_path) for output_path in output_settings["OutputPaths"]]
    for output_path in output_paths:
        output_path.mkdir(parents=True, exist_ok=True)
        output_filename = output_path / output_settings["OutputFile"]
        shutil.copy(build_filename, output_filename)


def get_build_path(settings: Settings) -> pathlib.Path:
    """Return, and create if necessary, the build path from the settings."""
    return get_path(settings, "BuildPath")


def get_path(settings: Settings, pathname: str) -> pathlib.Path:
    """Return, and create if necessary, the specified path from the settings."""
    path = pathlib.Path(settings[pathname])
    path.mkdir(parents=True, exist_ok=True)
    return path


def main(settings_filenames: List[str], version: str) -> None:
    """Convert the input documents specified in the list of JSON settings files."""
    for settings_filename in settings_filenames:
        convert(settings_filename, version)


if __name__ == "__main__":
    args = parse_cli_arguments()
    logging.basicConfig(level=getattr(logging, args.log))
    main(args.settings, os.getenv("VERSION") or args.version)
