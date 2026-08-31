# Kill Test — Production Qualification / Procurement Wedge

Research date: 2026-08-31
Status: `KILL_CURRENT_WEDGE / PIVOT_CANDIDATE`

## Purpose

This is an adversarial test of the current product hypothesis. The objective is to find evidence that makes the opportunity unnecessary, already solved, too cheap to buy, or structurally difficult to defend.

The test does **not** attempt to prove the opportunity. Positive evidence is useful only after the strongest negative cases survive.

## Hypothesis under test

> A customer-owned, vendor-neutral software system for workload-specific AI compute qualification can provide enough value to justify an independent product, especially for accelerator procurement, production acceptance, and continuous requalification.

## Strongest kill evidence found

### 1. Vendor ecosystems already provide substantial qualification inside their boundary

AMD publishes a Kubernetes-native GPU Server Intake & Validation architecture that automates hardware validation, burn-in, failure remediation, release decisions, quarantine/RMA paths, and production handoff. Burn-in durations include a dedicated production-qualification path. This materially weakens a generic production-qualification product for a single vendor ecosystem.

NVIDIA NIM Certified provides broad hardware validation, validated deployment profiles, production branches, workload-specific tuning, and lifecycle support. NVIDIA also provides AIPerf/GenAI-Perf benchmarking and real-traffic payload capture/replay capabilities.

AWS Neuron provides Autoport and multi-stage numerical-equivalence validation, reducing the need for generic model-port qualification within the AWS Trainium/Inferentia ecosystem.

Tenstorrent provides an end-to-end compiler/runtime/deployment stack, validated model sources, production inference server, hardware telemetry, and Kubernetes support.

**Assessment:** Strong negative evidence against vendor-specific qualification software.

### 2. Cloud/infrastructure operators already implement acceptance workflows internally

Together AI documents automatic acceptance testing for newly provisioned GPU clusters, including GPU diagnostics and sustained stress testing, with recorded pass/fail criteria. Together also describes acceptance testing across clusters containing thousands of GPUs as an operational process built to protect customer-facing production infrastructure.

AMD's published intake architecture similarly demonstrates that a customer/operator can assemble automated validation, burn-in, remediation, and release decisions using Kubernetes-native components.

**Assessment:** Strong negative evidence against the claim that enterprises necessarily need an external product to automate basic production acceptance.

### 3. Independent services already sell workload-specific accelerator evaluation

Substrate Co markets independent, documented, repeatable workload-specific accelerator benchmarking, including cross-vendor NVIDIA/AMD/custom-ASIC studies, comparative reports, reusable benchmark methods, and an advisory retainer.

TensorPi markets a discovery → multi-hardware evaluation → benchmark report → procurement recommendation → deployment workflow, explicitly covering GPUs and other accelerators.

TechnoLynx/LynxBenchAI markets workload-faithful, stack-disclosed benchmarking and procurement evidence, including TCO and reproducibility framing.

These examples establish that customers can already buy independent evaluation services without adopting new qualification software.

**Assessment:** Strong negative evidence against a simple "we will automate independent accelerator evaluation" product wedge.

### 4. Benchmark infrastructure is already highly developed

MLPerf/Endpoints, InferenceX, AA-AgentPerf, ByteMLPerf, and related tooling cover standardized or continuous performance evaluation, cross-vendor comparison, power/energy measurement, workload realism, provenance, and repeatability.

**Assessment:** Generic benchmark/evidence collection is a killed positioning.

### 5. The internal-build alternative is credible

An enterprise can combine CI/CD, vendor matrices, benchmark suites, Kubernetes, telemetry, MLflow/other experiment tracking, and custom scripts to implement significant portions of qualification.

The existence of production practices published by operators and vendors demonstrates that this is not merely theoretical.

**Assessment:** The product must replace meaningful recurring labor/risk, not merely consolidate convenient scripts.

## What the kill test does NOT establish

It does not prove that a cross-vendor, customer-owned qualification control plane is unnecessary.

The remaining potentially distinct function is the combination of:

- customer-owned workload requirements;
- vendor-neutral acceptance policy;
- cross-vendor configuration comparison;
- normalized consumption of heterogeneous evidence sources;
- lifecycle identity for model/compiler/runtime/driver/firmware/hardware;
- explicit qualification state owned by the customer;
- release gating based on that state;
- automatic requalification after relevant changes;
- historical state that survives vendor or infrastructure changes.

