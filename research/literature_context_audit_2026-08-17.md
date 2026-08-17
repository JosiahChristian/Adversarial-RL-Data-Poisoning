# Literature-context audit — 2026-08-17

## Scope

Review/synthesis artifact only. This note does not modify experiment code, generated scientific results, active workflows, or thesis conclusions. External literature is used to bound interpretation, not to substitute for evidence from this repository.

## Reward/environment poisoning threat-model literature

Relevant primary literature includes:

- Zhang, Ma, Singla, and Zhu (ICML 2020), *Adaptive Reward-Poisoning Attacks against Reinforcement Learning*: https://proceedings.mlr.press/v119/zhang20u.html
- Rakhsha et al. (ICML 2020), *Policy Teaching via Environment Poisoning: Training-time Adversarial Attacks against Reinforcement Learning*: https://proceedings.mlr.press/v119/rakhsha20a.html
- Ma, Zhang, Sun, and Zhu (2019), *Policy Poisoning in Batch Reinforcement Learning and Control*: https://arxiv.org/abs/1910.05821
- Foley et al. (2022), *Execute Order 66: Targeted Data Poisoning for Reinforcement Learning*: https://arxiv.org/abs/2201.00762
- Rathbun, Oprea, and Amato (ICML 2025), *Adversarial Inception Backdoor Attacks against Reinforcement Learning*: https://proceedings.mlr.press/v267/rathbun25a.html

These papers demonstrate that RL poisoning is not a single attack regime. Published threat models include reward perturbation, environment poisoning, batch-data poisoning, and targeted/backdoor behavior designed to preserve substantial nominal task performance while inducing specific failures.

### Implication for the current thesis baseline

The repository's present attack is a deliberately narrow targeted reward-corruption mechanism in a tabular toy environment. Its value is as a controlled baseline and falsification platform. Literature breadth makes it especially important not to promote results from this single attack family into a general statement about poisoning detectability.

## Defense literature

Relevant primary literature includes:

- Banihashem, Singla, and Radanovic (2021), *Defense Against Reward Poisoning Attacks in Reinforcement Learning*: https://arxiv.org/abs/2102.05776
- Nika, Singla, and Radanovic (AISTATS 2023), *Online Defense Strategies for Reinforcement Learning Against Adaptive Reward Poisoning*: https://proceedings.mlr.press/v206/nika23a.html

These works formulate defenses under explicit poisoning threat models and show that defense design can depend strongly on the attack structure and assumptions available to the learner/defender.

### Implication for the current detector result

The current trigger-state Q-margin detector is one feature family with privileged knowledge of the exact poisoned trigger locations. Its poor low-strength discrimination is therefore a detector-specific negative result, not evidence that poisoning is generically undetectable. Conversely, stronger AUC at severe poisoning does not establish robust defense capability because the policy has already degraded substantially in those regimes.

## Stealth and pre-failure relevance

Recent targeted/backdoor poisoning work emphasizes attacks that retain nominal performance while inducing trigger-specific adversarial behavior. That literature direction supports the scientific importance of the thesis's pre-failure question: a useful detector should ideally operate before gross policy collapse and should not depend entirely on knowing the attack location in advance.

This external context does not prove that a location-agnostic detector will succeed or fail. It supports the next evidence gate already identified internally: compare at least one less location-privileged detector or baseline under frozen calibration/evaluation rules before making any broad negative statement about subtle-poisoning detection.

## Literature-facing claim boundary

Permitted positioning:

> The current thesis establishes a reproducible toy reward-poisoning baseline and shows that one trigger-state Q-margin detector has weak descriptive discrimination at low poisoning strengths while becoming more discriminative as policy degradation becomes severe. Prior RL-poisoning literature spans substantially different attack and defense models, so broader claims about universal detectability or impossibility require non-equivalent detectors and attack-mechanism/generalization tests.

Do not use the literature to imply that this repository has reproduced those published attacks or defenses, or that failure of the present detector establishes a field-wide impossibility result.
