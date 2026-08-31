# Competitor Teardown — InferenceX

Status: `RESEARCHED`

## What it is

InferenceX is an open-source continuous inference performance research platform. Its core proposition is that inference performance changes continuously as hardware, models, serving frameworks, kernels, and software versions change. The project continuously benchmarks combinations of hardware, model, framework, and precision and publishes linked evidence from recipe to workflow run to artifacts to database row.

## Current relevance

The current public repository lists support for major NVIDIA and AMD systems and planned support for additional TPU/custom hardware. It has also expanded into realistic long-context and agentic workloads through AgentX.

## Workflow coverage

```text
Pinned benchmark recipe
  -> GitHub Actions workflow
  -> real target hardware
  -> logs/artifacts/power telemetry
  -> result validation / processing
  -> database
  -> public dashboard
  -> repeated runs as software evolves
```

## Capability assessment

| Capability | InferenceX | Assessment |
|---|---|---|
| Real hardware execution | Yes | Strong |
| Cross-vendor performance | Yes | Strong |
| Continuous benchmarking | Yes | Strong |
| Power telemetry | Yes | Strong |
| Provenance from recipe to result | Yes | Strong |
| Reproducibility | Strong | Core strength |
| Agentic workloads | Yes | Increasingly strong |
| Customer-specific requirements | Not primary | Potential gap |
| Formal qualification policy | Not primary | Potential gap |
| Production acceptance decision | Not primary | Potential gap |
| Procurement workflow ownership | Research/data platform | Not a dedicated acceptance system |
| Configuration lifecycle registry | Strong for benchmark dimensions | Different objective from customer deployment lifecycle |

## Red-team conclusion

InferenceX is the strongest direct counterexample to any proposal framed as:

> “A neutral continuous benchmark with reproducible evidence across hardware vendors.”

That proposition is already occupied.

It also raises the bar for our design: if we build a qualification layer, it must be able to *consume benchmark evidence such as InferenceX*, not recreate it.

## Remaining candidate gap

The candidate gap is downstream of benchmark generation:

```text
Benchmark evidence
  + customer-specific workload contract
  + customer SLOs / power budget / accuracy requirement
  + software/hardware configuration identity
  + acceptance policy
  + production release decision
  + requalification triggers
```

The differentiator is **qualification and release governance**, not benchmark collection.

## Evidence

InferenceX states that every public datapoint is tied to a GitHub Actions run and that the recipe, logs, artifacts, and resulting database row are linked end to end. Its repository also documents explicit schemas for configuration, result validation, and power telemetry.

Sources:
- https://inferencex.semianalysis.com/about
- https://github.com/SemiAnalysisAI/InferenceX
- https://github.com/SemiAnalysisAI/InferenceX/blob/main/.github/AGENT_OPERATIONS.md
- https://github.com/SemiAnalysisAI/InferenceX/blob/main/docs/testing.md
