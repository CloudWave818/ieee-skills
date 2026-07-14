# IEEE Engineering Logic

Use this reference for IEEE-style manuscripts in engineering, computer science, AI, communications, control, signal processing, electrical/electronic engineering, and applied systems.

## Core Claim Chain

An IEEE paper should make this chain explicit:

1. Object: the system, device, signal, task, dataset, process, or operating target.
2. Condition: the operating condition, disturbance, constraint, scenario, dataset shift, resource limit, or failure mode that makes the problem difficult.
3. Harm: why the problem matters in engineering terms, such as safety, reliability, cost, latency, efficiency, accuracy, robustness, or deployment feasibility.
4. Prior limitation: why existing methods are insufficient under the stated condition.
5. Method rationale: why the proposed method is suited to the object and condition.
6. Verification: which experiments prove the claimed advantage over traditional and recent baselines.

If any link is missing, ask for the missing information or state the weakness directly.

## Title Rule

Prefer titles that include object, method, and condition.

Weak:

```text
An Improved Fault Diagnosis Method Based on Deep Learning
```

Stronger:

```text
A Lightweight Transformer-Based Fault Diagnosis Method for Rolling Bearings Under Variable-Speed Conditions
```

Do not force all three elements when the venue or field has a shorter established convention, but flag vague titles that omit the real application condition.

## Introduction Logic

Avoid arguing novelty only by saying that few studies exist. Instead, show:

1. The object is important.
2. The condition causes a serious engineering problem.
3. Existing method families fail or degrade under that condition.
4. The proposed design addresses the specific failure.
5. Contributions are concrete, testable, and preferably numbered.

## Method Rationale

When a method is selected, connect it to the system characteristics.

Weak:

```text
We use a CNN because it has good feature extraction ability.
```

Stronger:

```text
Because the vibration signal contains local transient impulses whose locations vary with load, a multi-scale convolutional front end is used to capture short-duration fault signatures before temporal aggregation.
```

## Claims Discipline

Prefer quantified claims. Avoid unsupported words such as novel, effective, excellent, robust, advanced, and superior unless the manuscript provides concrete evidence.

When revising, preserve technical meaning and do not invent methods, datasets, metrics, or numerical results.
