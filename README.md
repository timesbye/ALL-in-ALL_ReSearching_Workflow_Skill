# DION AI Research Toolkit

一个面向科研写作与论文绘图的可复用工具仓库。

这个仓库把两个上游资源组织到同一个稳定入口下：

- `prompt-libraries/awesome-ai-research-writing/`
  用于学术写作、润色、翻译、实验分析和 reviewer 风格检查。
- `skills/scientific-figure-making/`
  用于生成论文级 matplotlib 科研图、导出 PDF/PNG，并沉淀可复现脚本。

仓库目标：

- 为 Trae / Trae_CN / GLM5.1 提供项目内显式路径调用方式。
- 为 Codex 提供全局 skill 安装方式。
- 让不同项目通过 `.ai/toolkit` 软链接或 Junction 复用本工具库。
- 避免在每个业务项目里重复复制 Prompt 库和绘图 Skill。

## Repository Layout

```text
DION-AI-Research-Toolkit/
|-- README.md
|-- BUILD.md
|-- ROUTER.md
|-- prompt-libraries/
|   `-- awesome-ai-research-writing/
|-- skills/
|   `-- scientific-figure-making/
|-- prompts/
|   |-- polish_cn.md
|   |-- translate_cn_to_en.md
|   |-- reviewer_check.md
|   |-- experiment_analysis.md
|   |-- figure_generation.md
|   `-- paper_figure_full_pipeline.md
|-- templates/
|   `-- project_ai/
|       |-- .ai/
|       |   |-- PROJECT_RULES.md
|       |   `-- TASK_TEMPLATE.md
|       |-- data/
|       |-- figures/
|       |   |-- scripts/
|       |   `-- outputs/
|       `-- paper/
`-- scripts/
    |-- install_to_codex.ps1
    |-- install_to_codex.sh
    |-- link_to_project.ps1
    `-- link_to_project.sh
```

## Quick Start

1. 复制模板到你的科研项目目录。
2. 通过 `scripts/link_to_project.ps1` 或 `scripts/link_to_project.sh` 把本仓库链接到目标项目的 `.ai/toolkit/`。
3. 在 Trae / Codex 中先读取：

```text
.ai/PROJECT_RULES.md
.ai/toolkit/ROUTER.md
```

4. 若使用 Codex 全局 skill，可执行：

```powershell
.\scripts\install_to_codex.ps1
```

或：

```bash
chmod +x scripts/install_to_codex.sh
./scripts/install_to_codex.sh
```

## Recommended Project Bootstrap

```text
My-Research-Project/
|-- .ai/
|   |-- PROJECT_RULES.md
|   |-- TASK_TEMPLATE.md
|   `-- toolkit -> DION-AI-Research-Toolkit
|-- data/
|-- figures/
|   |-- scripts/
|   `-- outputs/
`-- paper/
```

复制模板：

```powershell
Copy-Item -Recurse .\templates\project_ai\* D:\Projects\My-Research-Project\
```

建立链接：

```powershell
.\scripts\link_to_project.ps1 -ProjectPath "D:\Projects\My-Research-Project"
```

## Typical Workflows

- 仅写作任务：
  使用 `prompt-libraries/awesome-ai-research-writing/`。
- 仅绘图任务：
  使用 `skills/scientific-figure-making/`。
- 图表 + 论文表达联合任务：
  先生成图，再写图注、结果分析和 reviewer 检查。

详见 [ROUTER.md](ROUTER.md) 与 `prompts/` 目录中的入口文档。

## Example Project

仓库内置了一个基于模板生成的示例项目：

```text
examples/GeoAgent-Thesis/
```

示例项目包含样例数据、论文上下文和可直接发送给 Agent 的任务说明，适合用于验证整套工作流是否跑通。

建议先阅读：

- `examples/GeoAgent-Thesis/README.md`
- `examples/GeoAgent-Thesis/paper/notes/demo_task.md`
- `docs/USAGE.md`

## Usage Guide

完整教程见：

- `docs/USAGE.md`

其中包含：

- 如何从模板初始化一个新科研项目
- 如何把 toolkit 链接到具体项目
- 如何使用仓库内的示例项目
- Trae / Trae_CN / Codex 的推荐调用方式

## Notes

- 当前仓库采用 vendored 目录形式引入上游内容，便于直接随本仓库分发。
- 生成文件应保存到业务项目目录中，而不是保存到 toolkit 自身目录中。
- 若需要更新上游库，建议重新拉取并替换对应目录，再统一测试路由和脚本。
