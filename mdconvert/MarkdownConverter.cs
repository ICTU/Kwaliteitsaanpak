using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Xml;

namespace mdconvert
{
    /// <summary>
    /// Converts a collection of Markdown lines, usually the contents of a Markdown file, to an intermediary XML representation, that captures content
    /// and (some) semantics.
    /// </summary>
    internal class MarkdownConverter
    {
        private XmlWriter output;
        private int currentSectionLevel = 0;
        private int currentListLevel = 0;
        private bool in_bijlagen = false;
        private bool in_table = false;
        private bool in_measure = false;
        private XTable<string> table = null;

        // The name of the heading denoted the start of the appendix section.
        // Note: this should be part of the DocumentSettings.
        private const string AppendixHeading = "Bijlagen";


        private static readonly Dictionary<char, int> BulletLevel = new Dictionary<char, int>()
        {
            [MarkdownSyntax.BulletLevel1] = 1,
            [MarkdownSyntax.BulletLevel2] = 2,
            [MarkdownSyntax.BulletLevel3] = 3,
        };

        private static readonly Dictionary<TextAlignment, string> AlignmentToStr = new Dictionary<TextAlignment, string>()
        {
            [TextAlignment.Left] = XMLTags.AlignmentLeft,
            [TextAlignment.Center] = XMLTags.AlignmentCenter,
            [TextAlignment.Right] = XMLTags.AlignmentRight
        };

        public MarkdownConverter()
        {
        }

        /// <summary>
        /// Converts a collection of Markdown lines to an XML string.
        /// </summary>
        /// <param name="lines">The Markdown lines to be converted.</param>
        /// <param name="settings">Settings for the resulting document.</param>
        /// <returns>XML string representing the Markdown lines.</returns>
        public string Convert(IEnumerable<string> lines, DocumentSettings documentSettings)
        {
            StringBuilder stringBuilder = new StringBuilder();
            var settings = new XmlWriterSettings
            {
                OmitXmlDeclaration = true,
                Indent = true,
                IndentChars = "    ",
                NewLineOnAttributes = false
            };
            output = XmlWriter.Create(stringBuilder, settings);

            StartDocument(documentSettings);
            foreach (string line in lines)
            {
                ProcessLine(line, documentSettings);
            }
            EndDocument(documentSettings);

            output.Close();
            return stringBuilder.ToString();
        }

        /// <summary>
        /// Converts a Markdown file to an XML string.
        /// </summary>
        /// <param name="inputFilename">Name of the Markdown file to be converted.</param>
        /// <param name="settings">Settings for the resulting document.</param>
        /// <returns>XML string representing the Markdown file.</returns>
        public string ConvertFile(string inputFilename, DocumentSettings documentSettings)
        {
            List<string> lines = new List<string>();
            using (StreamReader input = new StreamReader(inputFilename))
            {
                string line;
                while ((line = input.ReadLine()) != null)
                {
                    lines.Add(line);
                }
            }
            return Convert(lines, documentSettings);
        }

        private void StartDocument(DocumentSettings documentSettings)
        {
            output.WriteStartElement(XMLTags.TagDocument);
            currentSectionLevel = 0;
            currentListLevel = 0;
            in_bijlagen = false;
            in_table = false;
            in_measure = false;

            if (!string.IsNullOrWhiteSpace(documentSettings.Title))
            {
                output.WriteAttributeString(XMLTags.AttributeTitle, documentSettings.Title);
            }

            CreateFrontPage(documentSettings);
            CreateHeader(documentSettings);
            CreateFooter();
        }

