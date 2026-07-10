"""Markdown syntax."""

# Official Markdown syntax
BOLD_START = BOLD_END = "**"
BOLD_ALTERNATIVE_START = BOLD_ALTERNATIVE_END = "__"
BULLET_LIST_PATTERN = r"^[\*\+\-] "
CELL_ALIGNMENT_MARKER = ":"
CODE_START = CODE_END = "`"
CODE_BLOCK_START = r"```([a-z]+)"
CODE_BLOCK_END = r"```"
HEADING_PATTERN = r"^(#+) (.*)"
# The path for the images does allow whitespace but no quote
# The title is delimited by the quotes, so it may contain any character except a quote (e.g. parentheses)
IMAGE_PATTERN = r'^!\[([^\]]+)\]\((.+) "([^"]+)"\)'
ITALIC_START = ITALIC_END = "_"
ITALIC_ALTERNATIVE_START = ITALIC_ALTERNATIVE_END = "*"
# The URL may contain balanced parentheses (e.g. https://en.wikipedia.org/wiki/Foo_(disambiguation)), one level deep
LINK_PATTERN = r"^\[([^\]]+)\]\(((?:[^()]|\([^()]*\))*)\)"
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
