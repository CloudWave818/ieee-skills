# ieee-skills

Codex skills for IEEE-style conference, journal, Transactions, Letters, and engineering manuscript workflows.

This project helps with IEEE-style academic writing, polishing, reviewer-style assessment, experimental validation, figure/table quality, revision responses, LaTeX formatting, citation checking, and paper reading. It is an unofficial IEEE-style skill collection, not an IEEE project.

## Skills

| Skill | Purpose |
|---|---|
| `ieee-writing` | Draft and restructure IEEE-style titles, abstracts, introductions, related work, methods, experiments, conclusions, and contribution statements |
| `ieee-polishing` | Polish or translate technical prose into precise IEEE-style English |
| `ieee-reviewer` | Simulate IEEE-style technical review across scope, novelty, validity, data, clarity, compliance, and advancement |
| `ieee-experiment` | Audit claim-evidence alignment, baselines, ablations, robustness, complexity, and reproducibility |
| `ieee-figure-table` | Audit figures, tables, captions, two-column readability, accessibility, and first-impression risks |
| `ieee-response` | Draft point-by-point responses, rebuttals, revision plans, and cover letters |
| `ieee-latex` | Fix IEEEtran LaTeX, floats, equations, tables, algorithms, BibTeX, and PDF checks |
| `ieee-citation` | Check BibTeX, reference metadata, DOI fields, IEEE style, and citation logic |
| `ieee-paper-reader` | Extract contributions, methods, equations, experiments, limitations, reproducibility details, and citation positioning |

## Repository Layout

```text
ieee-skills/
  skills/
    _shared/
      references/
    ieee-writing/
      SKILL.md
      manifest.yaml
      static/
      agents/
    ieee-polishing/
    ieee-reviewer/
    ieee-experiment/
    ieee-figure-table/
    ieee-response/
    ieee-latex/
    ieee-citation/
    ieee-paper-reader/
  scripts/
    update-codex-skills.ps1
    update-codex-skills.sh
```

Each `ieee-*` directory under `skills/` is an installable Codex skill. The `skills/_shared/` directory contains shared references and must be installed with the skills.

Do not copy only `SKILL.md`. Many skills depend on `manifest.yaml`, `static/`, `agents/`, and `_shared/references/`.

## Installation

Clone the repository:

```bash
git clone https://github.com/CloudWave818/ieee-skills.git
cd ieee-skills
```

Windows PowerShell:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\update-codex-skills.ps1
```

macOS / Linux / Git Bash:

```bash
bash scripts/update-codex-skills.sh
```

The default destination is:

```text
~/.codex/skills
```

Custom destination:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\update-codex-skills.ps1 -Dest "D:\codex-skills"
```

```bash
bash scripts/update-codex-skills.sh --dest "$HOME/.codex/skills"
```

Pull updates before installing:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\update-codex-skills.ps1 -Pull
```

```bash
bash scripts/update-codex-skills.sh --pull
```

Check local skill structure:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\update-codex-skills.ps1 -Check
```

```bash
bash scripts/update-codex-skills.sh --check
```

## Example Prompts

```text
Use $ieee-writing to draft an IEEE-style introduction from my problem statement and contributions.
```

```text
Use $ieee-polishing to polish this abstract into concise IEEE-style technical English.
```

```text
Use $ieee-reviewer to evaluate this manuscript like an IEEE Transactions reviewer.
```

```text
Use $ieee-experiment to check whether my experiments prove the claims in my abstract.
```

```text
Use $ieee-figure-table to audit my figures and result tables before submission.
```

```text
Use $ieee-response to draft point-by-point responses to these reviewer comments.
```

## Design Principle

IEEE-style papers should build a verifiable engineering evidence chain:

```text
object -> condition/constraint -> engineering harm -> prior limitation -> method rationale -> experimental evidence
```

These skills emphasize technical specificity, fair comparison, reproducibility, professional visual evidence, and disciplined reviewer response.

## Disclaimer

This project is unofficial and is not affiliated with, endorsed by, or sponsored by IEEE.

IEEE is a trademark of The Institute of Electrical and Electronics Engineers, Inc. This project only provides unofficial IEEE-style writing, review, and formatting assistance for research manuscripts.

Users must check the latest requirements of their target IEEE journal, conference, Transactions, Letters, or Magazine.

## License

MIT License. See [LICENSE](LICENSE).
