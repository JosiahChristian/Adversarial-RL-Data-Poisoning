# Open Evidence Questions

This file records unresolved scientific questions and evidence gaps. It is not manuscript prose and does not prescribe a publication narrative.

## Detector sensitivity before behavioral collapse

Current aggregate evidence shows weak Q-margin discrimination at poisoning strengths 0.025–0.100 while deterministic task completion remains near the clean condition. Open questions include:

- whether a non-equivalent detector family can discriminate low-strength conditions more effectively;
- whether any improvement remains after calibration is frozen and evaluation is held out;
- whether detector performance can be separated from obvious task-level degradation;
- which false-positive/false-negative tradeoffs persist across independent policy seeds.

## Seed-level uncertainty

Exact uncertainty for strength-specific AUC values is not recoverable from the aggregate JSON alone. Required evidence is the original per-seed detector-score artifact or provenance-preserving deterministic regeneration from the frozen producing revision.

## Persistence

Persistence after poisoning removal has not been established. A future persistence study would need to separate transient response, persistent benign signatures, persistent harmful behavior, and recovery.

## Generalization

Current held-out seeds do not constitute a distribution shift. Generalization remains unresolved across:

- attack mechanisms;
- environment/dynamics changes;
- learning algorithms;
- detector families;
- richer autonomous-guidance simulations.

## Unit of analysis

The trained policy/seed remains the experimental unit for current deterministic evaluations. Future analyses must preserve policy-level dependence and the shared-seed/common-clean-comparator structure where applicable.

## Current boundary

No current evidence establishes universal subtle-poisoning difficulty, real-system security, cross-domain transfer, or clinical relevance.
