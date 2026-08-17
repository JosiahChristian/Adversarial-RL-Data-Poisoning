# External Review B (Gemini) — frozen-snapshot reconciliation record

## Status

This file preserves the major blind Gemini pre-quadrangulation findings and performs an initial artifact-level adjudication against frozen reviewer snapshot `8596941ada6fa4fb551d22c06ee377f555a2fc49`.

It is a review/reconciliation artifact only. It does **not** modify experiment code, regenerate the tracked scientific record, change the thesis claim, or authorize new experiments. The manuscript/claim gate remains provisional pending the remaining independent audit and final cross-review reconciliation.

## Review-B headline finding

Gemini concluded that the detector does not meaningfully distinguish subtle poisoning from nominal variation and becomes strong only when poisoning already causes obvious task degradation. It also framed the detector as sensing generic trajectory collapse and described a strong defensible claim in terms of trajectory reward-distribution anomaly detection.

## RL-B1 — subtle-regime detector weakness

The frozen strength-sweep summary supports the central negative observation for the genuinely subtle regimes:

- strength 0.025: AUC 0.425, success 1.00
- strength 0.05: AUC 0.425, success 1.00
- strength 0.10: AUC 0.45, success 0.95

At stronger attacks:

- 0.15: AUC 0.675, success 0.475
- 0.20: AUC 0.80, success 0.225
- 0.30: AUC 1.00, success 0.00

**Initial disposition: CONFIRMED in the narrow form** that this detector is weak in low-strength regimes where task success remains near clean behavior and becomes much stronger as behavior degrades.

## RL-B2 — “alpha <= 0.15 is statistically indistinguishable from random”

Review B grouped `alpha <= 0.15` as non-obvious poisoning and described performance there as statistically indistinguishable from random.

That wording exceeds the frozen evidence:

- at 0.15, task success has already fallen to 0.475, so this point is not a near-clean/subtle regime by the experiment's own behavioral metric;
- AUC at 0.15 is 0.675, not a near-0.5 point estimate;
- the tracked summary contains no per-strength confidence interval, so “statistically indistinguishable from random” has not yet been established even at 0.025–0.10.

**Initial disposition: PARTIALLY REJECTED / REPORTING OVERREACH.** The point estimates at 0.025–0.10 support weak/uninformative detection; statistical equivalence to chance requires uncertainty analysis.

## RL-B3 — detector feature mischaracterization

Gemini's displayed strongest-defensible sentence described “statistical anomaly detection on trajectory reward distributions.”

The frozen implementation instead uses a hand-built **mean Q-value margin over the exact trigger states** (`mean_trigger_margin`) and applies a frozen threshold to that feature.

**Initial disposition: FACTUALLY INCORRECT DESCRIPTION.** Any final claim must identify the actual Q-margin detector and its trigger-state-privileged information.

## RL-B4 — generic degradation versus poisoning-specific detection

Review B's broader concern remains legitimate. The detector feature is evaluated at the precise states where corruption is injected, and the strongest detector performance occurs as policy behavior visibly deteriorates. Current evidence does not establish attack-mechanism transfer or a location-agnostic anomaly detector.

**Initial disposition: MAJOR SCOPE LIMITATION CONFIRMED.** The current result supports a narrow detector-specific negative finding, not general poisoning detection capability or a universal impossibility claim.

## RL-B5 — high-degradation detection threshold

Gemini stated that AUC > 0.90 occurs only at strength >= 0.30. The frozen summary has AUC 1.00 at 0.30, while 0.20 is 0.80. This numeric statement is compatible with the artifact, but the more scientifically relevant boundary is that substantial degradation is already present at 0.15 and severe at 0.20.

## RL-B6 — cross-repository conceptual overfitting

Review B inferred shared conceptual overfitting partly from review-index framing. No primary artifact supplied by Review B demonstrates that ADT result knowledge selected the RL detector hypothesis or vice versa.

**Initial disposition: NOT ESTABLISHED.** Retain as a chronology/provenance question rather than a confirmed flaw.

## Review-B severity corrections at this stage

| Review-B finding | Artifact-grounded status now |
|---|---|
| Detector weak under subtle 0.025–0.10 attacks | **Confirmed** |
| All `alpha <= 0.15` statistically random-like | **Overstated**; 0.15 is behaviorally degraded and AUC=0.675; CIs absent |
| Detector is trajectory reward-distribution anomaly detector | **Incorrect**; implementation uses trigger-state mean Q margin |
| Current detector establishes general poisoning detection | **Not supported**; scope must remain detector/mechanism specific |
| Shared ADT/RL conceptual overfitting | **Not established from primary evidence supplied** |

## Claim gate

No thesis conclusion is rewritten here. The current negative result remains preserved: the first trigger-state Q-margin detector is weak where poisoning is subtle by task behavior and becomes useful mainly as task behavior deteriorates.

This record does not authorize a stronger statement that subtle poisoning is generally undetectable, nor a stronger statement that the detector is a robust general poisoning detector.

## Next adjudication gates

1. obtain/derive uncertainty for per-strength AUC from retained or deterministically regenerated seed-level evidence;
2. assess a less location-privileged baseline/detector before elevating the negative result from “this feature fails” to “subtle detection is broadly difficult”;
3. preserve the 0.15 calibration-point caveat in any trend interpretation;
4. keep persistence and attack-mechanism transfer explicitly unestablished until prospectively tested.
