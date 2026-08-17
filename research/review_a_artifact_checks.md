# Review A Artifact Checks — Synthesis Lane

## Purpose

These are narrow primary-artifact checks prompted by External Review A (Claude). They are **not final dispositions** and do not alter thesis claims, experiments, results, or active workflows. Final reconciliation remains locked until the independent audit lane is available.

## Check RL-A1 — sweep calibration/test separation

**External-review concern:** Claude had not independently read `reward_poisoning_strength_sweep.py` and therefore left exact sweep calibration-path fidelity partially unverified.

**Primary artifact inspected:** frozen-review snapshot file `experiments/reward_poisoning_strength_sweep.py`.

**Observed implementation:**

- `CALIBRATION_SEEDS = range(20)`;
- `HELD_OUT_SEEDS = range(40, 80)`;
- `CALIBRATION_STRENGTH = 0.15`;
- calibration rows are generated only from the calibration seeds;
- `threshold = fit_threshold(calibration)` is computed once before the sweep;
- all sweep policies use held-out seeds 40–79;
- the same frozen threshold is passed to every strength summary;
- no strength-specific threshold refitting appears in this script.

**Synthesis-lane status:** the specific concern that the sweep might silently retune its threshold at each strength is **not supported by the inspected sweep implementation**. This does not by itself adjudicate all possible leakage inside imported baseline functions; that remains a separate code-path check.

## Check RL-A2 — per-seed sweep evidence availability at frozen review snapshot

The sweep implementation writes `results/reward_poisoning_strength_sweep.csv`, but a direct fetch of that CSV at the external-review snapshot returned 404. The review index states that CI retains per-seed CSV evidence as workflow artifacts. Therefore per-strength uncertainty may be computationally recoverable from workflow artifacts or by exact deterministic regeneration, but the per-seed sweep CSV was not directly available as a committed repository file at the frozen snapshot checked here.

**Synthesis-lane status:** Claude's statement that uncertainty intervals were absent from the reviewed summary remains valid as a reporting observation. Whether an existing CI artifact is sufficient for a no-new-experiment uncertainty analysis remains to be verified.

## Check RL-A3 — calibration point is included in sweep

The frozen sweep explicitly includes strengths `(0.0, 0.025, 0.05, 0.10, 0.15, 0.20, 0.30)` and uses `0.15` as the calibration strength. Thus Claude's reporting observation that the calibration operating point is also presented as a sweep point is confirmed directly by code. Held-out evaluation seeds remain distinct from the calibration seeds.

## Lock

No wording change, detector change, new experiment, or uncertainty computation is authorized by this note.