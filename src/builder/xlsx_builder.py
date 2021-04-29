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
    HEADER_ROW = 1
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
                    "A{row}:D{row}".format(row=self.row),
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
                self.__write_measure(self.measure_id, measure_title.strip())
            self.measure_text.append(text)
        elif self.measure_text:
            if (
                tag == xmltags.LIST_ITEM
                and xmltags.LIST_ITEM_NUMBER in attributes
                and self.measure_id in ("M05", "M07", "M16", "M31")
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

    def __write_measure(self, measure_id, measure_text, submeasure: bool = False) -> None:
        """Write a measure row."""
        measure_format_key = "submeasure" if submeasure else "measure"
        status_format_key = "substatus" if submeasure else "status"
        self.checklist.write(self.row, self.MEASURE_ID_COLUMN, measure_id, self.formats[measure_format_key])
        self.checklist.write(self.row, self.MEASURE_COLUMN, measure_text, self.formats[measure_format_key])
        self.checklist.write(self.row, self.STATUS_COLUMN, "", self.formats[status_format_key])
        self.checklist.write(self.row, self.EXPLANATION_COLUMN, "", self.formats["explanation"])

    def end_element(self, tag: str, attributes: TreeBuilderAttributes) -> None:
        super().end_element(tag, attributes)
        if tag == xmltags.DOCUMENT:
            self.__finish_checklist()
        elif tag == xmltags.SECTION and self.measure_text:
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
            "Onderstaande checklist kan gebruikt worden voor het uitvoeren van een assessment tegen de "
            "ICTU Kwaliteitsaanpak Softwareontwikkeling versie {0}, {1}.".format(
                version, datetime.date.today().strftime("%d-%m-%Y")
            ),
            self.formats["header"],
        )
        self.checklist.set_row(0, 30)
        self.checklist.set_row(self.HEADER_ROW, 30)
        for column, (header, width) in enumerate(
            [("Maatregel", 12), ("Omschrijving", 70), ("Status", 20), ("Toelichting", 70)]
        ):
            self.checklist.write(self.HEADER_ROW, column, header, self.formats["header"])
            self.checklist.set_column("{0}:{0}".format("ABCD"[column]), width)
        self.checklist.write_comment(
            self.HEADER_ROW,
            2,
            "Bij maatregelen die primair door een project moeten worden toegepast geeft Status aan in "
            "hoevere het project dat doet. Bij maatregelen die primair door ICTU "
            "moeten worden toegepast geeft de status aan in hoeverre ICTU dat "
            "doet, gezien vanuit het perspectief van het project.",
            dict(x_scale=3, y_scale=3),
        )

    def __finish_checklist(self) -> None:
        """Wrap up the checklist."""
        self.__write_assessment_choices()
        self.checklist.freeze_panes(self.MEASURE_START_ROW, self.STATUS_COLUMN)

    def __write_assessment_choices(self) -> None:
        """Write the assessment choices, colors and data validation in the status column."""
        assessment_choices = ["voldoet", "voldoet deels", "voldoet niet", "niet van toepassing"]
        for choice in assessment_choices:
            self.checklist.conditional_format(
                self.MEASURE_START_ROW,
                self.STATUS_COLUMN,
                self.row + self.MEASURE_START_ROW - 1,
                self.STATUS_COLUMN,
                {"type": "cell", "criteria": "==", "value": '"{0}"'.format(choice), "format": self.formats[choice]},
            )
        self.checklist.data_validation(
            self.MEASURE_START_ROW,
            self.STATUS_COLUMN,
            self.row + self.MEASURE_START_ROW - 1,
            self.STATUS_COLUMN,
            dict(validate="list", source=assessment_choices),
        )

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
            action_list.set_column("{0}:{0}".format("ABCD"[column]), width)
