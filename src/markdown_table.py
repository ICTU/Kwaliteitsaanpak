"""Table class."""

from typing import List

import markdown_syntax


class Table:
    """Markdown table class."""

    def __init__(self, header_cells: List[str]):
        self.header_cells = header_cells
        self.column_alignment: List[str] = ["left" for _ in self.header_cells]  # alignment per column
        self.column_widths = [len(cell) for cell in header_cells]
        self.rows: List[List[str]] = []

    def process_table_cells(self, cells: List[str]) -> None:
        """Process the table cells."""
        if "---" in cells[0] and len(self.rows) == 0:
            self.__process_table_alignment(cells)
        else:
            self.rows.append(cells)
            self.column_widths = [
                max(current_width, len(cell)) for current_width, cell in zip(self.column_widths, cells)
            ]

    def __process_table_alignment(self, cells: List[str]) -> None:
        """Process the alignment row of the Markdown table."""
        alignment_marker = markdown_syntax.CELL_ALIGNMENT_MARKER
        self.column_alignment = []
        for cell in cells:
            if cell.startswith(alignment_marker) and cell.endswith(alignment_marker):
                alignment = "center"
            elif cell.endswith(alignment_marker):
                alignment = "right"
            else:
                alignment = "left"
            self.column_alignment.append(alignment)

    @staticmethod
    def get_table_cells(line: str) -> List[str]:
        """Return the table cells."""
        line = line.strip().strip(markdown_syntax.TABLE_MARKER)
        return [cell.strip() for cell in line.split(markdown_syntax.TABLE_MARKER)]
