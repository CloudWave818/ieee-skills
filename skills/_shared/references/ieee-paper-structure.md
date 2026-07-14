# IEEE Paper Structure

Use this reference when drafting, diagnosing, or restructuring IEEE manuscripts.

## Abstract

Use a compact problem-method-result-contribution structure:

1. Background or engineering problem under a specific condition.
2. Limitation of existing methods.
3. Proposed method and its key mechanism.
4. Experimental setting and quantitative result if available.
5. Practical contribution or implication.

The abstract may follow the paper sequence, but it should not become a table of contents. Include the most important result when available.

## Introduction

Build the argument in this order:

1. Engineering context and object.
2. Condition that makes the problem hard or important.
3. Review of method families and their limitations.
4. Gap statement tied to the condition, not only to citation scarcity.
5. Proposed idea and why it fits the system.
6. Numbered contributions.

Contribution bullets should be specific and verifiable. Avoid claiming a contribution for routine implementation details.

## Related Work

Organize by method family or technical limitation, not by one-paper-one-sentence chronology.

For each cluster, identify:

1. What the family does well.
2. What condition or assumption limits it.
3. How this limitation motivates the proposed method.

## Method

Make the method reproducible:

1. Problem definition and notation.
2. Overall framework.
3. Core modules or algorithm steps.
4. Loss functions, constraints, or optimization details.
5. Complexity, deployment cost, or implementation details when relevant.

Every major design choice should be justified by the object, condition, or prior limitation.

## Experiments

Minimum expectation:

1. Dataset, hardware, implementation, and parameter settings.
2. Traditional baseline and recent baseline comparisons.
3. Ablation studies for each claimed module.
4. Robustness or condition-specific tests when the title or claim mentions a condition.
5. Complexity or efficiency analysis when deployment, lightweight design, or real-time performance is claimed.

## Conclusion

Summarize the technical finding, not only the task completion. Include the most important quantitative result if available. Limitations and future work can help preempt reviewer concerns, but do not expose a fatal weakness that the manuscript cannot address.
