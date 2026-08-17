# External Review A — Claude Pre-Quadrangulation Review

## Status

Frozen external review record captured from the 2026-08-17 Claude hostile pre-quadrangulation review. This file records reviewer findings and scope only. It does **not** alter thesis claims, modify experiments, select a new detector, or authorize remediation work.

Claude reported reading the thesis research review index, baseline reward-poisoning implementation, baseline summary, strength-sweep summary, failure-modes/controls document, and evidence ledger. It explicitly reported that it had **not** independently inspected every per-seed CSV, the sweep implementation itself, or all scope/contribution documents. Findings depending on those unread artifacts remain provisional until separately verified.

## Findings recorded for reconciliation

### C-RL-01 — The subtle-regime detector failure is a real negative result within the tested setup

Claude found that the frozen Q-margin detector is weak/uninformative at low poisoning strengths while policy success remains near clean performance, and becomes strong only as policy success collapses at larger attack strengths. It treated that pattern as an honestly reported negative/falsification result for this specific detector rather than an inflated success claim.

### C-RL-02 — The detector is location/trigger privileged

Claude emphasized that `mean_trigger_margin` is calculated at the exact states where poisoning is injected. Therefore the current evidence supports, at most, a mechanism-specific/location-informed detector result and not a general poisoning-anomaly detector claim.

Proposed severity: major-correctable for any broad detection framing.

### C-RL-03 — Per-strength AUC uncertainty is missing

Claude noted that AUC point estimates around 0.425–0.45 at low attack strengths are not accompanied by confidence intervals in the summary it inspected. Without uncertainty, point estimates below 0.5 cannot be distinguished cleanly from sampling variation around chance.

Proposed severity: major-correctable/reporting-inference.

Suggested existing-artifact analysis: bootstrap/exact uncertainty intervals from retained per-seed evidence if available.

### C-RL-04 — Calibration strength 0.15 is also reported as a sweep point

Claude flagged strength 0.15 as partially privileged because it is the operating point used for calibration and is also one of the reported sweep strengths, even though evaluation seeds are disjoint. It recommended annotating this point or excluding it from independent trend rhetoric.

Proposed severity: minor/reporting.

### C-RL-05 — Persistence and attack-mechanism transfer remain unestablished

Claude found no evidence in the reviewed artifacts that the detector signal persists after poisoning ceases or transfers to a meaningfully distinct poisoning mechanism. It treated the repository's explicit acknowledgment of these absences as appropriate.

Proposed severity: major only if broader generalization is claimed; otherwise an open evidence boundary.

### C-RL-06 — Calibration/evaluation separation survived the reviewed code

Claude found disjoint calibration/baseline/sweep seed blocks in what it inspected and no obvious leakage in the baseline path it read. It did not independently inspect every sweep-code path, so complete sweep implementation fidelity remains to be checked.

### C-RL-07 — Additional attack-strength points should not be added before uncertainty is resolved

Claude advised against adding more sweep points merely to accumulate evidence while the current per-strength uncertainty question remains unresolved.

## Claude's strongest bounded thesis claim

Claude permitted a narrow claim: in the tested 11-state tabular Q-learning task, the trigger-state Q-margin detector calibrated at poisoning probability 0.15 is weak/uninformative in low-strength regimes where policy success remains high, and becomes strong mainly after policy performance has already deteriorated substantially. This is a negative result for one hand-built, trigger-state-privileged feature, not evidence that subtle poisoning is generally undetectable.

## Publication/readiness assessment recorded

Claude regarded the negative detector result as potentially suitable for workshop-level review in a bounded form, but not as a faculty-ready thesis body of work because persistence, mechanism transfer, richer environments, and less privileged detectors remain unresolved. This is a reviewer judgment, not an adopted project status.

## Freeze reminder

No thesis claim, manuscript language, experiment, result artifact, or detector implementation is changed by this record. All findings remain unadjudicated until reconciled with the independent audit lane and primary committed evidence.