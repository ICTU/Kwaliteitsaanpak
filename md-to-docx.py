import sys
import pathlib
import re
from docx import Document
from docx.shared import Inches
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


STYLE_NORMAL = 'Normal'
STYLE_NORMAL_COMPACT = 'Compact'
STYLE_DEFAULT_PARAGRAPH_TEXT = 'Body Text Char'
STYLE_HEADING1 = 'Heading 1'
STYLE_HEADING2 = 'Heading 2'
STYLE_HEADING3 = 'Heading 3'
STYLE_HEADING4 = 'Heading 4'
STYLE_HEADING5 = 'Heading 5'
STYLE_APPENDIX_HEADING1 = 'Kop 1 Bijlage'
STYLE_APPENDIX_HEADING2 = 'Kop 2 Bijlage'
STYLE_APPENDIX_HEADING3 = 'Kop 3 Bijlage'
STYLE_HEADING_TOC = 'Kop inhoudsopgave 1'
STYLE_LIST_BULLET = 'Lijst opsom.teken1'
STYLE_LIST_NUMBER = 'Lijstnummering1'
STYLE_TABLE = 'Tabelraster1'
STYLE_TITLE = 'Title'
STYLE_MAATREGEL = 'Maatregel'
STYLE_INSTRUCTION = 'Instructie'
DEFAULT_FONT = 'Calibri'
IMAGE_ICTU_LOGO = './Content/Images/ICTU.png'
IMAGE_WORDCLOUD = './Content/Images/word-cloud.png'
MD_BOLD = '**'
MD_BOLD_ALTERNATIVE = '__'
MD_ITALIC = '_'
MD_ITALIC_ALTERNATIVE = '*'
MD_STRIKETHROUGH = '~~'
MD_INSTRUCTION_START = '{'
MD_INSTRUCTION_END = '}'


class ParagraphConverter:
    def __init__(self):
        self.buffer = ""
        self.format_started = {
            MD_BOLD: False, MD_BOLD_ALTERNATIVE: False, MD_ITALIC: False, MD_ITALIC_ALTERNATIVE: False,
            MD_STRIKETHROUGH: False}
        self.instruction_started = False

    def format(self, paragraph, line):
        pos = 0
        while pos < len(line):
            remainder = line[pos:]

            cont = False
            for md_format in self.format_started.keys():
                if remainder.startswith(md_format):
                    if md_format in remainder[len(md_format):]:
                        self.start_style(paragraph)
                        pos += len(md_format)
                        self.format_started[md_format] = True
                        cont = True
                        break
                    elif self.format_started[md_format]:
                        self.end_style(paragraph, md_format)
                        self.format_started[md_format] = False
                        pos += len(md_format)
                        cont = True
                        break
            if cont:
                continue

            self.buffer += remainder[0]

            if remainder.startswith(MD_INSTRUCTION_START) and MD_INSTRUCTION_END in remainder[1:]:
                self.start_style(paragraph)
                self.instruction_started = True
            if remainder.startswith(MD_INSTRUCTION_END) and self.instruction_started:
                self.end_style(paragraph, MD_INSTRUCTION_END)
                self.instruction_started = False

            pos += 1

        if self.buffer:
            paragraph.add_run(self.buffer)

        return paragraph

    def start_style(self, paragraph):
        self.flush(paragraph)

    def end_style(self, paragraph, markup):
        self.flush(
            paragraph,
            is_bold=markup in (MD_BOLD, MD_BOLD_ALTERNATIVE),
            is_italic=markup in (MD_ITALIC, MD_ITALIC_ALTERNATIVE),
            is_strikethrough=(markup==MD_STRIKETHROUGH),
            is_instructie=(markup==MD_INSTRUCTION_END))

    def flush(self, paragraph, is_bold=False, is_italic=False, is_strikethrough=False, is_instructie=False):
        p = paragraph.add_run(self.buffer)
        p.bold = is_bold or self.format_started[MD_BOLD] or self.format_started[MD_BOLD_ALTERNATIVE]
        p.italic = is_italic or self.format_started[MD_ITALIC] or self.format_started[MD_ITALIC_ALTERNATIVE]
        p.font.strike = is_strikethrough or self.format_started[MD_STRIKETHROUGH]
        if is_instructie:
            p.style = STYLE_INSTRUCTION
        self.buffer = ""


