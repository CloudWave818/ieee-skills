# IEEE Visual Style Reference

Use this reference when a figure is technically correct but does not yet look like a polished, reviewer-ready IEEE manuscript figure.

This style borrows the useful idea of a stable publication house style from high-quality matplotlib figure repositories, but adapts it for IEEE evidence: the figure must look clean and must still prove the engineering claim after one-column or two-column scaling.

## Design Target

An IEEE figure should read as:

```text
minimal background + strong evidence hierarchy + semantic color + print-safe redundancy + reproducible export
```

Do not optimize beauty by hiding uncertainty, baselines, negative results, axis units, or cost metrics.

## Typography

- Use a portable sans-serif stack: Arial, Helvetica, DejaVu Sans, sans-serif.
- Preserve editable vector text: `svg.fonttype = "none"` and `pdf.fonttype = 42`.
- Use final-size text, not screen-size text:
  - one-column figure: base font 7.5-8.5 pt;
  - two-column figure: base font 8-10 pt;
  - poster or slide export: larger is acceptable, but do not reuse slide font sizes in a manuscript figure.
- Use bold sparingly for panel labels, proposed method labels, and table-best values.

## Line, Marker, and Axis System

- Remove top and right spines unless a boxed axis is needed for a matrix or image.
- Use visible but restrained axes: about 0.8-1.1 pt at manuscript size.
- Pair color with marker and line style:
  - proposed: solid line + circle or star;
  - recent neural baseline: dashed line + square;
  - traditional baseline: dotted or dash-dot line + triangle;
  - reference or oracle: thin neutral line.
- Use black or dark gray bar edges when bars may be printed in grayscale.
- Use hatching for ablation groups or method families when color alone would fail.

## Semantic Palette

Use color roles consistently across figures:

| Role | Color | Use |
|---|---|---|
| proposed | `#0B5CAD` | main method, main claim |
| proposed-light | `#8EC3F5` | uncertainty band or related variant |
| recent-baseline | `#0F766E` | strong recent baseline |
| traditional-baseline | `#B64040` | classical or contrast baseline |
| cost | `#B7791F` | latency, energy, FLOPs, memory, resource tradeoff |
| neutral | `#6B7280` | reference, background, non-highlight curves |
| grid | `#D7DEE8` | subtle grid lines |
| text | `#172033` | labels and axes |

Avoid one-note palettes and rainbow category maps. Use highlight color once, not on every important thing.

## Layout Patterns

- Decide final placement first: one-column, two-column, page-wide, or supplement.
- Prefer two-column width for:
  - more than four methods;
  - more than two panels;
  - a shared legend;
  - long method names;
  - accuracy-cost Pareto or multi-metric comparisons.
- Use one panel for one evidence role. Do not make every panel repeat the same superiority claim.
- Put dense legends outside the data region or in a dedicated legend axis.
- Align axes across panels when comparing the same metric or condition.
- Add panel labels `(a)`, `(b)`, `(c)` only when the manuscript will cite panels.

## Table Visual Style

- Use units in column headers.
- Keep decimal precision consistent within each metric.
- Group rows by method family or condition.
- Use subtle row banding only when it improves scanning.
- Bold best and underline or mark second-best only if the comparison is fair.
- Keep deployment metrics visible when the claim mentions lightweight, real-time, efficient, low-power, or low-complexity behavior.

## Caption Style

Caption should answer:

```text
what is compared;
under which dataset/testbed/condition;
which metric and direction;
what the main takeaway is;
what uncertainty or repeat definition is used when relevant.
```

Avoid captions that only restate the axis labels.

## Final Polish Checklist

- The proposed method is identifiable without relying only on color.
- Baselines are visually present, not de-emphasized into unreadability.
- The figure still reads at IEEE column size.
- The visual hierarchy makes the main evidence obvious within a few seconds.
- The source data and script can regenerate the figure.
- SVG/PDF/PNG/TIFF outputs are exported from the same script.

