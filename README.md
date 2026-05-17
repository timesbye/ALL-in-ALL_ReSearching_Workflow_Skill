# ALL-in-ALL ReSearching Workflow Skill

[![GitHub](https://img.shields.io/badge/Github-timesbye%2FALL--in--ALL\_ReSearching\_Workflow\_Skill-blue?logo=github)](https://github.com/timesbye/ALL-in-ALL_ReSearching_Workflow_Skill)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**从论文阅读到论文表达的一体式科研 workflow skill 集合。**

本项目整合前沿开源科研工具的设计理念，构建原创 brainstorm 能力，将文献综述、论文阅读、选题、实验设计、绘图、写作、润色、审稿检查等分散环节串联为一个连续的、可追溯的工作流。

**GitHub 仓库**：[https://github.com/timesbye/ALL-in-ALL_ReSearching_Workflow_Skill](https://github.com/timesbye/ALL-in-ALL_ReSearching_Workflow_Skill)

## 项目定位

这个项目做的事情其实很简单——把散落在各处的好工具串到一起，补上缺失的关键环节，再让它们按正确顺序跑起来：

1. **引入已有的好工具**：文献综述、论文阅读、学术写作、科研绘图、实验设计……这些领域已经有成熟的开源方案，我们直接引用它们的设计理念，不再重复造轮子
2. **补上缺失的关键环节**：现有的工具链里，最缺的就是一个能主动质疑、检索已有方案、收敛到可执行方向的 brainstorm 能力——这就是我们原创的 `critical-ideation` Skill
3. **让它们按正确顺序跑起来**：通过路由规则、项目模板和产物目录，把综述 → 阅读 → 选题 → 实验设计 → 绘图 → 写作 → 润色 → 审稿检查串成一个顺序依赖的连续工作流

> **补充声明**：本项目的核心是 **Skill 整合概念**。各 Skill 均为 prompt 模块，后续会根据开源项目进展及前沿方向持续更新和替换，确保工作流始终与最新实践保持同步。

## 九类核心能力

| 能力 | 来源 | 用途 |
|------|------|------|
| 文献综述 Skill | 参考 [CAICAIIs/Auto-Scholar](https://github.com/CAICAIIs/Auto-Scholar) (MIT)；v4 引用验证参考 [PaperOrchestra](https://arxiv.org/abs/2604.05018)，期刊质量排序参考 [Paperguide.ai](https://paperguide.ai/)，合规检查参考 [ARS](https://github.com/Imbad0202/academic-research-skills) | 系统性文献综述、引用验证、期刊质量排序、多论文数据提取、系统综述合规检查 |
| 论文阅读 Skill | 参考 [917Dhj/DeepPaperNote](https://github.com/917Dhj/DeepPaperNote) | 深度阅读单篇论文、生成结构化研究笔记 |
| Critical Ideation Skill | **本项目原创**；v4 辩论机制参考 [Google AI Co-Scientist](https://arxiv.org/abs/2502.18864)，五维构思框架参考 [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | brainstorm、主动质疑、正反辩论、竞品检索、方向重构、MVP 收敛、五维构思 |
| 实验设计 Skill | 参考 [wjgoarxiv/autoresearch-skill](https://github.com/wjgoarxiv/autoresearch-skill) (MIT) | 实验方案设计、变量控制、消融实验规划 |
| 科研绘图 Skill | 参考 [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers)；v4 VLM 审查参考 [PaperOrchestra](https://arxiv.org/abs/2604.05018) 和 [AI Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) | 论文级 matplotlib 图、VLM 图表审查、概念示意图生成 |
| 引导式论文写作 Skill | 参考 [ShiyangZheng/scholarly](https://github.com/ShiyangZheng/scholarly)；v4 JSON 大纲参考 [PaperOrchestra](https://arxiv.org/abs/2604.05018)，引用接地参考 [LiRA](https://arxiv.org/abs/2510.05138)，并行写作参考 [AutoSurvey2](https://arxiv.org/abs/2510.26012)，风格校准和 Material Passport 参考 [ARS](https://github.com/Imbad0202/academic-research-skills)，Introduction Flowchart 参考 [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | 结构化 JSON 大纲、引用接地校验、并行章节写作、风格校准、产物溯源、引言流程图 |
| 学术写作 Prompt 库 | 引用 [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | 润色、翻译、实验分析、reviewer 检查 |
| 审稿检查 | 使用 awesome-ai-research-writing 中的 reviewer_check prompt；v4 评审+回滚参考 [PaperOrchestra](https://arxiv.org/abs/2604.05018)，多角度评审参考 [AI Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2)，完整性闸门和反谄媚协议参考 [ARS](https://github.com/Imbad0202/academic-research-skills) | 多角度评审、评审+回滚机制、结构化评分、完整性闸门、反谄媚协议 |
| Deep Research Skill (v4 new) | 参考 [Paperguide.ai](https://paperguide.ai/) 的 Deep Research | 自动发现→筛选→提取→趋势分析→综合报告 |

## Workflow 链条

```text
literature-review → paper-reading → critical-ideation → experiment-design → scientific-figure-making → scholarly-writing + awesome-ai-research-writing → reviewer_check
```

1. `literature-review`：系统性综述领域现状，识别研究 gap（v4: + 引用验证 + 期刊质量排序 + Workbooks 提取 + 合规检查）
2. `paper-reading`：深度阅读关键论文，生成结构化笔记
3. `critical-ideation`：先筛方向，不让项目在错误的 idea 上浪费时间（v4: + 正反辩论机制 + 五维构思框架）
4. `experiment-design`：设计实验方案，规划变量控制与消融实验
5. `scientific-figure-making`：把方向绑定到可见证据，而不是抽象口号（v4: + VLM 审查闭环 + 概念示意图）
6. `scholarly-writing`：从零构建论文骨架，按章节引导写作（v4: + 结构化 JSON 大纲 + 引用接地 + 并行写作 + 风格校准 + Material Passport + Introduction Flowchart）
7. `awesome-ai-research-writing`：把草稿润色到论文级表达
8. `reviewer_check`：防止过度 claim，逼着结论回到证据边界内（v4: + 多角度评审 + 评审回滚 + 完整性闸门 + 反谄媚协议）

### Deep Research Pipeline (v4 new)

```text
deep-research → (optional) critical-ideation → scholarly-writing + awesome-ai-research-writing → reviewer_check
```

## v4 变更摘要

基于 2026 年初 AI 科研工具领域全景比对（详见 `Version4_20260515/Paper_比对.md`），v4 重点补齐了以下核心质量短板：

| 变更 | 来源借鉴 | 说明 |
|------|---------|------|
| 引用验证 (Stage 3.5) | PaperOrchestra | Semantic Scholar API 验证 + LLM 降级验证 |
| 期刊质量排序 (Stage 4.5) | Paperguide.ai | SJR/SNIP 期刊质量指标 |
| Workbooks 结构化数据提取 | Paperguide.ai | 多论文对比提取表 |
| 结构化 JSON 大纲 | PaperOrchestra | 含可视化计划、文献策略、章节计划 |
| 引用接地校验 (Stage 2.5) | LiRA | 写作过程中实时校验引用真实性 |
| 并行章节写作 | AutoSurvey2 | 各章节可并行撰写后整合 |
| VLM 图表审查闭环 | PaperOrchestra / AI Scientist-v2 | 生成→VLM 检查→修正→再检查 |
| 概念示意图生成 | PaperOrchestra | PaperBanana 思路的概念图 prompt |
| 正反辩论机制 | Google AI Co-Scientist | Generate-Debate-Evolve 循环 |
| 评审+回滚机制 | PaperOrchestra | 仅当总分提升时接受修改 |
| 多角度评审 | AI Scientist-v2 | 5 份独立评审 + AC Meta-review |
| 完整性闸门 | ARS | 7项AI失败模式清单，关键阶段强制检查 |
| 反谄媚协议 | ARS | 魔鬼代言人机制，防止AI降低批评强度 |
| 风格校准 | ARS | 学习用户写作风格，减少AI味 |
| Material Passport | ARS | 产物溯源链，记录每段内容生成来源和验证状态 |
| Introduction Flowchart | Supervisor-Skills | 结构化引言写作流程图模型 |
| 五维构思框架 | Supervisor-Skills | 更高/更快/更强/更省/更广的Idea评估维度 |
| 合规检查 | ARS | PRISMA-trAIce 17项 + RAISE 4原则系统综述合规 |
| Deep Research Skill | Paperguide.ai | 自动发现→筛选→提取→趋势分析→综合报告 |

## Repository Layout

```text
ALL-in-ALL_ReSearching_Workflow_Skill/
|-- README.md
|-- LICENSE
|-- ROUTER.md
|-- cli.py                            (交互式 CLI 入口)
|-- DEPENDENCIES.md                   (上游依赖声明)
|-- docs/
|   `-- USAGE.md
|-- prompt-libraries/
|   `-- awesome-ai-research-writing/   (引用入口，需单独 clone 上游仓库)
|-- skills/
|   |-- literature-review/             (参考 Auto-Scholar + PaperOrchestra + Paperguide)
|   |   |-- SKILL.md
|   |   `-- templates/
|   |       |-- review_scope.md
|   |       |-- paper_summary_table.md
|   |       `-- workbooks_extraction.md (v4 new)
|   |-- paper-reading/                 (参考 DeepPaperNote 编写的使用指南)
|   |   |-- SKILL.md
|   |   `-- templates/
|   |-- critical-ideation/             (本项目原创 + Google AI Co-Scientist)
|   |   |-- SKILL.md
|   |   |-- templates/
|   |   |   |-- idea_card.md
|   |   |   |-- search_log.md
|   |   |   |-- decision_matrix.md
|   |   |   |-- critique_checklist.md
|   |   |   |-- mvp_plan.md
|   |   |   `-- debate_log.md          (v4 new)
|   |   `-- examples/
|   |-- experiment-design/             (参考 autoresearch-skill 编写的使用指南)
|   |   |-- SKILL.md
|   |   `-- templates/
|   |-- scientific-figure-making/      (参考 figures4papers + PaperOrchestra + AI Scientist-v2)
|   |   |-- SKILL.md
|   |   |-- references/
|   |   `-- templates/
|   |       `-- concept_diagram.md     (v4 new)
|   |-- scholarly-writing/             (参考 Scholarly + PaperOrchestra + LiRA + AutoSurvey2)
|   |   |-- SKILL.md
|   |   `-- templates/
|   `-- deep-research/                 (v4 new, 参考 Paperguide.ai)
|       |-- SKILL.md
|       `-- templates/
|-- prompts/
|   |-- reviewer_check.md              (v4 enhanced: 多角度评审 + 回滚)
|   |-- review_scorecard.md            (v4 new)
|   |-- experiment_analysis.md
|   |-- figure_generation.md
|   |-- paper_figure_full_pipeline.md
|   |-- polish_cn.md
|   `-- translate_cn_to_en.md
|-- templates/
|   `-- project_ai/
|-- examples/
|   `-- GeoAgent-Thesis/
`-- scripts/
```

## Quick Start

### 方式一：交互式 CLI / Interactive CLI

```bash
python cli.py
```

启动后可选择：
- **完整 Workflow**：文献综述 → 论文阅读 → 选题构思 → 实验设计 → 绘图 → 写作 → 润色 → 审稿检查
- **Idea Brainstorm**：与 Critical Ideation Skill 对质，可联动文献综述、论文阅读、实验设计
- **Paper Writing**：科研绘图 + 引导式论文写作 + 学术润色 + 审稿检查
- **Deep Research**：深度研究 → 趋势分析 → 综合报告 (v4 new)

CLI 会根据选择自动生成任务提示，复制到 Trae / Codex 中执行即可。

### 方式二：手动配置

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

- 仅文献综述：使用 `skills/literature-review/`
- 仅论文阅读：使用 `skills/paper-reading/`
- 仅 ideation / 选题：使用 `skills/critical-ideation/`
- 仅实验设计：使用 `skills/experiment-design/`
- 仅绘图：使用 `skills/scientific-figure-making/`
- 仅论文写作：使用 `skills/scholarly-writing/`
- 仅润色/翻译：使用 `prompt-libraries/awesome-ai-research-writing/`
- 深度研究报告：使用 `skills/deep-research/` (v4 new)
- 完整流程：综述 → 阅读 → 选题 → 实验设计 → 绘图 → 写作 → 润色 → reviewer 检查

详见 [ROUTER.md](https://github.com/timesbye/ALL-in-ALL_ReSearching_Workflow_Skill/blob/main/ROUTER.md)。

## Example Project

仓库内置了示例项目，展示完整 workflow：

- [`examples/GeoAgent-Thesis/WORKFLOW_SHOWCASE.md`](https://github.com/timesbye/ALL-in-ALL_ReSearching_Workflow_Skill/blob/main/examples/GeoAgent-Thesis/WORKFLOW_SHOWCASE.md)

## Third-Party Acknowledgments

| 项目 | 作者 | 用途 | 许可证 |
|------|------|------|--------|
| [Auto-Scholar](https://github.com/CAICAIIs/Auto-Scholar) | [CAICAIIs](https://github.com/CAICAIIs) | 文献综述 Skill 设计参考 | MIT |
| [DeepPaperNote](https://github.com/917Dhj/DeepPaperNote) | [917Dhj](https://github.com/917Dhj) | 论文阅读 Skill 设计参考 | 未声明 |
| [autoresearch-skill](https://github.com/wjgoarxiv/autoresearch-skill) | [wjgoarxiv](https://github.com/wjgoarxiv) | 实验设计 Skill 设计参考 | MIT |
| [Scholarly](https://github.com/ShiyangZheng/scholarly) | [ShiyangZheng](https://github.com/ShiyangZheng) | 引导式写作 Skill 设计参考 | 未声明 |
| [awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | [Leey21](https://github.com/Leey21) | 学术写作 Prompt 库 | 未声明 |
| [figures4papers](https://github.com/ChenLiu-1996/figures4papers) | [Chen Liu](https://chenliu-1996.github.io/) (Yale) | 科研绘图范式参考 | 未声明 |
| [PaperOrchestra](https://arxiv.org/abs/2604.05018) | Google Cloud AI Research | v4 引用验证、JSON 大纲、VLM 审查、评审回滚参考 | 学术参考 |
| [AI Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) | Sakana AI / Oxford / UBC | v4 VLM 审查、多角度评审参考 | 学术参考 |
| [Google AI Co-Scientist](https://arxiv.org/abs/2502.18864) | Google Research | v4 正反辩论机制参考 | 学术参考 |
| [LiRA](https://arxiv.org/abs/2510.05138) | 学术研究 | v4 引用接地校验参考 | 学术参考 |
| [AutoSurvey2](https://arxiv.org/abs/2510.26012) | 学术研究 | v4 并行章节写作参考 | 学术参考 |
| [Paperguide.ai](https://paperguide.ai/) | Paperguide | v4 期刊质量排序、Workbooks 提取、Deep Research 参考 | 商业产品 |
| [ARS](https://github.com/Imbad0202/academic-research-skills) | Edward Cheng-I Wu | v4 完整性闸门、反谄媚协议参考 | 开源 Plugin |
| [DeepScientist](https://github.com/ResearAI/DeepScientist) | 西湖大学 (ICLR 2026) | Findings Memory 科研长程记忆参考 | 开源 |
| [AI-Researcher](https://github.com/HKUDS/AI-Researcher) | 港大 HKUDS (NeurIPS 2025) | Knowledge Acquisition Agent、Idea Generator 参考 | 开源 |
| [SciDER](https://github.com/leonardodalinky/SciDER) | William & Mary 等 | Data Analysis Agent、自进化记忆参考 | 开源 |
| [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | 港科大 HKUSTDial | Introduction Flowchart、五维构思框架参考 | 开源 |

- 本项目**不复制分发**上述仓库的原始内容
- 各 Skill 目录为本项目基于上游理念编写的使用指南
- `skills/critical-ideation/` 为本项目原创内容

详见 [LICENSE](LICENSE) 中的 Third-Party Acknowledgments 部分。

## License

本项目原创内容采用 [MIT License](LICENSE) 授权。

上游项目的原始内容归各自作者所有，适用其各自的使用条款。
