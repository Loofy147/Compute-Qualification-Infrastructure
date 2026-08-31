# Research Plan

## Objective

Determine whether workload-specific, cross-vendor AI compute qualification is a sufficiently painful, underserved, valuable, feasible, and defensible opportunity.

## Phase 1 — Commercial Evidence

### Workstreams

1. Buyer/workflow discovery
2. Incumbent workflow mapping
3. Competitive capability teardown
4. Evidence quality assessment
5. Economic model
6. WTP validation

### Required research sources

Prefer, in order:

1. Primary vendor documentation and engineering publications
2. Public repositories and reproducible artifacts
3. Standards/benchmark organizations
4. Independent technical analyses
5. Customer/production reports
6. Financial/commercial evidence
7. Secondary reporting only as context or discovery

## Competitive Teardown Method

Each incumbent is mapped from workflow start to decision end, not by feature list.

Required dimensions:

- workload definition
- model/version capture
- environment fingerprinting
- execution orchestration
- hardware coverage
- software-stack coverage
- power measurement
- accuracy validation
- performance measurement
- TCO/economic analysis
- evidence/provenance
- reproducibility
- regression detection
- policy gating
- production acceptance
- historical results
- cross-vendor neutrality

## Technical Probe

The smallest acceptable prototype is:

```text
qualification spec
→ environment capture
→ controlled execution
→ measurements
→ evidence bundle
→ independent rerun
→ deterministic decision
```

The probe must not require custom silicon to prove its core architecture.

## Economic Validation

For each shortlisted workflow estimate:

`annual_value = engineering_time_saved + infra_cost_avoided + energy_savings + risk_avoided + deployment_acceleration + utilization_gain`

Then compare against plausible annual product cost.

All monetary figures must identify whether they are:

- observed;
- externally sourced;
- calculated from observed inputs;
- scenario assumptions.

## Red-Team Protocol

For each surviving wedge, actively search for:

- a product already solving the workflow;
- internal enterprise tooling that makes the product unnecessary;
- a vendor lock-in barrier;
- an insufficiently painful workflow;
- low frequency of occurrence;
- weak budget ownership;
- impossible or expensive instrumentation;
- inability to prove causality or ROI;
- legal/licensing limitations;
- a stronger adjacent market with better economics.

## Anti-Bias Rules

- Do not change decision thresholds after observing results.
- Record disconfirming evidence alongside supporting evidence.
- Do not cite funding as evidence of customer demand.
- Do not infer WTP from interest.
- Do not infer technical feasibility from a mockup.
- Do not infer neutrality from a vendor's marketing claim.
- Do not use a single benchmark to establish product value.

## Deliverables Before Final Decision

- commercial evidence matrix;
- competitor workflow teardowns;
- evidence ledger;
- technical qualification probe;
- ROI/economic model;
- red-team report;
- final decision record with explicit assumptions and unresolved unknowns.
