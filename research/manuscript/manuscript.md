# Failure Boundaries of a Trigger-State Q-Margin Detector Under Reward Poisoning in a Toy Tabular-RL Guidance Environment

**Draft status:** canonical manuscript source on the review branch only. Claims remain constrained by committed result artifacts, reproducibility audits, unit-of-analysis adjudication, and closed-evidence quadrangulation. This draft does not alter experiment code, generated results, or historical thesis records.

## Abstract

Detecting low-strength training-data corruption before obvious policy failure is an important but method-dependent problem in reinforcement learning. We evaluate a trigger-state Q-value-margin detector in an 11-state simulated guidance task trained with tabular Q-learning. The detector threshold was calibrated at poisoning strength 0.15 and frozen for a held-out sweep over 40 policy seeds per strength. At strengths 0.025, 0.050, and 0.100, frozen-threshold recall was 0.225, 0.175, and 0.25, while ROC AUC versus clean policies was 0.425, 0.425, and 0.45; the fraction of trained policies that completed the deterministic task was 1.0, 1.0, and 0.95. Detector discrimination increased at higher strengths as task completion deteriorated. These results support a narrow negative conclusion: this particular trigger-state Q-margin detector provides weak descriptive discrimination in the tested low-strength regime of this toy environment. They do not establish statistical equivalence to chance, general difficulty of detecting subtle poisoning, or impossibility of detection. The trained policy/seed, not the 200 deterministic evaluation episodes used to summarize each policy, is the relevant inferential unit.

## 1. Introduction

Training-time attacks against reinforcement learning span materially different threat models. Prior work has studied adaptive reward poisoning, environment poisoning, attack-specific online defenses, and backdoor-style attacks designed to preserve nominal task performance while inducing targeted behavior [1-4]. This breadth makes detector scope especially important: failure of one feature family under one poisoning mechanism cannot establish a general detectability limit.

This study evaluates a deliberately simple detector with privileged access to the exact trigger states used by the poisoning process. The detector summarizes the learned policy through the mean Q-value margin at those trigger states. Rather than asking whether subtle poisoning is universally detectable or undetectable, the present analysis asks a narrower question: how does this detector behave as poisoning strength varies in a controlled 11-state tabular-Q-learning guidance simulator under a frozen-threshold evaluation?

The manuscript preserves the distinction between descriptive detector performance and general detectability. It also treats the trained policy/seed as the experimental unit, recognizes dependence induced by reusing the same held-out seeds and clean comparator across strengths, and does not infer chance-equivalence from point-estimate AUC values without seed-level uncertainty.

External RL-poisoning literature is used only to establish that attack and defense assumptions vary across the field. It is not evidence that this repository reproduces those published attacks or defenses, and it cannot upgrade the detector-specific result into a universal negative claim.

### 1.1 Cross-repository non-conflation rule

The findings in this thesis are interpreted independently of the Adaptive-Digital-Twin-Framework results. Similar vocabulary such as poisoning, pre-failure/pre-decision evaluation, ranking/decision effects, or detector limitations does not constitute evidence of a shared causal mechanism, cross-domain replication, or general law. ADT findings may motivate separate hypotheses but are not corroborating evidence for this result.

## 2. Methods

### 2.1 Environment and learning setup

The experiment uses an 11-state simulated guidance task with tabular Q-learning. The strength-sweep artifact records a clean condition and poisoning strengths 0.025, 0.050, 0.100, 0.150, 0.200, and 0.300.

### 2.2 Detector and calibration

The implemented detector is a mean Q-value margin measured on the exact trigger states. Its threshold was calibrated at poisoning strength 0.15 using calibration seeds 0-19. The resulting threshold, 0.8445131510745894, was then frozen for the strength sweep. No strength-specific retuning was performed in the reported sweep.

### 2.3 Held-out evaluation

The sweep uses held-out seeds 40-79, giving 40 trained policies per condition. For each policy, 200 deterministic evaluation episodes from the same fixed start condition summarize learned behavior. Because the policy is greedy/deterministic and the evaluation contains no stochasticity, these episodes repeat the same trajectory for a fixed learned Q-table. They are not 200 independent learned-policy samples; the independent experimental unit is the trained policy/seed.

Consequently, the reported mean success rate is primarily the proportion of the 40 learned policies that complete the task under deterministic evaluation, not an estimate of stochastic within-policy reliability across independent episodes.

The same held-out seeds are reused across poisoning strengths, and the same clean-policy comparator set is reused in AUC calculations. Therefore AUC estimates across strengths are correlated and should not be treated as independent estimates.

### 2.4 Outcomes

