---
name: deep-research
description: Use for generating comprehensive deep research reports on a research topic. This skill goes beyond literature review by automatically discovering papers, filtering by relevance and quality, extracting structured data, analyzing trends, and synthesizing a comprehensive research report with trend analysis and future predictions. It extends literature-review into a deep-dive mode, operating as an independent standalone skill.
---

# Deep Research

> **设计灵感与参考来源**：本 Skill 的概念参考自 [Paperguide.ai](https://paperguide.ai/) 的 Deep Research 功能（自动发现 → 筛选 → 提取 → 趋势分析 → 综合报告）。本目录中的文档为 ALL-in-ALL_ReSearching_Workflow_Skill 项目基于其理念编写的使用指南。

Open `templates/` only as needed. Start from the workflow below.

## Purpose

Use this skill when the user needs a comprehensive deep research report on a topic, going beyond a standard literature review to include trend analysis, gap identification, and future direction predictions.

This skill differs from `literature-review`:

- **literature-review**: Systematic review of existing work, focused on organizing and citing papers
- **deep-research**: Comprehensive research report with trend analysis, data extraction across papers, and forward-looking insights

## When to use

Use this skill when the user asks to:

- do a deep research report
- analyze research trends on a topic
- generate a comprehensive research overview
- discover and synthesize papers with trend analysis
- create a research landscape report
- understand the evolution of a field
- 深度研究
- 研究趋势分析
- 领域全景报告
- 综合研究报告

## When not to use

Do not use this skill for:

- a simple literature review without trend analysis (use `literature-review`)
- reading and analyzing a single paper (use `paper-reading`)
- brainstorming new ideas (use `critical-ideation`)
- writing or polishing text (use `scholarly-writing` or `awesome-ai-research-writing`)
- generating figures (use `scientific-figure-making`)

## Core workflow

### Stage 1: Define the research scope

Clarify:

- Research topic or question
- Scope boundaries (time range, venues, domains, geographic scope)
- Required depth (landscape overview vs. deep-dive analysis)
- Target audience (researchers, practitioners, decision-makers)
- Key questions to answer
- Output format (report, presentation, brief)

```text
Deep Research Scope
- Topic:
- Time range:
- Domains:
- Depth:
- Target audience:
- Key questions:
- Output format:
```

### Stage 2: Automated discovery

Systematically discover relevant papers and resources:

1. **Seed query generation**: Create initial search queries from the topic
2. **Multi-source search**:
   - Semantic Scholar API (when available)
   - arXiv API (when available)
   - PubMed (for biomedical topics)
   - Google Scholar (via web search)
   - Conference proceedings (NeurIPS, ICML, ACL, CVPR, etc.)
3. **Snowball sampling**: For each discovered paper, check its references and citations
4. **Author network expansion**: Identify key authors and find their other relevant work
5. **Temporal coverage**: Ensure coverage across the specified time range

```text
Discovery Report
- Seed queries:
- Sources searched:
- Total papers discovered:
- Time range covered:
- Key authors identified:
- Key venues identified:
```

### Stage 3: Filtering and quality assessment

Filter discovered papers using multi-dimensional criteria:

1. **Relevance filtering**: Papers directly addressing the research questions
2. **Quality filtering**:
   - Venue tier (Tier 1/2/3/Preprint)
   - Citation count
   - SJR/SNIP (when available)
3. **Diversity filtering**: Ensure coverage across subtopics, methods, and perspectives
4. **Recency weighting**: Recent papers weighted higher unless historical survey is requested

Present the filtered list to the user for approval before proceeding.

### Stage 4: Citation verification

Apply the same citation verification pipeline as `literature-review` Stage 3.5:

- Semantic Scholar API verification (preferred)
- LLM self-verification (fallback)
- Deduplication and date filtering
- Generate verified .bib

### Stage 5: Deep extraction

For each approved paper, extract structured data beyond what a standard review would capture:

1. **Core data**: Contribution, method, results, limitations
2. **Trend data**: Publication year, method category, evaluation metrics, dataset used
3. **Comparative data**: Performance numbers, baselines compared, improvement percentages
4. **Evolution data**: How this paper builds on or differs from prior work
5. **Gap data**: What the paper identifies as future work or limitations

Use `skills/literature-review/templates/workbooks_extraction.md` for structured extraction.

### Stage 6: Trend analysis

Analyze the extracted data to identify patterns and trends:

1. **Temporal trends**:
   - How has the field evolved over time?
   - What methods were popular in each era?
   - What is the current trajectory?

2. **Method trends**:
   - What are the dominant methodological approaches?
   - What methods are emerging or declining?
   - What is the methodological convergence or divergence?

3. **Performance trends**:
   - How have benchmark results improved over time?
   - What are the current state-of-the-art numbers?
   - Where is progress stalling?

4. **Gap analysis**:
   - What subtopics are underexplored?
   - What methods have been tried but abandoned (and why)?
   - What evaluation dimensions are missing?

5. **Prediction**:
   - Based on current trends, what directions are most promising?
   - What bottlenecks are likely to emerge?
   - What cross-disciplinary opportunities exist?

```text
Trend Analysis Summary
- Temporal trend: [description]
- Method trend: [description]
- Performance trend: [description]
- Key gaps: [list]
- Predicted directions: [list]
```

### Stage 7: Synthesize the deep research report

Produce the final comprehensive report:

```text
1. Executive Summary
2. Research Scope & Methodology
3. Landscape Overview
   - Field definition and boundaries
   - Key players and groups
   - Publication volume trends
4. Thematic Deep-Dive
   - Theme A: [detailed analysis with trend data]
   - Theme B: [detailed analysis with trend data]
   - Theme C: [detailed analysis with trend data]
5. Trend Analysis
   - Temporal trends
   - Methodological trends
   - Performance trends
6. Comparative Analysis
   - Method comparison matrix
   - Performance benchmark table
7. Gap Analysis
   - Underexplored areas
   - Missing evaluation dimensions
   - Abandoned approaches worth revisiting
8. Future Directions
   - Most promising research directions
   - Emerging opportunities
   - Predicted bottlenecks
9. Recommendations
   - For researchers
   - For practitioners
   - For decision-makers
10. References (with verification status)
```

Save the output to the target project's `literature/` directory:

- Filename: `literature/deep_research_[topic-slug].md`
- BibTeX: `literature/deep_research_[topic-slug].bib`
- Trend data: `literature/deep_research_[topic-slug]_trends.json`

## Default output structure

```text
1. Executive Summary
2. Research Scope & Methodology
3. Landscape Overview
4. Thematic Deep-Dive
5. Trend Analysis
6. Comparative Analysis
7. Gap Analysis
8. Future Directions
9. Recommendations
10. References
```

## Style rules

- Organize by theme with temporal context
- Every claim must have a citation with verification status
- Separate established findings from emerging trends
- Quantify trends wherever possible (numbers, percentages, timelines)
- Identify specific gaps rather than vague "more research is needed"
- Make predictions with explicit confidence levels (High / Medium / Low)
- Connect findings to the user's research context
- Include visual trend descriptions (even without actual figures)

## Relationship to other skills

| Task | Use this skill |
|------|---------------|
| Standard literature review without trend analysis | `literature-review` |
| Read a single paper in depth | `paper-reading` |
| Brainstorm research directions | `critical-ideation` |
| Write a paper from the research findings | `scholarly-writing` |
| Generate figures for the report | `scientific-figure-making` |
| Polish the report text | `awesome-ai-research-writing` |

## Templates

Use these bundled files as needed:

- `templates/deep_research_scope.md`
  Use when defining the deep research scope and discovery strategy.
