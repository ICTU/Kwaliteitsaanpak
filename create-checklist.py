import pathlib
import re

import xlsxwriter


def process_m01(worksheet, row, contents, maatregel_format, status_format, toelichting_format):
    """ Read the list of products from the markdown table. """
    products = [line[1:].split("|")[0].strip() for line in contents if line.startswith("|")][2:]
    for index, product in enumerate(products):
        worksheet.write(row, 0, "", maatregel_format)
        worksheet.write(row, 1, "{0}. {1}".format(index + 1, product), maatregel_format)
        worksheet.write(row, 2, "", status_format)
        worksheet.write(row, 3, "", toelichting_format)
        row += 1
    return row


def process_m07(worksheet, row, contents, maatregel_format, status_format, toelichting_format):
    """ Read the list of parts from the markdown list. """
    parts = [line[2:].strip(",") for line in contents if line.startswith("- ")]
    for index, part in enumerate(parts):
        worksheet.write(row, 0, "", maatregel_format)
        worksheet.write(row, 1, "{0}. {1}".format(index + 1, part.strip().strip(".,")), maatregel_format)
        worksheet.write(row, 2, "", status_format)
        worksheet.write(row, 3, "", toelichting_format)
        row += 1
    return row


def process_m16_m17(worksheet, row, contents, maatregel_format, status_format, toelichting_format):
    """ Read the list of tools from the markdown list. """
    tools = [line for line in contents if re.match(r"^\d+\. ", line)]
    generic_tools = tools[:len(tools)//2]
    ictu_tools = tools[len(tools)//2:]
    for generic_tool, ictu_tool in zip(generic_tools, ictu_tools):
        worksheet.write(row, 0, "", maatregel_format)
        worksheet.write(row, 1, "{0} Bij ICTU: {1}".format(generic_tool.strip(), ictu_tool.strip().split(". ")[1]),
                        maatregel_format)
        worksheet.write(row, 2, "", status_format)
        worksheet.write(row, 3, "", toelichting_format)
        row += 1
    return row


def process_maatregel(workbook, worksheet, maatregel_folder, row):
    """ Process the maatregel in the given folder. """
    maatregel_md = maatregel_folder / "Maatregel.md"
    with maatregel_md.open(encoding="utf-8") as maatregel:
        contents = maatregel.readlines()
    ictu_md = maatregel_folder / "ICTU.md"
    if ictu_md.exists():
        with ictu_md.open(encoding="utf-8") as ictu:
            contents.append("\n")
            contents.extend(ictu.readlines())
    maatregel_id = contents[0].strip().split("(")[1].strip(")")
    maatregel_format_options = dict(bg_color="#BCD2EE", text_wrap=True)
    maatregel_format = workbook.add_format(maatregel_format_options)
    worksheet.write(row, 0, maatregel_id, maatregel_format)
    title = contents[0].strip("#").split("(")[0].strip()
    worksheet.write(row, 1, title, maatregel_format)
    worksheet.write_comment(row, 1, "".join([line.strip("#").strip(" ") for line in contents]), dict(x_scale=5, y_scale=7))
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
    elif maatregel_id == "M07":
        row = process_m07(worksheet, row, contents, sub_maatregel_format, sub_status_format, toelichting_format)
    elif maatregel_id in ("M16", "M17"):
        row = process_m16_m17(worksheet, row, contents, sub_maatregel_format, sub_status_format, toelichting_format)
    return row


def create_checklist():
    """ Create the spreadsheet with the checklist. """
    workbook = xlsxwriter.Workbook('ICTU-Kwaliteitsaanpak-Checklist.xlsx')
    worksheet = workbook.add_worksheet()
    with open("Content/Versie.md") as version_file:
        version = version_file.read().strip()

    header_format = workbook.add_format(dict(text_wrap=True, font_size=14, bold=True, bg_color="#B3D6C9"))
    worksheet.merge_range(
        "A1:D1",
        "Onderstaande checklist kan gebruikt worden voor het uitvoeren van een assessment tegen de "
        "Kwaliteitsaanpak ICTU Software Realisatie {0}.".format(version.lower()), header_format)
    worksheet.set_row(0, 30)
    worksheet.set_row(1, 30)
    for column, (header, width) in enumerate([("Maatregel", 12), ("Omschrijving", 70),
                                              ("Status", 20), ("Toelichting", 70)]):
        worksheet.write(1, column, header, header_format)
        worksheet.set_column('{0}:{0}'.format("ABCD"[column]), width)

    maatregel_start_row = row = 2

    maatregelen = pathlib.Path("Content/Maatregelen")
    for maatregel_folder in sorted(maatregelen.glob("*")):
        row = process_maatregel(workbook, worksheet, maatregel_folder, row)

    green = workbook.add_format(dict(fg_color="#0B5101", bg_color="#BBEDC3"))
    worksheet.conditional_format(
        maatregel_start_row, 2, row + maatregel_start_row - 1, 2,
        {"type": "cell", "criteria": "==", "value": '"voldoet"', "format": green})
    yellow = workbook.add_format(dict(fg_color="#894503", bg_color="#FEE88A"))
    worksheet.conditional_format(
        maatregel_start_row, 2, row + maatregel_start_row - 1, 2,
        {"type": "cell", "criteria": "==", "value": '"voldoet deels"', "format": yellow})
    red = workbook.add_format(dict(fg_color="#880009", bg_color="#FEB8C3"))
    worksheet.conditional_format(
        maatregel_start_row, 2, row + maatregel_start_row - 1, 2,
        {"type": "cell", "criteria": "==", "value": '"voldoet niet"', "format": red})
    grey = workbook.add_format(dict(fg_color="#6D6D6D", bg_color="#EFEFEF"))
    worksheet.conditional_format(
        maatregel_start_row, 2, row + maatregel_start_row - 1, 2,
        {"type": "cell", "criteria": "==", "value": '"niet van toepassing"', "format": grey})

    worksheet.data_validation(
        maatregel_start_row, 2, row + maatregel_start_row - 1, 2,
        dict(validate="list", source=["voldoet", "voldoet deels", "voldoet niet", "niet van toepassing"]))
    workbook.close()


if __name__ == "__main__":
    create_checklist()
