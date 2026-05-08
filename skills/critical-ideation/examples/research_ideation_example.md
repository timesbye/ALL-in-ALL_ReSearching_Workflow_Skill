# Research Ideation Example

## Scenario

The user wants research topics that are realistic for a student and not obviously saturated.

## Example Prompt

```text
Read the critical-ideation skill first.

Research area:
LLM agents for scientific workflow automation

Task:
Generate 6 research ideas, pressure-test novelty and feasibility, search recent papers / GitHub repos / benchmarks when needed, and recommend the top 3 topics for a student-sized project.

Requirements:
1. Prefer directions that can be validated with small-scale experiments.
2. Reject ideas that depend on huge compute or private data.
3. For each top idea, include:
   - research question
   - hypothesis
   - method sketch
   - dataset / benchmark
   - baseline
   - evaluation metric
   - novelty risk
   - minimum experiment
```

## Expected Shape

- problem framing
- initial ideas
- novelty critique
- search findings
- refined ideas
- ranking matrix
- top 3 recommendations with minimum experiments

## Good Outcome Pattern

Strong results usually avoid "train a bigger model" ideas and prefer evaluation harnesses, workflow decomposition, retrieval-quality studies, or benchmark construction that produce publishable evidence with limited resources.
