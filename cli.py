#!/usr/bin/env python3
"""ALL-in-ALL ReSearching Workflow Skill - Interactive CLI"""

import os
import sys
import subprocess
from pathlib import Path

TOOLKIT_ROOT = Path(__file__).resolve().parent
SKILLS_DIR = TOOLKIT_ROOT / "skills"
PROMPTS_DIR = TOOLKIT_ROOT / "prompts"
PROMPT_LIBS_DIR = TOOLKIT_ROOT / "prompt-libraries"

BANNER = r"""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ALL-in-ALL ReSearching Workflow Skill / 一体式科研工作流       ║
║                                                                  ║
║   从文献综述到审稿检查的连续科研工作流 Skill 集合                 ║
║   A sequential research workflow from literature review           ║
║   to reviewer check                                              ║
║                                                                  ╚══════════════════════════════════════════════════════════════════╝
"""

SEPARATOR = "─" * 66


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\n按 Enter 继续 / Press Enter to continue...")


def read_skill_description(skill_name: str) -> str:
    skill_path = SKILLS_DIR / skill_name / "SKILL.md"
    if not skill_path.exists():
        return f"  [Skill 文件未找到: {skill_path}]"
    lines = skill_path.read_text(encoding="utf-8").splitlines()
    desc_lines = []
    in_yaml = False
    in_desc_block = False
    for line in lines:
        stripped = line.strip()
        if stripped == "---":
            if in_yaml:
                in_yaml = False
                in_desc_block = False
            else:
                in_yaml = True
            continue
        if in_yaml:
            if in_desc_block:
                if stripped == "":
                    in_desc_block = False
                    continue
                desc_lines.append(stripped)
            elif stripped.startswith("description:"):
                desc = stripped[len("description:"):].strip()
                desc = desc.lstrip(">-").strip()
                if desc:
                    desc_lines.append(desc)
                else:
                    in_desc_block = True
            continue
        if stripped.startswith("# ") and not desc_lines:
            continue
        if stripped.startswith(">") and not desc_lines:
            continue
        if stripped == "" and not desc_lines:
            continue
        if stripped.startswith("Open `") or stripped.startswith("## Purpose") or stripped.startswith("## When to load"):
            break
        if stripped:
            desc_lines.append(stripped)
    if desc_lines:
        return "  " + "\n  ".join(desc_lines[:5])
    return "  (无描述 / No description)"


def show_main_menu() -> str:
    clear_screen()
    print(BANNER)
    print(SEPARATOR)
    print("  请选择工作模式 / Select Workflow Mode:")
    print()
    print("  [1] 🔄 完整 Workflow / Full Workflow")
    print("      文献综述→论文阅读→选题构思→实验设计→绘图→写作→润色→审稿检查")
    print("      Literature Review → Paper Reading → Critical Ideation →")
    print("      Experiment Design → Figure Making → Scholarly Writing →")
    print("      Academic Polishing → Reviewer Check")
    print()
    print("  [2] 🧩 单模块调用 / Individual Module")
    print("      选择特定功能模块与对应 Skill 进行交互")
    print("      Interact with a specific skill module")
    print()
    print("  [0] 🚪 退出 / Exit")
    print(SEPARATOR)
    while True:
        choice = input("  请输入选项 / Enter choice [0-2]: ").strip()
        if choice in ("0", "1", "2"):
            return choice
        print("  ⚠ 无效输入，请重新选择 / Invalid input, try again")


