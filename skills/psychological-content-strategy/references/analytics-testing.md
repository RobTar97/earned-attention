# Retention diagnosis and creative experiments

Use this reference to interpret supplied analytics, choose measures, and design practical tests. Keep a distinction between observed behavior and proposed explanations.

## Measure the job of the asset

| Question | Measure to use when available | Limit |
|---|---|---|
| Did the opening earn attention? | Chose to view/stayed to watch; early retention | Definitions and availability differ by platform |
| Did the structure hold interest? | Average watch time and time-based retention | Compare with duration and viewing context |
| Was the length suitable? | Average percentage viewed and completion | Similar purpose and duration give fairer comparisons |
| Was replay useful? | Replay indicators or unusually high watch duration | Value, a natural loop, and confusion can all produce replay |
| Did the audience find utility? | Saves, substantive comments, relevant profile actions | Not every save produces application or business value |
| Was it worth sending? | Shares/sends divided by a defined exposure denominator | Reach and views are different denominators |
| Did it help the business? | Qualified clicks, trials, leads, purchases, assisted outcomes | Requires attribution, quality checks, and suitable windows |
| Did the brand become easier to recall? | Recognition, category associations, recall research | Short-term engagement is not a substitute |

Where a source numerator and denominator are comparable, calculate a rate and label the denominator: share rate per reached account = shares / reach. Do not silently compare shares/views with shares/reach. Missing denominators or metric definitions should be visible in the diagnosis.

## Paid-creative metric dictionary

Before calculating, record platform, organic/paid placement, reporting dates, video duration, view definition, click type, conversion event, attribution window, currency, and the available counts. Impressions, starts, unique viewers, and reached accounts are different quantities. Do not silently swap them.

| Named diagnostic | Calculation when the inputs match | Required label or limitation |
|---|---|---|
| View rate at a stated threshold | qualifying views / impressions × 100 | State the seconds and qualification rule; a “thumb-stop” label alone is insufficient |
| Conditional hold | qualifying later views / qualifying earlier views × 100 | Custom diagnostic; later events must be a subset of earlier events in the same cohort and counting unit; otherwise do not calculate it |
| Completion per start | completed plays / starts × 100 | State that this is per start; a per-impression rate is different |
| Destination CTR | destination clicks / impressions × 100 | All-click CTR includes a different set of actions |
| Conversion rate | conversions / explicitly named denominator × 100 | Distinguish impressions, destination clicks, or landing sessions |
| CPM | spend / impressions × 1,000 | Same currency, period, placement, and delivery context |
| Destination CPC | spend / destination clicks | Do not substitute all clicks |
| Cost per conversion | spend / attributed conversions | Name the event and attribution window; qualify conversion quality |

