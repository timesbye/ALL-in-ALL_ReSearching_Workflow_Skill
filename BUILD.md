<br />

````
# BUILD.md

# DION-AI-Research-Toolkit 构建指南

本项目用于构建一个可被多个科研、论文、Agent、绘图项目复用的 AI Research Toolkit。

核心目标：

- 将 `awesome-ai-research-writing` 作为论文写作 Prompt 库；
- 将 `figures4papers` 中的 `scientific-figure-making` 作为科研绘图 Skill；
- 为 Trae / Trae_CN / GLM5.1 提供项目内显式调用方式；
- 为终端 Codex 提供全局 Skill 调用方式；
- 让不同项目通过 `.ai/toolkit` 软链接调用本工具库，而不是重复复制。

---

## 1. 推荐总目录结构

目标结构如下：

```text
DION-AI-Research-Toolkit/
├── README.md
├── BUILD.md
├── ROUTER.md
├── prompt-libraries/
│   └── awesome-ai-research-writing/
├── skills/
│   └── scientific-figure-making/
├── prompts/
│   ├── polish_cn.md
│   ├── translate_cn_to_en.md
│   ├── reviewer_check.md
│   ├── experiment_analysis.md
│   ├── figure_generation.md
│   └── paper_figure_full_pipeline.md
├── templates/
│   └── project_ai/
│       ├── .ai/
│       │   ├── PROJECT_RULES.md
│       │   └── TASK_TEMPLATE.md
│       ├── data/
│       ├── figures/
│       │   ├── scripts/
│       │   └── outputs/
│       └── paper/
└── scripts/
    ├── install_to_codex.ps1
    ├── install_to_codex.sh
    ├── link_to_project.ps1
    └── link_to_project.sh

````

***

## 2. 初始化工具仓库

### Windows PowerShell

```
mkdir DION-AI-Research-Toolkit
cd DION-AI-Research-Toolkit
git init

mkdir prompt-libraries
mkdir skills
mkdir prompts
mkdir templates
mkdir scripts

```

### WSL / Linux / macOS

```
mkdir DION-AI-Research-Toolkit
cd DION-AI-Research-Toolkit
git init

mkdir -p prompt-libraries
mkdir -p skills
mkdir -p prompts
mkdir -p templates
mkdir -p scripts

```

***

## 3. 引入两个外部仓库

### 方案 A：直接 clone，适合本地个人使用

```
git clone https://github.com/Leey21/awesome-ai-research-writing.git prompt-libraries/awesome-ai-research-writing

git clone https://github.com/ChenLiu-1996/figures4papers.git external_figures4papers

cp -r external_figures4papers/scientific-figure-making skills/scientific-figure-making

rm -rf external_figures4papers

```

Windows PowerShell：

```
git clone https://github.com/Leey21/awesome-ai-research-writing.git prompt-libraries/awesome-ai-research-writing

git clone https://github.com/ChenLiu-1996/figures4papers.git external_figures4papers

Copy-Item -Recurse external_figures4papers\scientific-figure-making skills\scientific-figure-making

Remove-Item -Recurse -Force external_figures4papers

```

优点：

- 简单；
- Trae / Trae\_CN / GLM5.1 读取路径稳定；
- 不需要理解 Git submodule。

缺点：

- 后续同步上游更新需要手动重新拉取。

***

### 方案 B：Git submodule，适合长期维护

```
mkdir -p external

git submodule add https://github.com/Leey21/awesome-ai-research-writing.git prompt-libraries/awesome-ai-research-writing

git submodule add https://github.com/ChenLiu-1996/figures4papers.git external/figures4papers

```

然后绘图 Skill 路径使用：

```
external/figures4papers/scientific-figure-making/

```

如果使用 submodule，别人 clone 你的工具库时需要：

```
git clone --recurse-submodules <your-repo-url>

```

或者 clone 后执行：

```
git submodule update --init --recursive

```

个人建议：初期使用方案 A，等工作流稳定后再升级到方案 B。

***

## 4. 创建总控 ROUTER.md

在项目根目录创建：

```
ROUTER.md

