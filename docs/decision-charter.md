# Decision Charter

## Purpose

This document is the permanent reference for the opportunity decision. Research and implementation must remain subordinate to the decision objective.

## Decision

The project must end in exactly one of:

- **GO:** evidence is sufficient to justify a bounded paid-pilot/productization phase.
- **PIVOT:** part of the hypothesis is validated, but the current buyer, wedge, workflow, or product form is not the best path.
- **KILL:** the opportunity does not survive evidence-based review.

## Core Hypothesis

A neutral system can qualify AI compute configurations for specific workloads by linking requirements, model, software stack, hardware, execution, measurements, reproducibility, evidence provenance, and deterministic policy decisions.

## Hypotheses

### H1 — Problem
The target workflow creates material pain, cost, delay, or risk.

### H2 — Gap
Existing tools and workflows do not adequately solve the complete problem in a neutral, reusable, workload-specific manner.

### H3 — Buyer
A recognizable buyer owns the problem and has authority/budget to act.

### H4 — Economic Value
The solution produces measurable economic value.

### H5 — Technical Feasibility
A bounded software-only qualification kernel can demonstrate the essential workflow across multiple compute backends.

### H6 — Defensibility
The product can develop durable advantages beyond commodity benchmarking or wrappers around existing vendor APIs.

### H7 — Willingness to Pay
At least one credible buyer provides direct commercial evidence, ideally a paid pilot or equivalent commitment.

## Evidence Rules

1. A vendor claim is not independent proof of customer demand.
2. A competitor is not evidence of a market gap.
3. Technical feasibility is not evidence of business value.
4. Market size is not willingness to pay.
5. Missing evidence is recorded as `UNKNOWN`.
6. Contradictory evidence must remain visible.
7. Research conclusions must identify the strongest supporting and opposing evidence.
8. Scores cannot conceal hard-gate failures.

## Evidence Levels

| Level | Meaning |
|---|---|
| L0 | Claim, marketing statement, or secondary assertion |
| L1 | Official documentation or first-party technical material |
| L2 | Reproducible public artifact |
| L3 | Independent technical evidence |
| L4 | Customer or production evidence |
| L5 | Commercial transaction / direct willingness-to-pay evidence |

## Claim Status

`ESTABLISHED` · `EXPERIMENTALLY_SUPPORTED` · `MARKET_SIGNAL` · `INFERENCE` · `HYPOTHESIS` · `UNKNOWN` · `CONTRADICTED` · `OPEN`

## Scoring

| Criterion | Weight |
|---|---:|
| Problem severity | 20 |
| Unmet gap | 15 |
| Buyer clarity | 15 |
| Economic value | 15 |
| Technical feasibility | 15 |
| Defensibility | 10 |
| Willingness to pay | 10 |

### Hard Gates

- Problem severity < 3/5 → No-Go
- Unmet gap < 3/5 → No-Go
- Buyer clarity < 3/5 → No-Go

### Thresholds

- `GO`: ≥ 75/100 and no hard-gate failure
- `PIVOT`: 50–74/100
- `KILL`: < 50/100

## Required Final Evidence

Before GO:

- three or more well-characterized target workflows;
- documented incumbent alternatives;
- a working qualification probe;
- reproducibility demonstration;
- quantified value model;
- explicit competitive red-team findings;
- credible WTP evidence.

Before PIVOT:

- at least one meaningful part of the problem must remain validated;
- the proposed pivot must address a specific failed assumption.

Before KILL:

- the strongest available evidence must show that the problem, gap, buyer, economics, or defensibility is insufficient.

## Current Decision State

`OPEN`

This charter deliberately prevents premature productization. The repository may contain experiments, prototypes, and research artifacts, but they are evidence-gathering instruments until the decision gates are passed.
