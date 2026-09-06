---
name: ieee-figure-table
description: Create or audit IEEE figures, tables, captions, plotting code, and publication-scale visual evidence.
---

# IEEE Figure and Table

Make figures and tables readable, fair, claim-aligned, and usable at IEEE publication scale.

## Route

Infer visual type, requested check, stage, and plotting backend. Load only the relevant fragments from `manifest.yaml`.

For plotting, honor an explicit backend first, then the input workflow or a saved preference. When either Python or R is suitable and no preference exists, use Python and continue. Persist a backend preference only when the user explicitly asks to save one.

Load the figure-contract material for creation or substantial redesign, first-impression guidance for visual audits, and export guidance when files are being delivered. Do not load all visual references for a caption-only or table-only task.

## Completion

For audits, identify the highest-impact readability, fairness, caption, layout, or evidence problem and give concrete corrections. For creation or redraw work, carry the task through code/file generation and proportionate QA when tools are available. Check the final intended column size and export requirements when they matter to delivery.

## Integrity

Do not alter or invent experimental data, uncertainty, or significance. Do not recommend misleading axes or scales. Do not use IEEE marks or imply official IEEE approval/compliance.
