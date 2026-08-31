# Compute Qualification Infrastructure

Research, validation, and engineering workspace for evaluating the opportunity to build a neutral, evidence-driven infrastructure layer for cross-vendor AI compute qualification.

## Decision Objective

This repository exists to answer one question:

> Is there a painful, valuable, defensible, and technically feasible problem around workload-specific AI compute qualification that justifies a product/business?

The decision is explicitly one of:

- **GO** — proceed to a bounded paid-pilot/productization stage.
- **PIVOT** — preserve validated evidence but change the buyer, wedge, workflow, or product form.
- **KILL** — stop the opportunity because the problem, gap, economics, buyer, or defensibility does not survive evidence-based review.

We do **not** treat the current hypothesis as established fact.

## Current Working Hypothesis

> A neutral system can turn workload requirements into reproducible cross-vendor compute qualification decisions by combining workload contracts, execution, environment fingerprinting, performance/quality/energy measurements, evidence provenance, reproducibility checks, and deterministic policy gates.

Working name: **Compute Qualification Infrastructure**.

## Non-Goals Before Validation

We will not prematurely build:

- a generic AI compiler;
- a generic accelerator runtime;
- a new public benchmark competing with MLPerf/InferenceX/AA-AgentPerf;
- a generic profiler/dashboard;
- a vendor-specific accelerator stack;
- a large SaaS platform.

## Evidence Discipline

Every material claim must be classified using:

`ESTABLISHED` · `EXPERIMENTALLY_SUPPORTED` · `MARKET_SIGNAL` · `INFERENCE` · `HYPOTHESIS` · `UNKNOWN` · `CONTRADICTED` · `OPEN`

Evidence strength is tracked separately from claim status:

`L0` claim/marketing → `L1` official documentation → `L2` reproducible public artifact → `L3` independent technical evidence → `L4` customer/production evidence → `L5` commercial transaction / willingness-to-pay evidence.

Absence of evidence is recorded as **UNKNOWN**, never converted into a positive assumption.

## Decision Gates

### Gate 1 — Problem

Is the workflow painful, frequent, and economically meaningful?

### Gate 2 — Gap

Do existing vendor tools, benchmarks, MLOps platforms, consultants, and internal workflows fail to solve the problem adequately?

### Gate 3 — Buyer

Is there a clear user, economic buyer, trigger, and budget owner?

### Gate 4 — Economic Value

Can the product create measurable value through cost reduction, engineering time saved, risk avoided, faster deployment, higher utilization, or better infrastructure decisions?

### Gate 5 — Technical Feasibility

Can a small, vendor-neutral qualification kernel demonstrate the workflow without requiring custom silicon?

### Gate 6 — Defensibility

Can durable advantages arise from qualification history, workload corpus, evidence graph, integrations, workflow ownership, or trust rather than code alone?

### Gate 7 — Willingness to Pay

Can we obtain credible evidence that a buyer would pay for the capability, ideally through a paid pilot or equivalent commercial commitment?

## Decision Scoring

The default weighted score is:

| Dimension | Weight |
|---|---:|
| Problem severity | 20% |
| Unmet gap | 15% |
| Buyer clarity | 15% |
| Economic value | 15% |
| Technical feasibility | 15% |
| Defensibility | 10% |
| Willingness to pay | 10% |
| **Total** | **100%** |

Hard gates:

- Problem < 3/5 → NO-GO
- Gap < 3/5 → NO-GO
- Buyer clarity < 3/5 → NO-GO

Decision thresholds:

- `GO` ≥ 75/100 **and** no hard-gate failure
- `PIVOT` 50–74/100
- `KILL` < 50/100

A high score does not override missing commercial evidence.

## Research Phases

1. **Decision Charter** — fixed criteria and anti-bias rules.
2. **Commercial Evidence** — buyer/workflow/use-case matrix.
3. **Competitive Workflow Teardown** — inspect incumbent workflows, not just feature lists.
4. **Technical Qualification Probe** — build the smallest evidence-producing runner.
5. **Economic Validation** — quantify customer value and pilot economics.
6. **Red Team** — try to falsify the opportunity.
7. **GO / PIVOT / KILL** — final decision record.

## Repository Structure

```text
.
├── README.md
├── docs/
│   ├── decision-charter.md
│   ├── research-plan.md
│   └── commercial-evidence-matrix.md
├── research/
│   ├── sources/
│   ├── competitor-teardowns/
│   └── evidence-ledger/
├── qualification-kernel/
│   ├── spec/
│   ├── runner/
│   ├── evidence/
│   └── tests/
├── experiments/
│   ├── workloads/
│   ├── backends/
│   └── results/
└── decisions/
    ├── hypotheses/
    ├── gates/
    └── final/
```

## Relationship to Earlier Work

Relevant reusable engineering patterns exist in the author's prior repositories, especially evidence-first validation, deterministic policy decisions, reproducibility, and adapter/core separation. Those repositories are references and sources of reusable patterns; this repository remains an independent opportunity-validation workspace until the business case is proven.

## Current State

**Phase:** 1 — Commercial Evidence

**Decision:** OPEN

**Current leading hypothesis:** Workload-specific, cross-vendor AI compute qualification with reproducible evidence and continuous requalification.

**Validated:** specialized AI compute is becoming heterogeneous and procurement/production decisions increasingly require workload-specific performance, power, quality, and TCO evidence.

**Not yet validated:** an independent buyer will pay for this exact product category.

## Operating Rule

> Do not build what we can build. Build only what the evidence says someone needs, can value, and may pay for; then build the smallest artifact capable of proving it.
