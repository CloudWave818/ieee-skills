# Abstract Polishing Example

Use this with `ieee-polishing` or `ieee-writing`.

## Before

```text
This paper proposes a new deep learning method for fault diagnosis. The method has good feature extraction ability and achieves better results than other methods. Experiments show that the proposed method is effective.
```

## Problems

| Problem | Reviewer Risk |
|---|---|
| No object | The reader does not know the target system or task. |
| No condition | The advantage is not tied to a difficult IEEE-style operating scenario. |
| Vague method | "Deep learning method" does not identify the technical mechanism. |
| Unsupported claim | "Better" and "effective" need dataset, metric, and comparison context. |

## After

```text
This paper studies `[object/task]` under `[operating condition]`, where `[engineering harm]` reduces the reliability of existing `[method family]` approaches. To address this problem, we propose `[method name]`, which combines `[mechanism 1]` with `[mechanism 2]` to `[technical purpose]`. Experiments on `[dataset/platform]` compare the proposed method with `[traditional baseline]` and `[recent baseline]` using `[metrics]`. The results show `[bounded quantitative finding]`, indicating that the proposed design improves `[claim]` under `[condition]`.
```

## IEEE Style Notes

- Keep the condition visible when the condition is the reason the method matters.
- Replace broad praise with bounded evidence.
- Do not invent numbers, datasets, or baselines during polishing.

