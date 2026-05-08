# DION AI Research Toolkit Router

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

## 3. Mixed Figure + Writing Workflow

When a task involves both experimental visualization and paper writing:

1. Use `scientific-figure-making` to design and generate the figure.
2. Save the plotting script into the target project.
3. Save PDF and PNG outputs into the target project.
4. Draft the figure caption.
5. Use `awesome-ai-research-writing` to polish the caption.
6. Write a thesis-style or paper-style result analysis paragraph.
7. Use reviewer-style critique to check whether the figure supports the stated claim.

---

## 4. Routing Rules

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

If the task is about both figure generation and experiment analysis:

Use both, in this order:

```text
scientific-figure-making
-> caption draft
-> awesome-ai-research-writing
-> result analysis
-> reviewer check
```

---

## 5. Important Safety Rule

Do not modify toolkit source files unless the user explicitly asks to update the toolkit itself.

When working inside another project, all generated outputs must be saved into the current project directory, not into the toolkit directory.
