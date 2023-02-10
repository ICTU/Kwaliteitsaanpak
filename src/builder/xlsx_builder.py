"""Self-assessment XLSX-spreadsheet builder."""

import datetime
import pathlib
import re
from typing import Dict, List, Optional

import xlsxwriter

import xmltags
from custom_types import TreeBuilderAttributes
from .builder import Builder


class XlsxBuilder(Builder):  # pylint: disable=too-many-instance-attributes
    """Self-assessment builder."""

    MEASURE_ID_COLUMN, MEASURE_COLUMN, STATUS_COLUMN, EXPLANATION_COLUMN = range(4)
    HEADER_ROW = 4
    MEASURE_START_ROW = HEADER_ROW + 1

    def __init__(self, filename: pathlib.Path) -> None:
        super().__init__(filename)
        filename.unlink(missing_ok=True)
        self.workbook = xlsxwriter.Workbook(filename)
        self.formats = self.__create_formats(self.workbook)
        self.checklist = self.workbook.add_worksheet("Self-assessment checklist")
        self.row = self.measure_row = self.MEASURE_START_ROW
        self.last_level_1_section_heading = ""
        self.measure_id: Optional[str] = None
        self.measure_text: List[str] = []

    @staticmethod
    def __create_formats(workbook: xlsxwriter.Workbook) -> Dict[str, xlsxwriter.format.Format]:
        """Create the formats."""
        measure_format_options = dict(bg_color="#BCD2EE", text_wrap=True, valign="top")
        status_format_options = dict(bg_color="#FED32D", text_wrap=True)
        return {
            "header": workbook.add_format(dict(text_wrap=True, font_size=14, bold=True, bg_color="#B3D6C9")),
            "instructions": workbook.add_format(dict(text_wrap=True, font_size=13, bg_color="#B3D6C9")),
            "measure": workbook.add_format(measure_format_options),
            "submeasure": workbook.add_format(dict(align="vjustify", indent=1, **measure_format_options)),
            "explanation": workbook.add_format(dict(bg_color="#FFFFA5", text_wrap=True)),
            "status": workbook.add_format(status_format_options),
            "substatus": workbook.add_format(dict(indent=1, **status_format_options)),
            "voldoet": workbook.add_format(dict(fg_color="#0B5101", bg_color="#BBEDC3")),
            "voldoet deels": workbook.add_format(dict(fg_color="#894503", bg_color="#FEE88A")),
            "voldoet niet": workbook.add_format(dict(fg_color="#880009", bg_color="#FEB8C3")),
            "niet van toepassing": workbook.add_format(dict(fg_color="#6D6D6D", bg_color="#EFEFEF")),
        }

    def start_element(self, tag: str, attributes: TreeBuilderAttributes) -> None:
        super().start_element(tag, attributes)
        if tag == xmltags.DOCUMENT:
            self.__create_checklist(str(attributes["version"]))
        elif tag == xmltags.MEASURE and not self.in_element(xmltags.SECTION, {xmltags.SECTION_IS_APPENDIX: "y"}):
            if self.last_level_1_section_heading:
                self.row += 1
                self.checklist.merge_range(
                    f"A{self.row}:D{self.row}",
                    self.last_level_1_section_heading,
                    self.formats["header"],
                )
                self.last_level_1_section_heading = ""
        elif self.measure_text:
            if tag == xmltags.LIST_ITEM:
                prefix = (
                    f"{str(attributes[xmltags.LIST_ITEM_NUMBER])}. "
                    if xmltags.LIST_ITEM_NUMBER in attributes
                    else "- "
                )
                self.measure_text.append(prefix)
            elif tag == xmltags.TABLE_CELL:
                self.measure_text.append("")  # Add empty string in case the cell is empty and text() is never called

    def text(self, tag: str, text: str, attributes: TreeBuilderAttributes) -> None:
        text = re.sub("[¹²³⁴⁵⁶⁷⁸⁹⁰]+", "", text)  # Remove footnotes
        if tag == xmltags.HEADING and self.nr_elements(xmltags.SECTION) == 1:
            self.last_level_1_section_heading = text
        elif self.in_element(xmltags.MEASURE) and not self.in_element(
            xmltags.SECTION, {xmltags.SECTION_IS_APPENDIX: "y"}
        ):
            if tag == xmltags.BOLD:
                self.measure_row = self.row
                self.measure_id, measure_title = text.split(":")
                has_submeasures = self.in_element(xmltags.MEASURE, dict(composite="true"))
                self.__write_measure(self.measure_id, measure_title.strip(), has_submeasures=has_submeasures)
            self.measure_text.append(text)
        elif self.measure_text:
            if (
                tag == xmltags.LIST_ITEM
                and xmltags.LIST_ITEM_NUMBER in attributes
                and self.measure_id in ("M01", "M02", "M05", "M07", "M16", "M31", "M32", "M34")
            ):
                self.row += 1
                self.__write_measure("", f"{str(attributes[xmltags.LIST_ITEM_NUMBER])}. {text}", submeasure=True)
            if tag == xmltags.TABLE_CELL and self.measure_id == "M01":
                # The unicode check symbol is wider than other characters, messing up the table layout:
                text = text.replace("✔", "x")
                column, row = int(attributes[xmltags.TABLE_CELL_COLUMN]), int(attributes[xmltags.TABLE_CELL_ROW])
                if row > 0 and column == 0:  # Table cell with a document
                    self.row += 1
                    # Write the document as (sub)measure
                    self.__write_measure("", f"{row}. {text}", submeasure=True)
                text += " " * (int(attributes[xmltags.TABLE_CELL_WIDTH]) - len(text))
            self.measure_text.append(text)

    def __write_measure(
        self, measure_id, measure_text, submeasure: bool = False, has_submeasures: bool = False
    ) -> None:
        """Write a measure row."""
        measure_format_key = "submeasure" if submeasure else "measure"
        self.checklist.write(self.row, self.MEASURE_ID_COLUMN, measure_id, self.formats[measure_format_key])
        self.checklist.write(self.row, self.MEASURE_COLUMN, measure_text, self.formats[measure_format_key])
        if has_submeasures:
            self.checklist.write(self.row, self.STATUS_COLUMN, "", self.formats[measure_format_key])
            self.checklist.write_comment(self.row, self.STATUS_COLUMN, "Bepaal a.u.b. de status per submaatregel")
        else:
            status_format_key = "substatus" if submeasure else "status"
            self.checklist.write(self.row, self.STATUS_COLUMN, "", self.formats[status_format_key])
            self.__write_assessment_choices(self.row, self.STATUS_COLUMN)
        self.checklist.write(self.row, self.EXPLANATION_COLUMN, "", self.formats["explanation"])

    def end_element(self, tag: str, attributes: TreeBuilderAttributes) -> None:
        super().end_element(tag, attributes)
        if tag == xmltags.DOCUMENT:
            self.__finish_checklist()
        elif tag == xmltags.SECTION and self.measure_text and self.nr_elements(xmltags.SECTION) == 1:
            self.checklist.write_comment(
                self.measure_row,
                self.MEASURE_COLUMN,
                "".join(self.measure_text),
                dict(x_scale=7, y_scale=8, font_name="Courier", font_size=9),
            )
            self.measure_text = []
            self.row += 1
        elif self.measure_text:
            if tag in (
                xmltags.LIST_ITEM,
                xmltags.BULLET_LIST,
                xmltags.NUMBERED_LIST,
                xmltags.TABLE_HEADER_ROW,
                xmltags.TABLE_ROW,
                xmltags.TABLE,
            ):
                self.measure_text.append("\n")
            elif tag == xmltags.TABLE_CELL:
                if not self.measure_text[-1]:
                    self.measure_text.append(" " * int(attributes[xmltags.TABLE_CELL_WIDTH]))
                self.measure_text.append(" ")
            elif tag in (xmltags.PARAGRAPH, xmltags.HEADING):
                self.measure_text.append("\n\n")

    def end_document(self) -> None:
        self.__create_action_list()
        self.workbook.close()

    def __create_checklist(self, version: str) -> None:
        self.checklist.merge_range(
            "A1:D1",
            "Onderstaande checklist kan gebruikt worden voor het uitvoeren van een assessment tegen de ICTU "
            f"Kwaliteitsaanpak Softwareontwikkeling versie {version}, {datetime.date.today().strftime('%d-%m-%Y')}.",
            self.formats["header"],
        )
        self.checklist.set_row(0, 30)
        self.checklist.merge_range(
            "A2:D2",
            "Gebruik de 'Status' kolom om aan te geven in hoeverre een maatregel uit de Kwaliteitsaanpak is toegepast. "
            "Bij maatregelen met submaatregelen hoeft alleen de status van de submaatregelen te worden ingevuld.",
            self.formats["instructions"],
        )
        self.checklist.set_row(1, 40)
        self.checklist.merge_range(
            "A3:D3",
            "Bij maatregelen die primair door een project moeten worden toegepast geeft de status aan in hoevere het "
            "project dat doet. Bij maatregelen die primair door ICTU moeten worden toegepast geeft de status aan in "
            "hoeverre ICTU dat doet, gezien vanuit het perspectief van het project.",
            self.formats["instructions"],
        )
        self.checklist.set_row(2, 40)
        self.checklist.merge_range(
            "A4:D4",
            "Gebruik 'niet van toepassing' alleen voor maatregelen die permanent niet van toepassing zijn. "
            "Bijvoorbeeld, als er geen due diligence wordt uitgevoerd is M32 niet van toepassing. "
            "Gebruik 'voldoet niet' als een maatregel nog niet is toegepast, maar wel nodig is. Bijvoorbeeld, als "
            "de performancetesten nog moeten worden opgezet is de status van M07.5 'voldoet niet'.",
            self.formats["instructions"],
        )
        self.checklist.set_row(3, 40)
        self.checklist.set_row(self.HEADER_ROW, 30)
        for column, (header, width) in enumerate(
            [("Maatregel", 12), ("Omschrijving", 70), ("Status", 20), ("Toelichting", 70)]
        ):
            self.checklist.write(self.HEADER_ROW, column, header, self.formats["header"])
            self.checklist.set_column(f"{'ABCD'[column]}:{'ABCD'[column]}", width)

    def __finish_checklist(self) -> None:
        """Wrap up the checklist."""
        self.checklist.freeze_panes(self.MEASURE_START_ROW, 0)

    def __write_assessment_choices(self, row: int, column: int) -> None:
        """Write the assessment choices, colors and data validation in the status column."""
        assessment_choices = ["voldoet", "voldoet deels", "voldoet niet", "niet van toepassing"]
        for choice in assessment_choices:
            self.checklist.conditional_format(
                row,
                column,
                row,
                column,
                {"type": "cell", "criteria": "==", "value": f'"{choice}"', "format": self.formats[choice]},
            )
        self.checklist.data_validation(row, column, row, column, dict(validate="list", source=assessment_choices))

    def __create_action_list(self) -> None:
        """Create a worksheet with room for actions from the self-assessment."""
        action_list = self.workbook.add_worksheet("Self-assessment verbeteracties")
        action_list.merge_range(
            "A1:D1",
            "Onderstaande actielijst kan gebruikt worden om acties n.a.v. de self-assessment bij te houden.",
            self.formats["header"],
        )
        action_list.set_row(0, 30)
        action_list.set_row(1, 30)
        for column, (header, width) in enumerate([("Datum", 12), ("Actie", 70), ("Status", 20), ("Toelichting", 70)]):
            action_list.write(1, column, header, self.formats["header"])
            action_list.set_column(f"{'ABCD'[column]}:{'ABCD'[column]}", width)
