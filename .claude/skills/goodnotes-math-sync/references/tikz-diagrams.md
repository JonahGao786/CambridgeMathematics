# TikZ diagram requirements

The user renders diagrams with the Obsidian **TikZJax** plugin.

## Format

````markdown
```tikz
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{document}
\begin{tikzpicture}[>=latex]
% drawing commands supported by the source
\end{tikzpicture}
\end{document}
```
````

- Basic TikZ plus common libraries (`arrows.meta`, `positioning`, `calc`, `decorations.markings`). TikZJax also supports `\foreach` and plain-TeX conditionals. Avoid PGFPlots unless verified; use `plot (\x,{…})` with `domain` instead.
- Keep each diagram short and readable (≲ 40 lines). Prefer `\foreach` over repeated blocks.
- No external images, PNGs or attachments in the repository.

## What to draw

- Every mathematically meaningful drawing in the source: graphs of functions, geometric figures, vector diagrams, Argand diagrams, set pictures, commutative/arrow diagrams, symmetry pictures.
- Preserve what carries meaning: labels, arrows and directions, colours that encode something (add a one-line legend), intersections, open/closed endpoints, axes, regions, which side is shaded.
- A clean schematic is fine when exact placement is irrelevant; do not invent equations or numerical data to produce a plot. A qualitative sketch is drawn qualitatively.
- Decorative doodles and pure handwriting flourishes are not diagrams.
- Prose, edge lists, Mermaid or arrow arrays do not replace a drawing; a one-sentence caption may supplement it.
- Unfinished or crossed-out drawings stay visibly unfinished / labelled superseded.

## Placement and captions

Place the diagram immediately after the sentence it illustrates. A caption, if any, is one line in italics below it (e.g. `*Secant through $x_0$ and $x_0+h$; curve schematic.*`). Do not narrate how coordinates were chosen.

## Verification

- If a TeX engine is available, compile the exact block outside the repository and compare it to the source page. Otherwise, re-read the code carefully against the source (labels, arrow directions, colours, incidences).
- Report local compilation separately from rendering in Obsidian; never claim an Obsidian render you did not see.
- If an essential diagram cannot be reconstructed faithfully, keep the readable parts, add `> [!todo] p. N — diagram incomplete: …`, and mark the upgrade pending in the manifest.
