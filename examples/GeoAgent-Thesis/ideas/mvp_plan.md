# MVP Plan

## Selected Idea

GeoAgent-Router

## MVP Goal

Prove that a simple latency-aware selection policy can turn the existing GeoAgent family into a deployment story, not just a leaderboard story.

## Core User Scenario

A practitioner wants the best available reasoning quality under a bounded response-time budget and does not want to always pay the full cost of the largest variant.

## Minimum Feature Set

1. Define 2-3 latency budget bands.
2. Map each budget band to a variant-selection policy.
3. Produce a figure and analysis showing what quality is gained or given up under each policy.

## Main Risks

- The current dataset may be too small to justify a routing narrative.
- A naive router may look trivial if it only re-labels fixed model choices.
- The claim becomes weak if "acceptable latency" is never defined explicitly.

## Kill Criteria

- If routing adds no clear story beyond "pick a smaller model when you want speed".
- If there is no measurable budget-based improvement over static selection.
- If the demo cannot explain when and why each variant should be chosen.

## Next Actions

1. Use the current table to establish the baseline quality-latency curve.
2. Add one simple routing-policy simulation.
3. Decide whether the next iteration should become a research benchmark or a deployment tool.
