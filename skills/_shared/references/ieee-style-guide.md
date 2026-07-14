# IEEE Style Guide

Use this reference for IEEE-style technical English polishing.

## Voice

Prefer direct, precise, engineering-oriented prose. Avoid inflated novelty language.

Prefer:

```text
The proposed encoder reduces the parameter count by 32.4% while maintaining comparable accuracy.
```

Avoid:

```text
The proposed method achieves excellent performance and has great practical significance.
```

## Sentence Pattern

Use explicit causality:

```text
Because X occurs under Y, existing methods Z degrade. Therefore, this paper introduces A to address B.
```

Use concrete technical nouns:

```text
load variation, class imbalance, missing labels, domain shift, multipath fading, computational latency
```

Avoid vague nouns:

```text
some problems, certain factors, many advantages, obvious improvement
```

## Contribution Wording

Good contribution statements usually include:

1. The technical object.
2. The proposed mechanism.
3. The condition or limitation addressed.
4. The evidence that verifies it.

Weak:

```text
This paper proposes a new model with better performance.
```

Stronger:

```text
This paper proposes a dual-branch temporal attention model that separates periodic and transient components, improving fault classification under variable-speed conditions.
```

## Polishing Rules

1. Preserve technical facts.
2. Do not invent citations, datasets, metrics, or numerical gains.
3. Replace vague praise with measurable evidence.
4. Split overloaded sentences.
5. Align terminology across title, abstract, method, experiments, and conclusion.
6. Use active voice when it improves clarity.
7. Keep abbreviations defined on first use.

## Common Repairs

Replace "has important significance" with a concrete engineering consequence.

Replace "the research on X is rare" with a limitation of existing methods under a specific condition.

Replace "simulation proves effectiveness" with the actual dataset, baseline, metric, and result when provided.
