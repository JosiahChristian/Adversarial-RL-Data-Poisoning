# Failure Boundaries of a Trigger-State Q-Margin Detector Under Reward Poisoning in a Toy Tabular-RL Guidance Environment

**Draft status:** canonical manuscript source on the review branch only. Claims remain constrained by committed result artifacts, reproducibility audits, unit-of-analysis adjudication, and closed-evidence quadrangulation. This draft does not alter experiment code, generated results, or historical thesis records.

## Abstract

Detecting low-strength training-data corruption before obvious policy failure is an important but method-dependent problem in reinforcement learning. We evaluate a trigger-state Q-value-margin detector in an 11-state simulated guidance task trained with tabular Q-learning. The detector threshold was calibrated at poisoning strength 0.15 and frozen for a held-out sweep over 40 policy seeds per strength. At strengths 0.025, 0.050, and 0.100, frozen-threshold recall was 0.225, 0.175, and 0.25, while ROC AUC versus clean policies was 0.425, 0.425, and 0.45; mean task success remained 1.0, 1.0, and 0.95. Detector discrimination increased at higher strengths as task success deteriorated. These results support a narrow negative conclusion: this particular trigger-state Q-margin detector provides weak descriptive discrimination in the tested low-strength regime of this toy environment. They do not establish statistical equivalence to chance, general difficulty of detecting subtle poisoning, or impossibility of detection. The trained policy/seed, not the 200 deterministic evaluation episodes used to summarize each policy, is the relevant inferential unit.

## 1. Introduction

Adversarial manipulation of reinforcement-learning training signals can alter learned policies while leaving the detectability of that manipulation strongly dependent on the threat model, representation, detector, and environment. A negative result for one detector can therefore be scientifically useful only if its scope is preserved precisely.

This study evaluates a deliberately simple detector with privileged access to the exact trigger states used by the poisoning process. The detector summarizes the learned policy through the mean Q-value margin at those trigger states. Rather than asking whether subtle poisoning is universally detectable or undetectable, the present analysis asks a narrower question: how does this detector behave as poisoning strength varies in a controlled 11-state tabular-Q-learning guidance simulator under a frozen-threshold evaluation?

The manuscript preserves the distinction between descriptive detector performance and general detectability. It also treats the trained policy/seed as the experimental unit, recognizes dependence induced by reusing the same held-out seeds and clean comparator across strengths, and does not infer chance-equivalence from point-estimate AUC values without seed-level uncertainty.

### 1.1 Cross-repository non-conflation rule

The findings in this thesis are interpreted independently of the Adaptive-Digital-Twin-Framework results. Similar vocabulary such as poisoning, pre-failure/pre-decision evaluation, ranking/decision effects, or detector limitations does not constitute evidence of a shared causal mechanism, cross-domain replication, or general law. ADT findings may motivate separate hypotheses but are not corroborating evidence for this result.

## 2. Methods

### 2.1 Environment and learning setup

The experiment uses an 11-state simulated guidance task with tabular Q-learning. The strength-sweep artifact records a clean condition and poisoning strengths 0.025, 0.050, 0.100, 0.150, 0.200, and 0.300.

### 2.2 Detector and calibration

The implemented detector is a mean Q-value margin measured on the exact trigger states. Its threshold was calibrated at poisoning strength 0.15 using calibration seeds 0-19. The resulting threshold, 0.8445131510745894, was then frozen for the strength sweep. No strength-specific retuning was performed in the reported sweep.

### 2.3 Held-out evaluation

The sweep uses held-out seeds 40-79, giving 40 trained policies per condition. For each policy, 200 deterministic evaluation episodes from the same start condition summarize learned behavior. Those episodes are not treated as 200 independent learned-policy samples; the independent experimental unit is the trained policy/seed.

The same held-out seeds are reused across poisoning strengths, and the same clean-policy comparator set is reused in AUC calculations. Therefore AUC estimates across strengths are correlated and should not be treated as independent estimates.

### 2.4 Outcomes

The reported detector outcomes are frozen-threshold recall and ROC AUC versus clean policies. Behavioral outcomes include mean task success rate, mean steps, trigger wrong-way rate, and mean trigger margin. The present manuscript emphasizes detector discrimination jointly with task success so that improved detectability at severe poisoning is not misrepresented as successful early detection.

### 2.5 Uncertainty and reproducibility boundary

The committed result JSON contains aggregate summaries for each 40-policy group. The repository workflow is configured to upload the per-seed strength-sweep CSV as a GitHub Actions artifact with finite retention. That per-seed artifact may permit seed-appropriate uncertainty analysis if recovered. The present connector could identify the commit that launched the sweep (`817ceb0`) but could not enumerate the associated push-triggered workflow run because its commit-run lookup exposes only PR-triggered runs.

Accordingly, the current manuscript treats the reported AUC values as descriptive point estimates and does not claim statistical equivalence to chance. No experiment is rerun or regenerated merely to fill that reporting gap.

## 3. Results

### 3.1 Clean condition

For strength 0.000, the committed summary reports 40 clean policies, zero false positives, clean specificity 1.0, and mean task success 1.0.

### 3.2 Low-strength regime

At strength 0.025, frozen-threshold recall was 0.225 and ROC AUC versus clean was 0.425, while mean task success remained 1.0. At strength 0.050, recall was 0.175 and ROC AUC 0.425, again with mean success 1.0. At strength 0.100, recall was 0.25 and ROC AUC 0.45, while mean success remained 0.95.

These point estimates support the descriptive statement that the tested trigger-state Q-margin detector is weak in the low-strength regime of this toy environment. They do not establish statistical equivalence to random discrimination because seed-level uncertainty is not reported in the committed aggregate summary.

