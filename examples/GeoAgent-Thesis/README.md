# GeoAgent-Thesis Example

[![Toolkit](https://img.shields.io/badge/Toolkit-ReSearching\_Figures\_Workflow-blue?logo=github)](https://github.com/timesbye/ReSearching_Figures_Workflow)

这是一个基于 [`templates/project_ai`](https://github.com/timesbye/ReSearching_Figures_Workflow/tree/main/templates/project_ai) 生成的示例科研项目，用来演示如何把 [ReSearching_Figures_Workflow](https://github.com/timesbye/ReSearching_Figures_Workflow) 挂接到具体论文或课题目录中。

> **项目定位**：ReSearching_Figures_Workflow 通过引用已有前沿科研绘图和学术写作工具，并在此基础上构建原创 brainstorm 能力，整合为从 ideation 到论文表达的一体式 workflow。本示例展示了这一完整工作流。

## 目录说明

- `.ai/PROJECT_RULES.md`
  项目级 AI 规则。
- `.ai/TASK_TEMPLATE.md`
  任务模板。
- `literature/`
  论文阅读笔记和文献综述。
- `data/results.csv`
  样例实验数据。
- `paper/context.md`
  论文背景与图表上下文。
- `paper/notes/demo_task.md`
  图表 + 写作联动任务示例。
- `ideas/demo_ideation_task.md`
  critical-ideation 任务示例。
- `ideas/`
  ideation 输出目录。

## 建立 toolkit 链接

本示例项目默认不提交 `.ai/toolkit` 实体链接，因为该链接依赖你的本地机器路径。

在仓库根目录执行：

```powershell
.\scripts\link_to_project.ps1 -ProjectPath "F:\AI-Research-Toolkit\examples\GeoAgent-Thesis"
```

执行后，示例项目中应出现：

```text
.ai/toolkit
```

## 运行方式

### 论文图表任务

1. 先让 Agent 读取：

```text
.ai/PROJECT_RULES.md
.ai/toolkit/ROUTER.md
```

2. 再把 `paper/notes/demo_task.md` 中的任务发送给 Agent。

3. 期望输出位置：

- 绘图脚本：`figures/scripts/`
- 绘图结果：`figures/outputs/`
- 分析草稿：聊天窗口或 `paper/notes/`

### Idea / 选题任务

1. 先让 Agent 读取：

```text
.ai/PROJECT_RULES.md
.ai/toolkit/ROUTER.md
.ai/toolkit/skills/critical-ideation/SKILL.md
```

2. 再把 `ideas/demo_ideation_task.md` 中的任务发送给 Agent。

3. 期望输出位置：

- `ideas/idea_report.md`
- `ideas/search_log.md`
- `ideas/decision_matrix.md`
- `ideas/mvp_plan.md`

## Workflow Showcase

如果你想直接展示“这个仓库如何把 ideation、绘图、写作和 reviewer 检查串成一个完整 workflow”，优先阅读：

- [`WORKFLOW_SHOWCASE.md`](https://github.com/timesbye/ReSearching_Figures_Workflow/blob/main/examples/GeoAgent-Thesis/WORKFLOW_SHOWCASE.md)

这份文档会按故事顺序展示：

1. 如何先筛选方向
2. 如何把方向转成图表证据
3. 如何把图表转成论文表达
4. 如何再用 reviewer 视角收缩 claim
