# Faculty Review Brief — Adversarial RL Data-Poisoning Thesis

## Working question

Under what conditions can controlled data poisoning produce persistent, difficult-to-detect behavioral changes in reinforcement-learning policies for safety-critical simulated dynamical systems, and which pre-failure signatures remain useful under held-out populations and domain shift?

## Current result

The repository has a reproducible tabular Q-learning poisoning baseline with separated calibration and held-out seeds. At poisoning probability 0.15, the first Q-margin detector reached 0.875 balanced accuracy and 0.800 ROC AUC on 20 clean and 20 poisoned held-out policies.

A stronger frozen-threshold falsification then evaluated 40 new seeds per attack strength. In the subtle regime, detector recall was poor (0.225 at 0.025, 0.175 at 0.05, and 0.250 at 0.10), while policy success remained 1.000, 1.000, and 0.950 respectively. Detection became reliable only at stronger poisoning levels where policy behavior was already substantially degraded.

## Why the negative result matters

The baseline demonstrates that a detector can look credible at one attack strength while failing the more scientifically important early-detection question. This gives the thesis a concrete falsification target:

**Can a detector identify poisoning before gross task-level failure makes the anomaly obvious?**

That is currently unresolved.

## Questions for faculty supervision

1. Which pre-failure feature families are theoretically justified rather than selected by metric search?
2. What should count as a practically meaningful subtle-poisoning regime?
3. Which attack mechanisms are sufficiently distinct to test mechanism generalization?
4. How should persistence be defined after poisoning ceases?
5. Which uncertainty/statistical procedure is appropriate for policy-level multi-seed evaluation?
6. At what point is the toy environment exhausted and migration to richer autonomous guidance scientifically justified?
7. Which distribution shifts would constitute meaningful generalization tests?
8. What minimum evidence would make a negative result—failure to detect subtle poisoning—publishable as a careful robustness study?

## Proposed contribution structure

- controlled poisoning benchmark;
- pre-failure detection or rigorous falsification of candidate detectors;
- persistence analysis;
- generalization-boundary analysis;
- richer autonomous-guidance validation if earlier stages survive;
- optional independently specified simulated biomedical validation only much later.

## Important boundaries

The current work does not demonstrate real autonomous-platform security, broad adversarial-RL robustness, clinical relevance, or general cross-domain transfer. Held-out seeds are not equivalent to a genuine distribution shift.

## Reviewer-facing repository map

- `research/thesis_scope.md` — working question and validation ladder
- `research/evidence_ledger.md` — supported and unsupported claims
- `research/failure_modes_and_controls.md` — ways the research can fool itself and corresponding controls
- `research/thesis_contribution_map.md` — minimal, strong, and exceptional contribution levels
- `results/baseline_reward_poisoning_summary.json` — initial held-out baseline
- `results/reward_poisoning_strength_sweep_summary.json` — frozen-threshold falsification

## Decision requested from future faculty supervision

The immediate design question is:

**Which theoretically motivated pre-failure signatures and attack controls would make the next experiment capable of distinguishing genuine subtle-poisoning detection from detection of already-degraded policy behavior?**
