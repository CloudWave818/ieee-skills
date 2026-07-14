# IEEE Experiment Checklist

Use this reference when designing, auditing, or rewriting experiments.

## Baseline Requirements

Include:

1. Traditional or classical baselines when the field expects them.
2. Recent strong baselines or state-of-the-art methods.
3. Same train/test split and preprocessing when possible.
4. Comparable hyperparameter tuning budget.
5. Clear hardware and software environment for runtime claims.

If the paper claims superiority over traditional methods, include at least one credible traditional method unless the field makes it irrelevant.

## Ablation Studies

Each claimed module should have an ablation:

1. Remove the module.
2. Replace it with a simpler alternative.
3. Vary key hyperparameters when the mechanism depends on them.
4. Report metrics that match the claimed benefit.

Do not add ablations for modules that are not claimed as contributions unless they clarify behavior.

## Condition-Specific Validation

If the title, abstract, or introduction names a condition, experiments must test that condition.

Examples:

1. Variable speed or load: test across speeds or loads.
2. Noisy signals: test multiple SNR levels.
3. Domain shift: cross-domain or cross-device testing.
4. Real-time or lightweight: runtime, memory, FLOPs, or parameter count.
5. Imbalanced data: class-wise metrics and imbalance settings.

## Metrics

Choose metrics that match the task:

1. Classification: accuracy, F1, precision, recall, confusion matrix.
2. Detection: mAP, precision-recall, latency.
3. Regression: MAE, RMSE, R2, error distribution.
4. Signal processing: SNR, MSE, spectral distortion, reconstruction quality.
5. Systems: throughput, latency, energy, memory, reliability.

## Reporting

Report means and variance when randomness matters. Use consistent decimal precision. Mark best and second-best results clearly. Explain why improvements matter in engineering terms, not only statistical terms.