def show_module_menu() -> str:
    clear_screen()
    print(BANNER)
    print(SEPARATOR)
    print("  模块选择 / Module Selection:")
    print()
    print("  ┌─────────────────────────────────────────────────────────────┐")
    print("  │ [1] 💡 Idea Brainstorm / 选题构思                          │")
    print("  │                                                             │")
    print("  │     核心模块 / Core:                                        │")
    print("  │       • Critical Ideation Skill / 批判性选题 Skill          │")
    print("  │         与 AI 进行对质式 brainstorm，主动质疑、检索、收敛    │")
    print("  │                                                             │")
    print("  │     可联动模块 / Linked Skills:                             │")
    print("  │       • Literature Review Skill / 文献综述 Skill            │")
    print("  │       • Paper Reading Skill / 论文阅读 Skill                │")
    print("  │       • Experiment Design Skill / 实验设计 Skill            │")
    print("  └─────────────────────────────────────────────────────────────┘")
    print()
    print("  ┌─────────────────────────────────────────────────────────────┐")
    print("  │ [2] 📝 Paper Writing / 论文写作                             │")
    print("  │                                                             │")
    print("  │     核心模块 / Core:                                        │")
    print("  │       • Scientific Figure Making Skill / 科研绘图 Skill      │")
    print("  │       • Scholarly Writing Skill / 引导式论文写作 Skill       │")
    print("  │       • Academic Writing Prompt Library / 学术写作 Prompt 库 │")
    print("  │                                                             │")
    print("  │     可联动模块 / Linked Skills:                             │")
    print("  │       • Reviewer Check / 审稿检查                           │")
    print("  └─────────────────────────────────────────────────────────────┘")
    print()
    print("  [0] ↩ 返回主菜单 / Back to Main Menu")
    print(SEPARATOR)
    while True:
        choice = input("  请输入选项 / Enter choice [0-2]: ").strip()
        if choice in ("0", "1", "2"):
            return choice
        print("  ⚠ 无效输入，请重新选择 / Invalid input, try again")


def show_idea_brainstorm_menu() -> str:
    clear_screen()
    print(BANNER)
    print(SEPARATOR)
    print("  💡 Idea Brainstorm / 选题构思")
    print(SEPARATOR)
    print()
    print("  核心交互 / Core Interaction:")
    print()
    print("  [1] 🎯 Critical Ideation / 批判性选题")
    print("      与 Critical Ideation Skill 进行对质式 brainstorm")
    print("      生成候选 idea → 主动质疑 → 检索已有方案 → 收敛推荐")
    print()
    print(read_skill_description("critical-ideation"))
    print()
    print("  ────────────────────────────────────────────────────────────")
    print("  联动模块 / Linked Skills (可在 brainstorm 过程中按需调用):")
    print()
    print("  [2] 📚 Literature Review / 文献综述")
    print("      系统性综述领域现状，识别研究 gap")
    print()
    print("  [3] 📖 Paper Reading / 论文阅读")
    print("      深度阅读关键论文，生成结构化笔记")
    print()
    print("  [4] 🔬 Experiment Design / 实验设计")
    print("      设计实验方案，规划变量控制与消融实验")
    print()
    print("  [5] 🔄 Idea Brainstorm 完整流程 (推荐 / Recommended)")
    print("      文献综述 → 论文阅读 → 批判性选题 → 实验设计")
    print()
    print("  [0] ↩ 返回模块选择 / Back to Module Selection")
    print(SEPARATOR)
    while True:
        choice = input("  请输入选项 / Enter choice [0-5]: ").strip()
        if choice in ("0", "1", "2", "3", "4", "5"):
            return choice
        print("  ⚠ 无效输入 / Invalid input")


def show_paper_writing_menu() -> str:
    clear_screen()
    print(BANNER)
    print(SEPARATOR)
    print("  📝 Paper Writing / 论文写作")
    print(SEPARATOR)
    print()
    print("  核心交互 / Core Interaction:")
    print()
    print("  [1] 📊 Scientific Figure Making / 科研绘图")
    print("      生成论文级 matplotlib 图，导出 PDF/PNG")
    print()
    print(read_skill_description("scientific-figure-making"))
    print()
    print("  [2] ✍️ Scholarly Writing / 引导式论文写作")
    print("      从零构建论文骨架，按章节引导写作")
    print()
    print(read_skill_description("scholarly-writing"))
    print()
    print("  [3] 📋 Academic Writing Prompt Library / 学术写作 Prompt 库")
    print("      润色、翻译、实验分析、reviewer 风格检查")
    print()
    print("  [4] 🔍 Reviewer Check / 审稿检查")
    print("      防止过度 claim，验证结论与证据匹配")
    print()
    print("  [5] 🔄 Paper Writing 完整流程 (推荐 / Recommended)")
    print("      科研绘图 → 引导式写作 → 学术润色 → 审稿检查")
    print()
    print("  [0] ↩ 返回模块选择 / Back to Module Selection")
    print(SEPARATOR)
    while True:
        choice = input("  请输入选项 / Enter choice [0-5]: ").strip()
        if choice in ("0", "1", "2", "3", "4", "5"):
            return choice
        print("  ⚠ 无效输入 / Invalid input")


