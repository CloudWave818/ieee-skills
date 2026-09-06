---
name: ieee-writing
description: Draft or restructure IEEE manuscript sections from supplied research material and evidence.
---

# IEEE Writing

Draft or rebuild the manuscript content the user requested.

## Route

Infer venue type, section, language, and technical domain from the request. Read `manifest.yaml` only when specialized guidance would materially improve the result, then load only the matching fragments or references. Do not pre-load unrelated core or shared files.

User instructions take precedence over workflow preferences in this skill. Keep routing decisions internal unless ambiguity materially affects the result or the user asks to see them.

Use the engineering chain `object -> condition -> harm -> prior limitation -> method rationale -> verification` when it helps the section's argument. Treat it as a reasoning aid rather than a mandatory prose template.

## Completion

Carry the authorized drafting task through to usable manuscript text. Return the requested prose first. Add compact author checks only for missing evidence or facts that materially constrain a claim.

For outlines, organize claims around the evidence they require. Use deeper structure, style, or domain fragments only when the task actually needs them.

## Integrity

Do not invent results, datasets, baselines, citations, equations, algorithms, numerical gains, or venue requirements. Keep claims falsifiable and bounded by supplied or verified evidence.
