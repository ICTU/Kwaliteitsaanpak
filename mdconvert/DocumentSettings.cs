using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System;
using System.Collections.Generic;
using System.Text;

namespace mdconvert
{
    public class DocumentSettings
    {
        public DocumentSettings()
        {
        }

        public string InputFile { get; set; } = "";

        public string OutputPath { get; set; } = "";

        public string Title { get; set; } = "";

        [JsonConverter(typeof(StringEnumConverter))]
        public DocumentType DocumentType { get; set; } = DocumentType.Generic;

        public bool IncludeFrontPage { get; set; } = true;

        public bool IncludeMarkdownSource { get; set; } = false;

        public bool IncludeTableOfContents { get; set; } = false;

        public string ImagePath { get; set; } = "images";

        public ExportFormat[] OutputFormats { get; set; } = new ExportFormat[] { ExportFormat.Docx };

        public string DocxReferenceFile { get; set; } = @".\reference.docx";
    }
}
