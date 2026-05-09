# DION AI Research Toolkit Router

[![GitHub](https://img.shields.io/badge/Github-timesbye%2FDION--AI--Research--Toolkit-blue?logo=github)](https://github.com/timesbye/DION-AI-Research-Toolkit)

## 1. Academic Writing Prompt Library

Path:

```text
prompt-libraries/awesome-ai-research-writing/
```

Use for:

- Chinese academic polishing
- English academic polishing
- Chinese-to-English academic translation
- English-to-Chinese academic translation
- abstract writing
- introduction rewriting
- related work organization
- experiment analysis
- reviewer-style critique
- AI-tone reduction
- logical coherence checking

Rules:

- Preserve technical meaning.
- Do not invent results, citations, or experimental claims.
- Use formal academic language.
- Avoid exaggerated contribution statements.
- Keep terminology consistent with the target project.

---

## 2. Scientific Figure Making Skill

Path:

```text
skills/scientific-figure-making/
```

Important files:

- `SKILL.md`
- `references/api.md`
- `references/design-theory.md`
- `references/common-patterns.md`
- `references/demos.md`
- `references/tutorials.md`

Use for:

- publication-quality scientific figures
- matplotlib scripts
- bar plots
- line plots
- radar plots
- ablation figures
- comparison figures
- heatmaps
- multi-panel figures
- exporting PDF and PNG

Rules:

- Generate reproducible Python scripts.
- Save scripts to the target project's `figures/scripts/`.
- Save outputs to the target project's `figures/outputs/`.
- Export both PDF and PNG.
- Use readable axis labels, legends, and captions.
- Prefer clean academic style.
- Do not use decorative or marketing-style charts.

---

## 3. Critical Ideation Skill

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

Do not use this skill for normal paper polishing, translation, figure generation, or deterministic coding tasks.

---

## 4. Combined Workflows

### Figure + Writing

When a task involves both experimental visualization and paper writing:

1. Use `scientific-figure-making` to design and generate the figure.
2. Save the plotting script into the target project.
3. Save PDF and PNG outputs into the target project.
4. Draft the figure caption.
5. Use `awesome-ai-research-writing` to polish the caption.
6. Write a thesis-style or paper-style result analysis paragraph.
7. Use reviewer-style critique to check whether the figure supports the stated claim.

### Ideation + Writing

When a task involves idea generation and formal writing:

1. Use `critical-ideation` to generate, challenge, search, refine, and rank ideas.
2. Save the ideation outputs to the target project's `ideas/`.
3. Use `awesome-ai-research-writing` to turn the selected idea into a proposal, PRD, README, or paper section.

### Ideation + Figure + Writing

When a task involves experiment design or benchmark planning:

1. Use `critical-ideation` to define the right experimental question and shortlist feasible directions.
2. Use `scientific-figure-making` to visualize results or benchmark comparisons.
3. Use `awesome-ai-research-writing` to write figure captions and result analysis.

---

## 5. Routing Rules

If the task is mainly about writing, translation, polishing, summarization, or review:

Use:

```text
prompt-libraries/awesome-ai-research-writing/
```

If the task is mainly about plotting, visualization, or chart design:

Use:

```text
skills/scientific-figure-making/
```

If the task is mainly about brainstorming, idea validation, novelty checks, project differentiation, or competitor-aware ideation:

Use:

```text
skills/critical-ideation/
```

If the task is about both figure generation and experiment analysis:

Use both, in this order:

```text
scientific-figure-making
-> caption draft
-> awesome-ai-research-writing
-> result analysis
-> reviewer check
```

If the task is about both ideation and formal writing:

Use both, in this order:

```text
critical-ideation
-> shortlist and MVP
-> awesome-ai-research-writing
-> proposal / PRD / introduction
```

---

## 6. Important Safety Rule

Do not modify toolkit source files unless the user explicitly asks to update the toolkit itself.

When working inside another project, all generated outputs must be saved into the current project directory, not into the toolkit directory.
