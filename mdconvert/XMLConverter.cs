using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml.Linq;

namespace mdconvert
{
    class XMLConverter
    {
        private readonly XDocument document;
        private readonly XElement root;
        private static readonly IEnumerable<XStyle> EmptyStyleList = new XStyle[0];
        private int listLevel = 0;

        private static readonly Dictionary<string, XStyle> TagToStyle = new Dictionary<string, XStyle>()
        {
            [Tags.TagBold] = XStyle.Bold,
            [Tags.TagItalic] = XStyle.Italic,
            [Tags.TagStrikethrough] = XStyle.Strikethrough,
            [Tags.TagInstruction] = XStyle.Instruction
        };

        public XMLConverter(string inputFilename)
        {
            document = XDocument.Load(inputFilename);
            root = document.Element(Tags.TagDocument); 
        }

        public void Convert(IDocumentBuilder builder, DocumentSettings documentSettings)
        {
            XElement xTitle = root.Elements(Tags.TagTitle).FirstOrDefault();
            string title = xTitle?.Value ?? "";
            listLevel = 0;

            builder.StartDocument(title);

            XElement xFrontpage = root.Elements(Tags.TagFrontPage).FirstOrDefault();

            if (xFrontpage != null)
            {
                ConvertContent(xFrontpage, Context.FrontPage, builder, documentSettings);
            }

            if (documentSettings.IncludeTableOfContents)
            {
                builder.BuildTableOfContents();
            }

            XElement xHeader = root.Elements(Tags.TagHeader).FirstOrDefault();
            if (xHeader != null)
            {
                XParagraph headerP = ReadParagraph(xHeader);
                builder.BuildHeader(headerP);
            }

            XElement xFooter = root.Elements(Tags.TagFooter).FirstOrDefault();
            if (xFooter != null)
            {
                builder.BuildFooter();
            }

            ConvertContent(root, Context.Regular, builder, documentSettings);

            builder.EndDocument();
        }

        private void ConvertContent(XElement parent, Context context, IDocumentBuilder builder, DocumentSettings documentSettings)
        {
            foreach (XElement element in parent.Elements())
            {
                string n = element.Name.LocalName.ToLower();
                switch (n)
                {
                    case Tags.TagParagraph:
                        builder.CreateParagraph(ReadParagraph(element), context);
                        break;
                    case Tags.TagSection:
                        ConvertSection(element, context, builder, documentSettings);
                        break;
                    case Tags.TagBulletList:
                        ConvertList(element, false, context, builder);
                        break;
                    case Tags.TagNumberedList:
                        ConvertList(element, true, context, builder);
                        break;
                    case Tags.TagTable:
                        ConvertTable(element, context, builder);
                        break;
                    case Tags.TagTitle:
                        builder.CreateParagraph(ReadParagraph(element), Context.Title);
                        break;
                    case Tags.TagPageBreak:
                        builder.InsertPageBreak();
                        break;
                    case Tags.TagImage:
                        builder.InsertPicture($"{documentSettings.ImagePath}/{element.Value}");
                        break;
                }           
            }
        }       

        private int ReadIntAttribute(XElement element, string name, int defaultValue)
        {
            int result = defaultValue;
            string value = element.Attribute(name)?.Value;
            int.TryParse(value, out result);
            return result;
        }

        private int ReadElementLevel(XElement element) => ReadIntAttribute(element, Tags.AttributeListLevel, 1);

        private void ConvertSection(XElement section, Context context, IDocumentBuilder builder, DocumentSettings documentSettings)
        {
            int level = ReadElementLevel(section);
            XAttribute appendix = section.Attribute(Tags.AttributeAppendix);
            bool isAppendix = appendix != null && appendix.Value.ToLower() == "y";

            XElement heading = section.Elements(Tags.TagHeading).FirstOrDefault();

            XParagraph headingParagraph = null;
            if (heading != null)
            {
                headingParagraph = ReadParagraph(heading);
                builder.CreateHeading(level, headingParagraph, isAppendix, context);
            }

            //Console.WriteLine($"Converting section level {level}: {(headingParagraph != null ? headingParagraph.ToString() : "")}");

            ConvertContent(section, context, builder, documentSettings);
        }

        private XParagraph ReadParagraph(XElement parent)
        {
            XParagraph result = new XParagraph();
            BuildParagraph(result, EmptyStyleList, parent);
            return result;
        }

        private void BuildParagraph(XParagraph paragraph, IEnumerable<XStyle> styles, XElement parent)
        {
            foreach (XNode node in parent.Nodes())
            {
                if (node is XText textNode)
                {
                    paragraph.Add(new XFragment(textNode.Value, styles));
                }
                else if (node is XElement element)
                {
                    string n = element.Name.LocalName.ToLower();
                    XStyle s = TagToStyle.GetValueOrDefault(n, XStyle.None);
                    BuildParagraph(paragraph, styles.Append(s), element);
                }
            }
        }

        private void ConvertList(XElement list, bool numbered, Context context, IDocumentBuilder builder)
        {
            if (listLevel == 0)
            {
                builder.StartList(numbered);
            }
            listLevel++;

            int level = ReadElementLevel(list);

            foreach (XElement element in list.Elements())
            {
                string n = element.Name.LocalName;
                if (n.Equals(Tags.TagListItem, StringComparison.OrdinalIgnoreCase))
                {
                    builder.CreateListItem(level, numbered, ReadParagraph(element), context);
                }
                else if (n.Equals(Tags.TagBulletList, StringComparison.OrdinalIgnoreCase))
                {
                    ConvertList(element, false, context, builder);
                }
                else if (n.Equals(Tags.TagNumberedList, StringComparison.OrdinalIgnoreCase))
                {
                    ConvertList(element, true, context, builder);
                }
            }

            listLevel--;

            if (listLevel == 0)
            {
                builder.EndList();
            }
        }

        private void ConvertTable(XElement tableElement, Context context, IDocumentBuilder builder)
        {
            int columns = ReadIntAttribute(tableElement, Tags.AttributeColumns, 1);
            int rows = ReadIntAttribute(tableElement, Tags.AttributeRows, 0);

            if (columns > 0)
            {
                XElement headerRow = tableElement.Elements(Tags.TagTableHeaderRow).FirstOrDefault();
                XTable<XParagraph> table = new XTable<XParagraph>(ReadRow(headerRow));

                foreach (XElement row in tableElement.Elements(Tags.TagTableRow))
                {
                    table.AddRow(ReadRow(row));
                }

                builder.CreateTable(table, context);
            }
        }

        private XParagraph[] ReadRow(XElement row)
        {
            List<XParagraph> cells = new List<XParagraph>();
            foreach (XElement cell in row.Elements(Tags.TagTableCell))
            {
                cells.Add(ReadParagraph(cell));
            }
            return cells.ToArray();
        }
    }
}