The reported detector outcomes are frozen-threshold recall and ROC AUC versus clean policies. Behavioral outcomes include deterministic task completion, mean steps, trigger wrong-way rate, and mean trigger margin. The present manuscript emphasizes detector discrimination jointly with task completion so that improved detectability at severe poisoning is not misrepresented as successful early detection.

### 2.5 Uncertainty and reproducibility boundary

The committed result JSON contains aggregate summaries for each 40-policy group. The repository workflow is configured to upload the per-seed strength-sweep CSV as a GitHub Actions artifact with 90-day retention. That per-seed artifact may permit seed-appropriate uncertainty analysis if recovered. The present connector identified the commit that launched the sweep (`817ceb0`) but could not enumerate the associated push-triggered workflow run because its commit-run lookup exposes only PR-triggered runs.

Accordingly, the current manuscript treats the reported AUC values as descriptive point estimates and does not claim statistical equivalence to chance. If the original CI artifact remains available, retrieval is preferred. If it has expired, deterministic regeneration from the frozen producing revision would be reproducibility work rather than a new hypothesis-generating experiment, provided the source revision and provenance are preserved.

## 3. Results

### 3.1 Clean condition

For strength 0.000, the committed summary reports 40 clean policies, zero false positives, clean specificity 1.0, and a policy-level deterministic task-completion proportion of 1.0.

### 3.2 Low-strength regime

At strength 0.025, frozen-threshold recall was 0.225 and ROC AUC versus clean was 0.425, while all 40 trained policies completed the deterministic task. At strength 0.050, recall was 0.175 and ROC AUC 0.425, again with all policies completing the task. At strength 0.100, recall was 0.25 and ROC AUC 0.45, while the task-completion proportion was 0.95.

These point estimates support the descriptive statement that the tested trigger-state Q-margin detector is weak in the low-strength regime of this toy environment. They do not establish statistical equivalence to random discrimination because seed-level uncertainty is not reported in the committed aggregate summary.

### 3.3 Higher-strength regime

At strength 0.150, recall rose to 0.575 and ROC AUC to 0.675 while deterministic task completion fell to 0.475. At strength 0.200, recall was 0.80 and ROC AUC 0.80 while completion fell to 0.225. At strength 0.300, recall and ROC AUC were both 1.0 while no trained policy completed the task.

Thus, detector discrimination increased as corruption became severe enough to coincide with substantial behavioral degradation. These results do not establish useful pre-failure detection at high strength; they show that this detector becomes easier to separate from clean policies as learned-policy failure becomes more visible.

### 3.4 Balanced result summary

| Strength | Policies | Recall | ROC AUC vs clean | Deterministic task-completion proportion | Narrow interpretation |
|---:|---:|---:|---:|---:|---|
| 0.025 | 40 | 0.225 | 0.425 | 1.000 | Weak descriptive discrimination while behavior remains clean-like |
| 0.050 | 40 | 0.175 | 0.425 | 1.000 | Weak descriptive discrimination while behavior remains clean-like |
| 0.100 | 40 | 0.250 | 0.450 | 0.950 | Weak descriptive discrimination with minimal behavioral degradation |
| 0.150 | 40 | 0.575 | 0.675 | 0.475 | Moderate discrimination after substantial degradation appears |
| 0.200 | 40 | 0.800 | 0.800 | 0.225 | Stronger discrimination with severe degradation |
| 0.300 | 40 | 1.000 | 1.000 | 0.000 | Perfect separation only when task failure is complete in this sweep |

Table 1 is a direct transcription/relabeling of committed aggregate results under the audited deterministic evaluation interpretation; it is not a new analysis.

## 4. Negative Result as Contribution

The scientifically defensible negative contribution is detector-specific:

> A trigger-state-privileged Q-margin detector fails to provide strong descriptive pre-failure discrimination at poisoning strengths 0.025-0.100 in the tested 11-state tabular-Q-learning environment under a frozen-threshold evaluation.

This conclusion is informative precisely because the detector is given privileged access to the trigger states. Even so, the result does not imply that non-equivalent detector families, different learned representations, other poisoning mechanisms, or richer environments must fail. Published poisoning and defense work uses different attack structures and defender assumptions [1-4], reinforcing the need to keep this negative result local to the tested detector and threat model.

## 5. Discussion

### 5.1 Detector-specific failure boundary

The low-strength sweep identifies a concrete failure boundary for the implemented detector. When policy behavior remained near the clean baseline, recall was low and AUC point estimates were below 0.5. As poisoning strength increased, detector performance improved alongside pronounced policy degradation.

The result therefore argues against presenting this Q-margin feature as a robust early-warning detector in the tested setup. It does not justify a field-wide claim that subtle poisoning is difficult or impossible to detect.

