namespace mdconvert
{
    /// <summary>
    /// Format of the document to be generated. Each export format should have its own implementation of IDocumentBuilder. 
    /// </summary>
    public enum ExportFormat
    {
        Docx,
        Markdown,
        Html
    }
}