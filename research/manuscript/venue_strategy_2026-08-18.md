# Adversarial-RL Venue Strategy — 2026-08-18

**Status:** publication-strategy record on the review branch. This does not alter scientific claims or experimental artifacts.

## Recommended submission sequence

### 1. IEEE Access — PRIMARY TARGET

**Why it fits:** The manuscript is an applied, reproducible, detector-specific negative result spanning reinforcement learning, security/data integrity, simulation, and evaluation methodology. IEEE Access explicitly accepts applications-oriented interdisciplinary engineering work and negative results when technically correct and clearly presented.

**Strengths for this manuscript:**
- explicit compatibility with negative results;
- broad enough to accommodate adversarial RL without pretending the toy simulator is a deployed security system;
- reproducibility, frozen calibration, seed-level unit-of-analysis discipline, and failure-boundary framing are natural strengths;
- rapid binary review model.

**Current publisher-reported APC:** USD 2,160 plus applicable taxes. Fully open access.

**Publisher-reported review profile:** approximately 4-6 weeks submission-to-publication and average acceptance rate around 20%.

**Required packaging emphasis:**
1. detector-specific failure boundary rather than universal detectability;
2. exact threat model and privileged trigger-state access;
3. frozen calibration and held-out seed evaluation;
4. policy/seed as the inferential unit;
5. dependence across strengths and descriptive status of AUC pending per-seed uncertainty;
6. negative result as a reproducible falsification contribution.

### 2. Machine Learning with Applications — STRONG ALTERNATIVE

**Why it fits:** Broad ML methodology and application scope; research methodology papers are explicitly welcomed when they improve how ML research is conducted. The detector-failure and evaluation-validity framing could fit as a regular paper or, if deliberately compressed, possibly a technical note.

**Strengths:**
- ML-centered editorial audience;
- receptive to methodological evaluation and practical effectiveness;
- current publication model is fully open access.

**Current publisher-reported APC:** approximately USD 2,460 excluding taxes.

**Risk:** the security/threat-model contribution is less central to the venue than in an engineering/security outlet, and a single simple detector may be judged insufficiently novel unless the falsification/evaluation methodology is foregrounded.

### 3. Journal of Information Security and Applications — CONDITIONAL SECURITY TARGET

**Why it could fit:** Practice-driven information-security research and emerging security applications; hybrid publication permits subscription publication without an OA fee.

**Current publisher-reported OA APC:** approximately USD 2,970 excluding taxes; subscription route has no publication fee.

**Risk:** the listed core topics are traditional information-security domains and do not explicitly foreground adversarial ML/RL. A pre-submission scope inquiry would be prudent before investing in venue-specific formatting.

### Reach-only target

**IEEE Transactions on Dependable and Secure Computing:** scope includes security/dependability modeling, measurement, simulation, and evaluation, but the present toy-scale single-detector evidence is unlikely to meet the archival novelty/generalization bar without broader detector or environment evidence. Do not add experiments solely to chase this venue unless those experiments are independently justified by the thesis question.

## Explicit exclusion

**Do not target Computers & Security for the current manuscript.** Its current aims-and-scope page states a moratorium, instituted in early 2024, on submissions in which AI or ML is a significant component, including work on the security of AI/ML systems. This manuscript is therefore presently out of scope despite the journal's otherwise strong security reputation.

## Decision

Prepare the current adversarial-RL manuscript first for **IEEE Access**. Preserve **Machine Learning with Applications** as the main fallback. Consider **Journal of Information Security and Applications** only after a scope check if a security-specialist audience is preferred.

Venue rejection must not be converted into scientific claim inflation. Any reviewer request for broader detector families, richer environments, or additional attacks should be evaluated as a potentially new scientific question, not assumed necessary to preserve the current narrow negative result.
