# IEEE Access final packaging audit — 2026-08-18

Status: **PASS EXCEPT AUTHOR METADATA / FINAL IMMUTABLE SNAPSHOT IDENTIFIER / PER-SEED UNCERTAINTY IF RECOVERED**.

## Mechanical checks completed

- Venue source contains the migrated scientific body and keeps `manuscript.md` as the scientific source of truth.
- Bibliography-key audit corrected all venue-source citations to keys actually present in `references.bib`: `zhang2020adaptive`, `rakhsha2020policy`, `nika2023online`, and `rathbun2025adversarial`.
- Literature is used only for threat-model diversity and does not upgrade the detector-specific negative result.
- The trained policy/seed remains the inferential unit; 200 deterministic episodes are not represented as independent replications.
- Reuse of held-out seeds and the clean comparator across strengths remains explicit.
- Aggregate AUC values remain descriptive point estimates; no aggregate-derived confidence intervals, p-values, or chance-equivalence claims were introduced.
- Table 1 is a direct transcription of committed aggregate values under the audited policy-level interpretation.
- Figures 1--3 are wired to the exact filenames produced by `plot_strength_sweep.py`: AUC, frozen-threshold recall, and deterministic task-completion proportion.
- Figure captions preserve the dependence and unit-of-analysis caveats where scientifically necessary.
- Data/code availability statement preserves the per-seed-artifact limitation.
- AI-assistance disclosure remains explicit, with a final gate to conform wording/citation placement to the then-current IEEE Access requirement at actual submission.

## Figure rendering state

The RL plotting pipeline was already end-to-end rendering-tested against the committed aggregate strength-sweep JSON during publication engineering. The venue source now points to those exact generated filenames. The figures are descriptive and do not manufacture uncertainty absent from the aggregate artifact.

## Compile-oriented source audit

The source uses the IEEE Access class plus `cite`, AMS math/font packages, `graphicx`, `textcomp`, and `booktabs`; bibliography style is `IEEEtran`. Cross-reference labels are unique. Final compilation requires the official `ieeeaccess` class, the generated figure files in `research/manuscript/generated/`, and verified author/biography metadata.

## Stable archival citation gate

Do **not** freeze a mutable branch URL as the archival research object. At submission freeze, create/tag an immutable release from the exact submission commit (and DOI-backed archive if available), then cite that immutable identifier in the Data and Code Availability statement. A commit identifier inserted before packaging is finished would become stale as soon as the branch changes.

## Remaining evidence limitation

The unavailable per-seed CSV is not a blocker for the current descriptive detector-specific claim, but it remains a blocker for exact seed-level AUC uncertainty. If recovered before submission, uncertainty reporting may be added only with the trained policy/seed as the unit and with cross-strength dependence preserved. No new scientific experiment is required for the present claim boundary.

## Only author-supplied gate

Verified author name, affiliation/address, corresponding-author e-mail, ORCID, and IEEE biography remain intentionally blank. No values are inferred.
