# ALL-in-ALL ReSearching Workflow Skill

[![GitHub](https://img.shields.io/badge/Github-timesbye%2FALL--in--ALL\_ReSearching\_Workflow\_Skill-blue?logo=github)](https://github.com/timesbye/ALL-in-ALL_ReSearching_Workflow_Skill)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**从论文阅读到论文表达的一体式科研 workflow skill 集合。**

本项目整合前沿开源科研工具的设计理念，构建原创 brainstorm 能力，将论文阅读、文献综述、选题、绘图、写作、润色、审稿检查等分散环节串联为一个连续的、可追溯的工作流。

**GitHub 仓库**：[https://github.com/timesbye/ALL-in-ALL_ReSearching_Workflow_Skill](https://github.com/timesbye/ALL-in-ALL_ReSearching_Workflow_Skill)

## 项目定位

这个项目做的事情其实很简单——把散落在各处的好工具串到一起，补上缺失的关键环节，再让它们按正确顺序跑起来：

1. **引入已有的好工具**：论文阅读、文献综述、学术写作、科研绘图……这些领域已经有成熟的开源方案，我们直接引用它们的设计理念，不再重复造轮子
2. **补上缺失的关键环节**：现有的工具链里，最缺的就是一个能主动质疑、检索已有方案、收敛到可执行方向的 brainstorm 能力——这就是我们原创的 `critical-ideation` Skill
3. **让它们按正确顺序跑起来**：通过路由规则、项目模板和产物目录，把阅读 → 综述 → 选题 → 绘图 → 写作 → 润色 → 审稿检查串成一个顺序依赖的连续工作流

> **补充声明**：本项目的核心是 **Skill 整合概念**。各 Skill 均为 prompt 模块，后续会根据开源项目进展及前沿方向持续更新和替换，确保工作流始终与最新实践保持同步。

## 六类核心能力

| 能力 | 来源 | 用途 |
|------|------|------|
| 论文阅读 Skill | 参考 [917Dhj/DeepPaperNote](https://github.com/917Dhj/DeepPaperNote) | 深度阅读单篇论文、生成结构化研究笔记 |
| 文献综述 Skill | 参考 [CAICAIIs/Auto-Scholar](https://github.com/CAICAIIs/Auto-Scholar) (MIT) | 系统性文献综述、研究现状调研、gap 识别 |
| Critical Ideation Skill | **本项目原创** | brainstorm、主动质疑、竞品检索、方向重构、MVP 收敛 |
| 科研绘图 Skill | 参考 [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers) | 论文级 matplotlib 图、PDF/PNG 导出 |
| 引导式论文写作 Skill | 参考 [ShiyangZheng/scholarly](https://github.com/ShiyangZheng/scholarly) | 从零构建论文骨架、按章节引导写作 |
| 学术写作 Prompt 库 | 引用 [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | 润色、翻译、实验分析、reviewer 检查 |

## Workflow 链条

```text
paper-reading → literature-review → critical-ideation → scientific-figure-making → scholarly-writing + awesome-ai-research-writing → reviewer check
```

1. `paper-reading`：深度阅读关键论文，生成结构化笔记
2. `literature-review`：系统性综述领域现状，识别研究 gap
3. `critical-ideation`：先筛方向，不让项目在错误的 idea 上浪费时间
4. `scientific-figure-making`：把方向绑定到可见证据，而不是抽象口号
5. `scholarly-writing`：从零构建论文骨架，按章节引导写作
6. `awesome-ai-research-writing`：把草稿润色到论文级表达
7. `reviewer_check`：防止过度 claim，逼着结论回到证据边界内

## Repository Layout

```text
ALL-in-ALL_ReSearching_Workflow_Skill/
|-- README.md
|-- LICENSE
|-- ROUTER.md
|-- docs/
|   `-- USAGE.md
|-- prompt-libraries/
|   `-- awesome-ai-research-writing/   (引用入口，需单独 clone 上游仓库)
|-- skills/
|   |-- paper-reading/                 (参考 DeepPaperNote 编写的使用指南)
|   |   |-- SKILL.md
|   |   `-- templates/
|   |-- literature-review/             (参考 Auto-Scholar 编写的使用指南)
|   |   |-- SKILL.md
|   |   `-- templates/
|   |-- critical-ideation/             (本项目原创)
|   |   |-- SKILL.md
|   |   |-- templates/
|   |   `-- examples/
|   |-- scientific-figure-making/      (参考 figures4papers 编写的使用指南)
|   |   |-- SKILL.md
|   |   `-- references/
|   `-- scholarly-writing/             (参考 Scholarly 编写的使用指南)
|       |-- SKILL.md
|       `-- templates/
|-- prompts/
|-- templates/
|   `-- project_ai/
|-- examples/
|   `-- GeoAgent-Thesis/
`-- scripts/
```

## Quick Start

1. 复制模板到你的科研项目目录。
2. 通过 `scripts/link_to_project.ps1` 或 `scripts/link_to_project.sh` 把本仓库链接到目标项目的 `.ai/toolkit/`。
3. 在 Trae / Codex 中先读取：

```text
.ai/PROJECT_RULES.md
.ai/toolkit/ROUTER.md
```

4. 若使用 Codex 全局 skill，可执行：

```powershell
.\scripts\install_to_codex.ps1
```

## Typical Workflows

- 仅论文阅读：使用 `skills/paper-reading/`
- 仅文献综述：使用 `skills/literature-review/`
- 仅 ideation / 选题：使用 `skills/critical-ideation/`
- 仅绘图：使用 `skills/scientific-figure-making/`
- 仅论文写作：使用 `skills/scholarly-writing/`
- 仅润色/翻译：使用 `prompt-libraries/awesome-ai-research-writing/`
- 完整流程：阅读 → 综述 → 选题 → 绘图 → 写作 → 润色 → reviewer 检查

详见 [ROUTER.md](https://github.com/timesbye/ALL-in-ALL_ReSearching_Workflow_Skill/blob/main/ROUTER.md)。

## Example Project

仓库内置了示例项目，展示完整 workflow：

- [`examples/GeoAgent-Thesis/WORKFLOW_SHOWCASE.md`](https://github.com/timesbye/ALL-in-ALL_ReSearching_Workflow_Skill/blob/main/examples/GeoAgent-Thesis/WORKFLOW_SHOWCASE.md)

## Third-Party Acknowledgments

| 项目 | 作者 | 用途 | 许可证 |
|------|------|------|--------|
| [DeepPaperNote](https://github.com/917Dhj/DeepPaperNote) | [917Dhj](https://github.com/917Dhj) | 论文阅读 Skill 设计参考 | 未声明 |
| [Auto-Scholar](https://github.com/CAICAIIs/Auto-Scholar) | [CAICAIIs](https://github.com/CAICAIIs) | 文献综述 Skill 设计参考 | MIT |
| [Scholarly](https://github.com/ShiyangZheng/scholarly) | [ShiyangZheng](https://github.com/ShiyangZheng) | 引导式写作 Skill 设计参考 | 未声明 |
| [awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | [Leey21](https://github.com/Leey21) | 学术写作 Prompt 库 | 未声明 |
| [figures4papers](https://github.com/ChenLiu-1996/figures4papers) | [Chen Liu](https://chenliu-1996.github.io/) (Yale) | 科研绘图范式参考 | 未声明 |

- 本项目**不复制分发**上述仓库的原始内容
- 各 Skill 目录为本项目基于上游理念编写的使用指南
- `skills/critical-ideation/` 为本项目原创内容

详见 [LICENSE](LICENSE) 中的 Third-Party Acknowledgments 部分。

## License

本项目原创内容采用 [MIT License](LICENSE) 授权。

上游项目的原始内容归各自作者所有，适用其各自的使用条款。
