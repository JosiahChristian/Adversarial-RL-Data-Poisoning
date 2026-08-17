# External Research Review Index

This file is the **front door for independent review** of the Adversarial-RL-Data-Poisoning-Thesis evidence. Reviewers should inspect experiment code and tracked result artifacts before relying on README or interpretation documents.

## Current reconciliation — read before broadening detector claims

- [`research/prequadrangulation_claim_reconciliation_2026-08-17.md`](research/prequadrangulation_claim_reconciliation_2026-08-17.md) — freezes the current detector-specific claim boundary after external-review adjudication.
- [`research/seed_level_uncertainty_reproducibility_audit_2026-08-17.md`](research/seed_level_uncertainty_reproducibility_audit_2026-08-17.md) — distinguishes aggregate tracked results from the per-seed CSV evidence intentionally retained by CI.

The current evidence supports a detector-specific subtle-regime failure in the toy environment. It does not establish universal subtle-poisoning undetectability or general poisoning detection capability.

## Start here — executed baseline and falsification

### Baseline implementation
- Repository: [`experiments/baseline_reward_poisoning.py`](experiments/baseline_reward_poisoning.py)
- Raw: https://raw.githubusercontent.com/JosiahChristian/Adversarial-RL-Data-Poisoning-Thesis/main/experiments/baseline_reward_poisoning.py

### Baseline tracked summary
- Repository: [`results/baseline_reward_poisoning_summary.json`](results/baseline_reward_poisoning_summary.json)
- Raw: https://raw.githubusercontent.com/JosiahChristian/Adversarial-RL-Data-Poisoning-Thesis/main/results/baseline_reward_poisoning_summary.json

### Frozen-threshold attack-strength sweep implementation
- Repository: [`experiments/reward_poisoning_strength_sweep.py`](experiments/reward_poisoning_strength_sweep.py)
- Raw: https://raw.githubusercontent.com/JosiahChristian/Adversarial-RL-Data-Poisoning-Thesis/main/experiments/reward_poisoning_strength_sweep.py

### Strength-sweep tracked summary
- Repository: [`results/reward_poisoning_strength_sweep_summary.json`](results/reward_poisoning_strength_sweep_summary.json)
- Raw: https://raw.githubusercontent.com/JosiahChristian/Adversarial-RL-Data-Poisoning-Thesis/main/results/reward_poisoning_strength_sweep_summary.json

The current key falsification is that the first Q-margin detector is weak in low-strength poisoning regimes where policy-level success remains near clean behavior, while detector performance becomes strong mainly once poisoning is severe enough to cause obvious behavioral degradation. Treat the reported AUC values as descriptive point estimates unless a seed-level uncertainty analysis is supplied.

## Claim and failure-mode documentation

### Evidence/claim ledger
- [`research/evidence_ledger.md`](research/evidence_ledger.md)
- Raw: https://raw.githubusercontent.com/JosiahChristian/Adversarial-RL-Data-Poisoning-Thesis/main/research/evidence_ledger.md

### Failure modes and experimental controls
- [`research/failure_modes_and_controls.md`](research/failure_modes_and_controls.md)
- Raw: https://raw.githubusercontent.com/JosiahChristian/Adversarial-RL-Data-Poisoning-Thesis/main/research/failure_modes_and_controls.md

### Thesis scope and validation ladder
- [`research/thesis_scope.md`](research/thesis_scope.md)
- Raw: https://raw.githubusercontent.com/JosiahChristian/Adversarial-RL-Data-Poisoning-Thesis/main/research/thesis_scope.md

### Thesis contribution map
- [`research/thesis_contribution_map.md`](research/thesis_contribution_map.md)
- Raw: https://raw.githubusercontent.com/JosiahChristian/Adversarial-RL-Data-Poisoning-Thesis/main/research/thesis_contribution_map.md

### Next evidence gate — pre-failure detection
- [`research/next_evidence_gate.md`](research/next_evidence_gate.md)
- Raw: https://raw.githubusercontent.com/JosiahChristian/Adversarial-RL-Data-Poisoning-Thesis/main/research/next_evidence_gate.md

## Reproducibility and provenance

### Reproducibility status
- [`research/reproducibility_status.md`](research/reproducibility_status.md)
- Raw: https://raw.githubusercontent.com/JosiahChristian/Adversarial-RL-Data-Poisoning-Thesis/main/research/reproducibility_status.md

The root README documents the executed 11-state Q-learning configuration, seed partitions, poisoning strength/reward shift, frozen-threshold logic, and current CI guarantees. CI regenerates experiment evidence, verifies exact tracked JSON reproduction, retains per-seed CSV evidence as workflow artifacts for 90 days, and records provenance/environment hashes.

- README raw: https://raw.githubusercontent.com/JosiahChristian/Adversarial-RL-Data-Poisoning-Thesis/main/README.md

A reviewer must distinguish deterministic computational reproducibility from independent scientific replication or distribution-shift generalization. Exact AUC uncertainty is not recoverable from the tracked aggregate JSON alone, but the configured CI artifact may preserve the required per-seed evidence without a new scientific experiment.

## Faculty/reviewer framing

### Faculty review brief
- [`research/faculty_review_brief.md`](research/faculty_review_brief.md)
- Raw: https://raw.githubusercontent.com/JosiahChristian/Adversarial-RL-Data-Poisoning-Thesis/main/research/faculty_review_brief.md

### Pre-quadrangulation hostile-review packet
- [`research/quadrangulation_review_packet.md`](research/quadrangulation_review_packet.md)
- Raw: https://raw.githubusercontent.com/JosiahChristian/Adversarial-RL-Data-Poisoning-Thesis/main/research/quadrangulation_review_packet.md

## Questions an independent reviewer should answer

1. Does the detector identify poisoning or merely gross policy degradation?
2. Is calibration/test separation implemented correctly?
3. Are held-out random seeds being over-described as distributional generalization?
4. Are the subtle attack-strength regimes independently meaningful?
5. What simple baselines and negative controls are still missing?
6. Is policy-level uncertainty handled appropriately?
7. Is persistence after poisoning removal established? (currently no.)
8. Is attack-mechanism transfer established? (currently no.)
9. Is migration to richer autonomous guidance justified before solving or rigorously falsifying subtle pre-failure detection?
10. Could a rigorous negative result—failure of candidate detectors in subtle regimes—constitute the strongest defensible thesis contribution?

## Scope boundary

This repository currently provides a toy-scale, reproducible simulated poisoning/detection baseline and a negative subtle-regime falsification result for the present Q-margin-style detector. It does not establish real autonomous-platform security, broad adversarial-RL robustness, universal subtle-poisoning undetectability, cross-domain transfer, or clinical relevance. Biomedical control is reserved only as a much-later independently specified simulated validation environment.
