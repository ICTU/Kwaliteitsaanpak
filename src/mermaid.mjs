// Render a Mermaid diagram, read from stdin, to SVG and PNG using Pele (https://pele.run) and resvg.
// Usage: node src/mermaid.mjs <output path without suffix> <id prefix>
// Writes <output path>.svg and <output path>.png. Exits with status 1 and an error message if the diagram is invalid.

import { readFileSync, writeFileSync } from "node:fs";
import { Resvg } from "@resvg/resvg-js";
import { render } from "pele";

const FONT_FAMILY = 'Arial, Helvetica, "Liberation Sans", sans-serif';
const PNG_ZOOM = 4; // Render PNG images at four times the SVG size so they stay sharp in docx and pptx

// Pele uses CSS variables for colors, but resvg does not support CSS variables. Replace the Pele variables by their
// default values and then replace the internal variables (e.g. --_l: var(--pele-line, #1f1f1f)) by their values.
function resolveVariables(svg) {
  svg = svg.replace(/var\(--pele-[a-z-]+,([^()]+)\)/g, "$1");
  const declarations = Object.fromEntries([...svg.matchAll(/(--_[a-z]+):([^;"]+)/g)].map((match) => match.slice(1)));
  return svg.replace(/var\((--_[a-z]+)\)/g, (match, name) => declarations[name] ?? match);
}

const [outputPath, idPrefix] = process.argv.slice(2);
let svg;
try {
  svg = resolveVariables(render(readFileSync(0, "utf8"), { fontFamily: FONT_FAMILY, idPrefix }).svg);
} catch (error) {
  console.error(error.message);
  process.exit(1);
}
writeFileSync(`${outputPath}.svg`, svg);
writeFileSync(`${outputPath}.png`, new Resvg(svg, { fitTo: { mode: "zoom", value: PNG_ZOOM } }).render().asPng());
