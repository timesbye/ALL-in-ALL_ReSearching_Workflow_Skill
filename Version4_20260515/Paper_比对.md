# AI 科研工具全景比对分析

> 本文档对当前主流 AI 科研辅助工具与 **ALL-in-ALL ReSearching Workflow Skill**（本项目）进行系统性比对，识别可学习的内容模块与改进方向。更新至 2026.05，包含 v4 已实现变更和新发现竞品。

---

## 一、比对对象概览

| 工具 | 类型 | 来源 | 发布时间 | 核心定位 |
|------|------|------|----------|----------|
| **ALL-in-ALL ReSearching Workflow Skill** | Prompt Skill 集合 | 开源社区 | 2025 (v4: 2026.05) | 从论文阅读到论文表达的一体式科研 workflow skill 集合 |
| **ARS (Academic Research Skills)** | Claude Code Plugin | Edward Cheng-I Wu | 2026.02 | 32-agent 全流程学术研究技能包（Deep Research + Paper + Review + Pipeline） |
| **DeepScientist** | 全自主科研系统 | 西湖大学 (ICLR 2026) | 2026.05 | 贝叶斯优化驱动的目标导向全自主科学发现 |
| **AI-Researcher** | 全自主科研系统 | 港大 HKUDS (NeurIPS 2025) | 2025.09 | 端到端自主科研：文献→构思→实验→论文 |
| **SciDER** | 数据驱动科研系统 | William & Mary 等 | 2026.03 | 以数据为核心的端到端科研自动化（4 sub-agent） |
| **Supervisor-Skills** | AI 科研副导师 | 港科大 HKUSTDial | 2026.04 | 博导十年经验炼化的 7 个 AI 科研技能 |
| **Paperguide.ai** | SaaS 平台 | Paperguide (前 ChatWithPDF) | 2024 | 一站式 AI 研究助手：搜索、综述、写作、文献管理 |
| **PaperOrchestra** | Multi-Agent 框架 | Google Cloud AI Research | 2026.04 | 从非结构化材料自动生成投稿级 LaTeX 论文 |
| **AI Scientist-v2** | 端到端自主科研系统 | Sakana AI / Oxford / UBC (Nature 2026.03) | 2025.04 | 全生命周期自动化科研：假设→实验→论文→评审 |
| **CycleResearcher** | RL 训练的开源模型 | 西湖大学 (ICLR 2025) | 2024.11 | 基于强化学习的自动化研究-评审循环 |
| **AutoSurvey2** | 综述生成流水线 | 学术研究 | 2025.10 | 多阶段自动化综述论文生成 |
| **LiRA** | Multi-Agent 综述框架 | 学术研究 | 2025 | 可靠可读的文献综述多智能体生成 |
| **Google AI Co-Scientist** | 多智能体假设生成 | Google Research | 2025.02 | 科学假设发现与验证（非写作工具） |
| **Elicit** | SaaS 研究助手 | Ought Inc. | 2023+ | 学术论文搜索、数据提取、文献综述 |
| **SciSpace** | SaaS 研究平台 | Typeset.io | 2023+ | AI PDF 阅读、Deep Review、自定义 Agent |

---

## 二、核心功能维度比对图

### 2.1 功能覆盖矩阵（v4 更新）

