# Commercial Evidence Matrix

Research snapshot: 2026-08-31. This is a working research artifact; scores are not validated WTP.

## Evidence classes

- `E`: established by primary/strong evidence
- `S`: strong market signal
- `H`: hypothesis requiring direct validation
- `U`: unknown

## Workflow Matrix

| ID | Workflow | Primary Buyer | Current Alternatives | Pain | Gap | Economic Value | WTP | Priority |
|---|---|---|---|---|---|---|---|---:|
| CW-01 | Accelerator procurement / selection | AI infrastructure leadership | RFPs, vendor benchmarks, internal PoCs, consultants | High | S/H | High | H | 5 |
| CW-02 | GPU → ASIC workload migration qualification | AI platform / infra | Vendor SDKs, porting workflows, manual validation | High | S | High | H | 5 |
| CW-03 | Production acceptance testing | Enterprise AI platform | Manual acceptance tests, vendor reports | High | S/H | High | H | 5 |
| CW-04 | Accelerator TCO comparison | Infrastructure + finance | RFPs, benchmark reports, spreadsheets, consultants | High | S | High | H | 5 |
| CW-05 | Power / energy qualification | Data center / infra | MLPerf Power, vendor telemetry, bespoke measurement | Medium/High | S | High | H | 4 |
| CW-06 | Compiler/runtime regression qualification | Platform engineering | CI, custom benchmarks, vendor tools | High | S | High | H | 4 |
| CW-07 | Driver/firmware/software-stack regression | Infrastructure engineering | Compatibility matrices, CI, vendor tooling | High | S | Medium/High | H | 4 |
| CW-08 | Agentic workload qualification | AI infrastructure | AA-AgentPerf, InferenceX, custom workloads | High | S | High | H | 5 |
| CW-09 | Heterogeneous pipeline qualification | AI infrastructure | Internal tooling, vendor stack, serving/orchestration | Very High | S/H | Very High | H | 5 |
| CW-10 | Production deployment gate | ML/AI platform | Manual checklists, CI/CD, observability | High | S/H | High | H | 5 |
| CW-11 | Hardware refresh decision | CIO/CTO/infra | RFP + spreadsheet + PoC | Medium/High | S | High | H | 4 |
| CW-12 | Partner interoperability validation | Hardware/software vendor | Bilateral testing, vendor labs | Medium/High | S | Medium/High | H | 4 |
| CW-13 | Independent customer-facing certification | Accelerator vendor / cloud | Vendor benchmarks + third-party consulting | Medium/High | H/S | High | H | 4 |
| CW-14 | Pre-silicon → silicon correlation | Semiconductor engineering | Internal simulation/validation | Very High | S | Very High | H | 4 |
| CW-15 | Continuous historical requalification | AI platform / infra | CI, dashboards, benchmark archives | High | S/H | High | H | 5 |

## Evidence from current teardown

### Procurement is a real decision problem

MLPerf Endpoints explicitly positions inference-compute procurement as a business decision and targets evaluation across cloud providers, neoclouds, and managed services. NVIDIA's current NIM documentation also shows workload-aware benchmarking and selection using metrics such as TTFT, ITL, throughput, concurrency, and model/hardware deployment profiles. This supports the existence of the workflow, not our exact product WTP.

### Benchmarking is already highly occupied

MLPerf provides standardized benchmarks and a mature submission ecosystem. InferenceX provides continuous real-hardware cross-vendor benchmarking with linked recipe/run/artifact/database provenance and power telemetry. This is strong negative evidence against creating a generic benchmark platform.

### Vendor-specific validation is already sophisticated

NVIDIA NIM provides model/hardware support matrices and validated deployment profiles. AWS Neuron provides model autoporting and a multi-stage numerical-equivalence workflow. Tenstorrent provides an end-to-end compiler/runtime stack plus validated-model sources. This is strong negative evidence against generic model-porting, compiler, runtime, or vendor-specific compatibility tooling as the primary wedge.

### Candidate gap

The remaining hypothesis is a customer-owned, vendor-neutral qualification layer that consumes existing benchmark/validation outputs and adds:

- workload requirements;
- reusable acceptance criteria;
- immutable environment/configuration identity;
- cross-vendor execution;
- evidence provenance;
- reproducibility checks;
- deterministic pass/review/fail policy;
- production release gating;
- continuous requalification when relevant configuration changes.

This is still a hypothesis. Public evidence does not yet establish that customers will buy it as a standalone product.

## Current candidate lifecycle

`SELECT → QUALIFY → DEPLOY → CHANGE → REQUALIFY`

The working product hypothesis is one lifecycle, not five separate products.

## Commercial questions that remain open

For every priority workflow, research must establish:

- who experiences the pain;
- who owns the budget;
- what triggers the workflow;
- frequency and duration;
- engineering effort;
- current tools and vendors;
- manual steps and failure modes;
- evidence currently produced;
- decision affected by the evidence;
- economic impact of a wrong decision;
- whether neutrality, speed, reproducibility, or risk reduction is valuable enough to pay for.

## WTP standard

The following are **not** proof of willingness to pay:

- market size;
- vendor claims;
- investor funding;
- positive interviews without commitment;
- technical interest;
- free pilot usage.

Strong WTP evidence includes paid discovery, paid qualification engagement, paid pilot, purchase order, signed commercial commitment, or measurable renewal/expansion.

## Sources

- MLPerf: https://docs.mlcommons.org/inference/index_gh/
- MLPerf Endpoints: https://mlcommons.org/2026/07/mlperf-endpoints-v0-7-release/
- InferenceX: https://inferencex.semianalysis.com/about
- NVIDIA NIM support: https://docs.nvidia.com/nim/large-language-models/latest/reference/support-matrix.html
- NVIDIA NIM benchmarking: https://docs.nvidia.com/nim/benchmarking/llm/latest/overview.html
- AWS Neuron equivalence: https://awsdocs-neuron.readthedocs-hosted.com/en/latest/tools/neuron-agentic-development/developer_guides/neuron-framework-equivalence.html
- AWS Neuron 2.30: https://aws.amazon.com/about-aws/whats-new/2026/05/aws-announce-neuron-2-30-0/
- Tenstorrent stack: https://docs.tenstorrent.com/getting-started/tt-software-stack.html