### 5.2 Inferential limits

The sampling structure matters. Forty trained policies are evaluated per strength; the 200 deterministic episodes per policy are repeated executions of each learned policy, not independent policy replicates. The reported success statistic therefore primarily represents a between-policy completion proportion. In addition, repeated held-out seeds and the shared clean comparator induce dependence across strength-specific AUC estimates. Any future uncertainty or trend analysis should preserve that seed structure.

### 5.3 Generalization limits

The result is confined to one small simulator, tabular Q-learning, one trigger-state Q-margin detector, one calibration procedure, the implemented poisoning design, and the documented seed population. It does not establish deployment robustness, cross-domain validity, persistence under distribution shift, transfer across attack mechanisms, or universal subtle-poisoning difficulty.

Adaptive reward-poisoning, environment-poisoning, attack-specific defense, and backdoor literature demonstrates that materially different adversarial objectives and information structures exist in RL [1-4]. That literature motivates broader future comparisons but is not corroborating evidence for the present detector result.

## 6. Limitations

The largest current reporting limitation is the absence of directly recovered per-seed detector scores in the committed result tree. The aggregate summary is sufficient for descriptive point estimates but not for exact seed-level uncertainty around AUC. The CI workflow was configured to retain the per-seed CSV temporarily, and the run-producing commit is known, but the current connector could not enumerate the push-triggered run needed to retrieve the artifact. This limitation should remain visible until the artifact is recovered, definitively expires, or is deterministically regenerated from the frozen producing revision with provenance preserved.

The environment is deliberately small, the detector family is narrow, and calibration occurs at a single poisoning strength. The same held-out seeds and clean comparator are reused across the sweep. These design choices make the study reproducible as a controlled detector benchmark while sharply limiting general claims.

## 7. Conclusion

In this 11-state tabular-Q-learning guidance simulator, the tested trigger-state Q-margin detector showed weak descriptive discrimination at poisoning strengths 0.025-0.100 while deterministic task completion remained near the clean condition. Detector separation improved only as behavioral degradation became substantial. This is a reproducible detector-specific negative result, not evidence that subtle poisoning is generally impossible to detect.

No new scientific experiment is required solely to report this narrow finding. Retrieval—or, if necessary, provenance-preserving deterministic regeneration—of the existing per-seed evidence would strengthen uncertainty reporting without changing the scientific question. Broader claims about general detectability, attack transfer, richer environments, or universal pre-failure difficulty require new prospectively specified studies.

## 8. Primary evidence map

- Aggregate strength-sweep results: `results/reward_poisoning_strength_sweep_summary.json`.
- Sweep implementation/run provenance: commits `30bf313`, `817ceb0`, and `a069ec0`.
- Unit-of-analysis audit: `research/strength_sweep_unit_of_analysis_audit_2026-08-17.md`.
- Seed-level uncertainty/reproducibility audit: `research/seed_level_uncertainty_reproducibility_audit_2026-08-17.md`.
- Current claim boundaries: `research/research_claim_matrix_2026-08-17.md`.
- Pre-quadrangulation reconciliation: `research/prequadrangulation_claim_reconciliation_2026-08-17.md`.
- Closed-evidence quadrangulation: `research/genspark_closed_evidence_quadrangulation_adjudication_2026-08-17.md`.
- Literature context: `research/literature_context_audit_2026-08-17.md`.

## 9. References

1. Zhang X, Ma Y, Singla A, Zhu X. Adaptive Reward-Poisoning Attacks against Reinforcement Learning. *Proceedings of the 37th International Conference on Machine Learning*. PMLR 119:11225-11234, 2020.
2. Rakhsha A, Radanovic G, Devidze R, Zhu X, Singla A. Policy Teaching via Environment Poisoning: Training-time Adversarial Attacks against Reinforcement Learning. *Proceedings of the 37th International Conference on Machine Learning*. PMLR 119:7974-7984, 2020.
3. Nika A, Singla A, Radanovic G. Online Defense Strategies for Reinforcement Learning Against Adaptive Reward Poisoning. *Proceedings of The 26th International Conference on Artificial Intelligence and Statistics*. PMLR 206:335-358, 2023.
4. Rathbun E, Oprea A, Amato C. Adversarial Inception Backdoor Attacks against Reinforcement Learning. *Proceedings of the 42nd International Conference on Machine Learning*. PMLR 267:51273-51296, 2025.

## Evidence-governance note

This manuscript is subordinate to the committed result artifacts and later audit/adjudication records. External literature supplies threat-model context only. A failure of this detector cannot be generalized into a universal impossibility claim without new evidence.