```
                        我v4  ARS  DeepSci  AI-Res  SciDER  SupvSk  Paper  PaperOrch  AISci-v2  CycleRes  AutoSur2  LiRA  Co-Sci  Elicit  SciSpace
                        ────  ───  ───────  ──────  ──────  ──────  ─────  ─────────  ────────  ────────  ────────  ────  ──────  ──────  ────────
文献搜索/发现            ○     ●      ●       ●       ●       ○       ●       ●         ●         ○         ●       ●      ●       ●       ●
文献综述生成             ●     ●      ○       ●       ○       ○       ●       ●         ○         ○         ●       ●      ○       ○       ●
论文深度阅读             ●     ○      ○       ○       ○       ○       ●       ○         ○         ○         ○       ○      ○       ○       ●
选题/构思/Ideation       ●     ○      ●       ●       ○       ●       ○       ○         ●         ○         ○       ○      ●       ○       ○
实验设计                 ●     ○      ●       ●       ●       ○       ○       ○         ●         ○         ○       ○      ○       ○       ○
实验自动执行             ○     ○      ●       ●       ●       ○       ○       ○         ●         ○         ○       ○      ○       ○       ○
科研绘图                 ●     ○      ○       ○       ○       ●       ○       ●         ●         ○         ○       ○      ○       ○       ○
概念示意图生成           ●     ○      ○       ○       ○       ○       ○       ●         ○         ○         ○       ○      ○       ○       ○
论文写作(骨架→初稿)      ●     ●      ○       ●       ○       ●       ●       ●         ●         ●         ○       ○      ○       ○       ○
学术润色/翻译            ●     ○      ○       ○       ○       ○       ●       ○         ○         ○         ○       ○      ○       ○       ○
审稿检查/模拟评审        ●     ●      ○       ○       ○       ●       ○       ●         ●         ●         ○       ○      ○       ○       ○
引用验证/API 验证        ●     ●      ○       ○       ○       ○       ○       ●         ●         ○         ○       ●      ○       ○       ○
参考文献管理             ○     ○      ○       ○       ○       ○       ●       ○         ○         ○         ○       ○      ○       ●       ○
PDF 对话/交互阅读        ○     ○      ○       ○       ○       ○       ●       ○         ○         ○         ○       ○      ○       ○       ●
查重/Plagiarism          ○     ○      ○       ○       ○       ○       ●       ○         ○         ○         ○       ○      ○       ○       ○
Deep Research 报告       ●     ●      ○       ○       ○       ○       ●       ○         ○         ○         ○       ○      ○       ○       ○
假设发现/验证            ○     ○      ●       ○       ○       ○       ○       ○         ○         ○         ○       ○      ●       ○       ○
LaTeX 全自动输出         ○     ●      ○       ●       ○       ○       ○       ●         ●         ●         ○       ○      ○       ○       ○
正反辩论机制             ●     ○      ○       ○       ○       ○       ○       ○         ○         ○         ○       ○      ●       ○       ○
评审+回滚机制            ●     ●      ○       ○       ○       ○       ○       ●         ○         ○         ○       ○      ○       ○       ○
并行写作                 ●     ○      ○       ○       ○       ○       ○       ●         ○         ○         ●       ○      ○       ○       ○
VLM 图表审查             ●     ●      ○       ○       ○       ○       ○       ●         ●         ○         ○       ○      ○       ○       ○
完整性闸门               ●     ●      ○       ○       ○       ○       ○       ○         ○         ○         ○       ○      ○       ○       ○
反谄媚协议               ●     ●      ○       ○       ○       ○       ○       ○         ○         ○         ○       ○      ○       ○       ○
风格校准                 ●     ●      ○       ○       ○       ○       ○       ○         ○         ○         ○       ○      ○       ○       ○
产物溯源                 ●     ●      ○       ○       ○       ○       ○       ○         ○         ○         ○       ○      ○       ○       ○
合规检查                 ●     ●      ○       ○       ○       ○       ○       ○         ○         ○         ○       ○      ○       ○       ○
五维构思框架             ●     ○      ○       ○       ○       ●       ○       ○         ○         ○         ○       ○      ○       ○       ○
Introduction Flowchart   ●     ○      ○       ○       ○       ●       ○       ○         ○         ○         ○       ○      ○       ○       ○
开源                     ●     ●      ●       ●       ●       ●       ○       ○         ●         ●         ●       ●      ○       ○       ○
Human-in-the-loop        ●     ●      ○       ○       ○       ●       ●       ○         ○         ○         ○       ○      ●       ●       ●

● = 原生支持   ○ = 不支持或不作为核心功能
```

### 2.2 性能与关键指标比对

| 指标 | 我们 v4 | ARS | DeepScientist | AI-Researcher | PaperOrchestra | AI Scientist-v2 |
|------|--------|-----|---------------|---------------|----------------|-----------------|
| **论文数据库** | 无内置 | Semantic Scholar API | Research Graph | 多源搜索 | Semantic Scholar API | Semantic Scholar API |
| **引用验证** | API+LLM降级 | API (Levenshtein≥0.70) | 无 | 无 | API双重验证 | Semantic Scholar验证 |
| **Agent 数量** | N/A (Prompt Skill) | 32 agents | 多智能体 | 5+ agents | 5 agents | 4阶段 Agentic |
| **生成速度** | 人工节奏 | ~$4-6/1.5万字 | 月级(5000 ideas) | 数小时-数天 | 39.6分钟/篇 | 35.1分钟/篇 |
| **评审质量** | 多角度+回滚 | 5人评审+DA(0-100分) | 无 | 无 | AgentReview 模拟评审 | 自动评审 69%准确率 |
| **完整性检查** | 7项AI失败模式清单 | 7项AI失败模式清单 | 无 | 无 | 无 | 无 |
| **定价** | 免费开源 | API成本$4-6/篇 | 需GPU集群 | 需GPU+API | 需自部署 API | 需自部署 API |

