"""Render Mermaid diagrams to SVG and PNG images."""

import hashlib
import pathlib
import subprocess
from dataclasses import dataclass
from xml.etree.ElementTree import Element, parse

RENDER_SCRIPT = pathlib.Path(__file__).parent / "mermaid.mjs"
PELE_PACKAGE = pathlib.Path(__file__).parents[1] / "node_modules" / "pele" / "package.json"
CACHE_FOLDER = pathlib.Path("build/diagrams")
SVG_NAMESPACE = "{http://www.w3.org/2000/svg}"
CM_PER_PIXEL = 2.54 / 96


class DiagramError(Exception):
    """The diagram could not be rendered."""


@dataclass(frozen=True)
class Diagram:
    """A rendered diagram."""

    svg_path: pathlib.Path
    png_path: pathlib.Path

    def svg(self) -> Element:
        """Return the SVG root element."""
        return parse(self.svg_path).getroot()

    def width_cm(self) -> float:
        """Return the natural width of the diagram in centimeters."""
        return float(self.svg().get("width", 0)) * CM_PER_PIXEL

    def title(self) -> str:
        """Return the accessible title of the diagram (Mermaid accTitle), if any."""
        return self._text("title")

    def description(self) -> str:
        """Return the accessible description of the diagram (Mermaid accDescr), if any."""
        return self._text("desc")

    def _text(self, tag: str) -> str:
        """Return the text of the child element of the SVG root element with the given tag."""
        element = self.svg().find(SVG_NAMESPACE + tag)
        return "" if element is None else "".join(element.itertext())


def render_mermaid(source: str, cache_folder: pathlib.Path = CACHE_FOLDER) -> Diagram:
    """Render the Mermaid diagram, unless it was rendered before with the same version of the renderer."""
    renderer = RENDER_SCRIPT.read_text() + PELE_PACKAGE.read_text()
    name = "mermaid-" + hashlib.sha256((renderer + source).encode()).hexdigest()[:16]
    stem = cache_folder / name
    diagram = Diagram(stem.with_suffix(".svg"), stem.with_suffix(".png"))
    if diagram.svg_path.exists() and diagram.png_path.exists():
        return diagram
    cache_folder.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["node", str(RENDER_SCRIPT), str(stem), name],
        input=source,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise DiagramError(f"Invalid Mermaid diagram:\n{source}\n{result.stderr.strip()}")
    return diagram
