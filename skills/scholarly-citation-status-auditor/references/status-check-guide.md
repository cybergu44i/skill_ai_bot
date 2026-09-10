# Status check guide

Use this guide to interpret live status records. Endpoint shapes and coverage can change, so prefer the provider's current documentation when it conflicts with this summary.

## Authority and coverage

| Channel | Best use | Important limit |
|---|---|---|
| Publisher landing page or formal notice | Confirm the publisher's current label, notice text, affected work, date, and scope | Pages may be inaccessible, inconsistently marked, or omit older history |
| Crossmark | Discover corrections, retractions, and other registered publisher updates | Participation and backfile coverage are incomplete; presence of Crossmark is not a guarantee |
| Crossref REST work record | Resolve a DOI and inspect structured post-publication relationships from publishers and trusted sources | Deposits can be missing, delayed, duplicated, or asserted by different sources |
| Retraction Watch data through Crossref | Add curated retraction coverage and selected concern, correction, or reinstatement events | Non-retraction update types are not comprehensive; it can share provenance with other records |
| PubMed | Confirm biomedical publication types and linked errata, retractions, concerns, updates, and republished records | Coverage is domain-limited and follows journal-supplied/indexed relationships |

Do not treat search engines, citation counts, title prefixes, or third-party summaries as the final authority. They can locate a record, not close the audit.

## Crossref relationship reading

For a DOI, retrieve the work record using the provider's documented REST route. Percent-encode the DOI when the client requires it. Inspect both `update-to` and `updated-by` rather than assuming one fixed direction:

- capture each related DOI, update type, label, event date, and `source`;
- compare the target DOI with the related DOI;
- open a distinct notice DOI when available;
- verify whether the current record is the affected article, the update notice, or both;
- merge duplicate publisher and Retraction Watch assertions as one event with two provenances, not two independent events.

An empty relationship field means only that this Crossref record contains no such relationship at retrieval time. It does not prove that no publisher notice exists.

## PubMed relationship reading

Check the publication types on the cited article and inspect linked comments/corrections. Relevant labels include:

- `Retracted Publication` on an affected article;
- `Retraction Notice` on the notice;
- `Published Erratum` for a correction notice;
- `Expression of Concern` for a formal concern;
- `Corrected and Republished Article` for a replacement record.

Follow the linked PMID in both directions where available. A notice PMID is not the affected article PMID. Preserve partial-retraction, retracted-and-republished, and update relationships when the detailed record exposes them.

## Chronology and precedence

Build an event timeline before assigning a primary status. Use this order of reasoning, not a blind severity sort:

1. Confirm identity and the affected scope.
2. Order formal events by effective date.
3. Determine whether a later event supersedes an earlier one, such as a reinstatement or corrected republication.
4. Retain superseded events for provenance.
5. If chronology or scope conflicts, assign `Conflicting status` and request the exact notice or publisher clarification.

## Minimum evidence for a bounded clean result

Use `No status update found` only when:

- identity is resolved to a stable identifier;
- the named live checks completed without a material error;
- at least the publisher/Crossmark path and one appropriate structured index were checked when both are available;
- the retrieval timestamp and coverage limits are recorded.

If one required channel fails, report the completed observations and use `Cannot decide` for high-consequence reliance. Never convert a timeout, paywall, missing identifier, blocked page, skipped endpoint, or stale local export into a clean status.

## Claim-impact questions

For each changed work, ask:

1. Is the citation used as positive evidence, historical context, or an example of a retraction?
2. Which exact finding, table, figure, subgroup, or conclusion supports the claim?
3. Does the notice affect that component or the entire work?
4. Is there an authoritative corrected or republished version?
5. Does the claim retain independent support if this citation is blocked?
6. Who must accept residual risk for high-stakes use?

Status checking ends with a scoped action. It does not replace reading the notice, checking claim entailment, or appraising the study.
