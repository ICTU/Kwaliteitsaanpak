using System;
using System.Collections.Generic;
using System.Text;

namespace mdconvert
{
    interface IDocumentBuilder
    {
        string Extension { get; }

        void StartDocument(string title);

        void EndDocument();

        void BuildHeader(XParagraph header);

        void BuildFooter();

        void BuildTableOfContents();

        void CreateParagraph(XParagraph paragraph, Context context);

        void CreateHeading(int level, XParagraph paragraph, bool isAppendix, Context context);

        void StartList(bool numbered);

        void EndList();

        void CreateListItem(int level, bool numbered, XParagraph paragraph, Context context);

        void CreateTable(XTable<XParagraph> table, Context context);

        void InsertPageBreak();

        void InsertPicture(string name);
    }
}
