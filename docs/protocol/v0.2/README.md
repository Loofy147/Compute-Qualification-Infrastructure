# Venture Evidence & Decision Protocol v0.2

## Purpose

This protocol turns venture evaluation into an evidence-gated decision process. It is intentionally conservative and is designed to prevent technical enthusiasm, weak market signals, and unsupported assumptions from becoming a `GO` decision.

## Data flow

```text
Claims
  -> Evidence Records
  -> Falsification State
  -> Claim Strength
  -> Pillar Gates
  -> Weighted Score
  -> GO / PIVOT / KILL
```

## Core design changes from v0.1

1. **Evidence-first:** the input records evidence and provenance rather than a self-declared `PROVEN` confidence value.
2. **Claim-centric:** each claim belongs to a pillar and has its own evidence and falsification test.
3. **Independent evidence:** every evidence record has an `independence_group`, so multiple assertions from one source are not treated as independent corroboration.
4. **Falsification-aware:** a claim cannot silently be marked survived unless a valid falsification state exists.
5. **Hard gates:** Pain, Buyer, Gap, Economics, WTP, and Legal can block `GO` regardless of score.
6. **WTP discipline:** `GO` requires at least one direct commercial-transaction evidence record at level 5.
7. **Economic provenance:** CAC/LTV/etc. carry `OBSERVED`, `CALCULATED`, `SCENARIO`, or `ASSUMPTION` basis.
8. **Alternative attack:** the market attack must explicitly cover direct competitors, internal build, status quo, and adjacent platforms.
9. **Separate red-team metrics:** coverage and survival are both visible rather than collapsing all adversarial evidence into a single opaque confidence field.

## Evidence levels

| Level | Meaning |
|---:|---|
| 0 | Claim / unsupported assertion |
| 1 | Primary documentation |
| 2 | Public reproducible artifact |
| 3 | Independent technical evidence |
| 4 | Customer / production evidence |
| 5 | Commercial transaction / direct WTP evidence |

## Decision rules

`GO` requires:

- all critical gates pass;
- weighted score >= 75/100;
- red-team coverage >= 70%;
- direct commercial evidence exists for WTP.

A failed critical gate yields `PIVOT`, except when at least two major commercial gates fail simultaneously, in which case the engine returns `KILL`.

The thresholds are protocol configuration, not an industry standard. They must be calibrated against a larger adversarial corpus before being treated as mature policy.

## Canonical artifacts

- `evidence-schema.json` — JSON Schema for the evidence case.
- `evidence-case.template.json` — empty case template.
- `../../../../tools/venture_decision_protocol.py` — executable reference implementation.

## Usage

```bash
python tools/venture_decision_protocol.py --template
python tools/venture_decision_protocol.py --selftest
python tools/venture_decision_protocol.py path/to/case.json
```

`--selftest` must remain green before changing protocol semantics.
