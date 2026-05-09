下面是专门用于构建第三个核心 skill：`critical-ideation`。

````
# BUILD_skill3.md

# Critical Ideation Skill 构建指南

本文件用于在 `DION-AI-Research-Toolkit` 中构建第三个核心 Skill：

```text
skills/critical-ideation/

````

该 Skill 的目标不是普通头脑风暴，而是：

```
Brainstorm
→ 主动质疑
→ 检索已有方案
→ 判断新颖性与可行性
→ 重构 idea
→ 给出可执行 MVP

```

适用于：

- 科研选题 brainstorm
- 产品 idea 生成
- PRD 创新点优化
- Agent workflow 设计
- GitHub 项目差异化
- 竞品调研
- 论文 novelty 检查
- 自媒体选题策划
- 创业方向初筛

***

## 1. Skill 定位

`critical-ideation` 是一个 **Critic + Search + Ideation** 型 Skill。

它和普通 brainstorm 的区别：

类型

特点

问题

普通 brainstorm

快速发散，给很多点子

容易空泛、重复、缺少验证

Research ideation

偏科研 idea 生成

不一定适合产品/项目

Product brainstorming

偏产品功能发散

可能缺少证据检索

Critical Ideation

生成 idea + 主动质疑 + 检索 + 重构 + 排序

更适合真实项目决策

核心原则：

```
不要只鼓励用户。
不要把弱 idea 包装成好 idea。
不要只给方向，要给验证路径。
不要只发散，要收敛到可执行方案。

```

***

## 2. 推荐目录结构

在工具库根目录下创建：

```
DION-AI-Research-Toolkit/
├── skills/
│   ├── scientific-figure-making/
│   └── critical-ideation/
│       ├── SKILL.md
│       ├── templates/
│       │   ├── idea_card.md
│       │   ├── search_log.md
│       │   ├── decision_matrix.md
│       │   ├── critique_checklist.md
│       │   └── mvp_plan.md
│       └── examples/
│           ├── product_ideation_example.md
│           ├── research_ideation_example.md
│           └── agent_workflow_ideation_example.md

```

创建命令：

### Windows PowerShell

```
mkdir skills\critical-ideation
mkdir skills\critical-ideation\templates
mkdir skills\critical-ideation\examples

```

### WSL / Linux / macOS

```
mkdir -p skills/critical-ideation/templates
mkdir -p skills/critical-ideation/examples

```

***

## 3. 创建核心文件：`SKILL.md`

文件位置：

```
skills/critical-ideation/SKILL.md

```

内容如下：

````
# Critical Ideation Skill

## Purpose

Use this skill when the user wants to brainstorm ideas, research directions, product concepts, paper topics, PRD improvements, startup ideas, agent workflows, project differentiation strategies, or self-media content directions.

This skill is not a free-association brainstorming tool. It must actively challenge assumptions, search for existing work when possible, compare alternatives, and refine ideas based on evidence.

The goal is to help the user move from vague ideas to evidence-aware, critic-tested, executable directions.

---

## When to Use

Use this skill when the user asks for:

- brainstorm ideas
- brainstorm research directions
- 找 idea
- 选题构思
- 产品差异化
- 项目创新点
- paper idea
- research direction
- startup idea
- PRD optimization
- 竞品对比
- 项目方向判断
- “有没有更好的方向”
- “这个想法是否可行”
- “帮我质疑一下这个 idea”
- “积极检索内容”
- “帮我看看是不是已经有人做过”
- “帮我找更有差异化的切入点”

---

## Do Not Use For

Do not use this skill for:

- simple text polishing
- ordinary translation
- purely emotional support
- deterministic coding tasks
- ordinary figure generation
- pure summarization without ideation
- tasks where the user only wants direct execution and not idea evaluation

For writing tasks, use the academic writing prompt library.

For figure tasks, use the scientific figure making skill.

For rebuttal tasks, use the rebuttal workflow tool if available.

---

## Core Workflow

### Stage 1: Clarify the Ideation Target

Identify:

- Domain
- User goal
- Target audience
- Current idea
- User constraints
- Available resources
- Technical capacity
- Time horizon
- Expected output type
- Success criteria

If the user has already provided enough context, do not ask follow-up questions. Proceed with reasonable assumptions and mark them clearly.

Output:

```text
Problem Framing
- Domain:
- Goal:
- Target user / reader:
- Constraints:
- Available resources:
- Success criteria:
- Assumptions:

