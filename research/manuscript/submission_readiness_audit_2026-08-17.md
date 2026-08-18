# Adversarial-RL Manuscript Submission-Readiness Audit — 2026-08-17

**Scope:** end-to-end audit of `research/manuscript/manuscript.md` on the review branch after quadrangulation, unit-of-analysis audit, uncertainty/reproducibility audit, and literature positioning. No experiment code, generated result artifact, workflow, or historical thesis record is modified by this audit.

## Verdict

**REVIEW-READY MANUSCRIPT CANDIDATE; NOT YET FINAL-SUBMISSION-READY.**

The narrow detector-specific negative claim is consistent with the tracked aggregate result, current research claim matrix, unit-of-analysis adjudication, and closed-evidence external review. No new scientific experiment is required solely to publish that narrow claim. Final submission packaging would be strengthened by retrieval or provenance-preserving deterministic regeneration of the per-seed CSV so seed-level uncertainty can be reported.

## Gate checks

### 1. Numerical traceability — PASS

All strength-specific policy counts, frozen-threshold recall values, ROC AUC point estimates, and deterministic task-completion proportions in the manuscript match `results/reward_poisoning_strength_sweep_summary.json`.

### 2. Calibration/test separation — PASS FOR THE NARROW CLAIM

The detector threshold was calibrated at strength 0.15 using seeds 0-19 and evaluated on held-out seeds 40-79 without retuning. This supports a held-out frozen-threshold sensitivity sweep. It does not establish distribution-shift generalization because environment, learner, attack family, trigger states, and simulator remain fixed.

### 3. Unit of analysis — PASS

The manuscript identifies the trained policy/seed as the scientific evaluation unit. The 200 deterministic episodes repeat one fixed learned trajectory and are not presented as 200 independent policy observations. Mean success is explicitly interpreted as a between-policy deterministic task-completion proportion.

### 4. Cross-strength dependence — PASS

The manuscript states that strengths reuse the same seed identities and a common clean comparator, so AUC estimates across strengths are correlated. It prohibits independent-across-strength inference that ignores this pairing/common-control structure.

### 5. Uncertainty language — PASS WITH OUTSTANDING EVIDENCE-COMPLETION ITEM

The committed JSON is aggregate-only and cannot support exact empirical AUC intervals. The manuscript therefore treats low-strength AUCs as descriptive point estimates and does not claim statistical equivalence to chance.

The CI workflow is documented as retaining `reward_poisoning_strength_sweep.csv` for 90 days. The producing commit `817ceb0` has been identified, but the available connector cannot enumerate its push-triggered workflow run. Retrieval remains preferred; if the artifact has expired, deterministic regeneration from the frozen producing revision is reproducibility work rather than a new scientific experiment, provided provenance is preserved.

### 6. Claim scope — PASS

The manuscript supports only:

> The tested trigger-state Q-margin detector shows weak descriptive discrimination at strengths 0.025-0.100 in the 11-state tabular-Q-learning environment while deterministic task completion remains near clean behavior.

It does not claim universal subtle-poisoning difficulty, impossibility of detection, field-wide detector failure, deployment security, or cross-domain validity.

### 7. Literature positioning — PASS

Primary literature on adaptive reward poisoning, environment poisoning, attack-specific defense, and backdoor attacks is used only to show that RL poisoning/defense threat models differ materially. It is not used as evidence that the present experiment reproduces those attacks or that this detector result generalizes to them.

### 8. Negative-result visibility — PASS

The detector failure boundary is presented as the contribution rather than hidden as a limitation. High-strength AUC is always presented together with severe policy failure, preventing the manuscript from implying successful early detection where the policy has already degraded substantially.

### 9. Cross-repository non-conflation — PASS

ADT results are explicitly barred from functioning as statistical replication, mechanistic corroboration, or cross-domain validation of the RL result.

## Current publication boundary

The manuscript can be treated as a **review-ready publication/thesis candidate for the detector-specific negative result**. It is not yet a final-submission package because venue formatting and seed-level uncertainty evidence remain incomplete.

## Next actions

1. Continue attempting artifact retrieval while its retention window may still be open, but do not rerun the scientific experiment solely to rescue a claim.
2. If retrieval is impossible and exact reproduction is needed for reporting, regenerate deterministically from the frozen producing revision with provenance captured and label this reproducibility work.
3. Do not launch new scientific studies unless a broader question—non-equivalent detector families, attack transfer, persistence, richer environments, or distribution shift—is intentionally introduced.
