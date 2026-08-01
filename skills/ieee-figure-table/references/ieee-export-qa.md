# IEEE Export and QA Reference

Use this before final figure delivery or when auditing whether a figure is submission-ready.

## Export Bundle

For generated or redrawn figures, prefer:

```text
source data: CSV/TSV/XLSX or clearly documented script variables
script: Python/R file or notebook that regenerates the figure
editable vector: SVG and/or PDF
preview raster: PNG
high-resolution raster when needed: TIFF, 300-600 dpi
caption draft:
QA notes:
```

For hybrid figures that are partially finished outside Python/R, also require:

```text
base exports: editable SVG/PDF generated from code
layout source: editable SVG/AI/PPTX/Figma/draw.io/Inkscape source
edit log: manual changes after code export
final export: PDF/SVG plus PNG/TIFF preview
```

## Column-Size QA

Check the figure at intended placement:

```text
one-column width: 3.5 in / 88.9 mm
two-column width: 7.16 in / 181.9 mm
axis/tick/legend text: about 7-8 pt or larger at final size
line width: visible after PDF compression
markers: distinguishable after grayscale conversion
legend: not hiding evidence
caption: enough to interpret the result without rereading the whole method
```

## Reviewer First-Impression QA

Flag as high risk when:

- text is unreadable at column size;
- plotted values are not tied to a dataset, metric, or condition;
- color is the only category encoding;
- axes omit units or use misleading truncation;
- uncertainty is absent for repeated experiments;
- baseline selection is unclear or unfair;
- table precision is inconsistent;
- figure and caption make stronger claims than the data supports.

## Reproducibility QA

For quantitative figures, record:

```text
data source:
preprocessing:
metric definition:
number of runs/seeds/folds:
center statistic:
spread/interval:
statistical test, if any:
baseline implementation:
code/script:
```

If any item is missing, expose it as a missing-information placeholder rather than inventing it.

For hybrid figures, also record which elements were manually edited and confirm that plotted values, axis limits, tick locations, uncertainty bands, and baseline labels were not manually altered.