### 3.3 Higher-strength regime

At strength 0.150, recall rose to 0.575 and ROC AUC to 0.675 while mean task success fell to 0.475. At strength 0.200, recall was 0.80 and ROC AUC 0.80 while success fell to 0.225. At strength 0.300, recall and ROC AUC were both 1.0 while mean task success was 0.0.

Thus, detector discrimination increased as corruption became severe enough to coincide with substantial behavioral degradation. These results do not establish useful pre-failure detection at high strength; they show that this detector becomes easier to separate from clean policies as the learned policy itself fails more visibly.

### 3.4 Balanced result summary

| Strength | Policies | Recall | ROC AUC vs clean | Mean task success | Narrow interpretation |
|---:|---:|---:|---:|---:|---|
| 0.025 | 40 | 0.225 | 0.425 | 1.000 | Weak descriptive discrimination while behavior remains clean-like |
| 0.050 | 40 | 0.175 | 0.425 | 1.000 | Weak descriptive discrimination while behavior remains clean-like |
| 0.100 | 40 | 0.250 | 0.450 | 0.950 | Weak descriptive discrimination with minimal behavioral degradation |
| 0.150 | 40 | 0.575 | 0.675 | 0.475 | Moderate discrimination after substantial degradation appears |
| 0.200 | 40 | 0.800 | 0.800 | 0.225 | Stronger discrimination with severe degradation |
| 0.300 | 40 | 1.000 | 1.000 | 0.000 | Perfect separation only when task failure is complete in this sweep |

Table 1 is a direct transcription of committed aggregate results, not a new analysis.

## 4. Negative Result as Contribution

The scientifically defensible negative contribution is detector-specific:

> A trigger-state-privileged Q-margin detector fails to provide strong descriptive pre-failure discrimination at poisoning strengths 0.025-0.100 in the tested 11-state tabular-Q-learning environment under a frozen-threshold evaluation.

This conclusion is informative precisely because the detector is given privileged access to the trigger states. Even so, the result does not imply that non-equivalent detector families, different learned representations, other poisoning mechanisms, or richer environments must fail.

## 5. Discussion

### 5.1 Detector-specific failure boundary

The low-strength sweep identifies a concrete failure boundary for the implemented detector. When policy behavior remained near the clean baseline, recall was low and AUC point estimates were below 0.5. As poisoning strength increased, detector performance improved alongside pronounced policy degradation.

The result therefore argues against presenting this Q-margin feature as a robust early-warning detector in the tested setup. It does not justify a field-wide claim that subtle poisoning is difficult or impossible to detect.

### 5.2 Inferential limits

The sampling structure matters. Forty trained policies are evaluated per strength; the 200 deterministic episodes per policy are summaries of each learned policy, not independent policy replicates. In addition, the repeated held-out seeds and shared clean comparator induce dependence across strength-specific AUC estimates. Any future uncertainty analysis should preserve that structure.

### 5.3 Generalization limits

The result is confined to one small simulator, tabular Q-learning, one trigger-state Q-margin detector, one calibration procedure, the implemented poisoning design, and the documented seed population. It does not establish deployment robustness, cross-domain validity, persistence under distribution shift, transfer across attack mechanisms, or universal subtle-poisoning difficulty.

## 6. Limitations

The largest current reporting limitation is the absence of directly recovered per-seed detector scores in the committed result tree. The aggregate summary is sufficient for descriptive point estimates but not for exact seed-level uncertainty around AUC. The CI workflow was configured to retain the per-seed CSV temporarily, and the run-producing commit is known, but the current connector could not enumerate the push-triggered run needed to retrieve the artifact. This limitation should remain visible until the artifact is recovered or definitively expires.

The environment is deliberately small, the detector family is narrow, and calibration occurs at a single poisoning strength. The same held-out seeds and clean comparator are reused across the sweep. These design choices make the study reproducible as a controlled detector benchmark while sharply limiting general claims.

## 7. Conclusion

In this 11-state tabular-Q-learning guidance simulator, the tested trigger-state Q-margin detector showed weak descriptive discrimination at poisoning strengths 0.025-0.100 while task success remained near clean behavior. Detector separation improved only as behavioral degradation became substantial. This is a reproducible detector-specific negative result, not evidence that subtle poisoning is generally impossible to detect.

No new scientific experiment is required solely to report this narrow finding. Retrieval and seed-appropriate analysis of the existing CI artifact would strengthen uncertainty reporting without changing the experimental design. Broader claims about general detectability, attack transfer, richer environments, or universal pre-failure difficulty require new prospectively specified studies.

## 8. Primary evidence map

- Aggregate strength-sweep results: `results/reward_poisoning_strength_sweep_summary.json`.
- Sweep implementation/run provenance: commits `30bf313`, `817ceb0`, and `a069ec0`.
- Current claim boundaries: `research/research_claim_matrix_2026-08-17.md`.
- Pre-quadrangulation reconciliation: `research/prequadrangulation_claim_reconciliation_2026-08-17.md`.
- Unit-of-analysis and reproducibility audits indexed through `RESEARCH_REVIEW_INDEX.md`.
- Closed-evidence quadrangulation: `research/genspark_closed_evidence_quadrangulation_adjudication_2026-08-17.md`.
- Literature context is maintained separately in `research/literature_context_audit_2026-08-17.md` and must not be used to expand the detector-specific claim.

## Evidence-governance note

This manuscript is subordinate to the committed result artifacts and later audit/adjudication records. A failure of this detector cannot be generalized into a universal impossibility claim without new evidence.