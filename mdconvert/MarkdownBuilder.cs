using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace mdconvert.Builders
{
    /// <summary>
    /// Document builder for Markdown documents. 
    /// </summary>
    internal class MarkdownBuilder : IDocumentBuilder
    {
        private readonly string filename;
        private const int MaxLevel = 3;
        private readonly StringBuilder doc;
        private bool listItemBefore = false;
        private readonly int[] listItemCount = new int[MaxLevel + 1];
        private static readonly IEnumerable<XStyle> EmptyStyleList = Array.Empty<XStyle>();

        private static readonly Dictionary<XStyle, string> StyleToMarkdownMapping = new Dictionary<XStyle, string>()
        {
            [XStyle.Bold] = MarkdownSyntax.Bold,
            [XStyle.Italic] = MarkdownSyntax.Italic,
            [XStyle.Strikethrough] = MarkdownSyntax.Strikethrough,
        };

        public MarkdownBuilder(string filename)
        {
            this.filename = filename;
            doc = new StringBuilder();
        }

        public string Extension => "md";

        public void StartDocument(string title)
        {
        }

        public void EndDocument()
        {
            WriteDocument();
        }

        private void WriteDocument()
        {
            StreamWriter writer;
            if (filename != null)
            {
                writer = new StreamWriter(filename);
            }
            else
            {
                writer = new StreamWriter(Console.OpenStandardOutput())
                {
                    AutoFlush = true
                };
                Console.SetOut(writer);
            }
            writer.WriteLine(doc.ToString());
            writer.Close();
        }

        public void BuildHeader(XParagraph header)
        {
            // Markdown documents don't have headers.
        }

        public void BuildFooter()
        {
            // Markdown documents don't have footers.
        }

        public void BuildTableOfContents()
        {
            // Markdown documents don't have tables of contents.
        }

        public void CreateHeading(int level, XParagraph paragraph, bool isAppendix, Context context)
        {
            doc.AppendLine($"{Repeat("#", level)} {Format(paragraph)}");
            doc.AppendLine();
        }

        public void StartList(bool numbered)
        {
        }

        public void EndList()
        {
            if (listItemBefore)
            {
                doc.AppendLine();
                for (int i = 0; i < listItemCount.Length; i++)
                {
                    listItemCount[i] = 0;
                }
                listItemBefore = false;
            }
        }

        public void CreateListItem(int level, bool numbered, XParagraph paragraph, Context context)
        {
            string prefix = "";

            listItemCount[level]++;

            switch (level)
            {
                case 1:
                    prefix = numbered ? $"{listItemCount[level]}." : "*";
                    break;

                case 2:
                    prefix = numbered ? "  a." : "  +";
                    break;

                case 3:
                    prefix = numbered ? $"    {listItemCount[level]}." : "    -";
                    break;
            }
            doc.AppendLine($"{prefix} {Format(paragraph)}");

            listItemBefore = true;
        }

        public void CreateParagraph(XParagraph paragraph, Context context)
        {
            doc.AppendLine(Format(paragraph));
            doc.AppendLine();
        }

        public void CreateTable(XTable<XParagraph> table, Context context)
        {
            string headerRow = "";
            string alignmentRow = "";

            foreach (XParagraph headerCell in table.HeaderCells)
            {
                string f = Format(headerCell);
                headerRow += $"{MarkdownSyntax.TableMarker} {f} ";
                alignmentRow += $"{MarkdownSyntax.TableMarker}{Repeat("-", f.Length + 2)}";
            }

            headerRow += MarkdownSyntax.TableMarker;
            alignmentRow += MarkdownSyntax.TableMarker;
            doc.AppendLine(headerRow);
            doc.AppendLine(alignmentRow);

            for (int r = 0; r < table.RowCount; r++)
            {
                string dataRow = "";
                XParagraph[] row = table.GetRowCells(r);
                for (int c = 0; c < row.Length; c++)
                {
                    dataRow += $"{MarkdownSyntax.TableMarker} { Format(row[c])} ";
                }
                dataRow += MarkdownSyntax.TableMarker;
                doc.AppendLine(dataRow);
            }

            doc.AppendLine();
        }

        public void InsertPageBreak()
        {
        }

        public void InsertPicture(string name)
        {
        }

        private static string Format(XParagraph paragraph)
        {
            string result = "";
            for (int i = 0; i < paragraph.NumFragments; i++)
            {
                IEnumerable<XStyle> previousStyles = (i > 0)
                    ? paragraph.Get(i - 1).Styles
                    : EmptyStyleList;
                IEnumerable<XStyle> nextStyles = (i < paragraph.NumFragments - 1)
                    ? paragraph.Get(i + 1).Styles
                    : EmptyStyleList;
                result += Format(paragraph.Get(i), previousStyles, nextStyles);
            }
            return result;
        }

        private static string Format(XFragment fragment, IEnumerable<XStyle> previousStyles, IEnumerable<XStyle> nextStyles)
        {
            IEnumerable<XStyle> stylesStarted = fragment.Styles.Where(s => !previousStyles.Contains(s));
            IEnumerable<XStyle> stylesEnded = fragment.Styles.Where(s => !nextStyles.Contains(s));
            return $"{StylesToPrefix(stylesStarted)}{fragment.Text}{StylesToSuffix(stylesEnded)}";
        }

        private static string StylesToPrefix(IEnumerable<XStyle> styles)
        {
            string result = "";
            foreach (XStyle style in styles)
            {
                result += StyleToMarkdown(style);
            }
            return result;
        }

        private static string StylesToSuffix(IEnumerable<XStyle> styles)
        {
            string result = "";
            foreach (XStyle style in styles.Reverse())
            {
                result += StyleToMarkdown(style);
            }
            return result;
        }

        private static string StyleToMarkdown(XStyle style)
            => StyleToMarkdownMapping.GetValueOrDefault(style, "");

        private static string Repeat(string value, int count)
        {
            return new StringBuilder(value.Length * count).Insert(0, value, count).ToString();
        }
    }
}