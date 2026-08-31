# Portfolio-Grounded Assumption Audit

Date: 2026-09-01
Status: OPEN / adversarial validation

## Purpose

The `Portfolio-Repository-Inventory` repository is now the primary map for testing whether an internal portfolio-intelligence system is actually needed for our institution.

This document deliberately does **not** promote the idea to a product or company. It tests the narrower internal-use hypothesis using the real repository portfolio.

## Source snapshot

The inventory reports 313 deduplicated repository records from a GitHub search snapshot dated 2026-08-30. The inventory explicitly warns that this is an accessible search census, not proof of a complete historical portfolio.

Source: https://github.com/Loofy147/Portfolio-Repository-Inventory

## Current observed portfolio signals

The inventory shows a heterogeneous portfolio containing:

- product/application candidates such as `Bravolino`, `A-louer`, `CloudCostGuard`, `Marchants`, `NeuraSynth`, and `Meta-meta`;
- foundational/research systems such as `canonical-capability-core`, `Software-res`, `HAG`, `RE-UP`, `Orvio`, `Algorithms-`, and `self-growing-machine`;
- agent/orchestration systems such as `ai-meta-orchestrator`, `Unified-ai`, `ACE-Agentic-Context-Engineering`, `Gemini-app`, and related repositories;
- multiple possible lineage/duplicate families, including `Software-res` ↔ `Ai-evaluation-system`, `canonical-capability-core` ↔ `algeria-ai-product-fabric`, `algeria-multi-agent-platform` ↔ `algeria-multiagent-platform`, and `Doha-platform` ↔ `Doha-platform-`;
- upstream/derived repositories such as `gemini-cli`, `LightRAG`, and other externally-originated surfaces that must not automatically be counted as original institutional assets.

These are observed inventory signals, not final strategic classifications.

## Initial evidence that the problem exists internally

The inventory already documents repeated situations where repository identity, project identity, lineage, implementation surface, and strategic meaning diverge. Examples include:

1. Similar or near-identical repositories that require history/content comparison before deciding whether they are duplicates or successors.
2. Repositories whose README identity differs materially from package/source identity.
3. Repositories that are wrappers, upstream copies, or generated surfaces rather than independent original projects.
4. Foundational capabilities appearing in more than one repository family.
5. Research artifacts and production-oriented applications coexisting in the same portfolio.

The inventory therefore provides genuine material for a portfolio-reconciliation problem. It does **not** yet prove that a new internal system is necessary.

## Assumptions to attack

### A1 — Humans cannot efficiently maintain portfolio relationships

Falsify by showing that the existing inventory plus disciplined manual review can maintain accurate relationships at acceptable effort.

Status: OPEN.

### A2 — Existing tools are insufficient

Candidate substitutes include Backstage, GitHub/GitLab metadata and search, project-management systems, documentation, dependency scanners, code search, and manually maintained inventory files.

Backstage already provides a software catalog with ownership, inventory, lifecycle, dependency mapping, API relationships, and extensible entity types. Therefore a generic software catalog is not a gap.

Status: CHALLENGED.

### A3 — Semantic relationship discovery adds enough value

The relevant test is not whether an LLM can suggest relationships. The test is whether it finds materially useful relationships that humans plus ordinary repository tooling would miss or would find substantially more slowly.

Status: UNPROVEN.

### A4 — A capability graph reduces duplicated work

The test must measure actual duplicate/similar capability discovery across the portfolio, including false positives.

Status: UNPROVEN.

### A5 — Cross-project composition discovery creates better decisions

A candidate composition is valuable only if human review confirms that combining existing assets changes a real engineering or portfolio decision.

Status: UNPROVEN.

### A6 — Repository-level intelligence is enough

This may be false. The real unit may be the project, capability, asset, research result, or business hypothesis rather than the repository. Repository != project != capability must remain explicit.

Status: OPEN.

### A7 — AI graph extraction should be authoritative

This is explicitly rejected as a default. AI-generated relationships must remain hypotheses until supported by source/history/evidence or human confirmation.

Status: CONTRADICTED as a design principle.

### A8 — More centralization is always better

A centralized graph could introduce false coupling, stale metadata, maintenance cost, and a new system-of-record conflict. Any internal system must preserve repository-local authority and provenance.

