# W2 — Qualification Model and Decision Boundary

Research snapshot: 2026-08-31

## Core distinction

The investigation must keep four states separate:

```text
SUPPORTED
  = vendor/documentation says configuration is supported.

BENCHMARKED
  = a defined workload/test produced measured evidence.

QUALIFIED
  = the measured evidence satisfies a customer's explicit acceptance policy.

PRODUCTION-APPROVED
  = qualified evidence has passed the organization's release/approval control.
```

These are not interchangeable. A supported model can fail a benchmark. A benchmarked model can fail a customer SLO. A qualified configuration can later become unqualified when a material dependency changes.

## Proposed qualification object

```yaml
qualification:
  subject:
    workload: <workload-id>
    model: <model-id>
    configuration: <configuration-id>

  requirements:
    quality: <policy>
    latency: <policy>
    throughput: <policy>
    energy: <policy>
    reliability: <policy>

  evidence:
    execution_refs: []
    measurements: []
    provenance_refs: []
    reproduction_refs: []

  decision:
    state: QUALIFIED | REVIEW | REJECTED
    policy_version: <id>
    evaluated_at: <timestamp>
```

## Qualification state transitions

```text
UNASSESSED
    ↓
EVIDENCE_PENDING
    ↓
EVIDENCE_AVAILABLE
    ↓
POLICY_EVALUATED
    ├── QUALIFIED
    ├── REVIEW
    └── REJECTED

QUALIFIED
    ↓ material change
REQUALIFICATION_REQUIRED
    ↓
EVIDENCE_PENDING
```

A material change can include model, weights, compiler, runtime, driver, firmware, hardware SKU, topology, serving configuration, precision, or workload definition. The exact change policy is customer-defined.

## Why customer ownership matters

Vendor ecosystems already decide questions such as:

- Is this model supported?
- Is this deployment profile validated?
- Does this model port correctly?
- Does the target stack meet vendor validation criteria?

The candidate layer instead asks:

> Does this exact configuration meet **our** requirements, and can we prove that decision independent of the vendor that produced the stack?

## Requalification contract

The system should not rerun every test after every change. It should maintain a dependency graph and classify changes:

```text
NO_IMPACT
  → qualification remains valid

POTENTIAL_IMPACT
  → targeted requalification

MATERIAL_IMPACT
  → full qualification required
```

This dependency-aware behavior is a key technical hypothesis because it can make continuous qualification materially cheaper than full benchmark reruns.

## Evidence inputs

The qualification layer should be measurement-agnostic. It may consume:

- MLPerf results;
- InferenceX runs/artifacts;
- vendor validation results;
- AIPerf/GenAI-Perf results;
- custom enterprise tests;
- power telemetry;
- numerical-equivalence/evaluation results;
- local controlled execution.

The qualification system owns normalization, provenance references, requirement evaluation, and state transitions rather than recreating every measurement tool.

## Falsification target

This model is falsified if an existing system already provides customer-owned requirements, cross-vendor execution/evidence composition, deterministic acceptance policy, production release gating, and durable historical qualification state for arbitrary workloads.

Finding each component separately is not sufficient; the complete workflow must exist in one credible reusable system or be shown to be trivial for the target customer to assemble and maintain.

## Technical acceptance test

A minimum proof should demonstrate all of the following:

1. Configuration A is supported but fails customer policy → `REJECTED`.
2. Configuration B is benchmarked and meets performance but fails energy → `REVIEW` or `REJECTED` according to policy.
3. Configuration C satisfies all required predicates → `QUALIFIED`.
4. Changing a declared material dependency marks C as `REQUALIFICATION_REQUIRED`.
5. Re-running the qualification with the new evidence yields a deterministic new state.
6. The previous qualification state remains immutable and historically queryable.

This test is intentionally small; it validates the decision semantics before any large benchmark infrastructure is built.
