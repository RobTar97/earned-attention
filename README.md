# Earned Attention

**Hooks, scripts, copy, and retention audits for AI agents.**

[![Validate](https://github.com/RobTar97/earned-attention/actions/workflows/validate.yml/badge.svg)](https://github.com/RobTar97/earned-attention/actions/workflows/validate.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-limegreen)](LICENSE)
[![skills.sh](https://skills.sh/b/RobTar97/earned-attention)](https://skills.sh/RobTar97/earned-attention)

Turn an idea or a weak draft into content a viewer has a reason to watch—and a payoff worth staying for.

Earned Attention is a reusable agent skill for TikTok, Instagram Reels, YouTube Shorts, educational YouTube videos, marketing copy, and content planning. It combines audience psychology with concrete scripting, production decisions, and honest measurement. Give your agent a brief, script, outline, or retention data; get creative you can use and a focused next experiment.

## Install

```bash
npx skills add RobTar97/earned-attention --skill psychological-content-strategy
```

Choose your agent in the installer. For a project installation targeting Codex directly:

```bash
npx skills add RobTar97/earned-attention --skill psychological-content-strategy --agent codex
```

The npm [`skills` CLI](https://www.npmjs.com/package/skills) downloads the skill from this GitHub repository. The command and layout follow the [official CLI documentation](https://skills.sh/docs/cli) and [upstream skill format](https://github.com/vercel-labs/skills#creating-skills).

Need global installation, Claude Code, Windows copy mode, updates, or troubleshooting? Read [Installation](docs/installation.md).

## Try it

Starting without a brief? Try:

```text
Use psychological-content-strategy. Help me get started with a video
for my brand. Ask what matters, then show me three hook directions
that fit my audience and voice before we choose one.
```

The agent asks up to three focused questions at a time, reuses your answers, and builds a short working brief. Hook choices include real opening words, a first-frame idea, why they fit, and the proof/payoff needed. It recommends a direction and waits when you ask to choose together. A complete brief can go straight to drafting:

```text
Use psychological-content-strategy to write a 30-second Reel for a
project checklist app. It saves and reuses checklists; it does not
automate tasks. Audience: small agency team leads. Give three hook
angles, a timed script, screen-demo directions, and one free-trial CTA.
```

In Codex, you can explicitly invoke `$psychological-content-strategy`. Invocation and automatic discovery vary by agent; the installed skill's name and description help the agent select it.

Provide the audience, desired outcome, available proof, and production limits. The skill works with partial briefs, but it labels assumptions and missing evidence rather than inventing features or results.

## What you get

| Request | Deliverable |
|---|---|
| Help me get started | Short intake, working brief, three brand-matched hook directions, and a recommendation before the requested next step |
| Find angles from customer material | Source-linked findings, scoped claim register, distinct angles, proof requirements, and remaining unknowns |
| Create a short | Distinct hook angles, a selected opening, timed beat table, capture/edit notes, and one test |
| Plan or write an educational video | Learning contract, research gaps, audience depth, Point A → Point B arc, causal outline or requested script |
| Improve a draft | Prioritized problems tied to the supplied evidence, followed by a complete rewrite |
| Write copy | Headlines, catchcopy, captions, or sales copy matched to audience awareness and voice |
| Diagnose retention | Observations, plausible explanations, evidence gaps, and a controlled-variable experiment |
| Diagnose lead quality or reuse account lessons | Stage-specific hypotheses, supported contribution limits, contextual learning records, and a bounded next step |
| Plan a series | Audience moments, useful messages, proof, brand cues, CTAs, and separate recognition/acquisition measures |

English is supported by default; Japanese catchcopy and localization guidance are available when requested. Examples include product demonstrations, educational Shorts, project-checklist copy, and brand/trial content plans.

The [hook-pattern guide](skills/psychological-content-strategy/references/hook-patterns.md) adds 24 confession, experiment, contrarian, and lesson starters, with truth requirements, matching payoffs, and a method for studying successful creative.

The [five-phase educational-scriptwriting guide](skills/psychological-content-strategy/references/educational-scriptwriting.md) adds Foundation, Target, Structure, Draft, and Refine: packaging and shared value, research gaps, honest transformation, useful critique, causal transitions, and spoken rhythm. It scales those ideas to short and longer formats. The [supplied framework and transcript](skills/psychological-content-strategy/references/source-material/viral_scriptwriting_framework_and_transcript.md) is preserved separately for detailed reference.

The [viewer-first content principles](skills/psychological-content-strategy/references/content-principles.md) help the agent write to one recognizable person, show useful value early, connect each line, use concrete evidence, and answer likely objections. They guide the writing silently; your requested output determines whether you get finished copy, a production plan, or an explained critique.

The [Master Blueprint adaptation](skills/psychological-content-strategy/references/short-form-optimization.md) connects PAS, BAB, AIDA, FAB, and Picture/Promise/Proof/Push to visible evidence, honest presenter roles, useful sharing, and paid-funnel diagnosis. [Progressive story arcs](skills/psychological-content-strategy/references/story-arcs.md) add rapid context and meaningful mini payoffs from the supplied video. The [metric dictionary](skills/psychological-content-strategy/references/analytics-testing.md#paid-creative-metric-dictionary) names each denominator instead of treating source benchmark tables as universal targets.

## How it works

The [guided-intake workflow](skills/psychological-content-strategy/references/guided-intake.md) helps a new user specify the deliverable, viewer, goal, voice, and available material. It loads the relevant hook, brand, and evidence references to shape concrete choices. You can choose a direction, combine options, or ask the agent to choose and write. Complete briefs and small copy requests skip unnecessary intake.

The [evidence-to-angle workflow](skills/psychological-content-strategy/references/evidence-to-angles.md) connects customer observations to supportable claims and genuinely different creative concepts. The [commercial-learning guide](skills/psychological-content-strategy/references/commercial-learning.md) keeps qualified outcomes, contribution assumptions, attribution, and reusable lessons separate. Voice cards and essential-shot availability/fallback checks extend the existing production guide. Real customer/account records stay in project storage; the installed skill contains empty templates and fictional examples.

```mermaid
flowchart LR
  A[Audience and situation] --> B[Credible promise]
  B --> C[Early proof]
  C --> D[Meaningful progress]
  D --> E[Complete payoff]
  E --> F[Useful next step]
  F --> G[Measure and test]
  G --> B
```

1. Understand the viewer's situation and the asset's job.
2. Choose a relevant message and an answerable curiosity gap.
3. Match the first frame, spoken opening, headline, and sound.
4. Deliver proof and small payoffs through meaningful beats.
5. Make editing, captions, and audio support understanding.
6. Connect the ending to one appropriate next step.
7. Test the largest uncertainty with clear measures and guardrails.

The skill uses psychology to improve relevance, clarity, trust, and memory. It qualifies numerical rules, avoids invented evidence, and treats retention-curve patterns as hypotheses. It does not promise virality or neurochemical effects from editing.

## A sample output

For a 30-second demonstration, expect a table like this, expanded into shootable beats:

| Time | Spoken line | Visual/proof | On-screen copy | Audio/edit | Purpose |
|---|---|---|---|---|---|
| 0–3 | A specific, supported promise | Show the actual output | One clear headline | Voice starts immediately | Relevance and proof |
| 3–22 | Explain the workflow in useful steps | Demonstrate the real controls | Progress labels | Cut on meaningful change | Comprehension and progress |
| 22–27 | State the completed result | Hold the finished example | Concise takeaway | Give the result reading time | Payoff |
| 27–30 | One appropriate action | Clear destination or next step | One CTA | Simple ending | Action |

Timing is a production plan until rehearsed. See [Example prompts](docs/examples.md) and the [worked examples](skills/psychological-content-strategy/references/templates-examples.md).

## Documentation

- [Installation](docs/installation.md): install, inspect, update, remove, and troubleshoot.
- [Example prompts](docs/examples.md): practical briefs for each mode.
- [Workflow and reference map](docs/workflow.md): what the agent reads and returns.
- [Evidence and evaluations](docs/evidence.md): source provenance, qualifications, and testing limits.
- [Skill instructions](skills/psychological-content-strategy/SKILL.md): the complete agent workflow.
- [Contributing](CONTRIBUTING.md): improve the skill, docs, and examples.

## Repository layout

```text
skills/psychological-content-strategy/
  SKILL.md                       # Main workflow and routing
  LICENSE                        # License travels with installed copies
  references/                    # Fourteen focused guides + source fingerprints
    source-material/             # Supplied framework/transcript and attribution
docs/                            # Human-facing documentation
evals/                           # Initial tasks and focused workflow checks
scripts/validate.py              # Dependency-free structural validation
skills.sh.json                   # Catalog display configuration
```

The runtime skill consists of Markdown, a source-provenance JSON file, and its license. It has no required API keys, application dependency, or executable runtime code. Browsing or media tools are used only when the requested task needs them. Actual recording, rendering, and publishing use a separate authorized workflow.

## Validation

```bash
python scripts/validate.py
npx skills add . --list
```

The initial version was checked with three task pairs: product-demo scripting, retention audit/rewrite, and bilingual copy with a brand/acquisition plan. The skill-assisted responses passed 24/24 workflow expectations; the baseline passed 22/24. These small, author-graded checks demonstrate specified behavior, not measured audience retention or conversion lift. Details are in [Evidence and evaluations](docs/evidence.md).

## License and attribution

[MIT](LICENSE), for this repository's original skill instructions, synthesis, documentation, and examples. Linked studies, books, platform documentation, and source materials remain subject to their respective rights and terms. The original supplied playbooks are acknowledged in [source notes](skills/psychological-content-strategy/references/sources-evidence.md) and are not redistributed in full.

Maintained by [RobTar97](https://github.com/RobTar97). See [CHANGELOG.md](CHANGELOG.md) for releases.
