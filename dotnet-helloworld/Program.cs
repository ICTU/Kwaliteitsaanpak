﻿using System;
using DocumentFormat.OpenXml;
using DocumentFormat.OpenXml.Packaging;
using DocumentFormat.OpenXml.Wordprocessing;

namespace HelloWorldDotNet
{
    class Program
    {
        static void Main(string[] args)
        {
            // Open a WordprocessingDocument for editing using the filepath.
            using (WordprocessingDocument wordDocument = WordprocessingDocument.Create("/output/Hello world.docx", WordprocessingDocumentType.Document))
            {
                // Add a main document part. 
                MainDocumentPart mainPart = wordDocument.AddMainDocumentPart();

                // Create the document structure and add some text.
                mainPart.Document = new Document();
                Body body = mainPart.Document.AppendChild(new Body());
                Paragraph para = body.AppendChild(new Paragraph());
                Run run = para.AppendChild(new Run());
                run.AppendChild(new Text($"Hello world @ {DateTime.Now.ToLongTimeString()}"));
            }
        }
    }
}