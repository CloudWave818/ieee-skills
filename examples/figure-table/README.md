# IEEE Figure/Table Examples

These examples show how `ieee-figure-table` turns IEEE-style review concerns into concrete visual evidence.

Updated on 2026-08-01: the three SVG demos were rebuilt after a stricter quality pass. The new version uses wide two-column canvases, multi-panel evidence organization, dedicated legend/summary panels, short labels, text-safe margins, semantic colors, and visible deployment or baseline context.

The skill now also includes a matplotlib house-style helper:

```text
skills/ieee-figure-table/scripts/ieee_plot_style.py
```

Use that helper for real manuscript figures when matplotlib is available. It standardizes IEEE one-column/two-column sizes, semantic colors, print-safe line and marker redundancy, panel labels, grouped bars, trend plots, Pareto plots, and SVG/PDF/PNG/TIFF export.

For figures that are not made end-to-end in Python, use the hybrid workflow in `skills/ieee-figure-table/references/ieee-hybrid-figure-workflow.md`: generate reproducible base panels from code, finish vector layout and annotations in a design/editor tool, and keep an edit log so quantitative evidence remains traceable.

## Examples

| Example | Claim | Output |
|---|---|---|
| Robustness SNR curve | The proposed method remains reliable under low-SNR operating conditions. | `figures/robustness-snr-curve.svg` |
| Accuracy-latency Pareto | The proposed method provides a better accuracy-cost tradeoff for deployment. | `figures/accuracy-latency-pareto.svg` |
| Ablation result table | Each module contributes to accuracy/F1 while preserving deployability. | `figures/ablation-result-table.svg` |
| Hybrid composite workflow | Data panels remain reproducible while vector finishing stays editable and traceable. | `hybrid-workflow.md` |

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
