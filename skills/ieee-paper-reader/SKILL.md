---
name: ieee-paper-reader
description: Read, decompose, and analyze IEEE-style papers using routed technical-reading workflows. Use when extracting problem setting, object-method-condition logic, contributions, method pipeline, equations, datasets, baselines, metrics, ablations, limitations, replication details, citation role, related-work positioning, implementation notes, or reviewer-style assessment from a paper, PDF, abstract, or manuscript excerpt.
---

# IEEE Paper Reader Router

Use this skill to turn an IEEE paper into a structured technical brief. Focus on contribution logic, method mechanics, evidence, and reuse value.

Do not provide only a generic summary. Follow the routing protocol and load the selected fragments.

## Routing Protocol

1. Read `manifest.yaml`.
2. Read every file listed under `always_load`.
3. Detect the axes:
   - `reading_purpose`: literature-review / implementation / replication / reviewer-assessment / citation-positioning / quick-summary.
   - `input_scope`: full-paper / abstract-only / introduction-related-work / method-only / experiments-only / figures-tables / excerpt.
   - `paper_type`: algorithmic / system / hardware / control / communications / signal-processing / survey / general.
   - `extraction_focus`: contribution / method-pipeline / equations / experiments / limitations / reproducibility / related-work.
   - `output_depth`: brief / standard / deep.
4. State the detected axes in one short line.
5. Load only the matching fragments.
6. Extract a source-bounded fact base before analysis.
7. Mark missing information when the input is partial.

## Output Contract

Default:

```text
Detected axes: reading_purpose=..., input_scope=..., paper_type=..., extraction_focus=..., output_depth=...

Paper kernel
- Object:
- Method:
- Condition:
- Prior limitation:
- Main contribution:
- Evidence:

Structured notes
[purpose-specific output]

Limitations / missing information
- ...
```

For implementation or replication, include a checklist of missing details.

For citation positioning, include how the paper should and should not be cited.

## Red Lines

Do not invent paper content, equations, results, datasets, or limitations not present in the supplied material.

Do not overquote source text. Summarize and paraphrase.

If the input is only an abstract or excerpt, keep the assessment bounded.