```

内容如下：

````
# DION AI Research Toolkit Router

## 1. Academic Writing Prompt Library

Path:

prompt-libraries/awesome-ai-research-writing/

Use for:

- Chinese academic polishing
- English academic polishing
- Chinese-to-English academic translation
- English-to-Chinese academic translation
- abstract writing
- introduction rewriting
- related work organization
- experiment analysis
- reviewer-style critique
- AI-tone reduction
- logical coherence checking

Rules:

- Preserve technical meaning.
- Do not invent results, citations, or experimental claims.
- Use formal academic language.
- Avoid exaggerated contribution statements.
- Keep terminology consistent with the target project.

---

## 2. Scientific Figure Making Skill

Path:

skills/scientific-figure-making/

Important files:

- SKILL.md
- references/api.md
- references/design-theory.md
- references/common-patterns.md
- references/demos.md

Use for:

- publication-quality scientific figures
- matplotlib scripts
- bar plots
- line plots
- radar plots
- ablation figures
- comparison figures
- heatmaps
- multi-panel figures
- exporting PDF and PNG

Rules:

- Generate reproducible Python scripts.
- Save scripts to the target project's `figures/scripts/`.
- Save outputs to the target project's `figures/outputs/`.
- Export both PDF and PNG.
- Use readable axis labels, legends, and captions.
- Prefer clean academic style.
- Do not use decorative or marketing-style charts.

---

## 3. Mixed Figure + Writing Workflow

When a task involves both experimental visualization and paper writing:

1. Use `scientific-figure-making` to design and generate the figure.
2. Save the plotting script into the target project.
3. Save PDF and PNG outputs into the target project.
4. Draft the figure caption.
5. Use `awesome-ai-research-writing` to polish the caption.
6. Write a thesis-style or paper-style result analysis paragraph.
7. Use reviewer-style critique to check whether the figure supports the stated claim.

---

## 4. Routing Rules

If the task is mainly about writing, translation, polishing, summarization, or review:

Use:

```text
prompt-libraries/awesome-ai-research-writing/

````

If the task is mainly about plotting, visualization, or chart design:

Use:

```
skills/scientific-figure-making/

```

If the task is about both figure generation and experiment analysis:

Use both, in this order:

```
scientific-figure-making
→ caption draft
→ awesome-ai-research-writing
→ result analysis
→ reviewer check

```

***

## 5. Important Safety Rule

Do not modify toolkit source files unless the user explicitly asks to update the toolkit itself.

When working inside another project, all generated outputs must be saved into the current project directory, not into the toolkit directory.

````

---

## 5. 创建常用 Prompt 入口

### 5.1 `prompts/polish_cn.md`

```md
# 中文论文润色

请参考 `prompt-libraries/awesome-ai-research-writing/` 中的中文论文润色思路，对输入文本进行毕业论文或学术论文级别润色。

要求：

1. 保持原技术含义不变。
2. 不虚构实验结果、数据或引用。
3. 删除口语化表达。
4. 增强逻辑衔接。
5. 保持正式、克制、学术化表达。
6. 输出：
   - 修改后正文
   - 主要修改点
   - 可能仍需人工确认的问题

````

***

### 5.2 `prompts/translate_cn_to_en.md`

```
# 中文转英文学术表达

请参考 `prompt-libraries/awesome-ai-research-writing/` 中的中英学术翻译思路。

要求：

1. 保持技术含义准确。
2. 使用计算机科学论文常见表达。
3. 不过度拔高贡献。
4. 保留 LaTeX、变量名、方法名和缩写。
5. 输出：
   - English Version
   - Terminology Notes
   - Potential Ambiguities

```

***

### 5.3 `prompts/reviewer_check.md`

```
# Reviewer 视角检查

请参考 `prompt-libraries/awesome-ai-research-writing/` 中的审稿、逻辑检查、论文批评思路。

请从以下角度检查论文片段：

1. 研究问题是否清楚。
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

```

***

### 5.4 `prompts/experiment_analysis.md`

```
# 实验结果分析

