# Evidence Ledger

This ledger records material claims used in the decision process.

| ID | Claim | Status | Evidence Level | Source | Decision Impact | Counterevidence / Caveat |
|---|---|---|---|---|---|---|
| E-001 | Specialized AI accelerators are moving beyond a single GPU architecture. | ESTABLISHED | L3/L4 | d-Matrix production announcement; Tenstorrent software/hardware ecosystem; other accelerator vendors | Supports problem context | Does not prove our specific product gap. |
| E-002 | AI accelerator procurement increasingly requires workload-specific performance, power, latency, and TCO evidence. | STRONG MARKET SIGNAL | L1/L3 | Google accelerator benchmarking guidance; NVIDIA procurement guidance | Strongly supports workflow relevance | Vendor guidance is not independent WTP proof. |
| E-003 | Public neutral/continuous AI benchmarking is already a developed category. | ESTABLISHED | L2/L3 | MLPerf, InferenceX, AA-AgentPerf, ByteMLPerf, xpu-perf | Rejects generic benchmark positioning | Qualification may still be distinct; must prove it. |
| E-004 | Vendor software stacks already cover significant portions of compiler/runtime/model enablement. | ESTABLISHED | L1/L2 | NVIDIA, AMD ROCm, AWS Neuron, Tenstorrent, d-Matrix, Lightmatter, Mythic | Rejects generic compiler/runtime positioning | Cross-vendor decision workflow remains open. |
| E-005 | Configuration compatibility across model/runtime/compiler/driver/firmware/hardware is operationally significant. | ESTABLISHED | L1/L2 | AMD compatibility matrix; vendor compatibility matrices; serving framework matrices | Supports qualification hypothesis | Existing matrices may solve narrower parts. |
| E-006 | Unconventional AI publicly demonstrates a dynamical AI model and research around system modeling/ISA/physical computing. | ESTABLISHED | L1/L2 | Unconventional AI publications and public Un-0 repository | Supplies future heterogeneous backend/use case | Public artifacts do not establish commercial silicon energy claims. |
| E-007 | A cross-vendor, workload-specific qualification layer is not yet proven to be a standalone paid category. | UNKNOWN / OPEN | — | Research conclusion | Critical commercial gate | Requires buyer/WTP evidence. |
| E-008 | Continuous requalification could become more valuable as software/hardware configurations change. | HYPOTHESIS | L1/L3 supporting signals | InferenceX continuous benchmarks; vendor compatibility/version practices | Candidate product wedge | Must prove budget ownership and willingness to pay. |

## Rules

- Add a new row for every material claim that influences a decision.
- Use primary sources where possible.
- Preserve contradictory evidence; do not delete unfavorable findings.
- Upgrade claim status only when evidence quality warrants it.
- Never mark WTP as established without direct commercial evidence.
