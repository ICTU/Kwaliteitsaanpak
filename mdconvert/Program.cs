using mdconvert.Builders;
using Newtonsoft.Json;
using System;
using System.IO;
using System.Linq;

namespace mdconvert
{
    internal class Program
    {
        public const string APP_NAME = "mdconvert";
        public const string APP_PREFIX = APP_NAME + "> ";
        private static bool DEBUG = false;

        private static int Main(string[] args)
        {
            DocumentSettings documentSettings;

            if (args.Length == 1)
            {
                string settingsFile = args[0];

                if (!File.Exists(settingsFile))
                {
                    Error($"File not found: '{settingsFile}'");
                    return 1;
                }

                try
                {
                    string json = File.ReadAllText(settingsFile);
                    documentSettings = JsonConvert.DeserializeObject<DocumentSettings>(json);
                }
                catch (Exception e)
                {
                    Error($"Exception during reading document settings: {e.Message}");
                    throw;
                }
            }
            else
            {
                Info($"USAGE: {APP_NAME} <document settings file>");
                return 1;
            }

            if (string.IsNullOrWhiteSpace(documentSettings.InputFile))
            {
                Error($"Missing input file name");
                return 1;
            }

            //if (!File.Exists(documentSettings.InputFile))
            //{
                //Error($"File not found '{documentSettings.InputFile}'");
                //return 1;
            //}

            string filename = Path.GetFileName(documentSettings.InputFile);
            string xmlFile = Path.Combine(documentSettings.BuildPath, Path.ChangeExtension(filename, "xml"));

            if (!documentSettings.ImagePath.EndsWith("/", StringComparison.OrdinalIgnoreCase)
                && !documentSettings.ImagePath.EndsWith("\\", StringComparison.OrdinalIgnoreCase))
            {
                documentSettings.ImagePath = $"{documentSettings.ImagePath}/";
            }

            try
            {
                Info($"Converting file '{documentSettings.InputFile}' using settings:");
                Info($".Title = '{documentSettings.Title}'");
                Info($".Type = {documentSettings.DocumentType}");
                Info($".Include front page = {documentSettings.IncludeFrontPage}");
                Info($".Include Markdown source = {documentSettings.IncludeMarkdownSource}");
                Info($".Include table of contents = {documentSettings.IncludeTableOfContents}");
                Info($".Image path = {documentSettings.ImagePath}");

                string formats = "";
                foreach (ExportFormat format in documentSettings.OutputFormats)
                {
                    formats += $"{format} ";
                }
                Info($".Output formats = {{{formats}}}");

                if (documentSettings.OutputFormats.Contains(ExportFormat.Docx))
                {
                    Info($".Docx reference file = {documentSettings.DocxReferenceFile}");
                }

                //Info($"Converting file '{documentSettings.InputFile}' to '{xmlFile}'");
                //MarkdownConverter converter = new MarkdownConverter();
                //string result = converter.ConvertFile(documentSettings.InputFile, documentSettings);
                //WriteOutput(result, xmlFile);
            }
            catch (Exception e)
            {
                Error($"Exception while converting Markdown: {e.Message}");
                throw;
            }

            string outputFilename;
            IDocumentBuilder builder;

            foreach (ExportFormat format in documentSettings.OutputFormats)
            {
                builder = null;
                switch (format)
                {
                    case ExportFormat.Markdown:
                        outputFilename = Path.Combine(documentSettings.OutputPath, Path.ChangeExtension(filename, "md"));
                        builder = new MarkdownBuilder(outputFilename);
                        break;

                    case ExportFormat.Html:
                        outputFilename = Path.Combine(documentSettings.OutputPath, Path.ChangeExtension(filename, "html"));
                        builder = new HtmlBuilder(outputFilename);
                        break;

                    case ExportFormat.Docx:
                        outputFilename = Path.Combine(documentSettings.OutputPath, Path.ChangeExtension(filename, "docx"));

                        if (!File.Exists(documentSettings.DocxReferenceFile))
                        {
                            Error($"Docx reference file not found: {documentSettings.DocxReferenceFile}");
                        }
                        else
                        {
                            builder = new DocxBuilder(outputFilename, documentSettings.DocxReferenceFile);
                        }
                        break;

                    default:
                        Warning($"{APP_PREFIX}unknown output format: '{format}'");
                        continue;
                }

                if (!File.Exists(xmlFile))
                {
                    Error($"File not found: '{xmlFile}'");
                    return 1;
                }

                if (builder != null)
                {
                    try
                    {
                        Info($"Converting file '{xmlFile}' to '{outputFilename}'");
                        XMLConverter converter = new XMLConverter(xmlFile);
                        converter.Convert(builder, documentSettings);
                    }
                    catch (Exception e)
                    {
                        Error($"{APP_PREFIX}Exception during conversion: {e.Message}\nTRACE:\n{e.StackTrace}");
                        throw;
                    }
                }
            }

            return 0;
        }

        public static void Info(string output)
        {
            Console.WriteLine($"{APP_PREFIX}{output}");
        }

        public static void Debug(string output)
        {
            if (DEBUG)
            {
                Console.WriteLine($"{APP_PREFIX}DEBUG: {output}");
            }
        }

        public static void Error(string output)
        {
            Console.WriteLine($"{APP_PREFIX}ERROR: {output}");
        }

        public static void Warning(string output)
        {
            Console.WriteLine($"{APP_PREFIX}WARNING: {output}");
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