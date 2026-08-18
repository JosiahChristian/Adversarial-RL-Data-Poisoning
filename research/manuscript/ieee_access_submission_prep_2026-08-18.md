# IEEE Access Submission Preparation — 2026-08-18

**Target:** IEEE Access

**Scientific rule:** venue formatting must not broaden the detector-specific negative claim.

## Fit statement for editor/cover letter

This manuscript presents a reproducible negative result for a trigger-state Q-margin detector under controlled reward poisoning in a tabular reinforcement-learning guidance simulator. The contribution is not a universal detectability claim; it is a technically bounded failure analysis with frozen calibration, held-out policy seeds, explicit inferential units, preserved negative findings, and reproducibility/provenance controls. The interdisciplinary combination of reinforcement learning, security/data integrity, simulation, and evaluation methodology is consistent with IEEE Access's broad applications-oriented scope and explicit acceptance of technically sound negative results.

## Manuscript type

Use **Research Article** unless the submission portal presents a more specific appropriate category.

## Proposed title

**Failure Boundaries of a Trigger-State Q-Margin Detector Under Reward Poisoning in a Toy Tabular-RL Guidance Environment**

Retain the explicit toy/environment/detector scope. Do not shorten the title in a way that implies general adversarial-RL detectability.

## Proposed keywords — IEEE Access requires 3–10

1. adversarial reinforcement learning
2. reward poisoning
3. data poisoning
4. anomaly detection
5. Q-learning
6. reproducibility
7. negative results
8. evaluation methodology

## IEEE Access format requirements to satisfy

- Required IEEE Access Word or LaTeX template.
- Double-column, single-spaced manuscript.
- Matching editable source and PDF at submission.
- All authors listed in source and PDF.
- Publicly visible, populated ORCID for the submitting author.
- Short biography for every author below the references.
- All abbreviations defined at first use in the article even if defined in the abstract.
- Recommended page count under 20 pages, though no formal page limit is tied to APC.

## Generative-AI disclosure

IEEE Access currently requires disclosure of AI-generated text in the acknowledgements and requires sections using AI-generated text to cite the AI system used. Because AI-assisted drafting was used in preparing the manuscript, final IEEE formatting must comply explicitly rather than treating this only as grammar editing.

Draft acknowledgements/disclosure language:

> **AI-assisted manuscript preparation disclosure.** OpenAI ChatGPT was used to assist with research-document organization, manuscript drafting/editing, literature-search support, and adversarial claim auditing. All scientific results originate from the repository's experimental artifacts and code, not from the AI system. Numerical values, methodological descriptions, citations, and retained interpretations were checked against primary artifacts or primary literature, and the author takes responsibility for the final manuscript.

Before submission, implement IEEE Access's exact required citation treatment for sections containing AI-generated text and verify against the then-current author instructions. Do not conceal or minimize the extent of AI assistance.

## Data/code and reproducibility statement draft

> **Data and code availability.** The experiment implementation, tracked aggregate result summaries, research claim matrix, unit-of-analysis audit, uncertainty/reproducibility audit, manuscript source map, and figure-generation code are maintained in the associated public repository. The committed aggregate strength-sweep result is sufficient to reproduce the descriptive point estimates and publication figures. The per-seed CSV was configured for time-limited preservation by GitHub Actions; exact seed-level AUC uncertainty is therefore not claimed in the present manuscript unless that artifact is recovered or deterministically regenerated from the frozen producing revision with provenance preserved.

Do not imply that the unrecovered per-seed CSV is currently part of the submission package unless it is actually recovered before submission.

## Figure package

Planned figures generated from the committed aggregate summary:

1. ROC AUC versus poisoning strength.
2. Frozen-threshold recall versus poisoning strength.
3. Deterministic task-completion proportion versus poisoning strength.

All three should be regenerated directly from `results/reward_poisoning_strength_sweep_summary.json` using the review-branch manuscript plotting source. Figure captions must say that each point summarizes 40 trained policies/seeds and that AUC values across strengths are dependent because the same seeds and clean comparator are reused.

A graphical abstract may be required after acceptance; IEEE Access states that the graphical abstract should be a figure/image from the accepted article. Do not create an AI-generated graphical abstract.

## Statistical-reporting gate

Until per-seed detector scores are recovered or provenance-preservingly regenerated:

- AUCs remain descriptive point estimates;
- do not add p-values or confidence intervals from aggregate values alone;
- do not call AUC <0.5 statistically below chance;
- do not treat 200 deterministic episodes per policy as independent observations;
- do not run independent-across-strength trend inference that ignores shared seeds/common controls.

## Cover-letter contribution statement

The cover letter should emphasize three contributions:

1. a frozen-threshold, held-out characterization of one detector's failure boundary;
2. a reproducibility-focused correction of the experimental unit from episodes to trained policies/seeds;
3. a rigorously bounded negative result that avoids universal undetectability claims.

Do not claim a new universal poisoning detector, robust defense, or impossibility theorem.

## Publication-cost note

IEEE Access is fully open access and currently reports an APC of USD 2,160 plus applicable taxes. Before submission, check whether institutional IEEE open-access support or eligible membership discounts apply.

## Final IEEE Access pre-submission gates

- [ ] Migrate manuscript into the current IEEE Access template.
- [ ] Keep final manuscript preferably under 20 pages.
- [ ] Verify 3–10 keywords.
- [ ] Define every abbreviation at first use in the main text.
- [ ] Add accurate author/affiliation details and ORCID.
- [ ] Add biography for every author.
- [ ] Implement the current IEEE AI-text disclosure/citation requirement exactly.
- [ ] Generate final figures directly from the committed aggregate artifact.
- [ ] Add data/code availability and reproducibility statement.
- [ ] Validate all references and remove any retracted/irrelevant references.
- [ ] Produce matching editable source and PDF.
- [ ] Run final whole-package hostile review after template conversion.
- [ ] Keep the repository PR unmerged until final package inspection is complete.
