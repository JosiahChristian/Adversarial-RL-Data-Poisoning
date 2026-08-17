# Strength-sweep unit-of-analysis and dependence audit — 2026-08-17

## Scope

Review/synthesis artifact only. This note does not modify experiment code, generated scientific results, active workflows, or thesis conclusions.

## Primary evidence

- `experiments/baseline_reward_poisoning.py`
- `experiments/reward_poisoning_strength_sweep.py`
- `results/reward_poisoning_strength_sweep_summary.json`

## Findings

### 1. The policy/seed is the scientific evaluation unit

`evaluate()` runs 200 evaluation episodes, but the evaluation policy is greedy/deterministic, the start state is fixed, and there is no evaluation-time randomness. For a fixed learned Q-table, these 200 episodes repeat the same trajectory.

Therefore the 200 episodes are not 200 independent scientific observations. They are repeated deterministic executions used to summarize one learned policy. The relevant independent/generated unit for the strength sweep is the trained policy indexed by generation/training seed.

This is consistent with the summary's use of 40 held-out seeds per strength, but manuscript or thesis wording must not imply an episode-level sample size of 8,000 independent evaluations per strength.

### 2. `mean_success_rate` is effectively a between-policy proportion in this deterministic setup

Because each fixed greedy policy repeatedly follows the same trajectory from the same start state, an individual policy's evaluation success rate is effectively all-success or all-failure under the present environment/evaluation procedure. The reported mean success rate across 40 seeds therefore primarily describes the fraction of learned policies that reach the goal under deterministic evaluation, not stochastic within-policy reliability over independent episodes.

This does not make the metric invalid. It changes its interpretation.

### 3. Strength conditions are paired by seed and share a common clean comparator

The strength-sweep code trains every poisoning strength on the same held-out seed set `40..79`. The clean condition uses those same seeds. Each per-strength ROC AUC is then computed against the same 40 clean-policy rows.

Thus AUC estimates across strengths are statistically dependent. The design also intentionally uses common random seeds across conditions, which can be useful for controlled comparisons, but any interval for a contrast between strengths should preserve the seed structure.

A naive independent-row bootstrap across each condition would discard this pairing and can misstate uncertainty. A seed-level paired/cluster bootstrap or an explicitly paired permutation/resampling procedure is the natural unit-preserving approach for cross-strength contrasts.

### 4. Point-estimate AUC computation itself is valid as descriptive discrimination

The `roc_auc()` implementation computes the usual pairwise rank probability with half credit for ties using `-mean_trigger_margin` as the poisoning score. Reuse of the clean comparator does not invalidate each descriptive AUC point estimate.

The issue arises when treating the set of AUC values as independent estimates, attaching uncertainty with an incompatible resampling unit, or testing a monotonic trend without accounting for repeated seeds/common controls.

### 5. Calibration and held-out seed separation is implemented

The detector threshold is fitted using seeds `0..19` at the baseline poisoning strength and the sweep evaluates seeds `40..79` without threshold retuning. On the evidence inspected, the threshold-calibration and sweep seed sets are separated.

This supports the narrow claim that the frozen-threshold sensitivity sweep is held out with respect to threshold fitting. It does not constitute distribution-shift generalization because the environment, learning algorithm, trigger states, attack family, and simulator remain fixed.

## Claim impact

The existing detector-specific conclusion survives:

> The current trigger-state Q-margin detector has weak descriptive discrimination in the tested low-strength conditions and improves as poisoning strength increases in this toy simulator.

But reporting should preserve these boundaries:

- `n = 40 trained policies/seeds per strength`, not 8,000 independent evaluation episodes;
- mean deterministic success rate is chiefly a between-policy success proportion under the present evaluation setup;
- AUCs across strengths are correlated because strengths share seeds and the same clean comparator;
- uncertainty or trend tests should resample at the seed/policy level while preserving the repeated-condition structure;
- held-out seeds are not equivalent to held-out environments or attack mechanisms.

## Adjudication

**DESCRIPTIVE STRENGTH-SWEEP RESULT RETAINED; UNIT-OF-ANALYSIS AND CROSS-STRENGTH DEPENDENCE MUST BE EXPLICIT IN INFERENCE.**

No new scientific experiment is needed to resolve this reporting issue. If the retained CI artifact is available, a seed-structured uncertainty analysis can be performed on existing evidence. A new experiment is required only for a new scientific question such as less location-privileged detection, attack-mechanism transfer, persistence, or distribution shift.
