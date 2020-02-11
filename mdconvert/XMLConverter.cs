using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml.Linq;

namespace mdconvert
{
    /// <summary>
    /// An XMLConverter converts an intermediary XML file to a specific document representation, specified by a document builder and document settings. 
    /// </summary>
    internal class XMLConverter
    {
        private readonly XDocument document;
        private readonly XElement root;
        private static readonly IEnumerable<XStyle> EmptyStyleList = Array.Empty<XStyle>();
        private int listLevel = 0;

        private static readonly Dictionary<string, XStyle> TagToStyle = new Dictionary<string, XStyle>()
        {
            [XMLTags.TagBold] = XStyle.Bold,
            [XMLTags.TagItalic] = XStyle.Italic,
            [XMLTags.TagStrikethrough] = XStyle.Strikethrough,
            [XMLTags.TagInstruction] = XStyle.Instruction
        };

        public XMLConverter(string inputFilename)
        {
            document = XDocument.Load(inputFilename);
            root = document.Element(XMLTags.TagDocument);
        }

        public void Convert(IDocumentBuilder builder, DocumentSettings documentSettings)
        {
            XElement xTitle = root.Elements(XMLTags.TagTitle).FirstOrDefault();
            string title = xTitle?.Value ?? "";
            listLevel = 0;

            builder.StartDocument(title);

            XElement xFrontpage = root.Elements(XMLTags.TagFrontPage).FirstOrDefault();

            if (xFrontpage != null)
            {
                ConvertContent(xFrontpage, Context.FrontPage, builder, documentSettings);
            }

            if (documentSettings.IncludeTableOfContents)
            {
                builder.BuildTableOfContents();
            }

            XElement xHeader = root.Elements(XMLTags.TagHeader).FirstOrDefault();
            if (xHeader != null)
            {
                XParagraph headerP = ReadParagraph(xHeader);
                builder.BuildHeader(headerP);
            }

            XElement xFooter = root.Elements(XMLTags.TagFooter).FirstOrDefault();
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
#pragma warning disable CA1308 // Normalize strings to uppercase
                string n = element.Name.LocalName.ToLowerInvariant();
#pragma warning restore CA1308 // Normalize strings to uppercase
                switch (n)
                {
                    case XMLTags.TagParagraph:
                        builder.CreateParagraph(ReadParagraph(element), context);
                        break;

                    case XMLTags.TagSection:
                        ConvertSection(element, context, builder, documentSettings);
                        break;

                    case XMLTags.TagBulletList:
                        ConvertList(element, false, context, builder);
                        break;

                    case XMLTags.TagNumberedList:
                        ConvertList(element, true, context, builder);
                        break;

                    case XMLTags.TagTable:
                        ConvertTable(element, context, builder);
                        break;

                    case XMLTags.TagTitle:
                        builder.CreateParagraph(ReadParagraph(element), Context.Title);
                        break;

                    case XMLTags.TagPageBreak:
                        builder.InsertPageBreak();
                        break;

                    case XMLTags.TagImage:
                        builder.InsertPicture($"{documentSettings.ImagePath}{element.Value}");
                        break;
                }
            }
        }

        private static int ReadIntAttribute(XElement element, string name, int defaultValue)
        {
            string value = element.Attribute(name)?.Value;
            if (!int.TryParse(value, out int result))
            {
                result = defaultValue;
            }
            return result;
        }

        private static int ReadElementLevel(XElement element) => ReadIntAttribute(element, XMLTags.AttributeListLevel, 1);

        private void ConvertSection(XElement section, Context context, IDocumentBuilder builder, DocumentSettings documentSettings)
        {
            int level = ReadElementLevel(section);
            XAttribute appendix = section.Attribute(XMLTags.AttributeAppendix);
            bool isAppendix = appendix != null && appendix.Value.ToUpperInvariant() == "Y";

            XElement heading = section.Elements(XMLTags.TagHeading).FirstOrDefault();

            XParagraph headingParagraph;
            if (heading != null)
            {
                headingParagraph = ReadParagraph(heading);
                builder.CreateHeading(level, headingParagraph, isAppendix, context);
            }

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
#pragma warning disable CA1308 // Normalize strings to uppercase
                    string n = element.Name.LocalName.ToLowerInvariant();
#pragma warning restore CA1308 // Normalize strings to uppercase
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
                if (n.Equals(XMLTags.TagListItem, StringComparison.OrdinalIgnoreCase))
                {
                    builder.CreateListItem(level, numbered, ReadParagraph(element), context);
                }
                else if (n.Equals(XMLTags.TagBulletList, StringComparison.OrdinalIgnoreCase))
                {
                    ConvertList(element, false, context, builder);
                }
                else if (n.Equals(XMLTags.TagNumberedList, StringComparison.OrdinalIgnoreCase))
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
            int columns = ReadIntAttribute(tableElement, XMLTags.AttributeColumns, 1);
            //int rows = ReadIntAttribute(tableElement, Tags.AttributeRows, 0);

            if (columns > 0)
            {
                XElement headerRow = tableElement.Elements(XMLTags.TagTableHeaderRow).FirstOrDefault();
                XTable<XParagraph> table = new XTable<XParagraph>(ReadRow(headerRow));

                foreach (XElement row in tableElement.Elements(XMLTags.TagTableRow))
                {
                    table.AddRow(ReadRow(row));
                }

                builder.CreateTable(table, context);
            }
        }

        private XParagraph[] ReadRow(XElement row)
        {
            List<XParagraph> cells = new List<XParagraph>();
            foreach (XElement cell in row.Elements(XMLTags.TagTableCell))
            {
                cells.Add(ReadParagraph(cell));
            }
            return cells.ToArray();
        }
    }
}