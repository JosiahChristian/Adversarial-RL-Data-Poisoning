# Pre-quadrangulation claim reconciliation — 2026-08-17

## Status

Review/synthesis artifact only. This record does not modify experiment code, generated scientific results, active workflows, or thesis conclusions. Primary experimental artifacts remain authoritative.

## Reconciled claim map

### Claim A — the current trigger-state Q-margin detector reliably detects subtle poisoning

**Status: NOT SUPPORTED.**

The frozen strength sweep shows AUC 0.425 at poisoning strengths 0.025 and 0.05 and AUC 0.45 at 0.10 while task success remains 1.00, 1.00, and 0.95 respectively. The current detector is weak in the low-strength regimes where task behavior remains near clean performance.

### Claim B — the detector becomes strong only after poisoning becomes behaviorally obvious

**Status: SUPPORTED as a detector-specific trend, with careful wording.**

AUC rises to 0.675 at strength 0.15, 0.80 at 0.20, and 1.00 at 0.30 while task success falls to 0.475, 0.225, and 0.00. This supports the interpretation that the present feature becomes useful mainly as policy degradation becomes substantial.

### Claim C — subtle poisoning is generally statistically indistinguishable from chance or broadly undetectable

**Status: NOT ESTABLISHED.**

The available tracked summary does not provide per-strength confidence intervals sufficient to establish statistical equivalence to chance, and only one trigger-state-privileged feature family has been falsified. The evidence supports failure of this detector, not a universal impossibility result.

### Claim D — the detector is a trajectory reward-distribution anomaly detector

**Status: FACTUALLY INCORRECT.**

The implemented feature is a mean Q-value margin measured on the exact trigger states. Final descriptions must preserve that trigger-state-privileged information rather than relabeling the detector as a generic reward-distribution anomaly method.

### Claim E — current evidence establishes general poisoning detection capability

**Status: NOT SUPPORTED.**

Attack-mechanism transfer, location-agnostic detection, persistence after poisoning removal, and broader distributional generalization remain unestablished.

## External-review reconciliation

Gemini Review B correctly identified the central subtle-regime weakness and the danger of interpreting high AUC under severe policy degradation as evidence of subtle pre-failure detection. Its stronger statement that all alpha <= 0.15 regimes are statistically random-like is overbroad because 0.15 is already behaviorally degraded, has AUC 0.675, and lacks a reported uncertainty interval establishing chance equivalence.

The cross-repository conceptual-overfitting allegation remains unestablished from primary evidence. It should remain a chronology/provenance question rather than a scientific defect unless direct evidence shows that outcomes from one program selected hypotheses or endpoints in the other.

## Next evidence gate

The highest-information next step is not to repeat the current Q-margin detector. Before any broad negative thesis claim is made, obtain uncertainty for per-strength AUC from retained or deterministically regenerated seed-level evidence and evaluate at least one less location-privileged detector or simple baseline under prospectively frozen rules.

A defensible thesis contribution may ultimately be a rigorous negative result: specific plausible detectors fail to identify subtle poisoning before policy-level degradation. That claim becomes substantially stronger only after multiple non-equivalent detector families or baselines fail under properly separated calibration and test evidence.

## Decision gate

Do not elevate the present result into either a general poisoning detector claim or a universal subtle-poisoning impossibility claim. Preserve the detector-specific negative result and use the next experiment only if it discriminates between “this privileged feature fails” and “pre-failure poisoning detection is broadly difficult.”
