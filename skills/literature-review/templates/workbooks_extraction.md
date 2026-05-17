# Workbooks Extraction Template

> **来源**：Paperguide.ai 的 Workbooks 多论文结构化数据提取功能

Use this template to extract and compare structured data across multiple papers. This complements the simpler `paper_summary_table.md` when the user needs a detailed multi-dimensional comparison matrix.

## Extraction Dimensions

Define the dimensions to extract from each paper. Adjust based on the research domain.

### Core dimensions (always extract)

| Dimension | Description |
|-----------|-------------|
| Title | Paper title |
| Authors | First author + et al. or full list |
| Year | Publication year |
| Venue | Conference / Journal |
| Problem | What problem does it address? |
| Method | Core approach in one sentence |
| Key Result | Most important quantitative finding |
| Limitation | Stated or identified limitation |

### Domain-specific dimensions (select as needed)

| Dimension | Description |
|-----------|-------------|
| Dataset | Datasets used for evaluation |
| Baselines | Methods compared against |
| Metrics | Evaluation metrics |
| Code Available | Is code open-sourced? |
| Reproducibility | Can results be reproduced from the paper alone? |
| Scale | Problem/data scale |
| Domain | Application domain |
| Model Size | Parameter count or model scale |
| Compute | Computational requirements |
| Latency | Runtime or inference speed |
| Ablation | Are ablation studies provided? |
| Novelty Type | Architecture / Methodology / Application / Analysis |
| Open Problem | What remains unsolved? |

## Comparison Matrix Template

```markdown
# Multi-Paper Comparison: [Topic]

## Extraction Dimensions
- [ ] Core dimensions (default)
- [ ] Domain-specific: [list selected]

## Comparison Matrix

| Dimension | Paper 1 | Paper 2 | Paper 3 | Paper 4 | Paper 5 |
|-----------|---------|---------|---------|---------|---------|
| **Title** | | | | | |
| **Year** | | | | | |
| **Venue** | | | | | |
| **Problem** | | | | | |
| **Method** | | | | | |
| **Key Result** | | | | | |
| **Dataset** | | | | | |
| **Baselines** | | | | | |
| **Metrics** | | | | | |
| **Limitation** | | | | | |
| **Code** | | | | | |
| **Novelty Type** | | | | | |

## Cross-Paper Patterns

### Common approaches
- [Pattern shared across papers]

### Key differences
- [Where papers diverge]

### Progression over time
- [How the field has evolved year over year]

### Missing elements
- [What no paper adequately addresses]

## Gap Analysis
- [Specific gap 1]: No paper addresses [X] in context of [Y]
- [Specific gap 2]: [Method A] and [Method B] have not been compared on [Dataset C]

## Recommendations
- Best paper for [use case 1]: [Paper N] because [reason]
- Best paper for [use case 2]: [Paper M] because [reason]
- Most promising direction: [description] based on [evidence from matrix]
```

## Usage notes

- Start with core dimensions, then add domain-specific ones based on the user's needs
- Keep each cell concise — one sentence or a few keywords
- The comparison matrix can have up to 50 columns (papers), but 5-15 is typical
- After filling the matrix, always generate the Cross-Paper Patterns and Gap Analysis sections
- This template complements (not replaces) the narrative review — use both when appropriate