        private void CreateFrontPage(DocumentSettings documentSettings)
        {
            if (documentSettings.IncludeFrontPage)
            {
                output.WriteStartElement(XMLTags.TagFrontPage);

                switch (documentSettings.DocumentType)
                {
                    case DocumentType.Generic:
                        output.WriteElementString(XMLTags.TagTitle, documentSettings.Title);
                        output.WriteElementString(XMLTags.TagPageBreak, "");
                        break;

                    case DocumentType.Kwaliteitsaanpak:
                        output.WriteElementString(XMLTags.TagImage, "ICTU.png");
                        output.WriteElementString(XMLTags.TagTitle, documentSettings.Title);
                        output.WriteElementString(XMLTags.TagImage, "word-cloud.png");
                        output.WriteElementString(XMLTags.TagPageBreak, "");
                        break;

                    case DocumentType.Template:
                        output.WriteElementString(XMLTags.TagImage, "ICTU.png");
                        output.WriteElementString(XMLTags.TagTitle, documentSettings.Title);

                        output.WriteStartElement(XMLTags.TagParagraph);
                        output.WriteStartElement(XMLTags.TagInstruction);
                        output.WriteElementString(XMLTags.TagBold, "{Projectnaam}");
                        output.WriteEndElement();
                        output.WriteEndElement();

                        output.WriteElementString(XMLTags.TagParagraph, "");

                        output.WriteStartElement(XMLTags.TagParagraph);
                        output.WriteString("Versie ");
                        output.WriteElementString(XMLTags.TagInstruction, "{Versienummer}");
                        output.WriteEndElement();

                        output.WriteStartElement(XMLTags.TagParagraph);
                        output.WriteString("Datum ");
                        output.WriteElementString(XMLTags.TagInstruction, "{Datum}");
                        output.WriteEndElement();

                        output.WriteElementString(XMLTags.TagParagraph, "");

                        output.WriteElementString(XMLTags.TagImage, "word-cloud.png");
                        output.WriteElementString(XMLTags.TagPageBreak, "");
                        break;
                }

                output.WriteEndElement();
            }
        }

        private void CreateHeader(DocumentSettings documentSettings)
        {
            output.WriteStartElement(XMLTags.TagHeader);

            if (documentSettings.DocumentType == DocumentType.Template)
            {
                output.WriteStartElement(XMLTags.TagParagraph);
                output.WriteString($"{documentSettings.Title} ");
                output.WriteElementString(XMLTags.TagInstruction, "{Projectnaam}");
                output.WriteEndElement();
            }
            else
            {
                output.WriteElementString(XMLTags.TagParagraph, documentSettings.Title);
            }

            output.WriteEndElement();
        }

        private void CreateFooter()
        {
            output.WriteStartElement(XMLTags.TagFooter);
            output.WriteEndElement();
        }

        private void EndDocument(DocumentSettings documentSettings)
        {
            FinishAll(documentSettings);

            while (currentSectionLevel > 0)
            {
                output.WriteEndElement();
                currentSectionLevel--;
            }

            output.WriteEndElement();
        }

        private void FinishList()
        {
            while (currentListLevel > 0)
            {
                output.WriteEndElement();
                currentListLevel--;
            }
        }

        private void FinishTable(DocumentSettings documentSettings)
        {
            if (in_table)
            {
                FlushTable(documentSettings);
                table = null;
                in_table = false;
            }
        }

        private void FinishAll(DocumentSettings documentSettings)
        {
            FinishList();
            FinishTable(documentSettings);
        }

