# Reviewer 视角检查 (v4 enhanced)

> **v4 增强**：评审+回滚机制参考自 [PaperOrchestra](https://arxiv.org/abs/2604.05018) 的 AgentReview；多角度评审参考自 [AI Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) 的 5 份独立评审 + AC Meta-review 模式；完整性闸门和反谄媚协议参考自 [ARS](https://github.com/Imbad0202/academic-research-skills) 的 AI 失败模式清单和魔鬼代言人机制。

请参考 `prompt-libraries/awesome-ai-research-writing/` 中的审稿、逻辑检查、论文批评思路（需先 clone 上游仓库）。

## 第一部分：单次评审检查

请从以下角度检查论文片段：

1. 研究问题是否清晰。
2. 方法动机是否充分。
3. 贡献是否过度声称。
4. 实验是否支撑结论。
5. 是否存在逻辑跳跃。
6. 是否有术语不一致。
7. 是否存在表达冗余或 AI 味过重的问题。

输出：

- Major Issues
- Minor Issues
- Suggested Revision
- Risk Level: Low / Medium / High

## 第二部分：多角度评审 (v4 new)

> **来源**：AI Scientist-v2 的 5 份独立评审 + AC Meta-review

生成 **5 份独立评审**，每份从不同角色视角出发：

### Reviewer 1: 方法论专家 (Methodology Expert)
- 方法是否合理？
- 实验设计是否严谨？
- 是否有遗漏的 baseline？

### Reviewer 2: 领域专家 (Domain Expert)
- 问题是否有意义？
- 与领域前沿的关联是否准确？
- 领域内的重要工作是否被遗漏？

### Reviewer 3: 写作质量评审 (Writing Quality Reviewer)
- 论述是否清晰？
- 结构是否合理？
- 是否有冗余或模糊的表达？

### Reviewer 4: 实验严谨性评审 (Experimental Rigor Reviewer)
- 实验是否可复现？
- 消融实验是否充分？
- 统计显著性是否报告？

### Reviewer 5: 新颖性评审 (Novelty Reviewer)
- 贡献是否真正新颖？
- 与已有工作的区别是否足够？
- 是否存在隐性的前期工作重叠？

### AC Meta-Review

综合 5 份评审，生成 Area Chair 级别的 Meta-review：

1. 评审共识（所有评审者同意的点）
2. 评审分歧（评审者意见不一致的点）
3. 关键问题排名（按严重程度排序）
4. 最终建议：Accept / Minor Revision / Major Revision / Reject
5. 置信度：High / Medium / Low

## 第三部分：评审+回滚机制 (v4 new)

> **来源**：PaperOrchestra 的 AgentReview 评审+回滚机制

### 评审流程

1. **基线评分**：对当前论文版本打分（使用 `prompts/review_scorecard.md`）
2. **生成修改建议**：基于评审结果生成具体修改方案
3. **执行修改**：应用修改建议，生成新版本
4. **再评分**：对新版本重新打分
5. **决策**：
   - 如果新版本总分 **≥** 旧版本总分：**接受修改**，以新版本为基线继续
   - 如果新版本总分 **<** 旧版本总分：**回滚修改**，恢复旧版本，标记该修改方向为无效
6. **迭代**：重复步骤 2-5，直到无更多可改进项或达到最大迭代次数

### 回滚规则

- 每次修改前保存当前版本快照
- 回滚时完整恢复到修改前的版本
- 被回滚的修改方向不再尝试
- 最大迭代次数：3（可配置）
- 如果连续 2 次修改均被回滚，终止评审循环

### 终止条件

- 所有 Major Issues 已解决且无回滚
- 达到最大迭代次数
- 连续 2 次修改被回滚
- 总分达到目标阈值（如 8/10 以上）

```text
Review-Rollback Log
- Iteration 1: Score [old] → [new] → [Accept/Rollback]
- Iteration 2: Score [old] → [new] → [Accept/Rollback]
- ...
- Final score: [score]
- Total iterations: [N]
- Rollbacks: [N]
```

## 第四部分：完整性闸门 — 7项AI失败模式清单 (v4 new)

> **来源**：ARS 的 7 项 AI 失败模式清单（源自 Nature 研究 Lu et al., 2026）

在论文写作和评审的关键阶段（如大纲完成后、初稿完成后），必须运行以下完整性检查。任何一项检测到问题，必须人工确认后才能进入下一阶段。

### 检查清单

| # | AI 失败模式 | 检测方法 | 严重程度 |
|---|------------|---------|---------|
| 1 | **引用幻觉** | 引用是否在 Semantic Scholar API 中可验证？是否存在编造的作者、年份或标题？ | 🔴 Critical |
| 2 | **数据捏造** | 实验数据是否来自真实实验或可信来源？是否存在 AI 编造的数值？ | 🔴 Critical |
| 3 | **方法论编造** | 描述的方法是否真实存在且可执行？是否虚构了不存在的 baseline 或技术？ | 🔴 Critical |
| 4 | **过度声称** | 贡献声明是否与实验证据匹配？是否使用了"首次"、"最佳"等无法验证的断言？ | 🟡 Major |
| 5 | **逻辑不一致** | 引言提出的问题是否与结论回答的问题一致？方法描述是否与实验设置匹配？ | 🟡 Major |
| 6 | **隐性抄袭** | 是否存在大段与已有文献高度相似的文本？是否正确标注了引用来源？ | 🟡 Major |
| 7 | **统计谬误** | 是否报告了统计显著性？是否存在 p-hacking 或选择性报告？ | 🟡 Major |

### 闸门规则

- **Critical 级别**：检测到任何一项 → **必须人工确认**，否则阻止进入下一阶段
- **Major 级别**：检测到任何一项 → **标记警告**，建议人工确认后继续
- 闸门位置：scholarly-writing Stage 2.5（大纲完成后）和 Stage 4（初稿完成后）

```text
Integrity Gate Report
- Gate stage: [2.5 / 4]
- Critical issues found: [N]
- Major issues found: [N]
- Status: PASS / BLOCKED (requires human confirmation) / WARNED
- Items requiring confirmation: [list]
```

## 第五部分：反谄媚协议 (v4 new)

> **来源**：ARS 的反谄媚协议（Anti-Flattery Protocol）

### 问题定义

AI 在评审和修改过程中，可能为了讨好用户而：
- 降低批评强度
- 轻易接受用户的修改要求（即使修改降低了论文质量）
- 回避指出用户想法的根本性缺陷
- 在评审意见中使用过于温和的语言

### 协议规则

1. **魔鬼代言人约束**：在多角度评审中，Novelty Reviewer（新颖性评审）同时担任魔鬼代言人角色。当其评分低于 4/10 时，写作/修改团队**不得轻易让步**——必须先尝试正面回应批评，而非直接删除被批评的内容。

2. **批评强度保持**：在评审+回滚机制的迭代过程中，如果某次修改导致评审中某维度的分数下降，**不得通过降低该维度的评审标准来"修复"总分**。分数下降必须通过改进内容来弥补。

3. **独立评审不可协商**：5 份独立评审的原始评分和意见**不可被修改**。如果用户对某份评审有异议，只能通过追加"用户回应"附注，不能覆盖原始评审。

4. **过度声称检测**：如果评审发现贡献声明与实验证据不匹配，**不得通过弱化实验描述来匹配贡献声明**。正确做法是降低贡献声明的强度。

5. **修改方向标记**：被回滚的修改方向标记为"无效"。如果用户坚持尝试同一方向，必须提供新的理由（不能简单重试）。

```text
Anti-Flattery Compliance Report
- Devil's advocate score: [score]
- Score regression in any dimension: [Yes/No, which dimensions]
- Original reviews modified: [Yes/No]
- Overclaim detected and handled: [description]
- Blocked retry directions: [list]
```
