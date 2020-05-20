"""Table of Contents."""

from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph


def add_table_of_contents(paragraph: Paragraph) -> None:
    """Add a table of contents to the paragraph."""
    run = paragraph.add_run()
    fld_char = OxmlElement("w:fldChar")  # creates a new element
    fld_char.set(qn("w:fldCharType"), "begin")  # sets attribute on element
    instr_text = OxmlElement("w:instrText")
    instr_text.set(qn("xml:space"), "preserve")  # sets attribute on element
    instr_text.text = 'TOC \\o "1-3" \\h \\z \\u'  # change 1-3 depending on heading levels you need

    fld_char2 = OxmlElement("w:fldChar")
    fld_char2.set(qn("w:fldCharType"), "separate")
    fld_char3 = OxmlElement("w:t")
    fld_char3.text = "Right-click to update field."
    fld_char2.append(fld_char3)

    fld_char4 = OxmlElement("w:fldChar")
    fld_char4.set(qn("w:fldCharType"), "end")

    r_element = run._r  # pylint: disable=protected-access
    r_element.append(fld_char)
    r_element.append(instr_text)
    r_element.append(fld_char2)
    r_element.append(fld_char4)
