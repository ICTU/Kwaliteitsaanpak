import pathlib
import re
import sys

import xlsxwriter


def process_submaatregel(worksheet, row, submaatregelen, maatregel_format, status_format, toelichting_format):
    """ Write the submaatregelen. """
    for index, submaatregel in enumerate(submaatregelen):
        worksheet.write(row, 0, "", maatregel_format)
        worksheet.write(row, 1, "{0}. {1}".format(index + 1, submaatregel), maatregel_format)
        worksheet.write(row, 2, "", status_format)
        worksheet.write(row, 3, "", toelichting_format)
        row += 1
    return row


def process_m01(worksheet, row, contents, maatregel_format, status_format, toelichting_format):
    """ Read the list of products from the markdown table. """
    products = [line[1:].split("|")[0].strip() for line in contents if line.startswith("|")][2:]
    return process_submaatregel(worksheet, row, products, maatregel_format, status_format, toelichting_format)


def process_m05_m07(worksheet, row, contents, maatregel_format, status_format, toelichting_format):
    """ Read the list of parts from the markdown list. """
    parts = [line[2:].strip().strip(",.") for line in contents if line.startswith("- ") or line.startswith("* ")]
    return process_submaatregel(worksheet, row, parts, maatregel_format, status_format, toelichting_format)


def process_m16_m17(worksheet, row, contents, maatregel_format, status_format, toelichting_format):
    """ Read the list of tools from the markdown list. """
    tools = [line.split(". ")[1].strip() for line in contents if re.match(r"^\d+\. ", line)]
    return process_submaatregel(worksheet, row, tools, maatregel_format, status_format, toelichting_format)


def read_md_file(filepath, title):
    """ Read the markdown file and process #include's, if any. """
    contents = []
    reference_without_link = re.compile(r"\{\{M\d+\-no\-link\}\}")
    references = re.compile(r"@\{|\}@|\{\{|\}\}")
    with filepath.open(encoding="utf-8") as markdown:
        for line in markdown.readlines():
            line = line.replace("{{TITLE}}", title)
            if line.startswith("#include "):
                included_filepath = pathlib.Path(line.strip('# include "').strip().strip('"'))
                contents.extend(read_md_file(included_filepath, title))
            else:
                line = reference_without_link.sub("", line)
                line = references.sub("", line)
                if line:
                    contents.append(line)
    return contents


def process_maatregel(workbook, worksheet, maatregel_folder, row, title):
    """ Process the maatregel in the given folder. """
    maatregel_md = maatregel_folder / "Maatregel.md"
    contents = read_md_file(maatregel_md, title)
    maatregel_id = contents[0].strip().split(":")[0][len("## "):]
    maatregel_format_options = dict(bg_color="#BCD2EE", text_wrap=True)
    maatregel_format = workbook.add_format(maatregel_format_options)
    worksheet.write(row, 0, maatregel_id, maatregel_format)
    title = contents[0].strip("#").split("(")[0].strip()
    worksheet.write(row, 1, title, maatregel_format)
    worksheet.write_comment(row, 1, "".join([line.strip("#").strip(" ") for line in contents]),
                            dict(x_scale=5, y_scale=7))
    status_format_options = dict(bg_color="#FED32D", text_wrap=True)
    status_format = workbook.add_format(status_format_options)
    worksheet.write(row, 2, "", status_format)
    toelichting_format = workbook.add_format(dict(bg_color="#FFFFA5", text_wrap=True))
    worksheet.write(row, 3, "", toelichting_format)
    row += 1
    sub_maatregel_format = workbook.add_format(dict(align="vjustify", indent=1, **maatregel_format_options))
    sub_status_format = workbook.add_format(dict(indent=1, **status_format_options))
    if maatregel_id == "M01":
        row = process_m01(worksheet, row, contents, sub_maatregel_format, sub_status_format, toelichting_format)
    elif maatregel_id in ("M05", "M07"):
        row = process_m05_m07(worksheet, row, contents, sub_maatregel_format, sub_status_format, toelichting_format)
    elif maatregel_id in ("M16", "M17"):
        row = process_m16_m17(worksheet, row, contents, sub_maatregel_format, sub_status_format, toelichting_format)
    return row


