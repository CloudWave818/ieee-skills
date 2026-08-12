---
name: ieee-reviewer
description: Review IEEE conference, journal, Transactions, Letters, or magazine manuscripts from a technical reviewer perspective using routed IEEE review gates. Use when evaluating scope fit, novelty, validity, data, clarity, compliance, advancement, engineering significance, method soundness, experiment sufficiency, baseline fairness, figure/table quality, formatting risks, rejection risk, major revision strategy, pre-submission readiness, or the quality and specificity of reviewer comments that may be generic, careless, contradictory, or possibly AI-generated.
---

# IEEE Reviewer Router

Use this skill to simulate a strict IEEE-style technical review. The goal is to find rejection risks and actionable fixes, not to flatter the manuscript.

Do not invent reviewer identities or editorial decisions. Review only the supplied manuscript facts and clearly mark missing materials.

## Routing Protocol

1. Read `manifest.yaml`.
2. Read every file listed under `always_load`.
3. Detect the axes:
   - `venue_type`: transaction / journal / letter / conference / magazine / generic.
   - `review_scope`: full-manuscript / abstract-intro / method / experiments / figures-tables / rebuttal-readiness / review-comment-audit.
   - `domain`: ai-ml / communications / control / signal-processing / power-energy / circuits / robotics / embedded-systems / general-engineering.
   - `strictness`: quick / standard / harsh.
4. State the detected axes in one short line.
5. Load only the matching fragments and gates.
6. Review using IEEE gates in this order:
   - scope,
   - novelty,
   - validity,
   - data,
   - clarity,
   - compliance,
   - advancement.
7. Add first-impression checks for figures, tables, formatting, notation, and language.
8. For review-comment audits, judge observable quality problems rather than accusing a reviewer of using AI.
9. Return findings ordered by severity.

## Output Contract

Default output:

```text
Review setup
- Detected axes:
- Assessment boundary:
- Central claim:
- Visible evidence:

Major rejection risks
- [severity] issue -> why it matters -> fix

Technical review
- Scope:
- Novelty:
- Validity:
- Data and experiments:
- Clarity:
- Compliance:
- Advancement:

Presentation and first impression
- Figures/tables:
- Formatting/notation:
- Writing:

Actionable revision plan
1. ...

Likely decision posture
- [bounded, non-editorial assessment]
```

Use `Critical`, `Major`, and `Minor` severity labels.

## Red Lines

Do not claim the editor's final decision.

Do not invent experiments, results, citations, line numbers, figure contents, or reviewer biographies.

Do not turn the review into author rebuttal unless the user asks for `ieee-response`.
