# IEEE SubmitCheck Example

This is a template-style example. Replace the placeholders with facts from your manuscript.

## Review Setup

- Target venue: IEEE Transactions / Journal / Conference / Letters / Magazine
- Domain: signal processing / communications / control / AI / power systems / robotics / other
- Assessment boundary: title, abstract, introduction, experiments, figures, references, LaTeX
- Central claim: `[state the main technical claim]`
- Visible evidence: `[datasets, baselines, ablations, robustness tests, figures, tables]`

## Major Rejection Risks

| Severity | Issue | Why It Matters | Fix |
|---|---|---|---|
| Critical | Main condition is named in the title but not tested directly. | IEEE reviewers expect the claimed operating condition to appear in experiments. | Add a condition-specific experiment and report the metric under each condition. |
| Major | Baselines include only weak or outdated methods. | The improvement may look incremental or unfair. | Add one credible traditional baseline and one recent strong baseline. |
| Major | Method rationale is not tied to system characteristics. | The method can look like module stacking. | Explain why the design matches the object, signal, constraint, or failure mode. |
| Minor | Figure captions describe curves but not the takeaway. | Reviewers need to see what evidence each figure proves. | Rewrite captions with dataset, condition, metric, and result takeaway. |

## IEEE Gates

| Gate | Pass Status | Evidence Needed |
|---|---|---|
| Scope | `[pass / risk / unknown]` | Target venue aims and article type |
| Novelty | `[pass / risk / unknown]` | Closest prior work and concrete difference |
| Validity | `[pass / risk / unknown]` | Assumptions, equations, algorithms, implementation details |
| Data | `[pass / risk / unknown]` | Dataset, split, baselines, ablations, robustness |
| Clarity | `[pass / risk / unknown]` | Object-condition-harm chain and notation |
| Compliance | `[pass / risk / unknown]` | IEEE template, ethics, reference style, PDF checks |
| Advancement | `[pass / risk / unknown]` | Engineering meaning beyond one dataset |

## Revision Priorities

1. Close the evidence gap behind the main claim.
2. Strengthen baseline fairness before polishing language.
3. Fix figure/table first-impression risks before final submission.
4. Run IEEEtran, reference, and PDF checks after the technical edits.

