---
name: ieee-experiment
description: Design, audit, and strengthen experimental validation for IEEE manuscripts using routed claim-evidence checks. Use when planning experiments, selecting baselines, designing ablations, choosing metrics, checking fairness, adding robustness tests, explaining results, analyzing complexity, building claim-to-evidence matrices, or responding to reviewer concerns about insufficient experiments.
---

# IEEE Experiment Router

Use this skill to decide whether the experiments prove the paper's claims. The primary output is an evidence audit, not generic advice.

Do not design experiments from memory alone. Follow the routing protocol and load the selected fragments.

## Routing Protocol

1. Read `manifest.yaml`.
2. Read every file listed under `always_load`.
3. Detect the axes:
   - `task_type`: classification / detection / regression / control / signal-processing / communications / optimization / hardware-system / general.
   - `evidence_type`: baseline / ablation / robustness / complexity / statistical / real-world / reproducibility.
   - `failure_mode`: missing-traditional-baseline / unfair-comparison / weak-ablation / no-condition-test / overclaimed-results / insufficient-reproducibility.
   - `stage`: planning / audit / result-writing / reviewer-response.
4. State the detected axes in one short line.
5. Load only the matching fragments.
6. Build or update a claim-evidence matrix.
7. Identify missing experiments by reviewer impact.

## Output Contract

Default output:

```text
Detected axes: task_type=..., evidence_type=..., failure_mode=..., stage=...

Claim-evidence matrix
Claim | Required evidence | Current evidence | Missing experiment | Review risk

Priority fixes
1. ...
```

For experiment planning, return an experiment plan with baselines, metrics, variables, controlled conditions, and expected claims.

For result writing, return IEEE-style result paragraphs and flag any claim that lacks evidence.

## Red Lines

Do not invent numerical results, datasets, baseline performance, p-values, hardware metrics, or statistical significance.

Do not recommend unnecessary experiments that do not support a stated claim.

Do not treat "more experiments" as automatically better. Prioritize experiments that close the reviewer's proof gap.
