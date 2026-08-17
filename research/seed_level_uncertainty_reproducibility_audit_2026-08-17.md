# Seed-level uncertainty and reproducibility audit — 2026-08-17

## Scope

Review/synthesis artifact only. This note does not modify experiment code, generated scientific results, active workflows, or thesis conclusions.

## Question

Are the seed-level observations required for uncertainty analysis of the poisoning-strength ROC AUC values actually unavailable, or are they preserved outside the tracked aggregate summaries?

## Primary evidence

- `results/reward_poisoning_strength_sweep_summary.json`
- `.github/workflows/research-baseline.yml`
- `README.md`
- `research/prequadrangulation_claim_reconciliation_2026-08-17.md`

## Findings

### 1. The tracked result on `main` is aggregate-only

The committed strength-sweep summary reports 40 observations per poisoning strength and point estimates for recall, ROC AUC, and policy behavior, but it does not contain the individual detector scores required to reconstruct an exact empirical AUC confidence interval from that file alone.

The earlier claim reconciliation is therefore correct in the narrow sense that uncertainty cannot be reconstructed honestly from the tracked aggregate JSON by itself.

### 2. The CI workflow intentionally preserves the per-seed CSV

The `research-baseline.yml` workflow deterministically reruns the strength sweep and uploads:

- `results/baseline_reward_poisoning.csv`
- `results/baseline_reward_poisoning_summary.json`
- `results/reward_poisoning_strength_sweep.csv`
- `results/reward_poisoning_strength_sweep_summary.json`
- `results/evidence_provenance.txt`

under the artifact name `adversarial-rl-baseline-evidence` with a 90-day retention period.

Thus the repository's reproducibility design does preserve the seed-level strength-sweep evidence in CI artifacts even though the CSV is not tracked on `main`.

### 3. Claim-boundary implication

It is too strong to say that the seed-level evidence is simply absent from the research package. The accurate distinction is:

> Exact AUC uncertainty cannot be reconstructed from the committed aggregate summary alone. The deterministic CI workflow is configured to retain the per-seed CSV as a time-limited evidence artifact, so uncertainty analysis may be possible without a new scientific experiment if the relevant artifact is retrieved while retained.

If the artifact has expired, deterministic regeneration from the frozen source revision would be reproducibility work rather than a new hypothesis-generating experiment, but any such regeneration should preserve the producing commit and provenance.

### 4. Current statistical claim remains bounded

Until a seed-level interval or other prospectively justified uncertainty analysis is actually computed, the low-strength AUC values should remain descriptive point estimates. Wording such as `AUC = 0.425/0.450` and `poor discrimination for this detector in the tested low-strength conditions` is supported descriptively. Statistical equivalence to chance, a confidence-bound claim around 0.5, or universal subtle-poisoning undetectability is not established.

## Adjudication

**SEED-LEVEL EVIDENCE IS NOT COMMITTED IN THE CLAIM-FACING SUMMARY, BUT IS INTENTIONALLY PRESERVED BY CI FOR 90 DAYS.**

This resolves a reproducibility ambiguity but does not itself strengthen the detector claim. Retrieval and analysis of the existing CI artifact would be an uncertainty/reporting audit, not a new detector experiment.

## Next evidence gate

Prefer retrieval of an existing matching CI artifact over rerunning the experiment. If retrieved, verify its provenance manifest against the frozen source revision before calculating uncertainty. Do not use an uncertainty estimate to promote a universal impossibility claim; it can only sharpen the detector-specific result in this toy environment.