def write_assessment_choices(workbook, worksheet, start_row, end_row, column):
    """ Write the assessment choices, colors and data validation in the status column. """
    green = workbook.add_format(dict(fg_color="#0B5101", bg_color="#BBEDC3"))
    yellow = workbook.add_format(dict(fg_color="#894503", bg_color="#FEE88A"))
    red = workbook.add_format(dict(fg_color="#880009", bg_color="#FEB8C3"))
    grey = workbook.add_format(dict(fg_color="#6D6D6D", bg_color="#EFEFEF"))
    assessment_choices = [("voldoet", green), ("voldoet deels", yellow), ("voldoet niet", red),
                          ("niet van toepassing", grey)]
    for choice, color in assessment_choices:
        worksheet.conditional_format(
            start_row, column, end_row + start_row - 1, column,
            {"type": "cell", "criteria": "==", "value": '"{0}"'.format(choice), "format": color})
    worksheet.data_validation(
        start_row, column, end_row + start_row - 1, column,
        dict(validate="list", source=[choice[0] for choice in assessment_choices]))


class DocumentStructure:
    """ Class representing the document structure of the kwaliteitsaanpak. """
    def __init__(self):
        with pathlib.Path("DocumentDefinitions/Full/document.md").open() as document_structure:
            self.lines = document_structure.readlines()

    def maatregelen_sections(self):
        """ Return a list of sections in the document. """
        for line in self.lines:
            if line.startswith("# ") and not "Bijlagen" in line:
                yield line.strip().strip("# ")

    def maatregelen_folders(self, section):
        """ Return a list of maatregelen folders in the right order. """
        in_section = False
        for line in self.lines:
            if line.startswith("# "):
                in_section = section in line
            if in_section and '/Maatregel.md"' in line:
                yield pathlib.Path(line.strip().strip('# include "').strip('/Maatregel.md"'))


def create_checklist(workbook, title):
    """ Create the worksheet  with the self-assessment checklist. """
    worksheet = workbook.add_worksheet('Self-assessment checklist')
    with open("Content/Versie.md") as version_file:
        version = version_file.read().strip()

    header_format = workbook.add_format(dict(text_wrap=True, font_size=14, bold=True, bg_color="#B3D6C9"))
    header_row = 1
    worksheet.merge_range(
        "A1:D1",
        "Onderstaande checklist kan gebruikt worden voor het uitvoeren van een assessment tegen de "
        "ICTU Kwaliteitsaanpak Softwareontwikkeling {0}.".format(version.lower()), header_format)
    worksheet.set_row(0, 30)
    worksheet.set_row(header_row, 30)
    for column, (header, width) in enumerate([("Maatregel", 12), ("Omschrijving", 70),
                                              ("Status", 20), ("Toelichting", 70)]):
        worksheet.write(header_row, column, header, header_format)
        worksheet.set_column('{0}:{0}'.format("ABCD"[column]), width)
    worksheet.write_comment(
        header_row, 2,
        "Bij maatregelen die primair door een project moeten worden toegepast geeft Status aan in "
        "hoevere het project dat doet. Bij maatregelen die primair door ICTU "
        "moeten worden toegepast geeft de status aan in hoeverre ICTU dat "
        "doet, gezien vanuit het perspectief van het project.",
        dict(x_scale=3, y_scale=3))

    maatregel_start_row = row = 2

    document = DocumentStructure()
    for section in document.maatregelen_sections():
        row += 1
        worksheet.merge_range("A{row}:D{row}".format(row=row), section, header_format)
        for folder in document.maatregelen_folders(section):
            row = process_maatregel(workbook, worksheet, folder, row, title)

    status_column = 2
    write_assessment_choices(workbook, worksheet, maatregel_start_row, row, status_column)
    worksheet.freeze_panes(maatregel_start_row, status_column)


def create_action_list(workbook):
    """ Create a worksheet with room for actions from the self-assessment. """
    worksheet = workbook.add_worksheet('Self-assessment verbeteracties')
    header_format = workbook.add_format(dict(text_wrap=True, font_size=14, bold=True, bg_color="#B3D6C9"))
    worksheet.merge_range(
        "A1:D1",
        "Onderstaande actielijst kan gebruikt worden om acties n.a.v. de self-assessment bij te houden.",
        header_format)
    worksheet.set_row(0, 30)
    worksheet.set_row(1, 30)
    for column, (header, width) in enumerate([("Datum", 12), ("Actie", 70),
                                              ("Status", 20), ("Toelichting", 70)]):
        worksheet.write(1, column, header, header_format)
        worksheet.set_column('{0}:{0}'.format("ABCD"[column]), width)


def create_workbook():
    """ Create the workbook with the different worksheets. """
    workbook = xlsxwriter.Workbook('dist/ICTU-Kwaliteitsaanpak-Checklist.xlsx')
    title = sys.argv[1]
    create_checklist(workbook, title)
    create_action_list(workbook)
    workbook.close()


if __name__ == "__main__":
    create_workbook()
