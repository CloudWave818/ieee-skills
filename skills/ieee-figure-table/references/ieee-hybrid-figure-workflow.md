# IEEE Hybrid Figure Workflow

Use this reference when a figure should not be forced into an end-to-end Python/R script. High-quality paper figures often combine reproducible data plots with manual vector composition. This is acceptable when the evidence remains traceable and the final export is publication-ready.

## When Hybrid Is Better

Prefer a hybrid workflow for:

1. mechanism diagrams, system pipelines, architecture figures, graphical summaries, and experimental setups;
2. multi-source composites that combine plots, tables, photos, screenshots, or schematic panels;
3. dense annotation, arrows, callouts, grouped labels, icons, or spatial narratives;
4. figures where code-generated placement creates text collisions or brittle manual coordinates;
5. polished cover-style or teaser figures that still need IEEE evidence discipline.

Prefer pure Python/R for:

1. ordinary line, bar, scatter, heatmap, ROC/PR, confusion matrix, convergence, and ablation plots;
2. figures that must be regenerated repeatedly after experiments change;
3. final quantitative panels where manual editing could alter values or axis geometry.

## Layer Contract

Every hybrid figure must keep layers explicit:

| Layer | What it contains | Required artifact |
|---|---|---|
| Data layer | CSV/TSV/XLSX, scripts, notebooks, generated plots | source data plus script or notebook |
| Plot layer | base charts with correct axes, scales, markers, and values | editable SVG/PDF exported from code |
| Layout layer | manual alignment, labels, arrows, icons, grouped panels, photos | editable SVG/AI/PPTX/Figma/draw.io/Inkscape source |
| Export layer | manuscript-ready figure | PDF/SVG plus PNG/TIFF preview |
| Audit layer | what changed manually and what must not change | edit log and QA notes |

## Manual-Edit Rules

Allowed manual edits:

1. reposition labels, legends, arrows, callouts, and panel tags;
2. align panels, normalize spacing, crop whitespace, and group related components;
3. add schematic arrows, icons, workflow blocks, and visual separators;
4. adjust font family/size consistently across panels;
5. assemble multiple reproducible panels into one figure.

Do not manually edit:

1. plotted values;
2. axis scale or tick positions without updating the source plot;
3. baseline identity, method labels, or metric definitions;
4. uncertainty bands or error bars;
5. visual emphasis in a way that hides negative results or cost metrics.

## Recommended Pipeline

```text
1. Define claim and evidence map.
2. Generate quantitative base panels from data/code.
3. Export editable SVG/PDF with text preserved.
4. Assemble and polish in a vector/layout editor.
5. Record manual edits in a short edit log.
6. Export final PDF/SVG and PNG/TIFF preview.
7. Inspect at IEEE one-column or two-column size.
```

## Deliverable Bundle

For hybrid figures, return or request:

```text
data/
  source.csv
scripts/
  make_base_panels.py or make_base_panels.R
base_exports/
  panel_a.svg
  panel_b.svg
layout/
  figure_final.editable.svg or figure_final.pptx or figure_final.drawio
exports/
  figure_final.pdf
  figure_final.svg
  figure_final.png
  figure_final.tiff
figure_edit_log.md
caption.md
qa_notes.md
```

## Edit Log Template

```markdown
# Figure Edit Log

Figure:
Target placement: one-column / two-column / page-wide

Data-generated panels:
- Panel A:
- Panel B:

Manual layout edits:
- Moved legend outside data region.
- Added workflow arrows and panel labels.
- Aligned panels to shared margins.

No manual changes were made to:
- plotted values
- axis limits/ticks
- baseline labels
- uncertainty/error bars

Final QA:
- Text readable at target column width:
- Grayscale/marker redundancy:
- Caption states condition, metric, and takeaway:
- Source data and scripts available:
```

## IEEE Reviewer Risk Checks

Flag the figure as high risk when:

1. manual edits cannot be traced;
2. source data or base plot script is missing for quantitative panels;
3. screenshots replace vector plots without a reason;
4. photos or screenshots lack source/provenance;
5. manual layout changes distort axis geometry;
6. the figure looks attractive but no longer maps cleanly to a manuscript claim.
