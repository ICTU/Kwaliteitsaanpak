"""Self-assessment XLSX-spreadsheet builder."""

import datetime
import pathlib
import re

import xlsxwriter

from .builder import Attributes, Builder
import xmltags


class XlsxBuilder(Builder):
    """Self-assessment builder."""

    def __init__(self, filename: pathlib.Path) -> None:
        super().__init__(filename)
        filename.unlink(missing_ok=True)
        self.workbook = xlsxwriter.Workbook(filename)
        self.header_format = self.workbook.add_format(
            dict(text_wrap=True, font_size=14, bold=True, bg_color="#B3D6C9")
        )
        measure_format_options = dict(bg_color="#BCD2EE", text_wrap=True, valign="top")
        self.measure_format = self.workbook.add_format(measure_format_options)
        self.sub_measure_format = self.workbook.add_format(dict(align="vjustify", indent=1, **measure_format_options))
        self.explanation_format = self.workbook.add_format(dict(bg_color="#FFFFA5", text_wrap=True))
        status_format_options = dict(bg_color="#FED32D", text_wrap=True)
        self.status_format = self.workbook.add_format(status_format_options)
        self.sub_status_format = self.workbook.add_format(dict(indent=1, **status_format_options))
        self.green = self.workbook.add_format(dict(fg_color="#0B5101", bg_color="#BBEDC3"))
        self.yellow = self.workbook.add_format(dict(fg_color="#894503", bg_color="#FEE88A"))
        self.red = self.workbook.add_format(dict(fg_color="#880009", bg_color="#FEB8C3"))
        self.grey = self.workbook.add_format(dict(fg_color="#6D6D6D", bg_color="#EFEFEF"))
        self.header_row = 1
        self.end_row = self.measure_row = self.measure_start_row = self.header_row + 1
        self.measure_id_column, self.measure_column, self.status_column, self.explanation_column = range(4)
        self.last_level_1_section_heading = ""
        self.measure_id = None
        self.measure_text = []
        self.in_appendices = False

    def start_element(self, tag: str, attributes: Attributes) -> None:
        super().start_element(tag, attributes)
        if tag == xmltags.DOCUMENT:
            self.__create_checklist(attributes["version"])
        elif tag == xmltags.SECTION:
            self.in_appendices = attributes.get(xmltags.SECTION_IS_APPENDIX) == "y"
        elif tag == xmltags.MEASURE and not self.in_appendices:
            if self.last_level_1_section_heading:
                self.end_row += 1
                self.checklist.merge_range(
                    "A{row}:D{row}".format(row=self.end_row), self.last_level_1_section_heading, self.header_format
                )
                self.last_level_1_section_heading = ""
        elif self.measure_text:
            if tag == xmltags.LIST_ITEM:
                prefix = (
                    f"{attributes[xmltags.LIST_ITEM_NUMBER]}. " if xmltags.LIST_ITEM_NUMBER in attributes else "- "
                )
                self.measure_text.append(prefix)
            elif tag == xmltags.TABLE_CELL:
                self.measure_text.append("")  # Add empty string in case the cell is empty and text() is never called

    def text(self, tag: str, text: str, attributes: Attributes) -> None:
        text = re.sub("[¹²³⁴⁵⁶⁷⁸⁹⁰]+", "", text)  # Remove footnotes
        if tag == xmltags.HEADING and self.tag_path.count(xmltags.SECTION) == 1:
            self.last_level_1_section_heading = text
        elif len(self.tag_path) >= 3 and xmltags.MEASURE in self.tag_path and not self.in_appendices:
            if self.tag_path[-3] == xmltags.MEASURE and tag == xmltags.BOLD:
                self.measure_row = self.end_row
                self.measure_id, measure_title = text.split(":")
                self.__write_measure(self.measure_id, measure_title.strip())
            self.measure_text.append(text)
        elif self.measure_text:
            if (
                tag == xmltags.LIST_ITEM
                and xmltags.LIST_ITEM_NUMBER in attributes
                and self.measure_id in ("M05", "M07", "M16", "M17")
            ):
                self.end_row += 1
                self.__write_measure("", f"{attributes[xmltags.LIST_ITEM_NUMBER]}. {text}")
            if tag == xmltags.TABLE_CELL and self.measure_id == "M01":
                # The unicode checkmarx symbol is wider than other characters, messing up the table layout:
                text = text.replace("✔", "x")
                column, row = int(attributes[xmltags.TABLE_CELL_COLUMN]), int(attributes[xmltags.TABLE_CELL_ROW])
                if row > 0 and column == 0:  # Table cell with a document
                    self.end_row += 1
                    # Write the document as (sub)measure
                    self.__write_measure("", f"{row}. {text}")
                text += " " * (int(attributes[xmltags.TABLE_CELL_WIDTH]) - len(text))
            self.measure_text.append(text)

    def __write_measure(self, measure_id, measure_text) -> None:
        """Write a measure row."""
        self.checklist.write(self.end_row, self.measure_id_column, measure_id, self.measure_format)
        self.checklist.write(self.end_row, self.measure_column, measure_text, self.measure_format)
        self.checklist.write(self.end_row, self.status_column, "", self.status_format)
        self.checklist.write(self.end_row, self.explanation_column, "", self.explanation_format)

    def end_element(self, tag: str, attributes: Attributes) -> None:
        super().end_element(tag, attributes)
        if tag == xmltags.DOCUMENT:
            self.__finish_checklist()
        elif tag == xmltags.SECTION and self.measure_text:
            self.checklist.write_comment(
                self.measure_row,
                self.measure_column,
                "".join(self.measure_text),
                dict(x_scale=7, y_scale=8, font_name="Courier", font_size=9),
            )
            self.measure_text = []
            self.end_row += 1
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
        self.checklist = self.workbook.add_worksheet("Self-assessment checklist")
        self.checklist.merge_range(
            "A1:D1",
            "Onderstaande checklist kan gebruikt worden voor het uitvoeren van een assessment tegen de "
            "ICTU Kwaliteitsaanpak Softwareontwikkeling versie {0}, {1}.".format(
                version, datetime.date.today().strftime("%d-%m-%Y")
            ),
            self.header_format,
        )
        self.checklist.set_row(0, 30)
        self.checklist.set_row(self.header_row, 30)
        for column, (header, width) in enumerate(
            [("Maatregel", 12), ("Omschrijving", 70), ("Status", 20), ("Toelichting", 70)]
        ):
            self.checklist.write(self.header_row, column, header, self.header_format)
            self.checklist.set_column("{0}:{0}".format("ABCD"[column]), width)
        self.checklist.write_comment(
            self.header_row,
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
        self.checklist.freeze_panes(self.measure_start_row, self.status_column)

    def __write_assessment_choices(self) -> None:
        """ Write the assessment choices, colors and data validation in the status column. """
        assessment_choices = [
            ("voldoet", self.green),
            ("voldoet deels", self.yellow),
            ("voldoet niet", self.red),
            ("niet van toepassing", self.grey),
        ]
        for choice, color in assessment_choices:
            self.checklist.conditional_format(
                self.measure_start_row,
                self.status_column,
                self.end_row + self.measure_start_row - 1,
                self.status_column,
                {"type": "cell", "criteria": "==", "value": '"{0}"'.format(choice), "format": color},
            )
        self.checklist.data_validation(
            self.measure_start_row,
            self.status_column,
            self.end_row + self.measure_start_row - 1,
            self.status_column,
            dict(validate="list", source=[choice[0] for choice in assessment_choices]),
        )

    def __create_action_list(self) -> None:
        """ Create a worksheet with room for actions from the self-assessment. """
        action_list = self.workbook.add_worksheet("Self-assessment verbeteracties")
        action_list.merge_range(
            "A1:D1",
            "Onderstaande actielijst kan gebruikt worden om acties n.a.v. de self-assessment bij te houden.",
            self.header_format,
        )
        action_list.set_row(0, 30)
        action_list.set_row(1, 30)
        for column, (header, width) in enumerate([("Datum", 12), ("Actie", 70), ("Status", 20), ("Toelichting", 70)]):
            action_list.write(1, column, header, self.header_format)
            action_list.set_column("{0}:{0}".format("ABCD"[column]), width)
