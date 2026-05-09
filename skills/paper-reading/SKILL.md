---
name: paper-reading
description: Use for deep-reading a single research paper and generating structured research notes. This skill extracts key contributions, methodology, results, limitations, and connections to the user's own work. It produces Obsidian-style notes that can be stored in the project's literature/ directory.
---

# Paper Reading

> **设计灵感与参考来源**：本 Skill 的概念参考自 [917Dhj/DeepPaperNote](https://github.com/917Dhj/DeepPaperNote)（Agent Skill 格式的论文深度阅读工具）。本目录中的文档为 ReSearching_Figures_Workflow 项目基于其理念编写的使用指南，不包含 DeepPaperNote 的原始内容。

Open `templates/` only as needed. Start from the workflow below.

## Purpose

Use this skill when the user needs to deeply read and understand a research paper, rather than just skimming the abstract.

This skill produces structured research notes that:

- extract the core contribution and novelty claim
- decompose the methodology into reproducible steps
- identify assumptions, limitations, and threats to validity
- connect the paper to the user's own research context
- flag open questions and potential extensions

## When to use

Use this skill when the user asks to:

- read a paper
- analyze a paper
- generate notes from a paper
- understand a paper's contribution
- extract key information from a paper
- compare a paper with their own work
- evaluate a paper's methodology
- 读论文
- 论文笔记
- 论文分析
- 理解论文
- 提取论文要点

## When not to use

Do not use this skill for:

- generating a literature review across multiple papers (use `literature-review`)
- brainstorming new ideas based on a paper (use `critical-ideation`)
- writing or polishing text (use `scholarly-writing` or `awesome-ai-research-writing`)
- generating figures (use `scientific-figure-making`)

## Core workflow

### Stage 1: Paper identification

Identify the paper to read:

- Paper title
- Authors and affiliations
- Venue and year
- arXiv / DOI link (if available)

If the user provides a PDF or URL, extract metadata first.

### Stage 2: Structural decomposition

Break the paper into its structural components:

- Abstract: What is the one-sentence contribution?
- Introduction: What problem? Why now? What gap?
- Related Work: What are the key baselines and how does this differ?
- Method: What is the core technical approach?
- Experiments: What datasets, metrics, and baselines?
- Results: What are the main numbers and what do they claim?
- Discussion / Limitations: What do the authors acknowledge as limitations?
- Conclusion: What is the take-home message?

### Stage 3: Deep analysis

For each component, go beyond surface-level summary:

1. **Novelty claim**: What exactly is new? Is the claim precise or vague?
2. **Method reproducibility**: Could you reimplement this from the paper alone?
3. **Experimental rigor**: Are the baselines fair? Are the metrics appropriate? Is the evaluation comprehensive?
4. **Assumption audit**: What assumptions does the method make? Which are stated vs. implicit?
5. **Limitation identification**: What are the unstated limitations? Where might the method fail?
6. **Connection potential**: How does this relate to the user's own research direction?

### Stage 4: Generate structured notes

Produce notes in the following structure:

```text
# [Paper Title]

## Metadata
- Authors:
- Venue:
- Year:
- Link:

## One-line Summary
[One sentence capturing the core contribution]

## Problem & Motivation
- What problem:
- Why it matters:
- Gap in prior work:

## Key Contribution
- Claim:
- Mechanism:
- Differentiation from prior art:

## Method Breakdown
1. [Step 1]
2. [Step 2]
3. [Step 3]
...

## Experimental Setup
- Datasets:
- Metrics:
- Baselines:
- Key results:

## Strengths
- [Strength 1]
- [Strength 2]

## Weaknesses & Limitations
- [Limitation 1]
- [Limitation 2]

## Open Questions
- [Question 1]
- [Question 2]

## Connection to My Work
- Relevance:
- Potential extension:
- Risk of overlap:

## Key References
- [Ref 1]
- [Ref 2]
```

### Stage 5: Save notes

Save the generated notes to the target project's `literature/` directory:

- Filename: `literature/[author_year_short-title].md`
- Example: `literature/liu2026_geoagent-router.md`

## Default output structure

```text
1. Paper Metadata
2. One-line Summary
3. Problem & Motivation
4. Key Contribution
5. Method Breakdown
6. Experimental Setup & Results
7. Strengths
8. Weaknesses & Limitations
9. Open Questions
10. Connection to My Work
11. Key References
```

## Style rules

- Be precise about what the paper claims vs. what it actually demonstrates
- Separate facts from interpretation
- Flag vague claims explicitly
- Note reproducibility concerns
- Do not inflate the paper's contribution
- Do not dismiss the paper without specific evidence
- Connect to the user's context when possible

## Templates

Use these bundled files as needed:

- `templates/paper_note.md`
  Use when generating structured notes for a single paper.
