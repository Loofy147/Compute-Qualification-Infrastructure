# Commercial Evidence Matrix

Status: working research artifact. Scores must not be interpreted as validated WTP.

## Qualification

- `E`: established by primary/strong evidence
- `S`: strong market signal
- `H`: hypothesis requiring direct validation
- `U`: unknown

## Initial Workflow Matrix

| ID | Workflow | Primary Buyer | Current Alternatives | Pain | Gap | Economic Value | WTP | Priority |
|---|---|---|---|---|---|---|---|---:|
| CW-01 | Accelerator procurement / selection | AI infrastructure leadership | RFPs, vendor benchmarks, internal PoCs, consultants | High | S/H | High | H | 5 |
| CW-02 | GPU → ASIC workload migration qualification | AI platform / infra | Vendor SDKs, porting scripts, manual validation | High | S | High | H | 5 |
| CW-03 | Production acceptance testing | Enterprise AI platform | Manual acceptance tests, vendor reports | High | S | High | H | 5 |
| CW-04 | Accelerator TCO comparison | Infrastructure + finance | Spreadsheets, benchmark reports, consultants | High | S | High | H | 5 |
| CW-05 | Power / energy qualification | Data center / infra | MLPerf Power, vendor tooling, bespoke measurement | Medium/High | S | High | H | 4 |
| CW-06 | Compiler/runtime regression qualification | Platform engineering | CI, custom benchmarks, vendor tools | High | S | High | H | 4 |
| CW-07 | Driver/firmware/software-stack regression | Infrastructure engineering | Compatibility matrices, CI, vendor tooling | High | S | Medium/High | H | 4 |
| CW-08 | Agentic workload qualification | AI infrastructure | AA-AgentPerf, InferenceX, custom workloads | High | S | High | H | 5 |
| CW-09 | Heterogeneous pipeline qualification | AI infrastructure | Internal tooling, vendor stack | Very High | S | Very High | H | 5 |
| CW-10 | Production deployment gate | ML/AI platform | Manual checklists, CI/CD, observability | High | S/H | High | H | 5 |
| CW-11 | Hardware refresh decision | CIO/CTO/infra | RFP + spreadsheet + PoC | Medium/High | S | High | H | 4 |
| CW-12 | Partner interoperability validation | Hardware/software vendor | Bilateral testing | Medium/High | S | Medium/High | H | 4 |
| CW-13 | Independent customer-facing certification | Accelerator vendor / cloud | Vendor benchmark + third-party consulting | Medium/High | H/S | High | H | 4 |
| CW-14 | Pre-silicon → silicon correlation | Semiconductor engineering | Internal simulation/validation | Very High | S | Very High | H | 4 |
| CW-15 | Continuous historical requalification | AI platform / infra | Dashboards, CI, benchmark archives | High | S/H | High | H | 5 |

## Current Research Conclusion

The strongest candidate wedges are:

1. **CW-01 Accelerator Procurement Qualification**
2. **CW-03 Production Acceptance / Qualification**
3. **CW-15 Continuous Requalification**

These may be one lifecycle rather than three separate products:

`SELECT → QUALIFY → DEPLOY → CHANGE → REQUALIFY`

## Commercial Questions That Must Be Answered

For every high-priority workflow, research must establish:

- Who experiences the pain?
- Who owns the budget?
- What triggers the workflow?
- How often does it occur?
- How many engineering hours are spent?
- Which tools are used today?
- What remains manual?
- What evidence is produced?
- What decisions depend on that evidence?
- What happens when the decision is wrong?
- What is the measurable economic impact?
- Would a buyer pay for external neutrality, speed, reproducibility, or reduced risk?

## WTP Standard

The following are not sufficient proof of WTP:

- market size;
- vendor claims;
- investor funding;
- positive interviews without commitment;
- technical interest;
- free pilot usage.

Strong WTP evidence includes:

- paid discovery;
- paid qualification engagement;
- paid pilot;
- purchase order;
- signed commercial commitment;
- measurable renewal/expansion.

## Research Rule

Do not aggregate all evidence into a single positive narrative. Record positive, negative, and contradictory evidence for each workflow.
