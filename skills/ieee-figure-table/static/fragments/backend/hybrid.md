# Backend: Hybrid Figure Workflow

Use this route when the final IEEE figure is not made end-to-end in Python/R.

Typical cases:

1. Python/R generates quantitative base plots, then a vector editor finishes labels, callouts, arrows, alignment, or panel composition.
2. A mechanism, system architecture, experimental pipeline, or conceptual schematic needs Illustrator, Inkscape, PowerPoint, Figma, draw.io, or similar tools.
3. Multiple exported plots, photos, diagrams, screenshots, or tables are assembled into one figure.
4. The final visual quality depends on typography, icon alignment, manual grouping, or spatial narrative that would be brittle in code.

Do not treat hybrid as permission to make unreproducible figures. Separate:

- data layer: source data, code, generated SVG/PDF/PNG;
- layout layer: editable vector/source file such as SVG, AI, PPTX, Figma, draw.io, or Inkscape SVG;
- export layer: final PDF/SVG/TIFF/PNG and manuscript preview;
- edit log: manual changes made after code export.

Read `references/ieee-hybrid-figure-workflow.md` before proposing or delivering hybrid figures.
