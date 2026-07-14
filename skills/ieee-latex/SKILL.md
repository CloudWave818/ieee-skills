---
name: ieee-latex
description: Diagnose, fix, and improve IEEEtran LaTeX manuscripts using routed template, layout, float, equation, algorithm, table, bibliography, and PDF-compliance guidance. Use when fixing IEEE LaTeX compile errors, overfull boxes, float placement, two-column layout, figure sizing, tables, equations, algorithms, BibTeX, citation commands, template compliance, or final submission PDF checks.
---

# IEEE LaTeX Router

Use this skill to fix IEEE LaTeX issues while preserving manuscript content and target-template compliance.

Do not make broad package or template changes unless necessary. Follow the routing protocol and load the selected fragments.

## Routing Protocol

1. Read `manifest.yaml`.
2. Read every file listed under `always_load`.
3. Detect the axes:
   - `task_type`: compile-debug / layout-fix / float-placement / table-formatting / equation-formatting / algorithm-formatting / bibliography / pdf-check.
   - `venue_type`: transaction / journal / letter / conference / magazine / generic.
   - `object_type`: figure / table / equation / algorithm / reference / class-file / whole-manuscript.
   - `failure_mode`: overfull-hbox / float-too-large / figure-at-end / broken-citation / duplicate-label / package-conflict / unreadable-table / sparse-page.
   - `stage`: drafting / pre-submission / revision / final-production.
4. State the detected axes when useful.
5. Load only the matching fragments.
6. Inspect source, log, and rendered output when available. Do not judge final layout from `.tex` alone when a PDF can be rendered or inspected.
7. Apply the smallest IEEE-compatible fix.

## Output Contract

```text
Diagnosis:
- Cause:
- Affected object:

Fix:
[minimal LaTeX change or instructions]

Why this works:
[short explanation]

Follow-up checks:
- [compile/render/check PDF]
```

For direct code edits, preserve author content and change only the necessary LaTeX structure.

## Red Lines

Do not switch away from the target IEEE template for convenience.

Do not break IEEE bibliography style for cosmetic citation output.

Do not use screenshots for plots when vector or high-resolution exports are possible.
