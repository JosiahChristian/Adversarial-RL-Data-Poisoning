# Pre-Quadrangulation Reconciliation Matrix

## Purpose

This coordination artifact will reconcile the experiment record, synthesis review, independent ChatGPT audit, and external Claude hostile review after both independent reviews are available. It does not alter experiments, results, thesis claims, or active workflows.

## Freeze rule

Until the external Claude review and independent audit are both returned, use this file only for review provenance and logistics. Do not use it to promote thesis claims, select a new detector from target outcomes, launch remediation experiments, or harden manuscript conclusions.

## Finding matrix

| ID | Reviewer | Experiment / topic | Exact finding | Primary artifact(s) cited | Claim(s) affected | Severity proposed | Existing-analysis remedy? | New experiment needed? | Documentation-only? | Cross-review agreement | Evidence-based disposition | Resolution artifact / commit | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C-RL-01 | C | E2 / subtle-regime detector | Low-strength detector weakness is a genuine negative result in this tested setup; detector becomes strong mainly after policy behavior has already degraded. | baseline code/summary; strength-sweep summary | narrow negative detector claim | reviewer-supported bounded claim | maybe uncertainty refinement | no | no | pending I review | locked pending reconciliation | `research/external_review_a_claude_2026-08-17.md` | recorded |
| C-RL-02 | C | E1/E2 feature construction | `mean_trigger_margin` is measured at the exact poisoning-injection states, so the detector is location/trigger privileged rather than a general anomaly detector. | baseline reward-poisoning implementation | general poisoning-detection framing | major-correctable | yes, scope/code audit | future less-privileged detector may be needed for broader claim | partly | pending I review | locked pending reconciliation | `research/external_review_a_claude_2026-08-17.md` | recorded |
| C-RL-03 | C | E2 uncertainty | Per-strength ROC AUC point estimates lack CIs in the reviewed summary; low-strength values below 0.5 may be sampling variation around chance. | strength-sweep summary | below-chance / anti-correlation wording | major-correctable | yes if per-seed data retained | no | no | pending I review | locked pending reconciliation | `research/external_review_a_claude_2026-08-17.md` | recorded |
| C-RL-04 | C | E2 calibration-point reporting | Strength 0.15 is both the calibration operating point and a reported sweep point; trend rhetoric should flag that partial privilege. | sweep summary | trend interpretation | minor/reporting | no | no | yes | pending I review | locked pending reconciliation | `research/external_review_a_claude_2026-08-17.md` | recorded |
| C-RL-05 | C | persistence / transfer | Persistence after poisoning stops and transfer to another attack mechanism remain unestablished. | review index / evidence documents | broad detector generalization | major only if overclaimed; otherwise open boundary | no | yes for stronger claim | no | pending I review | locked pending reconciliation | `research/external_review_a_claude_2026-08-17.md` | recorded |
| C-RL-06 | C | calibration/test separation | Reviewed baseline code used disjoint calibration/baseline/sweep seed blocks with no obvious leakage; Claude did not independently inspect every sweep-code path. | baseline code; sweep summary | calibration integrity | strength / partially verified | yes, direct sweep-code verification | no | no | pending I review | locked pending reconciliation | `research/external_review_a_claude_2026-08-17.md` | recorded / sweep code verification pending |
| C-RL-07 | C | experiment prioritization | Do not add more attack-strength sweep points before resolving uncertainty on the existing points. | sweep summary | research efficiency / anti-significance-chasing | methodological guidance | yes | no | no | pending I review | locked pending reconciliation | `research/external_review_a_claude_2026-08-17.md` | recorded |

## Allowed dispositions after both reviews arrive

- **ALREADY ADDRESSED**
- **VALID / UNRESOLVED**
- **PARTIALLY VALID**
- **NOT SUPPORTED**
- **ANALYSIS REQUIRED**
- **NEW EXPERIMENT REQUIRED**
- **WORDING / REPORTING CHANGE**

Every disposition must cite primary committed evidence. Agreement among agents is not itself evidence.

## Mandatory thesis reconciliation topics

- clean/calibration/evaluation separation;
- detector-threshold calibration leakage;
- whether subtle-poisoning regimes are defined independently of detector performance;
- whether the detector detects poisoning or generic behavioral degradation;
- feature-selection/search degrees of freedom;
- adequacy of simple baselines;
- seed/policy unit of analysis and uncertainty;
- false-negative behavior in subtle regimes;
- persistence after poisoning ceases;
- attack-mechanism generalization;
- distinction between deterministic computational reproducibility and scientific replication;
- simulator-only scope and avoidance of autonomous-system/biomedical overclaiming.

## Claim-change lock

Thesis-level strong claims and any future manuscript Abstract/Discussion/conclusion language remain provisional until the external review and independent audit are reconciled. Negative detector results and failed subtle-regime performance remain part of the evidence record.
