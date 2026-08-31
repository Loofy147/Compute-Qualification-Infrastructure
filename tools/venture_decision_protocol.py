#!/usr/bin/env python3
"""Evidence-first Venture Decision Protocol v0.2.

Pipeline:
  evidence -> claim assessment -> hard gates + soft score -> GO/PIVOT/KILL

Design rules:
- Evidence is input; the engine never upgrades evidence by belief.
- Confidence is derived from evidence level, source independence, and falsification state.
- Unknown is not pass.
- Hard gates cannot be rescued by a high weighted score.
- WTP requires commercial evidence, not interest or hypothetical pricing.
- Economic inputs preserve their provenance (observed/calculated/scenario/assumption).
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any


WEIGHTS = {
    "PAIN": 0.12,
    "BUYER": 0.08,
    "GAP": 0.10,
    "ALTERNATIVE_ATTACK": 0.10,
    "ECONOMIC_PROOF": 0.15,
    "MOAT": 0.12,
    "TECHNICAL_PROOF": 0.10,
    "WTP": 0.15,
    "RED_TEAM": 0.08,
}
assert abs(sum(WEIGHTS.values()) - 1.0) < 1e-9

GO_THRESHOLD = 75.0
PIVOT_FLOOR = 50.0
MIN_GATE_SCORE = 0.60
MIN_REDTEAM_COVERAGE = 0.70

CRITICAL_GATES = {
    "PAIN",
    "BUYER",
    "GAP",
    "ECONOMIC_PROOF",
    "WTP",
    "LEGAL",
}


class EvidenceLevel(int, Enum):
    CLAIM = 0
    PRIMARY_DOCUMENTATION = 1
    PUBLIC_ARTIFACT = 2
    INDEPENDENT_TECHNICAL = 3
    CUSTOMER_PRODUCTION = 4
    COMMERCIAL_TRANSACTION = 5


class Basis(str, Enum):
    OBSERVED = "OBSERVED"
    CALCULATED = "CALCULATED"
    SCENARIO = "SCENARIO"
    ASSUMPTION = "ASSUMPTION"


@dataclass(frozen=True)
class Evidence:
    id: str
    source: str
    source_type: str
    evidence_level: int
    independence_group: str
    detail: str
    observed_at: str | None = None


@dataclass(frozen=True)
class Falsification:
    test: str
    attempted: bool
    result: str


@dataclass(frozen=True)
class Claim:
    id: str
    pillar: str
    statement: str
    evidence: tuple[Evidence, ...]
    falsification: Falsification


@dataclass(frozen=True)
class EconomicInput:
    value: float
    basis: Basis
    source: str = ""
    notes: str = ""


@dataclass(frozen=True)
class Economics:
    cac: EconomicInput | None
    ltv: EconomicInput | None
    gross_margin_pct: EconomicInput | None
    payback_months: EconomicInput | None

    @property
    def ltv_cac(self) -> float | None:
        if self.cac is None or self.ltv is None or self.cac.value <= 0:
            return None
        return self.ltv.value / self.cac.value


@dataclass(frozen=True)
class Legal:
    status: str
    jurisdictions: tuple[str, ...] = ()
    scope: tuple[str, ...] = ()
    evidence: tuple[str, ...] = ()
    rationale: str = ""


@dataclass(frozen=True)
class Opportunity:
    id: str
    name: str
    claim: str
    claims: tuple[Claim, ...]
    economics: Economics
    legal: Legal


@dataclass
class PillarResult:
    pillar: str
    score: float
    gate_pass: bool | None
    notes: list[str] = field(default_factory=list)


@dataclass
class Verdict:
    decision: str
    total_score: float
    hard_gate_failures: list[str]
    pillar_results: list[PillarResult]
    rationale: list[str]


def validate_falsification(f: Falsification) -> None:
    if not f.test.strip():
        raise ValueError("falsification.test must be non-empty")
    if not f.attempted and f.result != "NOT_TESTED":
        raise ValueError("falsification.result must be NOT_TESTED when attempted=false")
    if f.attempted and f.result == "NOT_TESTED":
        raise ValueError("falsification.result cannot be NOT_TESTED when attempted=true")


def validate_evidence(e: Evidence) -> None:
    if not e.id or not e.source or not e.detail or not e.independence_group:
        raise ValueError(f"evidence {e.id!r} is missing required fields")
    if not 0 <= e.evidence_level <= 5:
        raise ValueError(f"evidence {e.id!r}: evidence_level must be 0..5")


def _claim_strength(c: Claim) -> float:
    if not c.evidence:
        return 0.0
    for e in c.evidence:
        validate_evidence(e)
    validate_falsification(c.falsification)

    # Evidence quality is capped when the claim has never been falsification-tested.
    best_level = max(e.evidence_level for e in c.evidence)
    independent = len({e.independence_group for e in c.evidence})
    diversity_bonus = min(1.0, independent / 2.0)
    level_score = best_level / 5.0
    falsification_factor = {
        "SURVIVED": 1.0,
        "INCONCLUSIVE": 0.55,
        "FALSIFIED": 0.0,
        "NOT_TESTED": 0.60,
    }[c.falsification.result]
    return max(0.0, min(1.0, (0.70 * level_score + 0.30 * diversity_bonus) * falsification_factor))


def _pillar_claims(opp: Opportunity, pillar: str) -> list[Claim]:
    return [c for c in opp.claims if c.pillar == pillar]


def score_pillar(opp: Opportunity, pillar: str) -> PillarResult:
    claims = _pillar_claims(opp, pillar)
    if not claims:
        return PillarResult(pillar, 0.0, False if pillar in CRITICAL_GATES else None, ["no claims supplied"])

    values = [_claim_strength(c) for c in claims]
    score = sum(values) / len(values)
    notes = [f"{c.id}: strength={_claim_strength(c):.2f}" for c in claims]
    gate = score >= MIN_GATE_SCORE if pillar in CRITICAL_GATES else None
    if gate is False:
        notes.append(f"GATE FAIL: pillar score {score:.2f} < {MIN_GATE_SCORE:.2f}")
    return PillarResult(pillar, score, gate, notes)


def score_alternative_attack(opp: Opportunity) -> PillarResult:
    required = {"direct_competitor", "internal_build", "status_quo", "adjacent_platform"}
    claims = _pillar_claims(opp, "ALTERNATIVE_ATTACK")
    covered = {
        c.statement.strip().lower()
        for c in claims
    }
    # A structured claim may state its class at the start: [internal_build] ...
    classes = set()
    for c in claims:
        prefix = c.statement.split(" ", 1)[0].strip().lower()
        if prefix.startswith("[") and prefix.endswith("]"):
            classes.add(prefix[1:-1])
    coverage = len(classes & required) / len(required)
    base = sum(_claim_strength(c) for c in claims) / len(claims) if claims else 0.0
    score = 0.5 * base + 0.5 * coverage
    gate = coverage == 1.0 and base >= MIN_GATE_SCORE
    notes = [f"alternative classes covered: {sorted(classes & required)}"]
    notes.append(f"class coverage={coverage:.2f}, evidence strength={base:.2f}")
    if not gate:
        notes.append("GATE FAIL: attack must cover direct competitor, internal build, status quo, and adjacent platform with adequate evidence")
    return PillarResult("ALTERNATIVE_ATTACK", min(1.0, score), gate, notes)


def score_economics(opp: Opportunity) -> PillarResult:
    ratio = opp.economics.ltv_cac
    notes: list[str] = []
    if ratio is None:
        return PillarResult("ECONOMIC_PROOF", 0.0, False, ["GATE FAIL: LTV:CAC cannot be calculated from supplied inputs"])
    notes.append(f"LTV:CAC={ratio:.2f}")
    # The ratio is only one component; observed/calculated values get more trust than scenarios.
    provenance = []
    for item in (opp.economics.cac, opp.economics.ltv):
        provenance.append(1.0 if item and item.basis in {Basis.OBSERVED, Basis.CALCULATED} else 0.5)
    prov = sum(provenance) / len(provenance)
    ratio_score = min(1.0, ratio / 3.0)
    score = ratio_score * prov
    gate = ratio >= 1.0 and prov >= 0.5
    if not gate:
        notes.append("GATE FAIL: economics are either structurally weak or insufficiently grounded")
    return PillarResult("ECONOMIC_PROOF", score, gate, notes)


def score_wtp(opp: Opportunity) -> PillarResult:
    claims = _pillar_claims(opp, "WTP")
    if not claims:
        return PillarResult("WTP", 0.0, False, ["GATE FAIL: no WTP evidence"])
    commercial = [c for c in claims if any(e.evidence_level == EvidenceLevel.COMMERCIAL_TRANSACTION for e in c.evidence)]
    score = sum(_claim_strength(c) for c in claims) / len(claims)
    gate = bool(commercial) and score >= MIN_GATE_SCORE
    notes = [f"commercial-transaction claims={len(commercial)}", f"overall WTP strength={score:.2f}"]
    if not gate:
        notes.append("GATE FAIL: WTP requires direct commercial evidence; interest/LOI-only claims are insufficient for GO")
    return PillarResult("WTP", score, gate, notes)


def score_red_team(opp: Opportunity) -> PillarResult:
    critical = [c for c in opp.claims if c.pillar in {"PAIN", "BUYER", "GAP", "MOAT", "TECHNICAL_PROOF", "WTP"}]
    if not critical:
        return PillarResult("RED_TEAM", 0.0, None, ["no claims to test"])
    tested = [c for c in critical if c.falsification.attempted]
    survived = [c for c in tested if c.falsification.result == "SURVIVED"]
    falsified = [c for c in tested if c.falsification.result == "FALSIFIED"]
    coverage = len(tested) / len(critical)
    survival = len(survived) / len(tested) if tested else 0.0
    score = 0.5 * coverage + 0.5 * survival
    notes = [f"coverage={coverage:.2f}", f"survival={survival:.2f}", f"falsified={len(falsified)}"]
    if falsified:
        notes.append("falsified claims reduce the score to zero for those claims")
    return PillarResult("RED_TEAM", score, None, notes)


def score_legal(opp: Opportunity) -> PillarResult:
    status = opp.legal.status
    passed = status in {"ASSESSED_CLEAR", "NOT_APPLICABLE"}
    score = 1.0 if passed else 0.0
    notes = [f"legal status={status}"]
    if not passed:
        notes.append("GATE FAIL: legal/regulatory status is unresolved or blocked")
    return PillarResult("LEGAL", score, passed, notes)


def decide(opp: Opportunity) -> Verdict:
    results = [
        score_pillar(opp, "PAIN"),
        score_pillar(opp, "BUYER"),
        score_pillar(opp, "GAP"),
        score_alternative_attack(opp),
        score_economics(opp),
        score_pillar(opp, "MOAT"),
        score_pillar(opp, "TECHNICAL_PROOF"),
        score_wtp(opp),
        score_red_team(opp),
        score_legal(opp),
    ]
    by_name = {r.pillar: r for r in results}

    total = sum(WEIGHTS[p] * by_name[p].score for p in WEIGHTS)
    total_pct = round(total * 100.0, 1)
    failures = sorted(p for p in CRITICAL_GATES if by_name[p].gate_pass is False)

    rationale: list[str] = []
    if len([p for p in failures if p in {"PAIN", "BUYER", "GAP", "ECONOMIC_PROOF", "WTP"}]) >= 2:
        decision = "KILL"
        rationale.append("multiple critical commercial gates failed simultaneously")
    elif failures:
        decision = "PIVOT"
        rationale.append("one or more critical gates failed; current formulation is not GO-ready")
    elif total_pct >= GO_THRESHOLD and by_name["RED_TEAM"].score >= MIN_REDTEAM_COVERAGE:
        decision = "GO"
        rationale.append(f"all critical gates pass; score {total_pct}/100 and red-team coverage is adequate")
    elif total_pct >= PIVOT_FLOOR:
        decision = "PIVOT"
        rationale.append(f"gates pass but score {total_pct}/100 is below GO threshold or red-team evidence is insufficient")
    else:
        decision = "KILL"
        rationale.append(f"score {total_pct}/100 is below the PIVOT floor")

    if by_name["RED_TEAM"].score < MIN_REDTEAM_COVERAGE:
        rationale.append("red-team coverage is below the required threshold")

    return Verdict(decision, total_pct, failures, results, rationale)


def _economic_input(value: Any) -> EconomicInput | None:
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ValueError("economic inputs must be objects or null")
    return EconomicInput(
        value=float(value["value"]),
        basis=Basis(str(value["basis"]).upper()),
        source=str(value.get("source", "")),
        notes=str(value.get("notes", "")),
    )


def _parse_evidence(d: dict) -> Evidence:
    return Evidence(
        id=str(d["id"]),
        source=str(d["source"]),
        source_type=str(d["source_type"]),
        evidence_level=int(d["evidence_level"]),
        independence_group=str(d["independence_group"]),
        detail=str(d["detail"]),
        observed_at=d.get("observed_at"),
    )


def _parse_claim(d: dict) -> Claim:
    f_raw = d["falsification"]
    claim = Claim(
        id=str(d["id"]),
        pillar=str(d["pillar"]).upper(),
        statement=str(d["statement"]),
        evidence=tuple(_parse_evidence(x) for x in d.get("evidence", [])),
        falsification=Falsification(
            test=str(f_raw["test"]),
            attempted=bool(f_raw["attempted"]),
            result=str(f_raw["result"]).upper(),
        ),
    )
    validate_falsification(claim.falsification)
    return claim


def load_case(path: Path) -> Opportunity:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if raw.get("schema_version") != "0.2":
        raise ValueError("schema_version must be '0.2'")
    o = raw["opportunity"]
    e = raw["economics"]
    l = raw["legal"]
    return Opportunity(
        id=str(o["id"]),
        name=str(o["name"]),
        claim=str(o["claim"]),
        claims=tuple(_parse_claim(x) for x in raw.get("claims", [])),
        economics=Economics(
            cac=_economic_input(e.get("cac")),
            ltv=_economic_input(e.get("ltv")),
            gross_margin_pct=_economic_input(e.get("gross_margin_pct")),
            payback_months=_economic_input(e.get("payback_months")),
        ),
        legal=Legal(
            status=str(l["status"]).upper(),
            jurisdictions=tuple(l.get("jurisdictions", [])),
            scope=tuple(l.get("scope", [])),
            evidence=tuple(l.get("evidence", [])),
            rationale=str(l.get("rationale", "")),
        ),
    )


def blank_template() -> dict:
    return {
        "schema_version": "0.2",
        "opportunity": {"id": "opp-001", "name": "", "claim": ""},
        "claims": [
            {
                "id": "pain-001",
                "pillar": "PAIN",
                "statement": "",
                "evidence": [
                    {
                        "id": "ev-001",
                        "source": "",
                        "source_type": "CUSTOMER",
                        "evidence_level": 4,
                        "independence_group": "customer-001",
                        "detail": "",
                        "observed_at": ""
                    }
                ],
                "falsification": {
                    "test": "",
                    "attempted": False,
                    "result": "NOT_TESTED"
                }
            }
        ],
        "economics": {
            "cac": None,
            "ltv": None,
            "gross_margin_pct": None,
            "payback_months": None
        },
        "legal": {
            "status": "NOT_ASSESSED",
            "jurisdictions": [],
            "scope": [],
            "evidence": [],
            "rationale": ""
        }
    }


def synthetic_cases() -> list[tuple[str, Opportunity, str]]:
    def ev(i: str, level: int, group: str = "independent") -> Evidence:
        return Evidence(i, "synthetic", "OTHER", level, group, "synthetic self-test evidence")
    def c(i: str, pillar: str, level: int, result: str = "SURVIVED", attempted: bool = True) -> Claim:
        return Claim(i, pillar, "synthetic claim", (ev(i + "-ev", level),), Falsification("synthetic break test", attempted, result))

    go = Opportunity(
        "go", "SYNTHETIC-GO", "synthetic", tuple(
            [c("p","PAIN",4), c("b","BUYER",4), c("g","GAP",4),
             c("a1","ALTERNATIVE_ATTACK",4), c("a2","ALTERNATIVE_ATTACK",4),
             c("a3","ALTERNATIVE_ATTACK",4), c("a4","ALTERNATIVE_ATTACK",4),
             c("m","MOAT",4), c("t","TECHNICAL_PROOF",4),
             c("w","WTP",5)]),
        Economics(EconomicInput(100, Basis.OBSERVED), EconomicInput(500, Basis.OBSERVED), None, None),
        Legal("ASSESSED_CLEAR"))
    # Tag alternatives with required coverage classes.
    alt_classes = ["direct_competitor", "internal_build", "status_quo", "adjacent_platform"]
    go.claims = tuple(
        Claim(x.id, x.pillar, f"[{alt_classes[j]}] synthetic alternative" if x.pillar == "ALTERNATIVE_ATTACK" else x.statement, x.evidence, x.falsification)
        for j, x in enumerate(go.claims)
    )

    pivot = Opportunity(
        "pivot", "SYNTHETIC-PIVOT", "synthetic", tuple(
            [c("p","PAIN",3), c("b","BUYER",3), c("g","GAP",2), c("m","MOAT",2), c("t","TECHNICAL_PROOF",4), c("w","WTP",5)]),
        Economics(EconomicInput(100, Basis.OBSERVED), EconomicInput(250, Basis.SCENARIO), None, None),
        Legal("ASSESSED_CLEAR"))
    kill = Opportunity(
        "kill", "SYNTHETIC-KILL", "synthetic", tuple(),
        Economics(None, None, None, None), Legal("NOT_ASSESSED"))
    return [("GO", go, "GO"), ("PIVOT", pivot, "PIVOT"), ("KILL", kill, "KILL")]


def report(v: Verdict) -> str:
    lines = [f"DECISION: {v.decision}", f"WEIGHTED SCORE: {v.total_score}/100"]
    if v.hard_gate_failures:
        lines.append("HARD GATE FAILURES: " + ", ".join(v.hard_gate_failures))
    for r in v.pillar_results:
        gate = "" if r.gate_pass is None else (" PASS" if r.gate_pass else " FAIL")
        lines.append(f"{r.pillar}: {r.score * 100:.1f}/100{gate}")
        lines.extend(f"  - {n}" for n in r.notes)
    lines.append("RATIONALE:")
    lines.extend(f"  - {x}" for x in v.rationale)
    return "\n".join(lines)


def run_selftest() -> bool:
    ok = True
    for label, opp, expected in synthetic_cases():
        actual = decide(opp).decision
        passed = actual == expected
        ok = ok and passed
        print(f"[SELF-TEST] {label}: expected={expected}, got={actual} -> {'PASS' if passed else 'FAIL'}")
    # Invariant: no evidence must never reach GO.
    empty = synthetic_cases()[-1][1]
    assert decide(empty).decision != "GO"
    return ok


def main() -> None:
    p = argparse.ArgumentParser(description="Evidence-first Venture Decision Protocol v0.2")
    p.add_argument("input", nargs="?", help="JSON evidence case")
    p.add_argument("--selftest", action="store_true")
    p.add_argument("--template", action="store_true")
    args = p.parse_args()

    if args.template:
        print(json.dumps(blank_template(), indent=2))
        return
    if args.selftest or not args.input:
        sys.exit(0 if run_selftest() else 1)
    try:
        verdict = decide(load_case(Path(args.input)))
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(2)
    print(report(verdict))


if __name__ == "__main__":
    main()