````

***

### Stage 2: Generate Initial Ideas

Generate 5–10 candidate ideas.

Each idea must include:

- Idea name
- One-sentence concept
- Target user / problem
- Why now
- Core mechanism
- Expected value
- Minimum viable version

Avoid vague names like “AI Assistant” or “Smart Platform.” Use specific, testable concepts.

***

### Stage 3: Adversarial Critique

For each idea, challenge it directly.

Critique from at least five angles:

1. Novelty risk\
   Has this already been done?
2. Feasibility risk\
   Can the user realistically build it with current resources?
3. Data/resource risk\
   Does it require unavailable data, compute, permissions, users, or APIs?
4. Differentiation risk\
   Why would anyone choose this over existing tools or methods?
5. Evaluation risk\
   How can success be measured?
6. Research/publication risk\
   If it is a research idea, is there enough novelty and experimental support?
7. Business/monetization risk\
   If it is a product idea, is there a real user pain point and payment scenario?
8. Legal/platform risk\
   Does it rely on scraping, copyrighted data, platform automation, privacy-sensitive information, or restricted APIs?
9. Demo risk\
   Can a clear demo be built quickly?

Do not be overly polite. If the idea is weak, say so.

***

### Stage 4: Evidence Search

When current information, competitors, papers, tools, policies, products, benchmarks, GitHub repos, market conditions, or platform rules matter, perform web search.

Search for:

- Existing products
- GitHub repositories
- Recent papers
- Benchmark datasets
- Blog posts
- Open-source demos
- Commercial competitors
- Similar startups
- Platform restrictions
- Legal or policy constraints

For each relevant source, extract:

- What already exists
- What gap remains
- What can be borrowed
- What should be avoided
- Whether the user’s idea still has room for differentiation

Important rule:

Never claim that something was searched unless actual search was performed.

If search is unavailable, say:

```
Search was not performed. The following judgment is based on internal reasoning and may miss recent work.

```

***

### Stage 5: Refine Ideas

Revise the best ideas after critique and evidence search.

Each refined idea must include:

- Improved positioning
- Unique angle
- MVP scope
- Technical path
- Data path
- Evaluation method
- Main risk
- Next concrete action

The refined idea should be narrower, more testable, and more differentiated than the initial version.

***

### Stage 6: Rank and Decide

Score each idea from 1–5 on:

- Novelty
- Feasibility
- User value
- Differentiation
- Demonstrability
- Research or business potential
- Fit with the user’s background and resources

Then classify each idea as:

- Build now
- Keep as backup
- Needs more research
- Drop

Do not recommend more than 3 top ideas unless the user explicitly asks for a longer list.

***

## Output Format

Use this structure by default:

```
# Critical Ideation Report

## 1. Problem Framing

## 2. Initial Idea List

## 3. Evidence Search Findings

## 4. Critical Objections

## 5. Refined Ideas

## 6. Ranking Matrix

## 7. Recommended Top Ideas

## 8. MVP Execution Plan

## 9. Risks and Unknowns

## 10. Next Actions

```

***

## Style Rules

- Be direct.
- Do not flatter weak ideas.
- Prefer mechanisms over slogans.
- Separate assumptions from evidence.
- Separate speculation from search findings.
- Mark uncertainty clearly.
- Give executable next steps.
- Prioritize ideas the user can actually prototype.
- Do not invent sources, competitors, papers, or market facts.
- If an idea is not worth building, say so.
- If an idea is promising but too broad, narrow it.
- If an idea is already common, find a more specific angle.

***

## Default Priorities

When evaluating ideas for this user, prefer:

1. Ideas that can be prototyped within days or weeks.
2. Ideas that can become GitHub projects, demos, PRDs, papers, or self-media content.
3. Ideas that leverage LLM, Agent, VLM, embodied AI, research workflow, or academic productivity.
4. Ideas that do not require huge compute, inaccessible private data, or complex business licensing.
5. Ideas that can produce a visible artifact:
   - demo
   - benchmark
   - paper draft
   - PRD
   - GitHub repo
   - video
   - experimental figure
   - workflow template

***

## Common Task Modes

### Mode A: Research Idea Brainstorm

Use when the user wants academic research directions.

Extra criteria:

