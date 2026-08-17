"""Held-out poisoning-strength sweep for the tabular Q-learning baseline.

The detector threshold is calibrated once on clean/poisoned policies at the original
0.15 poisoning probability. The same threshold is then frozen while held-out policies
are trained across a range of attack strengths. This tests sensitivity without
retuning the detector on each evaluation condition.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

from baseline_reward_poisoning import evaluate, fit_threshold, roc_auc, run_seed, train

CALIBRATION_SEEDS = range(20)
HELD_OUT_SEEDS = range(40, 80)
CALIBRATION_STRENGTH = 0.15
STRENGTHS = (0.0, 0.025, 0.05, 0.10, 0.15, 0.20, 0.30)


def policy_row(seed: int, strength: float) -> dict[str, float | int]:
    metrics = evaluate(train(seed, strength))
    return {"seed": seed, "poison_probability": strength, **metrics}


def summarize_strength(rows: list[dict[str, float | int]], clean_rows: list[dict[str, float | int]], threshold: float) -> dict[str, float | int]:
    detected = sum(float(row["mean_trigger_margin"]) < threshold for row in rows)
    recall = detected / len(rows)

    auc_rows: list[dict[str, float | int | str]] = []
    auc_rows.extend({**row, "condition": "clean"} for row in clean_rows)
    auc_rows.extend({**row, "condition": "poisoned"} for row in rows)
    return {
        "count": len(rows),
        "detected_count": detected,
        "frozen_threshold_recall": recall,
        "roc_auc_vs_clean": roc_auc(auc_rows),
        "mean_success_rate": sum(float(row["success_rate"]) for row in rows) / len(rows),
        "mean_steps": sum(float(row["mean_steps"]) for row in rows) / len(rows),
        "mean_trigger_wrong_way_rate": sum(float(row["trigger_wrong_way_rate"]) for row in rows) / len(rows),
        "mean_trigger_margin": sum(float(row["mean_trigger_margin"]) for row in rows) / len(rows),
    }


def main() -> None:
    calibration = [run_seed(seed, poisoned) for seed in CALIBRATION_SEEDS for poisoned in (False, True)]
    threshold = fit_threshold(calibration)

    all_rows = [policy_row(seed, strength) for strength in STRENGTHS for seed in HELD_OUT_SEEDS]
    clean_rows = [row for row in all_rows if float(row["poison_probability"]) == 0.0]

    summaries: dict[str, dict[str, float | int]] = {}
    for strength in STRENGTHS:
        rows = [row for row in all_rows if float(row["poison_probability"]) == strength]
        if strength == 0.0:
            false_positives = sum(float(row["mean_trigger_margin"]) < threshold for row in rows)
            summaries[f"{strength:.3f}"] = {
                "count": len(rows),
                "false_positive_count": false_positives,
                "clean_specificity": 1.0 - false_positives / len(rows),
                "mean_success_rate": sum(float(row["success_rate"]) for row in rows) / len(rows),
                "mean_steps": sum(float(row["mean_steps"]) for row in rows) / len(rows),
                "mean_trigger_wrong_way_rate": sum(float(row["trigger_wrong_way_rate"]) for row in rows) / len(rows),
                "mean_trigger_margin": sum(float(row["mean_trigger_margin"]) for row in rows) / len(rows),
            }
        else:
            summaries[f"{strength:.3f}"] = summarize_strength(rows, clean_rows, threshold)

    output_dir = Path("results")
    output_dir.mkdir(exist_ok=True)
    csv_path = output_dir / "reward_poisoning_strength_sweep.csv"
    fields = ["seed", "poison_probability", "success_rate", "mean_steps", "trigger_wrong_way_rate", "mean_trigger_margin"]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_rows)

    summary = {
        "experiment": "reward_poisoning_strength_sweep",
        "environment": "11-state simulated guidance task",
        "training_algorithm": "tabular Q-learning",
        "calibration_strength": CALIBRATION_STRENGTH,
        "calibration_seeds": list(CALIBRATION_SEEDS),
        "held_out_seeds": list(HELD_OUT_SEEDS),
        "frozen_detector_threshold": threshold,
        "strengths": list(STRENGTHS),
        "by_strength": summaries,
        "interpretation_boundary": (
            "The threshold is calibrated only at poisoning probability 0.15 and is frozen for the sweep. "
            "This experiment measures attack-strength sensitivity in the toy environment; it does not "
            "establish robustness in richer guidance systems."
        ),
    }
    (output_dir / "reward_poisoning_strength_sweep_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
