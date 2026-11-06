# Commercial diagnosis and reusable creative lessons

Use this reference for poor lead quality, economics questions, experiment planning, and lessons from earlier creative. Use [analytics and testing](analytics-testing.md) for the maintained metric dictionary; do not create competing definitions here. Accept a rigorous experiment design from an available specialist while retaining a basic local workflow.

## Define the decision before judging the asset

Distinguish organic reach, brand understanding/memory, lead qualification, and paid acquisition. Name the actual decision, objective, offer, intended buyer, destination, primary measure, quality/business guardrails, and review conditions. Define lead eligibility and intent before treating form volume as qualified demand.

For each measure, preserve numerator, denominator, counting rule, source, time window, attribution settings, deduplication, and cohort maturity. Separate intended audience from observed audience. Views do not establish comprehension; clicks do not establish fit; qualified inquiries do not establish sales; an attributed purchase does not establish incremental demand or profit.

## Investigate the relevant stage

| Observation | Plausible checks before rewriting |
|---|---|
| Weak opening response | Audience fit, first-frame clarity, delivery, and actual view definition |
| Strong viewing, weak destination activity | Objective, offer fit, link availability, and CTA relevance |
| Clicks, weak form completion | Promise continuity, page usability/language, conditions, and tracking |
| Many inquiries, poor qualification | Overbroad promise, buyer eligibility, incentive, form criteria, and qualification consistency |
| Qualified leads, few sales | Follow-up, sales process, offer, price, and sales-cycle maturity |
| Declining performance | Exposure/frequency, audience and placement mix, auction conditions, offer or tracking changes, and possible fatigue |

A decline alone does not establish creative fatigue. Check whether CTA, destination, form, and follow-up continue the same promise. If measurement or qualification is broken, repair the specification before declaring a creative winner. Choose a testable uncertainty rather than claiming one aggregate pattern proves a cause.

## Calculate contribution limits only from explicit inputs

These are planning identities, not empirical performance forecasts. Use one consistent currency, cohort, horizon, and per-sale or per-customer unit.

- `R`: retained sale receipts after discounts, refunds, and taxes remitted.
- `V`: variable fulfillment, payment, support, and return-processing costs not already deducted from `R`.
- `C = R - V`: contribution before acquisition.
- `N`: non-media acquisition cost allocated to that same sale/customer unit.
- `T`: required contribution remaining after acquisition.

The media acquisition cost must be **no more than `C - N - T`** to meet that specified contribution requirement. A negative ceiling means no nonnegative media cost meets it under those assumptions. Keep marginal media decisions separate from fully loaded channel profitability and state which costs are included.

For qualified leads, let `p` be an observed qualified-lead-to-sale probability from a relevant mature cohort and `S` the non-media acquisition and sales cost allocated per qualified lead. The corresponding media cost per qualified lead must be **no more than `p * (C - T) - S`**. Here `S` is the lead-level allocation of non-media costs; do not also subtract the same costs as `N`. State other excluded costs. Unknown `p` or contribution means the ceiling is unknown; speculative lifetime value is not a substitute.

Fictional arithmetic: `R = 120`, `V = 50`, `N = 15`, and `T = 20` imply `C = 70` and a media ceiling of `35` per sale. An alternative lead-level allocation with `p = 0.20` and `S = 3` gives `7` per qualified lead. These inputs are stipulated, not estimates of a real business. Zero qualified outcomes make observed cost per qualified outcome undefined; never report it as zero.

## Test within the available evidence

Specify hypothesis, variable family, stable elements, allocation method, primary measure, guardrails, exposure/spend feasibility, and a review condition. Fit these to supplied limits; label illustrative assumptions rather than inventing an approved budget. Account for delayed conversions and sales follow-up. Sparse evidence may justify comprehension or qualification review before a larger outcome comparison.

Keep three classifications separate:

- **Attributed outcome:** credited under a stated measurement system and window.
- **Incremental effect:** estimated causal difference under a suitable design and stated uncertainty.
- **Directional association:** an uncontrolled comparison useful for another investigation.

An ordinary sequence of organic posts is uncontrolled. A randomized comparison between creative A and creative B can compare those treatments; it does not automatically estimate advertising versus no advertising. If evidence cannot distinguish decision-relevant outcomes, keep the conclusion directional or inconclusive.

## Preserve bounded lessons

Use this record when a reusable account lesson is requested; shorten it for a small diagnosis:

```yaml
learning_id: L1
account_and_asset_variant_ids: null
parent_concept_and_angle_ids: null
intended_and_observed_audience: null
offer_destination_objective: null
hook_promise_proof_structure_voice: null
duration_and_basis: null
production_cost_and_included_scope: null
platform_placement_mode_dates_timezone: null
spend_allocation_and_delivery_changes: null
primary_measure_name_counts_rule_source: null
quality_and_business_guardrails: []
attribution_window_deduplication_cohort_maturity: null
observed_and_attributed_outcomes: null
incremental_effect_and_design_if_established: null
result_classification: inconclusive
uncertainty_and_contradictions: []
decision_and_bounded_lesson: null
applicable_context: null
supersedes_or_contradicts_learning_ids: []
next_action_and_review_date: null
```

Retrieve previous lessons only when their account, offer, audience, objective, language, proof, and distribution context are relevant. Check date, counting rules, attribution, maturity, and uncertainty. Keep contradictory and superseded findings discoverable. For acquisition, poor qualified outcomes can disqualify a variant despite a stronger opening-view rate; prefer outcomes meeting the stated quality and economics criteria. Different objectives may justify different decisions.

Write “in this audience/offer/test context, this opening had the observed qualified response, with these limits,” rather than “this hook always converts.” Apply it to a new brief as a hypothesis when context changes. Do not invent a previous experiment or claim access to unavailable records. Keep real learning records in the user's requested project storage, outside the public skill package. Source evidence and transfer limits are maintained in [sources and evidence](sources-evidence.md).
