---
name: critical-ideation
description: Use for brainstorming, research directions, product concepts, PRD improvements, startup ideas, agent workflow design, project differentiation, novelty checks, competitor-aware ideation, and "is this idea actually good/feasible?" requests. This skill pressure-tests ideas, searches existing work when current information matters, ranks options, and converges on MVPs instead of doing vague brainstorming.
---

# Critical ideation

Open `templates/` and `examples/` only as needed. Start from the workflow below, then load the specific template or example that matches the user's task.

## Purpose

Use this skill when the user wants to move from vague ideas to evidence-aware, critic-tested, executable directions.

This is not a free-association brainstorming skill. It should:

- generate candidate ideas
- challenge each idea directly
- search for existing work when novelty, feasibility, or market context depends on current information
- refine ideas after critique
- rank options explicitly
- recommend only the ideas worth building

## When to use

Use this skill when the user asks for:

- brainstorm ideas
- brainstorm research directions
- product differentiation
- PRD optimization
- startup idea validation
- project differentiation
- competitor-aware ideation
- adversarial critique of an idea
- agent workflow design
- self-media topic ideation
- paper idea or novelty check
- 找 idea
- 选题构思
- 产品差异化
- 项目创新点
- 竞品对比
- 项目方向判断
- “有没有更好的方向”
- “这个想法是否可行”
- “帮我质疑一下这个 idea”
- “帮我看看是不是已经有人做过”
- “帮我找更有差异化的切入点”

## When not to use

Do not use this skill for:

- simple text polishing
- ordinary translation
- purely emotional support
- deterministic coding tasks
- ordinary figure generation
- pure summarization without ideation
- tasks where the user wants direct execution but not idea evaluation

For writing tasks, use the academic writing prompt library.

For figure tasks, use the scientific figure making skill.

## Core workflow

### Stage 1: Clarify the ideation target

Identify:

- Domain
- User goal
- Target audience
- Current idea
- User constraints
- Available resources
- Technical capacity
- Time horizon
- Expected output type
- Success criteria

If the user already provided enough context, do not stop to ask follow-up questions. Proceed with reasonable assumptions and mark them clearly.

Default section:

```text
Problem Framing
- Domain:
- Goal:
- Target user / reader:
- Constraints:
- Available resources:
- Success criteria:
- Assumptions:
```

### Stage 2: Generate initial ideas

Generate 5-10 candidate ideas unless the user asked for a different count.

Each idea should include:

- Idea name
- One-sentence concept
- Target user / problem
- Why now
- Core mechanism
- Expected value
- Minimum viable version

Avoid vague names like "AI Assistant" or "Smart Platform". Prefer specific, testable concepts.

### Stage 3: Attack each idea

Critique every idea directly. Do not soften obviously weak ideas.

Use at least five of these angles:

1. Novelty risk  
   Has this already been done?
2. Feasibility risk  
   Can the user realistically build it with current resources?
3. Data or resource risk  
   Does it require unavailable data, compute, permissions, users, or APIs?
4. Differentiation risk  
   Why would anyone choose this over existing tools or methods?
5. Evaluation risk  
   How can success be measured?
6. Research or publication risk  
   If it is a research idea, is there enough novelty and experimental support?
7. Business or monetization risk  
   If it is a product idea, is there a real user pain point and payment scenario?
8. Legal or platform risk  
   Does it rely on scraping, copyrighted data, automation restrictions, privacy-sensitive information, or blocked APIs?
9. Demo risk  
   Can a convincing demo be built quickly?

### Stage 4: Search existing work when current information matters

When novelty, feasibility, market context, platform rules, benchmarks, papers, products, GitHub repos, policies, or competitors may have changed recently, search before making a strong judgment.

Search for:

- existing products
- GitHub repositories
- recent papers
- benchmarks and datasets
- competitors
- policy or platform restrictions

Record:

- what you searched
- what you found
- which existing solutions are close
- what differentiation space remains

If no search was performed, say so explicitly:

```text
No web search was performed in this round, so novelty / competitor judgment may be incomplete.
```

### Stage 5: Refine ideas

After critique and search, narrow, reshape, merge, or discard ideas.

Good refinements usually:

- reduce scope
- sharpen the user or reviewer value
- make the mechanism clearer
- remove fragile dependencies
- improve demoability

### Stage 6: Rank ideas

Use an explicit matrix. Prefer 1-5 scoring.

Default dimensions:

