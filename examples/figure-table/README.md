# IEEE Figure/Table Examples

These examples show how `ieee-figure-table` turns IEEE-style review concerns into concrete visual evidence.

## Examples

| Example | Claim | Output |
|---|---|---|
| Robustness SNR curve | The proposed method remains reliable under low-SNR operating conditions. | `figures/robustness-snr-curve.svg` |
| Accuracy-latency Pareto | The proposed method provides a better accuracy-cost tradeoff for deployment. | `figures/accuracy-latency-pareto.svg` |
| Ablation result table | Each module contributes to accuracy/F1 while preserving deployability. | `figures/ablation-result-table.svg` |

## Generate

The generator intentionally uses only the Python standard library, so the examples can be regenerated without installing plotting packages.

```bash
python examples/figure-table/generate_examples.py
```

Generated files:

```text
examples/figure-table/data/
examples/figure-table/figures/
examples/figure-table/captions.md
```

For real manuscript work, `ieee-figure-table` can still route to matplotlib/seaborn or ggplot2. These examples are lightweight repository demos.
