"""Add hyperlink."""

from docx import opc, oxml

from .utils import slugify

MAX_BOOKMARK_LENGTH = (
    40  # https://stackoverflow.com/questions/852922/what-are-the-limitations-for-bookmark-names-in-microsoft-word
)


def add_bookmark(paragraph) -> None:
    """Add a bookmark in the paragraph."""
    bookmark_name = slugify(paragraph.text)[:MAX_BOOKMARK_LENGTH]
    element = paragraph._p

    # Add bookmark start before the first subelement
    start = oxml.shared.OxmlElement("w:bookmarkStart")
    start.set(oxml.ns.qn("w:id"), "0")
    start.set(oxml.ns.qn("w:name"), bookmark_name)
    element.insert(0, start)

    # Add bookmark end after the last subelement
    end = oxml.shared.OxmlElement("w:bookmarkEnd")
    end.set(oxml.ns.qn("w:id"), "0")
    end.set(oxml.ns.qn("w:name"), bookmark_name)
    element.append(end)


def add_hyperlink(paragraph, url, text, style="Hyperlink"):
    """
    A function that places a hyperlink within a paragraph object.

    :param paragraph: The paragraph we are adding the hyperlink to.
    :param url: A string containing the required url
    :param text: The text displayed for the url
    :param style: The style to apply to the text
    :return: The hyperlink object
    """

    # This gets access to the document.xml.rels file and gets a new relation id value
    part = paragraph.part
    url = (url[: MAX_BOOKMARK_LENGTH + 1]) if url.startswith("#") else url  # +1 for the hash
    r_id = part.relate_to(url, opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)

    # Create the w:hyperlink tag and add needed values
    hyperlink = oxml.shared.OxmlElement("w:hyperlink")
    hyperlink.set(oxml.shared.qn("r:id"), r_id)

    # Create a w:r element
    new_run = oxml.shared.OxmlElement("w:r")

    # Create a new w:rPr element
    r_pr_element = oxml.shared.OxmlElement("w:rPr")

    # Join all the xml elements together add add the required text to the w:r element
    new_run.append(r_pr_element)
    new_run.text = text
    new_run.style = style
    hyperlink.append(new_run)

    paragraph._p.append(hyperlink)

    return hyperlink
