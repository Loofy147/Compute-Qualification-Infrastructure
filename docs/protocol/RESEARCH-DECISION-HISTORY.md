# Research & Decision History

## Purpose

This document is the durable memory of how this investigation evolved. The conversation is treated as a temporary working surface; repository records are the long-lived source for assumptions, evidence, corrections, decisions, and rejected ideas.

## Epistemic rule

Every material statement should be identifiable as one of:

- `OBSERVED` — directly inspected or sourced.
- `DERIVED` — mechanically derived from observed facts.
- `INFERRED` — reasoned interpretation that may be wrong.
- `USER_REPORTED` — supplied by the project owner.
- `HYPOTHESIS` — explicitly proposed and not established.
- `CONTRADICTED` — materially challenged by evidence.
- `UNKNOWN` — insufficient evidence.

A later decision must not silently erase an earlier assumption. Corrections are research assets.

## Decision genealogy

### D0 — Initial opportunity

**Question:** Could an independent software business be built around AI compute qualification?

**Initial framing:** workload-specific, cross-vendor compute qualification using workload contracts, execution, environment capture, measurements, evidence, reproducibility, and deterministic policy.

**Status:** `HYPOTHESIS`

### D1 — Competitive teardown

We examined MLPerf, InferenceX, NVIDIA, AWS Neuron, Tenstorrent and related ecosystems at workflow level rather than by marketing feature list.

**Correction:** generic benchmarking, profiler functionality, vendor enablement, compatibility tooling, and significant portions of production qualification were already well served.

**Research asset:** the distinction among `SUPPORTED`, `BENCHMARKED`, `QUALIFIED`, and `PRODUCTION-APPROVED`.

### D2 — First narrowing

**Residual hypothesis:** customer-owned, cross-vendor qualification state plus lifecycle/requalification.

**Status:** `OPEN / UNPROVEN`

### D3 — Kill Test: internal build alternative

We tested whether enterprise teams could assemble the workflow from internal CI, telemetry, benchmarks, Kubernetes, MLOps, and vendor tooling.

**Result:** credible internal-build alternative exists.

Additional evidence showed large infrastructure operators explicitly maintaining technical compute qualification roles and acceptance workflows.

**Decision:** generic qualification SaaS is not sufficiently differentiated.

### D4 — Final kill of Compute Qualification opportunity

**Decision:** `KILL` on 2026-08-31.

**Important nuance:** the industry problem was not disproven. The independent venture wedge was not sufficiently underserved, defensible, or commercially validated.

See:

- `decisions/final/2026-08-31-KILL.md`
- `decisions/gates/2026-08-31-kill-test-production-qualification.md`
- `decisions/gates/2026-08-31-kill-test-internal-build-alternative.md`

### D5 — VEDP as a possible internal tool

We proposed the Venture Evidence & Decision Protocol as a reusable internal decision engine rather than a commercial product.

**Counterevidence:** generic startup validation and portfolio/innovation-management software already exist; graph/RAG/repository intelligence are also crowded categories.

**Status:** `RESEARCH TOOL / NOT A VENTURE`

### D6 — Portfolio Intelligence for our institution

We considered using a decision/graph engine internally across a large repository portfolio to connect projects, assets, capabilities, research, features, and relationships.

**Critical assumption:** the internal tool should create measurable value beyond existing repository/catalog/CI/project-management tools and beyond human analysis.

**Status:** `OPEN / UNPROVEN`

### D7 — Portfolio-grounded adversarial test

The repository inventory was introduced as a real testbed rather than a conceptual example.

The inventory currently reports 313 observed repository records in a 2026-08-30 search snapshot. It explicitly warns that this is not a proof of complete historical coverage.

The inventory also demonstrates identity ambiguity, probable duplicates, upstream mirrors, generated surfaces, research artifacts, and possible lineage across repositories. These are signals worth testing, not proof that a new intelligence system is required.

## Current hypothesis

> A portfolio-grounded internal intelligence workflow may be useful if it can reliably discover actionable relationships, capability reuse, duplication/lineage, composition opportunities, or prioritization insights that materially improve decisions or reduce work compared with the current tool stack and human baseline.

This remains a `HYPOTHESIS`.

## Required falsification

Before productizing anything, attempt to disprove the hypothesis through:

1. Existing-stack substitution: determine what GitHub/GitLab, Backstage, issue/project tools, CI/CD, document stores, search, and OSS graph/RAG systems already provide.
2. Human baseline: measure what a competent reviewer can discover from the existing inventory without a new engine.
3. Value test: require discovered relationships to change a real action (merge, extract, archive, reuse, prioritize, or kill).
4. Precision test: false-positive relationships must not overwhelm useful discoveries.
5. Time test: compare human-only analysis with assisted analysis.
6. TCO test: compare build + integration + maintenance against the value created.
7. Authority test: AI suggestions must remain non-authoritative until independently verified.

## Current non-goals

Until the hypothesis survives the above tests, do not build:

- a generic enterprise portfolio-management platform;
- a generic repository graph/RAG product;
- a general AI startup validator;
- a dashboard-first product;
- a SaaS version for external customers;
- a large autonomous agent platform.

## Provenance principle

The conversation can contain useful reasoning, but the repository is the durable record. When reasoning changes, preserve the old assumption and append the correction rather than rewriting history as though the corrected view had always been known.

## Source anchors

Primary portfolio context:

- `Loofy147/Portfolio-Repository-Inventory`
- `README.md`
- `reports/portfolio-overview.md`
- `inventory/triage.json`
- `catalog/reassessment-2026-08-30.md`
- `catalog/repository-cards-001.md` through later batches

Relevant internal research assets include:

- `Loofy147/canonical-capability-core`
- `Loofy147/Software-res`
- `Loofy147/algeria-ai-product-fabric`
- `Loofy147/Compute-Qualification-Infrastructure`

These sources provide context and implementation evidence, but each claim must retain its own epistemic status.
