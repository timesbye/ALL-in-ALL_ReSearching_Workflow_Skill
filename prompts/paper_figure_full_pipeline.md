# 论文图表完整流水线

请完成从实验数据到论文表达的完整流水线。

需要使用：

- `skills/scientific-figure-making/`：负责绘图脚本与图像输出
- `prompt-libraries/awesome-ai-research-writing/`：负责图注、实验分析、论文表达润色
- `prompts/reviewer_check.md`：负责检查图表是否足以支撑论文 claim

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
