"""Script to convert the WCAG success critera to a Markdown table, and include which Axe-core rules check which WCAG
criteria."""

import json
import pathlib
import subprocess


def url(anchor, uri):
    """Return a Markdown URL."""
    return f"[{anchor}]({uri})"


def item_url(item):
    """Return a Markdown URL for the WCAG item."""
    fragment = item["id"].split(":")[1]
    return url(item["handle"], f"https://www.w3.org/TR/WCAG22/#{fragment}")


def rule_url(rule):
    """Return a Markdown URL for the Axe rule."""
    return url(rule["ruleId"], rule["helpUrl"]) + (" (experimenteel)" if "experimental" in rule["tags"] else "")


def node(script):
    """Run a Javascript script with node and return its stdout."""
    return subprocess.run(["node", "--eval", script], text=True, capture_output=True).stdout.strip()


# Read the Axe-core version and rules
axe_core_version = node("console.log(require('axe-core').version)")
node("""
const axe = require('axe-core');
const fs = require('fs');

fs.writeFileSync('/tmp/wcag_rules.json', JSON.stringify(axe.getRules(), null, 2), 'utf-8')
""")
rules = json.load(pathlib.Path("/tmp/wcag_rules.json").open())

# Read the WCAG success criteria
with pathlib.Path("wcag.json").open() as wcag_file:
    wcag = json.loads(wcag_file.read())

# Generate the Markdown table
lines = []
lines.extend(
    [
        f"| Item | Omschrijving | Niveau | Axe-core {axe_core_version} regels |",
        "| :--- | :--- | :--- | :--- |",
    ]
)
for principle in wcag["principles"]:
    lines.append(f"| Principe {principle['num']} | {item_url(principle)} | | |")
    for guideline in principle["guidelines"]:
        lines.append(f"| Richtlijn {guideline['num']} | {item_url(guideline)} | | |")
        for sc in guideline["successcriteria"]:
            tag = f"wcag{sc['num'].replace('.', '')}"
            if applicable_rules := [rule for rule in rules if tag in rule["tags"]]:
                rule_ids = ", ".join(sorted([rule_url(rule) for rule in applicable_rules]))
            else:
                rule_ids = "geen"
            lines.append(f"| Succes criterium {sc['num']} | {item_url(sc)} | {sc['level']} | {rule_ids} |")

# Write the Markdown table to the Kwaliteitsaanpak Content folder
with pathlib.Path("../../Content/Templates/NFE/WCAG-Tabel-Gegenereerd.md").open("w") as wcag_table:
    wcag_table.write("\n".join(lines))
