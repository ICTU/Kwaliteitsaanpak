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
from builder import DocxBuilder, HTMLBuilder, HTMLContentBuilder, HTMLCoverBuilder, PptxBuilder, XlsxBuilder
from markdown_converter import MarkdownConverter
from markdown_syntax import VARIABLE_USE_PATTERN
from custom_types import JSON, Settings, Variables


def convert(settings_filename: str, version: str) -> None:
    """Convert the input document to the specified output formats."""
    # pylint: disable=unsubscriptable-object,unsupported-assignment-operation
    variables = read_variables(settings_filename, version)
    settings = read_settings(settings_filename, variables)
    logging.info("Converting with settings:\n%s", pprint.pformat(settings))
    get_build_path(settings)
    xml = MarkdownConverter(variables).convert(settings)
    write_xml(xml, settings)
    converter = Converter(xml)
    if "docx" in settings["OutputFormats"]:
        convert_docx(converter, settings)
    if "pdf" in settings["OutputFormats"]:
        copy_files(settings, "pdf")
        convert_pdf(converter, settings, variables)
    if "pptx" in settings["OutputFormats"]:
        convert_pptx(converter, settings)
    if "xlsx" in settings["OutputFormats"]:
        convert_xlsx(converter, settings)
    if "html" in settings["OutputFormats"]:
        copy_files(settings, "html")
        convert_html(converter, settings)


def read_variables(settings_filename: str, version: str) -> dict:
    """Read the variables."""
    settings = cast(Settings, read_json(settings_filename))
    variables = cast(Variables, {})
    for variable_file in settings["VariablesFiles"]:
        variables.update(cast(Variables, read_json(variable_file)))
    variables["VERSIE"] = version if version == "wip" else f"v{version}"
    variables["VERSIE_ZONDER_V"] = version
    variables["DATUM"] = datetime.date.today().strftime("%d-%m-%Y")
    return variables


def read_settings(settings_filename: str, variables: Variables) -> dict:
    """Read the settings."""
    settings = read_json(settings_filename, variables)
    settings["Version"] = variables["VERSIE"]
    settings["Date"] = variables["DATUM"]
    return settings


def read_json(json_filename: str, variables: Variables | None = None) -> JSON:
    """Read JSON from the specified filename."""
    variables = variables or {}
    with open(json_filename, encoding="utf-8") as json_file:
        json_text = re.sub(
            VARIABLE_USE_PATTERN,
            lambda variable: variables.get(variable.group(1), variable.group(0)),
            json_file.read()
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


def convert_pdf(converter, settings: Settings, variables: Variables) -> None:
    """Convert the XML to PDF."""
    build_path = get_build_path(settings)
    html_filename = build_path / pathlib.Path(settings["InputFile"]).with_suffix(".html").name
    html_builder = HTMLContentBuilder(html_filename, build_path)
    converter.convert(html_builder)
    html_cover_filename = build_path / pathlib.Path(settings["InputFile"]).with_suffix(".cover.html").name
    html_cover_builder = HTMLCoverBuilder(html_cover_filename, build_path)
    converter.convert(html_cover_builder)
    with open("DocumentDefinitions/Shared/header.html", encoding="utf-8") as header_template_file:
        header_contents = header_template_file.read() % variables["KWALITEITSAANPAK"]
    header_filename = build_path / "header.html"
    with open(header_filename, mode="w", encoding="utf-8") as header_file:
        header_file.write(header_contents)
    pdf_build_filename = build_path / pathlib.Path(settings["OutputFormats"]["pdf"]["OutputFile"])
    os.system(
        f"""wkhtmltopdf \
        --enable-local-file-access \
        --footer-html DocumentDefinitions/Shared/footer.html --footer-spacing 10 \
        --header-html {header_filename} --header-spacing 10 \
        --margin-bottom 27 --margin-left 34 --margin-right 34 --margin-top 27 \
        --title '{settings["Title"]}' \
        cover {html_cover_filename} \
        {"toc --xsl-style-sheet DocumentDefinitions/Shared/toc.xsl" if settings["IncludeTableOfContents"] else ""} \
        {html_filename} {pdf_build_filename}"""
    )
    pdf_build_filename2 = build_path / pathlib.Path(settings["OutputFormats"]["pdf"]["OutputFile"] + ".step2")
    os.system(f"gs -o {pdf_build_filename2} -sDEVICE=pdfwrite -dPrinted=false -f {pdf_build_filename} src/pdfmark.txt")
    copy_output(pdf_build_filename2, settings, "pdf")


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
    pptx_builder = PptxBuilder(pptx_build_filename, pathlib.Path(settings["OutputFormats"]["pptx"]["ReferenceFile"]))
    converter.convert(pptx_builder)
    copy_output(pptx_build_filename, settings, "pptx")


def convert_xlsx(converter, settings: Settings) -> None:
    """Convert the XML to xlsx."""
    build_path = get_build_path(settings)
    xlsx_build_filename = build_path / settings["OutputFormats"]["xlsx"]["OutputFile"]
    xlsx_builder = XlsxBuilder(xlsx_build_filename)
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