请参考 `prompt-libraries/awesome-ai-research-writing/` 中的实验分析写作思路。

基于输入数据、图表和论文上下文，写一段论文中的实验结果分析。

要求：

1. 只描述数据支持的结论。
2. 先说总体趋势，再说关键对比。
3. 可以解释可能原因，但不得过度推断。
4. 与图注、表格标题保持术语一致。
5. 使用正式中文论文表达。
6. 不虚构数值、实验设置或结论。

输出：

- 实验结果分析正文
- 该段落支撑的核心 claim
- 可能存在的过度推断风险

```

***

### 5.5 `prompts/figure_generation.md`

```
# 论文实验图生成

请使用 `skills/scientific-figure-making/` 中的规范生成论文级科研图。

输入：

- 实验数据
- 图类型
- 论文场景
- 想表达的核心结论

要求：

1. 生成可复现 Python matplotlib 脚本。
2. 输出 PDF 和 PNG。
3. 图片保存到当前项目的 `figures/outputs/`。
4. 脚本保存到当前项目的 `figures/scripts/`。
5. 坐标轴、图例、标题、字体大小适合论文和答辩。
6. 不使用花哨或营销风格。
7. 同时生成中文图注和结果分析草稿。

```

***

### 5.6 `prompts/paper_figure_full_pipeline.md`

```
# 论文图表完整流水线

请完成从实验数据到论文表达的完整流水线。

需要使用：

- `skills/scientific-figure-making/`：负责绘图脚本与图像输出；
- `prompt-libraries/awesome-ai-research-writing/`：负责图注、实验分析、论文表达润色；
- `prompts/reviewer_check.md`：负责检查图表是否足以支撑论文 claim。

输入：

- 实验数据
- 论文上下文
- 目标图类型
- 想表达的核心结论

输出：

1. Python 绘图脚本
2. PDF 图像
3. PNG 图像
4. 中文图注
5. 英文图注，如果用户需要
6. 中文实验结果分析段落
7. Reviewer 风格检查意见
8. 是否存在 claim 过度的问题

保存路径：

- 脚本：`figures/scripts/`
- 图像：`figures/outputs/`
- 分析草稿：可输出到聊天或保存到 `paper/notes/`

```

***

## 6. 创建项目模板

创建模板目录：

```
mkdir -p templates/project_ai/.ai
mkdir -p templates/project_ai/data
mkdir -p templates/project_ai/figures/scripts
mkdir -p templates/project_ai/figures/outputs
mkdir -p templates/project_ai/paper

```

Windows PowerShell：

```
mkdir templates\project_ai\.ai
mkdir templates\project_ai\data
mkdir templates\project_ai\figures\scripts
mkdir templates\project_ai\figures\outputs
mkdir templates\project_ai\paper

```

***

## 7. 创建模板 PROJECT\_RULES.md

文件位置：

```
templates/project_ai/.ai/PROJECT_RULES.md

```

内容：

````
# Project AI Rules

## Project Identity

This is a project using DION-AI-Research-Toolkit.

Before starting any task, read:

```text
.ai/toolkit/ROUTER.md

````

## Toolkit Path

The toolkit should be linked as:

```
.ai/toolkit/

```

## Writing Rules

For academic writing, polishing, translation, experiment analysis, and reviewer-style critique, use:

```
.ai/toolkit/prompt-libraries/awesome-ai-research-writing/

```

General writing requirements:

- Preserve technical meaning.
- Do not invent results, citations, or experimental claims.
- Use formal academic style.
- Avoid exaggerated contribution statements.
- Keep terminology consistent with this project.

## Figure Rules

For scientific figures, use:

```
.ai/toolkit/skills/scientific-figure-making/

```

Figure output rules:

- Save scripts to `figures/scripts/`.
- Save PDF and PNG to `figures/outputs/`.
- Generate reproducible Python matplotlib scripts.
- Use readable labels, legends, and captions.
- Avoid decorative or marketing-style charts.

## Mixed Task Workflow

For figure + paper writing tasks:

