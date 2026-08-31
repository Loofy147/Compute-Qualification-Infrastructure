# W2 — Production Qualification Teardown

Research snapshot: 2026-08-31

## Decision question

Does a **customer-owned, vendor-neutral production qualification layer** solve a material problem that vendor stacks and existing benchmark systems do not already solve adequately?

The unit of analysis is the workflow from a candidate change/configuration to an explicit production decision.

---

## Canonical workflow

```text
Change / new configuration
        ↓
Identify affected workload + requirements
        ↓
Resolve exact model / runtime / compiler / driver / firmware / hardware
        ↓
Select tests / benchmarks / validation procedures
        ↓
Execute on target environment
        ↓
Validate correctness / quality
        ↓
Measure latency / throughput / power / cost
        ↓
Collect provenance + artifacts
        ↓
Evaluate customer acceptance policy
        ↓
QUALIFIED / REVIEW / REJECT
        ↓
Record qualification state
        ↓
Trigger requalification on relevant future changes
```

This is a reference model, not a claim that every organization follows it exactly.

---

## Vendor / ecosystem teardown

### NVIDIA NIM

**What is clearly solved**

- NIM provides supported model / deployment-profile / hardware information.
- NIM Certified is explicitly positioned for enterprise production, including broad hardware validation, lifecycle handling, rolling inference-stack updates, and production-branch baselines.
- NVIDIA documents deployment paths for containers, Kubernetes, multi-node, and major cloud providers.
- NVIDIA benchmarking tooling measures workload-relevant inference behavior.

**What remains vendor-owned**

The production guarantee is scoped to the NVIDIA ecosystem. NIM Certified can establish that a supported NIM/profile is appropriate within NVIDIA's validated lifecycle, but it is not a neutral acceptance authority across competing accelerator vendors.

**Potential gap**

Customer-owned acceptance criteria spanning NVIDIA + non-NVIDIA configurations, using a common qualification state and common lifecycle semantics.

**Evidence**

NVIDIA states that NIM Certified provides broader hardware validation and enterprise lifecycle options for production deployments, including rolling updates and production-branch validation patterns. Its support FAQ directs users to verified hardware, validated profiles, software prerequisites, and deployment paths.

Sources:
- https://docs.nvidia.com/nim/large-language-models/latest/about-nim-llm/nim-offerings.html
- https://docs.nvidia.com/nim/large-language-models/latest/resources/support-and-faq.html

---

### AWS Neuron

**What is clearly solved**

- Model porting to Trainium / Inferentia.
- Numerical-equivalence validation through a multi-stage workflow.
- Structural analysis, smoke testing, component-level testing, fault localization, end-to-end comparison, and downstream evaluation are documented capabilities.
- Kubernetes resource integration and accelerator scheduling are part of the stack.

**What remains vendor-owned**

These capabilities determine whether a workload is successfully ported to AWS Neuron and whether target/reference outputs are sufficiently equivalent. The scope is the AWS Trainium/Inferentia ecosystem.

**Potential gap**

A customer may still need to compare the AWS-qualified candidate against NVIDIA, AMD, or another accelerator under the same business acceptance policy. Numerical equivalence alone also does not constitute an enterprise production decision covering TCO, energy, SLOs, operational risk, and alternative configurations.

**Evidence**

AWS Neuron 2.30.0 added framework Autoport, numerical-equivalence validation, and Kubernetes DRA for Trainium/Inferentia. The Equivalence workflow is documented as an explicit staged process rather than a single benchmark.

Sources:
- https://aws.amazon.com/about-aws/whats-new/2026/05/aws-announce-neuron-2-30-0/
- https://awsdocs-neuron.readthedocs-hosted.com/en/latest/tools/neuron-agentic-development/developer_guides/neuron-framework-equivalence.html

---

### Tenstorrent

**What is clearly solved**

- Validated model catalog and hardware/software compatibility guidance.
- TT-Inference-Server automates production-oriented deployment setup for validated configurations.
- The software ecosystem spans compiler, runtime, low-level SDK, serving, monitoring, and cloud-native deployment.
- Tenstorrent publishes validated hardware/software combinations and explicitly warns about version matching for some native setups.

**What remains vendor-owned**

The qualification is primarily a statement about Tenstorrent hardware and its software stack.

**Potential gap**

A customer selecting among Tenstorrent, NVIDIA, AMD, AWS, or another accelerator still needs a common customer-owned policy and historical qualification state that is independent of the vendor catalogs.

**Evidence**

Tenstorrent describes TT-Inference-Server as its official production workflow automation tool and documents validated configurations. Its version-compatibility documentation publishes specific tested combinations and identifies native-installation version-matching challenges.

Sources:
- https://docs.tenstorrent.com/getting-started/tt-software-stack.html
- https://docs.tenstorrent.com/tt-vscode-toolkit/version-compat/
- https://docs.tenstorrent.com/tt-vscode-toolkit/lessons/tt-inference-server/

---

### InferenceX

**What is clearly solved**

- Cross-vendor real-hardware benchmarking.
- Continuous re-runs as model, hardware, framework, kernels, and software change.
- Strong recipe → workflow → attempt → artifact → database provenance.
- Power telemetry and reproducibility controls.
- Explicit testing layers and review gates.

