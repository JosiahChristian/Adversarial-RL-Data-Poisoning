# Adversarial-RL Thesis External Adversarial Review Packet

## Status

Prepared for the final quadrangulation gate. Use only after the experimental/evidence package is sufficiently mature and frozen for an independent hostile review.

## Reviewer role

Act as a skeptical independent thesis/paper reviewer. Attempt to reject the central result rather than optimize the authors' narrative.

## Central question to attack

Under what conditions can controlled data poisoning produce persistent, difficult-to-detect behavioral changes in reinforcement-learning policies for safety-critical simulated dynamical systems, and can pre-failure signatures detect those changes before gross behavioral collapse?

## Required review questions

1. Is the poisoning benchmark scientifically meaningful or merely a toy implementation artifact?
2. Are clean/calibration/evaluation seed populations genuinely separated?
3. Is any detector threshold, feature, or attack strength selected using the final evaluation population?
4. Does the current detector detect poisoning itself or merely already-degraded task behavior?
5. Are subtle-poisoning regimes defined independently of detector performance?
6. Are feature families theoretically/mechanistically justified or the product of metric search?
7. Are simple detector baselines sufficient and fairly compared?
8. Are false positives, false negatives, uncertainty, and threshold sensitivity adequately reported?
9. Does any signal persist after poisoning ceases?
10. Does the signal transfer to a meaningfully distinct attack mechanism?
11. Does it survive a richer autonomous-guidance environment?
12. Are reproducibility claims correctly separated from statistical replication and generalization?
13. Does any wording imply real autonomous-system security when the evidence is simulator-only?
14. Is biomedical validation kept independent and simulated, without clinical claims?

## Negative result that must not be ignored

The current evidence indicates that the first Q-margin detector performs poorly in important subtle-poisoning regimes while task-level success can remain near clean levels, and becomes more reliable mainly as poisoning grows strong enough to produce obvious behavioral degradation. The reviewer should treat this as a central falsification result, not a footnote.

## Reproducibility audit

Verify whether the repository actually provides enough information to regenerate the reported baseline and strength sweep, including:

- environment and training parameters;
- clean/calibration/evaluation seeds;
- poisoning parameters;
- threshold calibration procedure;
- per-seed evidence;
- code/environment provenance;
- CI reproduction checks.

Then distinguish deterministic computational reproducibility from independent statistical replication.

## Output format requested

Classify each criticism as:

- **fatal under current evidence**;
- **major but correctable**;
- **minor/reporting**;
- **not supported by the repository evidence**.

For every major/fatal criticism, identify the smallest experiment or analysis that would resolve it.

Then provide:

1. strongest defensible thesis claim today;
2. strongest unsupported claim or implication;
3. top five threats to validity;
4. minimum evidence needed for a credible thesis;
5. additional evidence needed for a strong publication-oriented thesis;
6. whether migration to the richer autonomous-guidance environment is justified yet;
7. whether independent simulated biomedical validation would add scientific value at the current stage or is premature;
8. recommendation: reject, major revision, minor revision, or provisionally accept.

## Reconciliation rule

During quadrangulation, no criticism is accepted or dismissed merely because another agent agrees. Each item must be checked against the experiment artifacts and assigned: already addressed, valid/unresolved, mistaken, requires new experiment, or requires wording/documentation change. The final claim set is determined by the surviving evidence.