### 2.3 架构模式比对

| 维度 | 我们 v4 | ARS | DeepScientist | AI-Researcher | SciDER | PaperOrchestra |
|------|--------|-----|---------------|---------------|--------|----------------|
| **架构** | Prompt Skill 链 | 32-Agent Pipeline | 贝叶斯优化+多智能体 | 3阶段 Agentic | 4 sub-agent | 5-Agent 流水线 |
| **输入** | 自然语言指令 | 研究主题/初稿 | 目标函数+基线 | 研究方向/参考论文 | 原始数据+主题 | 想法+实验日志 |
| **输出** | Markdown 笔记/草稿 | Markdown/DOCX/LaTeX/PDF | LaTeX→PDF | LaTeX→PDF | 论文文本+代码 | LaTeX→PDF |
| **自动化程度** | 半自动(HITL) | 半自动(HITL) | 全自动 | 全自动 | 全自动 | 全自动 |
| **可定制性** | 高(Prompt可改) | 中(Prompt可改) | 低(需改代码) | 中(需改代码) | 中(Python包) | 中(需改代码) |
| **部署方式** | 本地+AI编码工具 | Claude Code / Codex | 本地+GPU集群 | 本地+GPU | 本地+API | 本地/API |
| **依赖** | AI编码工具 | Claude Code | LLM API + GPU | LLM API + GPU + Docker | LangGraph + litellm | LLM API + LaTeX |

---

## 三、各工具深度分析

### 3.1 ARS (Academic Research Skills) — 新增

**核心优势：**
- **32 个专业化 Agent**，4 大团队分工：Deep Research (13 agents) + Academic Paper (12 agents) + Academic Paper Reviewer (7 agents) + Academic Pipeline (编排器)
- **10 阶段流水线**：Research → Write → Integrity Check → Review (5人) → Socratic Coaching → Revise → Re-Review → Re-Revise → Final Integrity Check → Finalize
- **Semantic Scholar API 引用核验**：Levenshtein 相似度 ≥ 0.70 模糊匹配，杜绝编造引用
- **7 项 AI 失败模式清单**（源自 Nature 研究）：引用幻觉、数据捏造等方法论造假检测，Stage 2.5 和 4.5 强制闸门
- **反谄媚协议**：魔鬼代言人评分 < 4 时，写作团队不轻易让步
- **三层数据隔离**：原始输入(不可信) / 验证后产物 / 评分标准，防止 AI 偷看答案
- **风格校准 (Style Calibration)**：学习用户过往写作风格，减少 AI 味
- **协作深度观察器**：评估人机协作质量的 4 维度打分
- **Compliance Agent**：PRISMA-trAIce 17 项 + RAISE 4 原则合规检查
- **VLM 图表验证**：视觉语言模型闭环验证图表质量
- **Material Passport**：产物溯源链，记录每段内容的生成来源
- **GitHub 6.4k stars**，活跃迭代（380+ commits）

**不足：**
- 强绑定 Claude Code / Codex CLI，不支持其他 AI 编码工具
- 无实验自动执行能力
- 无选题构思/Ideation 能力
- 无科研绘图能力（依赖外部工具）
- 无 Deep Research 报告的趋势分析
- 无正反辩论机制
- 闭源核心逻辑（Plugin 格式），用户无法自由修改 Agent 行为

**可学习模块：**
- ✅ **7 项 AI 失败模式清单**：完整性闸门机制，在关键阶段强制检查 AI 常见失败模式
- ✅ **反谄媚协议**：防止 AI 为讨好用户而降低批评强度
- ✅ **风格校准**：学习用户写作风格，减少 AI 味
- ✅ **Material Passport 产物溯源**：记录每段内容的生成来源和验证状态
- ✅ **Compliance Agent 合规检查**：PRISMA-trAIce + RAISE 系统综述合规

### 3.2 DeepScientist — 新增

