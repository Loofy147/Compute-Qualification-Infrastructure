#!/usr/bin/env python3
"""Evidence-first Venture Decision Protocol v0.2.

Input: a claim/evidence case. Output: deterministic GO/PIVOT/KILL assessment.
The engine never treats self-reported confidence as proof.
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
CRITICAL_GATES = {"PAIN", "BUYER", "GAP", "ECONOMIC_PROOF", "WTP", "LEGAL"}
ALTERNATIVE_CLASSES = {"direct_competitor", "internal_build", "status_quo", "adjacent_platform"}


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
        raise ValueError("result must be NOT_TESTED when attempted=false")
    if f.attempted and f.result not in {"SURVIVED", "FALSIFIED", "INCONCLUSIVE"}:
        raise ValueError("result must be SURVIVED, FALSIFIED, or INCONCLUSIVE when attempted=true")


def validate_evidence(e: Evidence) -> None:
    if not e.id or not e.source or not e.detail or not e.independence_group:
        raise ValueError(f"evidence {e.id!r} is missing required fields")
    if not 0 <= e.evidence_level <= 5:
        raise ValueError(f"evidence {e.id!r}: evidence_level must be 0..5")


def _claim_strength(c: Claim) -> float:
    validate_falsification(c.falsification)
    if not c.evidence:
        return 0.0
    for e in c.evidence:
        validate_evidence(e)
    level_score = max(e.evidence_level for e in c.evidence) / 5.0
    diversity = min(1.0, len({e.independence_group for e in c.evidence}) / 2.0)
    falsification_factor = {"SURVIVED": 1.0, "INCONCLUSIVE": 0.55, "FALSIFIED": 0.0, "NOT_TESTED": 0.60}[c.falsification.result]
    return max(0.0, min(1.0, (0.70 * level_score + 0.30 * diversity) * falsification_factor))


def _claims(opp: Opportunity, pillar: str) -> list[Claim]:
    return [c for c in opp.claims if c.pillar == pillar]


def score_pillar(opp: Opportunity, pillar: str) -> PillarResult:
    claims = _claims(opp, pillar)
    if not claims:
        return PillarResult(pillar, 0.0, False if pillar in CRITICAL_GATES else None, ["no claims supplied"])
    vals = [_claim_strength(c) for c in claims]
    score = sum(vals) / len(vals)
    gate = score >= MIN_GATE_SCORE if pillar in CRITICAL_GATES else None
    notes = [f"{c.id}: strength={_claim_strength(c):.2f}" for c in claims]
    if gate is False:
        notes.append(f"GATE FAIL: {score:.2f} < {MIN_GATE_SCORE:.2f}")
    return PillarResult(pillar, score, gate, notes)


def score_alternative_attack(opp: Opportunity) -> PillarResult:
    claims = _claims(opp, "ALTERNATIVE_ATTACK")
    classes: set[str] = set()
    for c in claims:
        token = c.statement.split(" ", 1)[0].strip().lower()
        if token.startswith("[") and token.endswith("]"):
            classes.add(token[1:-1])
    base = sum(_claim_strength(c) for c in claims) / len(claims) if claims else 0.0
    coverage = len(classes & ALTERNATIVE_CLASSES) / len(ALTERNATIVE_CLASSES)
    score = 0.5 * base + 0.5 * coverage
    gate = coverage == 1.0 and base >= MIN_GATE_SCORE
    notes = [f"coverage={coverage:.2f}", f"evidence_strength={base:.2f}", f"classes={sorted(classes & ALTERNATIVE_CLASSES)}"]
    if not gate:
        notes.append("GATE FAIL: cover direct competitor, internal build, status quo, and adjacent platform")
    return PillarResult("ALTERNATIVE_ATTACK", score, gate, notes)


def score_economics(opp: Opportunity) -> PillarResult:
    ratio = opp.economics.ltv_cac
    if ratio is None:
        return PillarResult("ECONOMIC_PROOF", 0.0, False, ["GATE FAIL: LTV:CAC unavailable"])
    bases = [opp.economics.cac.basis, opp.economics.ltv.basis]
    provenance = sum(b in {Basis.OBSERVED, Basis.CALCULATED} for b in bases) / 2.0
    score = min(1.0, ratio / 3.0) * (0.5 + 0.5 * provenance)
    gate = ratio >= 1.0 and provenance >= 0.5
    notes = [f"LTV:CAC={ratio:.2f}", f"provenance={provenance:.2f}"]
    if not gate:
        notes.append("GATE FAIL: economics structurally weak or insufficiently grounded")
    return PillarResult("ECONOMIC_PROOF", score, gate, notes)


def score_wtp(opp: Opportunity) -> PillarResult:
    claims = _claims(opp, "WTP")
    if not claims:
        return PillarResult("WTP", 0.0, False, ["GATE FAIL: no WTP evidence"])
    commercial = [c for c in claims if any(e.evidence_level == 5 for e in c.evidence)]
    score = sum(_claim_strength(c) for c in claims) / len(claims)
    gate = bool(commercial) and score >= MIN_GATE_SCORE
    notes = [f"commercial_transaction_claims={len(commercial)}", f"strength={score:.2f}"]
    if not gate:
        notes.append("GATE FAIL: GO requires direct commercial transaction evidence")
    return PillarResult("WTP", score, gate, notes)


def score_red_team(opp: Opportunity) -> PillarResult:
    relevant = [c for c in opp.claims if c.pillar != "LEGAL"]
    if not relevant:
        return PillarResult("RED_TEAM", 0.0, None, ["no claims to test"])
    tested = [c for c in relevant if c.falsification.attempted]
    survived = [c for c in tested if c.falsification.result == "SURVIVED"]
    falsified = [c for c in tested if c.falsification.result == "FALSIFIED"]
    coverage = len(tested) / len(relevant)
    survival = len(survived) / len(tested) if tested else 0.0
    return PillarResult("RED_TEAM", 0.5 * coverage + 0.5 * survival, None, [f"coverage={coverage:.2f}", f"survival={survival:.2f}", f"falsified={len(falsified)}"])


def score_legal(opp: Opportunity) -> PillarResult:
    passed = opp.legal.status in {"ASSESSED_CLEAR", "NOT_APPLICABLE"}
    return PillarResult("LEGAL", 1.0 if passed else 0.0, passed, [f"status={opp.legal.status}"] + ([] if passed else ["GATE FAIL: legal/regulatory status unresolved or blocked"]))


def decide(opp: Opportunity) -> Verdict:
    results = [
        score_pillar(opp, "PAIN"), score_pillar(opp, "BUYER"), score_pillar(opp, "GAP"),
        score_alternative_attack(opp), score_economics(opp), score_pillar(opp, "MOAT"),
        score_pillar(opp, "TECHNICAL_PROOF"), score_wtp(opp), score_red_team(opp), score_legal(opp),
    ]
    by = {r.pillar: r for r in results}
    total = round(sum(WEIGHTS[k] * by[k].score for k in WEIGHTS) * 100.0, 1)
    failures = sorted(k for k in CRITICAL_GATES if by[k].gate_pass is False)
    commercial_failures = {"PAIN", "BUYER", "GAP", "ECONOMIC_PROOF", "WTP"} & set(failures)
    rationale: list[str] = []
    if len(commercial_failures) >= 2:
        decision = "KILL"
        rationale.append("multiple critical commercial gates failed")
    elif failures:
        decision = "PIVOT"
        rationale.append("critical gate failure prevents GO")
    elif total >= GO_THRESHOLD and by["RED_TEAM"].score >= MIN_REDTEAM_COVERAGE:
        decision = "GO"
        rationale.append("all critical gates pass and evidence survived adequate red-team coverage")
    elif total >= PIVOT_FLOOR:
        decision = "PIVOT"
        rationale.append("gates pass but evidence is not strong enough for GO")
    else:
        decision = "KILL"
        rationale.append("weighted score below pivot floor")
    if by["RED_TEAM"].score < MIN_REDTEAM_COVERAGE:
        rationale.append("red-team coverage is below required threshold")
    return Verdict(decision, total, failures, results, rationale)


def _economic_input(value: Any) -> EconomicInput | None:
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ValueError("economic input must be object or null")
    return EconomicInput(float(value["value"]), Basis(str(value["basis"]).upper()), str(value.get("source", "")), str(value.get("notes", "")))


def load_case(path: Path) -> Opportunity:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if raw.get("schema_version") != "0.2":
        raise ValueError("schema_version must be '0.2'")
    o, e, l = raw["opportunity"], raw["economics"], raw["legal"]
    return Opportunity(str(o["id"]), str(o["name"]), str(o["claim"]), tuple(_parse_claim(x) for x in raw.get("claims", [])), Economics(_economic_input(e.get("cac")), _economic_input(e.get("ltv")), _economic_input(e.get("gross_margin_pct")), _economic_input(e.get("payback_months"))), Legal(str(l["status"]).upper(), tuple(l.get("jurisdictions", [])), tuple(l.get("scope", [])), tuple(l.get("evidence", [])), str(l.get("rationale", ""))))


def _parse_claim(d: dict) -> Claim:
    f = d["falsification"]
    return Claim(str(d["id"]), str(d["pillar"]).upper(), str(d["statement"]), tuple(_parse_evidence(e) for e in d.get("evidence", [])), Falsification(str(f["test"]), bool(f["attempted"]), str(f["result"]).upper()))


def _parse_evidence(d: dict) -> Evidence:
    return Evidence(str(d["id"]), str(d["source"]), str(d["source_type"]), int(d["evidence_level"]), str(d["independence_group"]), str(d["detail"]), d.get("observed_at"))


def blank_template() -> dict:
    return {"schema_version": "0.2", "opportunity": {"id": "opp-001", "name": "", "claim": ""}, "claims": [], "economics": {"cac": None, "ltv": None, "gross_margin_pct": None, "payback_months": None}, "legal": {"status": "NOT_ASSESSED", "jurisdictions": [], "scope": [], "evidence": [], "rationale": ""}}


def _ev(i: str, level: int, group: str = "g") -> Evidence:
    return Evidence(i, "synthetic", "OTHER", level, group, "synthetic evidence")


def _cl(i: str, pillar: str, level: int, result: str = "SURVIVED") -> Claim:
    return Claim(i, pillar, "synthetic claim", (_ev(i + "-ev", level),), Falsification("synthetic break test", True, result))


def synthetic_cases() -> list[tuple[str, Opportunity, str]]:
    alt = [Claim(f"a{j}", "ALTERNATIVE_ATTACK", f"[{kind}] synthetic alternative", (_ev(f"a{j}-ev", 4),), Falsification("synthetic break test", True, "SURVIVED")) for j, kind in enumerate(sorted(ALTERNATIVE_CLASSES))]
    go = Opportunity("go", "SYNTHETIC-GO", "synthetic", tuple([_cl("p", "PAIN", 4), _cl("b", "BUYER", 4), _cl("g", "GAP", 4), *alt, _cl("m", "MOAT", 4), _cl("t", "TECHNICAL_PROOF", 4), _cl("w", "WTP", 5)]), Economics(EconomicInput(100, Basis.OBSERVED), EconomicInput(500, Basis.OBSERVED), None, None), Legal("ASSESSED_CLEAR"))
    pivot = Opportunity("pivot", "SYNTHETIC-PIVOT", "synthetic", (_cl("p", "PAIN", 3), _cl("b", "BUYER", 3), _cl("g", "GAP", 2), _cl("m", "MOAT", 2), _cl("t", "TECHNICAL_PROOF", 4), _cl("w", "WTP", 5)), Economics(EconomicInput(100, Basis.OBSERVED), EconomicInput(250, Basis.SCENARIO), None, None), Legal("ASSESSED_CLEAR"))
    kill = Opportunity("kill", "SYNTHETIC-KILL", "synthetic", tuple(), Economics(None, None, None, None), Legal("NOT_ASSESSED"))
    return [("GO", go, "GO"), ("PIVOT", pivot, "PIVOT"), ("KILL", kill, "KILL")]


def run_selftest() -> bool:
    ok = True
    for label, opp, expected in synthetic_cases():
        got = decide(opp).decision
        passed = got == expected
        ok &= passed
        print(f"[SELF-TEST] {label}: expected={expected}, got={got} -> {'PASS' if passed else 'FAIL'}")
    invalid = Falsification("invalid", False, "SURVIVED")
    try:
        validate_falsification(invalid)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid falsification state accepted")
    assert decide(synthetic_cases()[-1][1]).decision != "GO"
    return ok


def main() -> None:
    p = argparse.ArgumentParser(description="Evidence-first Venture Decision Protocol v0.2")
    p.add_argument("input", nargs="?")
    p.add_argument("--selftest", action="store_true")
    p.add_argument("--template", action="store_true")
    args = p.parse_args()
    if args.template:
        print(json.dumps(blank_template(), indent=2))
        return
    if args.selftest or not args.input:
        sys.exit(0 if run_selftest() else 1)
    try:
        print(report(decide(load_case(Path(args.input)))))
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(2)


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


if __name__ == "__main__":
    main()
