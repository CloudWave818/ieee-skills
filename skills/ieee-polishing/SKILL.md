---
name: ieee-polishing
description: Polish or translate existing technical prose into concise IEEE-style English while preserving facts and claim strength.
---

# IEEE Polishing

Improve the supplied prose while preserving its technical meaning and evidence boundary.

## Route

Infer section, source language, dominant writing problem, and edit depth from the text. Read `manifest.yaml` and load only fragments that address the visible issue. Light edits should stay light; structural guidance is for passages whose argument structure actually needs repair.

User instructions take precedence over this skill's workflow preferences. Keep routing metadata internal unless it affects an important editorial choice.

## Completion

Return finished polished text first. Repair section logic when needed, then sentence-level clarity and natural author voice. Add notes only when a structural change, unsupported claim, or missing evidence still requires author attention.

## Integrity

Do not invent numerical results, datasets, baselines, citations, equations, algorithms, or claims. Preserve uncertainty and claim strength. Keep IEEE prose direct, technical, and verifiable.
