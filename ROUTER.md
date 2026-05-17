# ALL-in-ALL ReSearching Workflow Skill Router

[![GitHub](https://img.shields.io/badge/Github-timesbye%2FALL--in--ALL\_ReSearching\_Workflow\_Skill-blue?logo=github)](https://github.com/timesbye/ALL-in-ALL_ReSearching_Workflow_Skill)

> **项目定位**：把散落在各处的好工具串到一起，补上缺失的关键环节，再让它们按正确顺序跑起来。核心是 Skill 整合概念，后续会根据开源项目进展及前沿方向持续更新。

## 1. Literature Review Skill

> 来源：参考 [CAICAIIs/Auto-Scholar](https://github.com/CAICAIIs/Auto-Scholar)（MIT License）文献综述自动化理念；v4 引用验证参考 [PaperOrchestra](https://arxiv.org/abs/2604.05018)，期刊质量排序参考 [Paperguide.ai](https://paperguide.ai/)，Workbooks 提取参考 Paperguide.ai，合规检查参考 [ARS](https://github.com/Imbad0202/academic-research-skills)

Path:

```text
skills/literature-review/
```

Use for:

- systematic literature review on a research topic
- surveying existing work
- writing a related work section
- identifying research gaps
- finding and organizing relevant papers
- citation verification (v4)
- journal quality ranking with SJR/SNIP (v4)
- multi-paper structured data extraction / Workbooks mode (v4)
- systematic review compliance check / PRISMA-trAIce (v4)

---

## 2. Paper Reading Skill

> 来源：参考 [917Dhj/DeepPaperNote](https://github.com/917Dhj/DeepPaperNote) 论文深度阅读理念，本项目编写使用指南

Path:

```text
skills/paper-reading/
```

Use for:

- deep-reading a single research paper
- generating structured research notes
- extracting key contributions and methodology
- identifying limitations and open questions
- connecting a paper to the user's own work

---

## 3. Critical Ideation Skill

> 来源：**本项目原创**；v4 辩论机制参考 [Google AI Co-Scientist](https://arxiv.org/abs/2502.18864) 的 Generate-Debate-Evolve 循环；五维构思框架参考 [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills)

Path:

```text
skills/critical-ideation/
```

Use for:

- brainstorming
- research idea generation
- product idea generation
- PRD innovation
- startup idea validation
- project differentiation
- competitor-aware ideation
- adversarial critique
- Agent workflow design
- self-media topic ideation
- paper novelty check
- structured debate from opposing perspectives (v4)

Workflow:

1. Frame the ideation problem.
2. Generate candidate ideas.
3. Critique each idea aggressively (with Generate-Debate-Evolve cycle for promising ideas) (v4).
4. Search for existing work when novelty, feasibility, or market context depends on current information.
5. Refine ideas based on critique, debate, and evidence.
6. Rank ideas by novelty, feasibility, user value, differentiation, demonstrability, and fit.
7. Recommend only the ideas worth building.

---

## 4. Experiment Design Skill

> 来源：参考 [wjgoarxiv/autoresearch-skill](https://github.com/wjgoarxiv/autoresearch-skill)（MIT License）实验设计理念，本项目编写使用指南

Path:

```text
skills/experiment-design/
```

Use for:

- designing experiment plans and protocols
- variable control and confound identification
- ablation study planning
- baseline and benchmark selection
- experiment result logging and analysis
- reproducibility checklist

Rules:

- Save experiment plans to the target project's `experiments/`.
- Define clear independent/dependent variables before running.
- Specify baselines and metrics before seeing results.
- Plan ablation studies alongside main experiments.
- Document all hyperparameters and random seeds.

---

## 5. Scientific Figure Making Skill

> 来源：参考 [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers) 绘图范式；v4 VLM 审查参考 [PaperOrchestra](https://arxiv.org/abs/2604.05018) 和 [AI Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2)，概念示意图参考 PaperOrchestra

Path:

```text
skills/scientific-figure-making/
```

Use for:

- publication-quality scientific figures
- matplotlib scripts
- bar plots, line plots, radar plots
- ablation figures, comparison figures, heatmaps
- multi-panel figures
- exporting PDF and PNG
- VLM figure quality verification (v4)
- concept diagram generation (v4)

Rules:

- Generate reproducible Python scripts.
- Save scripts to the target project's `figures/scripts/`.
- Save outputs to the target project's `figures/outputs/`.
- Export both PDF and PNG.
- Use readable axis labels, legends, and captions.
- Prefer clean academic style.
- Run VLM review loop for publication figures (v4, when VLM available).

---

## 6. Scholarly Writing Skill

> 来源：参考 [ShiyangZheng/scholarly](https://github.com/ShiyangZheng/scholarly) 引导式论文写作理念；v4 结构化 JSON 大纲参考 [PaperOrchestra](https://arxiv.org/abs/2604.05018)，引用接地参考 [LiRA](https://arxiv.org/abs/2510.05138)，并行写作参考 [AutoSurvey2](https://arxiv.org/abs/2510.26012)，风格校准和 Material Passport 参考 [ARS](https://github.com/Imbad0202/academic-research-skills)，Introduction Flowchart 参考 [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills)

Path:

```text
skills/scholarly-writing/
```

Use for:

- writing a paper from scratch, section by section
- building paper structure and skeleton
- guided abstract, introduction, method, results, discussion writing
- thesis writing guidance
- structured JSON outline with visualization plan and literature strategy (v4)
- citation grounding verification (v4)
- parallel section writing mode (v4)
- style calibration (v4)
- material passport / content provenance tracking (v4)
- introduction flowchart model (v4)

Relationship to `awesome-ai-research-writing`:

- `scholarly-writing`: Builds the paper skeleton (from zero to first draft)
- `awesome-ai-research-writing`: Polishes existing text (from draft to publication-ready)

---

## 7. Academic Writing Prompt Library

> 来源：引用 [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing)

Path:

```text
prompt-libraries/awesome-ai-research-writing/
```

Use for:

- Chinese academic polishing
- English academic polishing
- Chinese-to-English academic translation
- English-to-Chinese academic translation
- experiment analysis
- reviewer-style critique
- AI-tone reduction
- logical coherence checking

Rules:

- Preserve technical meaning.
- Do not invent results, citations, or experimental claims.
- Use formal academic language.
- Avoid exaggerated contribution statements.

---

## 8. Deep Research Skill (v4 new)

> 来源：参考 [Paperguide.ai](https://paperguide.ai/) 的 Deep Research 功能（自动发现 → 筛选 → 提取 → 趋势分析 → 综合报告）

Path:

```text
skills/deep-research/
```

Use for:

- comprehensive deep research reports with trend analysis
- research landscape analysis
- automated paper discovery and synthesis
- trend analysis across time, methods, and performance
- gap analysis and future direction prediction
- 深度研究
- 研究趋势分析
- 领域全景报告

Relationship to `literature-review`:

- `literature-review`: Systematic review of existing work, focused on organizing and citing papers
- `deep-research`: Comprehensive research report with trend analysis, data extraction, and forward-looking insights

---

## 9. Reviewer Check

> 来源：使用 awesome-ai-research-writing 中的 reviewer_check prompt；v4 评审+回滚参考 [PaperOrchestra](https://arxiv.org/abs/2604.05018) 的 AgentReview，多角度评审参考 [AI Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) 的 5 份独立评审 + AC Meta-review，完整性闸门和反谄媚协议参考 [ARS](https://github.com/Imbad0202/academic-research-skills)

Path:

```text
prompts/reviewer_check.md
prompts/review_scorecard.md (v4 new)
```

Use for:

- reviewer-perspective quality check
- multi-perspective review (5 independent reviewers + AC Meta-review) (v4)
- review-rollback mechanism (only accept modifications that improve total score) (v4)
- structured scoring with review scorecard (v4)
- integrity gate — 7-item AI failure mode checklist (v4)
- anti-flattery protocol (v4)

---

## 10. Full Workflow

The complete workflow chain from literature review to reviewer check (v4 enhanced):

```text
literature-review → paper-reading → critical-ideation → experiment-design → scientific-figure-making → scholarly-writing + awesome-ai-research-writing → reviewer_check
```

Each skill's internal workflow has been enhanced in v4:

- `literature-review`: + citation verification + journal quality ranking + Workbooks mode + compliance check
- `critical-ideation`: + Generate-Debate-Evolve cycle + five-dimension framework
- `scientific-figure-making`: + VLM review loop + concept diagram generation
- `scholarly-writing`: + structured JSON outline + citation grounding + parallel writing + style calibration + material passport + introduction flowchart
- `reviewer_check`: + multi-perspective review + review-rollback mechanism + integrity gate + anti-flattery protocol

### Full Pipeline

When a user wants to go from zero to a complete paper:

1. Use `literature-review` to survey the field and identify gaps (with citation verification, quality ranking, and compliance check).
2. Use `paper-reading` to deeply read key papers and generate notes.
3. Use `critical-ideation` to generate, challenge, debate, and converge on a research direction (with five-dimension framework).
4. Use `experiment-design` to plan experiments, define variables, and design ablation studies.
5. Use `scientific-figure-making` to visualize experimental evidence (with VLM quality review).
6. Use `scholarly-writing` to build the paper structure (with JSON outline, citation grounding, style calibration, material passport, and introduction flowchart) and draft each section.
7. Use `awesome-ai-research-writing` to polish the draft.
8. Use `reviewer_check` to run multi-perspective review with rollback mechanism, integrity gate, and anti-flattery protocol.

### Deep Research Pipeline (v4 new)

When a user wants a comprehensive research landscape report:

```text
deep-research → (optional) critical-ideation → scholarly-writing + awesome-ai-research-writing → reviewer_check
```

1. Use `deep-research` to discover, filter, extract, analyze trends, and synthesize a comprehensive report.
2. Optionally use `critical-ideation` to identify promising directions from the report.
3. Use `scholarly-writing` + `awesome-ai-research-writing` to write up the findings.
4. Use `reviewer_check` to verify quality.

### Partial Pipelines

**Review + Reading + Ideation** (no writing yet):

```text
literature-review -> paper-reading -> critical-ideation
```

**Ideation + Experiment Design** (already have a direction):

```text
critical-ideation -> experiment-design
```

**Experiment + Figure + Writing** (already have results):

```text
experiment-design -> scientific-figure-making -> scholarly-writing -> awesome-ai-research-writing -> reviewer check
```

**Figure + Writing** (already have results and experiment plan):

```text
scientific-figure-making -> scholarly-writing -> awesome-ai-research-writing -> reviewer check
```

**Deep Research only** (comprehensive landscape report):

```text
deep-research
```

---

## 11. Routing Rules

If the task is mainly about surveying a research area (standard review):

```text
skills/literature-review/
```

If the task is about comprehensive deep research with trend analysis:

```text
skills/deep-research/
```

If the task is mainly about reading and understanding papers:

```text
skills/paper-reading/
```

If the task is mainly about brainstorming, idea validation, or novelty checks:

```text
skills/critical-ideation/
```

If the task is mainly about designing experiments, planning ablations, or variable control:

```text
skills/experiment-design/
```

If the task is mainly about plotting or visualization:

```text
skills/scientific-figure-making/
```

If the task is mainly about writing a paper from scratch:

```text
skills/scholarly-writing/
```

If the task is mainly about polishing, translating, or refining existing text:

```text
prompt-libraries/awesome-ai-research-writing/
```

If the task is mainly about reviewer-style quality checking:

```text
prompts/reviewer_check.md
```

---

## 12. Important Safety Rule

Do not modify toolkit source files unless the user explicitly asks to update the toolkit itself.

When working inside another project, all generated outputs must be saved into the current project directory, not into the toolkit directory.
