---
name: ieee-summarize
description: Summarize, organize, and normalize messy research materials into an IEEE-ready writing brief before manuscript drafting. Use when Codex needs to process a folder or collection of experiment logs, code files, AI chat exports, idea notes, literature summaries, related-work notes, copied introduction excerpts, Zotero-derived paper summaries, tables, figures, or scattered Markdown/text records and convert them into structured inputs for ieee-writing, ieee-experiment, ieee-citation, ieee-reviewer, or ieee-response.
---

# IEEE Summarize Router

Use this skill before `ieee-writing` when the user's research materials are scattered, chronological, duplicated, or not yet in manuscript structure. The output is not final prose; it is an evidence-grounded research brief that later writing skills can use.

Do not turn messy notes into polished claims by guessing. Preserve uncertainty, source paths, missing evidence, and contradictions.

## Routing Protocol

1. Read `manifest.yaml`.
2. Read every file listed under `always_load`.
3. Detect the request axes:
   - `material_scope`: folder / pasted-notes / code-and-logs / literature-pack / mixed.
   - `output_target`: research-brief / writing-input / experiment-summary / related-work-seed / claim-evidence-seed.
   - `cleanup_level`: inventory / standard / deep.
4. State the detected axes in one short line.
5. If a folder path is provided, inventory first:
   - Prefer `scripts/inventory_research_folder.py <folder>`.
   - If the script is unsuitable, use `rg --files <folder>`.
   - Do not read every large file blindly. Select representative and high-signal files by category.
6. Map raw material into IEEE evidence slots:
   - problem object and operating condition,
   - engineering harm or practical motivation,
   - method idea and implementation clues from notes/code,
   - datasets, baselines, metrics, ablations, robustness, complexity, and reproducibility,
   - related-work families and closest-prior-work candidates,
   - contribution candidates and conclusion candidates.
7. Preserve provenance. Every important extracted point should include a file path, heading, filename, or note source when available.
8. Mark `solid`, `partial`, `unclear`, or `missing` for each evidence block.
9. Hand off to the next skill explicitly: `ieee-writing`, `ieee-experiment`, `ieee-citation`, `ieee-reviewer`, or `ieee-polishing`.

## Output Contract

Default output:

```text
Detected axes: material_scope=..., output_target=..., cleanup_level=...

Material inventory
- Notes:
- Code:
- Experiments:
- Literature:
- Figures/tables:
- Unknown / skipped:

IEEE Research Brief
- Working title:
- Research object:
- Operating condition / constraints:
- Engineering harm:
- Core method:
- Implementation clues:
- Experiment evidence:
- Related-work seed:
- Contribution candidates:
- Conclusion candidates:
- Missing evidence:
- Contradictions / risks:

Next skill handoff
- Recommended next skill:
- Prompt-ready brief:
```

For folder-level work, create or update a Markdown file only when the user asks for a file. Suggested filename: `ieee-research-brief.md`.

## Red Lines

Do not invent paper titles, citations, datasets, numerical results, code behavior, reviewer comments, or experiment outcomes.

Do not treat AI chat exports as verified evidence. Label them as ideation unless confirmed by code, logs, data, or papers.

Do not summarize copied paper introductions into plagiarism-ready text. Extract reusable background logic, domain motivation, and citation roles instead.

Do not remove negative results or failed experiments; classify them as limitation, ablation clue, or future-work evidence.
