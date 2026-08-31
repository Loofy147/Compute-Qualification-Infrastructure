# Cross-Competitor Workflow Matrix

Research snapshot: 2026-08-31

This is a workflow teardown, not a feature-count comparison. The key question is where each incumbent starts and ends relative to a customer-owned production qualification decision.

## Legend

- **Y** = clearly provided / documented
- **P** = partial or indirect
- **N** = not the primary purpose / no evidence found
- **U** = unknown from reviewed public evidence

| Capability | MLPerf / Endpoints | InferenceX | NVIDIA NIM | AWS Neuron | Tenstorrent | Candidate layer |
|---|---:|---:|---:|---:|---:|---:|
| Standard workload definition | Y | Y | P | P | P | Y |
| Customer-specific workload contract | P | P | P | P | P | **Y** |
| Cross-vendor execution | Y | Y | N | N | N | **Y** |
| Hardware/software config identity | Y | Y | Y | Y | Y | **Y** |
| Performance measurement | Y | Y | Y | Y | Y | Consume |
| Power measurement | Y / separate program | Y | P | P | Y | Consume/normalize |
| Accuracy validation | Y | P/Y by workload | Y/P | Y | Y/P | **Y** |
| Numerical equivalence / port correctness | P | P | P | **Y** | P | Consume/normalize |
| Reproducible execution | Y/P | **Y** | P | P | P | **Y** |
| Evidence provenance | Y/P | **Y** | Vendor-owned | Vendor-owned | Vendor-owned | **Y** |
| Customer acceptance policy | N | N | P/customer code | P/customer code | P/customer code | **Y** |
| Production qualification decision | N | N | P within vendor ecosystem | P within vendor ecosystem | P within vendor ecosystem | **Y** |
| Cross-vendor qualification decision | N | N | N | N | N | **Y** |
| Continuous requalification | Benchmark releases | **Y** | Vendor lifecycle | Vendor lifecycle | Vendor lifecycle | **Y** |
| Historical customer-owned qualification state | N | Research database | N | N | N | **Y** |
| Deployment release gate | N | N | P | P | P | **Y** |
| Neutrality across vendors | **Y** | **Y** | N | N | N | **Y** |

## Critical interpretation

### What the incumbents already cover

The existing ecosystem is much stronger than our original hypothesis assumed:

1. MLPerf provides standardized, cross-vendor performance evaluation and is explicitly extending toward inference procurement.
2. InferenceX provides continuous real-hardware cross-vendor benchmarking with public recipe-to-artifact provenance and power telemetry.
3. NVIDIA NIM provides model support matrices, validated deployment profiles, production serving, and workload-aware benchmarking within its own ecosystem.
4. AWS Neuron provides porting, numerical-equivalence validation, profiling, compilation, and deployment integrations within the AWS hardware/software ecosystem.
5. Tenstorrent provides an end-to-end compiler/runtime/hardware software stack plus validated-model sources and cloud-native support.

### What still appears structurally different

The candidate product should own a *customer's acceptance decision*, while using all of the above as execution/evidence inputs:

```text
Customer requirement
  -> vendor-neutral workload contract
  -> choose benchmark/test sources
  -> execute on candidate configurations
  -> capture immutable environment identity
  -> validate quality/performance/energy
  -> collect evidence
  -> evaluate customer policy
  -> produce qualification state
  -> re-run when relevant configuration changes
```

This is a hypothesis, not yet a proven market gap.

## Important falsification test

The hypothesis should be killed or pivoted if a credible existing system is found that already provides, for arbitrary customer workloads and multiple vendors, all of:

- reusable workload requirements;
- cross-vendor execution;
- immutable configuration/environment identity;
- quality + performance + energy evidence;
- customer-owned acceptance policies;
- provenance/reproducibility;
- production release gating;
- continuous requalification;
- historical qualification state.

The burden of proof is on us to test this against actual workflows, not product marketing pages alone.

## Sources

- https://docs.mlcommons.org/inference/index_gh/
- https://mlcommons.org/2026/07/mlperf-endpoints-v0-7-release/
- https://inferencex.semianalysis.com/about
- https://github.com/SemiAnalysisAI/InferenceX
- https://docs.nvidia.com/nim/large-language-models/latest/reference/support-matrix.html
- https://docs.nvidia.com/nim/benchmarking/llm/latest/overview.html
- https://awsdocs-neuron.readthedocs-hosted.com/en/latest/tools/neuron-agentic-development/developer_guides/neuron-framework-equivalence.html
- https://aws.amazon.com/about-aws/whats-new/2026/05/aws-announce-neuron-2-30-0/
- https://docs.tenstorrent.com/getting-started/tt-software-stack.html
- https://docs.tenstorrent.com/software/index.html
