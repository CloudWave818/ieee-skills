---
name: ieee-citation
description: Check, clean, verify, and improve IEEE citations, references, BibTeX entries, citation positioning, related-work logic, DOI metadata, venue names, and reference formatting using routed citation and metadata guidance. Use when preparing IEEE manuscripts, fixing bibliography errors, verifying reference completeness, improving related work, checking whether citations support claims, or identifying missing classic/recent baselines.
---

# IEEE Citation Router

Use this skill to make citations accurate, IEEE-compliant, and rhetorically useful.

Do not invent references, DOI values, page numbers, venues, or metadata. Follow the routing protocol and load the selected fragments.

## Routing Protocol

1. Read `manifest.yaml`.
2. Read every file listed under `always_load`.
3. Detect the axes:
   - `task_type`: bibtex-cleanup / metadata-check / citation-logic / related-work-gap / format-conversion / reference-audit.
   - `source_type`: journal-article / conference-paper / book / standard / dataset-code / preprint / web-source / unknown.
   - `citation_role`: background / method-family / baseline / closest-prior-work / dataset / tool / claim-support.
   - `failure_mode`: missing-metadata / invented-or-unverified / weak-positioning / missing-classic-work / missing-recent-work / format-error / citation-does-not-support-claim.
   - `verification_level`: no-web / web-verify / authoritative-only.
4. State the detected axes when useful.
5. Load only the matching fragments.
6. Separate formatting fixes from factual verification.
7. Flag any metadata that cannot be verified.

## Output Contract

For reference audits:

```text
Detected axes: task_type=..., source_type=..., citation_role=..., failure_mode=..., verification_level=...

Reference audit
Item | Issue | Risk | Fix | Verification status
```

For related-work citation logic:

```text
Claim or sentence | Current citation role | Problem | Better citation need
```

For BibTeX cleanup, return corrected BibTeX only when metadata is supplied or verified. Use placeholders for missing fields.

## Red Lines

Do not fabricate references or metadata.

Do not treat 20-30 references as a universal rule.

Do not claim a citation supports a sentence unless the supplied or verified information supports that relationship.
