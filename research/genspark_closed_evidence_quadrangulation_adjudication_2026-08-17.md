# Genspark closed-evidence quadrangulation adjudication — 2026-08-17

## Scope

Review/synthesis artifact only. This note preserves and adjudicates the externally generated Genspark GPT-5.6 Luna closed-evidence review. It does not modify experiment code, generated scientific results, active workflows, or thesis conclusions.

## Protocol validity

A delivery-handshake was completed before the substantive review. The reviewer explicitly acknowledged closed-evidence mode, confirmed visibility of the inline evidence dossier and delivery marker, and did not begin scientific review during the handshake. The substantive response contained no external URLs, citations, literature references, or other obvious web-derived material. The review is therefore admissible as a closed-evidence external quadrangulation component.

## Adversarial-RL claim adjudication

### Detector-specific subtle-regime weakness

External verdict: **SUPPORTED ONLY WITH NARROWER WORDING**.

The reviewer accepted the descriptive result that, in the 11-state tabular-Q-learning environment, the tested trigger-state Q-margin detector showed weak discrimination at poisoning strengths 0.025–0.100. It explicitly required restriction to this detector, simulator, attack-strength range, and descriptive interpretation.

### Broad subtle-poisoning difficulty or impossibility

External verdict: **NOT SUPPORTED**.

The reviewer independently rejected generalization from one detector family and one toy environment to a claim that subtle poisoning is generally difficult or impossible to detect.

### Unit of analysis and dependence

The reviewer independently recognized that the scientifically meaningful unit is the trained policy/seed, not the 200 deterministic evaluation episodes. It also noted that reuse of the same held-out seeds and clean comparator across poisoning strengths induces dependence among across-strength AUC estimates.

### Seed-level uncertainty

The reviewer identified recovery and analysis of the preserved per-seed CI evidence as the highest-information next analysis. This converges with the repository reproducibility audit: exact AUC uncertainty is not reconstructable from the tracked aggregate JSON alone, but the GitHub Actions workflow is configured to preserve the per-seed strength-sweep CSV artifact for 90 days.

## Publication recommendation

External recommendation: **READY AFTER DOCUMENTATION CORRECTION** for appropriately narrowed claims.

The reviewer concluded that no new scientific experiment is required before publication of the detector-specific negative result, provided the thesis/manuscript preserves the narrow scope and does not claim statistical equivalence to chance, broad subtle-poisoning difficulty, universal impossibility, or general detection capability.

## Claim boundary after quadrangulation

1. The present Q-margin detector shows weak descriptive discrimination at low poisoning strengths in the tested toy simulator.
2. The current result is detector-, environment-, attack-, and seed-design-specific.
3. The 200 deterministic evaluation episodes are not independent trained-policy samples.
4. Across-strength AUC estimates are correlated because seeds and the clean comparator are reused.
5. Universal or field-wide claims about subtle-poisoning detectability are not supported.
6. Seed-level uncertainty should be recovered from existing CI evidence if possible before stronger inferential wording is adopted.

## Experiment gate

No new scientific experiment is required solely to publish the appropriately narrowed detector-specific negative result. A new discriminating experiment becomes necessary only if the thesis seeks a broader contribution about pre-failure poisoning detectability across non-equivalent detector families or attack/environment conditions.
