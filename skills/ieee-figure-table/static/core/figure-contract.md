# IEEE Figure Contract

For plotting, redrawing, or major redesign tasks, establish this contract before writing code or proposing layout polish.

1. **Core engineering claim**: one sentence the figure/table must defend.
2. **Evidence map**: each panel, curve, row, or column must support a unique part of the claim.
3. **Comparison contract**: list baseline methods, proposed method variants, operating conditions, datasets, metrics, and whether higher/lower is better.
4. **IEEE layout contract**: decide one-column, two-column, page-wide, or supplementary use before choosing font size, line width, legend position, and aspect ratio.
5. **Export contract**: specify source data, editable SVG/PDF, high-DPI PNG/TIFF preview, and the script/notebook needed to regenerate the figure.

If the user provides only a vague request such as "make this figure better", first infer a provisional contract and mark missing items explicitly.

Default IEEE dimensions:

```text
one-column: 3.5 in / 88.9 mm wide
two-column: 7.16 in / 181.9 mm wide
minimum final text: about 7-8 pt for axis/tick/legend text
line art: vector preferred
raster preview: 300-600 dpi depending on target use
```

Never sacrifice fair comparison or uncertainty reporting to make a figure look cleaner.
