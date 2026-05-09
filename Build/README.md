# Build 文件夹

本目录包含 DION-AI-Research-Toolkit 的构建指南和相关文档。

## 文件说明

| 文件 | 说明 |
|---|---|
| `BUILD.md` | 主构建指南：从零搭建整个 Toolkit 的完整步骤，包括目录结构、外部仓库引入、Prompt 入口、项目模板、安装脚本、使用方式等 |
| `BUILD_skill3.md` | 第三个核心 Skill `critical-ideation` 的专项构建指南：Skill 定位、目录结构、核心文件 SKILL.md、模板、示例、路由规则、调用模板等 |

## 相关文件（位于仓库其他位置）

- `scripts/install_to_codex.ps1` / `scripts/install_to_codex.sh`：将 Toolkit Skills 安装到 Codex 全局目录
- `scripts/link_to_project.ps1` / `scripts/link_to_project.sh`：将 Toolkit 链接到目标项目的 `.ai/toolkit/`
- `templates/project_ai/`：新科研项目的最小模板
- `ROUTER.md`：运行时路由规则（位于仓库根目录）
