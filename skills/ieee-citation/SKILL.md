---
name: ieee-citation
description: Audit or fix IEEE citations, references, BibTeX, citation support, or missing prior work.
---

# IEEE Citation

Make references accurate, support the manuscript's claims, and follow the requested IEEE citation conventions.

## Route

Infer the citation task, source type, citation role, visible failure mode, and required verification level. Use `manifest.yaml` to load only matching fragments. Formatting-only work can stay local; factual metadata or claim-support checks should use the level of verification the task requires.

User instructions take precedence over workflow preferences in this skill. Keep router metadata internal unless the distinction between supplied and verified information matters to the result.

## Completion

For audits, identify unsupported, incomplete, misplaced, or missing citations and give a concrete fix. For BibTeX cleanup, return corrected entries only from metadata the user supplied or that was verified. Separate formatting changes from factual verification.

## Integrity

Do not fabricate references, DOI values, page numbers, venues, or metadata. Do not claim that a source supports a sentence without source evidence. Mark unresolved metadata as unverified.
