# Captions and QA Notes

## Robustness SNR Curve

Caption draft: Bit error rate under decreasing SNR. The proposed method shows lower BER than MMSE, CNN, and Transformer baselines across all tested channel conditions, supporting the robustness claim under low-SNR operation.

QA: The figure uses a dedicated evidence panel, a visible stress-condition band, log-scale labeling, and marker/line-style redundancy. The legend is outside the data area.

## Accuracy-Latency Pareto

Caption draft: Accuracy-latency tradeoff for deployment-oriented comparison. The proposed method lies on the Pareto frontier by improving macro-F1 while keeping inference latency lower than larger neural baselines.

QA: The figure shows accuracy, latency, and parameter cost in one claim-facing view. Labels are short, the role encoding is separated from the scatter area, and deployment cost is not hidden in text.

## Ablation Result Table

Caption draft: Ablation study of the proposed model components. Adding attention, temporal modeling, physics guidance, and augmentation improves accuracy and F1, while the table keeps parameter count and latency visible.

QA: The table uses consistent precision, highlights only the full-model/best metrics, keeps cost metrics visible, and states missing real-manuscript requirements such as variance, seeds, and significance testing.

## DRL Framework Diagram

Caption draft: Deep reinforcement learning control framework for an IEEE-style engineering system. The environment exposes state, reward/cost, and constraints; the DRL agent encodes state, uses actor-critic networks to generate actions, and updates from replayed transition tuples before deployment in a closed loop.

QA: The diagram states the system boundary, state-action-reward path, training loop, deployment action, and reviewer-risk placeholders. It is suitable for hybrid vector finishing because quantitative panels or real testbed photos can be added without changing the core evidence map.
