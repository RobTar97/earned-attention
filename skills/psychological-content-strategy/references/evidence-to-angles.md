# Customer evidence to distinct creative angles

Use this reference for review/comment analysis, buying-trigger research, claim checking, and angle discovery. Accept an existing research brief or positioning document when it provides traceable inputs. A simple copy edit or an approved script brief does not require a new research project.

## Bound the research

Record the offer, intended buyer and buying situation, objective, geography/language, destination, verified capabilities, available proof, and production limits. Define which sources were inspected, why they were selected, the date range, and important missing groups. If no customer material is available, give labeled research hypotheses or a collection plan; do not invent quotes or findings.

Different sources expose different slices: interviews can reveal decision sequences; sales questions reveal evaluation barriers; support tickets reveal usage problems; reviews describe selected experiences; comments reveal reactions without establishing buyer status; search questions show information needs; competitor assets show visible claims and creative choices. Neither a convenience sample's mention count nor a popular competitor post establishes market importance, demand, or profit.

## Preserve what the evidence actually says

Separate an observed statement, observed behavior, verified capability, researcher interpretation, and untested hypothesis. Keep exact wording distinct from translation or paraphrase. Retain source location, date, context, inclusion reason, contradictions, and supplied reuse restrictions. Reading customer material for analysis does not itself authorize publishing identifying details or presenting a synthetic quote as a real customer statement.

Use a record like this when traceability matters; omit irrelevant fields from a small response:

```yaml
evidence_id: E1
classification: observed-statement
source_and_location: null
source_date: null
access_date: null
speaker_or_observation_context: null
exact_wording_or_observation: null
translation_or_paraphrase: null
researcher_interpretation: null
selection_reason: null
reuse_and_storage_limits: null
contradictory_evidence_ids: []
```

Extract a buying trigger, desired outcome, objection, failed alternative, and buyer wording only where supported. “Setup took longer than expected” can document one person's experience; it does not establish that setup anxiety is the market's main barrier.

## Match each promise to appropriate proof

| Claim type | Evidence to look for | Scope to preserve |
|---|---|---|
| Capability | Verified operation under stated conditions | Show what the product demonstrably does |
| Performance | Relevant measurement and method | Preserve task, conditions, version, and outcome |
| Customer outcome | Traceable case with appropriate reuse basis | Attribute that experience; avoid universalizing it |
| Comparison | Compatible alternatives, tasks, versions, and conditions | Explain the actual comparison |
| Economic result | Relevant business data and explicit assumptions | Do not infer profit from a screen demonstration or public engagement |

Maintain a compact claim register: `claim_id; proposed wording; evidence_ids; proof_asset_ids; conditions; limitations; reuse limits; status`. Use statuses such as supported-with-scope, needs-verification, or rejected. This is an internal evidence decision, not an extra user approval step.

When a promise exceeds its proof, narrow it, identify evidence to obtain, turn the asset into an honest investigation, or remove the claim. A testimonial records a person's account; it does not guarantee the same outcome for others. Decorative B-roll or a generated reconstruction cannot verify actual product behavior.

## Generate different reasons to care

An angle changes a buying reason, decision criterion, objection, constraint, or proof path. Hook wording is the expression of that angle. Explore actual triggers, workaround costs, trade-offs, objections, useful mechanisms, unsuitable uses, and handoff needs; keep unsupported possibilities labeled as hypotheses.

For a fictional tool whose verified features are mapping CSV headers and exporting a separate file:

- A recurring-file angle can show the mapping operation for a repeated import task.
- An output-verification angle can show whether the exported header matches the destination's expected field.
- A source-preservation angle needs verification that the original is unchanged before that promise is used.

“Work smarter,” “stop wasting time,” and “save hours” supply neither three distinct reasons nor evidence of time savings.

```yaml
angle_id: A1
brief_id: null
status: hypothesis
viewer_situation_and_trigger: null
desired_outcome_or_decision: null
insight_and_classification: null
evidence_ids: []
supported_promise: null
claim_ids: []
proof_asset_ids: []
objection_or_failed_alternative: null
awareness_assessment_and_basis: null
creative_direction_and_proof_order: null
voice_and_production_constraints: []
next_action_and_destination: null
distinctness_reason: null
uncertainty_and_contradictions: []
```

Select for production only angles with a relevant situation, a supportable promise, obtainable proof, feasible production, and a coherent next step. Keep unverified research candidates in the bank with a hypothesis or needs-verification status and explicit evidence gaps. Compare relevance, credibility, distinctness, evidence, and effort using reasons; do not invent conversion probabilities or a predictive “winning angle” score. When options are similarly plausible, consider the cheaper useful test.

## Handoff and storage

Return the requested number of angles, their source/proof basis, a recommendation with reasons, and the material unknowns. An expanded research brief can add corpus boundaries, observed findings, hypotheses, verified capabilities, claim register, available assets, and remaining decisions. Pass the chosen angle to [hooks and copy](hooks-copy.md) and [video production](video-production.md).

Publish empty templates and fictional examples in the skill package. Keep real customer material, account data, and reusable research records in the user's requested project location, outside the public repository and global skill installation. Produce a proposed record in the response when no persistent storage was requested. See [sources and evidence](sources-evidence.md) for the supporting methodology and transfer limits.