        private void ProcessLine(string line, DocumentSettings documentSettings)
        {
            int indent = line.TakeWhile(c => c == ' ').Count();
            string trimmedLine = line.Trim();
            bool ending_measure = false;

            if (!string.IsNullOrWhiteSpace(trimmedLine))
            {
                if (trimmedLine.StartsWith(MarkdownSyntax.MeasureStart, StringComparison.OrdinalIgnoreCase) && !in_measure)
                {
                    output.WriteStartElement(XMLTags.TagMeasure);
                    trimmedLine = trimmedLine.Substring(MarkdownSyntax.MeasureStart.Length);
                    in_measure = true;
                }

                if (trimmedLine.EndsWith(MarkdownSyntax.MeasureEnd, StringComparison.OrdinalIgnoreCase) && in_measure)
                {
                    ending_measure = true;
                    trimmedLine = trimmedLine.Substring(0, trimmedLine.Length - MarkdownSyntax.MeasureEnd.Length);
                }

                bool matched = MatchHeading(trimmedLine, documentSettings)
                        || MatchList(trimmedLine, indent, documentSettings)
                        || MatchTableRow(trimmedLine);

                if (!matched)
                {
                    FinishAll(documentSettings);
                    output.WriteStartElement(XMLTags.TagParagraph);

                    if (documentSettings.IncludeMarkdownSource)
                    {
                        output.WriteAttributeString(XMLTags.AttributeSource, line);
                    }

                    ProcessFormattedText(trimmedLine);
                    output.WriteEndElement();
                }

                if (in_measure && ending_measure)
                {
                    output.WriteEndElement();
                    in_measure = false;
                }
            }
        }

        private bool MatchHeading(string line, DocumentSettings documentSettings)
        {
            Match m = Regex.Match(line, MarkdownSyntax.HeadingPattern);
            if (m.Success)
            {
                int level = m.Length - 1;
                string heading = line.Substring(m.Length).Trim();

                if (level == 1)
                {
                    in_bijlagen = heading.Equals(AppendixHeading, StringComparison.OrdinalIgnoreCase);
                }

                FinishAll(documentSettings);

                if (currentSectionLevel >= level)
                {
                    while (currentSectionLevel > level)
                    {
                        output.WriteEndElement();
                        currentSectionLevel--;
                    }

                    output.WriteEndElement();
                    output.WriteStartElement(XMLTags.TagSection);
                    output.WriteAttributeString(XMLTags.AttributeSectionLevel, currentSectionLevel.ToString(CultureInfo.InvariantCulture));
                }
                else
                {
                    while (currentSectionLevel < level)
                    {
                        currentSectionLevel++;
                        output.WriteStartElement(XMLTags.TagSection);
                        output.WriteAttributeString(XMLTags.AttributeSectionLevel, currentSectionLevel.ToString(CultureInfo.InvariantCulture));
                    }
                }
                if (in_bijlagen)
                {
                    output.WriteAttributeString(XMLTags.AttributeAppendix, "y");
                }
                if (documentSettings.IncludeMarkdownSource)
                {
                    output.WriteAttributeString(XMLTags.AttributeSource, line);
                }
                output.WriteStartElement(XMLTags.TagHeading);
                ProcessFormattedText(heading);
                output.WriteEndElement();

                return true;
            }
            return false;
        }

        private static bool IsDigit(char c) => c >= '0' && c <= '9';

        private bool MatchList(string line, int indent, DocumentSettings documentSettings)
        {
            string tag;
            int listLevel;

            Match m = Regex.Match(line, MarkdownSyntax.BulletListPattern);
            if (m.Success)
            {
                tag = XMLTags.TagBulletList;
                listLevel = BulletLevel.GetValueOrDefault(line[0], MarkdownSyntax.BulletLevel1);
            }
            else
            {
                m = Regex.Match(line, MarkdownSyntax.NumberedListPattern);

                if (!m.Success)
                {
                    return false;
                }

                tag = XMLTags.TagNumberedList;
                listLevel = IsDigit(line[0]) ? ((indent == 0) ? 1 : 3) : 2;
            }

            string item = line.Substring(m.Length).Trim();

            while (currentListLevel < listLevel)
            {
                currentListLevel++;
                output.WriteStartElement(tag);
                output.WriteAttributeString(XMLTags.AttributeListLevel, currentListLevel.ToString(CultureInfo.InvariantCulture));
            }
            while (currentListLevel > listLevel)
            {
                output.WriteEndElement();
                currentListLevel--;
            }

            output.WriteStartElement(XMLTags.TagListItem);
            if (documentSettings.IncludeMarkdownSource)
            {
                output.WriteAttributeString(XMLTags.AttributeSource, line);
            }
            ProcessFormattedText(item);
            output.WriteEndElement();

            return true;
        }

