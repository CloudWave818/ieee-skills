# IEEE Research Brief Template

Use this template as the normalized output before `ieee-writing`.

```markdown
# IEEE Research Brief

## 1. Material Boundary
- Source folder or inputs:
- Files inspected:
- Files skipped:
- Confidence:

## 2. Problem Definition
- Research object:
- Operating condition / constraints:
- Engineering harm:
- Target IEEE domain:
- Target venue type if known:

## 3. Method Seed
- Core idea:
- System pipeline:
- Key modules:
- Algorithm / model / optimization clues:
- Implementation evidence:
- What is confirmed by code:
- What is only from notes or AI chat:

## 4. Experiment Seed
| Claim | Current evidence | Missing evidence | Source |
|---|---|---|---|
|  | solid / partial / unclear / missing |  |  |

## 5. Related-Work Seed
| Paper / note | Role | Why relevant | Limitation to use | Source |
|---|---|---|---|---|
|  | background / baseline / closest prior / dataset / method family |  |  |  |

## 6. Contribution Candidates
1. [claim] - evidence status: solid / partial / unclear / missing - source:
2. ...

## 7. Section Handoff
- Title keywords:
- Abstract facts:
- Introduction logic:
- Related-work groups:
- Method facts:
- Experiment facts:
- Conclusion facts:

## 8. Risks and Missing Inputs
- Unsupported claims:
- Weak baseline risk:
- Missing ablation / robustness / complexity:
- Citation gaps:
- Reproducibility gaps:
- Contradictions:

## 9. Recommended Next Skill
- Use `$ieee-writing` for:
- Use `$ieee-experiment` for:
- Use `$ieee-citation` for:
- Use `$ieee-reviewer` for:
```

## Evidence Status

- `solid`: backed by code, data, logs, figures, citations, or repeated notes.
- `partial`: plausible but missing one support layer.
- `unclear`: present in notes but ambiguous or contradicted.
- `missing`: required for the claim but not found.
