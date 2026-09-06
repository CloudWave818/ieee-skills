---
name: ieee-paper-reader
description: Analyze a paper for contributions, methods, equations, experiments, limitations, replication details, or citation positioning.
---

# IEEE Paper Reader

Turn the supplied paper material into a source-bounded technical analysis.

## Route

Infer reading purpose, available scope, paper type, extraction focus, and desired depth. Read `manifest.yaml` and load only fragments that serve that purpose. A quick summary should remain lightweight; implementation, replication, or reviewer analysis may justify deeper fragments and references.

User instructions take precedence over workflow preferences in this skill. Keep routing metadata internal unless the available source scope materially limits the answer.

## Completion

Establish a fact base from the supplied paper before drawing conclusions. Extract the method mechanics and evidence relevant to the user's purpose. For implementation or replication, identify missing details that block reproduction. For citation positioning, explain the role the paper can support.

## Integrity

Do not invent paper content, equations, results, datasets, limitations, or implementation details. Mark claims that cannot be established from a partial paper. Paraphrase rather than reproducing long source passages.
