# Kill Test — Internal Build Alternative

Research date: 2026-08-31
Status: `FAILED_TO_KILL_BROAD_PROBLEM / KILLED_SOFTWARE_WEDGE`

## Purpose

Test whether a customer can reasonably implement the remaining hypothesis with existing engineering tools and internal processes, making an independent product unnecessary.

## Hypothesis under test

> A customer-owned, cross-vendor qualification state and continuous requalification layer is valuable enough to exist as independent software rather than as CI scripts, experiment tracking, vendor validation tooling, and internal program management.

## Internal-build stack examined

A credible customer can assemble:

```text
GitHub/GitLab CI
+ Argo Workflows / Kubernetes
+ MLflow or experiment tracking
+ Prometheus / telemetry
+ vendor benchmark + validation suites
+ vendor compatibility matrices
+ custom Python/SQL/scripts
+ internal approval/checklists
```

Argo already provides cloud-agnostic Kubernetes-native DAG/workflow orchestration suitable for compute-intensive and ML workflows. MLflow provides model packaging, evaluation, validation thresholds, deployment, and integrations with Kubernetes/cloud targets. GitLab provides performance regression testing and merge-request comparisons. Kubernetes Node Readiness Controller provides declarative readiness gates based on infrastructure health signals.

## Strongest kill evidence

### 1. The primitives are available

The core machinery needed to assemble qualification workflows is not scarce:

- CI systems can execute tests and block changes.
- Workflow engines can orchestrate multi-step jobs across clusters.
- Experiment/model systems can retain model versions and evaluation results.
- Observability systems can capture telemetry.
- Vendor suites already provide hardware health, benchmarks, acceptance criteria, and validation.

MLflow explicitly supports automated model evaluation and metric thresholds and provides deployment integrations. Argo provides Kubernetes-native workflow orchestration. GitLab provides performance regression testing. Kubernetes' Node Readiness Controller extends readiness gating based on custom health signals.

**Assessment:** Strong negative evidence against selling orchestration, metric thresholding, dashboards, or CI integration as the primary product.

### 2. Customers already build qualification processes internally

Together AI currently advertises a dedicated Technical Compute Qualification Manager role responsible for the end-to-end process of qualifying compute providers, maintaining standards/templates, coordinating infrastructure/network/storage/power evaluations, and keeping an auditable record of go/no-go outcomes. This is direct evidence that a sophisticated compute operator may choose people + internal tooling rather than buying a standalone qualification product.

AMD's current Instinct Customer Acceptance Guide provides detailed checklists, acceptance thresholds, automated Cluster Validation Suite workflows, and production-readiness criteria. This further demonstrates that operator-side qualification can be implemented as an internal process using available tooling.

**Assessment:** Strong negative evidence against generic production-qualification SaaS.

### 3. Independent evaluation can also be purchased as a service

Substrate Co sells workload benchmark setup, comparative benchmark studies, and an ongoing advisory retainer. TensorPi sells multi-hardware evaluation, benchmark reports, procurement recommendations, and deployment support. Therefore a buyer with occasional evaluation needs can outsource the problem rather than adopt software.

**Assessment:** Strong negative evidence against a simple software replacement for consulting.

## Does the internal build fully eliminate the remaining hypothesis?

Not proven.

Existing primitives make it plausible to build the system, but composition still requires customer-specific engineering and process ownership. The unresolved question is whether recurring cross-vendor qualification state becomes sufficiently costly when the customer has:

- many workload/model versions;
- multiple hardware vendors;
- multiple software stacks;
- frequent compiler/driver/firmware changes;
- contractual or operational acceptance requirements;
- auditability/reproducibility requirements;
- a need to know the blast radius of changes;
- repeated procurement and capacity decisions.

The public evidence reviewed does **not** establish that every organization faces this complexity, nor that a product is preferred to internal build.

## Structural comparison

