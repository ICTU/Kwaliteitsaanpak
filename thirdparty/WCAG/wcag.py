"""Script to convert the WCAG success critera to a Markdown table, and include which Axe-core rules check which WCAG
criteria."""

import ast
import json
import pathlib
import re
import subprocess


def url(anchor, uri):
    """Return a Markdown URL."""
    return f"[{anchor}]({uri})"


def item_url(item):
    """Return a Markdown URL for the WCAG item."""
    fragment = item["id"].split(":")[1]
    return url(item["handle"], f"https://www.w3.org/TR/WCAG21/#{fragment}")


def node(script):
    """Run a Javascript script with node and return its stdout."""
    return subprocess.run(["node", "--eval", script], text=True, capture_output=True).stdout.strip()


# Read the Axe-core version and rules
axe_core_version = node("console.log(require('axe-core').version)")
rules_text = node("axe = require('axe-core'); console.log(axe.getRules())")
rules_text = re.sub(r"([a-zA-Z]+): ", r'"\1": ', rules_text)
rules = ast.literal_eval(rules_text)

# Read the WCAG success criteria
with pathlib.Path("wcag.json").open() as wcag_file:
    wcag = json.loads(wcag_file.read())

# Generate the Markdown table
lines = []
lines.extend([f"| Item | Omschrijving | Niveau | Axe-core {axe_core_version} regels |", "| :--- | :--- | :--- | :--- |"])
for principle in wcag["principles"]:
    lines.append(f"| Principe {principle['num']} | {item_url(principle)} | | |")
    for guideline in principle["guidelines"]:
        lines.append(f"| Richtlijn {guideline['num']} | {item_url(guideline)} | | |")
        for sc in guideline["successcriteria"]:
            tag = f"wcag{sc['num'].replace('.', '')}"
            if applicable_rules := [rule for rule in rules if tag in rule["tags"]]:
                rule_ids = ", ".join(sorted([url(rule["ruleId"], rule["helpUrl"]) for rule in applicable_rules]))
            else:
                rule_ids = "geen"
            lines.append(f"| Succes criterium {sc['num']} | {item_url(sc)} | {sc['level']} | {rule_ids} |")

# Write the Markdown table to the Kwaliteitsaanpak Content folder
with pathlib.Path("../../Content/Templates/NFE/WCAG-Tabel-Gegenereerd.md").open("w") as wcag_table:
    wcag_table.write("\n".join(lines))