1. Read project data from `data/`.
2. Generate plotting script.
3. Save figure outputs.
4. Draft figure caption.
5. Polish caption using academic writing prompts.
6. Write result analysis paragraph.
7. Check whether the figure supports the stated claim.

## Important Rule

Do not modify `.ai/toolkit/` source files unless explicitly asked.

All generated files should be saved inside the current project.

````

---

## 8. 创建模板 TASK_TEMPLATE.md

文件位置：

```text
templates/project_ai/.ai/TASK_TEMPLATE.md

````

内容：

````
# Task Template

请先读取：

```text
.ai/PROJECT_RULES.md
.ai/toolkit/ROUTER.md

````

本次任务：

\[在这里填写任务]

输入材料：

- 数据：
- 论文上下文：
- 目标输出：
- 特殊要求：

调用规则：

1. 如果是绘图任务，使用 `.ai/toolkit/skills/scientific-figure-making/`。
2. 如果是论文表达任务，参考 `.ai/toolkit/prompt-libraries/awesome-ai-research-writing/`。
3. 如果是混合任务，先完成图，再完成图注和论文分析。
4. 所有输出都保存到当前项目，不要修改 toolkit 源文件。

期望输出：

- Python 脚本
- PDF 图像
- PNG 图像
- 中文图注
- 英文图注
- 实验分析段落
- Reviewer 检查意见

````

---

## 9. 创建 Codex 全局安装脚本

### 9.1 Windows：`scripts/install_to_codex.ps1`

```powershell
# Install scientific-figure-making skill to Codex global skills directory

$ToolkitRoot = Split-Path -Parent $PSScriptRoot
$SkillSource = Join-Path $ToolkitRoot "skills\scientific-figure-making"
$CodexSkills = Join-Path $env:USERPROFILE ".codex\skills"
$SkillTarget = Join-Path $CodexSkills "scientific-figure-making"

if (!(Test-Path $CodexSkills)) {
    New-Item -ItemType Directory -Path $CodexSkills -Force
}

if (Test-Path $SkillTarget) {
    Write-Host "Existing skill target found: $SkillTarget"
    Write-Host "Remove it manually if you want to recreate the link."
    exit
}

New-Item -ItemType Junction -Path $SkillTarget -Target $SkillSource

Write-Host "Installed scientific-figure-making skill to Codex:"
Write-Host $SkillTarget

````

运行方式：

```
.\scripts\install_to_codex.ps1

```

***

### 9.2 WSL / Linux / macOS：`scripts/install_to_codex.sh`

```
#!/usr/bin/env bash
set -e

TOOLKIT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_SOURCE="$TOOLKIT_ROOT/skills/scientific-figure-making"
CODEX_SKILLS="$HOME/.codex/skills"
SKILL_TARGET="$CODEX_SKILLS/scientific-figure-making"

mkdir -p "$CODEX_SKILLS"

if [ -e "$SKILL_TARGET" ]; then
  echo "Existing skill target found: $SKILL_TARGET"
  echo "Remove it manually if you want to recreate the link."
  exit 0
fi

ln -s "$SKILL_SOURCE" "$SKILL_TARGET"

echo "Installed scientific-figure-making skill to Codex:"
echo "$SKILL_TARGET"

```

运行方式：

```
chmod +x scripts/install_to_codex.sh
./scripts/install_to_codex.sh

```

***

## 10. 创建项目链接脚本

### 10.1 Windows：`scripts/link_to_project.ps1`

```
param (
    [Parameter(Mandatory=$true)]
    [string]$ProjectPath
)

$ToolkitRoot = Split-Path -Parent $PSScriptRoot
$AiDir = Join-Path $ProjectPath ".ai"
$ToolkitLink = Join-Path $AiDir "toolkit"

if (!(Test-Path $ProjectPath)) {
    Write-Host "Project path does not exist: $ProjectPath"
    exit 1
}

if (!(Test-Path $AiDir)) {
    New-Item -ItemType Directory -Path $AiDir -Force
}

