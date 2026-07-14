# ieee-skills

面向 IEEE 会议、期刊、Transactions、Letters 和工程技术论文工作流的 Codex skills 集合。

本项目用于辅助 IEEE 风格论文的写作、润色、预审、实验设计、图表检查、审稿回复、LaTeX 排版、引用核验和论文阅读。它不是 IEEE 官方项目，而是一套非官方的 IEEE-style academic writing and review skills。

## 适用场景

- 写 IEEE 论文标题、摘要、引言、Related Work、方法、实验和结论。
- 把中文草稿或中式英文改成更清晰的 IEEE 风格英文。
- 从审稿人角度检查 novelty、validity、data、clarity、compliance 和 advancement。
- 检查实验是否支撑论文 claim，包括 baseline、ablation、robustness、complexity 和 reproducibility。
- 检查图表是否清晰、规范、适合 IEEE 双栏缩放。
- 写 rebuttal、major revision、minor revision、cover letter 和 point-by-point response。
- 处理 IEEEtran LaTeX、BibTeX、参考文献、引用逻辑和论文阅读笔记。

## 技能索引

| Skill | 用途 |
|---|---|
| `ieee-writing` | 起草和重构 IEEE 论文标题、摘要、引言、Related Work、方法、实验、结论和贡献点 |
| `ieee-polishing` | IEEE 风格英文润色、中文转英文、逻辑重构、空泛表达修复 |
| `ieee-reviewer` | 模拟 IEEE 审稿人，检查 scope、novelty、validity、data、clarity、compliance、advancement |
| `ieee-experiment` | 设计和审查实验，构建 claim-evidence matrix，检查 baseline、ablation、robustness、complexity |
| `ieee-figure-table` | 检查图表、caption、双栏可读性、灰度可读性、表格精度和第一印象风险 |
| `ieee-response` | 生成审稿回复、revision plan、cover letter、point-by-point response |
| `ieee-latex` | 处理 IEEEtran、编译错误、浮动体、公式、表格、算法、BibTeX 和 PDF 检查 |
| `ieee-citation` | 检查 BibTeX、参考文献元数据、DOI、IEEE 格式、Related Work 引用逻辑 |
| `ieee-paper-reader` | 阅读 IEEE 论文，提取贡献、方法、公式、实验、局限、可复现信息和引用定位 |

## 目录结构

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

`skills/` 下每个 `ieee-*` 目录都是一个可安装的 Codex skill。`skills/_shared/` 是共享规则目录，不能省略。

不要只复制 `SKILL.md`。很多 skill 依赖 `manifest.yaml`、`static/`、`agents/` 和 `_shared/references/`。

## 安装

先克隆仓库：

```bash
git clone https://github.com/CloudWave818/ieee-skills.git
cd ieee-skills
```

Windows PowerShell：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\update-codex-skills.ps1
```

macOS / Linux / Git Bash：

```bash
bash scripts/update-codex-skills.sh
```

默认安装到：

```text
~/.codex/skills
```

如果希望安装到其他位置：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\update-codex-skills.ps1 -Dest "D:\codex-skills"
```

```bash
bash scripts/update-codex-skills.sh --dest "$HOME/.codex/skills"
```

如果仓库是用 git clone 得到的，可以顺便拉取更新：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\update-codex-skills.ps1 -Pull
```

```bash
bash scripts/update-codex-skills.sh --pull
```

只检查本地 skill 结构：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\update-codex-skills.ps1 -Check
```

```bash
bash scripts/update-codex-skills.sh --check
```

## 典型用法

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

## 设计原则

IEEE 论文的核心不是宽泛叙事，而是可验证的工程证据链：

```text
对象 -> 工况/约束 -> 工程危害 -> 现有方法局限 -> 方法依据 -> 实验证据
```

本项目强调：

- 题目和摘要中的对象、方法、工况。
- 引言中的工程必要性，而不是只说“研究较少”。
- 方法选择与系统特点之间的因果关系。
- 实验与论文 claim 的一一对应。
- 传统方法、强 baseline、ablation、robustness、complexity 和 reproducibility。
- 图表的专业第一印象和 IEEE 双栏可读性。
- 审稿回复中的具体修改、证据和克制表达。

## 免责声明

This project is unofficial and is not affiliated with, endorsed by, or sponsored by IEEE.

IEEE is a trademark of The Institute of Electrical and Electronics Engineers, Inc. This project only provides unofficial IEEE-style writing, review, and formatting assistance for research manuscripts.

用户应自行核对目标期刊、会议、Transactions、Letters 或 Magazine 的最新投稿指南和模板要求。

## License

MIT License. See [LICENSE](LICENSE).
