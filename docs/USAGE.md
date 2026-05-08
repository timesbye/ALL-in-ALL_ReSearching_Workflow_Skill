# 使用教程

本文档给出从工具仓库到实际科研项目的完整使用方式，并提供仓库内置示例项目的演示流程。

## 1. 仓库用途

本仓库统一提供两类能力：

- 学术写作与翻译 Prompt 库：
  `prompt-libraries/awesome-ai-research-writing/`
- 论文级科研绘图 Skill：
  `skills/scientific-figure-making/`

推荐使用方式不是把这些内容复制到每个项目里，而是让具体项目通过 `.ai/toolkit/` 链接到本仓库。

## 2. 目录说明

根目录中的关键路径：

- `ROUTER.md`
  统一路由说明，告诉 Agent 遇到不同任务时应该使用哪个能力入口。
- `prompts/`
  常用任务入口模板，例如润色、翻译、实验分析、完整图表流水线。
- `templates/project_ai/`
  新科研项目的最小模板。
- `examples/GeoAgent-Thesis/`
  基于模板生成的完整示例项目。
- `scripts/install_to_codex.ps1`
  将 `scientific-figure-making` 安装到 Codex 全局 skills。
- `scripts/link_to_project.ps1`
  将本仓库链接到目标项目的 `.ai/toolkit/`。

## 3. 新项目初始化

### Windows PowerShell

1. 创建业务项目目录：

```powershell
mkdir D:\Projects\My-Research-Project
```

2. 复制模板：

```powershell
Copy-Item -Recurse F:\AI-Research-Toolkit\templates\project_ai\* D:\Projects\My-Research-Project\
```

3. 连接 toolkit：

```powershell
F:\AI-Research-Toolkit\scripts\link_to_project.ps1 -ProjectPath "D:\Projects\My-Research-Project"
```

4. 在 Agent 中先读取：

```text
.ai/PROJECT_RULES.md
.ai/toolkit/ROUTER.md
```

### Linux / macOS / WSL

1. 创建业务项目目录：

```bash
mkdir -p ~/Projects/My-Research-Project
```

2. 复制模板：

```bash
cp -r /path/to/DION-AI-Research-Toolkit/templates/project_ai/* ~/Projects/My-Research-Project/
```

3. 连接 toolkit：

```bash
/path/to/DION-AI-Research-Toolkit/scripts/link_to_project.sh ~/Projects/My-Research-Project
```

4. 在 Agent 中先读取：

```text
.ai/PROJECT_RULES.md
.ai/toolkit/ROUTER.md
```

## 4. 使用示例项目

仓库内已经提供了一个现成示例：

```text
examples/GeoAgent-Thesis/
```

它包含：

- `.ai/PROJECT_RULES.md`
- `.ai/TASK_TEMPLATE.md`
- `data/results.csv`
- `paper/context.md`
- `paper/notes/demo_task.md`

### 在本仓库内给示例项目建立 toolkit 链接

Windows PowerShell：

```powershell
F:\AI-Research-Toolkit\scripts\link_to_project.ps1 -ProjectPath "F:\AI-Research-Toolkit\examples\GeoAgent-Thesis"
```

Linux / macOS / WSL：

```bash
/path/to/DION-AI-Research-Toolkit/scripts/link_to_project.sh /path/to/DION-AI-Research-Toolkit/examples/GeoAgent-Thesis
```

建立完成后，示例项目里会出现：

```text
examples/GeoAgent-Thesis/.ai/toolkit
```

## 5. Trae / Trae_CN 使用方式

在你的项目中直接输入类似任务：

```text
请先读取：
.ai/PROJECT_RULES.md
.ai/toolkit/ROUTER.md

任务：
基于 data/results.csv 生成论文级比较图，并给出中文图注与实验分析段落。

要求：
1. 绘图使用 .ai/toolkit/skills/scientific-figure-making/
2. 写作参考 .ai/toolkit/prompt-libraries/awesome-ai-research-writing/
3. 脚本保存到 figures/scripts/
4. PDF 和 PNG 保存到 figures/outputs/
5. 不要修改 .ai/toolkit/ 下的源文件
```

## 6. Codex 使用方式

### 可选：安装全局 skill

Windows PowerShell：

```powershell
F:\AI-Research-Toolkit\scripts\install_to_codex.ps1
```

Linux / macOS / WSL：

```bash
chmod +x scripts/install_to_codex.sh
./scripts/install_to_codex.sh
```

### 在项目中发起任务

先让 Codex 读取：

```text
.ai/PROJECT_RULES.md
.ai/toolkit/ROUTER.md
```

然后给出任务：

```text
Use the global scientific-figure-making skill for plotting.
Use .ai/toolkit/prompt-libraries/awesome-ai-research-writing for academic writing prompts.

Task:
Generate a publication-quality comparison figure from data/results.csv, save PDF/PNG, then write the Chinese thesis result analysis paragraph.
```

## 7. 推荐工作流

### 只做写作

使用：

```text
prompt-libraries/awesome-ai-research-writing/
```

### 只做绘图

使用：

```text
skills/scientific-figure-making/
```

### 图表 + 写作联合任务

按以下顺序：

1. 读 `data/` 中的数据
2. 生成绘图脚本
3. 导出 PDF / PNG
4. 写图注
5. 写实验分析
6. 做 reviewer 风格检查

## 8. 常见注意事项

- 所有生成文件都应保存到当前业务项目，而不是 toolkit 根目录。
- 除非明确要求，不要修改 `.ai/toolkit/` 内的 toolkit 源文件。
- 若 `figures/outputs/` 里的产物不打算入库，可以保留模板里的 `.gitignore` 默认规则。
- 若你希望论文图片也纳入版本控制，可以删掉项目内 `.gitignore` 中的对应忽略规则。

## 9. 最短上手路径

如果你只想最快跑通一遍：

1. 给 `examples/GeoAgent-Thesis` 建立 `.ai/toolkit` 链接。
2. 打开 [examples/GeoAgent-Thesis/paper/notes/demo_task.md](/F:/AI-Research-Toolkit/examples/GeoAgent-Thesis/paper/notes/demo_task.md)。
3. 把其中的任务文本直接发给 Trae 或 Codex。
4. 检查生成的脚本是否落在 `figures/scripts/`，图像是否落在 `figures/outputs/`。