- Literature novelty
- Dataset availability
- Evaluation method
- Compute requirement
- Publication risk
- Baseline feasibility

Output must include:

- Research question
- Hypothesis
- Method sketch
- Dataset / benchmark
- Baseline
- Evaluation metric
- Main novelty risk
- Minimum experiment

***

### Mode B: Product Idea Brainstorm

Use when the user wants product or startup ideas.

Extra criteria:

- Target user
- User pain
- Existing alternatives
- Differentiation
- MVP scope
- Distribution channel
- Monetization possibility
- Legal/platform risk

Output must include:

- User scenario
- Core feature
- MVP
- Competitor comparison
- Demo plan
- Risk

***

### Mode C: Agent Workflow Brainstorm

Use when the user wants to design AI Agent systems.

Extra criteria:

- Agent roles
- Tool calls
- Memory
- Human-in-the-loop points
- Failure modes
- Evaluation harness
- Guardrails
- Cost and latency

Output must include:

- Agent architecture
- Workflow steps
- Required tools
- Input/output schema
- Failure cases
- Evaluation harness
- MVP implementation plan

***

### Mode D: Self-media Topic Brainstorm

Use when the user wants content ideas.

Extra criteria:

- Hook strength
- Audience resonance
- Filming feasibility
- Differentiation from existing content
- Series potential
- Personal brand fit
- Risk of looking generic or forced

Output must include:

- Title
- Opening hook
- Core conflict
- Content structure
- Why audience cares
- Filming plan
- Risk

````

---

## 4. 创建模板：`idea_card.md`

文件位置：

```text
skills/critical-ideation/templates/idea_card.md

````

内容：

```
# Idea Card Template

## Idea Name

## One-sentence Concept

## Target User / Reader

## Pain Point

## Why Now

## Existing Alternatives

## Core Mechanism

## Core Differentiation

## Why This Might Work

## Why This Might Fail

## Required Data / Resources

## MVP Version

## Evaluation Method

## Search Keywords

## Evidence Found

## Main Risks

## Final Judgment

- Build now / Backup / Research more / Drop

```

***

## 5. 创建模板：`search_log.md`

文件位置：

```
skills/critical-ideation/templates/search_log.md

```

内容：

```
# Search Log Template

## Search Objective

What are we trying to verify?

## Search Queries

1. 
2. 
3. 

## Sources Found

| Source | Type | What It Shows | Relevance | Gap |
|---|---|---|---|---|
|  | Paper / GitHub / Product / Blog / Dataset / Policy |  |  |  |

## Existing Solutions

## Similar Products / Projects

## Similar Papers / Methods

## Datasets / Benchmarks

## What Is Already Saturated

## Remaining Opportunity

## Evidence-Based Judgment

## Uncertainties

```

***

## 6. 创建模板：`decision_matrix.md`

文件位置：

```
skills/critical-ideation/templates/decision_matrix.md

```

内容：

```
# Idea Decision Matrix

| Idea | Novelty | Feasibility | User Value | Differentiation | Demo Potential | Research/Business Potential | Fit | Risk | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| Idea A |  |  |  |  |  |  |  |  |  |
| Idea B |  |  |  |  |  |  |  |  |  |
| Idea C |  |  |  |  |  |  |  |  |  |

Scoring:

- 1 = weak
- 2 = below average
- 3 = acceptable
- 4 = strong
- 5 = excellent

Verdict:

- Build now
- Backup
- Research more
- Drop

```

***

## 7. 创建模板：`critique_checklist.md`

文件位置：

```
skills/critical-ideation/templates/critique_checklist.md

```

内容：

```
# Critique Checklist

Use this checklist to attack an idea before recommending it.

## Novelty

- Has this already been done?
- Is the difference real or only cosmetic?
- Is the idea just a wrapper around an existing tool?
- Would a reviewer or user immediately say “this already exists”?

## Feasibility

- Can the user build a working MVP?
- What is the minimum technical path?
- Does it require unavailable compute, data, APIs, or users?
- Is the scope too large?

## Data and Resources

- What data is required?
- Can the data be collected legally and practically?
- Does the idea depend on copyrighted or platform-restricted content?
- Is there a public dataset or benchmark?

## Differentiation

- Why would users choose this?
- What is the unique mechanism?
- Is the positioning narrow enough?
- Can the difference be demonstrated visually or experimentally?

