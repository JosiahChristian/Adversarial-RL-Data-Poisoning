# Adversarial-RL Publication Packaging Plan — 2026-08-17

**Status:** review-branch publication-engineering record. This plan does not alter experiment code, generated scientific results, active workflows, or historical thesis records.

## Governing rule

Manuscript displays must be generated from committed result artifacts or provenance-verified retained CI evidence. The independent scientific unit is the trained policy/seed. Deterministic evaluation episodes must not be plotted or counted as independent replicates.

## Current reproducible source

`research/manuscript/plot_strength_sweep.py` reads only `results/reward_poisoning_strength_sweep_summary.json` and generates descriptive manuscript outputs. It does not train policies, rerun the strength sweep, change thresholds, or recompute scientific outcomes.

The current script intentionally produces separate figures rather than visually combining detector performance and behavioral degradation in a way that could imply a causal relationship.

## Recommended displays

### Table 1 — Strength-sweep summary

Source: committed aggregate strength-sweep JSON.

Columns:

- poisoning strength;
- trained policies (`n = 40` per strength);
- frozen-threshold recall;
- ROC AUC vs the common clean comparator;
- deterministic task-completion proportion.

Required note:

> The 200 deterministic evaluation episodes for each trained policy are repeated executions from the same start state and are not independent inferential units. Across-strength AUC values are correlated because strengths reuse held-out seeds and the same clean comparator set.

### Figure 1 — ROC AUC vs poisoning strength

Source: committed aggregate JSON.

Caption must state that values are **descriptive point estimates** pending seed-level uncertainty. A horizontal 0.5 reference line may be added for visual orientation only if the caption explicitly says the manuscript does not claim statistical equivalence to chance or significant deviation from chance without seed-level uncertainty.

### Figure 2 — Frozen-threshold recall vs poisoning strength

Source: committed aggregate JSON.

Caption should identify the single threshold as calibrated at strength 0.15 on seeds 0-19 and frozen for evaluation seeds 40-79.

### Figure 3 — Deterministic task completion vs poisoning strength

Source: committed aggregate JSON field `mean_success_rate`, relabeled under the unit-of-analysis audit as the fraction of trained policies completing the deterministic task.

Caption must not describe this as stochastic within-policy reliability.

## Optional final display after seed-level evidence recovery

If the retained CI artifact is recovered—or if deterministic regeneration from the frozen producing revision is necessary after artifact expiry—add seed-structured uncertainty around detector metrics using trained policy/seed as the resampling unit and preserving repeated-seed/common-control dependence.

Do not use regenerated or recovered uncertainty to promote a universal detectability or impossibility claim. It may only sharpen the detector-specific inference in the tested toy environment.

## Reproducibility requirements

Before final submission:

- [ ] Run `plot_strength_sweep.py` in a clean environment and archive the producing commit.
- [ ] Verify generated table values against `results/reward_poisoning_strength_sweep_summary.json` byte-for-value after formatting/rounding rules.
- [ ] Record Python and matplotlib versions used for final rendering.
- [ ] Prefer retrieval of the original retained per-seed CI artifact over regeneration while it remains available.
- [ ] If regeneration is required, freeze the producing source commit and preserve provenance separately from the original experimental record.
- [ ] After uncertainty is added, re-audit all captions for policy/seed-level inference and cross-strength dependence.
- [ ] Re-run the whole-manuscript hostile review after final figure insertion.

## Visual claim restrictions

Prohibited:

- calling AUC 0.425/0.450 statistically equivalent to random without an appropriate uncertainty/equivalence procedure;
- treating 8,000 deterministic episodes per strength as the sample size;
- describing improved high-strength detection as useful early detection when task completion has already collapsed;
- extrapolating one detector family into a general subtle-poisoning impossibility result.

## Current packaging verdict

The manuscript is review-ready and has a reproducible aggregate-figure source. Final-submission readiness would be strengthened by seed-level uncertainty recovery/regeneration and final venue-specific formatting, but no new scientific experiment is required for the narrow detector-specific result.