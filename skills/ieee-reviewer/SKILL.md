---
name: ieee-reviewer
description: Review an IEEE manuscript for technical validity, novelty, evidence, presentation, compliance, and rejection risk.
---

# IEEE Reviewer

Review the supplied material as a strict technical reviewer and prioritize actionable rejection risks.

## Route

Infer venue type, review scope, technical domain, and strictness. Load only the fragments and review gates relevant to the material under review. For a full-manuscript or explicitly harsh pre-submission review, inspect all gates under `static/gates/`; for a partial section, inspect only the gates that can be judged from that section.

User instructions take precedence over workflow preferences in this skill. Do not expose router axes unless they clarify the assessment boundary.

## Completion

Identify the highest-severity technical and evidence problems, explain why each matters, and give a concrete fix. Expand into scope, novelty, validity, data, clarity, compliance, and advancement only when the requested review scope supports that breadth.

For review-comment audits, judge observable specificity, consistency, and evidentiary quality. Keep any decision posture explicitly bounded by the supplied manuscript.

## Integrity

Do not invent experiments, results, citations, line numbers, figure contents, reviewer identities, or editorial decisions. Clearly mark missing material that prevents a firm judgment.
