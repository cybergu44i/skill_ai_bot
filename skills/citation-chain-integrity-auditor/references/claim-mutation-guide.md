# Claim Mutation Guide

Use this guide only after the target claim and both sides of a citation hop have been located. A textual difference is not automatically a material mutation; explain how it changes what a reader may conclude.

## Compare the claim vector

Check these dimensions independently:

| Dimension | Typical mutation | Example pattern |
|---|---|---|
| Entity or population | population widening or substitution | mice becomes humans; one sector becomes the whole economy |
| Relation and direction | reversal or changed mechanism | A predicts B becomes B predicts A; association through M becomes direct effect |
| Quantity | precision or magnitude inflation | a range becomes a point estimate; `up to 40%` becomes `40%` |
| Unit or denominator | construct or base-rate shift | calories becomes all food; withdrawals becomes consumption |
| Time or version | temporal transfer | a historical estimate becomes a current fact without a new measurement |
| Geography or setting | scope expansion | one country becomes global; laboratory conditions become routine practice |
| Comparator | baseline substitution | comparison with placebo becomes comparison with standard care |
| Strength | certainty or causal escalation | may becomes does; association becomes cause; hypothesis becomes demonstrated fact |
| Attribution | authority laundering | a review's interpretation is attributed to the primary study or institution |
| Qualification | caveat loss | exclusions, uncertainty, adverse results, or conditions disappear |

## Label the change

- `Preserved` — wording differs but the bounded proposition is materially the same.
- `Narrowed` — the citing source makes a more limited claim that the cited evidence still supports.
- `Qualified upstream` — the cited source contains a material condition or uncertainty missing downstream.
- `Mutated` — the change alters the proposition or evidentiary strength.
- `Not comparable` — the passages concern different propositions.
- `Unresolved` — text or context is insufficient.

Record the exact words, values, or definitions responsible for the label. Do not rely on semantic similarity alone for numbers, negation, causal direction, named entities, or technical constructs.

## Handle common chain patterns

### Secondary synthesis

A review, guideline, or analysis may legitimately originate a synthesis even though it cites primary inputs. Record it as `Synthesis` when the downstream claim is the synthesis itself and the method or reasoning is inspectable. Do not replace it automatically with one input study.

### Citation bundle

When several references follow one claim, determine what each reference contributes. Do not assume every item supports the full sentence or that the bundle supplies independent corroboration.

### Missing original

If the upstream artifact cannot be inspected, retain the downstream source as a secondary citation and use `Unresolved`. Recommend an explicit `as cited in` disclosure when the relevant style and context permit; never imply that the original was read.

### Multiple paths

Audit the path actually offered as support first. If another path reaches genuine support, report it separately as a possible repair rather than using it to retroactively make a broken citation faithful.

### Cycles

List the repeated node and close the path as `Circular chain`. A cycle can coexist with external support, but the cycle itself contributes no evidence.
