# Evidence and Claim Ledger

This ledger records what the adversarial-RL repository currently demonstrates, what it has falsified or exposed as weak, and what remains outside the evidence. It should evolve with the experiments rather than with the desired thesis conclusion.

## Supported observations

### E1 — The baseline pipeline can distinguish some poisoned policies under held-out seed evaluation

**Status:** supported only in the current 11-state tabular Q-learning environment.

The initial held-out baseline reported balanced accuracy 0.875, poisoned-policy recall 0.750, clean specificity 1.000, and ROC AUC 0.800 using a detector threshold learned on a separate calibration split.

**Permitted wording:** the baseline demonstrates a reproducible controlled poisoning-and-detection pipeline with calibration/test separation in a toy simulated guidance task.

**Do not claim:** general RL poisoning detection, real autonomous-system robustness, or detection under meaningful distribution shift.

Primary artifact: [`results/baseline_reward_poisoning_summary.json`](../results/baseline_reward_poisoning_summary.json)

### E2 — The baseline detector is weak in the subtle-poisoning regime

**Status:** supported negative result.

With the detector threshold frozen after calibration at poisoning probability 0.15, held-out recall is only 0.225 at attack probability 0.025, 0.175 at 0.05, and 0.250 at 0.10. Detection becomes strong at 0.20 and 0.30, but those conditions coincide with much larger behavioral degradation.

**Permitted wording:** the current detector primarily becomes reliable once poisoning is comparatively severe; it does not yet solve the scientifically important problem of detecting subtle poisoning before gross policy degradation.

Primary artifacts:

- [`results/reward_poisoning_strength_sweep.csv`](../results/reward_poisoning_strength_sweep.csv)
- [`results/reward_poisoning_strength_sweep_summary.json`](../results/reward_poisoning_strength_sweep_summary.json)

## Active research target

### P1 — Pre-failure policy/training signatures can detect subtle poisoning better than the current margin detector

**Status:** unresolved.

This is the appropriate near-term target because E2 shows that simply detecting already-damaged policies is not sufficient. Candidate signatures should be judged against simple baselines with frozen calibration, held-out seeds, false-positive reporting, and explicit failure cases.

A favorable result should not be promoted merely because its AUC improves. It must show useful discrimination in attack-strength regimes where task behavior has not already collapsed.

## Evidence required before the thesis claim can expand

The current evidence does not yet establish:

- persistence after poisoning ceases
- robustness to a second poisoning mechanism
- robustness to environment or operating-condition shift
- transfer to a richer autonomous-guidance environment
- transfer across model classes or RL algorithms
- cross-domain recurrence in simulated physiological control
- real-world cyber-physical or clinical relevance

These are validation stages, not assumptions.

## Claim boundaries

Repository language should not currently state or imply that:

- the work has solved adversarial RL data poisoning
- the detector is effective against stealthy poisoning in general
- held-out random seeds constitute broad distributional generalization
- the toy guidance environment represents a deployed autonomous system
- a later biomedical simulator would constitute clinical validation

## Promotion rule

A provisional claim becomes evidence-supported only when an experiment designed to falsify it completes with the relevant calibration/test separation and competing explanations addressed. Null, negative, and reversal results remain in this ledger because they define the actual boundary of the thesis contribution.
