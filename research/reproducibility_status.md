# Reproducibility Status

This document records what the repository can currently reproduce exactly and what additional reproducibility evidence is still required before stronger thesis claims are promoted.

## Current guarantees

The present tabular Q-learning baseline is deterministic for a fixed seed and source revision. The repository currently freezes and documents:

- 11-state guidance environment;
- start and goal states;
- action definitions;
- trigger-state set;
- Q-learning hyperparameters;
- training and evaluation horizons;
- poisoning probability and reward shift;
- calibration, held-out, and attack-sweep seed ranges;
- attack-strength sweep probabilities.

The detector threshold is learned only from the calibration population and is then frozen for held-out evaluation.

## CI evidence guarantees

The research CI now does more than test that scripts execute. It:

1. structurally validates research-critical Python/evidence files;
2. reruns both deterministic baseline programs;
3. verifies exact reproduction of the tracked JSON summaries;
4. retains per-seed baseline and strength-sweep CSV evidence;
5. records the producing Git revision, workflow/run metadata, runtime environment, and SHA-256 hashes of the workflow, experiment programs, and evidence files.

This means the current aggregate baseline claims can be traced back to deterministic source, per-seed evidence, and a specific execution environment.

## What this does not yet guarantee

Exact reproduction of the current toy baseline does **not** establish:

- robustness to dependency/version changes outside the captured runtime;
- reproducibility of future richer-environment experiments;
- statistical generalization beyond the frozen seed populations;
- transfer across attack mechanisms;
- persistence of poisoning-induced effects;
- distribution-shift robustness;
- cross-domain recurrence.

Those require new experimental evidence, not stronger provenance around the existing baseline.

## Reproducibility promotion gates

Before a future result is allowed into the central thesis claim set, it should have, where applicable:

- exact source revision recorded;
- frozen configuration or preregistered analysis plan;
- explicit calibration/train/test population identifiers;
- deterministic seeds or a documented nondeterminism policy;
- raw/per-seed or per-run result retention;
- machine-readable aggregate summary;
- runtime/dependency capture sufficient to reproduce the environment;
- hash/provenance linkage between code and generated evidence;
- a one-command or clearly documented reproduction path;
- CI verification for any result represented as a canonical repository artifact.

## Statistical reproducibility is separate

Bit-for-bit reproduction of a result artifact is necessary but not sufficient for scientific robustness. The thesis must separately test whether conclusions remain stable under new seeds, attack mechanisms, operating conditions, environments, and model choices.

The research package should therefore distinguish:

- **computational reproducibility:** can the same code/configuration regenerate the same evidence?;
- **statistical replication:** does the result recur on new samples/seeds?;
- **mechanism generalization:** does the phenomenon survive meaningful changes in attack or environment?;
- **cross-domain validation:** does a prospectively defined phenomenon recur in an independently specified simulator?

No one level substitutes for another.

## Current conclusion

The baseline and attack-strength sweep have now reached a credible computational-reproducibility standard for their current toy environment. The next scientific priority remains research depth—especially subtle-regime detection, persistence, attack-mechanism variation, and richer guidance validation—not additional polishing of the already reproducible baseline.
