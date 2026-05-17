---
name: literature-review
description: Use for generating systematic literature reviews on a research topic. This skill searches academic databases, identifies relevant papers, extracts key findings, and synthesizes them into a structured review with proper citations. It supports human-in-the-loop paper selection, API-level citation verification, journal quality ranking, and multi-paper structured data extraction. Produces well-cited academic reviews with verified references.
---

# Literature Review

> **设计灵感与参考来源**：本 Skill 的概念参考自 [CAICAIIs/Auto-Scholar](https://github.com/CAICAIIs/Auto-Scholar)（MIT License，AI 驱动的文献综述生成器）。v4 引用验证流程参考自 [PaperOrchestra](https://arxiv.org/abs/2604.05018)（Google Cloud AI Research）的 API 级双重验证机制；期刊质量排序参考自 [Paperguide.ai](https://paperguide.ai/) 的 SJR/SNIP 指标；Workbooks 结构化数据提取参考自 Paperguide.ai 的多论文对比提取功能；合规检查参考自 [ARS](https://github.com/Imbad0202/academic-research-skills) 的 PRISMA-trAIce 合规 Agent。本目录中的文档为 ALL-in-ALL_ReSearching_Workflow_Skill 项目基于其理念编写的使用指南，不包含上述项目的原始代码。

Open `templates/` only as needed. Start from the workflow below.

## Purpose

Use this skill when the user needs a systematic literature review on a research topic, rather than reading individual papers.

This skill:

- generates search keywords from the research topic
- searches academic databases (Semantic Scholar, arXiv, PubMed)
- **verifies citation existence via API** (Semantic Scholar API, optional)
- filters and ranks candidate papers with **journal quality signals** (SJR/SNIP)
- presents candidates for user approval (human-in-the-loop)
- synthesizes approved papers into a structured, cited review
- supports **multi-paper structured data extraction** (Workbooks mode)

## When to use

Use this skill when the user asks to:

- do a literature review
- survey existing work on a topic
- find related work
- write a related work section
- understand the state of the art
- identify research gaps
- extract and compare data across multiple papers
- verify citation reliability
- 文献综述
- 调研现有工作
- 写 related work
- 了解研究现状
- 找相关论文
- 多论文数据提取对比

## When not to use

Do not use this skill for:

- reading and analyzing a single paper in depth (use `paper-reading`)
- brainstorming new ideas (use `critical-ideation`)
- writing or polishing text (use `scholarly-writing` or `awesome-ai-research-writing`)
- generating figures (use `scientific-figure-making`)
- deep research reports with trend analysis (use `deep-research`)

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

### Stage 3.5: Citation verification (v4 new)

> **来源**：PaperOrchestra 的 API 级引用验证机制

Verify that collected references actually exist and are correctly attributed. This stage eliminates citation hallucinations.

**Verification pipeline:**

1. **Semantic Scholar API lookup** (when API is available):
   - For each candidate paper, query by title + first author
   - Verify: title match, author match, year match, venue match
   - Record the Semantic Scholar paper ID for each verified reference

2. **Deduplication**:
   - Cross-reference verified papers to remove duplicates
   - Merge entries that refer to the same paper with different citation formats

3. **Date filtering**:
   - Confirm publication dates against the review scope
   - Flag preprints vs. peer-reviewed publications

4. **Generate verified .bib**:
   - Produce a BibTeX file with only verified references
   - Mark unverified references with `[UNVERIFIED]` prefix

**Degradation mode**: If Semantic Scholar API is unavailable or rate-limited, fall back to LLM self-verification:
- Ask the LLM to cross-check each reference against known databases
- Flag all references as `[LLM-VERIFIED]` (lower confidence) instead of `[API-VERIFIED]`
- Explicitly note the verification method in the review output

```text
Citation Verification Report
- Total candidates: [N]
- API-verified: [N]
- LLM-verified (fallback): [N]
- Unverifiable: [N]
- Duplicates removed: [N]
- Date-filtered out: [N]
- Generated .bib: [path]
```

### Stage 4: Filter and rank candidates

Apply inclusion/exclusion criteria:

1. Relevance to the research question
2. Recency (prefer recent work unless surveying history)
3. Venue quality (prefer top-tier venues)
4. Citation count (as a signal of influence)
5. Methodological rigor

Present the filtered list to the user for approval before proceeding.

### Stage 4.5: Journal quality ranking (v4 new)

> **来源**：Paperguide.ai 的 SJR/SNIP 期刊质量指标

Enhance the ranking with journal-level quality signals:

1. **SJR (SCImago Journal Rank)**: Measures journal prestige based on citation weight
2. **SNIP (Source Normalized Impact per Paper)**: Measures contextual citation impact
3. **Venue tier classification**:
   - Tier 1: Top-tier venues (e.g., NeurIPS, ICML, ACL, Nature, Science)
   - Tier 2: Well-regarded venues
   - Tier 3: Regional or emerging venues
   - Preprint: Not yet peer-reviewed

4. **Quality-adjusted ranking**:
   - Combine relevance score with journal quality signal
   - Papers from higher-tier venues get a quality boost
   - Preprints are not penalized but are flagged separately

```text
Quality-Enhanced Ranking
| # | Title | Relevance | Venue | SJR/SNIP | Tier | Adjusted Score |
|---|-------|-----------|-------|----------|------|----------------|
| 1 |       |           |       |          |      |                |
```

**Note**: SJR/SNIP data may not be available for all venues. When unavailable, use venue tier classification as a proxy.

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
- **Citation verification status** (API-verified / LLM-verified / Unverifiable)
- Clear attribution for every claim
- Explicit gap identification
- Connection to the user's own research direction

Save the output to the target project's `literature/` directory:

- Filename: `literature/review_[topic-slug].md`
- BibTeX: `literature/review_[topic-slug].bib`

### Stage 8: Compliance check — systematic review standards (v4 new)

> **来源**：ARS 的 Compliance Agent（PRISMA-trAIce 17 项 + RAISE 4 原则）

For systematic reviews (not required for quick surveys or related work sections), verify compliance with established reporting standards.

**When to run compliance check:**

- The review is a systematic review or meta-analysis
- The target venue requires PRISMA compliance
- The user explicitly requests compliance verification

**PRISMA-trAIce checklist** (17 items, adapted for AI-assisted reviews):

| # | Item | Check |
|---|------|-------|
| 1 | Research question defined | Is the research question explicitly stated? |
| 2 | Search strategy documented | Are all search queries recorded? |
| 3 | Databases listed | Are all databases and sources listed? |
| 4 | Search date recorded | Is the date of each search recorded? |
| 5 | Inclusion criteria stated | Are inclusion criteria explicit? |
| 6 | Exclusion criteria stated | Are exclusion criteria explicit? |
| 7 | Screening process described | Is the paper screening process documented? |
| 8 | Data extraction method | Is the data extraction method described? |
| 9 | Number of results per source | Are result counts per database reported? |
| 10 | Number of included papers | Is the final included paper count reported? |
| 11 | Flow diagram possible | Can a PRISMA flow diagram be generated? |
| 12 | Citation verification method | Is the citation verification method stated? |
| 13 | Quality assessment method | Is the quality assessment method described? |
| 14 | Synthesis method | Is the synthesis method (thematic/chronological) stated? |
| 15 | AI assistance disclosed | Is AI assistance in the review process disclosed? |
| 16 | Limitations stated | Are review limitations explicitly discussed? |
| 17 | Reproducibility | Can the review be reproduced from the documented methods? |

**RAISE principles** (4 items, for AI-assisted research):

| # | Principle | Check |
|---|-----------|-------|
| 1 | Responsibility | Is human oversight documented at each stage? |
| 2 | Accountability | Can each claim be traced to a verified source? |
| 3 | Inclusivity | Are diverse perspectives and venues represented? |
| 4 | Sustainability | Is the review method reusable for future updates? |

```text
Compliance Report
- PRISMA-trAIce items passed: [N]/17
- PRISMA-trAIce items failed: [N]/17
- RAISE items passed: [N]/4
- RAISE items failed: [N]/4
- Overall compliance: [FULL / PARTIAL / NON-COMPLIANT]
- Items requiring attention: [list]
```

## Workbooks mode (v4 new)

> **来源**：Paperguide.ai 的 Workbooks 结构化数据提取

When the user needs to extract and compare structured data across multiple papers (instead of a narrative review), use Workbooks mode.

### When to use Workbooks mode

- "Compare the datasets used across these papers"
- "Extract the key metrics from each paper into a table"
- "Create a comparison matrix of methods and results"
- "多论文数据提取对比"

### Workbooks workflow

1. Define extraction dimensions (what to extract from each paper)
2. Deep-read each approved paper
3. Extract structured data per dimension
4. Generate a comparison matrix
5. Highlight patterns, outliers, and gaps

Use `templates/workbooks_extraction.md` for the extraction template.

## Default output structure

```text
1. Review Scope & Methodology
2. Search Strategy & Results
3. Citation Verification Report (v4)
4. Thematic Synthesis
   - Theme A
   - Theme B
   - Theme C
5. Cross-cutting Analysis
6. Identified Gaps
7. Connection to Current Work
8. References (with verification status)
```

## Style rules

- Organize by theme, not by paper
- Every claim must have a citation
- **Every citation must be verified** (API-verified preferred, LLM-verified acceptable, unverifiable flagged)
- Separate established findings from preliminary results
- Flag papers with conflicting findings
- Do not inflate the number of papers cited — prefer depth over breadth
- Identify specific gaps rather than vague "more research is needed"
- Connect findings to the user's research context
- When SJR/SNIP data is available, incorporate it into quality assessment transparently

## Templates

Use these bundled files as needed:

- `templates/review_scope.md`
  Use when defining the review scope and search strategy.
- `templates/paper_summary_table.md`
  Use when presenting candidate papers for user approval.
- `templates/workbooks_extraction.md` (v4 new)
  Use when extracting and comparing structured data across multiple papers.
