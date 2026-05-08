# Project AI Rules

## Project Identity

This is a project using DION-AI-Research-Toolkit.

Before starting any task, read:

```text
.ai/toolkit/ROUTER.md
```

## Toolkit Path

The toolkit should be linked as:

```text
.ai/toolkit/
```

## Writing Rules

For academic writing, polishing, translation, experiment analysis, and reviewer-style critique, use:

```text
.ai/toolkit/prompt-libraries/awesome-ai-research-writing/
```

General writing requirements:

- Preserve technical meaning.
- Do not invent results, citations, or experimental claims.
- Use formal academic style.
- Avoid exaggerated contribution statements.
- Keep terminology consistent with this project.

## Figure Rules

For scientific figures, use:

```text
.ai/toolkit/skills/scientific-figure-making/
```

Figure output rules:

- Save scripts to `figures/scripts/`.
- Save PDF and PNG to `figures/outputs/`.
- Generate reproducible Python matplotlib scripts.
- Use readable labels, legends, and captions.
- Avoid decorative or marketing-style charts.

## Mixed Task Workflow

For figure + paper writing tasks:

1. Read project data from `data/`.
2. Generate plotting script.
3. Save figure outputs.
4. Draft figure caption.
5. Polish caption using academic writing prompts.
6. Write result analysis paragraph.
7. Check whether the figure supports the stated claim.

## Important Rule

Do not modify `.ai/toolkit/` source files unless explicitly asked.

All generated files should be saved inside the current project.