- Feasibility
- Differentiation
- User Value
- Demo Potential
- Novelty
- Fit

For research tasks, emphasize:

- Novelty
- Feasibility
- Evaluation Clarity
- Dataset Availability
- Publication Potential
- Fit

For product tasks, emphasize:

- User Pain
- Differentiation
- Feasibility
- Distribution
- Monetization
- Demo Potential

Recommend no more than three top ideas by default.

### Stage 7: Recommend only the ideas worth building

The final recommendation should not repeat the full idea dump. It should name:

- the best options
- why they survived
- why weaker options were rejected

### Stage 8: Produce an MVP plan

For each top recommendation, give:

- MVP goal
- core user scenario
- minimum feature set
- out-of-scope items
- technical path
- required data / APIs
- evaluation method
- main risks
- kill criteria
- next actions

## Default output structure

Unless the user asked for a different format, structure the answer like this:

```text
1. Problem Framing
2. Initial Ideas
3. Critical Objections
4. Search Findings
5. Refined Ideas
6. Ranking Matrix
7. Recommended Top Ideas
8. MVP Execution Plan
9. Risks and Unknowns
10. Next Actions
```

Do not stop at a raw idea list.

## Style rules

- Be direct.
- Do not flatter weak ideas.
- Prefer mechanisms over slogans.
- Separate assumptions from evidence.
- Separate speculation from search findings.
- Mark uncertainty clearly.
- Give executable next steps.
- Prioritize ideas the user can actually prototype.
- Do not invent sources, competitors, papers, or market facts.
- If an idea is not worth building, say so.
- If an idea is promising but too broad, narrow it.
- If an idea is already common, find a more specific angle.

## Default priorities

Prefer ideas that:

1. can be prototyped within days or weeks
2. can become GitHub projects, demos, PRDs, papers, or self-media content
3. leverage LLM, Agent, VLM, embodied AI, research workflow, or academic productivity
4. do not require huge compute, inaccessible private data, or complex business licensing
5. can produce a visible artifact such as a demo, benchmark, paper draft, PRD, GitHub repo, video, figure, or workflow template

## Common task modes

### Mode A: Research idea brainstorm

Use when the user wants academic research directions.

Extra criteria:

- Literature novelty
- Dataset availability
- Evaluation method
- Compute requirement
- Publication risk
- Baseline feasibility

Output should include:

- Research question
- Hypothesis
- Method sketch
- Dataset / benchmark
- Baseline
- Evaluation metric
- Main novelty risk
- Minimum experiment

### Mode B: Product idea brainstorm

Use when the user wants product or startup ideas.

Extra criteria:

- Target user
- User pain
- Existing alternatives
- Differentiation
- MVP scope
- Distribution channel
- Monetization possibility
- Legal or platform risk

Output should include:

- User scenario
- Core feature
- MVP
- Competitor comparison
- Demo plan
- Risk

### Mode C: Agent workflow brainstorm

Use when the user wants to design AI agent systems.

Extra criteria:

- Agent roles
- Tool calls
- Memory
- Human-in-the-loop points
- Failure modes
- Evaluation harness
- Guardrails
- Cost and latency

Output should include:

- Agent architecture
- Workflow steps
- Required tools
- Input / output schema
- Failure cases
- Evaluation harness
- MVP implementation plan

### Mode D: Self-media topic brainstorm

Use when the user wants content ideas.

Extra criteria:

- Hook strength
- Audience resonance
- Filming feasibility
- Differentiation from existing content
- Series potential
- Personal brand fit
- Risk of looking generic or forced

Output should include:

- Title
- Opening hook
- Core conflict
- Content structure
- Why audience cares
- Filming plan
- Risk

## Templates and examples

Use these bundled files as needed:

- `templates/idea_card.md`
  Use when you need a per-idea evaluation sheet.
- `templates/search_log.md`
  Use when search findings should be recorded explicitly.
- `templates/decision_matrix.md`
  Use when multiple ideas need side-by-side ranking.
- `templates/critique_checklist.md`
  Use when pressure-testing a promising idea before recommendation.
- `templates/mvp_plan.md`
  Use when turning a top idea into an executable first version.
- `examples/product_ideation_example.md`
  Use as a pattern for PRD, startup, or product differentiation work.
- `examples/research_ideation_example.md`
  Use as a pattern for research topic and novelty evaluation work.
- `examples/agent_workflow_ideation_example.md`
  Use as a pattern for multi-agent or workflow architecture design.
