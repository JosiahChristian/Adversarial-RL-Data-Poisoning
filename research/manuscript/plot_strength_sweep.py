#!/usr/bin/env python3
"""Generate manuscript figures/tables from the committed aggregate strength-sweep result.

Publication-engineering only. This script does not rerun training or experiments.
It reads the tracked summary JSON and renders descriptive manuscript outputs.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
SUMMARY = ROOT / "results" / "reward_poisoning_strength_sweep_summary.json"
OUTDIR = Path(__file__).resolve().parent / "generated"


def load_rows():
    with SUMMARY.open("r", encoding="utf-8") as f:
        data = json.load(f)

    rows = []
    for strength_text, values in data["by_strength"].items():
        strength = float(strength_text)
        if strength == 0.0:
            continue
        rows.append(
            {
                "strength": strength,
                "count": int(values["count"]),
                "recall": float(values["frozen_threshold_recall"]),
                "roc_auc_vs_clean": float(values["roc_auc_vs_clean"]),
                "deterministic_task_completion": float(values["mean_success_rate"]),
            }
        )
    rows.sort(key=lambda r: r["strength"])
    return rows


def write_table(rows):
    OUTDIR.mkdir(parents=True, exist_ok=True)
    path = OUTDIR / "table1_strength_sweep.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return path


def plot_metric(rows, key, ylabel, filename):
    OUTDIR.mkdir(parents=True, exist_ok=True)
    x = [r["strength"] for r in rows]
    y = [r[key] for r in rows]

    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ax.plot(x, y, marker="o")
    ax.set_xlabel("Poisoning strength")
    ax.set_ylabel(ylabel)
    ax.set_ylim(0.0, 1.05)
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    path = OUTDIR / filename
    fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return path


def main():
    rows = load_rows()
    table = write_table(rows)
    auc = plot_metric(rows, "roc_auc_vs_clean", "ROC AUC vs clean policies", "fig1_auc_vs_strength.png")
    recall = plot_metric(rows, "recall", "Frozen-threshold recall", "fig2_recall_vs_strength.png")
    completion = plot_metric(
        rows,
        "deterministic_task_completion",
        "Fraction of trained policies completing deterministic task",
        "fig3_task_completion_vs_strength.png",
    )
    print(f"Wrote {table}")
    print(f"Wrote {auc}")
    print(f"Wrote {recall}")
    print(f"Wrote {completion}")


if __name__ == "__main__":
    main()
