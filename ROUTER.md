# ReSearching Figures Workflow Router

[![GitHub](https://img.shields.io/badge/Github-timesbye%2FReSearching\_Figures\_Workflow-blue?logo=github)](https://github.com/timesbye/ReSearching_Figures_Workflow)

> **项目定位**：通过引用已有前沿科研绘图和学术写作工具，并在此基础上构建原创 brainstorm 能力，整合为从论文阅读到论文表达的一体式 workflow。

## 1. Paper Reading Skill

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

## 2. Literature Review Skill

> 来源：参考 [CAICAIIs/Auto-Scholar](https://github.com/CAICAIIs/Auto-Scholar)（MIT License）文献综述自动化理念，本项目编写使用指南

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

---

## 3. Critical Ideation Skill

> 来源：**本项目原创**

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

Workflow:

1. Frame the ideation problem.
2. Generate candidate ideas.
3. Critique each idea aggressively.
4. Search for existing work when novelty, feasibility, or market context depends on current information.
5. Refine ideas based on critique and evidence.
6. Rank ideas by novelty, feasibility, user value, differentiation, demonstrability, and fit.
7. Recommend only the ideas worth building.

---

## 4. Scientific Figure Making Skill

> 来源：参考 [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers) 绘图范式，本项目编写使用指南

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

Rules:

- Generate reproducible Python scripts.
- Save scripts to the target project's `figures/scripts/`.
- Save outputs to the target project's `figures/outputs/`.
- Export both PDF and PNG.
- Use readable axis labels, legends, and captions.
- Prefer clean academic style.

---

## 5. Scholarly Writing Skill

> 来源：参考 [ShiyangZheng/scholarly](https://github.com/ShiyangZheng/scholarly) 引导式论文写作理念，本项目编写使用指南

Path:

```text
skills/scholarly-writing/
```

Use for:

- writing a paper from scratch, section by section
- building paper structure and skeleton
- guided abstract, introduction, method, results, discussion writing
- thesis writing guidance

Relationship to `awesome-ai-research-writing`:

- `scholarly-writing`: Builds the paper skeleton (from zero to first draft)
- `awesome-ai-research-writing`: Polishes existing text (from draft to publication-ready)

---

## 6. Academic Writing Prompt Library

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

## 7. Full Workflow

The complete workflow chain from reading to writing:

```text
paper-reading → literature-review → critical-ideation → scientific-figure-making → scholarly-writing + awesome-ai-research-writing → reviewer check
```

### Full Pipeline

When a user wants to go from zero to a complete paper:

1. Use `paper-reading` to deeply read key papers and generate notes.
2. Use `literature-review` to survey the field and identify gaps.
3. Use `critical-ideation` to generate, challenge, and converge on a research direction.
4. Use `scientific-figure-making` to visualize experimental evidence.
5. Use `scholarly-writing` to build the paper structure and draft each section.
6. Use `awesome-ai-research-writing` to polish the draft.
7. Use reviewer-style critique to check whether claims match evidence.

### Partial Pipelines

**Reading + Ideation** (no writing yet):

```text
paper-reading -> literature-review -> critical-ideation
```

**Figure + Writing** (already have results):

```text
scientific-figure-making -> scholarly-writing -> awesome-ai-research-writing -> reviewer check
```

**Ideation + Writing** (already have a direction):

```text
critical-ideation -> scholarly-writing -> awesome-ai-research-writing
```

---

## 8. Routing Rules

If the task is mainly about reading and understanding papers:

```text
skills/paper-reading/
```

If the task is mainly about surveying a research area:

```text
skills/literature-review/
```

If the task is mainly about brainstorming, idea validation, or novelty checks:

```text
skills/critical-ideation/
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

---

## 9. Important Safety Rule

Do not modify toolkit source files unless the user explicitly asks to update the toolkit itself.

When working inside another project, all generated outputs must be saved into the current project directory, not into the toolkit directory.
