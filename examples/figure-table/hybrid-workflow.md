# Hybrid Figure Workflow Example

Use this template when an IEEE figure is not made end-to-end in Python/R.

Typical cases:

- mechanism schematic;
- system architecture;
- experimental pipeline;
- multi-source composite figure;
- quantitative panels plus manual arrows, labels, photos, or callouts.

## Figure Contract

Core claim:
The proposed system improves robustness under low-SNR operation while remaining deployable.

Target placement:
Two-column `figure*`.

Evidence map:

| Panel | Source | Role |
|---|---|---|
| A. System pipeline | editable vector layout | explains signal flow and proposed module placement |
| B. BER-SNR curve | `scripts/make_panel_b.py` + `data/ber_snr.csv` | supports robustness claim |
| C. Latency/params table | `data/deployability.csv` | keeps engineering cost visible |
| D. Failure examples | curated image crops with source paths | explains remaining limitations |

## Required File Bundle

```text
data/
  ber_snr.csv
  deployability.csv
scripts/
  make_panel_b.py
base_exports/
  panel_b_ber_snr.svg
  panel_c_deployability.svg
layout/
  figure_3_hybrid.editable.svg
exports/
  figure_3.pdf
  figure_3.svg
  figure_3.png
  figure_3.tiff
figure_edit_log.md
caption.md
qa_notes.md
```

## Edit Log

```markdown
# Figure Edit Log

Figure: Fig. 3, system robustness and deployability evidence
Target placement: two-column figure*

Data-generated panels:
- Panel B was generated from `data/ber_snr.csv` using `scripts/make_panel_b.py`.
- Panel C was generated from `data/deployability.csv`.

Manual layout edits:
- Assembled panels A-D into one two-column layout.
- Moved legend into a dedicated side area.
- Added arrows connecting the system module in Panel A to robustness evidence in Panel B.
- Added panel labels and aligned all panels to a shared margin grid.

No manual changes were made to:
- plotted values;
- axis limits or tick positions;
- baseline names;
- uncertainty bands;
- numeric table values.

Final QA:
- Text remains readable at 7.16 in width.
- Baselines are visible in color and grayscale.
- The caption states condition, metric, and takeaway.
- Source data and base plot scripts are available.
```

## Caption Draft

Fig. 3. Hybrid evidence figure for robustness and deployability. Panel A shows the proposed system pipeline and where the new module enters the signal path. Panel B reports BER under SNR stress conditions, where lower values are better. Panel C summarizes deployment cost using latency and parameter count. Panel D lists representative failure modes for low-SNR edge cases. Quantitative panels are generated from source data; layout annotations are recorded in the edit log.

## Reviewer-Risk Notes

- Do not manually move data points after exporting Panel B.
- Do not crop axes in a way that changes the apparent performance gap.
- Do not let schematic arrows imply a causal claim that is not validated by Panels B-D.
- If Panel D uses screenshots or photos, record the source and selection rule.
