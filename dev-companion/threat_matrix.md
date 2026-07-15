# Threat matrix + verification blueprints — XSI-AIMS developer companion

> Verified against XSI-AIMS v2.1.2. Illustrative; the specification is the contract.

## Deterministic Ratification Gate (Principle 4)

No inference component executes an authority-bearing consequence unilaterally. A
proposal is ratified by a deterministic component first; a rigid function is
formally verified *where the property admits a proof*, and adversarial fuzzing
covers what isn't provable.

```
  [ Inference Stratum Proposal ]
                |
                v
  [ Deterministic Ratification Gate ]
                |
        +-------+-------+
        v               v
 [ Formal Proof ]   [ Continuous Fuzzing ]
 (where provable)    (where non-provable)
        |               |
        +-------+-------+
                v
      [ Enforcer Substrate ] --(if refused)--> [ Veto Rejection witnessed ]
                |
          (if ratified)
                v
   [ Execute authority consequence ]
```

## The T1-T9 threat matrix (corrected)

The T1-T9 axis names *who or what originates* a threat (the actor/vector axis);
the *mechanism* an attack uses is a separate A1-A7 technique axis. T8 (internal
AGI emergence) and T9 (substrate compromise) are **not** external threats.

| Threat | Origin | Primary target surface | Verification method | Expected automated outcome |
|---|---|---|---|---|
| T1 | Bad data | Input parsing / rigid functions | Malformed-schema fuzzing | Deterministic REFUSAL at the substrate; no model invocation |
| T2 | Bad human southbound | Southbound gateway edge | Indirect-injection vectors | Content **admitted as data** under a permanent `UNTRUSTED_EXTERNAL` tag; structural surface normalized; never routed as an instruction (it is **not** "stripped") |
| T3 | Malicious user | Session boundary / scope | Authority-escalation probes | Hard-stop at the Sovereign; mandatory `RE_AUTHENTICATION_PENDING` |
| T4 | External AGI southbound | Auxiliary API egress | Manipulation-pattern probes | Token-budget / alignment-anomaly quarantine |
| T5 | User compromised by AGI | Northbound request history | Behavioral-baseline drift scans | Correlated shadow-detection alert over a sustained window |
| T6 | AGI emulating user | Authentication gateway | Credential-replay probing | Cryptographic failure; session invalidated |
| T7 | Coordinated multi-vector | Cross-archetype fabric | Multi-agent composition | Rollback via independent counteragents |
| T8 | Internal AGI emergence | Resident foundation layer | Evaluation-evasion canaries | Out-of-band baseline mismatch → six-stage recovery |
| T9 | Cryptographic substrate compromise | Hardware enclaves / key wraps | Post-quantum + substrate probes | **No single node certifies its own substrate: Byzantine quorum keeps canonical history unrewritable, and cross-foundation attestation surfaces a single-substrate break as correlation deviation.** (Not "firewall the domain" — you can't firewall a broken substrate from itself.) |

## CI / test-automation flow

```
[ commit / scheduled hook ]
          |
          v
[ Formal verification (TLA+/Alloy, where provable) ] --(proof fails)--> [ block deployment ]
          | (properties proven)
          v
[ Adversarial corpus (T1-T9) ] --(canary fails)--> [ log regression case ]
          | (passing)
          v
[ Multi-agent fabric stress (provoke shadows, force heartbeat loss) ]
          |
          v
[ Sign off conformance package ]
```

> **Discipline note:** a failing test blocks *deployment*; it must never
> auto-tighten a *production* threshold. Over-tightening is its own failure mode
> (denial of service / the constraining-pull pathology) — tightening auto-clears
> a human's pre-approval but stays under shadow detection, and a red test is a
> gate on shipping, not a lever that silently reconfigures a running system.
