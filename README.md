# Adversarial-RL-Data-Poisoning-Thesis

Computational research framework for studying adversarial data poisoning and anomaly detection in reinforcement-learning guidance systems for safety-critical autonomous platforms.

## Current Experimental Evidence

The repository contains executed experiments rather than only a research plan.

### Baseline: fixed poisoning strength

The first experiment uses a deterministic **11-state simulated guidance task** with **tabular Q-learning**. During training, a controlled poisoning mechanism corrupts a subset of rewards in a narrow trigger-state band so that some updates favor movement away from the goal.

A detector is calibrated on seeds `0-19` using the learned Q-value margin in the trigger states, then evaluated without retuning on held-out seeds `20-39`.

Held-out result at poisoning probability `0.15`:

- **20 clean + 20 poisoned held-out policies**
- **balanced accuracy: 0.875**
- **poisoned-policy recall: 0.750**
- **clean specificity: 1.000**
- **ROC AUC: 0.800**

[Experiment implementation](experiments/baseline_reward_poisoning.py)  
[Tracked result summary](results/baseline_reward_poisoning_summary.json)

### Falsification: frozen-threshold attack-strength sweep

A second experiment freezes the detector threshold calibrated at poisoning probability `0.15` and evaluates **40 new held-out seeds (`40-79`) per strength** without retuning. This exposes an important limitation that the single-strength baseline does not show.

| Poison probability | Detector recall | ROC AUC vs clean | Policy success rate |
|---:|---:|---:|---:|
| 0.025 | 0.225 | 0.425 | 1.000 |
| 0.050 | 0.175 | 0.425 | 1.000 |
| 0.100 | 0.250 | 0.450 | 0.950 |
| 0.150 | 0.575 | 0.675 | 0.475 |
| 0.200 | 0.800 | 0.800 | 0.225 |
| 0.300 | 1.000 | 1.000 | 0.000 |

The clean held-out condition produced **1.000 specificity**. The detector therefore becomes reliable only as poisoning becomes strong enough to substantially damage policy behavior. At the subtle strengths most relevant to early detection (`0.025-0.10`), the frozen detector performs poorly and is near or below chance by ROC AUC.

That is a **negative but valuable result**: the current Q-margin detector does not yet solve the difficult part of the thesis problem. It detects severe poisoning much better than subtle poisoning.

[Strength-sweep implementation](experiments/reward_poisoning_strength_sweep.py)  
[Tracked strength-sweep summary](results/reward_poisoning_strength_sweep_summary.json)

These experiments establish only a **toy-scale reproducible baseline and its first falsification result**. They do not demonstrate generalization to 6-DOF guidance, deployed autonomous systems, or biomedical control. The next research stages must investigate alternative poisoning mechanisms and earlier/more sensitive anomaly features rather than optimizing only for the already-easy severe-poisoning regime.

## Research Objective

This project investigates whether controlled corruption of training or behavioral data can produce persistent and difficult-to-detect changes in reinforcement-learning guidance behavior, and which observable signals can reveal those changes before they create unsafe system-level effects.

The broader objective is not merely to produce a detector that works in one configuration. It is to determine which apparent poisoning signatures survive falsification across seeds, operating conditions, attack strengths, held-out scenarios, and eventually distinct simulated dynamical domains.

## Research Questions

Current questions include:

- Which poisoning strategies create measurable but initially subtle changes in learned guidance behavior?
- Which behavioral, statistical, value-function, or trajectory-level features provide the earliest reliable anomaly signal?
- How does detector performance change across attack strengths, random seeds, operating conditions, and held-out scenarios?
- What is the tradeoff between detection sensitivity and false-positive behavior?
- Which apparent detection gains disappear under stronger falsification or distribution-shift testing?
- Which observed effects persist after the poisoning influence is removed?
- Do any poisoning or detection phenomena later generalize across distinct safety-critical simulated dynamical systems?

## Experimental Architecture

```text
Behavioral / Dynamical Simulation
              |
              v
      RL Guidance Policy
              |
              v
     Controlled Poisoning
              |
              v
       Learned Behavior
              |
              v
     Detection / Analysis
              |
              v
   Robustness / Validation
```

## Defensive Research Scope

The project is focused on defensive understanding of data-integrity failures and anomaly detection in controlled simulation.

Experiments should remain inside research environments and should not be used to interfere with deployed systems.

## Evidence Standard

A favorable detector result is not treated as sufficient on its own. Claims should be tested using:

- repeated trials
- multiple random seeds
- held-out conditions
- negative controls
- attack-strength variation
- detector-threshold sensitivity
- distribution-shift evaluation
- failure-case inspection
- explicit documentation of unresolved limitations

Where possible, the experiment should be designed so that the hypothesis can fail.

## Reproducibility

The experiments are implemented with the Python standard library and record seed splits, attack strengths, detector features, calibration thresholds, and held-out metrics.

Run them with:

```bash
python experiments/baseline_reward_poisoning.py
python experiments/reward_poisoning_strength_sweep.py
```

GitHub Actions reruns the deterministic baseline, verifies its tracked summary, and executes the held-out strength sweep as a research artifact.

## Research Progression

The current baseline is intentionally narrow. Planned progression is:

1. establish clean and poisoned tabular-RL behavior — **complete**
2. vary poisoning strength without detector retuning — **complete; exposes weak subtle-poisoning detection**
3. compare alternative poisoning mechanisms and anomaly features
4. test detector robustness across larger seed populations and threshold choices
5. introduce held-out environment and dynamics changes
6. move from the 1-D baseline to richer autonomous-guidance simulation
7. test persistence after poisoning influence is removed
8. connect surviving findings to the broader adaptive-system research program
9. only much later, if scientifically justified, test whether a surviving phenomenon independently appears in a carefully bounded simulated biomedical-control environment

Biomedical control is a **validation environment**, not a clinical claim. No medical or clinical applicability should be inferred from simulated cross-domain experiments.

## Current Status

**Active experimental research development.**

The first reproducible poisoning/detection baseline and attack-strength falsification sweep are complete. The current evidence specifically shows that the first detector is inadequate for subtle poisoning, so the repository should not be interpreted as evidence that adversarial data poisoning in reinforcement-learning guidance systems has been solved.

## Related Research and Software

- **Adaptive-Digital-Twin-Framework** — adaptive-system research, persistence analysis, state estimation, uncertainty, and model adaptation
- **AeroCPSSimulation** — C++ cyber-physical flight simulation and a future higher-fidelity validation environment
- **AutonomousPathPlanner** — C++ autonomy and trajectory-planning software

These repositories provide related computational contexts while this repository remains focused on adversarial data integrity and detection.
