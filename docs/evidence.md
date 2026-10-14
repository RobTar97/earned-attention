# Evidence and evaluations

## Source provenance

The skill is an original practical synthesis of two supplied Markdown playbooks:

1. *Psychological Marketing & High-Retention Content Strategy: A Master Playbook for Short-Form Video, Copywriting, and Subconscious Engagement.*
2. *Short-Form Video Retention Playbook: TikTok, Instagram Reels and YouTube Shorts.*

Their original authorship, publication dates, and licensing were not established. This repository acknowledges their contribution and does not redistribute the original documents in full. The [source fingerprints](../skills/psychological-content-strategy/references/source-manifest.json) identify the specific supplied versions by filename, size, and hash, without local filesystem paths.

The runtime synthesis is self-contained. It does not require access to the original documents or a particular user's computer.

On 2026-10-14, the user supplied `viral_scriptwriting_framework_and_transcript.md`, which attributes a 17:33 source video to Isaac, `@isaaccverse`. The [supplied file](../skills/psychological-content-strategy/references/source-material/viral_scriptwriting_framework_and_transcript.md) is retained for reference, with separate [source-material notes](../skills/psychological-content-strategy/references/source-material/README.md). Its transcription, attribution, quotations, and satirical claims have not been verified against the video. The [operational adaptation](../skills/psychological-content-strategy/references/educational-scriptwriting.md) integrates its five phases without making a viral-performance promise or adopting its anti-AI directive as a refusal to write. External transcript and quotations are not relicensed under this repository's MIT license. Initial evaluation scores below predate these additions.

Five later user-supplied screenshots add four hook families and a creative-study prompt. Visible credits are `@kienobimedia` and `@kienobifilm`. Their [adapted hook-pattern reference](../skills/psychological-content-strategy/references/hook-patterns.md) preserves the supplied starters and adds specificity, truth, proof, and payoff guidance. The screenshot additions are creative scaffolds, not research findings; the images are not redistributed. Their fingerprints are recorded with the other source notes. The initial model-evaluation scores below predate this addition.

## What was retained

Audience relevance; manageable curiosity; customer-centered storytelling; distinctive brand cues; copy clarity; hooks and covers aligned with the actual payoff; timed short-form structures; meaningful edits; sound hierarchy; accurate captions; retention diagnosis; and hypothesis-led experiments.

## What was qualified

| Idea from the source material | Treatment in the skill |
|---|---|
| A universal 60:40 brand/activation rule | Contextual planning reference; budget and posting mix are separate decisions |
| “Dopamine” from cuts or reveals | Observable creative intent; no neurochemical measurement is implied |
| Universal color or text-position effects | Contextual composition and audience hypotheses |
| Long-form opening rules applied to Shorts | Immediate relevance and useful progress fitted to the requested runtime |
| Fixed cut intervals or retention thresholds | Explicitly labeled production heuristics; account-specific measurement |
| Replay spikes prove quality | Investigate useful replay and confusion/illegibility as alternatives |
| Strong completion guarantees reach or sales | Separate attention, satisfaction, distribution, and business outcomes |

The [complete evidence map](../skills/psychological-content-strategy/references/sources-evidence.md) links to primary platform and research-publisher sources checked during creation. Current platform requirements and exact research claims still need verification when relevant. Some precise source claims were omitted because their original evidence was not established.

## Initial workflow checks

Three prompts were executed in two configurations: with the skill, and a baseline that did not read it. Each task had eight expectations. The prompts and expectations are in [evals.json](../evals/evals.json); a portable result summary is in [summary.json](../evals/summary.json).

| Task | With skill | Baseline | What it exercised |
|---|---|---|---|
| Product-demo Reel | 8/8 | 7/8 | Truthful features, three hooks, timed handoff, one CTA, experiment guardrail |
| Retention audit/rewrite | 8/8 | 8/8 | Evidence and hypotheses, complete payoff, replay interpretation, rate denominators |
| Bilingual copy and brand plan | 8/8 | 7/8 | Scope, product truth, feasible assets, recognition versus acquisition measures |
| **Total** | **24/24** | **22/24** | Specified workflow behavior |

The four timed scripts were also checked programmatically for contiguous ranges, no overlap/gaps, and the requested 30- or 45-second endpoint. Performance timing remained estimated pending rehearsal.

In this sample, the skill added an explicit quality/business guardrail to the product hook test and a direct recognition measure to the brand plan. Most expectations passed in both configurations, so many checks do not distinguish the skill from competent baseline writing.

## Focused educational-workflow checks

The [additional prompts](../evals/educational-scriptwriting.json) exercise two distinct modes: a requested 30-second draft based on the supplied framework, and critique-only coaching for an eight-minute outline. Both were reviewed against four expectations each. The draft delivered the observable lesson despite the source's anti-AI opinion, with continuous 0–30-second beats and no invented personal story or results. Coaching used all five phases, labeled unresearched gaps, and preserved the supplied experience without inventing outcomes. Script/outline ranges were checked for continuity and their requested endpoints. These are focused smoke checks with author review, not a paired benchmark or evidence of audience-performance lift; they do not change the initial scores above.

## What these checks do not establish

There was one response per task/configuration. The skill author graded the outputs with cited evidence; the grading was not blind. These checks do not establish broad model reliability, actual audience-retention lift, conversion gains, or native-audience validation of Japanese copy. Token totals were unavailable and measured execution intervals used different scopes, so resource-efficiency comparisons are omitted.

The repository's CI performs structural checks: metadata, links, portability, example coverage, and catalog configuration. It does not rerun model evaluations or measure marketing performance.

## Improve the evidence

Submit a reproducible prompt, anonymized input, the observed output, and the behavior you expected. Use comparable account data for real creative experiments; report definitions, denominators, and relevant production context. A useful contribution identifies where the workflow fails and what change addresses the viewer's problem.
