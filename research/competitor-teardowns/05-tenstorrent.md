# Competitor Teardown — Tenstorrent Software Stack

Status: `RESEARCHED`

## What it is

Tenstorrent provides a vertically integrated software stack around its hardware. Current public documentation describes TT-Forge as an end-to-end MLIR-based compiler, TT-NN as a higher-level neural-network API, TT-Lang for custom fused operations, TT-MLIR as compiler infrastructure, and TT-Metalium as the low-level C++ hardware SDK. Tenstorrent also provides TT-Inference-Server, TT-Studio, device monitoring, and cloud-native/Kubernetes support.

## Workflow coverage

```text
PyTorch / JAX / ONNX
  -> TT-Forge / TT-XLA / ONNX frontend
  -> TT-MLIR
  -> TT-NN / TT-Metalium
  -> hardware execution
  -> TT-Inference-Server
  -> monitoring / deployment
```

The documentation states that TT-Inference-Server is the authoritative source for validated model support on each hardware generation, while TT-Forge Models tracks models validated against the compiler stack.

## Capability assessment

| Capability | Tenstorrent | Assessment |
|---|---|---|
| Model compilation | Yes | Very strong |
| Runtime/API | Yes | Very strong |
| Low-level hardware SDK | Yes | Very strong |
| Model validation catalog | Yes | Strong |
| Deployment | Yes | Strong |
| Monitoring | Yes | Strong |
| Kubernetes | Yes | Strong |
| Cross-vendor qualification | No | Outside vendor scope |
| Neutral comparison | No | Outside vendor scope |
| Customer acceptance policy | Customer tooling required | Potential gap |
| Cross-vendor evidence registry | No | Potential gap |

## Red-team conclusion

Tenstorrent is strong evidence against building another hardware enablement stack. A generic compiler/runtime/platform positioned as developer tooling would enter a mature and rapidly evolving vendor-owned ecosystem.

## Remaining candidate gap

The possible layer above Tenstorrent is not to replace TT-Forge or TT-Metalium, but to consume their outputs as one backend among several and answer a customer-owned question such as:

> Is this workload/configuration acceptable for production under our requirements, and can we prove that decision across competing hardware/software stacks?

Sources:
- https://docs.tenstorrent.com/getting-started/tt-software-stack.html
- https://docs.tenstorrent.com/software/index.html
- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/get_started/get_started.html
