---
name: ieee-experiment
description: Design or audit experiments that support IEEE manuscript claims, including baselines, ablations, robustness, complexity, and reproducibility.
---

# IEEE Experiment

Design or audit the evidence needed to support the paper's claims.

## Route

Infer the technical task, evidence category, visible failure mode, and manuscript stage. Read `manifest.yaml` and load only the fragments needed for those dimensions. Load `static/core/claim-evidence-matrix.md` for multi-claim audits or explicit claim-evidence work rather than for every experiment request.

User instructions take precedence over workflow preferences in this skill. Keep router metadata internal unless it resolves a material ambiguity.

## Completion

Prioritize the smallest set of experiments that closes the highest-impact proof gaps. For planning, specify baselines, metrics, controlled variables, conditions, and the claim each experiment tests. For audits, map claims to current evidence and missing evidence. For result writing, flag claims that exceed the supplied results.

Verification effort should match the task. Avoid adding experiments or repeated checks that do not test a stated claim or resolve an identified review risk.

## Integrity

Do not invent numerical results, datasets, baseline performance, p-values, hardware metrics, or statistical significance. Preserve negative results and fairness constraints.
