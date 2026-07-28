# Reviewer Response Example

Use this with `ieee-response` after receiving reviewer comments.

## Reviewer Comment

```text
The experimental comparison is insufficient. The manuscript does not compare with traditional methods, and it is unclear whether the proposed module is responsible for the reported improvement.
```

## Response Structure

```text
Response:
Thank you for pointing out the insufficient experimental comparison. We have revised the experimental section in three ways.

First, we added `[traditional baseline]` and `[recent baseline]` under the same `[dataset/split/preprocessing]` setting to make the comparison fair. The new results are reported in Table `[X]`.

Second, we added an ablation study by removing `[module]` and replacing it with `[simpler alternative]`. This isolates the contribution of `[module]`; the results are shown in Table `[Y]`.

Third, we revised Section `[Z]` to clarify the implementation setting, including `[hardware/software/parameters]`.

Manuscript changes:
- Section `[X]`, Paragraph `[Y]`: added baseline description.
- Table `[X]`: added baseline comparison.
- Table `[Y]`: added ablation study.
- Section `[Z]`: added implementation details.
```

## Check Before Sending

- Every reviewer concern has a direct action.
- Every new claim points to a manuscript location.
- Experiments are described as evidence, not as apology.
- Limitations are acknowledged only when they do not undermine the main contribution.

