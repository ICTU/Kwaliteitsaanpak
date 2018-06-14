""" Fix the generated Table of Contents. 

This is needed because markdown-toc generates different slugs than markdown-to-html. 

Differences:
- markdown-toc doesn't merge two hyphens into one.
- markdown-toc doesn't convert apostrophs to hyphens.

""" 

import sys

with sys.stdin as toc:
    for line in toc.readlines():
        line = line.replace("--", "-")
        line = line.replace("risicos", "risico-s")
        print(line.strip("\n"))


