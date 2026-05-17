# DEPENDENCIES

This document lists all upstream projects referenced by ALL-in-ALL_ReSearching_Workflow_Skill, along with their version/commit status and usage scope.

## Referenced Projects

| Project | Author | Repository | License | Usage in This Project | Version Status |
|---------|--------|-----------|---------|----------------------|----------------|
| Auto-Scholar | [CAICAIIs](https://github.com/CAICAIIs) | [CAICAIIs/Auto-Scholar](https://github.com/CAICAIIs/Auto-Scholar) | MIT | Design reference for `skills/literature-review/` | Not pinned; concept-level reference |
| DeepPaperNote | [917Dhj](https://github.com/917Dhj) | [917Dhj/DeepPaperNote](https://github.com/917Dhj/DeepPaperNote) | No explicit license | Design reference for `skills/paper-reading/` | Not pinned; concept-level reference |
| autoresearch-skill | [wjgoarxiv](https://github.com/wjgoarxiv) | [wjgoarxiv/autoresearch-skill](https://github.com/wjgoarxiv/autoresearch-skill) | MIT | Design reference for `skills/experiment-design/` | Not pinned; concept-level reference |
| Scholarly | [ShiyangZheng](https://github.com/ShiyangZheng) | [ShiyangZheng/scholarly](https://github.com/ShiyangZheng/scholarly) | No explicit license | Design reference for `skills/scholarly-writing/` | Not pinned; concept-level reference |
| figures4papers | [Chen Liu](https://chenliu-1996.github.io/) (Yale) | [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers) | No explicit license | Design reference and style guide for `skills/scientific-figure-making/` | Not pinned; concept-level reference |
| awesome-ai-research-writing | [Leey21](https://github.com/Leey21) | [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) | No explicit license | Referenced as external Prompt library for academic writing | See `prompt-libraries/awesome-ai-research-writing/README.md` for commit pinning (requires cloning the upstream repository first). |

## v4 New References

| Project | Author | Reference | License | Usage in This Project | Version Status |
|---------|--------|-----------|---------|----------------------|----------------|
| PaperOrchestra | Google Cloud AI Research | [arxiv.org/abs/2604.05018](https://arxiv.org/abs/2604.05018) | Academic | Citation verification, structured JSON outline, VLM review loop, review-rollback mechanism | Concept-level reference |
| AI Scientist-v2 | Sakana AI / Oxford / UBC | [github.com/SakanaAI/AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) | Academic | VLM figure review, multi-perspective review | Concept-level reference |
| Google AI Co-Scientist | Google Research | [arxiv.org/abs/2502.18864](https://arxiv.org/abs/2502.18864) | Academic | Generate-Debate-Evolve cycle for critical-ideation | Concept-level reference |
| LiRA | Academic research | [arxiv.org/abs/2510.05138](https://arxiv.org/abs/2510.05138) | Academic | Citation grounding mechanism for scholarly-writing | Concept-level reference |
| AutoSurvey2 | Academic research | [arxiv.org/abs/2510.26012](https://arxiv.org/abs/2510.26012) | Academic | Parallel section writing mode for scholarly-writing | Concept-level reference |
| Paperguide.ai | Paperguide | [paperguide.ai](https://paperguide.ai/) | Commercial | SJR/SNIP journal quality ranking, Workbooks extraction, Deep Research skill | Concept-level reference |
| ARS (Academic Research Skills) | Edward Cheng-I Wu | [github.com/Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | Open-source (Plugin) | Integrity gate (7-item AI failure mode checklist), anti-flattery protocol | Concept-level reference |
| DeepScientist | Westlake University | [github.com/ResearAI/DeepScientist](https://github.com/ResearAI/DeepScientist) | Open-source | Findings Memory, Bayesian optimization experiment strategy | Concept-level reference |
| AI-Researcher | HKUDS | [github.com/HKUDS/AI-Researcher](https://github.com/HKUDS/AI-Researcher) | No explicit license | Knowledge Acquisition Agent, Idea Generator, Scientist-Bench | Concept-level reference |
| SciDER | William & Mary et al. | [github.com/leonardodalinky/SciDER](https://github.com/leonardodalinky/SciDER) | Open-source | Data Analysis Agent, self-evolving memory, Critic Agent | Concept-level reference |
| Supervisor-Skills | HKUSTDial | [github.com/HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | Open-source | Introduction Flowchart, five-dimension ideation framework, Figure Design Advisor | Concept-level reference |

## API Dependencies (v4 new)

| API | Usage | Required | Fallback |
|-----|-------|----------|----------|
| Semantic Scholar API | Citation verification in `literature-review` Stage 3.5 and `scholarly-writing` Stage 2.5 | Optional | LLM self-verification (lower confidence) |
| SJR/SNIP data | Journal quality ranking in `literature-review` Stage 4.5 | Optional | Venue tier classification as proxy |
| VLM (Vision Language Model) | Figure quality review in `scientific-figure-making` Stage 3 | Optional | Skip VLM review; manual user review |

### Semantic Scholar API Details

- **Endpoint**: `https://api.semanticscholar.org/graph/v1/paper/search`
- **Rate limit**: 100 requests per 5 minutes (unauthenticated), 1000 per 5 minutes (with API key)
- **Usage**: Verify that cited papers exist and are correctly attributed
- **When unavailable**: Fall back to LLM self-verification with explicit `[LLM-VERIFIED]` marking
- **No API key required**: Basic usage works without authentication; API key recommended for higher rate limits

## Version Policy

- **Concept-level references** (Auto-Scholar, DeepPaperNote, autoresearch-skill, Scholarly, figures4papers, PaperOrchestra, AI Scientist-v2, Google AI Co-Scientist, LiRA, AutoSurvey2, Paperguide.ai): These are design inspirations, not code dependencies. The Skill directories in this project contain original usage guides written based on their concepts, not copies of their code. No version pinning is required.

- **Content-level references** (awesome-ai-research-writing): This is a Prompt library that users clone into the project. Its content directly affects Skill execution quality. Commit pinning is recommended for reproducibility.

- **API dependencies** (Semantic Scholar API): These are optional external services. The project is designed to degrade gracefully when APIs are unavailable.

## Important Notes

- This project does **not** redistribute content from any upstream repository.
- Each Skill directory contains original documentation written by this project, inspired by the upstream design concepts.
- `skills/critical-ideation/` is an original contribution of this project with no upstream dependency.
- `skills/deep-research/` is a v4 new skill inspired by Paperguide.ai's Deep Research feature.
- Users should visit upstream repositories directly and comply with their respective licenses and terms of use.
- API dependencies are optional; all skills function without them but with reduced verification confidence.
