# Manuscript Claim Reconciliation Draft — 2026-08-17

**Status:** proposed manuscript-facing language only. This review branch does not alter experiment code, generated scientific results, active workflows, or historical thesis records on `main`.

## Purpose

Translate the reconciled external review, reproducibility audit, unit-of-analysis audit, and closed-evidence quadrangulation into manuscript-facing claim boundaries.

## Cross-repository non-conflation rule

The findings in this repository must be interpreted independently of the Adaptive-Digital-Twin-Framework results. Similar vocabulary such as poisoning, pre-failure/pre-decision evaluation, ranking/decision effects, or detector limitations does **not** constitute evidence of a shared causal mechanism, cross-domain replication, or general law. ADT findings may motivate separate hypotheses, but they must not be used as corroborating evidence for this thesis unless a separately specified validation study directly tests that relationship.

## Abstract — proposed boundaries

### Permitted core result

> In an 11-state tabular-Q-learning guidance simulator, the tested trigger-state Q-margin detector showed weak descriptive discrimination at low poisoning strengths (0.025–0.10), where policy success remained near clean behavior, and stronger discrimination only as policy degradation became substantial. These results establish a detector- and environment-specific limitation, not a general impossibility result for subtle poisoning detection.

### Do not state

- that subtle poisoning is generally undetectable or statistically indistinguishable from chance;
- that one Q-margin detector establishes a field-wide impossibility result;
- that 200 deterministic evaluation episodes per policy constitute 200 independent policy samples;
- that held-out random seeds establish distribution-shift generalization;
- that high AUC at severe poisoning demonstrates successful pre-failure detection;
- that the current evidence establishes deployment-ready poisoning detection;
- that ADT results independently corroborate this detector result or establish cross-domain replication.

## Results — strength sweep

### Preserve the descriptive result

Report the frozen-threshold sweep exactly by poisoning strength, including low-strength AUC/recall and policy success together. The scientific sampling unit is the trained policy/seed.

### Required dependence statement

The same held-out seeds are reused across poisoning strengths, and the same clean comparator set is reused for AUC calculations. Therefore across-strength AUC values are correlated and should not be interpreted as independent estimates.

### Results wording

> With the threshold calibrated at poisoning strength 0.15 and frozen for evaluation, the Q-margin detector showed weak descriptive discrimination at strengths 0.025–0.10 (ROC AUC 0.425, 0.425, and 0.45; recall 0.225, 0.175, and 0.25), while mean policy success remained 1.0, 1.0, and 0.95. Detector discrimination increased at higher poisoning strengths as policy success deteriorated. Because the same held-out seeds and clean comparator are reused across strengths, these estimates are dependent; formal uncertainty should preserve this pairing structure.

## Unit of analysis

The manuscript must state that each trained policy/seed is the inferential unit. The 200 evaluation episodes are deterministic repeated trajectories from the same start condition for a fixed learned policy and should not be treated as 200 independent learned-policy observations.

## Uncertainty and reproducibility

The committed JSON contains aggregate summaries. The repository workflow is configured to preserve the per-seed strength-sweep CSV in GitHub Actions artifacts for 90 days. If that artifact is recovered, uncertainty analysis should be performed from the retained per-seed evidence without treating the deterministic evaluation episodes as independent replicates.

Until such seed-level uncertainty is reported, describe the AUC values as descriptive point estimates rather than claims of statistical equivalence to chance.

## Discussion — interpretation hierarchy

The Discussion should distinguish:

1. **Detector-specific result:** this Q-margin detector is weak in the tested subtle-strength regime.
2. **Behavioral timing:** stronger detector performance appears mainly once policy degradation is substantial.
3. **General detectability:** not established; one detector family cannot support a universal difficulty or impossibility claim.
4. **Generalization:** not established beyond this simulator, learning setup, trigger-state feature, poisoning design, and seed population.

The detector should be described accurately as a trigger-state Q-value-margin detector, not as a generic trajectory reward-distribution anomaly detector.

Any discussion of ADT should be contextual only. It must not imply mechanistic triangulation, statistical pooling, shared causal structure, or independent replication of this thesis result.

## Negative result as contribution

A defensible negative contribution is:

> A plausible trigger-state-privileged Q-margin detector fails to provide strong pre-failure discrimination in low-strength poisoning regimes of the tested toy environment under a frozen-threshold evaluation.

This wording is useful only if the manuscript preserves the limitations rather than converting detector failure into universal undetectability.

## Conclusion — proposed wording

> The current evidence demonstrates a reproducible limitation of the tested trigger-state Q-margin detector in a small tabular-RL guidance environment: low-strength poisoning is poorly separated from clean policies while task success remains near clean behavior, whereas detector performance improves as policy degradation becomes pronounced. The result should be interpreted as a detector-specific negative finding, not as evidence that subtle poisoning is generally impossible to detect. Broader conclusions require non-equivalent detector families, attack mechanisms, environments, and distribution-shift evaluations.

## Publication-readiness consequence

The closed-evidence adjudication supports **READY AFTER DOCUMENTATION CORRECTION** only for the detector- and environment-specific negative claim. Recovery of the existing per-seed CI artifact and seed-appropriate uncertainty analysis would strengthen reporting without constituting a new scientific experiment. New experiments are required for broader claims about general poisoning detectability, attack-mechanism transfer, persistence, richer guidance environments, cross-repository generalization, or universal pre-failure difficulty.