## Evaluation

- What metric proves it works?
- What baseline should be compared?
- Can success be shown in one demo?
- Can failure be diagnosed?

## Risk

- What is the biggest reason this idea may fail?
- What hidden assumption is most dangerous?
- What would make this idea not worth pursuing?

## Final Challenge

If this idea were rejected, what would be the most likely reason?

```

***

## 8. 创建模板：`mvp_plan.md`

文件位置：

```
skills/critical-ideation/templates/mvp_plan.md

```

内容：

```
# MVP Plan Template

## Selected Idea

## MVP Goal

What should the first prototype prove?

## Core User Scenario

## Minimum Feature Set

1. 
2. 
3. 

## Out of Scope

The MVP will not include:

- 
- 
- 

## Technical Architecture

## Required Data

## Required Tools / APIs

## Implementation Steps

### Day 1

### Day 2

### Day 3

### Week 1

## Demo Output

The MVP should produce:

- 
- 
- 

## Evaluation

How to decide whether the MVP works:

| Metric | Target | How to Measure |
|---|---|---|
|  |  |  |

## Main Risks

## Kill Criteria

Stop or pivot if:

- 
- 
- 

```

***

## 9. 添加到总控 `ROUTER.md`

在工具库根目录的 `ROUTER.md` 中加入：

````
## Critical Ideation Skill

Path:

```text
skills/critical-ideation/

````

Use for:

- brainstorming
- research idea generation
- product idea generation
- PRD innovation
- startup idea validation
- project differentiation
- competitor-aware ideation
- adversarial critique
- Agent workflow design
- self-media topic ideation

Workflow:

1. Frame the ideation problem.
2. Generate candidate ideas.
3. Critique each idea aggressively.
4. Search for existing work when novelty, feasibility, or market context depends on current information.
5. Refine ideas based on critique and evidence.
6. Rank ideas by novelty, feasibility, user value, differentiation, demonstrability, and fit.
7. Recommend only the ideas worth building.

Do not use this skill for normal paper polishing, translation, figure generation, or deterministic coding tasks.

````

---

## 10. 添加项目级调用规则

在项目的：

```text
.ai/PROJECT_RULES.md

````

中加入：

````
## Critical Ideation Rules

For brainstorming, idea validation, product differentiation, research topic generation, or Agent workflow design, use:

```text
.ai/toolkit/skills/critical-ideation/SKILL.md

````

When using this skill:

1. Do not only generate ideas.
2. Challenge each idea.
3. Search for existing products, papers, GitHub repos, or competitors when needed.
4. Refine ideas after critique.
5. Rank ideas using a decision matrix.
6. Recommend no more than three top ideas by default.

Generated ideation outputs should be saved to:

```
ideas/

```

Recommended files:

```
ideas/idea_report.md
ideas/search_log.md
ideas/decision_matrix.md
ideas/mvp_plan.md

```

````

---

## 11. 推荐业务项目目录

当某个项目使用该 Skill 时，建议项目内增加：

```text
Project/
├── .ai/
│   ├── toolkit/
│   └── PROJECT_RULES.md
├── ideas/
│   ├── idea_report.md
│   ├── search_log.md
│   ├── decision_matrix.md
│   └── mvp_plan.md
├── docs/
├── src/
└── README.md

````

创建命令：

### Windows PowerShell

```
mkdir ideas
New-Item ideas\idea_report.md
New-Item ideas\search_log.md
New-Item ideas\decision_matrix.md
New-Item ideas\mvp_plan.md

```

### WSL / Linux / macOS

```
mkdir -p ideas
touch ideas/idea_report.md ideas/search_log.md ideas/decision_matrix.md ideas/mvp_plan.md

```

***

## 12. Trae / Trae\_CN 调用模板

### 通用 idea brainstorm

```
请先读取：

.ai/PROJECT_RULES.md
.ai/toolkit/ROUTER.md
.ai/toolkit/skills/critical-ideation/SKILL.md

任务：
我想围绕 [领域/项目] brainstorm 一批 idea。

要求：
1. 生成 8 个候选 idea；
2. 对每个 idea 进行强质疑；
3. 主动检索已有论文、GitHub 项目、产品或竞品；
4. 判断哪些已经被做烂了，哪些还有差异化空间；
5. 最后给出 Top 3 推荐方向；
6. 每个方向给出 MVP、技术路线、风险和下一步行动；
7. 输出到 ideas/idea_report.md。

