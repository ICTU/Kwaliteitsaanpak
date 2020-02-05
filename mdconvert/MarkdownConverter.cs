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
    class MarkdownConverter
    {
        private XmlWriter output;
        private int currentSectionLevel = 0;
        private int currentListLevel = 0;
        private bool in_bijlagen = false;
        private bool in_table = false;
        private bool in_measure = false;
        private XTable<string> table = null;

        private static readonly Dictionary<char, int> BulletLevel = new Dictionary<char, int>()
        {
            [Markdown.BulletLevel1] = 1,
            [Markdown.BulletLevel2] = 2,
            [Markdown.BulletLevel3] = 3,
        };

        private static readonly Dictionary<Alignment, string> AlignmentToStr = new Dictionary<Alignment, string>()
        {
            [Alignment.Left] = Tags.AlignmentLeft,
            [Alignment.Center] = Tags.AlignmentCenter,
            [Alignment.Right] = Tags.AlignmentRight
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
            foreach(string line in lines)
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
            output.WriteStartElement(Tags.TagDocument);
            currentSectionLevel = 0;
            currentListLevel = 0;
            in_bijlagen = false;
            in_table = false;
            in_measure = false;

            if (!string.IsNullOrWhiteSpace(documentSettings.Title))
            {
                output.WriteAttributeString(Tags.AttributeTitle, documentSettings.Title);
            }

            CreateFrontPage(documentSettings);
            CreateHeader(documentSettings);
            CreateFooter();
        }

        private void CreateFrontPage(DocumentSettings documentSettings)
        {
            if (documentSettings.IncludeFrontPage)
            {
                output.WriteStartElement(Tags.TagFrontPage);

                switch (documentSettings.DocumentType)
                {
                    case DocumentType.Generic:
                        output.WriteElementString(Tags.TagTitle, documentSettings.Title);
                        output.WriteElementString(Tags.TagPageBreak, "");
                        break;

                    case DocumentType.Kwaliteitsaanpak:
                        output.WriteElementString(Tags.TagImage, "ICTU.png");
                        output.WriteElementString(Tags.TagTitle, documentSettings.Title);
                        output.WriteElementString(Tags.TagImage, "word-cloud.png");
                        output.WriteElementString(Tags.TagPageBreak, "");
                        break;

                    case DocumentType.Template:
                        output.WriteElementString(Tags.TagImage, "ICTU.png");
                        output.WriteElementString(Tags.TagTitle, documentSettings.Title);

                        output.WriteStartElement(Tags.TagParagraph);
                        output.WriteStartElement(Tags.TagInstruction);
                        output.WriteElementString(Tags.TagBold, "{Projectnaam}");
                        output.WriteEndElement();
                        output.WriteEndElement();

                        output.WriteElementString(Tags.TagParagraph, "");

                        output.WriteStartElement(Tags.TagParagraph);
                        output.WriteString("Versie ");
                        output.WriteElementString(Tags.TagInstruction, "{Versienummer}");
                        output.WriteEndElement();

                        output.WriteStartElement(Tags.TagParagraph);
                        output.WriteString("Datum ");
                        output.WriteElementString(Tags.TagInstruction, "{Datum}");
                        output.WriteEndElement();

                        output.WriteElementString(Tags.TagParagraph, "");

                        output.WriteElementString(Tags.TagImage, "word-cloud.png");
                        output.WriteElementString(Tags.TagPageBreak, "");
                        break;
                }

                output.WriteEndElement();
            }
        }

        private void CreateHeader(DocumentSettings documentSettings)
        {
            output.WriteStartElement(Tags.TagHeader);

            if (documentSettings.DocumentType == DocumentType.Template)
            {
                output.WriteStartElement(Tags.TagParagraph);
                output.WriteString($"{documentSettings.Title} ");
                output.WriteElementString(Tags.TagInstruction, "{Projectnaam}");
                output.WriteEndElement();
            }
            else
            {
                output.WriteElementString(Tags.TagParagraph, documentSettings.Title);
            }

            output.WriteEndElement();
        }

        private void CreateFooter()
        {
            output.WriteStartElement(Tags.TagFooter);
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
                if (trimmedLine.StartsWith(Markdown.MeasureStart, StringComparison.OrdinalIgnoreCase) && !in_measure)
                {
                    output.WriteStartElement(Tags.TagMeasure);
                    trimmedLine = trimmedLine.Substring(Markdown.MeasureStart.Length);
                    in_measure = true;
                }

                if (trimmedLine.EndsWith(Markdown.MeasureEnd, StringComparison.OrdinalIgnoreCase) && in_measure)
                {
                    ending_measure = true;
                    trimmedLine = trimmedLine.Substring(0, trimmedLine.Length - Markdown.MeasureEnd.Length);
                }

                bool matched = MatchHeading(trimmedLine, documentSettings)
                        || MatchList(trimmedLine, indent, documentSettings)
                        || MatchTableRow(trimmedLine);

                if (!matched)
                {
                    FinishAll(documentSettings);
                    output.WriteStartElement(Tags.TagParagraph);

                    if (documentSettings.IncludeMarkdownSource)
                    {
                        output.WriteAttributeString(Tags.AttributeSource, line);
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
            Match m = Regex.Match(line, Markdown.HeadingPattern);
            if (m.Success)
            {
                int level = m.Length - 1;
                string heading = line.Substring(m.Length).Trim();

                if (level == 1)
                {
                    in_bijlagen = heading.Equals(Tags.AppendixHeading, StringComparison.OrdinalIgnoreCase);
                }

                //Console.WriteLine($"Matched heading '{heading}', level {level}, in_bijlagen {in_bijlagen}");

                FinishAll(documentSettings);

                if (currentSectionLevel >= level)
                {
                    while (currentSectionLevel > level)
                    {
                        output.WriteEndElement();
                        currentSectionLevel--;
                    }

                    output.WriteEndElement();
                    output.WriteStartElement(Tags.TagSection);
                    output.WriteAttributeString(Tags.AttributeSectionLevel, currentSectionLevel.ToString(CultureInfo.InvariantCulture));
                }
                else
                {
                    while (currentSectionLevel < level)
                    {
                        currentSectionLevel++;
                        output.WriteStartElement(Tags.TagSection);
                        output.WriteAttributeString(Tags.AttributeSectionLevel, currentSectionLevel.ToString(CultureInfo.InvariantCulture));
                    }
                }
                if (in_bijlagen)
                {
                    output.WriteAttributeString(Tags.AttributeAppendix, "y");
                }
                if (documentSettings.IncludeMarkdownSource)
                {
                    output.WriteAttributeString(Tags.AttributeSource, line);
                }
                output.WriteStartElement(Tags.TagHeading);
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

            Match m = Regex.Match(line, Markdown.BulletListPattern);
            if (m.Success)
            {
                tag = Tags.TagBulletList;
                listLevel = BulletLevel.GetValueOrDefault(line[0], Markdown.BulletLevel1);
            }
            else
            {
                m = Regex.Match(line, Markdown.NumberedListPattern);

                if (!m.Success)
                {
                    return false;
                }

                tag = Tags.TagNumberedList;
                listLevel = IsDigit(line[0]) ? ((indent == 0) ? 1 : 3) : 2;
            }

            string item = line.Substring(m.Length).Trim();

            while (currentListLevel < listLevel)
            {
                currentListLevel++;
                output.WriteStartElement(tag);
                output.WriteAttributeString(Tags.AttributeListLevel, currentListLevel.ToString(CultureInfo.InvariantCulture));
            }
            while (currentListLevel > listLevel)
            {
                output.WriteEndElement();
                currentListLevel--;
            }

            output.WriteStartElement(Tags.TagListItem);
            if (documentSettings.IncludeMarkdownSource)
            {
                output.WriteAttributeString(Tags.AttributeSource, line);
            }
            ProcessFormattedText(item);
            output.WriteEndElement();

            return true;
        }
      
        private bool MatchTableRow(string line)
        {
            if (line.StartsWith(Markdown.TableMarker))
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
                for(int i = 0; i< cells.Length; i++)
                {
                    string c = cells[i];
                    if (c.StartsWith(Markdown.CellAlignmentMarker) && c.EndsWith(Markdown.CellAlignmentMarker))
                    {
                        table.SetAlignment(i, Alignment.Center);
                    }
                    else if (c.EndsWith(Markdown.CellAlignmentMarker))
                    {
                        table.SetAlignment(i, Alignment.Right);
                    }
                    else
                    {
                        table.SetAlignment(i, Alignment.Left);
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
            line = line.Trim(Markdown.TableMarker, ' ', '\t');
            string[] cells = line.Split(Markdown.TableMarker);
            for (int i = 0; i < cells.Length; i++)
            {
                cells[i] = cells[i].Trim();
            }
            return cells;
        }

        private void FlushTable(DocumentSettings documentSettings)
        {
            output.WriteStartElement(Tags.TagTable);
            output.WriteAttributeString(Tags.AttributeColumns, table.ColumnCount.ToString(CultureInfo.InvariantCulture));
            output.WriteAttributeString(Tags.AttributeRows, table.RowCount.ToString(CultureInfo.InvariantCulture));

            output.WriteStartElement(Tags.TagTableHeaderRow);
            if (documentSettings.IncludeMarkdownSource)
            {
                output.WriteAttributeString(Tags.AttributeSource, table.HeaderSource);
            }

            int column = 0;
            foreach(string headerCell in table.HeaderCells)
            { 
                output.WriteStartElement(Tags.TagTableCell);
                output.WriteAttributeString(Tags.AttributeColumnAlignment, 
                    AlignmentToStr.GetValueOrDefault(table.GetAlignment(column), Tags.AlignmentLeft));
                ProcessFormattedText(headerCell);
                output.WriteEndElement();
                column++;
            }

            output.WriteEndElement();

            for(int r = 0; r < table.RowCount; r++)
            {
                string[] cells = table.GetRowCells(r);
           
                output.WriteStartElement(Tags.TagTableRow);
                if (documentSettings.IncludeMarkdownSource)
                {
                    output.WriteAttributeString(Tags.AttributeSource, table.GetRowSource(r));
                }

                foreach (string cell in cells)
                {
                    output.WriteStartElement(Tags.TagTableCell);
                    ProcessFormattedText(cell);
                    output.WriteEndElement();
                }
                output.WriteEndElement();
            }

            output.WriteEndElement();
        }

        string buffer = "";
        int pos = 0;
        bool is_bold = false;
        bool is_italic = false;
        bool is_strikethrough = false;
        bool is_instruction = false;

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
                
                if (current2.Equals(Markdown.Bold, StringComparison.OrdinalIgnoreCase) || current2.Equals(Markdown.BoldAlternative, StringComparison.OrdinalIgnoreCase))
                {
                    if (is_bold)
                    {
                        EndStyle(current2);
                        is_bold = false;
                        continue;
                    }
                    else if (text.Substring(pos+2).Contains(current2, StringComparison.OrdinalIgnoreCase))
                    {
                        StartStyle(current2, Tags.TagBold);
                        is_bold = true;
                        continue;
                    }
                }
                else if (current2.Equals(Markdown.Strikethrough, StringComparison.OrdinalIgnoreCase))
                {
                    if (is_strikethrough)
                    {
                        EndStyle(current2);
                        is_strikethrough = false;
                        continue;
                    }
                    else if (text.Substring(pos + 2).Contains(current2, StringComparison.OrdinalIgnoreCase))
                    {
                        StartStyle(current2, Tags.TagStrikethrough);
                        is_strikethrough = true;
                        continue;
                    }
                }
                else if (current.Equals(Markdown.Italic, StringComparison.OrdinalIgnoreCase) || current.Equals(Markdown.ItalicAlternative, StringComparison.OrdinalIgnoreCase))
                {
                    if (is_italic)
                    {
                        EndStyle(current);
                        is_italic = false;
                        continue;
                    }
                    else if (text.Substring(pos + 1).Contains(current, StringComparison.OrdinalIgnoreCase))
                    {
                        StartStyle(current, Tags.TagItalic);
                        is_italic = true;
                        continue;
                    }
                }
                else if (current.Equals(Markdown.InstructionStart, StringComparison.OrdinalIgnoreCase)
                    && text.Substring(pos + 1).Contains(Markdown.InstructionEnd, StringComparison.OrdinalIgnoreCase))
                {
                    StartStyle(current, Tags.TagInstruction);
                    buffer += Markdown.InstructionStart;
                    is_instruction = true;
                    continue;
                }
                else if (current.Equals(Markdown.InstructionEnd, StringComparison.OrdinalIgnoreCase) && is_instruction)
                {
                    buffer += Markdown.InstructionEnd;
                    EndStyle(Markdown.InstructionEnd);
                    is_instruction = false;
                    continue;
                }

                buffer += current;
                pos += 1;
            }

            Flush();
        }
    }
}
