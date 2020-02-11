using System.Collections.Generic;
using System.Text;

namespace mdconvert
{
    internal class XParagraph
    {
        private readonly List<XFragment> fragments = new List<XFragment>();

        public XParagraph()
        {
        }

        public IEnumerable<XFragment> Fragments => fragments;

        public int NumFragments => fragments.Count;

        public XFragment Get(int index) => fragments[index];

        public void Add(XFragment fragment)
        {
            fragments.Add(fragment);
        }

        public override string ToString()
        {
            StringBuilder b = new StringBuilder();
            foreach (XFragment f in Fragments)
            {
                b.Append(f.ToString());
            }
            return b.ToString();
        }
    }
}