# IEEE Plotting API Reference

Use this reference when generating Python/matplotlib code for IEEE-style manuscript figures.

The bundled helper lives at:

```text
scripts/ieee_plot_style.py
```

Use it directly when available. For manuscript repositories that should not depend on this skill directory, copy the needed functions into the target plotting script and keep the API behavior.

## Core Constants

```python
IEEE_ONE_COL_IN = 3.5
IEEE_TWO_COL_IN = 7.16
PALETTE = {
    "proposed": "#0B5CAD",
    "proposed_light": "#8EC3F5",
    "recent_baseline": "#0F766E",
    "traditional_baseline": "#B64040",
    "cost": "#B7791F",
    "neutral": "#6B7280",
    "grid": "#D7DEE8",
    "text": "#172033",
}
```

## Style Setup

```python
from ieee_plot_style import IEEEFigureStyle, apply_ieee_style, figure_size

style = IEEEFigureStyle(width="two-column", font_size=8.5)
apply_ieee_style(style)
figsize = figure_size("two-column", aspect=0.58)
```

Use `width="one-column"` for compact single-axis plots. Use `width="two-column"` for multi-panel figures, dense legends, Pareto plots, and many methods.

## Export

```python
from ieee_plot_style import save_ieee_figure

save_ieee_figure(fig, "figures/main_result", formats=("svg", "pdf", "png", "tiff"))
```

Expected bundle:

```text
main_result.svg
main_result.pdf
main_result.png
main_result.tiff
```

## Plot Helpers

Use these helpers when the user asks for generated plotting code:

```python
plot_grouped_bars(ax, categories, series, labels, roles=None, ylabel=None, annotate=False)
plot_trend(ax, x, y_series, labels, roles=None, intervals=None, xlabel=None, ylabel=None, logy=False)
plot_pareto(ax, cost, score, labels, roles=None, size=None, xlabel=None, ylabel=None)
add_panel_label(ax, "a")
set_metric_axis(ax, xlabel="SNR (dB)", ylabel="BER (lower is better)")
```

Validation expectations:

- sequence lengths must match;
- bar charts usually start at zero;
- log axes must be explicitly labeled;
- color roles must match method roles;
- marker and line-style redundancy must remain after grayscale conversion.

## Generated-Code Contract

When returning plotting code, include:

```text
Files:
- plotting script
- source data file if created
- SVG/PDF/PNG/TIFF outputs if rendered

QA notes:
- final column width
- minimum text size
- legend position
- axis units
- color/marker redundancy
- missing uncertainty or source data placeholders
```

Do not generate decorative figures that weaken fair comparison or hide engineering cost.