if (Test-Path $ToolkitLink) {
    Write-Host "Existing toolkit link found: $ToolkitLink"
    Write-Host "Remove it manually if you want to recreate the link."
    exit 0
}

New-Item -ItemType Junction -Path $ToolkitLink -Target $ToolkitRoot

Write-Host "Linked toolkit to project:"
Write-Host $ToolkitLink

```

使用方式：

```
.\scripts\link_to_project.ps1 -ProjectPath "D:\Projects\GeoAgent-Thesis"

```

***

### 10.2 WSL / Linux / macOS：`scripts/link_to_project.sh`

```
#!/usr/bin/env bash
set -e

if [ -z "$1" ]; then
  echo "Usage: ./scripts/link_to_project.sh /path/to/project"
  exit 1
fi

PROJECT_PATH="$1"
TOOLKIT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AI_DIR="$PROJECT_PATH/.ai"
TOOLKIT_LINK="$AI_DIR/toolkit"

if [ ! -d "$PROJECT_PATH" ]; then
  echo "Project path does not exist: $PROJECT_PATH"
  exit 1
fi

mkdir -p "$AI_DIR"

if [ -e "$TOOLKIT_LINK" ]; then
  echo "Existing toolkit link found: $TOOLKIT_LINK"
  echo "Remove it manually if you want to recreate the link."
  exit 0
fi

ln -s "$TOOLKIT_ROOT" "$TOOLKIT_LINK"

echo "Linked toolkit to project:"
echo "$TOOLKIT_LINK"

```

使用方式：

```
chmod +x scripts/link_to_project.sh
./scripts/link_to_project.sh /path/to/GeoAgent-Thesis

```

***

## 11. 目标项目中的推荐结构

例如你的 `GeoAgent-Thesis` 项目最终应该是：

```
GeoAgent-Thesis/
├── .ai/
│   ├── toolkit -> DION-AI-Research-Toolkit
│   ├── PROJECT_RULES.md
│   └── TASK_TEMPLATE.md
├── data/
├── figures/
│   ├── scripts/
│   └── outputs/
├── paper/
└── README.md

```

其中：

```
.ai/toolkit/

```

是指向独立工具库的软链接或 Junction。

***

## 12. Trae / Trae\_CN 使用方式

在任意项目中，对 Trae / Trae\_CN 输入：

```
请先读取：

.ai/PROJECT_RULES.md
.ai/toolkit/ROUTER.md

本次任务：
基于 data/results.csv 生成论文级实验对比图，并写出中文图注和实验结果分析段落。

要求：
1. 绘图使用 .ai/toolkit/skills/scientific-figure-making/。
2. 写作参考 .ai/toolkit/prompt-libraries/awesome-ai-research-writing/。
3. 输出脚本到 figures/scripts/。
4. 输出 PDF 和 PNG 到 figures/outputs/。
5. 不要修改 .ai/toolkit/ 下的任何源文件。

```

***

## 13. Codex 终端使用方式

如果已经执行过：

```
./scripts/install_to_codex.sh

```

或：

```
.\scripts\install_to_codex.ps1

```

则可以在任意项目中使用：

```
Read .ai/PROJECT_RULES.md and .ai/toolkit/ROUTER.md first.

Use the global scientific-figure-making skill for plotting.
Use .ai/toolkit/prompt-libraries/awesome-ai-research-writing for academic writing prompts.

Task:
Generate a publication-quality comparison figure from data/results.csv, save PDF/PNG, then write the Chinese thesis result analysis paragraph.

```

***

## 14. 推荐新项目初始化流程

### Step 1：创建业务项目

```
mkdir GeoAgent-Thesis
cd GeoAgent-Thesis
git init