Status: OPEN / HIGH RISK.

### A9 — Building internally is cheaper than composing existing OSS

This cannot be assumed. The build-vs-compose decision must include integration, maintenance, upgrade, security, operating, and opportunity costs.

Status: UNPROVEN.

### A10 — Portfolio scale itself justifies a new platform

313 observed repositories is evidence of scale, not proof of pain. A smaller sample could be manageable manually.

Status: UNPROVEN.

## Existing external baseline

A serious internal implementation must start by treating these as competitors/substitutes rather than rebuilding them:

- Backstage Software Catalog: ownership, inventory, lifecycle, dependency mapping, search, extensible entity model.
- GitHub/GitLab: repository metadata, code search, dependency metadata, history, issues and CI.
- Code intelligence / graph tools: repository semantic and dependency analysis.
- Project-management systems: project dependencies, roadmaps, priorities, ownership.
- General knowledge/document systems: decision records and research documentation.

Backstage explicitly supports catalog entities for components, resources, systems and domains and supports relations such as `dependsOn`, `ownedBy`, `partOf`, `providesApi`, and `consumesApi`. It also recommends human governance for automatically generated metadata.

Reference: https://backstage.io/docs/features/software-catalog/
Reference: https://backstage.io/docs/features/software-catalog/creating-the-catalog-graph/

## Required experiment before any productization

We should not build a platform first. We should run a controlled portfolio experiment:

```text
Real repository sample
        ↓
Current inventory + ordinary tools
        ↓
Human baseline
        ↓
Candidate extraction/relationship engine
        ↓
Blind review
        ↓
Precision / recall / utility measurement
```

### Minimum sample

Select 30–50 repositories with known heterogeneity and suspected relationships, including:

- clear duplicates/variants;
- known shared foundational capabilities;
- known upstream/forked repositories;
- distinct projects that should **not** be merged;
- research artifacts;
- application repositories;
- at least several `UNKNOWN` repositories.

The inventory already supplies strong candidates for this sample.

## Metrics

### Relationship discovery

- true relationships discovered;
- false-positive relationships;
- missed known relationships;
- precision;
- recall;
- reviewer agreement.

### Portfolio utility

- duplicate work identified;
- reusable capability candidates identified;
- obsolete/superseded assets identified;
- meaningful composition opportunities identified;
- decisions changed after review;
- human time saved.

### Maintenance burden

- extraction cost;
- review cost;
- metadata correction rate;
- stale relationship rate;
- false-confidence incidents.

## Kill conditions

Kill the internal-system hypothesis if any of the following is demonstrated:

1. Existing catalog/search/documentation tools achieve comparable useful coverage with materially lower maintenance effort.
2. AI relationship discovery has high false-positive rates and does not materially improve human decisions.
3. Discovered relationships rarely change engineering or portfolio decisions.
4. The resulting graph is too volatile to remain trustworthy.
5. Build + maintenance TCO is worse than disciplined manual/OSS composition without offsetting value.

## Surviving hypothesis

The only hypothesis worth carrying forward is:

> A portfolio-specific, evidence-grounded relationship layer may reduce real duplicated engineering effort and improve asset/capability decisions enough to justify internal ownership.

This remains `OPEN`, not validated.

## Important boundary

This experiment is **not** a decision to create a SaaS product, commercialize the system, or replace Backstage/GitHub/project-management tooling.

The only immediate question is whether such a system produces enough incremental internal value for our own portfolio to justify its engineering and maintenance cost.

## Evidence sources

Primary internal source:
- https://github.com/Loofy147/Portfolio-Repository-Inventory

Key inventory records inspected for this audit:
- `README.md`
- `reports/portfolio-overview.md`
- `inventory/repositories.json`
- `inventory/triage.json`
- `catalog/reassessment-2026-08-30.md`
- `catalog/repository-cards-001.md`
- `catalog/repository-cards-002.md`
- `catalog/repository-cards-003.md`
- `catalog/repository-cards-004.md`
- `catalog/repository-cards-019.md`
- `catalog/repository-cards-042.md`

The inventory currently records only a partial structural inspection of many repositories. Lack of evidence remains `UNKNOWN` rather than evidence of absence.
