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

Caption draft: Multimodal deep reinforcement learning framework for an IEEE-style engineering system. Panel (a) shows state traces, topology graphs, and engineering constraints encoded by temporal, graph, and constraint branches before multimodal attention and actor-critic output. Panel (b) details graph construction. Panel (c) links operating conditions to low-cost and high-risk decisions. Panel (d) shows pretraining and transfer learning for downstream control tasks.

QA: The diagram states the system boundary, multimodal inputs, encoder roles, fusion path, decision head, graph construction, operating-condition evidence, and transfer-learning path. It is suitable for hybrid vector finishing because quantitative panels or real testbed photos can be added without changing the core evidence map.
