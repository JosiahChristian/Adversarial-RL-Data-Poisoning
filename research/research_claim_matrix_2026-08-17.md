# Research claim matrix — 2026-08-17

## Purpose

Review-only claim-control artifact for the controlled simulation studies. Primary experimental artifacts remain authoritative. This matrix does not modify experiment code, generated results, active workflows, or thesis/manuscript conclusions.

| Claim area | Current status | Publication-safe wording | Unsupported wording | Evidence gate for stronger claim |
|---|---|---|---|---|
| Original detector baseline | Supported as toy baseline | The trigger-state Q-margin detector achieved useful held-out discrimination at the original simulated baseline condition. | General detection capability or robustness beyond the tested setup. | Broader held-out conditions and method comparisons. |
| Low-strength detector performance | Supported descriptively, narrowly | In the 11-state tabular-Q-learning environment, the tested trigger-state Q-margin detector showed weak descriptive discrimination at strengths 0.025–0.100. | Statistical equivalence to chance without uncertainty; universal difficulty claim. | Recover seed-level uncertainty and compare non-equivalent detector families prospectively. |
| High-strength detector performance | Supported as method-specific trend | Detector discrimination increased as perturbation strength rose and policy success degraded substantially. | Evidence of early detection or general defense effectiveness. | Show information remains useful before gross behavioral failure and across shifts. |
| Broad low-strength detectability | Not established | Failure of this detector does not establish that low-strength training-data corruption is generally difficult or impossible to detect. | Universal undetectability or field-wide impossibility. | Multiple non-equivalent detectors, perturbation mechanisms, environments, and independently sampled evaluations. |
| Detector description | Must remain exact | The implemented detector is a mean Q-value margin measured on the exact trigger states. | Generic trajectory reward-distribution anomaly detector. | New detector implementation if a broader feature family is claimed. |
| Unit of analysis | Seed/policy level | The independent experimental unit is the trained policy/seed; the 200 deterministic evaluation episodes summarize each policy rather than provide independent policy samples. | Treating 200 evaluation episodes per seed as independent replicates. | None; this is a reporting/statistical requirement. |
| Across-strength AUC dependence | Correlated design | Across-strength AUC estimates are correlated because the same held-out seeds and clean comparator set are reused. | Independent-across-strength inference without preserving this structure. | Paired/seed-structured uncertainty analysis. |
| Seed-level uncertainty | Potentially recoverable from CI | Aggregate JSON alone is insufficient for exact AUC uncertainty, but CI is configured to retain per-seed CSV evidence for 90 days. | Claim that seed-level evidence is permanently unavailable; exact chance-equivalence claims without uncertainty. | Retrieve CI artifact and conduct seed-appropriate analysis. |
| Generalization | Not established | Current evidence is a reproducible toy-scale baseline and falsification result. | Deployed-system, cross-domain, or clinical validation. | Distribution-shift, richer simulation, mechanism-transfer, and persistence testing. |
| Negative thesis contribution | Plausible but incomplete | A rigorous detector-specific negative result can be scientifically valuable if failure boundaries and uncertainty are preserved. | Broad impossibility claim from one failed detector. | Multiple plausible detector families/baselines if the thesis seeks a broader negative result. |

## Global thesis boundary

The current package supports a reproducible controlled-data-integrity benchmark and a narrow negative result for one trigger-state Q-margin detector in low-strength regimes. It does not establish broad detection capability, universal difficulty, mechanism transfer, persistence, or real-system security.

## Publication readiness

External closed-evidence quadrangulation converged on **READY AFTER DOCUMENTATION CORRECTION** for the detector-specific narrowed claims. No new scientific experiment is required solely to publish that narrow negative result. Retrieval and seed-appropriate analysis of existing CI evidence is still recommended before stronger inferential wording; a new experiment is necessary only for broader cross-detector or general detectability claims.
