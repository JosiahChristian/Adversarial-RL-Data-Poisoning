# Next Evidence Gate — Pre-Failure Poisoning Detection

## Current evidence position

The repository now has a deterministic, provenance-tracked baseline and attack-strength sweep. The existing detector is credible at the baseline poisoning probability but fails the more important subtle-poisoning question: in low-strength regimes, policy success can remain high while detector recall remains poor.

That negative result should drive the next scientific stage rather than be hidden by additional tuning on the same held-out population.

## Primary unresolved question

**Can a detector identify persistent poisoning-induced policy changes before gross task-level degradation makes the attack behaviorally obvious?**

The next experimental stage should be designed to falsify that proposition.

## Evidence requirements before a stronger detector claim

1. **Feature timing:** every detector input must be available before the behavioral failure endpoint used to define practical harm.
2. **Frozen calibration:** thresholds and feature transformations must be fixed using calibration data only.
3. **Untouched evaluation population:** detector selection and thresholding must not use the final evaluation seeds.
4. **Simple baselines:** any richer detector must beat low-capacity alternatives such as one-feature thresholds and simple linear combinations.
5. **Subtle regime:** evaluation must include poisoning strengths where gross policy success remains near the clean regime.
6. **Uncertainty:** policy-level uncertainty/resampling should accompany aggregate discrimination and recall metrics.
7. **Failure cases:** false negatives in the subtle regime must be retained and characterized.
8. **Persistence:** if poisoning stops, the analysis should distinguish transient anomalies from persistent policy changes.

## Candidate feature families

Feature families should be selected for a mechanistic reason before target outcomes are inspected. Candidates include:

- Q-value margin and margin trajectory;
- state-conditioned action-preference instability;
- visitation-distribution changes around trigger states;
- temporal inconsistency between value estimates and realized returns;
- policy entropy or action-switching changes in states causally downstream of poisoned experience;
- recovery/persistence signatures after poisoning ceases.

This list is a design space, not permission to search all features and report whichever performs best. A small set should be justified and frozen prospectively.

## Required negative controls

A detector should be challenged by clean training stochasticity, non-adversarial reward perturbation, changed random seeds, and at least one perturbation that changes learning dynamics without using the poisoning mechanism. These controls are necessary to distinguish poisoning-specific signatures from generic policy variation.

## Promotion ladder

**Current:** reproducible poisoning benchmark plus a detector that fails important subtle regimes.

**Next promotion:** prospectively specified pre-failure detector that improves subtle-regime detection on untouched policies without relying on gross behavioral collapse.

**Stronger promotion:** persistence plus attack-mechanism generalization.

**Thesis-grade strong contribution:** clear generalization boundaries, including retained failures, with reproducible evidence and uncertainty.

A richer autonomous-guidance environment should be introduced only after the core detector/mechanism survives these controls. Biomedical validation remains an independently specified, carefully bounded simulated validation environment for a much later stage and must not be described as clinical applicability.

## Anti-overfitting rule

If the next frozen detector fails, the failure is evidence. Feature definitions, thresholds, poisoning strengths, and endpoints should not be repeatedly altered on the same target population. Any rescue hypothesis must be labeled exploratory and evaluated prospectively on new untouched policies.
