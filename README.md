# Adversarial-RL-Data-Poisoning

Controlled simulation research on reward poisoning and anomaly detection in reinforcement-learning guidance.

## Repository purpose

This repository is maintained as an experimental evidence record. It contains experiment implementations, generated result summaries, seed and provenance information, unit-of-analysis audits, failure analyses, and reproducibility controls.

No manuscript or publication is represented as complete on `main`. Interpretive papers will be authored separately from this evidence base.

## Current evidence

### Baseline detector condition

The baseline uses an 11-state deterministic guidance task with tabular Q-learning and a trigger-state Q-value-margin detector.

Calibration seeds: `0-19`  
Held-out baseline seeds: `20-39`

At poisoning probability `0.15`, the held-out baseline summary reports:

- 20 clean and 20 poisoned held-out policies
- balanced accuracy: **0.875**
- poisoned-policy recall: **0.750**
- clean specificity: **1.000**
- ROC AUC: **0.800**

[Baseline experiment](experiments/baseline_reward_poisoning.py)  
[Baseline result summary](results/baseline_reward_poisoning_summary.json)

### Frozen-threshold strength sweep

A separate sweep freezes the detector threshold calibrated at poisoning probability `0.15` and evaluates held-out seeds `40-79` without strength-specific retuning.

| Poison probability | Policies | Recall | ROC AUC vs clean | Deterministic task-completion proportion |
|---:|---:|---:|---:|---:|
| 0.025 | 40 | 0.225 | 0.425 | 1.000 |
| 0.050 | 40 | 0.175 | 0.425 | 1.000 |
| 0.100 | 40 | 0.250 | 0.450 | 0.950 |
| 0.150 | 40 | 0.575 | 0.675 | 0.475 |
| 0.200 | 40 | 0.800 | 0.800 | 0.225 |
| 0.300 | 40 | 1.000 | 1.000 | 0.000 |

[Strength-sweep experiment](experiments/reward_poisoning_strength_sweep.py)  
[Strength-sweep result summary](results/reward_poisoning_strength_sweep_summary.json)

The trained policy/seed is the experimental unit. The 200 deterministic evaluation episodes per policy summarize a fixed learned policy and are not 200 independent policy replications. Across-strength AUC estimates are dependent because the same held-out seeds and clean comparator set are reused.

The aggregate evidence supports a narrow detector-specific result: the tested Q-margin detector shows weak descriptive discrimination at poisoning strengths `0.025-0.100` in this toy environment. The aggregate result alone does not establish statistical equivalence to chance and does not support a general claim that subtle poisoning is difficult or impossible to detect.

### Uncertainty boundary

The committed aggregate JSON is sufficient for the descriptive point estimates above. Exact seed-level AUC uncertainty requires per-seed detector scores. The CI workflow was configured to preserve the per-seed CSV as a time-limited artifact; the current tracked aggregate summaries alone are not sufficient to reconstruct exact AUC uncertainty.

### Generalization boundary

Current evidence is limited to:

- one 11-state simulated guidance environment;
- tabular Q-learning;
- one trigger-state Q-margin detector;
- the implemented reward-poisoning mechanism;
- the documented calibration and held-out seed populations.

The repository does not establish deployed-system security, 6-DOF generalization, cross-domain transfer, clinical relevance, or universal poisoning detectability.

## Reproducibility

Current configuration includes:

- state space: 11 states, start `10`, goal `0`
- actions: `-1` toward goal and `+1` away from goal
- trigger states: `{4, 5, 6}`
- learning rate: `0.25`
- discount factor: `0.95`
- epsilon-greedy exploration: `0.15`
- 2000 training episodes per policy
- 40-step maximum horizon
- 200 deterministic evaluation episodes per policy
- poisoning probability baseline: `0.15`
- calibration seeds: `0-19`
- baseline held-out seeds: `20-39`
- strength-sweep held-out seeds: `40-79`

Run the tracked experiments with:

```bash
python experiments/baseline_reward_poisoning.py
python experiments/reward_poisoning_strength_sweep.py
```

GitHub Actions reruns the deterministic experiments, checks tracked summaries, and records provenance information for CI evidence artifacts.

## Evidence organization

```text
experiments/    executable experiment programs
results/        tracked aggregate result summaries
research/       evidence ledgers, audits, inferential-boundary records
.github/        reproducibility and CI workflows
```

## Current status

**Active research evidence base.**

The current repository records a reproducible toy baseline and a detector-specific low-strength failure result. It does not represent a completed paper and does not claim that adversarial reward poisoning in reinforcement learning has been solved.
