---
name: scholarly-writing
description: Use for guided academic paper writing, section by section. This skill helps researchers build complete papers through structured conversation — from Abstract to Introduction, Literature Review, Methods, Results, Discussion, and Conclusion. v4 adds structured JSON outlines with visualization plans and literature strategies, citation grounding verification, parallel section writing mode, style calibration, material passport, and introduction flowchart. Provides section-specific templates, common mistakes to avoid, and progressive development guidance.
---

# Scholarly Writing

> **设计灵感与参考来源**：本 Skill 的概念参考自 [ShiyangZheng/scholarly](https://github.com/ShiyangZheng/scholarly)（Agent Skill 格式的引导式论文写作工具）。v4 结构化 JSON 大纲参考自 [PaperOrchestra](https://arxiv.org/abs/2604.05018)（Google Cloud AI Research）的 Outline Agent JSON 蓝图；引用接地校验参考自 [LiRA](https://arxiv.org/abs/2510.05138) 的 citation grounding 机制；并行章节写作参考自 [AutoSurvey2](https://arxiv.org/abs/2510.26012) 的并行生成模式；完整性闸门参考自 [ARS](https://github.com/Imbad0202/academic-research-skills) 的 7 项 AI 失败模式清单；风格校准和 Material Passport 参考自 ARS；Introduction Flowchart 参考自 [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills)。本目录中的文档为 ALL-in-ALL_ReSearching_Workflow_Skill 项目基于其理念编写的使用指南，不包含 Scholarly 的原始内容。

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
- generate a structured outline
- write sections in parallel
- calibrate writing style
- track content provenance
- 写论文
- 写毕业论文
- 论文结构
- 写摘要
- 写引言
- 写方法
- 写结果
- 写讨论
- 并行写作
- 风格校准
- 产物溯源

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
- **User's writing style reference** (if available, for style calibration)

```text
Paper Scope
- Type:
- Target venue:
- Research question:
- Core contribution:
- Available materials:
- Estimated length:
- Style reference: [path to user's previous writing, or "default academic"]
```

### Stage 1.5: Style calibration (v4 new)

> **来源**：ARS 的风格校准（Style Calibration）机制

Before writing begins, calibrate the output style to match the user's voice and reduce AI-detectable patterns.

**When the user provides a style reference** (previous paper, thesis chapter, or writing sample):

1. **Analyze the reference text** for:
   - Sentence length distribution (short punchy vs. long complex)
   - Passive vs. active voice ratio
   - First-person usage ("we propose" vs. "this paper proposes")
   - Hedging intensity ("may", "might", "could" vs. definitive statements)
   - Paragraph structure (topic sentence position, paragraph length)
   - Technical jargon density
   - Transition patterns between ideas

2. **Generate a style profile**:
   ```text
   Style Profile
   - Avg sentence length: [N] words
   - Passive voice ratio: [N]%
   - First person usage: [frequent / moderate / rare]
   - Hedging intensity: [high / medium / low]
   - Avg paragraph length: [N] sentences
   - Jargon density: [high / medium / low]
   - Transition style: [explicit connectors / implicit flow]
   - Notable patterns: [description]
   ```

3. **Apply the style profile** during all subsequent writing stages.

**When no style reference is provided**:

Use the **default academic style**:
- Formal but not stiff
- Active voice preferred, passive for methodology
- Moderate hedging
- Clear topic sentences
- Explicit transitions between sections

**Anti-AI-tone rules** (always apply, regardless of style reference):

1. Avoid repetitive sentence structures (e.g., starting 3+ consecutive sentences with "Moreover", "Furthermore", "Additionally")
2. Vary sentence length — mix short declarative sentences with longer complex ones
3. Do not use formulaic transitions in every paragraph ("It is worth noting that...", "It is important to emphasize that...")
4. Avoid over-qualification chains ("It could potentially be argued that this might somewhat suggest...")
5. Prefer concrete statements over vague hedging when evidence supports it
6. Do not end every section with a summary sentence that merely restates the opening

### Stage 2: Build the structured JSON outline (v4 enhanced)

> **来源**：PaperOrchestra 的结构化 JSON 大纲生成

Create a structured JSON outline that goes beyond simple section headings. The outline must include visualization plans, literature search strategies, and per-section writing plans.

**Backward compatibility**: If the user prefers a simpler free-text outline, the original format from `templates/paper_skeleton.md` remains available. The JSON outline is the recommended default.

#### JSON outline schema

```json
{
  "paper_meta": {
    "title": "",
    "type": "",
    "target_venue": "",
    "research_question": "",
    "core_contribution": "",
    "estimated_length": ""
  },
  "visualization_plan": [
    {
      "figure_id": "fig1",
      "type": "bar_chart | line_plot | heatmap | scatter | table | diagram",
      "purpose": "",
      "data_source": "",
      "section": "",
      "priority": "required | recommended | optional"
    }
  ],
  "lit_search_strategy": {
    "primary_keywords": [],
    "secondary_keywords": [],
    "key_references": [
      {
        "citation_key": "",
        "title": "",
        "relevance": ""
      }
    ],
    "gaps_to_address": []
  },
  "section_plan": [
    {
      "section_id": "abstract",
      "title": "Abstract",
      "word_target": 200,
      "key_points": [],
      "dependencies": [],
      "figures": [],
      "citations_needed": []
    },
    {
      "section_id": "intro",
      "title": "1. Introduction",
      "word_target": 500,
      "key_points": ["Context", "Literature", "Gap", "Purpose"],
      "dependencies": [],
      "figures": [],
      "citations_needed": []
    },
    {
      "section_id": "related",
      "title": "2. Related Work",
      "word_target": 800,
      "key_points": ["Theme A", "Theme B", "Positioning"],
      "dependencies": ["lit_search_strategy"],
      "figures": [],
      "citations_needed": []
    },
    {
      "section_id": "method",
      "title": "3. Method",
      "word_target": 1200,
      "key_points": ["Problem formulation", "Overview", "Components", "Details"],
      "dependencies": [],
      "figures": ["fig1"],
      "citations_needed": []
    },
    {
      "section_id": "experiments",
      "title": "4. Experiments",
      "word_target": 1200,
      "key_points": ["Setup", "Main results", "Ablation", "Analysis"],
      "dependencies": ["method"],
      "figures": ["fig2", "fig3"],
      "citations_needed": []
    },
    {
      "section_id": "discussion",
      "title": "5. Discussion",
      "word_target": 400,
      "key_points": ["Interpretation", "Limitations", "Broader impact"],
      "dependencies": ["experiments"],
      "figures": [],
      "citations_needed": []
    },
    {
      "section_id": "conclusion",
      "title": "6. Conclusion",
      "word_target": 200,
      "key_points": ["Summary", "Key takeaway", "Future work"],
      "dependencies": ["experiments", "discussion"],
      "figures": [],
      "citations_needed": []
    }
  ],
  "writing_order": ["abstract", "intro", "related", "method", "experiments", "discussion", "conclusion"],
  "parallel_groups": []
}
```

Present the structured outline to the user for approval before proceeding.

### Stage 2.5: Citation grounding verification (v4 new)

> **来源**：LiRA 的引用接地（citation grounding）机制

Before and during writing, verify that all citations referenced in the outline are real and correctly attributed.

**Verification steps:**

1. **Pre-writing check**: For each citation in `lit_search_strategy.key_references`:
   - Verify the paper exists (Semantic Scholar API or web search)
   - Confirm the claimed relevance matches the paper's actual content
   - Flag any citations that cannot be verified

2. **During-writing check**: As each section is written:
   - Every in-text citation must trace to a verified reference
   - If a new citation is introduced during writing, verify it immediately
   - Mark unverified citations with `[CITE:?]` for the user to resolve

3. **Post-section check**: After each section is drafted:
   - Scan for any citation that lacks a corresponding entry in the reference list
   - Scan for any reference list entry that is never cited in the text
   - Report orphan citations and dangling references

```text
Citation Grounding Report (Section: [name])
- Total citations: [N]
- Verified: [N]
- Unverified (marked [CITE:?]): [N]
- Orphan references: [N]
- Dangling in-text citations: [N]
```

### Stage 3: Write section by section

For each section, follow the section-specific guidance below. **Apply the style profile from Stage 1.5 throughout.**

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

> **Enhanced with Introduction Flowchart** (v4 new, from Supervisor-Skills)

Use the **Introduction Flowchart** thinking model to structure the introduction:

```text
Introduction Flowchart
                    ┌─────────────┐
                    │   Context   │  What is the broad problem area?
                    │  (1-2 para) │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │ Literature  │  What have others done? (organized by theme)
                    │  (2-3 para) │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │    Gap      │  What is missing or insufficient?
                    │  (1-2 para) │  ← This is the most critical paragraph
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   Purpose   │  What does this paper do?
                    │  (1 para)   │  How is it different from existing work?
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │ Contributions│  Explicit list (3-5 items)
                    │  (1 para)   │  Each must trace to evidence
                    └─────────────┘
```

**Key rules for the Gap paragraph:**

1. The gap must be **specific**, not "more research is needed"
2. The gap must be **actionable** — it should directly motivate your approach
3. The gap must be **honest** — do not misrepresent prior work to create a gap
4. The gap must be **verifiable** — a reader familiar with the field should agree

Common mistakes to avoid:
- Starting too broadly ("Since the dawn of civilization...")
- Listing contributions before establishing the gap
- Overclaiming novelty
- Writing a "straw man" gap that misrepresents prior work

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

### Stage 3.5: Parallel section writing mode (v4 new)

> **来源**：AutoSurvey2 的并行章节生成模式

When the AI coding tool supports parallel execution (e.g., multiple agent instances), sections can be written in parallel based on the dependency graph in the JSON outline.

**Parallel groups** (default):

```text
Group 1 (independent): abstract, intro, related
Group 2 (depends on Group 1): method
Group 3 (depends on Group 2): experiments
Group 4 (depends on Group 3): discussion, conclusion
```

**Rules for parallel writing:**

1. Sections within the same parallel group can be written simultaneously
2. A section can only start after all its dependencies are complete
3. Each parallel section must use the same terminology and notation defined in the outline
4. After all parallel sections are complete, run a **cross-section consistency check** (Stage 4)
5. The abstract should be written last (or rewritten last) to ensure it matches the final content

**When to use parallel mode:**

- The user explicitly requests faster writing
- The AI coding tool supports parallel agent execution
- The paper is long enough that sequential writing is impractical

**When NOT to use parallel mode:**

- Short papers where sequential writing is fast enough
- When the user wants tight control over each section before proceeding
- When the AI coding tool does not support parallel execution

### Stage 4: Cross-section consistency check

After all sections are drafted:

1. Check that the abstract matches the actual content
2. Check that introduction claims are supported by results
3. Check that related work positions the paper correctly
4. Check that method description matches experiment setup
5. Check that discussion addresses the stated limitations
6. **Check that all citations are grounded** (from Stage 2.5)
7. **Check that all figures referenced in the outline appear in the text**
8. **Check terminology consistency across sections**
9. **Check style consistency** (from Stage 1.5 style profile)

### Stage 4.5: Integrity gate — 7-item AI failure mode checklist (v4 new)

> **来源**：ARS 的 7 项 AI 失败模式清单（源自 Nature 研究 Lu et al., 2026）

Before proceeding to the final draft, run the integrity gate from `prompts/reviewer_check.md` Part 4:

1. **Citation hallucination**: Are all citations API-verifiable?
2. **Data fabrication**: Are all experimental data from real experiments?
3. **Methodology fabrication**: Are all described methods real and executable?
4. **Overclaim**: Do contribution claims match experimental evidence?
5. **Logical inconsistency**: Do introduction questions match conclusion answers?
6. **Implicit plagiarism**: Is all text original or properly cited?
7. **Statistical fallacy**: Are statistical significances reported?

**Gate rule**: Any Critical-level issue (1-3) must be human-confirmed before proceeding. Any Major-level issue (4-7) triggers a warning.

```text
Integrity Gate Report (Stage 4.5)
- Critical issues: [N]
- Major issues: [N]
- Status: PASS / BLOCKED / WARNED
```

### Stage 5: Material Passport — content provenance tracking (v4 new)

> **来源**：ARS 的 Material Passport 产物溯源机制

After the draft is complete, generate a Material Passport that records the provenance of every content block in the paper. This enables traceability and accountability.

**Material Passport schema**:

For each paragraph or content block:

```text
Material Passport Entry
- Block ID: [section_id]-[paragraph_number]
- Section: [section name]
- Content summary: [1-sentence summary]
- Source type: [user_input | literature_cited | ai_generated | experiment_data | user_revision]
- Verification status: [verified | unverified | flagged]
- Citations in block: [list of citation keys]
- Last modified by: [user | ai]
- Modification history: [list of changes]
```

**Source type definitions**:

| Source type | Description | Trust level |
|------------|-------------|-------------|
| `user_input` | Directly provided by the user (original text, data, ideas) | High |
| `literature_cited` | Derived from a cited reference with proper attribution | High (if citation verified) |
| `experiment_data` | From actual experimental results | High |
| `ai_generated` | Generated by AI without direct user input or cited source | Medium — requires verification |
| `user_revision` | Modified by the user after AI generation | High |

**Material Passport report**:

```text
Material Passport Summary
- Total content blocks: [N]
- User input: [N] ([%])
- Literature cited: [N] ([%])
- Experiment data: [N] ([%])
- AI generated: [N] ([%])
- User revision: [N] ([%])
- Unverified blocks: [N]
- Flagged blocks: [N]

High-risk blocks (ai_generated + unverified):
- [Block ID]: [reason for flag]
```

**Usage**: The Material Passport is saved alongside the draft. During reviewer_check, the passport helps identify which content blocks need extra scrutiny.

### Stage 6: Save draft

Save the draft to the target project's `paper/` directory:

- Filename: `paper/draft_v1.md` or `paper/draft_v1.tex`
- JSON outline: `paper/outline.json`
- Citation grounding report: `paper/citation_grounding_report.md`
- Material Passport: `paper/material_passport.md`
- Style profile: `paper/style_profile.md`

## Default output structure

```text
1. Paper Scope Definition
2. Style Calibration (v4)
3. Structured JSON Outline (v4)
4. Citation Grounding Verification (v4)
5. Abstract
6. Introduction (with Flowchart model)
7. Related Work
8. Method
9. Experiments & Results
10. Discussion
11. Conclusion
12. Cross-section Consistency Check
13. Integrity Gate — AI Failure Mode Checklist (v4)
14. Material Passport (v4)
```

## Style rules

- Write in formal academic language
- Use consistent terminology throughout
- Every claim in the introduction should trace to evidence in the results
- Prefer specific statements over vague ones
- Separate facts from interpretation
- Follow the target venue's formatting guidelines
- **Every citation must be verifiable** — use `[CITE:?]` for unverified references
- **Figures referenced in the outline must appear in the corresponding section**
- **Apply the style profile from Stage 1.5** — match the user's voice
- **Follow anti-AI-tone rules** — avoid repetitive structures and formulaic transitions

## Relationship to other skills

| Task | Use this skill |
|------|---------------|
| Build paper structure from scratch | `scholarly-writing` |
| Polish, translate, or refine existing text | `awesome-ai-research-writing` |
| Read and analyze a single paper | `paper-reading` |
| Survey multiple papers on a topic | `literature-review` |
| Brainstorm research directions | `critical-ideation` |
| Generate figures | `scientific-figure-making` |
| Deep research with trend analysis | `deep-research` |

## Templates

Use these bundled files as needed:

- `templates/abstract_template.md`
  Use when writing the abstract.
- `templates/paper_skeleton.md`
  Use when building a simple free-text paper outline (backward compatible).
