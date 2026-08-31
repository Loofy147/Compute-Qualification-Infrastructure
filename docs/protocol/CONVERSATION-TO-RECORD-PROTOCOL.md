# Conversation-to-Record Protocol

## Why this exists

Working conversations are iterative and temporary. Assumptions, interpretations, hypotheses, and decisions can change as new evidence appears. Therefore important reasoning must be converted into durable repository records.

## Rule

A conversation statement is not authoritative merely because it was said confidently or repeated later.

The durable record must preserve:

`context → assumption → evidence → counterevidence → correction → decision → consequence`

## What must be recorded

Create or update a durable record when the conversation produces any of the following:

- a new material hypothesis;
- a new decision criterion or hard gate;
- a material assumption;
- evidence that changes an assumption;
- a falsification attempt or counterexample;
- a competitor/alternative that changes positioning;
- a project relationship or lineage claim;
- a decision to build, adapt, merge, freeze, archive, or kill;
- an important unresolved question;
- a change to protocol semantics.

## Provenance fields

Where practical, record:

- date/time or research snapshot;
- originating conversation context or task;
- source repository/document/URL;
- evidence level;
- epistemic status;
- affected assumption or claim;
- previous state;
- new state;
- decision impact.

## No hindsight rewriting

When a hypothesis is corrected, preserve the earlier state. Do not rewrite history to make the corrected conclusion appear to have been known from the beginning.

Example:

```text
HYPOTHESIS A
  ↓ evidence
CONTRADICTED
  ↓ correction
HYPOTHESIS B
```

Not:

```text
HYPOTHESIS B (pretending A never existed)
```

## Decision authority

Evidence records describe what was observed. Assessments describe what the evidence supports. Decisions record what action was chosen. These are separate layers.

`Evidence ≠ Assessment ≠ Decision`

## Portfolio implications

For multi-repository work, preserve distinctions among:

`repository ≠ project ≠ idea ≠ capability ≠ asset ≠ venture`

A repository may be archived while its capability is retained. A project may be killed while its research remains valuable. A feature may be extracted into shared infrastructure. A venture hypothesis may be killed while the underlying problem remains real.

## Minimum audit trail

Every significant research cycle should leave behind:

1. Current hypothesis.
2. Assumptions under attack.
3. Evidence and counterevidence.
4. What changed.
5. Current decision.
6. What remains unknown.
7. The next falsification test.

## Principle

> **Ephemeral conversation is a working surface; versioned artifacts are institutional memory.**

The goal is not to preserve every sentence. The goal is to preserve enough provenance that a future review can reconstruct why we believed something, why we changed our mind, and what evidence caused the change.
