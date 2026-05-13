# Change Record / 变更记录

## 2026-05-12: 一致性修复 + CLI 交互式入口

### Phase 1: 一致性与完整性修复 (commit 4a9373f)

基于对项目的完整 workflow 审视，修复了 7 个一致性缺陷和 2 个完整性缺陷。

| # | 修改项 | 文件 | 类型 |
|---|--------|------|------|
| A1 | 修复项目名称 "DION-AI-Research-Toolkit" → "ALL-in-ALL_ReSearching_Workflow_Skill" | examples/GeoAgent-Thesis/.ai/PROJECT_RULES.md | Bug fix |
| A2+A3 | 重写 TASK_TEMPLATE.md 覆盖全部 8 个 Skill（原仅 3 个） | templates/project_ai/.ai/TASK_TEMPLATE.md | 一致性修复 |
| A7 | 升级示例项目 PROJECT_RULES.md 与模板一致 | examples/GeoAgent-Thesis/.ai/PROJECT_RULES.md | 一致性修复 |
| B1 | 新增 literature/ 目录 | templates/project_ai/literature/.gitkeep | 完整性修复 |
| B2 | 新增 experiments/ 目录 | templates/project_ai/experiments/.gitkeep | 完整性修复 |
| C4 | 修复 .gitignore 不再忽略示例项目产物 | .gitignore | Bug fix |
| A5 | WORKFLOW_SHOWCASE.md 补充第零幕（文献综述与论文阅读） | examples/GeoAgent-Thesis/WORKFLOW_SHOWCASE.md | 完整性修复 |
| - | 新增 WORKFLOW_STATUS.md 工作流状态追踪 | templates/project_ai/.ai/WORKFLOW_STATUS.md | 新功能 |
| - | 新增 DEPENDENCIES.md 声明上游依赖与版本策略 | DEPENDENCIES.md | 新增 |
| - | awesome-ai-research-writing README 增加版本锁定指引 | prompt-libraries/awesome-ai-research-writing/README.md | 改进 |

### Phase 2: CLI 交互式入口 (commit TBD)

新增 `cli.py` 交互式命令行入口，支持用户选择完整 workflow 或单模块调用。

#### 新增文件

| 文件 | 说明 |
|------|------|
| cli.py | 交互式 CLI 主入口，纯 Python 标准库实现 |

#### CLI 功能结构

```
主菜单 / Main Menu
├── [1] 完整 Workflow / Full Workflow
│   └── 8 步顺序执行：文献综述→论文阅读→选题构思→实验设计→绘图→写作→润色→审稿检查
│
├── [2] 单模块调用 / Individual Module
│   ├── [1] 💡 Idea Brainstorm / 选题构思
│   │   ├── [1] Critical Ideation（核心：对质式 brainstorm）
│   │   ├── [2] Literature Review（联动：文献综述）
│   │   ├── [3] Paper Reading（联动：论文阅读）
│   │   ├── [4] Experiment Design（联动：实验设计）
│   │   └── [5] Idea Brainstorm 完整流程（推荐）
│   │
│   └── [2] 📝 Paper Writing / 论文写作
│       ├── [1] Scientific Figure Making（核心：科研绘图）
│       ├── [2] Scholarly Writing（核心：引导式论文写作）
│       ├── [3] Academic Writing Prompt Library（核心：学术润色）
│       ├── [4] Reviewer Check（联动：审稿检查）
│       └── [5] Paper Writing 完整流程（推荐）
│
└── [0] 退出 / Exit
```

#### CLI 特性

- 中英文双语界面
- 自动读取 SKILL.md 描述展示给用户
- 根据选择自动生成任务提示（可直接复制到 Trae/Codex 执行）
- 检测 .ai/toolkit/ 链接状态
- 纯 Python 标准库，零外部依赖

#### 同步更新

| 文件 | 修改内容 |
|------|---------|
| README.md | Quick Start 增加 CLI 使用方式；Repository Layout 增加 cli.py 和 DEPENDENCIES.md |
