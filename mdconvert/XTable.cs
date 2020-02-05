using System;
using System.Collections.Generic;
using System.Linq;

namespace mdconvert
{
    public class XTable<T>
    {
        private readonly List<T[]> rows = new List<T[]>();
        private readonly List<string> rowSource = new List<string>();
        private readonly TextAlignment[] columnAlignment = Array.Empty<TextAlignment>();

        public XTable(T[] headerCells, string headerSource = "")
        {
            HeaderCells = headerCells;
            HeaderSource = headerSource;
            columnAlignment = new TextAlignment[headerCells != null ? headerCells.Length : 0];
        }

        public IEnumerable<T> HeaderCells { get; private set; } = Array.Empty<T>();

        public string HeaderSource { get; private set; }

        public int RowCount => rows.Count;

        public int ColumnCount => HeaderCells.Count();

        public int DataRowCount => rows.Count;

        public void AddRow(T[] cells, string source = "")
        {
            rows.Add(cells);
            rowSource.Add(source);
        }

        public T[] GetRowCells(int row)
        {
            return rows[row];
        }

        public string GetRowSource(int row)
        {
            return rowSource[row];
        }

        public void SetAlignment(int column, TextAlignment alignment)
        {
            if (column >= 0 && column < ColumnCount)
            {
                columnAlignment[column] = alignment;
            }
        }

        public TextAlignment GetAlignment(int column)
            => column >= 0 && column < ColumnCount ? columnAlignment[column] : TextAlignment.Left;
    }
}