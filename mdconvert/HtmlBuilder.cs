using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Xml;

namespace mdconvert.Builders
{
    class HtmlBuilder : IDocumentBuilder
    {
        private readonly XmlWriter output;
        private readonly StringBuilder stringBuilder;
        private readonly string filename;

        private static readonly IEnumerable<XStyle> EmptyStyleList = new XStyle[0];

        private const string HtmlDocument = "html";
        private const string HtmlHead = "head";
        private const string HtmlTitle = "title";
        private const string HtmlStyle = "style";
        private const string HtmlBody = "body";
        private const string HtmlParagraph = "p";
        private const string HtmlHeading_Partial = "h";
        private const string HtmlBold = "b";
        private const string HtmlItalic = "i";
        private const string HtmlStrikethrough = "del";
        private const string HtmlTable = "table";
        private const string HtmlTableRow = "tr";
        private const string HtmlTableHeading = "th";
        private const string HtmlTableData = "td";
        private const string StyleInstruction = "instruction";

        private static readonly Dictionary<XStyle, string> StyleToHtmlMapping = new Dictionary<XStyle, string>()
        {
            [XStyle.Bold] = HtmlBold,
            [XStyle.Italic] = HtmlItalic,
            [XStyle.Strikethrough] = HtmlStrikethrough,
        };

        public HtmlBuilder(string filename)
        {
            this.filename = filename;
            stringBuilder = new StringBuilder();
            var settings = new XmlWriterSettings
            {
                OmitXmlDeclaration = true,
                Indent = true,
                IndentChars = "    ",
                NewLineOnAttributes = false
            };
            output = XmlWriter.Create(stringBuilder, settings);
        }

        public string Extension => "html";

        public void StartDocument(string title)
        {
            Console.WriteLine("Starting html document");
            output.WriteStartElement(HtmlDocument);
            output.WriteStartElement(HtmlHead);
            output.WriteElementString(HtmlTitle, title);

            output.WriteStartElement(HtmlStyle);
            output.WriteString($"{HtmlBody} {{ font-family: Verdana, Geneva, sans-serif; }} ");
            output.WriteString($"{HtmlTable}, {HtmlTableHeading}, {HtmlTableData} {{ border: 1px solid black; }} ");
            output.WriteString($".{StyleInstruction} {{ background: #ffff00; }} ");
            output.WriteEndElement(); // style

            output.WriteEndElement(); // head
            output.WriteStartElement(HtmlBody);
        }

        public void EndDocument()
        {
            output.WriteEndElement(); // Body
            output.WriteEndElement(); // Html

            output.Close();
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
            writer.WriteLine(stringBuilder.ToString());
            writer.Close();
        }

        public void BuildFrontPage(XParagraph title)
        {
        }

        public void BuildHeader(XParagraph header)
        {
        }

        public void BuildFooter()
        {
        }

        public void BuildTableOfContents()
        {
        }

        public void CreateHeading(int level, XParagraph paragraph, bool isAppendix, Context context)
        {
            output.WriteStartElement($"{HtmlHeading_Partial}{level}");
            Format(paragraph);
            output.WriteEndElement();
        }

        public void StartList(bool numbered)
        {
        }

        public void EndList()
        {
        }

        public void CreateListItem(int level, bool numbered, XParagraph paragraph, Context context)
        {
        }

        public void CreateParagraph(XParagraph paragraph, Context context)
        {
            output.WriteStartElement(HtmlParagraph);
            Format(paragraph);
            output.WriteEndElement();
        }

        public void CreateTable(XTable<XParagraph> table, Context context)
        {
            output.WriteStartElement(HtmlTable);
            output.WriteAttributeString("style", "width:100%");

            output.WriteStartElement(HtmlTableRow);
            foreach(XParagraph headerCell in table.HeaderCells)
            {
                output.WriteStartElement(HtmlTableHeading);
                Format(headerCell);
                output.WriteEndElement(); // th
            }
            output.WriteEndElement(); // tr

            for (int r= 0; r<table.DataRowCount; r++)
            {
                output.WriteStartElement(HtmlTableRow);
                foreach (XParagraph dataCell in table.GetRowCells(r))
                {
                    output.WriteStartElement(HtmlTableData);
                    Format(dataCell);
                    output.WriteEndElement(); // td
                }
                output.WriteEndElement(); // tr
            }

            output.WriteEndElement(); // table
        }

        public void InsertPageBreak()
        {
        }

        public void InsertPicture(string name)
        {
        }

        private void Format(XParagraph paragraph)
        {
            for (int i = 0; i < paragraph.NumFragments; i++)
            {
                IEnumerable<XStyle> previousStyles = (i > 0)
                    ? paragraph.Get(i - 1).Styles
                    : EmptyStyleList;
                IEnumerable<XStyle> nextStyles = (i < paragraph.NumFragments - 1)
                    ? paragraph.Get(i + 1).Styles
                    : EmptyStyleList;
                Format(paragraph.Get(i), previousStyles, nextStyles);
            }
        }

        private void Format(XFragment fragment, IEnumerable<XStyle> previousStyles, IEnumerable<XStyle> nextStyles)
        {
            IEnumerable<XStyle> stylesStarted = fragment.Styles.Where(s => !previousStyles.Contains(s));
            IEnumerable<XStyle> stylesEnded = fragment.Styles.Where(s => !nextStyles.Contains(s));

            StartStyles(stylesStarted);
            output.WriteString(fragment.Text);
            EndStyles(stylesEnded);
        }

        private void StartStyles(IEnumerable<XStyle> styles)
        {
            foreach (XStyle style in styles)
            {
                StartStyle(style);
            }
        }

        private void EndStyles(IEnumerable<XStyle> styles)
        {
            foreach (XStyle style in styles.Reverse())
            {
                switch (style)
                {
                    case XStyle.Bold:
                    case XStyle.Italic:
                    case XStyle.Strikethrough:
                    case XStyle.Instruction:
                        output.WriteEndElement();
                        break;
                }
            }
        }

        private void StartStyle(XStyle style)
        {
            switch (style)
            {
                case XStyle.Bold:
                case XStyle.Italic:
                case XStyle.Strikethrough:
                    output.WriteStartElement(StyleToHtmlMapping[style]);
                    break;
                case XStyle.Instruction:
                    output.WriteStartElement("span");
                    output.WriteAttributeString("class", StyleInstruction);
                    break;
            }
        }
    }
}
