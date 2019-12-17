using mdconvert.Builders;
using Newtonsoft.Json;
using System;
using System.IO;
using System.Linq;

namespace mdconvert
{
    class Program
    {
        static int Main(string[] args)
        {
            DocumentSettings documentSettings = new DocumentSettings()
            {
                Title = "No title",
                DocumentType = DocumentType.Generic,
                IncludeMarkdownSource = false,
                IncludeFrontPage = true,
                IncludeTableOfContents = true,
                ImagePath = "Images"
            };

            if (args.Length == 1)
            {
                string settingsFile = args[0];

                if (!File.Exists(settingsFile))
                {
                    Console.WriteLine($"File not found: '{settingsFile}'");
                    return 1;
                }

                try
                {
                    string json = File.ReadAllText(settingsFile);
                    documentSettings = JsonConvert.DeserializeObject<DocumentSettings>(json);
                }
                catch (Exception e)
                {
                    Console.WriteLine($"Exception during reading document settings: {e.Message}");
                    return 1;
                }
            }         
            else
            {
                Console.WriteLine("USAGE: mdconvert <document settings file>");
                return 1;
            }

            if (string.IsNullOrWhiteSpace(documentSettings.InputFile))
            {
                Console.WriteLine($"Error: missing input file name");
                return 1;
            }

            if (!File.Exists(documentSettings.InputFile))
            {
                Console.WriteLine($"Error: file not found '{documentSettings.InputFile}'");
                return 1;
            }

            string filename = Path.GetFileName(documentSettings.InputFile);
            string xmlFile = Path.Combine(documentSettings.OutputPath, Path.ChangeExtension(filename, "xml"));

            try
            {
                Console.WriteLine($"Converting file '{documentSettings.InputFile}' using settings:");
                Console.WriteLine($"....Title = '{documentSettings.Title}'");
                Console.WriteLine($"....Type = {documentSettings.DocumentType}");
                Console.WriteLine($"....Include front page = {documentSettings.IncludeFrontPage}");
                Console.WriteLine($"....Include Markdown source = {documentSettings.IncludeMarkdownSource}");
                Console.WriteLine($"....Include table of contents = {documentSettings.IncludeTableOfContents}");
                Console.WriteLine($"....Image path = {documentSettings.ImagePath}");
                Console.Write("....Output formats = {");

                foreach (DocumentFormat format in documentSettings.OutputFormats)
                {
                    Console.Write($"{format} ");
                }
                Console.WriteLine("}");

                if (documentSettings.OutputFormats.Contains(DocumentFormat.Docx))
                {
                    Console.WriteLine($"....Docx reference file = {documentSettings.DocxReferenceFile}");
                }

                Console.WriteLine($">> Converting file '{documentSettings.InputFile}' to '{xmlFile}'");
                MarkdownConverter converter = new MarkdownConverter();
                string result = converter.ConvertFile(documentSettings.InputFile, documentSettings);
                WriteOutput(result, xmlFile);
            }
            catch (Exception e)
            {
                Console.WriteLine($"Exception while converting Markdown: {e.Message}");
                return 1;
            }

            string outputFilename;
            IDocumentBuilder builder;

            foreach (DocumentFormat format in documentSettings.OutputFormats)
            {
                switch (format)
                {
                    case DocumentFormat.Markdown:
                        outputFilename = Path.Combine(documentSettings.OutputPath, Path.ChangeExtension(filename, "md"));
                        builder = new MarkdownBuilder(outputFilename);
                        break;

                    case DocumentFormat.Html:
                        outputFilename = Path.Combine(documentSettings.OutputPath, Path.ChangeExtension(filename, "html"));
                        builder = new HtmlBuilder(outputFilename);
                        break;

                    case DocumentFormat.Docx:
                        outputFilename = Path.Combine(documentSettings.OutputPath, Path.ChangeExtension(filename, "docx"));
                        builder = new DocxBuilder(outputFilename, documentSettings.DocxReferenceFile);
                        break;

                    default:
                        Console.WriteLine($"Warning: unknown output format: '{format}'");
                        continue;
                }

                if (!File.Exists(xmlFile))
                {
                    Console.WriteLine($"File not found: '{xmlFile}'");
                    return 1;
                }

                try
                {
                    Console.WriteLine($">> Converting file '{xmlFile}' to '{outputFilename}'");
                    XMLConverter converter = new XMLConverter(xmlFile);
                    converter.Convert(builder, documentSettings);
                }
                catch (Exception e)
                {
                    Console.WriteLine($"Exception during conversion: {e.Message}");
                    return 1;
                }
            }

            return 0;
        }

        private static void WriteOutput(string result, string outputFilename)
        {
            StreamWriter writer;

            if (outputFilename != null)
            {
                writer = new StreamWriter(outputFilename);
            }
            else
            {
                writer = new StreamWriter(Console.OpenStandardOutput())
                {
                    AutoFlush = true
                };
                Console.SetOut(writer);
            }

            writer.WriteLine(result);

            writer.Close();
        }
    }
}
