# Backend: Python

Use Python for matplotlib/seaborn-based IEEE figure generation, redraws, and exports.

Execution rule: when Python is selected, use Python for all plotting, preview rendering, export, and visual QA. Do not switch to R for a substitute render.

Quick-start style:

```python
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "font.size": 8,
    "axes.linewidth": 0.8,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "legend.frameon": False,
    "xtick.direction": "out",
    "ytick.direction": "out",
})

IEEE_COL_IN = 3.5
IEEE_TWO_COL_IN = 7.16

def save_ieee_figure(fig, stem, dpi=600):
    fig.savefig(f"{stem}.svg", bbox_inches="tight")
    fig.savefig(f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(f"{stem}.png", dpi=300, bbox_inches="tight")
    fig.savefig(f"{stem}.tiff", dpi=dpi, bbox_inches="tight")
```

Prefer marker + line-style redundancy for grayscale safety. Use color only when it adds meaning.

Read `references/ieee-chart-patterns.md` when selecting chart recipes. Read `references/ieee-export-qa.md` before final delivery.
