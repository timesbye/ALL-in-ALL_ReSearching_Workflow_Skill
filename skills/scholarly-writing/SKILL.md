---
name: scholarly-writing
description: Use for guided academic paper writing, section by section. This skill helps researchers build complete papers through structured conversation — from Abstract to Introduction, Literature Review, Methods, Results, Discussion, and Conclusion. It provides section-specific templates, common mistakes to avoid, and progressive development guidance.
---

# Scholarly Writing

> **设计灵感与参考来源**：本 Skill 的概念参考自 [ShiyangZheng/scholarly](https://github.com/ShiyangZheng/scholarly)（Agent Skill 格式的引导式论文写作工具）。本目录中的文档为 ALL-in-ALL_ReSearching_Workflow_Skill 项目基于其理念编写的使用指南，不包含 Scholarly 的原始内容。

Open `templates/` only as needed. Start from the workflow below.

## Purpose

Use this skill when the user needs to write an academic paper from scratch, section by section, with structured guidance.

This skill complements `awesome-ai-research-writing`:

- **scholarly-writing**: Builds the paper skeleton and structure (from zero to first draft)
- **awesome-ai-research-writing**: Polishes and refines existing text (from draft to publication-ready)

## When to use

Use this skill when the user asks to:

- write a paper
- write a thesis
- draft an abstract
- write an introduction
- write a literature review section
- write a methods section
- write a results section
- write a discussion
- structure a paper
- 写论文
- 写毕业论文
- 论文结构
- 写摘要
- 写引言
- 写方法
- 写结果
- 写讨论

## When not to use

Do not use this skill for:

- polishing existing text (use `awesome-ai-research-writing`)
- reading papers (use `paper-reading`)
- literature review research (use `literature-review`)
- brainstorming ideas (use `critical-ideation`)
- generating figures (use `scientific-figure-making`)

## Core workflow

### Stage 1: Determine paper type and scope

Identify:

- Paper type: conference paper, journal article, thesis chapter, technical report
- Target venue (if applicable)
- Research question
- Core contribution (one sentence)
- Available materials (data, figures, experiment results, literature notes)

```text
Paper Scope
- Type:
- Target venue:
- Research question:
- Core contribution:
- Available materials:
- Estimated length:
```

### Stage 2: Build the skeleton

Create the paper outline with section headings and one-sentence descriptions:

```text
1. Abstract [200-250 words]
2. Introduction [1-1.5 pages]
3. Related Work / Literature Review [1-2 pages]
4. Method / Approach [2-3 pages]
5. Experiments / Results [2-3 pages]
6. Discussion [0.5-1 page]
7. Conclusion [0.5 page]
```

Present the skeleton to the user for approval before proceeding.

### Stage 3: Write section by section

For each section, follow the section-specific guidance below.

#### Abstract

Structure:
1. Problem statement (1-2 sentences)
2. Gap in existing work (1 sentence)
3. Proposed approach (1-2 sentences)
4. Key result (1-2 sentences)
5. Impact / implication (1 sentence)

Common mistakes to avoid:
- Including background that belongs in the introduction
- Making claims not supported by the experiments
- Exceeding the word limit

#### Introduction

Four-layer structure:
1. **Context**: What is the broad problem area?
2. **Literature**: What have others done?
3. **Gap**: What is missing or insufficient?
4. **Purpose**: What does this paper do and why is it different?

Common mistakes to avoid:
- Starting too broadly ("Since the dawn of civilization...")
- Listing contributions before establishing the gap
- Overclaiming novelty

#### Related Work / Literature Review

Organize by theme, not by paper:
1. Theme A: [Group of related approaches]
2. Theme B: [Another group]
3. Positioning: How this work differs from all of the above

Common mistakes to avoid:
- Writing a paper-by-paper list instead of thematic synthesis
- Describing without comparing
- Failing to position your own work

#### Method / Approach

Structure:
1. Problem formulation
2. Overview of the approach
3. Detailed components (in order of execution)
4. Implementation details

Common mistakes to avoid:
- Mixing motivation with technical description
- Omitting details needed for reproducibility
- Using notation without definition

#### Experiments / Results

Structure:
1. Experimental setup (datasets, metrics, baselines, implementation)
2. Main results (with tables and figures)
3. Analysis (ablation, comparison, statistical significance)

Common mistakes to avoid:
- Reporting only best-case results
- Missing ablation studies
- Not explaining unexpected results

#### Discussion

Structure:
1. Interpretation of results
2. Connection to prior work
3. Limitations
4. Broader impact (if applicable)

Common mistakes to avoid:
- Repeating the results section
- Ignoring negative results
- Claiming more than the experiments support

#### Conclusion

Structure:
1. Summary of contribution (2-3 sentences)
2. Key takeaway
3. Future work (1-2 sentences)

Common mistakes to avoid:
- Introducing new information
- Repeating the abstract verbatim
- Vague future work ("we plan to explore...")

### Stage 4: Cross-section consistency check

After all sections are drafted:

1. Check that the abstract matches the actual content
2. Check that introduction claims are supported by results
3. Check that related work positions the paper correctly
4. Check that method description matches experiment setup
5. Check that discussion addresses the stated limitations

### Stage 5: Save draft

Save the draft to the target project's `paper/` directory:

- Filename: `paper/draft_v1.md` or `paper/draft_v1.tex`

## Default output structure

```text
1. Paper Scope Definition
2. Skeleton / Outline
3. Abstract
4. Introduction
5. Related Work
6. Method
7. Experiments & Results
8. Discussion
9. Conclusion
10. Cross-section Consistency Check
```

## Style rules

- Write in formal academic language
- Use consistent terminology throughout
- Every claim in the introduction should trace to evidence in the results
- Prefer specific statements over vague ones
- Separate facts from interpretation
- Follow the target venue's formatting guidelines

## Relationship to other skills

| Task | Use this skill |
|------|---------------|
| Build paper structure from scratch | `scholarly-writing` |
| Polish, translate, or refine existing text | `awesome-ai-research-writing` |
| Read and analyze a single paper | `paper-reading` |
| Survey multiple papers on a topic | `literature-review` |
| Brainstorm research directions | `critical-ideation` |
| Generate figures | `scientific-figure-making` |

## Templates

Use these bundled files as needed:

- `templates/abstract_template.md`
  Use when writing the abstract.
- `templates/paper_skeleton.md`
  Use when building the paper outline.
