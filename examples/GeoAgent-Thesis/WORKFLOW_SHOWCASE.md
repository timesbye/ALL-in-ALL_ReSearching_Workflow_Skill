# GeoAgent Workflow Showcase

这份示例不是在展示“某一个单点能力有多强”，而是在展示这个仓库如何把外部引用能力和我们自己的项目规则整合成一个可复用 workflow。

这里的关键不是声称我们发明了所有模块，而是：

- 引入 `awesome-ai-research-writing` 作为学术写作 Prompt 库
- 引入 `figures4papers` 中的 `scientific-figure-making` 作为科研绘图 Skill
- 在此基础上补上我们自己的 `critical-ideation`、路由规则、项目模板、产物目录和顺序调用方式

换句话说，这个仓库的价值在于 **把分散能力组织成一个能从想法走到图表、再走到论文表达的连续工作流**。

---

## 故事起点

假设我们现在在推进 `GeoAgent-Thesis` 这个项目。

手里已有的材料并不多：

- 一份当前实验结果表：[data/results.csv](data/results.csv)
- 一段论文上下文：[paper/context.md](paper/context.md)
- 三个可调用模块：
  - `critical-ideation`
  - `scientific-figure-making`
  - `awesome-ai-research-writing`

问题不是“能不能生成一张图”，而是：

1. 这个项目下一步到底该往哪个方向推进？
2. 现有数据能支撑怎样的图表与结论？
3. 最终怎么把这些内容写成论文表达，而不是散乱笔记？

这正是 workflow 应该解决的问题。

---

## 第一幕：先做 Ideation，不急着画图

### 调用顺序

先读取：

```text
.ai/PROJECT_RULES.md
.ai/toolkit/ROUTER.md
.ai/toolkit/skills/critical-ideation/SKILL.md
paper/context.md
```

然后执行任务模板：[ideas/demo_ideation_task.md](ideas/demo_ideation_task.md)

### 这一步为什么重要

很多项目一上来就开始画图、写段落，最后发现核心方向根本没收敛。  
我们这里先用 `critical-ideation` 做三件事：

1. 把问题 framing 清楚
2. 生成多个候选方向
3. 主动质疑并筛掉不值得继续投入的 idea

### 这一步的结果

产物已经保存到：

- [ideas/idea_report.md](ideas/idea_report.md)
- [ideas/search_log.md](ideas/search_log.md)
- [ideas/decision_matrix.md](ideas/decision_matrix.md)
- [ideas/mvp_plan.md](ideas/mvp_plan.md)

### 核心结论

这轮 ideation 没有把“GeoAgent 做成一个更大的万能系统”当成答案，而是收敛出了一个更可执行的方向：

**Top 1: `GeoAgent-Router`**

它的意思不是空泛地说“我们再加一个 Agent”，而是明确提出：

- GeoAgent 系列已经表现出性能-延迟权衡
- 下一步值得做的是预算感知的变体选择或路由策略
- 这个方向能直接连接到现有数据、图表和 MVP

这就是 workflow 的第一层价值：  
**先决定什么值得画、什么值得写，而不是先画再找故事。**

---

## 第二幕：把方向变成图，而不是停留在想法

有了上一步的 Top 1 方向后，下一步不是立刻写 proposal，而是先验证手头数据能否支撑一个清晰的可视化叙事。

### 调用顺序

先读取：

```text
.ai/PROJECT_RULES.md
.ai/toolkit/ROUTER.md
.ai/toolkit/skills/scientific-figure-making/SKILL.md
paper/context.md
data/results.csv
```

然后使用本地绘图脚本：

- [figures/scripts/plot_geoagent_workflow_showcase.py](figures/scripts/plot_geoagent_workflow_showcase.py)

### 产物位置

- [figures/outputs/geoagent_workflow_showcase.png](figures/outputs/geoagent_workflow_showcase.png)
- [figures/outputs/geoagent_workflow_showcase.pdf](figures/outputs/geoagent_workflow_showcase.pdf)

### 结果展示

![GeoAgent workflow showcase figure](figures/outputs/geoagent_workflow_showcase.png)

### 这张图在讲什么

这张图没有试图讲一个过大的故事，而是只讲两件已经被数据支持的事：

1. `GeoAgent` 系列在 Accuracy 和 F1 上持续优于两个基线方法
2. 性能提升伴随着逐步增加的推理延迟，因此存在明确的 quality-latency frontier

这一步的 workflow 价值是：  
**把 ideation 阶段收敛出的方向，转成一个能被肉眼直接理解的证据对象。**

换句话说，第一幕给出“接下来最值得推进什么”，第二幕回答“现有证据能不能把这个方向讲出来”。

---

## 第三幕：把图变成论文表达

只有图还不够。真正交付到论文或答辩中，还需要：

- 中文图注
- 英文图注
- 中文实验分析段落

### 调用顺序

先读取：