**核心优势：**
- **ICLR 2026 正会论文**，西湖大学 + 浙大
- **贝叶斯优化驱动**：将科学发现建模为贝叶斯优化问题，智能平衡探索与利用
- **Findings Memory 科研长程记忆**：累积发现记忆，跨实验迭代优化
- **三阶段探索周期**：策略与假设 → 实施与验证 → 分析与报告
- **大规模验证**：5000+ 独特想法，1100+ 实验验证，21 个科学创新
- **超越人类 SOTA**：在 3 个前沿 AI 任务上分别提升 183.7%、1.9%、7.9%
- **2 周完成 3 年人类研究进度**（AI 文本检测任务）
- **7500+ 注册用户**，来自数百所高校与研究机构
- **20,000+ GPU 小时**消耗，目标导向的长期自主发现

**不足：**
- 需要大量 GPU 资源（16×H800，月级运行）
- 面向 AI 领域科研，通用性待验证
- 无 Human-in-the-loop 检查点
- 无写作润色、绘图、审稿检查能力
- 专注于实验发现，不覆盖论文写作全流程
- 伦理争议大（AI 自主科研的学术诚信问题）

**可学习模块：**
- ✅ **Findings Memory 科研长程记忆**：跨实验迭代的知识积累和复用机制
- ✅ **贝叶斯优化实验策略**：将实验探索建模为优化问题，智能分配资源
- ✅ **分层验证机制**：低成本替代模型预筛 → 高保真验证 → 深度分析

### 3.3 AI-Researcher (HKUDS) — 新增

**核心优势：**
- **NeurIPS 2025 正会论文**，港大 HKUDS
- **3 阶段自主科研**：Literature Review & Idea Generation → Algorithm Design, Implementation & Validation → Automated Scientific Documentation
- **5+ 专业化 Agent**：Knowledge Acquisition → Resource Filter → Idea Generator → Algorithm Designer → Writer Agent
- **Scientist-Bench 评测基准**：涵盖 CV、NLP、Data Mining、IR 的综合评测
- **GitHub 5.2k stars**
- **生产就绪版本**：novix.science/chat
- 支持多种 LLM 后端（Claude, OpenAI, Deepseek, Gemini 等）

**不足：**
- 需 GPU + Docker 沙箱环境
- 无 Human-in-the-loop 检查点
- 无绘图、润色、审稿检查能力
- 文献综述质量有限
- 与自身实验流水线强耦合

**可学习模块：**
- ✅ **Knowledge Acquisition Agent**：系统性文献采集和代码仓库搜索
- ✅ **Idea Generator**：基于文献分析自动生成研究假设
- ✅ **Scientist-Bench 评测思路**：构建标准化评测基准评估科研工具质量

### 3.4 SciDER — 新增

**核心优势：**
- **数据驱动**：以原始实验数据为核心输入，非仅文本描述
- **4 个 sub-agent**：Ideation Agent → Data Analysis Agent → Experimentation Agent → Critic Agent
- **自进化记忆机制**：短期(任务级) + 长期(项目级) 记忆，RAG 检索
- **Critic-led 反馈循环**：评判 Agent 审查所有输出并提出改进
- **跨领域**：物理、化学、生物、数学等多学科
- **PyPI 包**：`pip install scider`，轻量 Web 界面
- 在 AI-Idea-Bench、MLEBench、SciCode 上超越通用 Agent

**不足：**
- 面向有实验数据的科研场景，不适用于纯理论/综述
- 无写作、绘图、审稿检查能力
- 无 Human-in-the-loop 检查点
- 依赖 LangGraph + litellm

**可学习模块：**
- ✅ **Data Analysis Agent**：自动清洗、结构化、分析原始实验数据
- ✅ **自进化记忆机制**：短期+长期记忆 + RAG 检索，跨任务知识积累
- ✅ **Critic Agent 反馈循环**：独立评判 Agent 审查所有输出

### 3.5 Supervisor-Skills — 新增

**核心优势：**
- **博导经验蒸馏**：基于十年 SIGMOD/VLDB/ICML/NeurIPS 审稿与发表经验
- **7 个可直接调用的 AI 技能**：Idea Evaluator、Introduction Drafter、Tech Paper Template、Benchmark Paper Template、Figure Design Advisor、Pre-Submission Reviewer、Vibe Research Guide
- **双轨制架构**：Handbook (6章系统指南) + Skills (7个可执行技能)
- **顶会案例教学**：3 篇真实顶会论文逐层剖析写作思路
- **Introduction Flowchart 思考模型**：结构化引言写作指导
- **"更高更快更强更省更广"五维构思框架**
- **GitHub 543+ stars**

