# Evidence Ledger

This ledger records material claims used in the decision process.

| ID | Claim | Status | Evidence Level | Source | Decision Impact | Counterevidence / Caveat |
|---|---|---|---|---|---|---|
| E-001 | Specialized AI accelerators are moving beyond a single GPU architecture. | ESTABLISHED | L3/L4 | d-Matrix production announcement; Tenstorrent ecosystem; other accelerator vendors | Supports problem context | Does not prove our product gap. |
| E-002 | AI accelerator procurement increasingly requires workload-specific performance, power, latency, and TCO evidence. | STRONG MARKET SIGNAL | L1/L3 | MLPerf Endpoints; Google accelerator benchmarking guidance; NVIDIA procurement guidance | Strongly supports workflow relevance | Vendor guidance is not WTP proof. |
| E-003 | Public neutral/continuous AI benchmarking is already a developed category. | ESTABLISHED | L2/L3 | MLPerf, InferenceX, AA-AgentPerf, ByteMLPerf, xpu-perf | Rejects generic benchmark positioning | Qualification may still be distinct; must prove it. |
| E-004 | Vendor software stacks already cover significant portions of compiler/runtime/model enablement and production serving. | ESTABLISHED | L1/L2 | NVIDIA NIM, AWS Neuron, Tenstorrent, d-Matrix and others | Rejects generic compiler/runtime positioning | Cross-vendor customer decision remains open. |
| E-005 | Configuration compatibility across model/runtime/compiler/driver/firmware/hardware is operationally significant. | ESTABLISHED | L1/L2 | Vendor compatibility matrices; Tenstorrent compatibility docs; NVIDIA support docs | Supports qualification context | Existing matrices solve narrower vendor-scoped parts. |
| E-006 | Unconventional AI publicly demonstrates a dynamical AI model and research around system modeling/ISA/physical computing. | ESTABLISHED | L1/L2 | Unconventional AI publications and public Un-0 repository | Supplies a future heterogeneous backend/use case | Public artifacts do not establish commercial silicon energy claims. |
| E-007 | A cross-vendor, workload-specific qualification layer is not yet proven to be a standalone paid category. | UNKNOWN / OPEN | — | Research conclusion | Critical commercial gate | Requires direct buyer/WTP evidence. |
| E-008 | Continuous requalification could become more valuable as software/hardware configurations change. | HYPOTHESIS | L1/L3 | InferenceX continuous testing; vendor lifecycle/version practices | Candidate wedge | Must prove budget ownership and WTP. |
| E-009 | NVIDIA has a formal vendor-scoped production lifecycle with NIM Certified, including broad hardware validation and production/feature branch maintenance. | ESTABLISHED | L1 | NVIDIA NIM documentation | Strong counterevidence to generic production qualification | Scope is NVIDIA ecosystem; neutrality remains outside scope. |
| E-010 | AWS Neuron provides automated model porting and multi-stage numerical-equivalence validation. | ESTABLISHED | L1 | AWS Neuron 2.30 and Equivalence documentation | Strong counterevidence to generic port-validation tooling | Scope is AWS Trainium/Inferentia ecosystem. |
| E-011 | Tenstorrent provides validated deployment workflows plus explicit hardware/software compatibility guidance. | ESTABLISHED | L1 | Tenstorrent software and compatibility documentation | Strong counterevidence to generic vendor enablement tooling | Scope is Tenstorrent ecosystem. |
| E-012 | InferenceX has a mature evidence/reproducibility/testing system, including configuration validation, workflow artifacts, and review gates. | ESTABLISHED | L2 | InferenceX public repository and testing documentation | Raises differentiation bar substantially | Primary purpose remains benchmarking/research rather than customer acceptance ownership. |
| E-013 | A useful qualification abstraction must distinguish SUPPORTED, BENCHMARKED, QUALIFIED, and PRODUCTION-APPROVED states. | INFERENCE / HYPOTHESIS | L2/L3 | Combined ecosystem workflow analysis | Defines technical experiment | Must be validated against real customer workflows. |
| E-014 | Customer-owned acceptance policy across competing accelerator vendors is not shown by reviewed public evidence to be a standard capability of existing benchmark/vendor stacks. | OPEN / STRONG INFERENCE | L1/L2 | Comparative teardown | Core candidate gap | Absence in public docs is not proof of absence in private/internal systems. |
| E-015 | Together AI has a dedicated Technical Compute Qualification Manager role owning end-to-end provider qualification, standards/templates, parallel evaluations, auditable records, and go/no-go recommendations. | ESTABLISHED | L1 | Together AI job posting | Strong evidence the problem is real; strong evidence sophisticated operators may solve it internally | This may reduce external software WTP; job posting is not customer purchase evidence. |
| E-016 | AMD publishes a current customer-acceptance methodology with node/cluster validation, explicit thresholds, automated Cluster Validation Suite workflows, and production go-live criteria. | ESTABLISHED | L1 | AMD Instinct Customer Acceptance Guide | Strong negative evidence against generic production-qualification software | Vendor-scoped and operator-oriented. |
| E-017 | MLflow, Argo Workflows, GitLab CI, and Kubernetes readiness primitives can compose substantial portions of evaluation, orchestration, thresholding, and release gating internally. | ESTABLISHED | L1 | Official project documentation | Strong negative evidence against generic orchestration/gating software | Composition still requires integration engineering and does not establish end-to-end cross-vendor qualification. |
| E-018 | Independent companies such as Substrate Co and TensorPi sell workload-specific multi-hardware evaluation and procurement guidance as services. | ESTABLISHED | L1 | Public company service pages | Strong negative evidence against simple benchmarking/consulting automation wedge | Does not prove they own continuous customer qualification state. |
| E-019 | The internal-build alternative kills the generic qualification SaaS proposition but does not prove that recurring cross-vendor change-impact/requalification is cheaply solved. | INFERENCE / HYPOTHESIS | L2/L3 | Kill Test #2 and ecosystem evidence | Preserves one narrow research question | Requires direct workflow/time-cost/WTP validation. |

## Rules

- Add a new row for every material claim that influences a decision.
- Prefer primary sources and public artifacts.
- Preserve contradictory evidence; never delete unfavorable findings.
- Upgrade claim status only when evidence quality warrants it.
- Never mark WTP as established without direct commercial evidence.
- Public absence is evidence about documented scope, not proof that no private/internal implementation exists.