```text
.ai/PROJECT_RULES.md
.ai/toolkit/ROUTER.md
.ai/toolkit/prompts/paper_figure_full_pipeline.md
paper/context.md
```

然后把图表结果交给写作 Prompt 库进行学术化表达整理。

### 产物位置

- [paper/notes/figure_caption_cn.md](paper/notes/figure_caption_cn.md)
- [paper/notes/figure_caption_en.md](paper/notes/figure_caption_en.md)
- [paper/notes/result_analysis_cn.md](paper/notes/result_analysis_cn.md)

### 结果示例

中文图注的核心句子是：

> GeoAgent 系列存在清晰的性能-延迟权衡关系，为后续设计面向预算约束的模型选择或路由策略提供了依据。

中文结果分析的核心判断是：

> 现有结果更适合支持“GeoAgent 系列存在可利用的性能-延迟权衡”这一结论，而不是直接声称所有变体都在任意部署场景下同时兼顾最优性能与最低成本。

### 这一步为什么不是“可有可无”

如果没有这一步，很多项目会停在“我有图，但我不会把图写成论文语言”。  
我们的 workflow 不把写作当成独立末端，而是把它接在图表之后，让表达自动继承前面已经收敛好的 claim 边界。

这一步的 workflow 价值是：  
**同一份数据、同一张图，被整理成可以直接进入论文上下文的语言产物。**

---

## 第四幕：最后再让 Reviewer 来拆台

如果到这里就结束，最常见的问题是过度声称。  
因此 workflow 的最后一步不是庆祝，而是反过来质疑自己。

### 调用顺序

使用 reviewer-style 检查当前图表与 claim 的匹配关系。

### 产物位置

- [paper/notes/reviewer_check.md](paper/notes/reviewer_check.md)

### Reviewer 给出的关键反馈

主要问题有两个：

1. 当前图只支撑“存在性能-延迟权衡”，还不能直接支撑“已经解决预算感知部署”
2. “practical latency” 这个词不够具体，缺少明确阈值

### 这一步的意义

这一步非常关键，因为它把 workflow 从“顺着讲故事”变成“会主动收缩 claim 边界”。

如果没有 reviewer 检查，项目很容易从：

```text
我们发现了清晰的 trade-off
```

滑向：

```text
我们已经证明 GeoAgent 在所有部署场景下都更优
```

这正是高质量 workflow 和普通拼接流程的区别。

---

## 最终串起来看，这个 workflow 做了什么

按顺序回看：

1. `critical-ideation`  
   先筛方向，不让项目在错误的 idea 上浪费时间
2. `scientific-figure-making`  
   把方向绑定到可见证据，而不是抽象口号
3. `awesome-ai-research-writing`  
   把图表结果整理成论文级表达
4. `reviewer_check`  
   防止过度 claim，逼着结论回到证据边界内

这不是四个功能的并排陈列，而是一个顺序依赖的链条：

```text
idea
-> shortlist
-> evidence figure
-> caption and analysis
-> reviewer constraint
-> final claim
```

---

## 这个示例真正展示的，不是“某个文件”，而是“我们的 workflow 能力”

这个示例说明：

- 我们可以把引用来的能力模块整合成统一入口
- 我们可以让不同模块之间通过项目目录和规则协同工作
- 我们可以把 brainstorm、图表、写作和 reviewer 检查串成一个连续生产链
- 我们最终交付的不是碎片化 prompt，而是**可复用、可落库、可追溯的项目工作流**

如果你要向别人展示这个仓库，最应该给他看的不是单个 skill，而是这条完整链路：

- ideation 结果在 `ideas/`
- 图表脚本与产物在 `figures/`
- 学术表达与 reviewer 检查在 `paper/notes/`
- 整体讲解就在这份文档里

---

## 建议的演示顺序

实际给别人做演示时，按下面顺序最清楚：

1. 先打开这份文档：[WORKFLOW_SHOWCASE.md](WORKFLOW_SHOWCASE.md)
2. 再打开 ideation 产物：
   - [ideas/idea_report.md](ideas/idea_report.md)
   - [ideas/decision_matrix.md](ideas/decision_matrix.md)
3. 再看图和脚本：
   - [figures/scripts/plot_geoagent_workflow_showcase.py](figures/scripts/plot_geoagent_workflow_showcase.py)
   - [figures/outputs/geoagent_workflow_showcase.png](figures/outputs/geoagent_workflow_showcase.png)
4. 最后看论文表达与 reviewer 收口：
   - [paper/notes/figure_caption_cn.md](paper/notes/figure_caption_cn.md)
   - [paper/notes/result_analysis_cn.md](paper/notes/result_analysis_cn.md)
   - [paper/notes/reviewer_check.md](paper/notes/reviewer_check.md)

这样别人看到的就不是“一个仓库里有很多文件”，而是“这个仓库可以把一个项目从想法一路推到表达，并且中间每一步都有产物可落地”。
