using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace mdconvert.Builders
{
    class MarkdownBuilder : IDocumentBuilder
    {
        private readonly string filename;
        private const int MaxLevel = 3;
        private StringBuilder doc;
        private bool listItemBefore = false;
        private int[] listItemCount = new int[MaxLevel+1];
        private Context previousContext = Context.Regular;
        private static readonly IEnumerable<XStyle> EmptyStyleList = new XStyle[0];

        private static readonly Dictionary<XStyle, string> StyleToMarkdownMapping = new Dictionary<XStyle, string>()
        {
            [XStyle.Bold] = Markdown.Bold,
            [XStyle.Italic] = Markdown.Italic,
            [XStyle.Strikethrough] = Markdown.Strikethrough,
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

        public void BuildFrontPage(XParagraph title)
        {
            // Markdown documents don't have front pages.
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
        }

        public void CreateHeading(int level, XParagraph paragraph, bool isAppendix, Context context)
        {
            doc.AppendLine($"{Repeat("#", level)} {Format(paragraph)}");
            doc.AppendLine();
            previousContext = context;
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

            switch(level)
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
            previousContext = context;
        }

        public void CreateParagraph(XParagraph paragraph, Context context)
        {
            doc.AppendLine(Format(paragraph));
            doc.AppendLine();
            previousContext = context;
        }

        public void CreateTable(XTable<XParagraph> table, Context context)
        {
            string headerRow = "";
            string alignmentRow = "";
            for (int i = 0; i < table.ColumnCount; i++)
            {
                string f = Format(table.HeaderCells[i]);
                headerRow += $"{Markdown.TableMarker} {f} ";
                alignmentRow += $"{Markdown.TableMarker}{Repeat("-", f.Length + 2)}";
            }
            headerRow += Markdown.TableMarker;
            alignmentRow += Markdown.TableMarker;
            doc.AppendLine(headerRow);
            doc.AppendLine(alignmentRow);

            for (int r = 0; r < table.RowCount; r++)
            {
                string dataRow = "";
                XParagraph[] row = table.GetRowCells(r);
                for (int c = 0; c < row.Length; c++)
                {
                    dataRow += $"{Markdown.TableMarker} { Format(row[c])} ";
                }
                dataRow += Markdown.TableMarker;
                doc.AppendLine(dataRow);
            }

            doc.AppendLine();
            previousContext = context;
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
            for(int i = 0; i< paragraph.NumFragments; i++)
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
            foreach(XStyle style in styles)
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

        private static string ContextPrefix(Context previousContext, Context currentContext) 
            => previousContext != Context.Measure && currentContext == Context.Measure ? Markdown.MeasureStart : "";

        private static string ContextSuffix(Context currentContext, Context nextContext)
            => currentContext == Context.Measure && nextContext != Context.Measure ? Markdown.MeasureEnd : "";
    }
}
