# IEEE LaTeX Diagnosis Example

Use this with `ieee-latex` when IEEEtran formatting blocks submission.

## Input

```text
Problem: Table is too wide for one IEEE column and causes overfull hbox warnings.
Object: comparison table
Venue: IEEE conference
Stage: pre-submission
```

## Diagnosis

- Cause: the table contains too many metric columns for a one-column `table` float.
- Affected object: result comparison table.
- Review risk: the PDF may look careless even if the numbers are correct.

## Minimal Fix

```latex
\begin{table*}[t]
\caption{Comparison under [condition] on [dataset].}
\label{tab:main-comparison}
\centering
\footnotesize
\setlength{\tabcolsep}{3.5pt}
\begin{tabular}{lcccccc}
\hline
Method & Metric 1 & Metric 2 & Metric 3 & Params & FLOPs & Latency \\
\hline
...
\hline
\end{tabular}
\end{table*}
```

## Follow-Up Checks

1. Recompile with the same IEEEtran class options required by the venue.
2. Check whether the table appears near its first citation.
3. Confirm that font size remains readable in the final PDF.
4. Confirm that citations, labels, and references resolve after a full LaTeX/BibTeX compile sequence.

