import pathlib
import json


def url(item):
    fragment = item['id'].split(":")[1] 
    anchor = item['handle']
    return f"[{anchor}](https://www.w3.org/TR/WCAG21/#{fragment})"


with pathlib.Path("wcag.json").open() as wcag_file:
    wcag = json.loads(wcag_file.read())

lines = []
lines.extend(["| Item | Level | Description |", "| :--- | :--- | :--- |"])
for principle in wcag["principles"]:
    lines.append(f"| Principle {principle['num']} | | {url(principle)} |")
    for guideline in principle["guidelines"]:
        lines.append(f"| Guideline {guideline['num']} | | {url(guideline)} |")
        for sc in guideline["successcriteria"]:
            if sc["level"] == "AAA":
                continue
            lines.append(f"| Success criterium {sc['num']} | {sc['level']} | {url(sc)} |")

with pathlib.Path("../../Content/Templates/NFE/WCAG-Tabel-Gegenereerd.md").open("w") as wcag_table:
    wcag_table.write("\n".join(lines))