def list_number(doc, par, prev=None, level=None, num=True):
    """
    Makes a paragraph into a list item with a specific level and
    optional restart.

    An attempt will be made to retreive an abstract numbering style that
    corresponds to the style of the paragraph. If that is not possible,
    the default numbering or bullet style will be used based on the
    ``num`` parameter.

    Parameters
    ----------
    doc : docx.document.Document
        The document to add the list into.
    par : docx.paragraph.Paragraph
        The paragraph to turn into a list item.
    prev : docx.paragraph.Paragraph or None
        The previous paragraph in the list. If specified, the numbering
        and styles will be taken as a continuation of this paragraph.
        If omitted, a new numbering scheme will be started.
    level : int or None
        The level of the paragraph within the outline. If ``prev`` is
        set, defaults to the same level as in ``prev``. Otherwise,
        defaults to zero.
    num : bool
        If ``prev`` is :py:obj:`None` and the style of the paragraph
        does not correspond to an existing numbering style, this will
        determine wether or not the list will be numbered or bulleted.
        The result is not guaranteed, but is fairly safe for most Word
        templates.
    """
    xpath_options = {
        True: {'single': 'count(w:lvl)=1 and ', 'level': 0},
        False: {'single': '', 'level': level},
    }

    def style_xpath(prefer_single=True):
        """
        The style comes from the outer-scope variable ``par.style.name``.
        """
        style = par.style.style_id
        return (
            'w:abstractNum['
                '{single}w:lvl[@w:ilvl="{level}"]/w:pStyle[@w:val="{style}"]'
            ']/@w:abstractNumId'
        ).format(style=style, **xpath_options[prefer_single])

    def type_xpath(prefer_single=True):
        """
        The type is from the outer-scope variable ``num``.
        """
        type = 'decimal' if num else 'bullet'
        return (
            'w:abstractNum['
                '{single}w:lvl[@w:ilvl="{level}"]/w:numFmt[@w:val="{type}"]'
            ']/@w:abstractNumId'
        ).format(type=type, **xpath_options[prefer_single])

    def get_abstract_id():
        """
        Select as follows:

            1. Match single-level by style (get min ID)
            2. Match exact style and level (get min ID)
            3. Match single-level decimal/bullet types (get min ID)
            4. Match decimal/bullet in requested level (get min ID)
            3. 0
        """
        for fn in (style_xpath, type_xpath):
            for prefer_single in (True, False):
                xpath = fn(prefer_single)
                ids = numbering.xpath(xpath)
                if ids:
                    return min(int(x) for x in ids)
        return 0

    if (prev is None or
            prev._p.pPr is None or
            prev._p.pPr.numPr is None or
            prev._p.pPr.numPr.numId is None):
        if level is None:
            level = 0
        numbering = doc.part.numbering_part.numbering_definitions._numbering
        # Compute the abstract ID first by style, then by num
        anum = get_abstract_id()
        # Set the concrete numbering based on the abstract numbering ID
        num = numbering.add_num(anum)
        # Make sure to override the abstract continuation property
        num.add_lvlOverride(ilvl=level).add_startOverride(1)
        # Extract the newly-allocated concrete numbering ID
        num = num.numId
    else:
        if level is None:
            level = prev._p.pPr.numPr.ilvl.val
        # Get the previous concrete numbering ID
        num = prev._p.pPr.numPr.numId.val
    par._p.get_or_add_pPr().get_or_add_numPr().get_or_add_numId().val = num
    par._p.get_or_add_pPr().get_or_add_numPr().get_or_add_ilvl().val = level

def define_style(document, name, font_name, font_size, top_margin=Pt(0), keep_with_next=False, page_break_before=False):
    style = document.styles[name]
    style.font.name = font_name
    style.font.size = font_size
    style.paragraph_format.space_before = top_margin
    style.paragraph_format.keep_with_next = keep_with_next
    style.paragraph_format.page_break_before = page_break_before

def define_char_style(document, name, font_name, font_size):
    style = document.styles[name]
    style.font.name = font_name
    style.font.size = font_size

def set_styles(document):
    define_char_style(document, STYLE_DEFAULT_PARAGRAPH_TEXT, DEFAULT_FONT, Pt(12))
    define_style(document, STYLE_NORMAL, DEFAULT_FONT, Pt(12))
    define_style(document, STYLE_HEADING1, DEFAULT_FONT, Pt(32), top_margin=Pt(30), keep_with_next=True, page_break_before=True)
    define_style(document, STYLE_HEADING2, DEFAULT_FONT, Pt(18), top_margin=Pt(20), keep_with_next=True)
    define_style(document, STYLE_HEADING3, DEFAULT_FONT, Pt(12), top_margin=Pt(10), keep_with_next=True)
    define_style(document, STYLE_HEADING4, DEFAULT_FONT, Pt(12), keep_with_next=True)
    define_style(document, STYLE_HEADING5, DEFAULT_FONT, Pt(12), keep_with_next=True)