def generate_task_prompt(skills: list[str], context: str, output_dir: str = "") -> str:
    lines = [
        "请先读取：",
        "",
        "```text",
        ".ai/PROJECT_RULES.md",
        ".ai/toolkit/ROUTER.md",
    ]
    for skill in skills:
        skill_dir = f"skills/{skill}/" if skill != "awesome-ai-research-writing" else "prompt-libraries/awesome-ai-research-writing/"
        lines.append(f".ai/toolkit/{skill_dir}SKILL.md" if skill != "awesome-ai-research-writing" else f".ai/toolkit/{skill_dir}README.md")
    lines.append("```")
    lines.append("")
    lines.append("本次任务：")
    lines.append("")
    lines.append(context)
    lines.append("")
    if output_dir:
        lines.append(f"输出保存到: {output_dir}")
        lines.append("")
    lines.append("要求：")
    lines.append("")
    lines.append("1. 不要修改 .ai/toolkit/ 下的源文件。")
    lines.append("2. 所有输出保存到当前项目。")
    lines.append("3. 只描述数据支持的结论，不虚构结果。")
    return "\n".join(lines)


def show_generated_prompt(prompt: str):
    clear_screen()
    print(BANNER)
    print(SEPARATOR)
    print("  📋 生成的任务提示 / Generated Task Prompt:")
    print(SEPARATOR)
    print()
    for line in prompt.splitlines():
        print(f"  {line}")
    print()
    print(SEPARATOR)
    print()
    print("  将以上提示复制到 Trae / Codex 中执行即可。")
    print("  Copy the prompt above into Trae / Codex to execute.")
    print()


def confirm_project_link() -> bool:
    toolkit_link = Path(".ai/toolkit/ROUTER.md")
    if toolkit_link.exists():
        return True
    print()
    print("  ⚠ 未检测到 .ai/toolkit/ 链接。")
    print("  ⚠ .ai/toolkit/ link not detected.")
    print()
    print("  请先运行链接脚本 / Run the link script first:")
    print()
    print("    PowerShell:")
    print("      .\\scripts\\link_to_project.ps1 -ProjectPath \"<你的项目路径>\"")
    print()
    print("    Bash:")
    print("      ./scripts/link_to_project.sh /path/to/your/project")
    print()
    ans = input("  是否继续生成提示？/ Continue generating prompt anyway? [y/N]: ").strip().lower()
    return ans in ("y", "yes")


SKILL_NAMES = {
    "literature-review": "Literature Review / 文献综述",
    "paper-reading": "Paper Reading / 论文阅读",
    "critical-ideation": "Critical Ideation / 批判性选题",
    "experiment-design": "Experiment Design / 实验设计",
    "scientific-figure-making": "Scientific Figure Making / 科研绘图",
    "scholarly-writing": "Scholarly Writing / 引导式论文写作",
    "awesome-ai-research-writing": "Academic Writing Prompt Library / 学术写作 Prompt 库",
}

FULL_WORKFLOW_STEPS = [
    ("literature-review", "Literature Review / 文献综述", "literature/"),
    ("paper-reading", "Paper Reading / 论文阅读", "literature/"),
    ("critical-ideation", "Critical Ideation / 批判性选题", "ideas/"),
    ("experiment-design", "Experiment Design / 实验设计", "experiments/"),
    ("scientific-figure-making", "Scientific Figure Making / 科研绘图", "figures/"),
    ("scholarly-writing", "Scholarly Writing / 引导式论文写作", "paper/"),
    ("awesome-ai-research-writing", "Academic Polishing / 学术润色", "paper/"),
    ("reviewer-check", "Reviewer Check / 审稿检查", "paper/notes/"),
]