        private bool MatchTableRow(string line)
        {
            if (line.StartsWith(MarkdownSyntax.TableMarker))
            {
                string[] cells = GetTableCells(line);
                if (cells.Length > 0)
                {
                    if (in_table)
                    {
                        ProcessTableRow(cells, line);
                    }
                    else
                    {
                        ProcessHeaderRow(cells, line);
                    }
                }
                return true;
            }

            return false;
        }

        private void ProcessHeaderRow(string[] cells, string source)
        {
            in_table = true;
            table = new XTable<string>(cells, source);
        }

        private void ProcessTableRow(string[] cells, string source)
        {
            if (cells[0].Contains("---", StringComparison.OrdinalIgnoreCase) && table.DataRowCount == 0)
            {
                for (int i = 0; i < cells.Length; i++)
                {
                    string c = cells[i];
                    if (c.StartsWith(MarkdownSyntax.CellAlignmentMarker) && c.EndsWith(MarkdownSyntax.CellAlignmentMarker))
                    {
                        table.SetAlignment(i, TextAlignment.Center);
                    }
                    else if (c.EndsWith(MarkdownSyntax.CellAlignmentMarker))
                    {
                        table.SetAlignment(i, TextAlignment.Right);
                    }
                    else
                    {
                        table.SetAlignment(i, TextAlignment.Left);
                    }
                }
            }
            else
            {
                table.AddRow(cells, source);
            }
        }

        private static string[] GetTableCells(string line)
        {
            line = line.Trim(MarkdownSyntax.TableMarker, ' ', '\t');
            string[] cells = line.Split(MarkdownSyntax.TableMarker);
            for (int i = 0; i < cells.Length; i++)
            {
                cells[i] = cells[i].Trim();
            }
            return cells;
        }

        private void FlushTable(DocumentSettings documentSettings)
        {
            output.WriteStartElement(XMLTags.TagTable);
            output.WriteAttributeString(XMLTags.AttributeColumns, table.ColumnCount.ToString(CultureInfo.InvariantCulture));
            output.WriteAttributeString(XMLTags.AttributeRows, table.RowCount.ToString(CultureInfo.InvariantCulture));

            output.WriteStartElement(XMLTags.TagTableHeaderRow);
            if (documentSettings.IncludeMarkdownSource)
            {
                output.WriteAttributeString(XMLTags.AttributeSource, table.HeaderSource);
            }

            int column = 0;
            foreach (string headerCell in table.HeaderCells)
            {
                output.WriteStartElement(XMLTags.TagTableCell);
                output.WriteAttributeString(XMLTags.AttributeColumnAlignment,
                    AlignmentToStr.GetValueOrDefault(table.GetAlignment(column), XMLTags.AlignmentLeft));
                ProcessFormattedText(headerCell);
                output.WriteEndElement();
                column++;
            }

            output.WriteEndElement();

            for (int r = 0; r < table.RowCount; r++)
            {
                string[] cells = table.GetRowCells(r);

                output.WriteStartElement(XMLTags.TagTableRow);
                if (documentSettings.IncludeMarkdownSource)
                {
                    output.WriteAttributeString(XMLTags.AttributeSource, table.GetRowSource(r));
                }

                foreach (string cell in cells)
                {
                    output.WriteStartElement(XMLTags.TagTableCell);
                    ProcessFormattedText(cell);
                    output.WriteEndElement();
                }
                output.WriteEndElement();
            }

            output.WriteEndElement();
        }

        private string buffer = "";
        private int pos = 0;
        private bool is_bold = false;
        private bool is_italic = false;
        private bool is_strikethrough = false;
        private bool is_instruction = false;

