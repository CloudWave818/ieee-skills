# IEEE Plotting Contract Reference

Use this reference when converting a user request into a reproducible IEEE figure or table plan.

## Contract Template

```text
Core claim:
Figure role: comparison / ablation / robustness / complexity / convergence / architecture / error analysis / system setup / qualitative example
Object and condition:
Dataset or testbed:
Methods and baselines:
Metrics:
Higher/lower is better:
Uncertainty or repeats:
Final placement: one-column / two-column / page-wide / supplement
Output formats:
Source data:
Reviewer risk:
```

## Panel Mapping

Use one panel for one evidence role:

- **comparison**: proposed method versus strong, recent, and traditional baselines.
- **ablation**: method variants that isolate contributions.
- **robustness**: performance across noise, load, shift, disturbance, missing data, or operating conditions.
- **complexity**: runtime, memory, FLOPs, parameters, latency, communication cost, or deployment resource.
- **convergence**: iteration/time behavior with a meaningful stopping condition.
- **error analysis**: confusion, residual, failure cases, subgroup behavior, or qualitative examples.
- **architecture/setup**: system boundary, signal/data flow, hardware/testbed, or algorithm pipeline.

Drop panels that only repeat the same claim unless they are necessary for a different operating condition.

## IEEE-Specific Risks

- A visually impressive chart that omits baseline fairness is weak evidence.
- A small improvement without variance, seeds, or repeats invites skepticism.
- A robustness claim without stress conditions is overclaimed.
- A low-complexity claim without runtime/resource evidence is under-supported.
- A two-column figure that only reads at screen zoom is not publication-ready.
- A table with inconsistent precision suggests careless result handling.

## Caption Contract

Captions should identify:

```text
what is compared;
dataset/testbed and condition;
metric and direction;
main takeaway;
uncertainty or repeat definition when relevant;
where missing details appear if not in the caption.
```

Avoid "Comparison of..." captions that do not state the technical takeaway.
