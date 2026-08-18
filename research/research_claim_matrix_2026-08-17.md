# Adversarial-RL evidence-status matrix — 2026-08-17

## Purpose

Machine-assisted review record for tracking the evidentiary status of the controlled simulation studies. Primary experiment code and generated result artifacts remain authoritative.

This file is not manuscript prose and is not a publication draft.

| Evidence area | Current status | Evidence-supported statement | Statement not supported by current evidence | Additional evidence needed for stronger inference |
|---|---|---|---|---|
| Original detector baseline | Supported as toy baseline | The trigger-state Q-margin detector achieved useful held-out discrimination at the original simulated baseline condition. | General detection capability or robustness beyond the tested setup. | Broader held-out conditions and method comparisons. |
| Low-strength detector performance | Supported descriptively, narrowly | In the 11-state tabular-Q-learning environment, the tested detector showed weak descriptive discrimination at strengths 0.025–0.100. | Statistical equivalence to chance without uncertainty or universal difficulty. | Seed-level uncertainty and prospectively compared non-equivalent detector families. |
| High-strength detector performance | Supported as method-specific trend | Detector discrimination increased as perturbation strength rose and policy completion degraded substantially. | Evidence of useful early detection or general defense effectiveness. | Evidence that detection remains useful before gross behavioral failure and across shifts. |
| Broad low-strength detectability | Not established | Failure of this detector does not establish that low-strength training-data corruption is generally difficult or impossible to detect. | Universal undetectability or field-wide impossibility. | Multiple detector families, perturbation mechanisms, environments, and independent evaluations. |
| Detector definition | Fixed by implementation | The implemented detector is a mean Q-value margin measured on the exact trigger states. | Generic trajectory or reward-distribution anomaly detector. | A separately implemented detector if a broader feature family is evaluated. |
| Unit of analysis | Seed/policy level | The trained policy/seed is the experimental unit; 200 deterministic evaluation episodes summarize each policy. | Treating deterministic episodes as independent trained-policy replications. | None; this is a reporting and inference constraint. |
| Across-strength AUC dependence | Correlated design | Across-strength AUC estimates share held-out seeds and the same clean comparator set. | Independent-across-strength inference that ignores shared structure. | Paired or seed-structured uncertainty analysis. |
| Seed-level uncertainty | Not available from aggregate JSON alone | Exact AUC uncertainty requires per-seed detector scores. | Exact chance-equivalence claims from aggregate values alone. | Recover the CI artifact or provenance-preservingly regenerate the existing per-seed evidence. |
| Generalization | Not established | Current evidence is a reproducible toy-scale baseline plus a detector-specific falsification result. | Deployed-system, cross-domain, or clinical validation. | Distribution-shift, richer-simulation, mechanism-transfer, and persistence studies. |

## Current global evidence boundary

The repository supports a reproducible controlled reward-poisoning benchmark and a narrow negative result for one trigger-state Q-margin detector in low-strength regimes. It does not establish broad detection capability, universal difficulty, mechanism transfer, persistence, or real-system security.
