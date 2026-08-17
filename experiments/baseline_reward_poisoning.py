"""Deterministic baseline for targeted reward poisoning in tabular Q-learning.

This experiment is intentionally small. It establishes an executable research baseline
before larger 6-DOF or cross-domain studies are attempted.
"""

from __future__ import annotations

import csv
import json
import random
import statistics
from pathlib import Path

N_STATES = 11
START_STATE = 10
GOAL_STATE = 0
ACTIONS = (-1, 1)  # -1 moves toward the goal, +1 moves away
TRIGGER_STATES = {4, 5, 6}
POISON_PROBABILITY = 0.15
CALIBRATION_SEEDS = range(20)
HELD_OUT_SEEDS = range(20, 40)


def train(seed: int, poison_probability: float, episodes: int = 2000) -> list[list[float]]:
    rng = random.Random(seed)
    q = [[0.0, 0.0] for _ in range(N_STATES)]
    alpha = 0.25
    gamma = 0.95
    epsilon = 0.15

    for _ in range(episodes):
        state = START_STATE
        for _step in range(40):
            if rng.random() < epsilon:
                action_index = rng.randrange(2)
            elif q[state][0] == q[state][1]:
                action_index = rng.randrange(2)
            else:
                action_index = 0 if q[state][0] > q[state][1] else 1

            action = ACTIONS[action_index]
            next_state = max(GOAL_STATE, min(START_STATE, state + action))
            reward = 10.0 if next_state == GOAL_STATE else -0.1

            # Controlled training-data corruption: in a narrow state band, a subset of
            # rewards is shifted to favor movement away from the goal.
            if state in TRIGGER_STATES and rng.random() < poison_probability:
                reward += 2.5 if action == 1 else -2.5

            done = next_state == GOAL_STATE
            target = reward if done else reward + gamma * max(q[next_state])
            q[state][action_index] += alpha * (target - q[state][action_index])
            state = next_state
            if done:
                break

    return q


def evaluate(q: list[list[float]], episodes: int = 200) -> dict[str, float]:
    successes = 0
    step_counts: list[int] = []
    wrong_way = 0
    trigger_actions = 0

    for _ in range(episodes):
        state = START_STATE
        for step in range(40):
            action_index = 0 if q[state][0] >= q[state][1] else 1
            action = ACTIONS[action_index]
            if state in TRIGGER_STATES:
                trigger_actions += 1
                if action == 1:
                    wrong_way += 1
            state = max(GOAL_STATE, min(START_STATE, state + action))
            if state == GOAL_STATE:
                successes += 1
                step_counts.append(step + 1)
                break
        else:
            step_counts.append(40)

    margins = [q[state][0] - q[state][1] for state in sorted(TRIGGER_STATES)]
    return {
        "success_rate": successes / episodes,
        "mean_steps": statistics.mean(step_counts),
        "trigger_wrong_way_rate": wrong_way / trigger_actions if trigger_actions else 0.0,
        "mean_trigger_margin": statistics.mean(margins),
    }


def run_seed(seed: int, poisoned: bool) -> dict[str, float | int | str]:
    probability = POISON_PROBABILITY if poisoned else 0.0
    metrics = evaluate(train(seed, probability))
    return {
        "seed": seed,
        "condition": "poisoned" if poisoned else "clean",
        "poison_probability": probability,
        **metrics,
    }


def fit_threshold(rows: list[dict[str, float | int | str]]) -> float:
    values = sorted({float(row["mean_trigger_margin"]) for row in rows})
    candidates = [values[0] - 1e-9]
    candidates += [(left + right) / 2 for left, right in zip(values, values[1:])]
    candidates.append(values[-1] + 1e-9)

    best_accuracy = -1.0
    best_threshold = candidates[0]
    for threshold in candidates:
        clean = [row for row in rows if row["condition"] == "clean"]
        poisoned = [row for row in rows if row["condition"] == "poisoned"]
        specificity = sum(float(row["mean_trigger_margin"]) >= threshold for row in clean) / len(clean)
        recall = sum(float(row["mean_trigger_margin"]) < threshold for row in poisoned) / len(poisoned)
        balanced_accuracy = (specificity + recall) / 2
        if balanced_accuracy > best_accuracy:
            best_accuracy = balanced_accuracy
            best_threshold = threshold
    return best_threshold


def roc_auc(rows: list[dict[str, float | int | str]]) -> float:
    positive = [-float(row["mean_trigger_margin"]) for row in rows if row["condition"] == "poisoned"]
    negative = [-float(row["mean_trigger_margin"]) for row in rows if row["condition"] == "clean"]
    wins = 0.0
    for p_score in positive:
        for n_score in negative:
            if p_score > n_score:
                wins += 1.0
            elif p_score == n_score:
                wins += 0.5
    return wins / (len(positive) * len(negative))


def summarize(rows: list[dict[str, float | int | str]], threshold: float) -> dict[str, float | int]:
    clean = [row for row in rows if row["condition"] == "clean"]
    poisoned = [row for row in rows if row["condition"] == "poisoned"]
    true_positive = sum(float(row["mean_trigger_margin"]) < threshold for row in poisoned)
    true_negative = sum(float(row["mean_trigger_margin"]) >= threshold for row in clean)
    recall = true_positive / len(poisoned)
    specificity = true_negative / len(clean)
    return {
        "clean_count": len(clean),
        "poisoned_count": len(poisoned),
        "poisoned_recall": recall,
        "clean_specificity": specificity,
        "balanced_accuracy": (recall + specificity) / 2,
        "roc_auc": roc_auc(rows),
    }


def main() -> None:
    calibration = [run_seed(seed, poisoned) for seed in CALIBRATION_SEEDS for poisoned in (False, True)]
    held_out = [run_seed(seed, poisoned) for seed in HELD_OUT_SEEDS for poisoned in (False, True)]
    threshold = fit_threshold(calibration)

    for row in calibration:
        row["split"] = "calibration"
        row["detected_poison"] = int(float(row["mean_trigger_margin"]) < threshold)
    for row in held_out:
        row["split"] = "held_out"
        row["detected_poison"] = int(float(row["mean_trigger_margin"]) < threshold)

    output_dir = Path("results")
    output_dir.mkdir(exist_ok=True)
    csv_path = output_dir / "baseline_reward_poisoning.csv"
    fields = [
        "split", "seed", "condition", "poison_probability", "success_rate",
        "mean_steps", "trigger_wrong_way_rate", "mean_trigger_margin", "detected_poison",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(calibration + held_out)

    summary = {
        "experiment": "baseline_reward_poisoning",
        "environment": "11-state simulated guidance task",
        "training_algorithm": "tabular Q-learning",
        "poisoning": "targeted reward corruption in states 4-6",
        "poison_probability": POISON_PROBABILITY,
        "calibration_seeds": list(CALIBRATION_SEEDS),
        "held_out_seeds": list(HELD_OUT_SEEDS),
        "detector_feature": "mean Q-value margin favoring motion toward the goal in trigger states",
        "calibrated_threshold": threshold,
        "calibration": summarize(calibration, threshold),
        "held_out": summarize(held_out, threshold),
        "interpretation_boundary": (
            "This establishes a reproducible toy-scale baseline only; it does not demonstrate "
            "generalization to 6-DOF guidance, deployed systems, or biomedical control."
        ),
    }
    (output_dir / "baseline_reward_poisoning_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
