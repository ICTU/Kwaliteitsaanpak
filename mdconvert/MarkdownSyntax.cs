namespace mdconvert
{
    /// <summary>
    /// Markdown-specific tokens and patterns, needed to parse Markdown files. 
    /// </summary>
    public static class MarkdownSyntax
    {
        public const string Bold = "**";
        public const string BoldAlternative = "__";
        public const string Italic = "_";
        public const string ItalicAlternative = "*";
        public const string Strikethrough = "~~";
        public const string InstructionStart = "{";
        public const string InstructionEnd = "}";

        public const string MeasureStart = "@{";
        public const string MeasureEnd = "}@";

        public const string HeadingPattern = @"^#+\s";
        public const string BulletListPattern = @"^[\*\+\-]\s";
        public const string NumberedListPattern = @"^[0-9A-Za-z]\.\s";

        public const char BulletLevel1 = '*';
        public const char BulletLevel2 = '+';
        public const char BulletLevel3 = '-';
        public const char TableMarker = '|';
        public const char CellAlignmentMarker = ':';
    }
}