def create_frontpage(document, title):
    document.add_picture(IMAGE_ICTU_LOGO)
    document.add_paragraph(f'{title}', style=STYLE_TITLE)
    p = document.add_paragraph('', style=STYLE_NORMAL_COMPACT)
    p = p.add_run('{Projectnaam}')
    p.style = STYLE_INSTRUCTION
    p.bold = True
    document.add_paragraph('')
    p = document.add_paragraph('Versie ', style=STYLE_NORMAL_COMPACT)
    p = p.add_run('{versienummer}')
    p.style = STYLE_INSTRUCTION
    p = document.add_paragraph('Datum ', style=STYLE_NORMAL_COMPACT)
    p = p.add_run('{datum}')
    p.style = STYLE_INSTRUCTION
    document.add_paragraph('')
    document.add_paragraph('')
    document.add_paragraph('')
    document.add_paragraph('')
    p = document.add_picture(IMAGE_WORDCLOUD)
    p.top_margin = Pt(36)
    document.add_page_break()

def create_header(document, title):
    document.sections[0].different_first_page_header_footer = True
    header_paragraph = document.sections[0].header.paragraphs[0]
    header_paragraph.clear()
    p = header_paragraph.add_run('{Projectnaam}')
    p.style = STYLE_INSTRUCTION
    header_paragraph.add_run(f'\t\t{title}')

def create_table_of_contents(document):
    document.add_paragraph("Inhoudsopgave", style=STYLE_HEADING_TOC)
    paragraph = document.add_paragraph()
    run = paragraph.add_run()
    fldChar = OxmlElement('w:fldChar')  # creates a new element
    fldChar.set(qn('w:fldCharType'), 'begin')  # sets attribute on element
    instrText = OxmlElement('w:instrText')
    instrText.set(qn('xml:space'), 'preserve')  # sets attribute on element
    instrText.text = 'TOC \\o "1-3" \\h \\z \\u'   # change 1-3 depending on heading levels you need

    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'separate')
    fldChar3 = OxmlElement('w:t')
    fldChar3.text = "Right-click to update field."
    fldChar2.append(fldChar3)

    fldChar4 = OxmlElement('w:fldChar')
    fldChar4.set(qn('w:fldCharType'), 'end')

    r_element = run._r
    r_element.append(fldChar)
    r_element.append(instrText)
    r_element.append(fldChar2)
    r_element.append(fldChar4)
    p_element = paragraph._p
    document.add_page_break()