**What remains outside the primary objective**

InferenceX is a research/benchmarking system. Its public testing guide distinguishes benchmark evidence from higher-level decisions: passing tests or completed evidence does not itself establish an enterprise production acceptance decision.

**Potential gap**

A customer-specific acceptance contract and policy engine that can consume InferenceX outputs alongside vendor-specific evidence, then establish a durable production qualification state and release gate.

**Evidence**

InferenceX explicitly states that a green later-layer check does not erase missing earlier evidence and that collectors can succeed even when executed evidence is empty. Its evidence standard requires exact commit, command, workflow run, artifacts, metrics, and evaluation image identity.

Source:
- https://github.com/SemiAnalysisAI/InferenceX/blob/main/docs/testing.md

---

### MLPerf / MLPerf Endpoints

**What is clearly solved**

- Standardized, cross-vendor benchmarking.
- Buyer-facing comparison of deployed systems.
- Performance dimensions such as throughput, interactivity, TTFT, and concurrency.
- MLPerf Endpoints explicitly frames inference compute procurement as a business decision and aims to provide current, comparable results across providers.

**What remains outside the primary objective**

MLPerf is a benchmark/measurement standard and decision input, not a customer-specific production release authority.

**Potential gap**

Translate benchmark and validation evidence into a customer's own requirements and lifecycle acceptance state.

Source:
- https://mlcommons.org/2026/07/mlperf-endpoints-v0-7-release/

---

## Decision-boundary matrix

| Workflow stage | NVIDIA | AWS | Tenstorrent | InferenceX | MLPerf | Candidate |
|---|---|---|---|---|---|---|
| Define customer-specific acceptance contract | Partial/customer code | Partial/customer code | Partial/customer code | Not primary | Not primary | **Core** |
| Cross-vendor candidate comparison | No | No | No | Yes | Yes | **Core** |
| Vendor-specific correctness validation | Strong | Strong | Strong | Partial/workload-dependent | Strong for benchmark | Consume |
| Production serving | Strong | Strong | Strong | Not primary | No | Consume |
| Customer acceptance policy | Customer-owned | Customer-owned | Customer-owned | No | No | **Core** |
| Formal qualification state | Vendor scope | Vendor scope | Vendor scope | Benchmark result state | Benchmark result state | **Core** |
| Release gate based on customer policy | Partial | Partial | Partial | No | No | **Core** |
| Continuous requalification | Vendor lifecycle | Vendor lifecycle | Vendor lifecycle | Yes (benchmark lifecycle) | Rolling benchmark submissions | **Core** |
| Historical customer-owned qualification registry | No evidence | No evidence | No evidence | Research results DB | Public results DB | **Core** |
| Neutral decision across vendors | No | No | No | Yes for benchmark | Yes for benchmark | **Core** |

---

## What this does **not** prove

The teardown does **not** prove that the remaining layer is a standalone commercial category.

It proves a narrower architectural observation:

> Existing systems strongly cover benchmark generation, vendor-specific enablement, port correctness, serving, and operational tooling. The hypothesized remaining layer is the customer's own qualification policy and lifecycle state across heterogeneous vendors/configurations.

That is still a **market hypothesis**.

---

## Strongest falsification conditions

Kill or pivot W2 if any of the following is established with credible evidence:

1. A mature third-party product already accepts arbitrary customer workloads and requirements across multiple accelerator vendors.
2. That product preserves immutable environment/configuration identity and reproducible evidence.
3. It can consume or execute multiple vendor stacks without being vendor-owned.
4. It has a customer policy engine capable of producing a production qualification decision.
5. It blocks/releases deployments based on that decision and maintains historical qualification state.
6. Customers demonstrably use it as a system of record for these decisions.

Finding only a benchmark or compatibility matrix is not sufficient to kill W2; the entire decision lifecycle must be covered.

---

## Commercial implication

The likely buyer is not the data scientist. Candidates are:

- Head / VP of AI Infrastructure;
- AI platform engineering leadership;
- infrastructure procurement / architecture;
- neocloud / inference provider operations;
- accelerator vendor field engineering or customer engineering.

The commercial question is:

> Will one of these buyers pay to externalize or standardize the qualification workflow instead of maintaining internal scripts, vendor tools, benchmark systems, and spreadsheets?

This remains unproven.

---

## Next experiment

Build a minimal **Qualification Kernel** with exactly four responsibilities:

```text
Workload Contract
→ Evidence Ingestion
→ Customer Policy Evaluation
→ Qualification State
```

For the first technical proof, do **not** build a new benchmark engine. Use existing measurements or simple reproducible local workloads as evidence inputs.

The experiment succeeds only if the kernel can demonstrate a meaningful distinction between:

```text
SUPPORTED
BENCHMARKED
QUALIFIED
```

and can re-evaluate qualification when a material configuration element changes.

The experiment fails if the distinction cannot be made deterministically or if existing systems already provide it adequately.

---

## Current W2 status

`OPEN — STRONG TECHNICAL HYPOTHESIS / COMMERCIAL GAP UNPROVEN`

Current evidence strongly supports that production qualification is richer than compatibility or benchmarking. It does not yet establish standalone willingness to pay.