        private void Flush()
        {
            if (!string.IsNullOrEmpty(buffer))
            {
                output.WriteString(buffer);
            }
            buffer = "";
        }

        private void StartStyle(string markup, string tag)
        {
            Flush();
            output.WriteStartElement(tag);
            pos += markup.Length;
        }

        private void EndStyle(string markup)
        {
            Flush();
            output.WriteEndElement();
            pos += markup.Length;
        }

        private void Link(string markup, string anchor, string link)
        {
            Flush();
            output.WriteStartElement(XMLTags.TagAnchor);
            output.WriteAttributeString(XMLTags.AttributeLink, link);
            output.WriteString(anchor);
            output.WriteEndElement();
            pos += markup.Length;
        }

        private void ProcessFormattedText(string text)
        {
            buffer = "";
            pos = 0;
            is_bold = false;
            is_italic = false;
            is_strikethrough = false;
            is_instruction = false;

            while (pos < text.Length)
            {
                string current = $"{text[pos]}";
                string current2 = (pos < text.Length - 1) ? $"{current}{text[pos + 1]}" : "";

                if (current2.Equals(MarkdownSyntax.Bold, StringComparison.OrdinalIgnoreCase) || current2.Equals(MarkdownSyntax.BoldAlternative, StringComparison.OrdinalIgnoreCase))
                {
                    if (is_bold)
                    {
                        EndStyle(current2);
                        is_bold = false;
                        continue;
                    }
                    else if (text.Substring(pos + 2).Contains(current2, StringComparison.OrdinalIgnoreCase))
                    {
                        StartStyle(current2, XMLTags.TagBold);
                        is_bold = true;
                        continue;
                    }
                }
                else if (current2.Equals(MarkdownSyntax.Strikethrough, StringComparison.OrdinalIgnoreCase))
                {
                    if (is_strikethrough)
                    {
                        EndStyle(current2);
                        is_strikethrough = false;
                        continue;
                    }
                    else if (text.Substring(pos + 2).Contains(current2, StringComparison.OrdinalIgnoreCase))
                    {
                        StartStyle(current2, XMLTags.TagStrikethrough);
                        is_strikethrough = true;
                        continue;
                    }
                }
                else if (current.Equals(MarkdownSyntax.Italic, StringComparison.OrdinalIgnoreCase) || current.Equals(MarkdownSyntax.ItalicAlternative, StringComparison.OrdinalIgnoreCase))
                {
                    if (is_italic)
                    {
                        EndStyle(current);
                        is_italic = false;
                        continue;
                    }
                    else if (text.Substring(pos + 1).Contains(current, StringComparison.OrdinalIgnoreCase))
                    {
                        StartStyle(current, XMLTags.TagItalic);
                        is_italic = true;
                        continue;
                    }
                }
                else if (current.Equals(MarkdownSyntax.InstructionStart, StringComparison.OrdinalIgnoreCase)
                    && text.Substring(pos + 1).Contains(MarkdownSyntax.InstructionEnd, StringComparison.OrdinalIgnoreCase))
                {
                    StartStyle(current, XMLTags.TagInstruction);
                    buffer += MarkdownSyntax.InstructionStart;
                    is_instruction = true;
                    continue;
                }
                else if (current.Equals(MarkdownSyntax.InstructionEnd, StringComparison.OrdinalIgnoreCase) && is_instruction)
                {
                    buffer += MarkdownSyntax.InstructionEnd;
                    EndStyle(MarkdownSyntax.InstructionEnd);
                    is_instruction = false;
                    continue;
                } else {
                    Match m = Regex.Match(text.Substring(pos), MarkdownSyntax.LinkPattern);
                    if (m.Success)
                    {
                        Link(m.Value, m.Groups[1].Value, m.Groups[2].Value);
                        continue;
                    }
                }

                buffer += current;
                pos += 1;
            }

            Flush();
        }
    }
}