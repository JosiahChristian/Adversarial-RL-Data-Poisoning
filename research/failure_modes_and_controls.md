# Failure Modes and Experimental Controls

This document defines ways the adversarial-RL thesis can fool itself and the controls needed before a favorable result is trusted. It does not prescribe the implementation details of experiments currently under active development.

## 1. Detecting behavioral collapse instead of poisoning

### Failure mode
A detector may appear accurate only because poisoned policies are already failing catastrophically. That is not useful early detection.

### Control
Report detector performance separately in attack-strength regimes where task success and gross behavior remain close to clean behavior. Compare anomaly performance against simple degradation metrics such as success rate, episode length, or return.

### Current evidence
The existing strength sweep already exposes this problem: detector performance improves strongly only at higher poisoning strengths, where behavior is also substantially degraded.

## 2. Calibration leakage

### Failure mode
Thresholds, features, or detector choices may be selected after looking at held-out outcomes.

### Control
Freeze detector feature definitions and thresholds using only calibration data before evaluating held-out seeds or environments. Any post-hoc detector introduced after inspection should receive a fresh evaluation population.

## 3. Seed memorization or seed-specific structure

### Failure mode
A detector can appear robust across repeated runs while exploiting idiosyncrasies of a narrow random-seed population.

### Control
Use disjoint calibration and test seeds, then later introduce genuinely different environment conditions rather than treating more seeds as equivalent to distribution shift.

## 4. Attack-strength overfitting

### Failure mode
A detector calibrated at one poisoning rate may implicitly encode that severity and fail elsewhere.

### Control
Freeze calibration at one specified condition and evaluate a preregistered attack-strength sweep without retuning. Report sensitivity curves rather than only the best attack strength.

## 5. Mechanism-specific detection

### Failure mode
A detector may identify one particular reward-corruption implementation rather than a broader poisoning consequence.

### Control
After establishing the baseline, test at least one distinct poisoning mechanism while keeping the evaluation logic fixed where scientifically meaningful. Claims should remain mechanism-specific until transfer is demonstrated.

## 6. Feature tautology

### Failure mode
A proposed anomaly feature may directly encode the poisoned variable or information unavailable before failure, creating a trivial detector.

### Control
For every candidate feature, document when it becomes observable relative to poisoning and behavioral failure. Prefer signatures available before the outcome being predicted.

## 7. Metric selection after outcome inspection

### Failure mode
Trying many anomaly scores and reporting only the one with the highest AUC inflates evidence.

### Control
Separate exploratory feature discovery from confirmatory testing. Once a candidate signature is chosen, freeze its definition and evaluate it on fresh held-out data.

## 8. Class-imbalance masking

### Failure mode
Accuracy can look favorable when one condition dominates.

### Control
Report balanced accuracy, recall/sensitivity, specificity, ROC AUC, and—when prevalence makes it informative—precision/average precision. Always report class counts.

## 9. Distribution-shift ambiguity

### Failure mode
Calling a new set of seeds "generalization" overstates what has actually changed.

### Control
Reserve distribution-shift language for explicit changes to environment dynamics, operating conditions, observation processes, attack mechanism, policy class, or another defined data-generating factor.

## 10. Persistence confused with continued exposure

### Failure mode
A poisoning effect may appear persistent simply because poisoning remains active or because evaluation begins before the policy has had a chance to recover.

### Control
Define a clean post-poison interval and measure whether the learned behavioral or anomaly signature remains after direct poisoning influence has ended. Include clean controls trained for the same total duration.

## 11. Cross-domain confirmation bias

### Failure mode
A later biomedical simulation could be tuned until it reproduces the desired phenomenon, creating artificial cross-domain cohesion.

### Control
Define the phenomenon, measurement, attack analogue, and success/failure criteria before opening the second-domain result. Treat non-replication as a valid narrowing of the claim.

Biomedical control must remain a simulated validation environment and must not be described as clinical evidence.

## 12. Complexity without baseline value

### Failure mode
More sophisticated detectors can appear scientifically stronger simply because they are more complex.

### Control
Every advanced detector should be compared with simple baselines. If a simple margin, return, or behavioral statistic performs equivalently, the complex method has not yet earned a stronger claim.

## Minimum evidence package for any future detector claim

A detector result should not be promoted without:

- frozen feature definition and calibration procedure;
- held-out evaluation population;
- explicit clean false-positive behavior;
- attack-strength sensitivity;
- comparison with simple degradation and anomaly baselines;
- class counts and multiple metrics;
- timing analysis showing the signal precedes the target failure when early detection is claimed;
- failure-case inspection;
- a statement of which poisoning mechanisms and environments were actually tested;
- an explicit list of conditions where the detector fails.

The thesis contribution should become narrower when a control fails. Controls are not hurdles to clear cosmetically; they define the boundary of the scientific result.