Public evidence reviewed to date does not show a single widely adopted product that clearly owns all of these capabilities across arbitrary vendors and customer workloads.

**However, absence of a found product is not proof of a market gap.**

## Decision impact

### Current wedges

| Wedge | Decision | Reason |
|---|---|---|
| Generic benchmark platform | **KILL** | Mature public ecosystem |
| Generic benchmark/profiler service | **KILL as software wedge** | Independent services + internal tooling |
| Vendor-specific qualification | **KILL** | Vendors already own large portions |
| Generic production acceptance automation | **KILL as standalone wedge** | AMD/Together/operator workflows demonstrate credible existing approaches |
| Cross-vendor procurement consulting | **PIVOT / crowded** | Multiple independent services already sell this |
| Customer-owned cross-vendor qualification state | **OPEN** | Potentially distinct, but not commercially proven |
| Continuous cross-vendor requalification gate | **OPEN** | Potentially distinct, but WTP not proven |

## Current scoring after kill test

| Criterion | Score | Interpretation |
|---|---:|---|
| Problem severity | 4.5/5 | Strong evidence that compute selection/acceptance matters |
| Unmet gap | 2.7/5 | Too much is already solved by vendors, operators, and services |
| Buyer clarity | 3.2/5 | Plausible buyers exist, but ownership is not sufficiently validated |
| Economic value | 3.8/5 | Wrong decisions and infrastructure regressions can be expensive |
| Technical feasibility | 4.6/5 | Software-only probe is feasible |
| Defensibility | 2.9/5 | Data/history could help, but incumbents and internal build are serious |
| Willingness to pay | 2.0/5 | No direct paid evidence yet |

Weighted score ≈ 67/100.

Because the **Unmet Gap score is below the 3/5 hard gate**, the current product hypothesis does **not** qualify for GO.

## Provisional decision

# `PIVOT`

This is a **pivot of the product wedge, not a conclusion that the broader opportunity is dead**.

The evidence currently supports killing the following framing:

> "A general AI compute qualification/benchmarking platform that automates evaluation."

The remaining hypothesis must be narrower and more economically consequential.

## Required pivot tests

1. **Contractual/acceptance evidence layer:** Is there a recurring need to turn workload requirements into contractual or operational acceptance criteria across independent vendors?
2. **Change-impact qualification:** When model/compiler/runtime/driver/firmware/hardware changes, who owns proving that production requirements still hold, and what does that process cost?
3. **Cross-vendor customer-owned state:** Is there a real system-of-record problem caused by vendor-specific qualification states that cannot be reconciled across vendors?
4. **Commercial trigger:** Can a buyer identify a budgeted event (procurement, migration, acceptance, renewal, major software change, capacity expansion) where an external product is preferred to internal tooling or consulting?
5. **Paid wedge:** Can the same narrow workflow be sold as a paid pilot without requiring us to own the measurement infrastructure?

## Kill conditions for the remaining hypothesis

Kill the project completely if research finds either:

- a credible, broadly adopted product already owning customer-specific cross-vendor qualification state + lifecycle requalification + release gating; or
- buyers consistently prefer existing internal tooling/services and cannot justify a standalone product budget.

## Sources

- https://instinct.docs.amd.com/projects/advanced-micro-devices-k8s-reference-arch/en/latest/reference/gpu-server-intake.html
- https://docs.together.ai/docs/health-checks
- https://www.together.ai/blog/a-practitioners-guide-to-testing-and-running-large-gpu-clusters-for-training-generative-ai-models
- https://docs.nvidia.com/nim/large-language-models/latest/about-nim-llm/nim-offerings.html
- https://docs.nvidia.com/nim/benchmarking/llm/latest/overview.html
- https://awsdocs-neuron.readthedocs-hosted.com/en/latest/tools/neuron-agentic-development/developer_guides/neuron-framework-equivalence.html
- https://docs.tenstorrent.com/getting-started/tt-software-stack.html
- https://www.substrat.pro/
- https://tensorpi.ai/businesses
- https://www.technolynx.com/post/procurement-definition-ai
- https://mlcommons.org/2026/07/mlperf-endpoints-v0-7-release/
- https://inferencex.semianalysis.com/about
