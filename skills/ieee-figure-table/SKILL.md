---
name: ieee-figure-table
description: Audit, redesign, and improve IEEE manuscript figures, tables, captions, result presentation, and layout using routed visual-evidence checks. Use when checking plot readability, axes, legends, line overlap, table structure, metric reporting, captions, grayscale accessibility, two-column layout, figure/table placement, claim-evidence mapping, or reviewer first-impression risks.
---

# IEEE Figure Table Router

Use this skill to make figures and tables function as professional IEEE evidence. The goal is not decoration; it is readable, fair, claim-aligned visual proof.

Do not rely on general design intuition alone. Follow the routing protocol and load the selected fragments.

## Routing Protocol

1. Read `manifest.yaml`.
2. Read every file listed under `always_load`.
3. Detect the axes:
   - `visual_type`: line-plot / bar-chart / scatter / confusion-matrix / comparison-table / ablation-table / architecture-diagram / algorithm-flowchart / multi-panel / generic.
   - `check_type`: readability / accessibility / caption / layout / evidence-mapping / statistical-presentation.
   - `failure_mode`: blurry-figure / bad-axis / overlapping-legend / misleading-scale / inconsistent-precision / weak-caption / unreadable-two-column.
   - `stage`: audit / redesign / caption-writing / latex-placement.
4. State the detected axes in one short line.
5. Load only the matching fragments.
6. Map each figure/table to the claim it supports.
7. Report first-impression risks before cosmetic suggestions.

## Output Contract

Default output:

```text
Detected axes: visual_type=..., check_type=..., failure_mode=..., stage=...

Figure/table audit
Item | Supported claim | First-impression risk | Technical issue | Fix

Priority fixes
1. ...
```

For caption writing, return revised captions plus missing information placeholders.

For redesign requests, provide concrete plot/table changes rather than generic advice.

## Red Lines

Do not recommend misleading axis scaling.

Do not invent experimental results or statistical significance.

Do not make visual changes that obscure fair comparison, uncertainty, or negative results.