def run_full_workflow():
    clear_screen()
    print(BANNER)
    print(SEPARATOR)
    print("  🔄 完整 Workflow / Full Workflow")
    print(SEPARATOR)
    print()
    print("  工作流步骤 / Workflow Steps:")
    print()
    for i, (skill_id, skill_name, out_dir) in enumerate(FULL_WORKFLOW_STEPS, 1):
        print(f"  Step {i}: {skill_name} → {out_dir}")
    print()
    print(SEPARATOR)
    print()

    if not confirm_project_link():
        return

    prompt = generate_task_prompt(
        skills=[s[0] for s in FULL_WORKFLOW_STEPS],
        context=(
            "执行完整科研工作流 / Execute the full research workflow:\n\n"
            "1. 使用 literature-review 对领域进行系统性综述\n"
            "2. 使用 paper-reading 深度阅读关键论文\n"
            "3. 使用 critical-ideation 生成、质疑、收敛选题方向\n"
            "4. 使用 experiment-design 设计实验方案与消融实验\n"
            "5. 使用 scientific-figure-making 生成论文级图表\n"
            "6. 使用 scholarly-writing 从零构建论文骨架\n"
            "7. 使用 awesome-ai-research-writing 润色论文表达\n"
            "8. 使用 reviewer check 检查 claim 是否过度\n\n"
            "每步完成后保存产物到对应目录，再进入下一步。"
        ),
    )
    show_generated_prompt(prompt)
    pause()


def run_idea_brainstorm(choice: str):
    if choice == "1":
        skills = ["critical-ideation"]
        context = (
            "与 Critical Ideation Skill 进行对质式 brainstorm。\n\n"
            "要求：\n"
            "1. 先做 problem framing\n"
            "2. 生成 5-10 个候选 idea\n"
            "3. 对每个 idea 做强质疑\n"
            "4. 如需判断 novelty 或竞品，主动检索\n"
            "5. 排序并推荐 Top 3\n"
            "6. 输出 idea_report.md, search_log.md, decision_matrix.md, mvp_plan.md"
        )
        out_dir = "ideas/"
    elif choice == "2":
        skills = ["literature-review"]
        context = (
            "对当前研究领域进行系统性文献综述。\n\n"
            "要求：\n"
            "1. 定义综述范围\n"
            "2. 生成搜索策略\n"
            "3. 搜索并收集论文\n"
            "4. 筛选和排序候选论文\n"
            "5. 深度阅读已批准论文\n"
            "6. 综合综述并识别 gap\n"
            "7. 输出到 literature/ 目录"
        )
        out_dir = "literature/"
    elif choice == "3":
        skills = ["paper-reading"]
        context = (
            "深度阅读一篇关键论文，生成结构化研究笔记。\n\n"
            "要求：\n"
            "1. 识别论文元数据\n"
            "2. 结构分解\n"
            "3. 深度分析（新颖性、可复现性、实验严谨性）\n"
            "4. 生成结构化笔记\n"
            "5. 输出到 literature/ 目录"
        )
        out_dir = "literature/"
    elif choice == "4":
        skills = ["experiment-design"]
        context = (
            "设计实验方案，规划变量控制与消融实验。\n\n"
            "要求：\n"
            "1. 形成可测试假设\n"
            "2. 设计实验管线\n"
            "3. 生成实验代码\n"
            "4. 执行与评估\n"
            "5. 迭代决策\n"
            "6. 输出到 experiments/ 目录"
        )
        out_dir = "experiments/"
    elif choice == "5":
        skills = ["literature-review", "paper-reading", "critical-ideation", "experiment-design"]
        context = (
            "执行 Idea Brainstorm 完整流程。\n\n"
            "1. 使用 literature-review 综述领域，识别 gap\n"
            "2. 使用 paper-reading 深度阅读关键论文\n"
            "3. 使用 critical-ideation 生成、质疑、收敛选题\n"
            "4. 使用 experiment-design 为选中方向设计实验\n\n"
            "每步完成后保存产物到对应目录，再进入下一步。"
        )
        out_dir = ""
    else:
        return

    if not confirm_project_link():
        return

    prompt = generate_task_prompt(skills, context, out_dir)
    show_generated_prompt(prompt)
    pause()


