#!/bin/env python

"""Main program to convert Markdown files to different possible output formats."""

import datetime
import io
import json
import logging
import os
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
from markdown_converter import MarkdownConverter
from custom_types import JSON, Settings, Variables


def read_json(json_filename: str) -> JSON:
    """Read JSON from the specified filename."""
    with open(json_filename) as json_file:
        return json.load(json_file)


def write_xml(xml: ElementTree, settings: Settings) -> None:
    """Write the XML to the file specified in the settings."""
    markdown_filename = pathlib.Path(settings["InputFile"])
    xml_filename = pathlib.Path(settings["BuildPath"]) / markdown_filename.with_suffix(".xml").name
    xml.write(xml_filename, encoding="utf-8")


def convert(settings_filename: str, version: str) -> None:
    """Convert the input document to the specified output formats."""
    settings = cast(Settings, read_json(settings_filename))
    variables: Variables = {}
    for variable_file in settings["VariablesFiles"]:
        variables.update(cast(Variables, read_json(variable_file)))
    variables["VERSIE"] = settings["Version"] = version
    variables["DATUM"] = settings["Date"] = datetime.date.today().strftime('%d-%m-%Y')
    logging.info("Converting with settings:\n%s", pprint.pformat(settings))
    output_path = pathlib.Path(settings["OutputPath"])
    output_path.mkdir(parents=True, exist_ok=True)
    build_path = pathlib.Path(settings["BuildPath"])
    build_path.mkdir(parents=True, exist_ok=True)
    xml = MarkdownConverter(variables).convert(settings)
    write_xml(xml, settings)
    converter = Converter(xml)
    if "docx" in settings["OutputFormats"]:
        docx_output_filename = output_path / settings["OutputFormats"]["docx"]["OutputFile"]
        docx_builder = DocxBuilder(docx_output_filename, pathlib.Path(settings["DocxReferenceFile"]))
        converter.convert(docx_builder)
    if "pdf" in settings["OutputFormats"]:
        pdf_filename = output_path / settings["OutputFormats"]["pdf"]["OutputFile"]
        html_filename = build_path / pathlib.Path(settings["InputFile"]).with_suffix(".html").name
        html_builder = HTMLBuilder(html_filename)
        converter.convert(html_builder)
        html_cover_filename = build_path / pathlib.Path(settings["InputFile"]).with_suffix(".cover.html").name
        html_cover_builder = HTMLCoverBuilder(html_cover_filename)
        converter.convert(html_cover_builder)
        with open("DocumentDefinitions/Shared/header.html") as header_templete_file:
            header_contents = header_templete_file.read() % variables["KWALITEITSAANPAK"]
        header_filename = build_path / "header.html"
        with open(header_filename, "w") as header_file:
            header_file.write(header_contents)
        wkhtmltopdf = f"""docker-compose run wkhtmltopdf -c "wkhtmltopdf \
            --footer-html DocumentDefinitions/Shared/footer.html --footer-spacing 10 \
            --header-html {header_filename} --header-spacing 10 \
            --margin-bottom 27 --margin-left 34 --margin-right 34 --margin-top 27 \
            cover {html_cover_filename} \
            toc --xsl-style-sheet DocumentDefinitions/Shared/toc.xsl \
            {html_filename} {pdf_filename}" """
        os.system(wkhtmltopdf)
    if "xlsx" in settings["OutputFormats"]:
        xlsx_output_filename = output_path / settings["OutputFormats"]["xlsx"]["OutputFile"]
        xlsx_builder = XlsxBuilder(xlsx_output_filename)
        converter.convert(xlsx_builder)


def main(settings_filenames: List[str], version: str) -> None:
    """Convert the input documents specified in the list of JSON settings files."""
    for settings_filename in settings_filenames:
        convert(settings_filename, version)


if __name__ == "__main__":
    args = parse_cli_arguments()
    logging.basicConfig(level=getattr(logging, args.log))
    main(args.settings, args.version)
