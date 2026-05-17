# Version 4 Update Log

**日期**：2026-05-15
**版本**：v4
**核心主题**：基于行业全景比对的能力升级规划

---

## 一、版本背景

2026 年初，AI 科研工具领域发生剧变：

- **PaperOrchestra**（Google, 2026.04）提出 5-Agent 流水线，文献综述质量胜率 +50-68%
- **AI Scientist-v2**（Sakana AI, 2025.04）首篇 AI 论文通过 ICLR 双盲评审，登上 Nature
- **CycleResearcher**（西湖大学, ICLR 2025）开源 RL 训练的研究-评审循环模型
- **Paperguide.ai** 从 PDF 对话工具进化为一站式研究平台，推出 Deep Research 和 Workbooks
- **Google AI Co-Scientist** 展示了 Generate-Debate-Evolve 假设发现范式

这些进展对我们的项目提出了明确的升级压力：**在保持全链路覆盖和 HITL 优势的同时，必须补齐引用验证、自动化评审、图表审查等核心质量短板**。

---

## 二、比对结论摘要

详细比对见同目录 [`Paper_比对.md`](Paper_比对.md)。

### 综合评分（10维度，满分50）

> 注：以下评分基于 v4 Phase 2 完成后的状态，与 Paper_比对.md 中的 10 维度评分体系一致。

| 排名 | 工具 | 总分 | 核心长板 | 核心短板 |
|------|------|------|---------|---------|
| 1 | **我们 v4** | **38** | 功能广度、开源度、HITL、科研前端 | 自动化程度 |
| 2 | ARS | 33 | 安全完整性、输出质量 | 科研前端覆盖 |
| 3 | AI Scientist-v2 | 28 | 自动化、科研前端 | 易用性、HITL |
| 4 | Paperguide | 28 | 易用性 | 开源度、科研前端 |
| 5 | DeepScientist | 26 | 自动化、科研前端 | 易用性、HITL |
| 5 | AI-Researcher | 26 | 自动化、科研前端 | 易用性、HITL |
| 5 | SciDER | 26 | 数据驱动 | 易用性、HITL |
| 5 | Supervisor-Skills | 26 | 易用性 | 功能广度 |
| 5 | PaperOrchestra | 26 | 引用可靠性、输出质量 | 功能广度、HITL |
| 10 | CycleResearcher | 21 | 开源度 | 功能广度 |

### 关键差距识别

| 差距领域 | 差距描述 | 影响等级 |
|---------|---------|---------|
| 引用验证 | 无 API 级验证，存在引用幻觉风险 | 🔴 严重 |
| 大纲结构化 | 大纲为自由文本，缺乏可视化计划和文献策略 | 🔴 严重 |
| 评审闭环 | reviewer_check 为单次检查，无迭代回滚 | 🔴 严重 |
| 图表审查 | 无 VLM 审查，图表质量无自动验证 | 🔴 严重 |
| 数据提取 | 无多论文结构化对比提取 | 🟡 中等 |
| 期刊质量信号 | 文献排序无 SJR/SNIP 指标 | 🟡 中等 |
| 辩论机制 | critical-ideation 批判为单向，无正反辩论 | 🟡 中等 |

---

## 三、v4 变更清单

### 3.1 Skill 增强

#### literature-review（文献综述）

| 变更 | 类型 | 来源借鉴 | 说明 |
|------|------|---------|------|
| 新增 Stage 3.5：引用验证 | 增强 | PaperOrchestra | 搜索结果 → Semantic Scholar API 验证存在性 → 去重 → 日期过滤 → 生成 .bib |
| 新增 Stage 4.5：期刊质量排序 | 增强 | Paperguide | 在排序阶段引入 SJR/SNIP 期刊质量指标 |
| 新增模板：workbooks_extraction.md | 新增 | Paperguide | 多论文结构化数据提取对比表（替代原 paper_summary_table.md 的增强版） |

#### scholarly-writing（论文写作）

| 变更 | 类型 | 来源借鉴 | 说明 |
|------|------|---------|------|
| Stage 2 增强：结构化 JSON 大纲 | 增强 | PaperOrchestra | 大纲输出从自由文本升级为 JSON，包含 visualization_plan、lit_search_strategy、section_plan |
| 新增 Stage 2.5：引用接地校验 | 增强 | LiRA | 写作过程中实时校验引用真实性 |
| 新增模式：并行章节写作 | 新增 | AutoSurvey2 | 各章节可并行撰写后整合 |

#### scientific-figure-making（科研绘图）

