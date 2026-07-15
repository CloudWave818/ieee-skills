# Backend: R

Use R for ggplot2, patchwork, ComplexHeatmap, svglite, cairo_pdf, and ragg-based IEEE figure generation, redraws, and exports.

Execution rule: when R is selected, use R for all plotting, preview rendering, export, and visual QA. Do not switch to Python for a substitute render.

Quick-start style:

```r
library(ggplot2)

theme_ieee <- function(base_size = 8, base_family = "Arial") {
  theme_classic(base_size = base_size, base_family = base_family) +
    theme(
      legend.title = element_blank(),
      legend.key = element_blank(),
      axis.line = element_line(linewidth = 0.35),
      axis.ticks = element_line(linewidth = 0.35),
      plot.title = element_text(face = "bold"),
      strip.background = element_blank()
    )
}

save_ieee_figure <- function(plot, stem, width = 3.5, height = 2.4, dpi = 600) {
  svglite::svglite(paste0(stem, ".svg"), width = width, height = height)
  print(plot)
  dev.off()
  grDevices::cairo_pdf(paste0(stem, ".pdf"), width = width, height = height, family = "Arial")
  print(plot)
  dev.off()
  ragg::agg_png(paste0(stem, ".png"), width = width, height = height, units = "in", res = 300)
  print(plot)
  dev.off()
  ragg::agg_tiff(paste0(stem, ".tiff"), width = width, height = height, units = "in", res = dpi)
  print(plot)
  dev.off()
}
```

Prefer shape, linetype, and direct labels when color alone would fail in grayscale or compressed PDFs.

Read `references/ieee-chart-patterns.md` when selecting chart recipes. Read `references/ieee-export-qa.md` before final delivery.
