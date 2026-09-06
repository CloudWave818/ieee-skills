---
name: ieee-summarize
description: Turn scattered research notes, code, logs, literature notes, and figures into an evidence-grounded brief for later manuscript work.
---

# IEEE Summarize

Normalize messy research material into a concise, provenance-preserving brief.

## Route

Infer material scope, intended output, and cleanup depth. For folders, inventory enough to locate high-signal sources, then read representative files relevant to the requested brief. Avoid exhaustive file reads unless the task explicitly requires reconciliation across the full collection.

Read `manifest.yaml` and supporting references only when they help the selected material type or output. User instructions take precedence over workflow preferences in this skill.

## Completion

Extract the research object, conditions, method, experiment evidence, related-work seed, contribution candidates, missing evidence, and contradictions that are actually supported by the material. Preserve file paths, headings, filenames, or note provenance for important claims when available.

Produce the brief the user requested. Recommend a downstream skill only when a handoff is useful to the current task.

## Integrity

Do not invent paper titles, citations, datasets, numerical results, code behavior, reviewer comments, or experiment outcomes. Treat AI chat exports as ideation until corroborated. Preserve negative and failed experiments as evidence.
