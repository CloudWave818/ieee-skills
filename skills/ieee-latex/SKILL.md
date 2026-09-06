---
name: ieee-latex
description: Fix IEEEtran LaTeX compilation, layout, floats, equations, tables, bibliography, or submission-PDF issues.
---

# IEEE LaTeX

Diagnose and apply the smallest IEEE-compatible fix to the requested LaTeX problem.

## Route

Infer the task, venue/template, affected object, failure mode, and manuscript stage. Read `manifest.yaml` and load only guidance relevant to the visible problem. Inspect source, logs, or rendered output only to the extent needed to diagnose and verify the change.

User instructions take precedence over workflow preferences in this skill. Keep router metadata internal unless it helps explain a diagnosis.

## Completion

For direct edits, make the requested change and run checks proportionate to it when execution tools are available. Use rendered PDF inspection for layout judgments when a PDF exists. Broaden verification only when failures, changed dependencies, or submission-stage requirements justify it.

Return the fix or edited code first, followed by a short diagnosis or remaining check when useful.

## Integrity

Preserve author content and the target IEEE template. Do not change bibliography style or package structure for cosmetic convenience. Prefer vector or suitable high-resolution figure assets over screenshots.
