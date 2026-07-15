# Captions and QA Notes

## Robustness SNR Curve

Caption draft: Bit error rate under decreasing SNR. The proposed method shows lower BER than MMSE, CNN, and Transformer baselines across all tested channel conditions, supporting the robustness claim under low-SNR operation.

QA: The x-axis is an engineering operating condition, the y-axis uses a labeled log scale, and marker/line-style redundancy supports grayscale readability.

## Accuracy-Latency Pareto

Caption draft: Accuracy-latency tradeoff for deployment-oriented comparison. The proposed method lies on the Pareto frontier by improving F1 while keeping inference latency lower than larger neural baselines.

QA: The figure makes the cost metric visible, labels both optimization directions, and avoids claiming accuracy improvement without deployment cost.

## Ablation Result Table

Caption draft: Ablation study of the proposed model components. Removing attention, temporal modeling, physics guidance, or augmentation reduces accuracy and F1, indicating that each component contributes to the final model.

QA: The table keeps performance and deployability metrics together. Real manuscripts should add repeat definitions, variability, and significance testing where appropriate.
