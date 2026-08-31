# Experiment 001 — Portfolio-Grounded Relationship Discovery

Date: 2026-09-01
Status: DESIGNED / NOT YET EXECUTED

## Objective

Test whether a lightweight, evidence-grounded relationship analysis layer provides materially useful information beyond the existing `Portfolio-Repository-Inventory` plus ordinary human review and existing repository tooling.

## Hypothesis

> On a representative sample of the portfolio, automated semantic/structural relationship suggestions can discover useful duplicate, lineage, dependency, capability, or composition relationships with sufficient precision and reviewer utility to justify maintaining an internal tool.

This is an internal-tool hypothesis only. It is not a commercial product hypothesis.

## Null hypothesis

> The current inventory, repository tooling, and disciplined manual review are already good enough; an additional relationship layer does not materially improve decisions relative to its engineering and maintenance cost.

## Sample design

Use 30–50 repositories selected from the inventory to maximize heterogeneity rather than convenience.

Required strata:

1. Known duplicate/successor candidates.
2. Known lineage candidates.
3. Shared foundational-capability candidates.
4. Clearly unrelated projects from the same domain.
5. Research artifacts.
6. Product/application repositories.
7. Upstream/derived repositories.
8. Metadata-only or currently unknown repositories.

Initial high-value candidates include:

- `canonical-capability-core`
- `Software-res`
- `algeria-ai-product-fabric`
- `ai-meta-orchestrator`
- `Unified-ai`
- `ACE-Agentic-Context-Engineering`
- `algeria-multi-agent-platform`
- `algeria-multiagent-platform`
- `Doha-platform`
- `Doha-platform-`
- `HAG`
- `Global-theorem-` / related mathematical lineage candidates
- `Healer-`
- `-Fiber-Stratified-Optimization---FSO-`
- `RE-UP`
- `Orvio`
- `Algorithms-`
- `gemini-cli`
- `Gemini-app`
- `LightRAG`
- `Drogon`
- `-AI-Driven-Crypto-Portfolio-Manager-`
- `Meta-meta`
- `Bravolino`
- `A-louer`
- `CloudCostGuard`
- `Marchants`
- `NeuraSynth`
- `training-home`

The final sample must include explicit negative pairs: repositories known to be distinct despite superficial similarity.

## Baselines

### Baseline A — Inventory only

Use the current cards, metadata, known relationship candidates, and evidence vocabulary from `Portfolio-Repository-Inventory`.

### Baseline B — Human structural review

Inspect the relevant repository surfaces using the inventory's protocol:

`METADATA -> ROOT TREE -> BUILD/MANIFEST -> SOURCE -> TESTS/CI -> DATA/ARTIFACTS -> README/DOCS -> HISTORY`

Record discovered relationships without using the candidate engine.

### Candidate system

Only after Baselines A and B are frozen, run automated relationship extraction over the same sample.

## Relationship classes

At minimum:

- `same_project`
- `same_idea`
- `successor`
- `predecessor`
- `fork`
- `duplicate_candidate`
- `dependency`
- `component_source`
- `research_source`
- `shared_capability`
- `feature_overlap`
- `composition_candidate`
- `upstream_derived`
- `unrelated`

The last class is mandatory. A useful system must be able to say that a tempting relationship should not be asserted.

## Evidence requirements

Every proposed relationship must identify why it exists, for example:

- repository/history evidence;
- dependency/import evidence;
- package/build identity;
- shared artifact hash or similarity signal;
- documentation reference;
- common external upstream;
- architectural/schema overlap;
- repeated capability surface;
- explicit repository cross-link.

A semantic similarity score without supporting evidence is not sufficient for promotion.

## Blind review

To reduce confirmation bias:

1. Freeze baseline human findings.
2. Hide relationship labels from the reviewer.
3. Present candidate relationships with evidence excerpts.
4. Have at least two independent reviews where feasible.
5. Measure agreement and adjudicate disagreements.

## Metrics

### Discovery quality

- precision per relationship class;
- recall against the frozen baseline;
- false-positive rate;
- false-negative rate;
- reviewer agreement.

### Utility

- new true relationships discovered;
- duplicates newly identified;
- reusable capabilities newly identified;
- meaningful composition candidates newly identified;
- decisions changed because of a discovered relationship;
- human review time saved per repository.

### Trustworthiness

- unsupported relationship rate;
- stale relationship rate;
- provenance coverage;
- evidence completeness;
- false-confidence incidents.

## Success threshold for internal continuation

The candidate must demonstrate all of the following:

- high precision on high-risk relationship classes such as duplicate/lineage;
- material incremental recall over the inventory baseline;
- at least one class where human review is measurably faster or better with the tool;
- no unacceptable false-confidence behavior;
- engineering + maintenance burden plausibly below the recurring internal value created.

These are experiment thresholds, not industry benchmarks.

## Failure / Kill thresholds

Kill the internal-tool hypothesis if:

- automated suggestions are mostly redundant with inventory/human review;
- false positives make the graph unsafe or expensive to maintain;
- the tool discovers relationships that rarely affect decisions;
- provenance is too weak to trust suggestions;
- maintenance burden exceeds measured utility;
- a composed OSS stack gives comparable results with materially less effort.

## Expected outputs

- frozen sample manifest;
- human baseline relationship set;
- automated candidate relationship set;
- adjudicated labels;
- precision/recall report;
- utility report;
- maintenance-cost estimate;
- final internal-tool decision: `KEEP_INTERNAL`, `PIVOT_INTERNAL`, or `KILL`.

## Source

Primary portfolio map:
https://github.com/Loofy147/Portfolio-Repository-Inventory
