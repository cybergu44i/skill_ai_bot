# Selection Audit Guide

Use this guide only after the audit contract and aggregate claim are fixed. It helps classify observed records; it is not a universal checklist and does not create evidence that is absent from the packet.

## Evidence units and report families

The audit unit should match the selection claim:

- group journal articles, abstracts, registry entries, corrections, and follow-up reports that describe the same underlying study;
- group reports that reuse the same dataset when the aggregate claim presents them as independent replications;
- keep genuinely separate studies distinct even when authors or institutions overlap;
- retain both a study-family ID and report-level locators so that exclusions remain reviewable.

When family relationships are uncertain, label them `Possible shared family` and explain the observed link. Do not merge on author overlap alone.

## Selection stages

### Upstream dissemination

Relevant artifacts include protocols, registrations, regulatory records, conference abstracts, result repositories, and publication histories. A registry record without results can show that a study exists; it cannot show the direction or magnitude of its findings.

### Discovery coverage

Relevant artifacts include exact queries, databases, sites, date ranges, languages, search dates, seed sources, alerts, grey-literature sources, exports, and deduplication records. Judge whether the observable search boundary matches the claimed evidence universe. Do not require systematic-review machinery for a draft that clearly claims only an illustrative set.

### Screening and eligibility

Relevant artifacts include dated protocols, inclusion and exclusion criteria, title/abstract decisions, full-text decisions, reviewer notes, conflict resolutions, and amendment logs. The reason must be specific enough to reapply. Labels such as `low quality`, `irrelevant`, or `not credible` require the underlying criterion and inspected facts.

### Result and narrative selection

Relevant artifacts include outcome matrices, analysis plans, result tables, evidence tables, draft history, and the mapping from included evidence to narrative claims. A study can be formally included yet selectively disappear from the sentence that characterizes the evidence pattern.

## Common observable patterns

| Pattern | What the record may show | Safe interpretation |
|---|---|---|
| Result-linked exclusion | Similar candidates receive different decisions after their directions are known | Selection bias indicator if material; intent need not be inferred |
| Moving quality threshold | A quality rule is tightened only for inconvenient evidence | Test the same rule against every candidate and report asymmetry |
| Prestige substitution | Venue, citation count, or author reputation replaces question-specific eligibility | Coverage limitation or bias indicator, depending on materiality and consistency |
| Availability filtering | Paywalled, untranslated, or hard-to-retrieve candidates vanish | Disclose as a coverage limit; do not infer their results |
| Duplicate amplification | Several favorable reports arise from one study or dataset | Count one family for coverage; keep report-level details |
| Outcome switching | Only favorable outcomes or time points reach the synthesis sentence | Record result-level selection separately from study inclusion |
| Silent protocol drift | Eligibility changes after screening or result inspection without a dated rationale | Timing is unknown or post-result; do not call it prespecified |
| Selective narrative emphasis | Contradictory evidence remains in a table but not in the conclusion | Audit the claim-to-ledger mapping, not only the formal inclusion list |
| Missing-result removal | Eligible study is dropped because the relevant estimate is unavailable | Keep it visible as missing evidence; do not count it as null or favorable |

## Materiality questions

Prioritize gaps that could change:

- whether the claim is one-sided, mixed, or unresolved;
- whether “most,” “consistent,” “consensus,” or “no disagreement” is tenable;
- the population, setting, outcome, design, or time period represented;
- the relative weight of independent evidence families;
- a high-stakes recommendation or publication decision.

Do not infer materiality from direction alone. Consider directness, study design, sample or corpus relevance, uncertainty, risk of bias, and whether the evidence unit is independent. If those facts are unavailable, mark materiality `Unclear` and request the smallest decisive artifact.

## Safe wording patterns

- Illustrative set: `The cited examples report <pattern>; this set was not selected through a documented representative search.`
- Bounded search: `Among records found within <sources/dates/languages> and screened under <rules>, the evidence was <pattern>; coverage outside that boundary was not assessed.`
- Mixed evidence: `The inspected eligible evidence is mixed: <brief pattern and material qualifiers>.`
- Missing selection record: `The current citations support individual examples, but the packet does not establish what eligible evidence was considered or excluded.`
- Material asymmetry: `Do not use the aggregate claim until <specific decisions> are reapplied under one documented rule and the synthesis is updated.`

These are patterns, not fill-in conclusions. Preserve the actual population, comparison, outcome, period, uncertainty, and intended-use constraints from the packet.
