---
name: ieee-response
description: Draft, diagnose, and improve IEEE rebuttals, revision plans, cover letters, response letters, and point-by-point replies using routed reviewer-comment handling. Use when responding to IEEE reviewer or editor comments about novelty, scope, method, experiments, baselines, figures, tables, citations, writing, LaTeX formatting, limitations, compliance, or technical correctness.
---

# IEEE Response Router

Use this skill to convert reviewer criticism into manuscript actions and precise, respectful point-by-point replies.

Do not write a defensive response. Do not promise changes that the manuscript does not make. Follow the routing protocol and load the selected fragments.

## Routing Protocol

1. Read `manifest.yaml`.
2. Read every file listed under `always_load`.
3. Detect the axes:
   - `comment_type`: novelty / scope / method / experiment / baseline / figure-table / citation / writing / format / limitation / technical-error.
   - `action_type`: add-experiment / add-explanation / revise-text / correct-error / add-citation / improve-figure-table / acknowledge-limitation / disagree-with-evidence.
   - `response_stage`: rebuttal / major-revision / minor-revision / resubmission / cover-letter.
   - `evidence_status`: evidence-added / evidence-planned / evidence-unavailable / text-only-fix.
   - `tone`: standard / concise / very-polite / firm.
4. State the detected axes in one short line when useful.
5. Load only the matching fragments.
6. For each reviewer comment, produce:
   - issue classification,
   - required manuscript action,
   - evidence needed,
   - response wording,
   - revision-location placeholder if exact page/line is unknown.

## Output Contract

Default point-by-point format:

```text
Reviewer comment:

Classification:
- comment_type:
- action_type:
- evidence_status:

Response:
[polite, specific response]

Manuscript revision:
[what changed and where]

Evidence:
[new experiment/result/citation/figure/textual clarification]
```

For multiple comments, add a `Revision action list` before the detailed responses.

For cover letters, summarize major changes, added experiments, figure/table improvements, and remaining limitations without overselling.

## Red Lines

Do not invent page numbers, line numbers, experiments, results, citations, or editor instructions.

Do not say "we have addressed all concerns" unless every concern is visibly addressed.

Do not dismiss reviewer comments as misunderstandings without first improving manuscript clarity.