class DocumentConverter:
    def __init__(self):
        self.in_bijlagen = False
        self.in_list = False
        self.in_maatregel = False
        self.in_table = False
        self.table = None
        self.cell_alignment = []

    def convert(self, input, output, reference, title):
        if reference != None:
            print(f"Converting {input} to {output} using reference {reference}.")
            document = Document(reference)
            self.clear_document(document)
            #for style in document.styles:
            #    print(f"style: {style.name}")
        else:
            print(f"Converting {input} to {output} using default styles.")
            document = Document()
            set_styles(document)

        create_header(document, title)
        create_frontpage(document, title)
        create_table_of_contents(document)

        with open(input, mode='r', encoding='utf8') as source_file:
            lines = source_file.readlines()
            previous = None
            for line in lines:
                indented = len(line) > 0 and line.startswith(' ')
                stripped_line = line.strip()
                if len(stripped_line) > 0:
                    previous = self.process_line(document, stripped_line, previous, indented)
        document.save(output)

    def process_line(self, document, line, previous, indented):
        p = None
        line, leaving_maatregel = self.process_maatregel_line(line)
        if line.startswith("|"):
            self.process_table_line(document, line)
        else:
            self.close_table()
            # heading
            if line.startswith('#'):
                p = self.create_heading(document, line)
            # bullet list
            elif re.match(r"^[*+-] .*", line):
                bullet_char = line[0]
                line = re.sub(r"^[*+-] ", "", line).strip()
                p = self.create_bullet_list_item(document, line, previous, bullet_char)
            # numbered list
            elif re.match(r"^[0-9a-zA-Z]+[.] .*", line):
                if line[0].isalpha():
                    level = 1
                elif indented:
                    level = 2
                else:
                    level = 0
                line = re.sub(r"^[0-9a-zA-Z]+[.] ", "", line).strip()
                p = self.create_numbered_list_item(document, line, previous, level)
            # regular text paragraph
            else:
                self.in_list = False
                p = self.create_paragraph(document, line)

        if leaving_maatregel:
            self.in_maatregel = False
        return p

    def process_maatregel_line(self, line):
        leaving_maatregel = False
        if line.startswith("@{"):
            self.in_maatregel = True
            line = line[2:]
        if self.in_maatregel and line.count('}@') > 0:
            leaving_maatregel = True
            line = line.replace('}@', '')
        return line, leaving_maatregel

    def process_table_line(self, document, line):
        if self.in_table:
            self.process_table_row(document, line)
        else:
            self.table = self.process_header_row(document, line)
            self.in_table = True

    def create_heading(self, document, line):
        heading_level = line.count('#')
        line = line.strip('#').strip()
        self.in_list = False
        if heading_level == 1 and line.upper() == 'BIJLAGEN':
            self.in_bijlagen = True

        if self.in_bijlagen:
            return document.add_paragraph(line, style=self.bijlage_heading_style(heading_level))
        else:
            return document.add_heading(line, level=heading_level)

    def create_numbered_list_item(self, document, line, previous, level=0):
        p = self.create_paragraph(document, line, style=STYLE_LIST_NUMBER)
        list_number(document, p, previous if self.in_list else None, level, True)
        self.in_list = True
        return p

    def create_bullet_list_item(self, document, line, previous, bullet_char):
        level = {'+': 1, '-': 2}.get(bullet_char, 0)
        p = self.create_paragraph(document, line, style=STYLE_LIST_BULLET)
        list_number(document, p, previous if self.in_list else None, level, False)
        self.in_list = True
        return p

    def create_paragraph(self, parent, line, style=STYLE_NORMAL):
        p = parent.add_paragraph("", style=STYLE_MAATREGEL if self.in_maatregel else style)
        return ParagraphConverter().format(p, line)

    def process_header_row(self, document, line):
        cells = self.get_cells(line)
        table = document.add_table(rows=1, cols=len(cells))
        table.style = STYLE_TABLE
        table.allow_autofit = True
        self.cell_alignment = []
        hdr_cells = table.rows[0].cells
        for i in range(len(cells)):
            ParagraphConverter().format(hdr_cells[i].paragraphs[0], cells[i])
        return table

    def process_table_row(self, document, line):
        cells = self.get_cells(line)
        if len(self.table.rows) == 1 and line.find('---') >= 0:
            self.process_table_row_alignment(cells)
        else:
            self.process_table_row_content(cells)

    def process_table_row_alignment(self, cells):
        self.cell_alignment = []
        for cell in cells:
            if re.match(r"^:.*:$", cell):
                self.cell_alignment.append(WD_ALIGN_PARAGRAPH.CENTER)
            elif re.match(r".*:$", cell):
                self.cell_alignment.append(WD_ALIGN_PARAGRAPH.RIGHT)
            else:
                self.cell_alignment.append(WD_ALIGN_PARAGRAPH.LEFT)
        for row in self.table.rows:
            for i in range(len(row.cells)):
                cell = row.cells[i]
                cell.paragraphs[0].alignment = self.cell_alignment[i]

    def process_table_row_content(self, cells):
        row_cells = self.table.add_row().cells
        for i in range(len(cells)):
            p = row_cells[i].paragraphs[0]
            ParagraphConverter().format(p, cells[i])
            if i < len(self.cell_alignment):
                p.alignment = self.cell_alignment[i]

    def close_table(self):
        if self.in_table:
            self.table.autofit = True
            self.table = None
            self.in_table = False

    def delete_element(self, paragraph):
        p = paragraph._element
        p.getparent().remove(p)
        p._p = p._element = None

    def clear_document(self, document):
        paragraphs = document.paragraphs
        for paragraph in paragraphs:
            self.delete_element(paragraph)
        tables = document.tables
        for table in tables:
            self.delete_element(table)

    @staticmethod
    def get_cells(line):
        return [cell.strip() for cell in line.strip('| ').split('|')]

    @staticmethod
    def bijlage_heading_style(level):
        return {1: STYLE_APPENDIX_HEADING1, 2: STYLE_APPENDIX_HEADING2}.get(level, STYLE_APPENDIX_HEADING3)


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if 3 <= len(arguments) <= 4:
        input = arguments[0]
        output = arguments[1]
        title = arguments[2]
        reference = None
        if len(arguments) == 4:
            reference = arguments[3]
        DocumentConverter().convert(input, output, reference, title)
    else:
        print(f"USAGE: md-to-docx <input file> <output file> <document title> [<reference file>]")
