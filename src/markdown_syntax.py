"""Markdown syntax."""

# Official Markdown syntax
# GitHub alerts, e.g. "> [!NOTE]", case-insensitive, optionally followed by a title (not supported by GitHub)
ADMONITION_PATTERN = r"^>\s?\[!(?i:(NOTE|TIP|IMPORTANT|WARNING|CAUTION))\]\s*(.*)"
BOLD_START = BOLD_END = "**"
BOLD_ALTERNATIVE_START = BOLD_ALTERNATIVE_END = "__"
BULLET_LIST_PATTERN = r"^[\*\+\-] "
CELL_ALIGNMENT_MARKER = ":"
CODE_START = CODE_END = "`"
CODE_BLOCK_START = r"```([a-z]+)"
CODE_BLOCK_END = r"```"
# Markers for bold, italic, strikethrough, and code
FORMATTING_MARKERS_PATTERN = r"\*\*|__|~~|[*_`]"
HEADING_PATTERN = r"^(#+) (.*)"
# The alternative text may be empty. The path for the images does allow whitespace but no quote
# The title is delimited by the quotes, so it may contain any character except a quote (e.g. parentheses)
# The image may be followed by a width in centimeters in an HTML comment, e.g. <!-- width: 5 -->, hidden by GitHub
IMAGE_PATTERN = r'^!\[([^\]]*)\]\((.+) "([^"]+)"\)(?:<!-- width: ([0-9]+) -->)?'
ITALIC_START = ITALIC_END = "_"
ITALIC_ALTERNATIVE_START = ITALIC_ALTERNATIVE_END = "*"
# The URL may contain balanced parentheses (e.g. https://en.wikipedia.org/wiki/Foo_(disambiguation)), one level deep
LINK_PATTERN = r"^\[([^\]]+)\]\(((?:[^()]|\([^()]*\))*)\)"
MERMAID_LANGUAGE = "mermaid"  # Code blocks in this language are rendered as diagrams
NUMBERED_LIST_PATTERN = r"^[0-9A-Za-z]+\. "
QUOTE_MARKER = ">"
STRIKETROUGH_START = STRIKETROUGH_END = "~~"
TABLE_MARKER = "|"

# Syntax specific to this repository
# Abbreviations, e.g. "API" in "API-server", but not "ISO" in "NEN-ISO". Format with the abbreviations separated by "|"
ABBREVIATION_PATTERN = r"(?<![\w-])(?:{})(?!\w)"
BEGIN_PATTERN = r"^<!-- begin: ([^ ]+)\s?([^ ]*) -->"
END_PATTERN = r"^<!-- end: ([^ ]+) -->"
FRONTPAGE_START = "<!-- begin: frontpage -->"
FRONTPAGE_END = "<!-- end: frontpage -->"
INSTRUCTION_START = "{"
LANDSCAPE_BLOCK = "landscape"  # Unlike other blocks, landscape blocks may contain headings
INSTRUCTION_END = "}"
MEASURE_TITLE_START = "[measure-title]"
MEASURE_TITLE_END = "[/measure-title]"
SUBMEASURE_TITLE_START = "[submeasure-title]"
SUBMEASURE_TITLE_END = "[/submeasure-title]"
# Marks the section it is in as explanation of the submeasures with the given numbers, e.g. <!-- submeasures: 1,2 -->
SUBMEASURES_PATTERN = r"^<!-- submeasures: ([0-9]+(?:, ?[0-9]+)*) -->"
VARIABLE_USE_PATTERN = r"\$([^\$]+)\$"
