"""Markdown syntax."""

# Official Markdown syntax
BOLD_START = BOLD_END = "**"
BOLD_ALTERNATIVE_START = BOLD_ALTERNATIVE_END = "__"
BULLET_LIST_PATTERN = r"^[\*\+\-] "
CELL_ALIGNMENT_MARKER = ":"
CODE_BLOCK_START = r"```([a-z]+)"
CODE_BLOCK_END = r"```"
HEADING_PATTERN = r"^(#+) (.*)"
IMAGE_PATTERN = r'^!\[([^\]]+)\]\(([^ ]+) "([^\)]+)"\)'
ITALIC_START = ITALIC_END = "_"
ITALIC_ALTERNATIVE_START = ITALIC_ALTERNATIVE_END = "*"
LINK_PATTERN = r"^\[([^\]]+)\]\(([^\)]+)\)"
NUMBERED_LIST_PATTERN = r"^[0-9A-Za-z]+\. "
STRIKETROUGH_START = STRIKETROUGH_END = "~~"
TABLE_MARKER = "|"

# Syntax specific to this repository
BEGIN_PATTERN = r"^<!-- begin: ([^ ]+)\s?([^ ]*) -->"
END_PATTERN = r"^<!-- end: ([^ ]+) -->"
INSTRUCTION_START = "{"
INSTRUCTION_END = "}"
MEASURE_TITLE_START = "[measure-title]"
MEASURE_TITLE_END = "[/measure-title]"
SUBMEASURE_TITLE_START = "[submeasure-title]"
SUBMEASURE_TITLE_END = "[/submeasure-title]"
VARIABLE_USE_PATTERN = r"\$([^\$]+)\$"
