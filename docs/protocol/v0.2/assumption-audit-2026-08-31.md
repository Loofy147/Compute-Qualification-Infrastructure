# VEDP v0.2 Assumption Audit — 2026-08-31

## Purpose

This document stress-tests the assumption that the Venture Evidence & Decision Protocol (VEDP) could itself become a valuable standalone product. The engine must be treated as an unproven research artifact until these assumptions survive evidence.

## Current hypothesis

> A structured, evidence-first decision engine that models claims, provenance, independence, falsification, economics, hard gates, and GO/PIVOT/KILL decisions could provide enough incremental value over existing research, venture-studio, diligence, and decision workflows to justify adoption or payment.

## Assumption register

| ID | Assumption | Current status | Strongest counterevidence | Required proof |
|---|---|---|---|---|
| A-01 | People have a material problem with startup/opportunity decision quality. | SUPPORTED | Established venture studios already run structured validation and kill gates, showing the workflow is real. | Evidence that the pain is costly enough for an external product. |
| A-02 | Existing methods are insufficiently rigorous. | OPEN | Strategyzer has long provided explicit hypothesis/test/learning workflows; venture studios already operationalize validation gates. | Demonstrate a material failure mode not covered by current methods. |
| A-03 | Evidence provenance/falsification is sufficiently novel to matter commercially. | WEAK | Existing validation products increasingly emphasize cited/live sources; DimeADozen advertises 1,200+ URL citations and decision reports. | Identify a specific buyer workflow where our provenance/falsification layer changes an actual decision. |
| A-04 | Users will trust an automated decision engine with GO/PIVOT/KILL output. | UNPROVEN | Existing venture-studio products explicitly retain human approval gates; Sullis and VEYTR position AI as decision support rather than autonomous final authority. | Human-in-the-loop acceptance evidence and outcome calibration. |
| A-05 | Better decision quality has measurable economic value. | PLAUSIBLE / UNPROVEN | Venture studios explicitly tie validation to capital/resource allocation, but this does not prove external WTP. | Quantified avoided loss / faster screening / better portfolio allocation. |
| A-06 | A standalone product can beat internal workflows. | UNPROVEN | Teams can use spreadsheets, Notion/Confluence, CRM, research tools, LLMs, and internal analyst processes; venture studios already bundle these workflows. | Show recurring labor or decision-risk cost that materially exceeds product cost. |
| A-07 | The market is not already saturated. | CONTRADICTED for generic idea validation | DimeADozen, IdeaProof, GoNoGo, ValidatorAI and others already sell AI validation; new venture-studio operating systems also bundle evaluation and decision gates. | Only a narrow differentiated wedge could survive; must define one explicitly. |
| A-08 | VEDP can become a durable moat. | OPEN / WEAK | Scoring logic is easy to replicate; market competitors already offer evidence-backed analysis. | Demonstrate accumulating data, calibrated predictive performance, workflow lock-in, proprietary distribution, or another durable advantage. |
| A-09 | Historical company outcomes can calibrate the protocol reliably. | UNKNOWN | Success/failure is confounded by timing, execution, capital, luck, and market shocks; hindsight leakage is a serious risk. | Build a dated, leakage-controlled real-company corpus and measure false-GO / false-KILL / false-PIVOT rates. |
| A-10 | The protocol can produce better decisions than a strong human/LLM workflow. | UNKNOWN | Modern LLM research workflows and experienced operators may already perform similar reasoning with lower switching cost. | Controlled comparison on historical cases and blinded decision tasks. |
| A-11 | L5 commercial evidence can be obtained cheaply enough to test the hypothesis. | UNKNOWN | Enterprise/VC workflows can have long sales cycles; low-priced founder validators lower the price ceiling. | At least one credible paid experiment with a defined buyer. |
| A-12 | Protocol generality is an advantage rather than a weakness. | OPEN | Broad products often lose to purpose-built workflow products; current venture-studio systems target specific operational contexts. | Identify repeated workflow across at least two distinct buyer classes without creating generic-feature sprawl. |

## Market boundary evidence

### Generic startup validation is already crowded

DimeADozen currently offers a free idea score, a $9 starter report, a $129 comprehensive report, source-linked research, unit-economics analysis, competitor analysis, and explicit build/don't-build decisions; it states that it has analyzed 100,000+ ideas and serves 3,100+ paying customers. Treat these claims as first-party market evidence, not independent validation.

IdeaProof and GoNoGo also market AI-powered startup idea validation with live/source-based research and paid tiers. This makes a founder-facing generic validator a poor candidate for differentiation.

### Venture-studio operating systems are converging on the same workflow

Venturzs markets structured venture validation, idea scoring, customer discovery, competitive mapping, go/no-go gates, portfolio resource allocation, and venture lifecycle management.

Flora markets venture-studio workspace capabilities including idea validation, deal flow, company formation, dashboards, and command-center orchestration.

Sullis markets intake, AI evaluation, evidence, human review, selection, portfolio management, and a shared decision layer.

VEYTR explicitly markets commercial validation, paid pilots/deposits/pricing tests, human approval gates, evidence verification, and opportunity scoring.

These products materially weaken the thesis that simply wrapping our protocol in a venture workflow UI creates a new category.

## Methodological precedent

Strategyzer's testing methodology independently reinforces several principles in VEDP: define critical hypotheses before building, design tests that can falsify assumptions, measure explicit thresholds, and use evidence to decide whether to continue, pivot, or stop. Therefore, these principles are not proprietary differentiation.

## What remains potentially differentiated

Only a narrower proposition remains worth investigating:

> A machine-checkable evidence and decision-control layer that makes high-stakes opportunity decisions auditable, reproducible, comparable, and calibratable across repeated investment/product-selection workflows.

Even this remains a hypothesis. It must beat existing venture-studio software, diligence platforms, research tools, and internal analyst workflows on a concrete recurring job.

## Falsification plan

The VEDP product hypothesis should be killed if any of the following becomes true:

1. A broadly adopted product already provides the required evidence graph + falsification + decision-state + human approval + historical calibration workflow for the intended buyer.
2. Buyers report that existing tools and analyst workflows are good enough and the incremental value is not budget-worthy.
3. Controlled historical tests show no meaningful improvement over a strong human/LLM baseline.
4. The only viable price point is too low to support acquisition, support, and research costs.
5. The proposed moat reduces to scoring formulas and a UI.

## Current assessment

`VEDP AS A RESEARCH PROTOCOL: PROMISING`

`VEDP AS A STANDALONE BUSINESS: UNPROVEN / DO NOT BUILD YET`

`GENERIC AI STARTUP VALIDATOR: KILL`

## Sources

- https://www.strategyzer.com/library/how-to-test-your-idea-start-with-the-most-critical-hypotheses
- https://www.strategyzer.com/library/validate-your-ideas-with-the-test-card
- https://www.dimeadozen.ai/pricing
- https://www.dimeadozen.ai/startup-idea-validation
- https://www.venturzs.com/
- https://florahq.co/
- https://sullis.ai/venture-studio
- https://www.veytr.com/platform
- https://gonogo.team/blog/startup-idea-validation-tools-2026
- https://ideaproof.io/ai-business-validator-comparison