**不足：**
- 无文献综述自动生成
- 无引用验证
- 无 Deep Research
- 无实验设计/执行
- 无并行写作
- 技能覆盖面较窄，偏写作指导

**可学习模块：**
- ✅ **Introduction Flowchart 思考模型**：结构化引言写作指导
- ✅ **五维构思框架**：更高/更快/更强/更省/更广的 Idea 评估维度
- ✅ **Figure Design Advisor**：动机图/总览图/实验图的设计范式
- ✅ **Pre-Submission Reviewer**：基于写作 Checklist 和英语语法易错点的投稿前审查

### 3.6 Paperguide.ai

**核心优势：**
- 一站式平台：搜索→综述→写作→管理全链路覆盖
- 2亿+论文数据库，全文分析（非仅摘要）
- Workbooks 模块：可从多论文中提取结构化数据，生成对比表（最多50列）
- Deep Research：自动发现、筛选、提取，生成综合报告
- AI Writer：基于参考文献库自动生成带引用的草稿
- SJR/SNIP 期刊质量指标
- 团队协作（共享文件夹、实时标注）
- 查重检测

**不足：**
- 闭源 SaaS，无法本地部署
- 综述深度有限，偏向快速提取而非深层分析
- 无实验设计、选题构思能力
- 无概念示意图生成
- 引用无 API 级验证，存在幻觉风险

**可学习模块（v4 已实现）：**
- ✅ Workbooks 结构化数据提取 → 已实现 `workbooks_extraction.md`
- ✅ Deep Research Report → 已实现 `deep-research` skill
- ✅ SJR/SNIP 期刊质量信号 → 已实现 Stage 4.5

### 3.7 PaperOrchestra

**核心优势：**
- 5个专业化 Agent 分工协作：Outline → Plotting/LitReview → SectionWriting → Refinement
- 接受非结构化输入（想法摘要 + 实验日志），无需模板
- **API 级引用验证**：LLM搜索 + Semantic Scholar API 双重验证，消除引用幻觉
- **PaperBanana 概念示意图生成**：VLM 闭环优化，反复检查直到满意
- **AgentReview 模拟评审**：模拟同行评审，仅接受总分提升的修改（版本控制）
- PaperWritingBench 标准化评测基准（200篇顶会论文）
- 文献综述质量显著优于 baseline（+50-68% 胜率）

**不足：**
- 需要大量 LLM API 调用（60-70次/篇）
- 无选题构思、实验设计能力
- 无 Human-in-the-loop 检查点
- 依赖 LaTeX 编译环境
- 仅覆盖写作环节，不涉及科研前端

**可学习模块（v4 已实现）：**
- ✅ 结构化 JSON 大纲 → 已实现 scholarly-writing Stage 2
- ✅ API 级引用验证 → 已实现 literature-review Stage 3.5
- ✅ VLM 闭环图表优化 → 已实现 scientific-figure-making Stage 3
- ✅ AgentReview 评审+回滚 → 已实现 reviewer_check 第三部分
- ✅ 概念示意图生成 → 已实现 `concept_diagram.md`

### 3.8 AI Scientist-v2

**核心优势：**
- **端到端全生命周期**：Ideation → Experiment → Writing → Review 完整闭环
- **Agentic Tree Search**：并行化实验探索（初步调查→超参调优→核心实验→消融），非简单线性
- 无模板模式（v2），可对广泛研究主题自主探索
- VLM 审查图表：检查坐标轴、图例、图文一致性
- 自动评审器：平衡准确率 69%，超越人类评审员间一致性
- **首篇 AI 生成论文通过 ICLR 双盲评审**（6.33分），发表于 Nature

**不足：**
- 与自身实验流水线强耦合，无法作为独立写作工具
- 文献综述质量较弱（简单关键词搜索，引用不足）
- 无概念示意图生成
- 需 GPU + Docker 沙箱环境
- 成功率有限（3篇投稿仅1篇过审）
- 伦理争议大

**可学习模块（v4 部分实现）：**
- ✅ VLM 图表审查 → 已实现
- ✅ 5份独立评审 + AC Meta-review → 已实现多角度评审
- ⬜ Agentic Tree Search 实验模式 → 未实现
- ⬜ Debug 分支机制 → 未实现

