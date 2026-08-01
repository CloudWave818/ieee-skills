# IEEE Figure/Table Examples

These examples show how `ieee-figure-table` turns IEEE-style review concerns into concrete visual evidence.

The skill now also includes a matplotlib house-style helper:

```text
skills/ieee-figure-table/scripts/ieee_plot_style.py
```

Use that helper for real manuscript figures when matplotlib is available. It standardizes IEEE one-column/two-column sizes, semantic colors, print-safe line and marker redundancy, panel labels, grouped bars, trend plots, Pareto plots, and SVG/PDF/PNG/TIFF export.

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

For real manuscript work, `ieee-figure-table` can route to matplotlib/seaborn or ggplot2. The repository SVG examples are lightweight demos; the bundled matplotlib helper is the preferred starting point for polished IEEE paper figures.