```

***

### 科研 idea brainstorm

```
请使用 critical-ideation skill。

研究方向：
[例如：VLM / 具身智能 / LLM Agent / NL2GIS / WorldQuant Alpha Agent]

目标：
帮我 brainstorm 适合普通学生推进的 research idea。

要求：
1. 检索近两年论文、GitHub repo、benchmark；
2. 质疑 novelty；
3. 判断是否需要大算力或大数据；
4. 优先推荐可以小规模验证的方向；
5. 输出 Top 3 选题；
6. 每个选题包含：
   - research question
   - hypothesis
   - method sketch
   - dataset / benchmark
   - baseline
   - evaluation metric
   - novelty risk
   - minimum experiment

```

***

### 产品 / PRD idea brainstorm

```
请使用 critical-ideation skill。

项目背景：
[粘贴 PRD 或产品想法]

目标：
帮我找到更有差异化的功能或产品切入点。

要求：
1. 积极检索竞品和已有方案；
2. 不要只鼓励我，要指出明显硬伤；
3. 给出可以一周内做出 demo 的 MVP 版本；
4. 最后用矩阵评分；
5. 输出：
   - idea list
   - competitor findings
   - critical objections
   - refined directions
   - MVP plan

```

***

### Agent workflow brainstorm

```
请使用 critical-ideation skill。

我正在设计一个 Agent workflow：

[描述当前 workflow]

目标：
帮我优化 Agent 架构，使其更稳定、更可评估、更容易扩展。

要求：
1. 质疑当前 workflow 的失败模式；
2. 检索类似 Agent 框架、benchmark 或开源项目；
3. 提出 3 个更优架构；
4. 每个架构包含：
   - agent roles
   - tool calls
   - memory design
   - human-in-the-loop points
   - evaluation harness
   - failure cases
   - MVP implementation plan

```

***

### 自媒体选题 brainstorm

```
请使用 critical-ideation skill。

账号定位：
[例如：聪明蛋小D的未来日记，武大到清华研0，AI项目，自我提升，旅欧记录]

目标：
帮我 brainstorm 20 个自媒体选题，并筛选出最值得拍的 5 个。

要求：
1. 检索近期类似内容趋势；
2. 质疑哪些选题太普通、太装、太像流水账；
3. 强化每个选题的冲突感和开头 hook；
4. 按拍摄难度、传播潜力、人设契合度排序；
5. 输出每个选题的：
   - title
   - opening hook
   - core conflict
   - content structure
   - filming plan
   - risk

```

***

## 13. Codex 调用模板

在项目根目录中使用 Codex：

```
Read the following files first:

.ai/PROJECT_RULES.md
.ai/toolkit/ROUTER.md
.ai/toolkit/skills/critical-ideation/SKILL.md

Task:
Create a critical ideation report for this project.

Requirements:
1. Generate candidate ideas.
2. Challenge each idea.
3. Search for existing solutions if needed.
4. Refine the ideas.
5. Rank them in a decision matrix.
6. Save outputs to:
   - ideas/idea_report.md
   - ideas/search_log.md
   - ideas/decision_matrix.md
   - ideas/mvp_plan.md

```

***

## 14. 和其他 Skill 的协同方式

### 14.1 与 writing prompt library 协同

```
critical-ideation
→ 找到 idea
→ awesome-ai-research-writing
→ 写成 proposal / PRD / paper introduction

```

适用任务：

- 科研选题说明
- 项目立项书
- PRD 初稿
- GitHub README
- 投稿前 introduction 逻辑

***

### 14.2 与 scientific-figure-making 协同

```
critical-ideation
→ 设计实验问题
→ scientific-figure-making
→ 可视化实验结果
→ writing prompt library
→ 写实验分析

```

适用任务：

- 实验设计
- benchmark 对比
- 项目 demo 数据展示
- 论文实验图

***

### 14.3 与 RebuttalStudio 协同

```
critical-ideation
→ 质疑论文 idea / 方法弱点
→ reviewer_check
→ 投稿前自查
→ RebuttalStudio
→ 收到 review 后逐点回复

```

适用任务：

- 投稿前预审
- reviewer 风险模拟
- rebuttal 前准备

***

## 15. Git 忽略建议

如果你不想把临时 brainstorm 输出提交到 Git，可以在业务项目 `.gitignore` 加入：

```
ideas/tmp/
ideas/drafts/

