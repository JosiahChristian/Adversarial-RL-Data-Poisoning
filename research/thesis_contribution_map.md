# Thesis Contribution Map

This document translates the working research question into a bounded contribution structure. It does not prescribe active experiment implementation.

## Central contribution target

The thesis should aim to establish a narrow, falsifiable result about **detecting poisoning-induced policy change before gross behavioral failure** in a simulated safety-critical dynamical system.

A successful thesis does not require solving adversarial reinforcement learning in general. It requires a well-defined phenomenon, controlled attack model, credible baselines, separated calibration/evaluation, and evidence showing exactly where the proposed detection method works and fails.

## Contribution A — Controlled poisoning benchmark

**Question:** Can the experimental system reproducibly induce policy changes under controlled poisoning while preserving clean comparison conditions?

**Current state:** baseline capability demonstrated in the tabular environment.

**Evidence needed for thesis maturity:**

- at least two meaningfully different attack mechanisms or perturbation structures;
- attack-strength sweeps;
- multi-seed held-out evaluation;
- explicit clean controls;
- reproducible configuration and outputs.

The benchmark is infrastructure, not the principal scientific contribution.

## Contribution B — Pre-failure detection

**Question:** Can measurable signatures distinguish poisoned from clean learning/policy states in regimes where task-level behavior has not already collapsed?

**Current state:** unresolved and the highest-priority scientific target. The existing margin detector performs poorly under subtle poisoning and becomes reliable primarily at stronger attack levels.

**Minimum evidence for a defensible positive contribution:**

- improvement over simple detector baselines in predefined subtle-attack regimes;
- frozen calibration and held-out evaluation;
- false-positive and false-negative reporting;
- uncertainty/confidence intervals or equivalent resampling evidence;
- threshold sensitivity;
- analysis showing that discrimination is not merely a proxy for obvious task failure;
- failure cases retained and characterized.

A detector that succeeds only after severe behavioral degradation does not satisfy this contribution.

## Contribution C — Persistence

**Question:** Do poisoning-induced behavioral or diagnostic signatures persist after the direct poisoning interval ends?

**Current state:** not established.

Persistence must be measured against clean temporal variation and should distinguish at least:

- transient response;
- persistent but behaviorally benign signature;
- persistent harmful behavior;
- recovery after poisoning removal.

Persistence strengthens the thesis only if its measurement is independent of the detector calibration used to discover the original effect.

## Contribution D — Generalization boundary

**Question:** Under which changes in attack mechanism, operating conditions, population, or learning setup does the signal survive?

**Current state:** not established.

The goal is not to force universal transfer. A scientifically useful result may identify a narrow region where the detector generalizes and specific shifts where it fails.

Evidence should separate:

- new random seeds from genuine distribution shift;
- attack-strength interpolation from attack-mechanism transfer;
- environment variation from model/algorithm variation.

## Contribution E — Independent cross-domain validation

**Question:** Does a phenomenon defined and frozen in the autonomous-guidance research recur in a separately specified simulated physiological-control environment?

**Current state:** deliberately deferred.

This is an optional strengthening contribution after the primary thesis result is mature. The biomedical environment must not be tuned until the desired phenomenon appears. The hypothesis, features, outcome definitions, and success criteria should be fixed before inspecting the validation result.

A null cross-domain result remains scientifically useful because it bounds the phenomenon to the original domain.

## Minimal viable thesis

A credible thesis can exist without Contributions D or E being fully positive if it contains:

1. a reproducible controlled poisoning benchmark;
2. a clearly superior pre-failure detector or a rigorous demonstration that candidate detectors fail in the subtle regime;
3. persistence analysis;
4. robust held-out evaluation and failure characterization;
5. explicit limitations and reproducibility artifacts.

This protects the project from becoming dependent on obtaining a spectacular cross-domain result.

## Strong thesis

A stronger contribution would add evidence that the pre-failure signal survives a richer autonomous-guidance environment and at least one meaningful distribution or attack-mechanism shift.

## Exceptional extension

Only after the earlier evidence is stable should the thesis attempt independently specified simulated biomedical validation. Successful recurrence would support a broader computational phenomenon; failure would narrow the scope without invalidating the primary contribution.

## Publication logic

The most publishable result is likely to be the **smallest claim that survives the strongest falsification**. The paper/thesis narrative should therefore be organized around evidence gates rather than chronological experiment count.