### 3.9 CycleResearcher

**核心优势：**
- **开源模型**（7B/72B/123B），可本地部署
- 强化学习训练（SimPO），研究-评审循环自改进
- CycleReviewer 评审准确率超越人类个体评审员（MAE↓26.89%）
- 生成论文模拟评分 5.36，超过人类预印本水平 5.24
- Research-14K / Review-5K 数据集开源

**不足：**
- 需要 GPU 部署大模型
- 论文质量仍低于人类已接收水平（5.69）
- 无实验执行能力
- 无图表生成
- 文献综述能力有限

**可学习模块（v4 部分实现）：**
- ✅ 研究-评审迭代循环 → 已实现评审+回滚机制
- ⬜ SimPO 偏好优化 → 不适用（我们是 Prompt Skill，非模型训练）

### 3.10 AutoSurvey2 / LiRA

**核心优势：**
- AutoSurvey2：多阶段综述生成流水线，并行章节生成 + 迭代精炼 + 实时检索
- LiRA：多智能体文献综述，引用接地（citation grounding）防幻觉
- 结构化评估框架（Coverage, Structure, Relevance）

**不足：**
- 仅生成综述，无法产出完整研究论文
- 无实验设计、选题、绘图能力

**可学习模块（v4 已实现）：**
- ✅ 并行章节生成 → 已实现 scholarly-writing Stage 3.5
- ✅ 引用接地机制 → 已实现 scholarly-writing Stage 2.5

### 3.11 Google AI Co-Scientist

**核心优势：**
- 6个专业化 Agent：Generation → Reflection → Ranking → Evolution → Proximity → Meta-review
- Generate-Debate-Evolve 循环：假设生成→科学辩论→进化优化
- Test-time compute scaling：推理时动态扩展计算
- **湿实验验证**：肝纤维化靶点、AML 药物再利用、抗菌素耐药性机制
- 2天解决10年科学谜团

**不足：**
- 非写作工具，专注于假设发现
- 闭源，仅 Trusted Tester 可用
- 面向生物医学领域，通用性待验证

**可学习模块（v4 已实现）：**
- ✅ Generate-Debate-Evolve 循环 → 已实现 critical-ideation Stage 3b

---

## 四、综合评分表（v4 更新）

| 维度 (1-5) | 我们 v4 | ARS | DeepScientist | AI-Researcher | SciDER | SupvSkills | Paperguide | PaperOrchestra | AI Sci-v2 | CycleRes |
|------------|---------|-----|---------------|---------------|--------|------------|-----------|----------------|-----------|----------|
| 功能广度 | **5** | 4 | 3 | 4 | 3 | 2 | 4 | 3 | 4 | 2 |
| 易用性 | 4 | 3 | 1 | 1 | 2 | 4 | **5** | 2 | 1 | 2 |
| 自动化程度 | 2 | 3 | **5** | **5** | **5** | 2 | 4 | **5** | **5** | 4 |
| 开源/可定制 | **5** | 3 | **5** | **5** | **5** | **5** | 1 | 2 | 4 | **5** |
| 引用可靠性 | 4 | 4 | 1 | 1 | 1 | 1 | 3 | **5** | 3 | 2 |
| 输出质量 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | **5** | 4 | 3 |
| 科研前端覆盖 | **5** | 2 | **5** | **5** | 4 | 3 | 2 | 1 | **5** | 1 |
| Human-in-the-loop | **5** | **5** | 1 | 1 | 1 | 4 | 4 | 1 | 1 | 1 |
| 安全/完整性保障 | 4 | **5** | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 1 |
| **总分** | **38** | 33 | 26 | 26 | 26 | 26 | 28 | 26 | 28 | 21 |

---

## 五、v4 已实现变更 vs 仍存在差距

### ✅ v4 已实现（对照原 Paper_比对 的改进路线）

