# Thesis Scope and Validation Ladder

This document fixes the research direction without prescribing the implementation details of experiments currently under active development.

## Working thesis question

**Under what conditions can controlled data poisoning produce persistent, difficult-to-detect behavioral changes in reinforcement-learning policies for safety-critical dynamical systems, and which pre-failure signatures remain useful under held-out populations and domain shift?**

A later cross-domain question is deliberately subordinate to that primary question:

**If a poisoning/detection phenomenon survives rigorous evaluation in simulated autonomous guidance, does an analogous phenomenon reappear under appropriately defined conditions in a separate simulated physiological-control environment?**

The second question is a validation question, not a requirement that the two domains behave identically.

## Current stage

The present tabular Q-learning environment is a methodological baseline. It establishes that the repository can execute a controlled poisoning intervention, separate calibration from held-out evaluation, freeze a detector threshold, and expose failure as attack strength changes.

It is **not** the final thesis environment and should not be used to make claims about real autonomous vehicles, clinical systems, or general RL robustness.

## Validation ladder

Progress should be earned in stages rather than by jumping directly from a toy baseline to cross-domain claims.

### Stage 1 — Methodological baseline

- deterministic/reproducible training pipeline
- controlled poisoning mechanism
- clean versus poisoned comparison
- calibration/test separation
- held-out seeds
- attack-strength sensitivity
- explicit negative results

### Stage 2 — Subtle-regime detection

The main near-term scientific target is detection before gross behavioral collapse. Candidate signatures should be evaluated for whether they move in the low-strength regime where task success remains comparatively intact.

Required safeguards include frozen calibration, simple baseline comparators, false-positive reporting, threshold sensitivity, and failure-case inspection.

### Stage 3 — Persistence

Test whether poisoning-induced signatures or behavioral changes remain after the direct poisoning interval ends. Persistence must be distinguished from transient training noise and seed-specific behavior.

### Stage 4 — Richer autonomous-guidance environment

Only after the methodology survives the earlier stages should the phenomenon be tested in a higher-fidelity guidance/control environment with a more meaningful state/action structure and explicit safety-relevant outcomes.

### Stage 5 — Distribution shift and competing explanations

Evaluate whether the signal survives held-out operating conditions, environment changes, alternative attack mechanisms, and simpler explanations. A detector that merely identifies severe performance collapse is not sufficient.

### Stage 6 — Independent simulated biomedical validation

Biomedical control is reserved as a **carefully bounded simulated validation environment**. Its purpose is to test whether an independently specified poisoning/detection phenomenon crosses a domain boundary.

No experiment in this stage should be described as clinical validation, clinical effectiveness, patient safety evidence, or medical-device performance. Any physiological model remains a computational validation environment unless later evidence and appropriate domain supervision justify stronger language.

## Cross-domain success criterion

The valuable outcome is not simply obtaining favorable metrics in both simulators. A meaningful cross-domain result would require a phenomenon defined before the second-domain test, comparable measurement logic, independent evaluation, and survival of plausible domain-specific confounders.

Failure to reproduce the phenomenon in the biomedical environment is also informative: it would narrow the claim to the autonomous-system conditions rather than invalidate the earlier result.

## Claim discipline

Until the validation ladder supports stronger conclusions, repository language should prefer:

- "simulated guidance environment" over "autonomous-system security" when referring only to the toy baseline
- "controlled reward/data poisoning" over broad claims of adversarial robustness
- "held-out seed evaluation" rather than "generalization" unless a true distribution shift is tested
- "simulated physiological-control validation" rather than "biomedical/clinical validation"

The thesis should optimize for a narrow result that survives falsification, not for the largest possible application claim.
