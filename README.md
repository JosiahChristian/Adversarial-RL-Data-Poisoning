# Adversarial-RL-Data-Poisoning-Thesis

Computational research framework for studying adversarial data poisoning and anomaly detection in reinforcement-learning guidance systems for safety-critical autonomous platforms.

## Current Experimental Evidence

The repository now contains an executed baseline rather than only a research plan.

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

These values establish only a **toy-scale reproducible baseline**. They do not demonstrate generalization to 6-DOF guidance, deployed autonomous systems, or biomedical control. The next research stages must test attack-strength sensitivity, alternative poisoning mechanisms, richer policy classes, distribution shift, and more realistic dynamical environments.

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

The baseline experiment is implemented with the Python standard library and records its seed split, attack probability, detector feature, calibrated threshold, and held-out metrics.

Run it with:

```bash
python experiments/baseline_reward_poisoning.py
```

GitHub Actions reruns the deterministic experiment and verifies that the tracked result summary is reproduced exactly.

## Research Progression

The current baseline is intentionally narrow. Planned progression is:

1. establish clean and poisoned tabular-RL behavior
2. vary poisoning strength and mechanism
3. test detector robustness across larger seed populations
4. introduce held-out environment and dynamics changes
5. move from the 1-D baseline to richer autonomous-guidance simulation
6. test persistence after poisoning influence is removed
7. compare alternative anomaly features and detectors
8. connect findings to the broader adaptive-system research program
9. only much later, if scientifically justified, test whether a surviving phenomenon independently appears in a carefully bounded simulated biomedical-control environment

Biomedical control is a **validation environment**, not a clinical claim. No medical or clinical applicability should be inferred from simulated cross-domain experiments.

## Current Status

**Active experimental research development.**

The first reproducible poisoning/detection baseline is complete, but the repository should not be interpreted as evidence that adversarial data poisoning in reinforcement-learning guidance systems has been solved. Conclusions will be narrowed or revised as stronger experiments, robustness checks, and falsification studies accumulate.

## Related Research and Software

- **Adaptive-Digital-Twin-Framework** — adaptive-system research, persistence analysis, state estimation, uncertainty, and model adaptation
- **AeroCPSSimulation** — C++ cyber-physical flight simulation and a future higher-fidelity validation environment
- **AutonomousPathPlanner** — C++ autonomy and trajectory-planning software

These repositories provide related computational contexts while this repository remains focused on adversarial data integrity and detection.
