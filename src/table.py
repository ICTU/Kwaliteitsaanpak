"""Table class."""

from typing import List


class Table:
    """Abstract table class."""
    def __init__(self, header_cells: List[str]):
        self.header_cells = header_cells
        self.column_alignment = []  # alignment per column
        self.column_widths = [len(cell) for cell in header_cells]
        self.rows = []

    def get_alignment(self, column: int) -> str:
        """Return the column alignment."""
        return self.column_alignment.get(column, "left")