| Function | Internal stack can do it? | Difficulty | Candidate independent value |
|---|---|---|---|
| Define tests | Yes | Low | Low |
| Run tests | Yes | Low/Medium | Low |
| Collect metrics | Yes | Low | Low |
| Store results | Yes | Low | Low |
| Threshold gates | Yes | Low | Low |
| Model evaluation | Yes | Low/Medium | Low |
| Vendor-specific qualification | Yes | Medium | Low |
| Cross-vendor execution | Yes, with engineering | Medium/High | Medium |
| Normalize evidence | Yes, with engineering | Medium | Medium |
| Maintain customer qualification state | Yes | Medium | Medium |
| Change-impact analysis | Partially | Medium/High | Potentially high |
| Automatic requalification selection | Partially | High | Potentially high |
| Historical qualification graph | Yes | Medium | Potentially high |
| Cross-vendor lifecycle continuity | Custom | High | Potentially high |
| Neutral decision policy | Yes | Low/Medium | Low alone |
| Production release gate | Yes | Low/Medium | Low alone |

## Key finding

The internal-build alternative does **not** kill the problem itself.

It does, however, kill the assumption that the product is valuable merely because it combines:

- CI,
- benchmark execution,
- evidence storage,
- thresholds,
- dashboards,
- release gates.

Those capabilities are too easy to compose.

The remaining potential value must come from reducing a recurring **cross-vendor change-management and qualification-state coordination burden** that is materially expensive to maintain internally.

## Commercial implication

The buyer must not be sold "a better benchmark system" or "a better CI pipeline."

The strongest possible commercial promise is closer to:

> Maintain a continuously defensible answer to: "Is this exact AI compute configuration still qualified for our workloads, and what changed when it stopped being qualified?"

Even this promise remains unproven as an independent paid category.

## Revised decision state

| Question | Result |
|---|---|
| Can customers build basic qualification internally? | **YES — established** |
| Does that kill generic qualification SaaS? | **YES** |
| Does that kill cross-vendor lifecycle qualification completely? | **NOT PROVEN** |
| Is change-impact/requalification pain demonstrated? | **STRONG SIGNAL, not sufficient WTP evidence** |
| Is independent software WTP demonstrated? | **NO** |

## Current scoring after Internal Build Kill Test

| Criterion | Score |
|---|---:|
| Problem severity | 4.3/5 |
| Unmet gap | 2.4/5 |
| Buyer clarity | 3.0/5 |
| Economic value | 3.6/5 |
| Technical feasibility | 4.7/5 |
| Defensibility | 2.4/5 |
| Willingness to pay | 1.8/5 |

Weighted score ≈ 62/100.

The broad software wedge remains below the 3/5 gap hard gate.

## Decision

# `PIVOT`

More precisely:

> **KILL the generic software product hypothesis. Preserve only the change-impact / lifecycle coordination problem as an unresolved research question.**

## Next falsification target

The project should now test a much narrower proposition:

> **Do organizations operating heterogeneous AI compute have a recurring, expensive change-impact problem that is not adequately handled by their existing CI/CMDB/MLOps/vendor tooling?**

The next investigation must examine:

1. hardware refresh / vendor migration;
2. compiler/runtime/driver/firmware changes;
3. model/version changes;
4. heterogeneous serving compositions;
5. acceptance evidence reuse;
6. audit or contractual performance commitments.

For each case we need evidence of frequency, engineering effort, failure cost, existing workaround, and budget ownership.

## Kill condition

If those workflows are typically infrequent, cheaply handled with existing internal tooling, or delegated to vendors/consultants without material recurring cost, **KILL the project entirely**.

If one workflow demonstrates recurring high cost and a credible buyer explicitly prefers an external solution, that workflow becomes the only surviving wedge.

## Sources

- https://mlflow.org/docs/latest/deployment/
- https://mlflow.github.io/mlflow-website/docs/latest/ml/evaluation/
- https://argoproj.github.io/workflows/
- https://docs.gitlab.com/ci/testing/load_performance_testing/
- https://kubernetes.io/blog/2026/02/03/introducing-node-readiness-controller/
- https://instinct.docs.amd.com/projects/system-acceptance/en/latest/
- https://www.substrat.pro/
- https://tensorpi.ai/enterprise
- https://docs.together.ai/docs/health-checks
