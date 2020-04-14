using System;
using System.Collections.Generic;
using System.Linq;

namespace mdconvert
{
    internal class XFragment
    {
        public XFragment(string text, string link, IEnumerable<XStyle> styles)
        {
            Text = text;
            Link = link;
            Styles = styles;
        }

        public XFragment(string text, IEnumerable<XStyle> styles)
            : this(text, "", styles)
        {
        }

        public XFragment(string text, string link)
            : this(text, link, Array.Empty<XStyle>())
        {
        }

        public XFragment(string text)
            : this(text, "", Array.Empty<XStyle>())
        {
        }

        public XFragment()
            : this("", "", Array.Empty<XStyle>())
        {
        }

        public string Text { get; set; }

        public string Link { get; set; }

        public IEnumerable<XStyle> Styles { get; set; }

        public bool Bold => Styles.Contains(XStyle.Bold);

        public bool Italic => Styles.Contains(XStyle.Italic);

        public bool Strikethrough => Styles.Contains(XStyle.Strikethrough);

        public bool Instruction => Styles.Contains(XStyle.Instruction);

        public bool HasStyle => Bold || Italic || Strikethrough || Instruction;

        public bool HasLink => Link.Length > 0;

        public override string ToString() => Text;
    }
}