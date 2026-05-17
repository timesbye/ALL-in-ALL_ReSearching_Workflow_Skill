---
name: experiment-design
description: Use for designing, planning, and iteratively executing scientific experiments. This skill helps researchers formulate hypotheses, design experiment pipelines, generate experiment code, run evaluation loops, and iterate based on results. Inspired by the autoresearch paradigm of hypothesis-experiment-evaluation-iteration cycles.
---

# Experiment Design

> **设计灵感与参考来源**：本 Skill 的概念参考自 [wjgoarxiv/autoresearch-skill](https://github.com/wjgoarxiv/autoresearch-skill)（MIT License，受 Karpathy autoresearch 启发的自主实验循环 Skill）。本目录中的文档为 ALL-in-ALL_ReSearching_Workflow_Skill 项目基于其理念编写的使用指南，不包含 autoresearch-skill 的原始代码。

Open `templates/` only as needed. Start from the workflow below.

## Purpose

Use this skill when the user needs to design, plan, or execute scientific experiments — from hypothesis formulation to code implementation to result evaluation.

This skill fills the gap between "having a research direction" and "having experimental results to visualize":

- `critical-ideation` gives you a direction
- `experiment-design` helps you test it
- `scientific-figure-making` helps you visualize the results

## When to use

Use this skill when the user asks to:

- design an experiment
- plan experiment pipeline
- write experiment code
- set up evaluation metrics
- run an experiment loop
- iterate on experiment results
- debug experiment code
- compare experiment configurations
- 设计实验
- 写实验代码
- 实验规划
- 评估指标
- 调参
- 消融实验

## When not to use

Do not use this skill for:

- brainstorming ideas (use `critical-ideation`)
- generating figures (use `scientific-figure-making`)
- writing papers (use `scholarly-writing`)
- polishing text (use `awesome-ai-research-writing`)

## Core workflow

### Stage 1: Hypothesis formulation

Transform the research direction into a testable hypothesis:

```text
Hypothesis:
- Claim: [What we believe will happen]
- Independent variable: [What we change]
- Dependent variable: [What we measure]
- Control: [What we keep constant]
- Prediction: [Expected outcome if hypothesis is correct]
```

A good hypothesis is:
- Specific and testable
- Falsifiable
- Connected to the research direction from `critical-ideation`

### Stage 2: Experiment design

Design the experiment pipeline:

1. **Data**: What data do we need? How to prepare it?
2. **Method**: What is the algorithm / model / approach?
3. **Baselines**: What do we compare against?
4. **Metrics**: How do we measure success?
5. **Ablation**: What components do we isolate?
6. **Hyperparameters**: What do we tune and what is the search space?
7. **Compute budget**: How much compute do we have?

```text
Experiment Design
- Dataset:
- Method:
- Baselines:
- Primary metric:
- Secondary metrics:
- Ablation plan:
- Hyperparameter search:
- Compute budget:
- Expected runtime:
```

### Stage 3: Code implementation

Generate experiment code following these principles:

1. **Reproducibility**: Set random seeds, log all configurations
2. **Modularity**: Separate data loading, model, training, evaluation
3. **Logging**: Log metrics, configurations, and checkpoints
4. **Configuration**: Use config files or argparse, not hardcoded values
5. **Error handling**: Catch and report failures clearly

Save code to the target project's `experiments/` directory:

```text
experiments/
|-- config.yaml
|-- data.py
|-- model.py
|-- train.py
|-- evaluate.py
|-- run.sh
`-- results/
    |-- metrics.json
    `-- checkpoints/
```

### Stage 4: Execution and evaluation

Run the experiment and collect results:

1. Execute the pipeline
2. Collect metrics on train/val/test splits
3. Compare against baselines
4. Run ablation studies
5. Record all results in a structured format

```text
Results Template:
- Method: [name]
- Metric 1: [value] (baseline: [value], improvement: [%])
- Metric 2: [value] (baseline: [value], improvement: [%])
- Runtime: [time]
- Notes: [observations]
```

### Stage 5: Iteration

Based on results, decide what to do next:

1. **If results match hypothesis**: Proceed to figure making and writing
2. **If results partially match**: Identify which components work and which don't, refine and re-run
3. **If results contradict hypothesis**: Re-examine assumptions, consider alternative explanations, potentially go back to `critical-ideation`

Iteration principles:
- Change one variable at a time
- Keep a detailed experiment log
- Don't cherry-pick results
- Be honest about negative results

### Stage 6: Save experiment artifacts

Save all artifacts to the target project:

- Code: `experiments/`
- Results: `experiments/results/`
- Experiment log: `experiments/experiment_log.md`
- Data summary: `data/`

## Default output structure

```text
1. Hypothesis Formulation
2. Experiment Design
3. Code Implementation
4. Execution & Evaluation
5. Iteration Decision
6. Experiment Log
```

## Style rules

- Every experiment must have a clear hypothesis before coding
- Log all configurations for reproducibility
- Report negative results honestly
- Compare against fair baselines
- Use appropriate statistical tests when needed
- Don't overfit to the test set
- Keep experiment code clean and well-structured

## Templates

Use these bundled files as needed:

- `templates/experiment_design.md`
  Use when designing the experiment pipeline.
- `templates/experiment_log.md`
  Use when recording experiment iterations and results.
