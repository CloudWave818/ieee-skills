---
name: ieee-writing
description: Draft, restructure, and diagnose IEEE-style technical manuscript sections using a routed static/dynamic workflow. Use for IEEE conference, journal, Transactions, Letters, or magazine papers when writing titles, abstracts, introductions, related work, methods, experiments, conclusions, contribution statements, section outlines, or Chinese-to-English engineering paper drafts in AI, computer science, communications, control, signal processing, electrical/electronic engineering, power, robotics, circuits, and applied systems.
---

# IEEE Writing Router

Use this skill to draft or rebuild IEEE manuscript sections. This skill is split into a dynamic router and static fragments so each request loads only the IEEE rules it needs.

Do not draft only from memory. Follow the routing protocol and load the selected files.

## Routing Protocol

1. Read `manifest.yaml`.
2. Read every file listed under `always_load`.
3. Detect the request axes from the user's material:
   - `venue_type`: transaction / journal / letter / conference / magazine / generic.
   - `section`: title / abstract / introduction / related-work / method / experiments / conclusion.
   - `language`: en / zh-to-en.
   - `domain`: ai-ml / communications / control / signal-processing / power-energy / circuits / robotics / embedded-systems / general-engineering.
4. State the detected axes in one short line before drafting.
5. Load only the fragments mapped to the detected axis values.
6. Draft using this priority order:
   - official IEEE constraints and engineering logic,
   - venue-type expectations,
   - section-specific structure,
   - domain-specific gates,
   - language repair rules.
7. If evidence, metrics, baselines, or constraints are missing, use explicit placeholders or list missing inputs. Do not invent results, datasets, citations, or numerical gains.

## Output Contract

For section drafting, return the drafted text first. Then add a compact `Author checks` note when the draft depends on missing evidence, unverified claims, or experiments that still need to be supplied.

For outline requests, return a section plan with claim, evidence, and reviewer-risk notes.

## On-Demand References

Read files under `references/` only when the manifest says they are relevant or when the user asks for deeper examples, official-source basis, paper-level diagnosis, or a pre-submission audit.
