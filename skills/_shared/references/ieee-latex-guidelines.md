# IEEE LaTeX Guidelines

Use this reference for IEEEtran manuscripts, LaTeX debugging, and formatting checks.

## IEEEtran Basics

Prefer the official IEEEtran class required by the target venue. Do not mix unrelated templates.

Common patterns:

```latex
\documentclass[journal]{IEEEtran}
\documentclass[conference]{IEEEtran}
```

Use venue instructions over generic advice when there is a conflict.

## Figures and Tables

Use `figure` and `table` for single-column floats. Use `figure*` and `table*` only when a double-column object is needed.

Keep captions concise but informative. Place figure captions below figures and table captions above tables unless the venue specifies otherwise.

## Equations and Algorithms

Define notation before use. Avoid unexplained symbols in equations.

For algorithms, use a package compatible with the target template. If a venue forbids specific packages, follow the venue.

## Bibliography

Use IEEE style when required:

```latex
\bibliographystyle{IEEEtran}
\bibliography{refs}
```

Check that BibTeX entries include enough metadata: authors, title, venue, year, volume, issue, pages or article number, and DOI when available.

## Common Problems

1. Overfull hboxes from long equations, URLs, or table entries.
2. Figures too wide for the column.
3. Unresolved references from missing labels or compile order.
4. Duplicate labels.
5. Package conflicts with IEEEtran.
6. Nonstandard citation commands that break the bibliography style.

When fixing LaTeX, preserve the author's content and make the smallest format-correct change.
