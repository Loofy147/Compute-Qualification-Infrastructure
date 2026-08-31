# Compute Qualification Infrastructure

**Decision: KILLED — 2026-08-31**

This repository is an archived opportunity-validation and research record. It is **not** an active product-development project.

## Final conclusion

The investigation established that specialized and heterogeneous AI compute creates real engineering and economic problems around performance, power, compatibility, acceptance, and lifecycle change. However, the proposed independent software business around cross-vendor compute qualification did not clear the required evidence threshold.

The strongest counterevidence was decisive:

- standardized and continuous benchmarking is already well served by MLPerf, InferenceX, AA-AgentPerf, ByteMLPerf, xpu-perf, and vendor tooling;
- NVIDIA, AMD, AWS, Tenstorrent, d-Matrix, and other ecosystems provide substantial vendor-scoped validation, deployment, compatibility, and production-readiness tooling;
- large operators such as Together AI demonstrate that sophisticated compute acceptance and qualification workflows can be built and operated internally;
- independent specialists already sell workload-specific accelerator benchmarking and procurement analysis as services;
- the residual hypothesis — customer-owned cross-vendor qualification state and continuous requalification — remained technically plausible but lacked direct willingness-to-pay evidence and sufficient defensibility against internal tooling and existing ecosystems.

Therefore the project is formally **KILL** rather than continued as a product build.

## Preserved research value

The repository remains useful as a research artifact containing:

- decision charter and anti-bias rules;
- commercial evidence matrix;
- competitor workflow teardowns;
- evidence ledger;
- kill tests and falsification results;
- distinctions among `SUPPORTED`, `BENCHMARKED`, `QUALIFIED`, and `PRODUCTION-APPROVED` states;
- future research leads around change-impact analysis and heterogeneous AI infrastructure governance.

## No further implementation

Do not implement or productize a Qualification Runner, benchmark platform, profiler, generic accelerator dashboard, vendor-neutral qualification SaaS, or consulting offering under this repository.

Any future idea derived from this work must begin as a **new opportunity investigation** with a new decision charter and fresh commercial evidence.

## Decision record

See [`decisions/final/2026-08-31-KILL.md`](decisions/final/2026-08-31-KILL.md) for the complete final decision and reopen conditions.
