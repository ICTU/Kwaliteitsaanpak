using mdconvert.Builders;
using Newtonsoft.Json;
using System;
using System.IO;
using System.Linq;

namespace mdconvert
{
    class Program
    {
        public const string APP_NAME = "mdconvert";
        public const string APP_PREFIX = APP_NAME + "> ";

        static int Main(string[] args)
        {
            DocumentSettings documentSettings;

            if (args.Length == 1)
            {
                string settingsFile = args[0];

                if (!File.Exists(settingsFile))
                {
                    Console.WriteLine($"{APP_PREFIX}File not found: '{settingsFile}'");
                    return 1;
                }

                try
                {
                    string json = File.ReadAllText(settingsFile);
                    documentSettings = JsonConvert.DeserializeObject<DocumentSettings>(json);
                }
                catch (Exception e)
                {
                    Console.WriteLine($"{APP_PREFIX}Exception during reading document settings: {e.Message}");
                    return 1;
                }
            }         
            else
            {
                Console.WriteLine($"USAGE: {APP_NAME} <document settings file>");
                return 1;
            }

            if (string.IsNullOrWhiteSpace(documentSettings.InputFile))
            {
                Console.WriteLine($"{APP_PREFIX}Missing input file name");
                return 1;
            }

            if (!File.Exists(documentSettings.InputFile))
            {
                Console.WriteLine($"{APP_PREFIX}File not found '{documentSettings.InputFile}'");
                return 1;
            }

            string filename = Path.GetFileName(documentSettings.InputFile);
            string xmlFile = Path.Combine(documentSettings.OutputPath, Path.ChangeExtension(filename, "xml"));

            if (!documentSettings.ImagePath.EndsWith("/") && !documentSettings.ImagePath.EndsWith("\\"))
            {
                documentSettings.ImagePath = $"{documentSettings.ImagePath}/";
            }

            try
            {
                Console.WriteLine($"{APP_PREFIX}Converting file '{documentSettings.InputFile}' using settings:");
                Console.WriteLine($"{APP_PREFIX}....Title = '{documentSettings.Title}'");
                Console.WriteLine($"{APP_PREFIX}....Type = {documentSettings.DocumentType}");
                Console.WriteLine($"{APP_PREFIX}....Include front page = {documentSettings.IncludeFrontPage}");
                Console.WriteLine($"{APP_PREFIX}....Include Markdown source = {documentSettings.IncludeMarkdownSource}");
                Console.WriteLine($"{APP_PREFIX}....Include table of contents = {documentSettings.IncludeTableOfContents}");
                Console.WriteLine($"{APP_PREFIX}....Image path = {documentSettings.ImagePath}");
                Console.Write($"{APP_PREFIX}....Output formats = {{");

                foreach (DocumentFormat format in documentSettings.OutputFormats)
                {
                    Console.Write($"{format} ");
                }
                Console.WriteLine("}");

                if (documentSettings.OutputFormats.Contains(DocumentFormat.Docx))
                {
                    Console.WriteLine($"{APP_PREFIX}....docx reference file = {documentSettings.DocxReferenceFile}");
                }

                Console.WriteLine($"{APP_PREFIX}Converting file '{documentSettings.InputFile}' to '{xmlFile}'");
                MarkdownConverter converter = new MarkdownConverter();
                string result = converter.ConvertFile(documentSettings.InputFile, documentSettings);
                WriteOutput(result, xmlFile);
            }
            catch (Exception e)
            {
                Console.WriteLine($"{APP_PREFIX}Exception while converting Markdown: {e.Message}");
                return 1;
            }

            string outputFilename;
            IDocumentBuilder builder;

            foreach (DocumentFormat format in documentSettings.OutputFormats)
            {
                builder = null;
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

                        if (!File.Exists(documentSettings.DocxReferenceFile))
                        {
                            Console.WriteLine($"{APP_PREFIX}Docx reference file not found: {documentSettings.DocxReferenceFile}");
                        }
                        else
                        {
                            builder = new DocxBuilder(outputFilename, documentSettings.DocxReferenceFile);
                        }
                        break;

                    default:
                        Console.WriteLine($"{APP_PREFIX}Warning: unknown output format: '{format}'");
                        continue;
                }

                if (!File.Exists(xmlFile))
                {
                    Console.WriteLine($"{APP_PREFIX}File not found: '{xmlFile}'");
                    return 1;
                }

                if (builder != null)
                {
                    try
                    {
                        Console.WriteLine($"{APP_PREFIX}Converting file '{xmlFile}' to '{outputFilename}'");
                        XMLConverter converter = new XMLConverter(xmlFile);
                        converter.Convert(builder, documentSettings);
                    }
                    catch (Exception e)
                    {
                        Console.WriteLine($"{APP_PREFIX}Exception during conversion: {e.Message}\nTRACE:\n{e.StackTrace}");
                        if (e.InnerException != null)
                        {
                            Console.WriteLine($"INNER:\n{e.InnerException?.Message}");
                        }
                        return 1;
                    }
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