```

如果你希望保留项目决策过程，建议提交：

```
ideas/idea_report.md
ideas/decision_matrix.md
ideas/mvp_plan.md

```

因为这些文件可以作为项目演化记录。

***

## 16. 推荐输出标准

每次使用该 Skill，至少应输出：

```
1. Problem framing
2. Initial ideas
3. Critical objections
4. Search findings
5. Refined ideas
6. Decision matrix
7. Top recommendation
8. MVP plan

```

不要只输出 idea list。

如果没有进行搜索，必须明确说明：

```
本轮未进行联网检索，因此 novelty / competitor 判断可能不完整。

```

如果进行了搜索，必须记录：

```
搜索了什么
发现了什么
哪些已有方案接近
还剩什么差异化空间

```

***

## 17. 推荐评分标准

默认使用 1–5 分：

分数

含义

1

明显弱，不建议做

2

有问题，除非大幅修改

3

可尝试，但需要进一步验证

4

值得推进

5

高优先级，适合立即做 MVP

默认权重：

维度

权重

Feasibility

25%

Differentiation

20%

User Value

20%

Demo Potential

15%

Novelty

10%

Fit

10%

如果是科研任务，调整为：

维度

权重

Novelty

25%

Feasibility

20%

Evaluation Clarity

20%

Dataset Availability

15%

Publication Potential

10%

Fit

10%

如果是产品任务，调整为：

维度

权重

User Pain

25%

Differentiation

20%

Feasibility

20%

Distribution

15%

Monetization

10%

Demo Potential

10%

***

## 18. 常见错误

### 错误 1：只生成很多 idea，不筛选

错误输出：

```
这里有 20 个 idea……

```

正确输出：

```
这里有 8 个初始 idea。
其中 3 个明显重复已有方案，2 个实现成本过高，剩下 3 个值得进一步推进。

```

***

### 错误 2：没有检索就判断 novelty

错误输出：

```
这个方向很新颖。

```

正确输出：

```
在未检索前只能说它看起来有一定差异化。需要进一步搜索 GitHub、论文和竞品确认。

```

***

### 错误 3：把功能差异当成核心创新

错误输出：

```
我们加一个 AI 模块，所以有创新。

```

正确输出：

```
仅加入 AI 模块不是创新。需要说明 AI 改变了哪个核心流程、降低了什么成本、解决了哪个旧方法解决不了的问题。

```

***

### 错误 4：推荐超出用户资源的 idea

错误输出：

```
训练一个大型 VLA 模型。

```

正确输出：

```
更现实的 MVP 是基于现有 VLM + 小规模任务环境做 evaluation harness，而不是训练大型模型。

```

***

## 19. 适合你的优先使用场景

该 Skill 特别适合以下项目：

```
WorldQuant-Agent
ScamShield Guard
AI 短剧 Multi-Agent
Embodied-AI-Guide
GeoAgent Thesis
D-watch
自媒体选题
研究生阶段科研选题

```

推荐调用方式：

```
请使用 critical-ideation skill，不要只鼓励我。
请主动质疑、检索已有方案，并给出真正值得推进的 Top 3。

```

***

## 20. 最终检查清单

构建完成后，应存在以下文件：

```
skills/critical-ideation/SKILL.md
skills/critical-ideation/templates/idea_card.md
skills/critical-ideation/templates/search_log.md
skills/critical-ideation/templates/decision_matrix.md
skills/critical-ideation/templates/critique_checklist.md
skills/critical-ideation/templates/mvp_plan.md

```

`ROUTER.md` 中应包含：

```
Critical Ideation Skill

```

业务项目 `.ai/PROJECT_RULES.md` 中应包含：

```
Critical Ideation Rules

```

测试 Prompt：

```
请读取 .ai/toolkit/skills/critical-ideation/SKILL.md。
围绕“AI Agent 提升 WorldQuant Alpha 构建效率”生成 8 个 idea，
主动质疑并检索已有方案，最后筛选 Top 3，并给出 MVP。

```

如果模型输出包含以下内容，则说明 Skill 配置成功：

```
Problem framing
Initial ideas
Critical objections
Search findings
Refined ideas
Decision matrix
Top recommendations
MVP plan

```

<br />