| # | 原始差距 | v4 实现 | 来源 |
|---|---------|---------|------|
| 1 | API 级引用验证 | literature-review Stage 3.5: Semantic Scholar API + LLM 降级验证 | PaperOrchestra |
| 2 | 结构化 JSON 大纲 | scholarly-writing Stage 2: JSON 蓝图含可视化计划+文献策略 | PaperOrchestra |
| 3 | 模拟评审+回滚机制 | reviewer_check 第三部分: 基线评分→修改→再评分→仅当提升时接受 | PaperOrchestra |
| 4 | VLM 图表审查闭环 | scientific-figure-making Stage 3: 生成→VLM检查→修正→再检查 | PaperOrchestra / AI Sci-v2 |
| 5 | Workbooks 数据提取 | literature-review 新模板 workbooks_extraction.md | Paperguide |
| 6 | Deep Research Report | 新增 deep-research skill | Paperguide |
| 7 | SJR/SNIP 期刊质量 | literature-review Stage 4.5 | Paperguide |
| 8 | 并行章节写作 | scholarly-writing Stage 3.5 | AutoSurvey2 |
| 9 | Generate-Debate-Evolve | critical-ideation Stage 3b | Google AI Co-Scientist |
| 10 | 引用接地校验 | scholarly-writing Stage 2.5 | LiRA |
| 11 | 概念示意图生成 | scientific-figure-making 新模板 concept_diagram.md | PaperOrchestra |
| 12 | 多角度评审 | reviewer_check 第二部分: 5角色独立评审 + AC Meta-review | AI Scientist-v2 |

### ⬜ 仍存在差距（基于 2026.05 最新比对）

| # | 差距 | 来源 | 优先级 | 实现难度 | 状态 |
|---|------|------|--------|---------|------|
| 1 | **7项AI失败模式清单 / 完整性闸门** | ARS | 🔴 高 | 低（Prompt 增强） | ✅ 已实现 |
| 2 | **反谄媚协议** | ARS | 🔴 高 | 低（Prompt 增强） | ✅ 已实现 |
| 3 | **风格校准 (Style Calibration)** | ARS | 🟡 中 | 中（需参考文本分析） | ✅ 已实现 |
| 4 | **Material Passport 产物溯源** | ARS | 🟡 中 | 中（需输出格式规范） | ✅ 已实现 |
| 5 | **Compliance Agent 合规检查** | ARS | 🟢 低 | 中（PRISMA-trAIce 规则） | ✅ 已实现 |
| 6 | **Findings Memory 科研长程记忆** | DeepScientist | 🟡 中 | 高（需持久化存储） | ⬜ 未实现 |
| 7 | **Introduction Flowchart 思考模型** | Supervisor-Skills | 🟡 中 | 低（Prompt 增强） | ✅ 已实现 |
| 8 | **五维构思框架** | Supervisor-Skills | 🟢 低 | 低（已有类似机制） | ✅ 已实现 |
| 9 | **Agentic Tree Search 实验模式** | AI Scientist-v2 | 🟢 低 | 高（需代码执行环境） | ⬜ 未实现 |
| 10 | **Data Analysis Agent** | SciDER | 🟢 低 | 高（需代码执行环境） | ⬜ 未实现 |

---

## 六、我们的差异化优势（v4 更新）

| 优势 | 说明 |
|------|------|
| **全链路覆盖** | 唯一覆盖 综述→阅读→选题→实验设计→绘图→写作→润色→审稿→深度研究 完整链条的 Prompt Skill 工具 |
| **Critical Ideation 原创能力** | 主动质疑、正反辩论、竞品检索、方向重构、MVP 收敛——含 Generate-Debate-Evolve 循环和五维构思框架 |
| **Human-in-the-loop 设计** | 每个环节都保留人类决策权，避免全自动化的伦理风险和质量失控 |
| **Prompt Skill 架构** | 轻量、可组合、可替换，不依赖特定模型或 API，不绑定特定 AI 编码工具 |
| **开源免费** | MIT 协议，无使用成本，可自由定制 |
| **AI 编码工具原生集成** | 专为 Trae / Codex 等 AI 编码工具设计，无缝融入开发者工作流 |
| **渐进式采用** | 可单独使用任意 Skill，也可串联完整 Workflow |
| **引用验证双模式** | API 验证 + LLM 降级验证，确保引用可靠性 |
| **评审+回滚机制** | 仅当总分提升时接受修改，防止修改导致质量退化 |
| **VLM 图表审查** | 生成→VLM检查→修正→再检查的闭环质量保障 |
| **完整性闸门** | 7项AI失败模式清单，关键阶段强制检查 |
| **反谄媚协议** | 魔鬼代言人机制，防止AI降低批评强度 |
| **风格校准** | 学习用户写作风格，减少AI味 |
| **Material Passport** | 产物溯源链，记录每段内容生成来源和验证状态 |
| **Introduction Flowchart** | 结构化引言写作流程图模型 |
| **合规检查** | PRISMA-trAIce 17项 + RAISE 4原则系统综述合规 |

