""" Script to extract abbreviations from markdown files. 

An abbreviation is detected when a word in all capitals is followed by text between brackets. 
For example: ICT (Information and communication technology). """


import re
import sys


abbreviations = dict()
errors = False

for line in sys.stdin.readlines():
    for match in re.finditer(r"([A-Z]+) \(([^)]+)\)", line):
        abbreviation, full_spelling = match.groups()
        if abbreviations.get(abbreviation, full_spelling) != full_spelling:
            sys.stderr.write(f"ERROR: Abbreviation {abbreviation} has inconsistent full spellings: {abbreviations[abbreviation]} != {full_spelling}\n")
            errors = True
        abbreviations[abbreviation] = full_spelling

if errors:
    sys.exit(1)

print("### Afkortingen\n")

for abbreviation, explanation in sorted(abbreviations.items()):
    print("- {0}: {1}".format(abbreviation, explanation))

print()
