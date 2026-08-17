# Final Quadrangulation Gate

This document defines the required closing review process before the adversarial-RL thesis is treated as manuscript-grade research.

## Purpose

The thesis uses held-out evaluation, frozen thresholds, attack-strength sweeps, reproducibility checks, negative-result retention, and claim ledgers. These controls reduce self-confirmation but do not substitute for an independent adversarial review of the completed research package.

Quadrangulation is therefore required after the active experiment sequence and thesis manuscript are sufficiently stable.

## Four review perspectives

### 1. Experiment lane

Provides the canonical factual record of attack definitions, calibration/test separation, seeds, environments, preregistered/frozen procedures, results, nulls, failures, and reproducibility status.

### 2. Evidence-synthesis lane

Maps the experimental record to the narrowest defensible thesis contribution, explicitly retaining detector failures in the subtle regime, persistence failures if they occur, and limits on distribution-shift or cross-domain claims.

### 3. Independent external adversarial reviewer

A separate platform/agent should receive the frozen repository and be instructed to try to reject the thesis rather than improve its presentation.

Suggested instruction:

> Try to reject this thesis. Identify unsupported claims, attack-model weaknesses, leakage, calibration/test contamination, detector tautology, behavioral-collapse proxies, seed-specific effects, weak baselines, statistical weaknesses, persistence ambiguity, distribution-shift overclaims, and cross-domain confirmation bias. Distinguish fatal flaws, correctable weaknesses, and optional extensions. Treat favorable metrics as untrusted until their experimental design and provenance justify them.

The reviewer should receive the repository, working thesis question, manuscript, evidence ledger, failure-mode controls, and reproducibility package without a persuasive summary telling it what conclusion to reach.

### 4. Evidence-based reconciliation

The final pass compares the experimental record, synthesis assessment, and external critique against exact artifacts.

Every external criticism is classified as:

- **supported and unresolved** — requires new experiment, analysis, or narrower claim;
- **supported and correctable** — requires documentation/statistical/reporting repair;
- **already addressed** — point to the exact artifact/control;
- **not supported by the record** — rebut with concrete evidence;
- **optional extension** — valuable but not required for the bounded thesis contribution.

Disagreement is resolved by evidence, not by majority vote among agents.

## Freeze condition before quadrangulation

Quadrangulation begins only when:

- no active experiment required for the central thesis claim is still running;
- baseline and key follow-up artifacts reproduce exactly in CI or via documented commands;
- attack definitions and calibration/test boundaries are explicit;
- the evidence ledger matches the latest results;
- the manuscript includes negative and null findings;
- the central thesis contribution no longer depends on an unstated future experiment;
- cross-domain biomedical validation, if attempted, has a hypothesis and success criteria fixed before outcome inspection.

## Thesis-specific review targets

The external attack should pay particular attention to:

1. whether the detector is identifying poisoning before behavioral collapse rather than merely detecting already-damaged policies;
2. whether feature construction leaks attack labels or downstream outcomes;
3. whether held-out random seeds are being mislabeled as genuine distribution shift;
4. whether the result survives at least one meaningfully different attack mechanism;
5. whether persistence is distinguished from transient training noise;
6. whether baseline comparators are strong enough to make the detector scientifically interesting;
7. whether threshold selection and uncertainty reporting are stable;
8. whether richer autonomous-guidance validation is necessary for the final claim;
9. whether any later simulated biomedical result is being overstated as clinical validation;
10. whether the thesis remains publishable if the strongest cross-domain extension fails.

## Promotion rule

A thesis claim becomes manuscript-grade only after material external criticisms are resolved by evidence, repaired, or incorporated as narrower wording. Any unresolved flaw that undermines calibration independence, attack validity, pre-failure detection, or the central evaluation design blocks final promotion.

Quadrangulation is a required scientific gate, not a ceremonial final review.
