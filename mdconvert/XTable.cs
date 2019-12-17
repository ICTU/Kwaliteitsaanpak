using System;
using System.Collections.Generic;
using System.Text;

namespace mdconvert
{
    public class XTable<T>
    {
        private readonly List<T[]> rows = new List<T[]>();
        private readonly List<string> rowSource = new List<string>();
        private readonly Alignment[] columnAlignment = new Alignment[0];

        public XTable(T[] headerCells, string headerSource = "")
        {
            HeaderCells = headerCells;
            HeaderSource = headerSource;
            columnAlignment = new Alignment[headerCells.Length];
        }

        public T[] HeaderCells { get; private set; } = new T[0];

        public string HeaderSource { get; private set; }

        public int RowCount => rows.Count;

        public int ColumnCount => HeaderCells.Length;

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

        public void SetAlignment(int column, Alignment alignment)
        {
            if (column >= 0 && column < ColumnCount)
            {
                columnAlignment[column] = alignment;
            }
        }

        public Alignment GetAlignment(int column) 
            => column >= 0 && column < ColumnCount ? columnAlignment[column] : Alignment.Left;
    }
}
