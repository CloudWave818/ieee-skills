# Review Comment Audit

Use this when the user asks whether reviewer comments are fair, specific, generic, careless, contradictory, or possibly AI-generated.

Audit observable quality, not reviewer identity or AI authorship.

Check each comment for:

1. manuscript-specific anchor: section, figure, table, equation, dataset, baseline, or claim;
2. technical correctness relative to the supplied manuscript;
3. internal consistency with other reviewer comments;
4. feasibility and scope fit of requested experiments;
5. hallucinated details: nonexistent method, dataset, metric, citation, figure, result, or page;
6. template-like wording that gives no actionable target;
7. whether a manuscript clarification would neutralize the risk.

Output:

```text
Reviewer-comment quality audit
Comment | Observable issue | Manuscript evidence | Response strategy | Editor-escalation risk
```

Use labels:

- `Substantive`: technically grounded and should be addressed.
- `Underspecified`: possibly valid but lacks actionable detail.
- `Contradicted`: conflicts with supplied manuscript evidence.
- `Out-of-scope`: asks for work beyond the paper's stated scope or venue expectations.
- `Possibly careless/generic`: template-like or non-specific; do not label as AI-generated without evidence.
