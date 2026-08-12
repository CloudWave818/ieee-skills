# Example: IEEE Research Brief From Messy Materials

This is the kind of output `ieee-summarize` should produce before `ieee-writing`.

## 1. Material Boundary

- Source folder: `project-notes/`
- Files inspected: idea notes, model code, experiment logs, Zotero paper summaries, copied introduction snippets
- Files skipped: large checkpoints, raw datasets, duplicate chat exports
- Confidence: partial; several experiment claims still need source tables

## 2. Problem Definition

- Research object: latency-aware edge inference scheduling
- Operating condition / constraints: dynamic wireless bandwidth, edge-device energy limits, real-time deadline
- Engineering harm: static offloading policies can miss deadlines or waste energy when channel quality changes
- Target IEEE domain: edge intelligence / communications / embedded systems

## 3. Method Seed

- Core idea: combine temporal state encoding, topology-aware device graph encoding, and constraint-aware policy optimization
- System pipeline: monitor state -> build device-task graph -> encode temporal and graph features -> optimize action under latency/energy constraints
- Implementation evidence:
  - `[source: src/agent.py]` contains actor-critic update logic
  - `[source: configs/edge_rl.yaml]` lists latency, energy, and bandwidth constraints
- Only from notes / AI chat:
  - "adaptive safety penalty" appears in chat export but has no code evidence yet

## 4. Experiment Seed

| Claim | Current evidence | Missing evidence | Source |
|---|---|---|---|
| Proposed policy reduces deadline violations under low bandwidth | partial | Need full baseline table and random-seed variance | `results/run_042.csv` |
| Graph encoder improves robustness to device topology changes | unclear | Need ablation without graph branch | `notes/ablation-plan.md` |
| Method is deployment-friendly | missing | Need complexity, inference latency, and memory footprint | none found |

## 5. Related-Work Seed

| Paper / note | Role | Why relevant | Limitation to use | Source |
|---|---|---|---|---|
| DRL offloading survey note | background | Frames edge offloading under dynamic networks | Too broad; not closest prior work | `literature/zotero-summary.md` |
| Graph-based resource allocation note | method family | Supports topology-aware modeling | Need exact citation metadata | `literature/graph-rl.md` |
| Static heuristic baseline note | baseline | Candidate traditional baseline | Need implementation details | `notes/baselines.md` |

## 6. Contribution Candidates

1. Constraint-aware multimodal state representation for edge scheduling - evidence status: partial - source: `src/agent.py`, `configs/edge_rl.yaml`
2. Topology-aware graph encoder for device-task interactions - evidence status: unclear - source: `notes/ablation-plan.md`
3. Low-bandwidth robustness improvement - evidence status: partial - source: `results/run_042.csv`

## 7. Section Handoff

- Title keywords: edge intelligence, latency-aware scheduling, graph reinforcement learning
- Abstract facts: object, dynamic bandwidth condition, actor-critic method, baseline comparison needed
- Introduction logic: dynamic edge environment -> deadline/energy harm -> static policy limitation -> topology/temporal constraints
- Related-work groups: DRL offloading, graph resource allocation, latency-aware edge inference
- Method facts: state encoder, graph encoder, constraint penalty, actor-critic update
- Experiment facts: low-bandwidth condition, deadline violation, energy cost, ablation still missing
- Conclusion facts: do not claim deployment readiness until complexity evidence is added

## 8. Risks and Missing Inputs

- Unsupported claims: deployment-friendly, generalization to unseen topology
- Weak baseline risk: only one traditional heuristic found
- Missing ablation / robustness / complexity: graph branch ablation, seed variance, inference latency
- Citation gaps: closest graph-RL and recent edge-intelligence baselines
- Reproducibility gaps: dataset split, hyperparameter budget, random seeds

## 9. Recommended Next Skill

- Use `$ieee-experiment` to convert the experiment seed into a claim-evidence matrix.
- Use `$ieee-citation` to verify the related-work seed and citation roles.
- Use `$ieee-writing` only after the missing evidence list is accepted or bounded.
