---
name: ieee-figure-table
description: Audit, redesign, generate, and improve IEEE manuscript figures, tables, captions, result presentation, plotting scripts, visual polish, hybrid Python/R plus vector-editor workflows, publication-ready matplotlib house style, and layout using routed visual-evidence checks. Use when checking or creating plot readability, axes, legends, line overlap, table structure, metric reporting, captions, grayscale accessibility, IEEE one-column/two-column layout, figure/table placement, claim-evidence mapping, reviewer first-impression risks, matplotlib/seaborn or ggplot2 figure code, SVG/PDF/TIFF/PNG export, Illustrator/Inkscape/PowerPoint/Figma finishing plans, or IEEE-style engineering evidence graphics.
---

# IEEE Figure Table Router

Use this skill to make figures and tables function as professional IEEE evidence. The goal is not decoration; it is readable, fair, claim-aligned visual proof that still works after IEEE column scaling.

Do not rely on general design intuition alone. Follow the routing protocol and load the selected fragments.

## Routing Protocol

1. Read `manifest.yaml`.
2. Read every file listed under `always_load`.
3. Detect the axes:
   - `visual_type`: line-plot / bar-chart / scatter / confusion-matrix / comparison-table / ablation-table / architecture-diagram / algorithm-flowchart / multi-panel / generic.
   - `check_type`: readability / accessibility / caption / layout / evidence-mapping / statistical-presentation.
   - `failure_mode`: blurry-figure / bad-axis / overlapping-legend / misleading-scale / inconsistent-precision / weak-caption / unreadable-two-column.
   - `stage`: audit / redesign / caption-writing / latex-placement.
   - `backend`: python / r / hybrid / no-plot. Use `hybrid` when a figure is partly generated from data/code and partly finished in a vector/design tool. Use `no-plot` for audit-only, caption-only, table-only, or LaTeX-placement tasks that do not generate plotting code or image files.
4. For plotting/redrawing tasks, resolve `backend` by explicit request, input workflow, or saved preference. If the intended output is a mechanism schematic, graphical workflow, polished composite, annotated experiment pipeline, or figure that cannot be cleanly produced end-to-end in Python/R, choose `hybrid`. If no preference exists for a pure plotting task, ask once: **Python or R? I will remember this as your default for IEEE figures.**
5. State the detected axes in one short line.
6. Load only the matching fragments.
7. For plotting/redrawing, establish an IEEE figure contract before code: core engineering claim, evidence-panel map, final column size, metric/condition definitions, export formats, visual style target, and QA risks.
8. Map each figure/table to the claim it supports.
9. For Python plotting, prefer the bundled `scripts/ieee_plot_style.py` helper or mirror its API when writing standalone manuscript code. For hybrid figures, separate data-generated layers from manually edited vector/layout layers and keep an edit log.
10. Report first-impression risks before cosmetic suggestions.

## Output Contract

Default output:

```text
Detected axes: visual_type=..., check_type=..., failure_mode=..., stage=..., backend=...

Figure/table audit
Item | Supported claim | First-impression risk | Technical issue | Fix

Priority fixes
1. ...
```

For caption writing, return revised captions plus missing information placeholders.

For redesign requests, provide concrete plot/table changes rather than generic advice.

For plotting or redraw requests, return:

```text
IEEE figure contract
- Core claim:
- Evidence map:
- Final size:
- Visual style:
- Export bundle:

Files or code:
- ...

QA notes:
- ...
```

## Red Lines

Do not recommend misleading axis scaling.

Do not invent experimental results or statistical significance.

Do not make visual changes that obscure fair comparison, uncertainty, or negative results.

Do not use the official IEEE logo, IEEE marks, or invented acceptance/compliance claims in figures.
