# Agent Workflow Ideation Example

## Scenario

The user already has an agent workflow idea but wants a stronger architecture and clearer failure analysis.

## Example Prompt

```text
Read the critical-ideation skill first.

Current workflow:
A planner agent decomposes a task, a coder agent writes code, and a reviewer agent checks output.

Task:
Critique this workflow, search for similar agent patterns if current ecosystem context matters, propose 3 better architectures, and recommend the best MVP.

Requirements:
1. Focus on failure modes, evaluation, and scalability.
2. Do not assume more agents automatically makes the system better.
3. Include:
   - agent roles
   - tool calls
   - memory design
   - human-in-the-loop points
   - evaluation harness
   - failure cases
   - MVP implementation plan
```

## Expected Shape

- explicit critique of the current workflow
- three candidate architectures
- concrete tradeoffs, not abstract praise
- evaluation harness proposal
- one recommended MVP with guardrails

## Good Outcome Pattern

Strong results usually reduce unnecessary agent count, define clearer ownership boundaries, add measurable evaluation checkpoints, and keep the first version narrow enough to debug.