### vs ARS 的差异化

| 维度 | 我们 | ARS |
|------|------|-----|
| 工具绑定 | 不绑定特定 AI 编码工具 | 强绑定 Claude Code / Codex |
| 选题构思 | ✅ Critical Ideation + 辩论 + 五维框架 | ❌ 无 |
| 科研绘图 | ✅ matplotlib + VLM 审查 | ❌ 无 |
| Deep Research | ✅ 趋势分析+综合报告 | ✅ 13-agent 文献调研 |
| 完整性闸门 | ✅ 7项AI失败模式清单 | ✅ 7项AI失败模式清单 |
| 反谄媚协议 | ✅ 魔鬼代言人机制 | ✅ 魔鬼代言人机制 |
| 风格校准 | ✅ 学习用户写作风格 | ✅ 学习用户写作风格 |
| 产物溯源 | ✅ Material Passport | ✅ Material Passport |
| 合规检查 | ✅ PRISMA-trAIce + RAISE | ✅ PRISMA-trAIce + RAISE |
| 正反辩论 | ✅ Generate-Debate-Evolve | ❌ 无 |
| 实验设计 | ✅ experiment-design skill | ❌ 无 |
| 五维构思 | ✅ 更高/更快/更强/更省/更广 | ❌ 无 |
| Introduction Flowchart | ✅ 结构化引言流程图 | ❌ 无 |

---

## 七、改进路线建议（v4 更新）

```
Phase 1 (核心质量提升) ✅ 已完成
├── ✅ 引入 API 级引用验证 (Semantic Scholar API)
├── ✅ 增强大纲生成为结构化 JSON 蓝图
├── ✅ 强化 reviewer_check 为评审+回滚机制
├── ✅ 增加 VLM 图表审查闭环
├── ✅ 新增 Workbooks 多论文数据提取模板
├── ✅ 新增 Deep Research Report 模式
├── ✅ 引入 SJR/SNIP 期刊质量信号
├── ✅ 增强 critical-ideation 辩论机制
├── ✅ 增加引用接地校验
├── ✅ 概念示意图自动生成
├── ✅ 并行章节写作模式
└── ✅ 多角度评审 + AC Meta-review

Phase 2 (安全与完整性) ✅ 已完成
├── ✅ 7项AI失败模式清单 + 完整性闸门 (参考 ARS)
├── ✅ 反谄媚协议 (参考 ARS)
├── ✅ 风格校准 (参考 ARS)
├── ✅ Material Passport 产物溯源 (参考 ARS)
├── ✅ Compliance Agent 合规检查 (参考 ARS PRISMA-trAIce)
├── ✅ Introduction Flowchart 思考模型 (参考 Supervisor-Skills)
└── ✅ 五维构思框架 (参考 Supervisor-Skills)

Phase 3 (生态扩展) ← 下一步
├── Findings Memory 科研长程记忆 (参考 DeepScientist)
├── Agentic Tree Search 实验模式 (参考 AI Scientist-v2)
├── Data Analysis Agent (参考 SciDER)
├── PDF 对话式阅读模式
└── 参考文献管理集成
```

---

## 八、参考来源

| 工具 | 链接 |
|------|------|
| ARS (Academic Research Skills) | https://github.com/Imbad0202/academic-research-skills |
| DeepScientist | https://github.com/ResearAI/DeepScientist |
| AI-Researcher (HKUDS) | https://github.com/HKUDS/AI-Researcher |
| SciDER | https://github.com/leonardodalinky/SciDER |
| Supervisor-Skills | https://github.com/HKUSTDial/Supervisor-Skills |
| Paperguide.ai | https://paperguide.ai/ |
| PaperOrchestra | https://arxiv.org/abs/2604.05018 |
| AI Scientist-v2 | https://github.com/SakanaAI/AI-Scientist-v2 |
| CycleResearcher | https://wengsyx.github.io/Researcher |
| AutoSurvey2 | https://arxiv.org/abs/2510.26012 |
| LiRA | https://arxiv.org/abs/2510.05138 |
| Google AI Co-Scientist | https://arxiv.org/abs/2502.18864 |
| Elicit | https://elicit.com/ |
| SciSpace | https://typeset.io/ |
