# IEEE Chart and Table Patterns

Use this reference when selecting a figure/table design or rewriting plotting code.

## Common IEEE Patterns

| Need | Prefer | Avoid |
|---|---|---|
| Method comparison across datasets | grouped bar, compact table, dot/interval plot | 3D bars, overcrowded radar |
| Ablation | ordered bar/table with variants named by removed component | arbitrary colors without variant logic |
| Robustness across stress level | line plot with markers and monotonic stress axis | disconnected bars for continuous stress |
| Runtime/complexity | log-scale line/scatter when range is large; Pareto plot for accuracy-cost tradeoff | hiding cost in text only |
| Convergence | line plot against iterations/time with baseline/reference | cropped y-axis that exaggerates small gains |
| Classification errors | normalized confusion matrix plus per-class table when needed | raw counts without class imbalance context |
| Detection/segmentation | PR/ROC, qualitative examples, IoU/F1 table | only cherry-picked images |
| Control/robotics | trajectory plot, tracking error, disturbance response, stability region | only final scalar score |
| Communications/signal processing | SNR/BER/SER curves, channel/load conditions, spectrum/PSD | missing operating condition |
| Learning-based control/RL | state-action-reward architecture plus actor/critic/update path and deployment action | black-box neural-network block without system boundary |
| Hardware/system | block diagram, timing/resource table, testbed photo/schematic | decorative architecture without data flow |

## Styling Defaults

- Use white plot background.
- Use black/gray axes with restrained method colors.
- Use line style and marker redundancy for grayscale.
- Use direct labels when a legend would obscure curves.
- Keep shared legends outside dense plots when possible.
- Align panels and axes across related comparisons.
- Make metric direction explicit: higher is better or lower is better.
- Start bar charts at zero unless there is a defensible reason not to.
- Use log scale only when the phenomenon or value range justifies it, and label it clearly.

## Table Defaults

- Put the main metric near the left or visually emphasize it without hiding other metrics.
- Group rows by method family or operating condition.
- Use consistent decimal precision per metric.
- Mark best and second-best only when the comparison is fair.
- Do not bold statistically indistinguishable wins unless the manuscript explains the test.
- Include units in headers, not repeated in every cell.

## Multi-Panel Defaults

- Give each panel a distinct evidence role.
- Use panel labels `(a)`, `(b)`, `(c)` consistently with the manuscript.
- Place architecture/setup before quantitative validation when it helps interpretation.
- Keep one visual grammar for the same metric across panels.
- Avoid squeezing many small panels into one column when a two-column figure is justified.
