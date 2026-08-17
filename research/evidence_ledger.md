# Evidence and Claim Ledger

This ledger records what the adversarial-RL repository currently demonstrates, what it has falsified or exposed as weak, and what remains outside the evidence. It should evolve with the experiments rather than with the desired thesis conclusion.

## Supported observations

### E1 — The baseline pipeline can distinguish some poisoned policies under held-out seed evaluation

**Status:** supported only in the current 11-state tabular Q-learning environment and frozen configuration.

The initial held-out baseline used 20 clean and 20 poisoned held-out policies after threshold calibration on a separate seed block. It reported balanced accuracy 0.875, poisoned-policy recall 0.750, clean specificity 1.000, and ROC AUC 0.800.

The result is computationally reproducible under the current deterministic implementation: CI regenerates the tracked summary, retains per-seed evidence, and records source/runtime provenance and hashes. This computational reproducibility does not by itself establish statistical replication or generalization beyond the frozen seed populations.

**Permitted wording:** the baseline demonstrates a reproducible controlled poisoning-and-detection pipeline with calibration/test separation in a toy simulated guidance task, and the current implementation can regenerate its tracked evidence exactly.

**Do not claim:** general RL poisoning detection, real autonomous-system robustness, distributional generalization, or that the point estimates are stable across materially different environments, algorithms, attacks, or seed populations.

Primary artifacts:

- [`results/baseline_reward_poisoning.csv`](../results/baseline_reward_poisoning.csv)
- [`results/baseline_reward_poisoning_summary.json`](../results/baseline_reward_poisoning_summary.json)
- [`research/reproducibility_status.md`](reproducibility_status.md)

### E2 — The baseline detector is weak in the subtle-poisoning regime

**Status:** supported negative result on 40 held-out policies per evaluated poisoning strength.

With the detector threshold frozen after calibration at poisoning probability 0.15, held-out recall is only 0.225 at attack probability 0.025, 0.175 at 0.05, and 0.250 at 0.10. ROC AUC versus clean is 0.425, 0.425, and 0.450 at those strengths. Policy success remains 1.000, 1.000, and 0.950 respectively, so the detector is weak specifically in regimes where gross task behavior has not yet collapsed.

Detection becomes much stronger at 0.20 and 0.30, but policy success has already fallen to 0.225 and 0.000. The favorable severe-regime detector performance therefore cannot be used as evidence that subtle or pre-failure poisoning is solved.

**Permitted wording:** the current Q-margin detector primarily becomes reliable once poisoning is comparatively severe; it does not yet solve the scientifically important problem of detecting subtle poisoning before gross policy degradation.

**Do not claim:** that the detector is stealth-robust, that low-strength poisoning is reliably detectable, or that severe-regime performance establishes practical early warning.

Primary artifacts:

- [`results/reward_poisoning_strength_sweep.csv`](../results/reward_poisoning_strength_sweep.csv)
- [`results/reward_poisoning_strength_sweep_summary.json`](../results/reward_poisoning_strength_sweep_summary.json)

## Active research target

### P1 — Pre-failure policy/training signatures can detect subtle poisoning better than the current margin detector

**Status:** unresolved; no stronger detector claim is permitted while the external review/experimental pause remains in effect.

This is the appropriate next scientific target because E2 shows that detecting already-damaged policies is insufficient. Candidate signatures must be judged against simple baselines with frozen calibration, untouched evaluation policies, false-positive reporting, uncertainty, and retained failure cases.

A favorable future result should not be promoted merely because its AUC improves. It must improve discrimination in attack-strength regimes where task behavior remains near the clean regime and must survive negative controls that distinguish poisoning-specific signal from generic learning variation.

## Current evidence quality

The present baseline evidence now has strong **computational reproducibility** for its narrow scope:

- exact configuration is documented;
- calibration and held-out seed ranges are explicit;
- per-seed CSV evidence is retained;
- tracked JSON summaries are regenerated in CI;
- producing Git revision and runtime metadata are retained;
- source/evidence files are linked by SHA-256 provenance hashes.

This should not be confused with **statistical replication**, **mechanism generalization**, or **external validity**. Those remain future experimental questions.

## Evidence required before the thesis claim can expand

The current evidence does not yet establish:

- a prospectively frozen detector that improves subtle-regime detection on untouched policies;
- uncertainty-stable replication of such a detector on new policy populations;
- persistence after poisoning ceases;
- robustness to a second poisoning mechanism;
- robustness to environment or operating-condition shift;
- transfer to a richer autonomous-guidance environment;
- transfer across model classes or RL algorithms;
- cross-domain recurrence in simulated physiological control;
- real-world cyber-physical or clinical relevance.

These are validation stages, not assumptions.

## Claim boundaries

Repository language should not currently state or imply that:

- the work has solved adversarial RL data poisoning;
- the detector is effective against stealthy poisoning in general;
- held-out random seeds constitute broad distributional generalization;
- exact computational reproduction constitutes statistical replication;
- the toy guidance environment represents a deployed autonomous system;
- a later biomedical simulator would constitute clinical validation.

## Promotion rule

A provisional claim becomes evidence-supported only when an experiment designed to falsify it completes with the relevant calibration/test separation and competing explanations addressed. Future promoted results should preserve raw/per-seed evidence, machine-readable summaries, source/runtime provenance, uncertainty, and explicit failure cases. Null, negative, and reversal results remain in this ledger because they define the actual boundary of the thesis contribution.
