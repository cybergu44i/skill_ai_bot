# Design-Specific Causal Evidence Guide

Use this guide to select assumptions and diagnostics for the inspected design. It is an audit router, not a method-selection manual and not a substitute for domain expertise.

## Randomized assignment

Inspect:

- allocation unit, sequence generation, concealment where relevant, and actual exposure to assignment;
- baseline balance as a diagnostic, not as proof that randomization occurred;
- deviations, noncompliance, crossover, contamination, attrition, and missing outcomes;
- whether analysis follows the assignment policy claimed by the estimand;
- outcome timing, prespecification, multiplicity, and uncertainty;
- interference or cluster structure when one unit can affect another.

Randomization supports exchangeability for assignment under the implemented design. It does not automatically identify full-adherence effects, effects in excluded populations, long-term effects, or effects under substantial missingness.

## Before-and-after comparison

Inspect:

- the pre-period level and trend, intervention timing, follow-up window, and measurement stability;
- seasonality, regression to the mean, maturation, concurrent changes, anticipation, and unrelated shocks;
- whether repeated pre-periods or a comparison series exist;
- whether only one aggregate before/after pair carries the claim.

A temporal change after an intervention is normally `Association only` without a design feature that separates the intervention from time and concurrent causes.

## Difference-in-differences or event study

Inspect:

- treatment timing, comparison-group construction, and the exact estimand;
- pre-intervention trends and event-time diagnostics;
- anticipation, spillovers, concurrent group-specific shocks, compositional change, and treatment heterogeneity;
- whether staggered adoption and weighting match the estimator's assumptions;
- clustering, inference, and robustness to plausible specifications.

Similar-looking pre-trends support but do not prove the counterfactual parallel-trends assumption. State it as a condition unless design evidence makes the remaining risk immaterial for the intended use.

## Regression adjustment, matching, or weighting

Inspect:

- the causal model or rationale for the adjustment set;
- whether adjustment avoids mediators and colliders;
- measurement and timing of confounders;
- overlap or extreme weights;
- balance after adjustment, missingness, functional-form dependence, and sensitivity to unmeasured confounding;
- whether treatment and outcome definitions match the target contrast.

A rich covariate list or high predictive performance does not establish exchangeability. If the no-unmeasured-confounding argument is absent, keep the causal support conditional or classify the packet as association only, depending on materiality.

## Instrumental variables

Inspect:

- relevance of the instrument to treatment;
- the exclusion restriction and plausible direct paths to the outcome;
- independence from common causes of instrument and outcome;
- monotonicity or the assumptions required by the stated estimand;
- instrument strength, weak-instrument diagnostics, and the population to which the local effect applies.

Do not generalize a local effect for compliers to every person or treatment policy.

## Regression discontinuity

Inspect:

- assignment rule, threshold, running variable, and bandwidth;
- manipulation or sorting around the cutoff;
- continuity of potential outcomes and covariates;
- functional-form and bandwidth sensitivity;
- concurrent rules at the same threshold;
- the local population and distance over which the claim is generalized.

A discontinuity can support a local causal effect without supporting a population-wide claim.

## Interrupted time series or synthetic control

Inspect:

- enough pre-intervention observations to characterize level, trend, and seasonality;
- intervention timing and any concurrent shocks or measurement changes;
- autocorrelation and uncertainty;
- donor-pool construction, pre-treatment fit, placebo checks, and sensitivity where a synthetic control is used;
- anticipation, delayed effects, and choice of post-period.

Good pre-period fit is necessary evidence for the comparison but is not proof that no concurrent event explains the post-period divergence.

## Natural experiment

Inspect the exact assignment mechanism rather than accepting the label. Identify why exposure variation is plausibly independent of potential outcomes, what population the mechanism covers, how manipulation or selective exposure is ruled out, and what exclusions or spillovers remain.

## Mediation and mechanism claims

Distinguish:

- evidence that the intervention affects the outcome;
- evidence that it affects the proposed mediator;
- evidence that the mediator itself carries the effect under additional assumptions.

Temporal ordering and attenuation after adding a mediator do not by themselves establish mediation. Require the assumptions and estimand appropriate to the mediation analysis.

## Safe downgrades

When the evidence does not warrant the causal wording:

- replace intervention verbs with observed-comparison language;
- retain the population, comparator, outcome, period, effect measure, and uncertainty;
- name the design rather than implying a stronger one;
- state the blocking alternative explanation or missing identification assumption;
- avoid phrases such as “proved no effect” for an inconclusive or imprecise estimate.

Example:

> In the observed stores, conversion was 12% higher in the four weeks after the launch than in the prior four weeks; this before-and-after comparison does not isolate the launch from seasonality or concurrent changes.
