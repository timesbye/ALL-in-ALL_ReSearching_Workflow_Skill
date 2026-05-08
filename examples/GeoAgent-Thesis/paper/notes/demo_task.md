# Demo Task

请先读取：

```text
.ai/PROJECT_RULES.md
.ai/toolkit/ROUTER.md
.ai/toolkit/prompts/paper_figure_full_pipeline.md
paper/context.md
```

本次任务：

基于 `data/results.csv` 生成一张论文级比较图，并写出中文图注、英文图注以及中文实验结果分析段落。

要求：

1. 绘图使用 `.ai/toolkit/skills/scientific-figure-making/`
2. 写作参考 `.ai/toolkit/prompt-libraries/awesome-ai-research-writing/`
3. 绘图脚本保存到 `figures/scripts/`
4. 输出 PDF 和 PNG 到 `figures/outputs/`
5. 图表应突出 GeoAgent 系列在 Accuracy 和 F1 上相对基线模型的提升
6. 可以提及 latency trade-off，但不要过度解释
7. 用 reviewer 视角检查图表是否足以支持 “GeoAgent 在保持可接受推理开销下带来稳定性能提升” 这一 claim
8. 不要修改 `.ai/toolkit/` 下的源文件

期望输出：

- Python matplotlib 脚本
- PDF 图像
- PNG 图像
- 中文图注
- 英文图注
- 中文实验分析段落
- Reviewer 检查意见