def run_paper_writing(choice: str):
    if choice == "1":
        skills = ["scientific-figure-making"]
        context = (
            "生成论文级科研图表。\n\n"
            "要求：\n"
            "1. 生成可复现的 Python matplotlib 脚本\n"
            "2. 导出 PDF 和 PNG\n"
            "3. 脚本保存到 figures/scripts/\n"
            "4. 图像保存到 figures/outputs/\n"
            "5. 同时生成中文图注和结果分析草稿"
        )
        out_dir = "figures/"
    elif choice == "2":
        skills = ["scholarly-writing"]
        context = (
            "从零构建论文骨架，按章节引导写作。\n\n"
            "要求：\n"
            "1. 确定论文类型和范围\n"
            "2. 构建论文骨架\n"
            "3. 逐章节写作（摘要→引言→相关工作→方法→实验→讨论→结论）\n"
            "4. 跨章节一致性检查\n"
            "5. 保存草稿到 paper/ 目录"
        )
        out_dir = "paper/"
    elif choice == "3":
        skills = ["awesome-ai-research-writing"]
        context = (
            "使用学术写作 Prompt 库进行润色、翻译或审稿检查。\n\n"
            "可选任务：\n"
            "1. 中文论文润色\n"
            "2. 英文论文润色\n"
            "3. 中译英学术翻译\n"
            "4. 英译中学术翻译\n"
            "5. 实验结果分析\n"
            "6. Reviewer 风格检查"
        )
        out_dir = "paper/"
    elif choice == "4":
        skills = ["awesome-ai-research-writing"]
        context = (
            "从 Reviewer 视角检查论文片段。\n\n"
            "检查角度：\n"
            "1. 研究问题是否清晰\n"
            "2. 方法动机是否充分\n"
            "3. 贡献是否过度声称\n"
            "4. 实验是否支撑结论\n"
            "5. 是否存在逻辑跳跃\n"
            "6. 术语不一致\n"
            "7. AI 味过重\n\n"
            "输出: Major Issues / Minor Issues / Suggested Revision / Risk Level"
        )
        out_dir = "paper/notes/"
    elif choice == "5":
        skills = ["scientific-figure-making", "scholarly-writing", "awesome-ai-research-writing"]
        context = (
            "执行 Paper Writing 完整流程。\n\n"
            "1. 使用 scientific-figure-making 生成论文级图表\n"
            "2. 使用 scholarly-writing 从零构建论文骨架并逐章节写作\n"
            "3. 使用 awesome-ai-research-writing 润色论文表达\n"
            "4. 使用 reviewer check 检查 claim 是否过度\n\n"
            "每步完成后保存产物到对应目录，再进入下一步。"
        )
        out_dir = ""
    else:
        return

    if not confirm_project_link():
        return

    prompt = generate_task_prompt(skills, context, out_dir)
    show_generated_prompt(prompt)
    pause()


def main():
    while True:
        main_choice = show_main_menu()
        if main_choice == "0":
            clear_screen()
            print("\n  👋 再见 / Goodbye!\n")
            sys.exit(0)
        elif main_choice == "1":
            run_full_workflow()
        elif main_choice == "2":
            while True:
                module_choice = show_module_menu()
                if module_choice == "0":
                    break
                elif module_choice == "1":
                    while True:
                        idea_choice = show_idea_brainstorm_menu()
                        if idea_choice == "0":
                            break
                        run_idea_brainstorm(idea_choice)
                elif module_choice == "2":
                    while True:
                        writing_choice = show_paper_writing_menu()
                        if writing_choice == "0":
                            break
                        run_paper_writing(writing_choice)


if __name__ == "__main__":
    main()