| 变更 | 类型 | 来源借鉴 | 说明 |
|------|------|---------|------|
| 新增 Stage：VLM 图表审查闭环 | 增强 | PaperOrchestra / AI Scientist-v2 | 生成 → VLM 检查 → 修正 → 再检查，直到通过质量标准 |
| 新增模板：concept_diagram.md | 新增 | PaperOrchestra | 概念示意图生成 prompt（PaperBanana 思路） |

#### critical-ideation（选题构思）

| 变更 | 类型 | 来源借鉴 | 说明 |
|------|------|---------|------|
| Stage 3 增强：正反辩论机制 | 增强 | Google AI Co-Scientist | Attack 阶段从单向批判升级为 Generate-Debate-Evolve 循环 |
| 新增模板：debate_log.md | 新增 | Google AI Co-Scientist | 记录正反方辩论过程和结论 |

#### reviewer_check / prompts（审稿检查）

| 变更 | 类型 | 来源借鉴 | 说明 |
|------|------|---------|------|
| 增强：评审+回滚机制 | 增强 | PaperOrchestra | 评审 → 打分 → 仅当总分提升时接受修改 → 否则回滚 |
| 增强：多角度评审 | 增强 | AI Scientist-v2 | 5 份独立评审 + AC Meta-review → 最终评分 |
| 新增模板：review_scorecard.md | 新增 | PaperOrchestra | 结构化评审记分卡 |

### 3.2 新增 Skill

| Skill | 来源借鉴 | 说明 |
|-------|---------|------|
| deep-research | Paperguide | 自动发现 → 筛选 → 提取 → 趋势分析 → 综合报告（literature-review 的深度模式独立化） |

### 3.3 架构变更

| 变更 | 说明 |
|------|------|
| Workflow 链条更新 | `literature-review → paper-reading → critical-ideation → experiment-design → scientific-figure-making → scholarly-writing + awesome-ai-research-writing → reviewer_check` 不变，但各环节内部流程增强 |
| ROUTER.md 更新 | 新增 deep-research 路由规则 |
| 新增依赖 | Semantic Scholar API（引用验证，可选） |

---

## 四、不变项

以下内容在 v4 中保持不变：

- 项目核心定位：Skill 整合概念，Prompt 模块化
- 9 类核心能力框架（v4 新增 deep-research）
- Human-in-the-loop 设计哲学
- MIT 开源协议
- CLI 入口和项目模板结构
- 各 Skill 的上游参考来源声明

---

## 五、实施路线

```
Phase 1 — 核心质量提升 ✅ 已完成
│
├── ✅ 1.1 literature-review: 引用验证 + 期刊质量排序
├── ✅ 1.2 scholarly-writing: 结构化 JSON 大纲
├── ✅ 1.3 reviewer_check: 评审+回滚 + 多角度评审
└── ✅ 1.4 scientific-figure-making: VLM 图表审查闭环
│
Phase 2 — 功能完整性 ✅ 已完成
│
├── ✅ 2.1 新增 workbooks_extraction 模板
├── ✅ 2.2 新增 deep-research skill
├── ✅ 2.3 scholarly-writing: 引用接地校验
├── ✅ 2.4 critical-ideation: 辩论机制
├── ✅ 2.5 并行章节写作模式
├── ✅ 2.6 完整性闸门 + 反谄媚协议
├── ✅ 2.7 风格校准 + Material Passport
├── ✅ 2.8 Introduction Flowchart + 五维构思框架
└── ✅ 2.9 合规检查 (PRISMA-trAIce + RAISE)
│
Phase 3 — 生态扩展 ← 下一步
│
├── 3.1 Findings Memory 科研长程记忆
├── 3.2 Agentic Tree Search 实验模式
├── 3.3 Data Analysis Agent
├── 3.4 PDF 对话式阅读模式
└── 3.5 参考文献管理集成
```

---

## 六、风险与约束

| 风险 | 影响 | 缓解措施 |
|------|------|---------|
| Semantic Scholar API 限流 | 引用验证可能失败 | 设计为可选步骤，API 不可用时降级为 LLM 自验证 |
| VLM 审查增加 API 成本 | 图表生成流程变慢变贵 | 设计为可选步骤，用户可跳过 |
| 结构化 JSON 大纲增加复杂度 | 用户理解成本上升 | 保持向后兼容，自由文本大纲仍可用 |
| 辩论机制增加 token 消耗 | critical-ideation 成本上升 | 辩论轮次可配置，默认 2 轮 |

---

## 七、文件清单

| 文件 | 说明 |
|------|------|
| `Update.md` | 本文件，v4 变更日志 |
| `Paper_比对.md` | AI 科研工具全景比对分析（10 工具 × 20 维度） |