```

### Step 2：复制模板

```
cp -r /path/to/DION-AI-Research-Toolkit/templates/project_ai/* .

```

Windows PowerShell：

```
Copy-Item -Recurse D:\AI\DION-AI-Research-Toolkit\templates\project_ai\* D:\Projects\GeoAgent-Thesis\

```

### Step 3：链接工具库

```
/path/to/DION-AI-Research-Toolkit/scripts/link_to_project.sh /path/to/GeoAgent-Thesis

```

Windows PowerShell：

```
D:\AI\DION-AI-Research-Toolkit\scripts\link_to_project.ps1 -ProjectPath "D:\Projects\GeoAgent-Thesis"

```

### Step 4：在 Trae / Codex 中调用

```
请先读取 .ai/PROJECT_RULES.md 和 .ai/toolkit/ROUTER.md。

```

***

## 15. 推荐 Git 忽略规则

在工具库根目录创建 `.gitignore`：

```
# OS
.DS_Store
Thumbs.db

# Python
__pycache__/
*.pyc
.venv/
venv/

# Generated figures
outputs/
*.png
*.pdf

# Temporary files
tmp/
temp/

# Local notes
.local/

```

在业务项目中可使用：

```
# AI toolkit link
.ai/toolkit

# Generated figure outputs if not intended to commit
figures/outputs/*.png
figures/outputs/*.pdf

# Python
__pycache__/
*.pyc
.venv/
venv/

```

注意：

如果你希望论文图片进入 Git，则不要忽略：

```
figures/outputs/

```

***

## 16. 维护策略

### 更新 writing prompt library

如果是直接 clone：

```
cd prompt-libraries/awesome-ai-research-writing
git pull

```

如果是 submodule：

```
git submodule update --remote prompt-libraries/awesome-ai-research-writing

```

### 更新 figures4papers

如果你复制的是 `scientific-figure-making`，建议重新拉取并覆盖：

```
git clone https://github.com/ChenLiu-1996/figures4papers.git tmp_figures4papers
rm -rf skills/scientific-figure-making
cp -r tmp_figures4papers/scientific-figure-making skills/scientific-figure-making
rm -rf tmp_figures4papers

```

Windows PowerShell：

```
git clone https://github.com/ChenLiu-1996/figures4papers.git tmp_figures4papers
Remove-Item -Recurse -Force skills\scientific-figure-making
Copy-Item -Recurse tmp_figures4papers\scientific-figure-making skills\scientific-figure-making
Remove-Item -Recurse -Force tmp_figures4papers

```

***

## 17. 标准任务调用模板

以后在任意项目中，可以直接使用：

```
请先读取：

.ai/PROJECT_RULES.md
.ai/toolkit/ROUTER.md
.ai/toolkit/prompts/paper_figure_full_pipeline.md

任务：
[填写你的任务]

输入：
[填写数据、论文段落、实验结果或目标]

要求：
1. 绘图使用 scientific-figure-making。
2. 写作参考 awesome-ai-research-writing。
3. 先生成图，再生成图注和分析段落。
4. 检查图表是否支撑 claim。
5. 所有文件保存到当前项目，不要修改 toolkit 源文件。

```

***

## 18. 最终推荐使用方式

长期使用时，保持以下结构：

```
D:\AI\
└── DION-AI-Research-Toolkit\

D:\Projects\
├── GeoAgent-Thesis\
│   └── .ai\toolkit -> D:\AI\DION-AI-Research-Toolkit
├── WorldQuant-Agent\
│   └── .ai\toolkit -> D:\AI\DION-AI-Research-Toolkit
├── Embodied-AI-Guide\
│   └── .ai\toolkit -> D:\AI\DION-AI-Research-Toolkit
└── ScamShield\
    └── .ai\toolkit -> D:\AI\DION-AI-Research-Toolkit

```

原则：

- 工具库负责通用能力；
- 每个项目只写自己的 `PROJECT_RULES.md`；
- Trae / Trae\_CN 通过显式路径读取；
- Codex 通过全局 skill + 项目 rules 调用；
- 不要在业务项目里重复复制两个外部仓库；
- 不要让 Agent 随意修改 toolkit 源文件。

````

如果你想直接开做，建议下一步在工具库里先建这 4 个文件：

```text
BUILD.md
ROUTER.md
prompts/paper_figure_full_pipeline.md
templates/project_ai/.ai/PROJECT_RULES.md

````

