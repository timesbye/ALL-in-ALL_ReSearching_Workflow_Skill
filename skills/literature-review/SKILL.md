---
name: literature-review
description: Use for generating systematic literature reviews on a research topic. This skill searches academic databases, identifies relevant papers, extracts key findings, and synthesizes them into a structured review with proper citations. It supports human-in-the-loop paper selection and produces well-cited academic reviews.
---

# Literature Review

> **设计灵感与参考来源**：本 Skill 的概念参考自 [CAICAIIs/Auto-Scholar](https://github.com/CAICAIIs/Auto-Scholar)（MIT License，AI 驱动的文献综述生成器）。本目录中的文档为 ReSearching_Figures_Workflow 项目基于其理念编写的使用指南，不包含 Auto-Scholar 的原始代码。

Open `templates/` only as needed. Start from the workflow below.

## Purpose

Use this skill when the user needs a systematic literature review on a research topic, rather than reading individual papers.

This skill:

- generates search keywords from the research topic
- searches academic databases (Semantic Scholar, arXiv, PubMed)
- filters and ranks candidate papers
- presents candidates for user approval (human-in-the-loop)
- synthesizes approved papers into a structured, cited review

## When to use

Use this skill when the user asks to:

- do a literature review
- survey existing work on a topic
- find related work
- write a related work section
- understand the state of the art
- identify research gaps
- 文献综述
- 调研现有工作
- 写 related work
- 了解研究现状
- 找相关论文

## When not to use

Do not use this skill for:

- reading and analyzing a single paper in depth (use `paper-reading`)
- brainstorming new ideas (use `critical-ideation`)
- writing or polishing text (use `scholarly-writing` or `awesome-ai-research-writing`)
- generating figures (use `scientific-figure-making`)

## Core workflow

### Stage 1: Define the review scope

Clarify:

- Research topic or question
- Scope boundaries (time range, venues, domains)
- Required depth (quick survey vs. comprehensive review)
- Target output format (narrative review, systematic review, related work section)
- User's existing knowledge level

```text
Review Scope
- Topic:
- Time range:
- Domains:
- Depth:
- Output format:
- User context:
```

### Stage 2: Generate search strategy

Create search keywords and queries:

1. Extract core concepts from the topic
2. Generate primary keywords (exact domain terms)
3. Generate secondary keywords (related terms, synonyms)
4. Generate exclusion terms (to filter noise)
5. Formulate database-specific queries

```text
Search Strategy
- Primary keywords:
- Secondary keywords:
- Exclusion terms:
- Databases to search:
- Expected paper count:
```

### Stage 3: Search and collect

Execute searches across available sources:

- Semantic Scholar API (when available)
- arXiv API (when available)
- PubMed (for biomedical topics)
- Google Scholar (via web search when APIs unavailable)
- User-provided papers

For each source, record:

- query used
- number of results
- top candidate papers with titles, authors, year, venue, abstract

### Stage 4: Filter and rank candidates

Apply inclusion/exclusion criteria:

1. Relevance to the research question
2. Recency (prefer recent work unless surveying history)
3. Venue quality (prefer top-tier venues)
4. Citation count (as a signal of influence)
5. Methodological rigor

Present the filtered list to the user for approval before proceeding.

### Stage 5: Deep-read approved papers

For each approved paper, use the `paper-reading` skill to extract:

- Core contribution
- Methodology
- Key results
- Limitations
- Relationship to other papers in the review

### Stage 6: Synthesize the review

Organize the review by theme, not by paper. Common structures:

**Thematic organization** (recommended):
```text
1. Introduction & Scope
2. Theme A: [First major theme]
   - Paper 1 contribution
   - Paper 2 contribution
   - Comparison and gap
3. Theme B: [Second major theme]
   ...
4. Cross-cutting analysis
5. Identified gaps
6. Conclusion & future directions
```

**Chronological organization** (for evolving topics):
```text
1. Introduction & Scope
2. Early work (before 2020)
3. Recent advances (2020-2023)
4. Current state (2024+)
5. Emerging directions
6. Conclusion
```

### Stage 7: Generate cited review

Produce the final review with:

- In-text citations in a consistent format
- Reference list at the end
- Clear attribution for every claim
- Explicit gap identification
- Connection to the user's own research direction

Save the output to the target project's `literature/` directory:

- Filename: `literature/review_[topic-slug].md`

## Default output structure

```text
1. Review Scope & Methodology
2. Search Strategy & Results
3. Thematic Synthesis
   - Theme A
   - Theme B
   - Theme C
4. Cross-cutting Analysis
5. Identified Gaps
6. Connection to Current Work
7. References
```

## Style rules

- Organize by theme, not by paper
- Every claim must have a citation
- Separate established findings from preliminary results
- Flag papers with conflicting findings
- Do not inflate the number of papers cited — prefer depth over breadth
- Identify specific gaps rather than vague "more research is needed"
- Connect findings to the user's research context

## Templates

Use these bundled files as needed:

- `templates/review_scope.md`
  Use when defining the review scope and search strategy.
- `templates/paper_summary_table.md`
  Use when presenting candidate papers for user approval.