**Platform check, 2026-10-21:** [TikTok's basic metric definitions](https://ads.tiktok.com/resources/help/article/basic-data?lang=en) distinguish CVR per impression from CVR (clicks) per destination click. Its [video-play definitions](https://ads.tiktok.com/resources/help/article/video-play?lang=en) include 2-second and 6-second views; the 6-second field can also qualify through early engagement or a completed shorter video. It cannot automatically stand for six seconds of continuous watching. Verify the actual exported field before interpretation. These paid definitions do not automatically apply to organic Reels or Shorts.

A 3-second-view/impression rate is usable only when the report supplies that matching numerator and denominator. Do not invent a 3-second count from a 2-second or 6-second field. Return an unavailable rate as unavailable. For a zero denominator, report the rate as undefined rather than zero or infinity.

**Fictional arithmetic example:** 100,000 impressions, 80,000 starts, 12,000 completed plays, 800 destination clicks, 40 attributed conversions, and $900 spend yield 15% completion per start, 0.8% destination CTR, 0.04% conversions per impression, 5% conversions per destination click, $9 CPM, $1.125 destination CPC (about $1.13), and $22.50 per conversion. These are calculations from example inputs, not industry targets. A view-rate field that includes engagement remains qualified even when the arithmetic is straightforward.

## Diagnose the paid funnel

| Pattern, relative to a matched account baseline | Investigate before declaring a cause |
|---|---|
| Weak opening attention | First-frame legibility, relevance, audience/placement fit, and the actual view definition |
| Good initial attention, weak continued viewing | Hook/body continuity, evidence order, progression, and readability |
| Useful viewing, weak destination clicks | Offer relevance, product understanding, CTA, and link destination |
| Destination clicks, weak qualified conversions | Page/message continuity, load or form friction, eligibility, event tracking, and attribution |
| Strong response, deteriorating economics | Auction/audience changes, frequency, creative fatigue, purchase quality, and margin context |

Change one variable family suited to the diagnosis. A strong hook metric does not compensate for an unsuitable offer, and a weak completion rate alone does not justify discarding an ad that brings qualified customers. Use controlled allocation where possible; account for exposure and delivery differences otherwise.

## Interpret curves as hypotheses

| Observation | Plausible explanations | First experiment or evidence needed |
|---|---|---|
| Immediate cliff | Unclear first frame, generic promise, wrong audience | Test opening subject/action and specific relevance |
| Drop after hook | Overpromise, body resets into background, missing proof | Fulfill the promise earlier using the same core body |
| Steady decay | Redundancy, weak progression, information overload | Compress setup or restructure proof; inspect comments |
| Mid-video dip | Confusing explanation, slow action, repeated point, premature CTA | Inspect that timestamp, then replace or clarify the beat |
| Spike | Useful detail, satisfying reveal, loop, or illegible/dense material | Check replay context, comments, readability, and saves |
| Exit before payoff | Predictable answer, ending telegraphed, CTA interrupts value | Deliver answer earlier and postpone or simplify the CTA |
| Strong completion, weak action | Goal mismatch, unclear next step, weak product relevance | Test one objective-linked CTA and qualified outcomes |
| Weak completion, good conversion | Highly qualified subset acts early | Examine business quality before optimizing only retention |

No curve shape proves a cause. State alternate explanations when materially plausible. A screenshot or sparse numbers may not identify the exact failing line; use provided timestamps without inventing precision.

## Cohorts and baselines

Compare assets within the same platform/account and group by duration, topic, audience, organic/paid use, format, distribution conditions, and objective. Use enough recent comparable posts to describe a baseline; state the cohort and its limitations.

No universal “80% completion means viral” rule is justified. A 12-second loop and a 60-second explanation ask different things of viewers. Strong response also does not guarantee reach when audience demand, competition, or distribution differs.

Treat supplied benchmark tables as claims to inspect. Record source, date, population, geography, placement, objective, duration, definition, attribution, and distribution statistic before use. Do not compare TopView with in-feed CTR, cross-platform engagement with different denominators, or averages from unrelated cohorts. The Master Blueprint's 25–30% hook-rate, 20% failure, 40–60% completion, 60-second watch-time, CPM, CTR, and CVR figures are not default thresholds in this skill.

Check metric definitions before comparing periods. YouTube Shorts view-counting and engaged-view definitions illustrate why starts, continuing viewers, and watch-time measures should not be treated as interchangeable. Verify the current definition when reporting exact numbers.

## Prioritize the largest uncertainty

Repair concept and audience relevance first, then hook/body alignment, proof/payoff, pacing/comprehension, and CTA. Cosmetic changes come later unless illegibility or bad audio prevents comprehension.

For a hook test:

1. State the hypothesis: which viewer question will a new angle answer more clearly?
2. Choose one primary measure and a guardrail tied to satisfaction or the business goal.
3. Write 3–5 meaningfully different openings, or follow the requested count.
4. Keep the promise compatible with the same body, proof, offer, and CTA.
5. Keep duration and distribution conditions as similar as practical.
6. Use a controlled split if available. Otherwise document posting order, timing, audience, and exposure differences.
7. Wait for enough comparable exposure to avoid calling tiny differences a winner. Define the review condition from account volume rather than inventing a universal sample size.
8. Retain the principle, then test a different variable family.

Do not claim an organic sequential comparison proves causation. Reposting can change exposure and create fatigue. If the aim is exploration, say so; if the aim is causal attribution, use stronger control and sufficient sample planning.

## Experiment record

| Field | What to record |
|---|---|
| Hypothesis | Expected viewer behavior and why |
| Variable family | Hook, proof order, pacing, duration, cover, CTA, or concept |
| Variants | Exact opening/asset changes |
| Stable elements | Body, audience, offer, CTA, and practical distribution controls |
| Primary measure | One clearly defined rate or outcome |
| Guardrail | Completion, useful responses, qualified leads, or another relevant quality check |
| Review condition | Comparable exposure/time, data availability, and uncertainty |
| Result | Observed values with denominators and context |
| Decision | Keep, reject, or gather more evidence |
| Learning | Transferable principle and next test |

For a small creative request, reduce this to a few sentences. Do not bury the finished script under an analytics plan.

## Platform adaptation

Treat TikTok, Reels, and Shorts as separate surfaces. Keep the creative's core truth stable while adapting first-frame text, title/cover, caption, sound, safe zones, and next-step placement.

- TikTok: a native-feeling demonstration and early relevance are useful creative directions. Verify current recommendation and ad guidance for precise claims.
- Reels: design an asset someone can understand and send to a specific person. Verify current creator guidance, UI, and account analytics rather than asserting fixed ranking weights.
- Shorts: inspect chose-to-view, watch duration, percentage viewed, and satisfaction-related response where available. Avoid treating raw starts as the sole success measure.

Specific platform advice often originates in advertising research. Label paid-ad evidence and validate any application to organic content. Ad recall, organic sharing, and purchase conversion are distinct outcomes.
