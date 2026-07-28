# Claim-Evidence Matrix Example

Use this with `ieee-experiment` to check whether the experiments prove the manuscript claims.

| Claim | Required Evidence | Current Evidence | Missing Experiment | Review Risk |
|---|---|---|---|---|
| The proposed method improves performance under `[condition]`. | Test across the named condition against traditional and recent baselines. | `[current table/figure]` | Add `[condition sweep / cross-domain / noise-level / load-speed]` experiment. | Critical if the condition is in the title or abstract. |
| Module A contributes to robustness. | Remove or replace Module A and compare robustness metrics. | `[ablation table?]` | Add ablation under the same condition used in the main experiment. | Major |
| The method is lightweight enough for deployment. | Parameters, FLOPs, memory, latency, and hardware/software setting. | `[accuracy only?]` | Add complexity and latency table with hardware details. | Major if lightweight or real-time is claimed. |
| The improvement is reproducible. | Dataset split, preprocessing, implementation details, random seeds or variance. | `[partial setup?]` | Add setup details and mean/std over repeated runs when randomness matters. | Major |

## Priority Fixes

1. Do not add experiments just to increase quantity. Add the smallest experiment that closes the highest-risk proof gap.
2. Match metrics to claims: accuracy for classification, F1 for imbalance, latency for real-time, memory/FLOPs for lightweight deployment, robustness curves for noisy or shifted conditions.
3. Keep negative or weaker results visible when they define the method's boundary.

