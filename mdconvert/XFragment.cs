using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace mdconvert
{
    class XFragment
    {
        public XFragment(string text, IEnumerable<XStyle> styles)
        {
            Text = text;
            Styles = styles;
        }

        public XFragment(string text)
            : this(text, new XStyle[0])
        {
        }

        public XFragment()
            : this("")
        {
        }

        public string Text { get; set; }

        public IEnumerable<XStyle> Styles { get; set; }

        public bool Bold => Styles.Contains(XStyle.Bold);

        public bool Italic => Styles.Contains(XStyle.Italic);

        public bool Strikethrough => Styles.Contains(XStyle.Strikethrough);

        public bool Instruction => Styles.Contains(XStyle.Instruction);

        public bool HasStyle => Bold || Italic || Strikethrough || Instruction;

        public override string ToString() =>Text;
    }
}
