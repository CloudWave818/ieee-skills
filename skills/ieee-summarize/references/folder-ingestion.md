# Folder Ingestion

Use this reference when the user provides a folder of research materials.

## File Categories

Classify files before summarizing:

1. `notes`: Markdown, text, doc exports, AI chat exports, idea logs.
2. `code`: Python, MATLAB, C/C++, Java, notebooks, configs, scripts.
3. `experiments`: CSV, logs, result tables, metric dumps, training output, screenshots with captions.
4. `literature`: BibTeX, RIS, Zotero exports, paper summaries, copied introductions, related-work notes.
5. `figures_tables`: SVG, PDF, PNG, PPTX, table drafts, plotting scripts.
6. `unknown`: binaries, large generated artifacts, ambiguous files.

## Reading Strategy

1. Start with inventory, README files, filenames, headings, recent notes, and result summaries.
2. For code, extract method names, model classes, pipeline functions, config keys, datasets, metrics, and output filenames. Do not infer behavior from filenames alone.
3. For AI chat exports, extract decision history, rejected ideas, open questions, and candidate claims. Label as ideation unless independently supported.
4. For literature summaries, group papers by method family, problem setting, baseline role, dataset, and limitation. Select closest-prior-work candidates by relevance, not by citation count alone.
5. For copied introduction excerpts, extract reusable argument moves:
   - application importance,
   - operating condition,
   - limitation of current methods,
   - why the proposed direction matters.
   Do not paraphrase into manuscript text without citation verification.
6. For experiment logs, preserve failed runs, parameter changes, negative results, and missing seeds because they often explain reviewer risks.

## Source Discipline

Use source tags such as:

```text
[source: notes/2026-07-idea.md#heading]
[source: src/model.py:class DRLAgent]
[source: results/run_042.csv]
[source: literature/zotero-summary.md:paper-key]
```

If exact line numbers are not available, use path plus heading or filename.

## Stop Conditions

Stop and report limits when:

1. the folder is too large to inspect fully in one pass,
2. core files are binary or inaccessible,
3. the notes contradict the code or logs,
4. literature summaries lack citation metadata,
5. claimed results have no source table, log, or figure.
