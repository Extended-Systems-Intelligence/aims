# XSI-AIMS Developer Companion

Illustrative, scaffolding-level templates that map the XSI-AIMS specification's
requirements to executable shape — for a team standing up a conformant agent
rig. These are *starting points with the correct semantics*, not production
code and not a reference implementation. Method bodies are deliberately left
unimplemented where the concrete work is deployment-specific.

**Verified against:** XSI-AIMS specification release **v2.1.2**
(commit `c125106556a5d1f7e38e38d1bcdc4034d53beaeb`).

Nothing in this directory is normative. Where a template and the specification
appear to diverge, the specification is the contract. Pin the specification
version you build against, exactly as these templates pin theirs.

## Layout

```
dev-companion/
  archetypes/       sovereign.py — Sovereign persistent-substrate + bounded inference workload
                    enforcer.py — K7 Bayesian trust gradient + fail-closed budget gate
                    executor_bridge.py — Bridge-of-Trust dual-enclave crossing (counter-signed handoff)
                    inbound_sanitization.py — untrusted-data admission gate (tag, never "strip")
  schemas/          iame_envelope.schema.json — internal message envelope (JSON Schema)
                    validation_ladder.json — the Enforcer's five-tier crossing-validation config
                    federation_envelope.json — federation treaty contract example
  cluster/          byzantine_participant.py — Cluster Mode BFT bootstrap + quorum-gated commit
                    cross_tenant_isolation.py — the four permitted cross-tenant crossing classes
  workload/         workload_migration.yaml — ten-phase atomic workload-offload profile
  tests/            threat_corpus_tests.py — illustrative T1–T9 assertion scaffolding
  threat_matrix.md  ratification-gate + CI-flow blueprints and the T1–T9 threat matrix
```

## Semantics these templates are careful about

A few points where implementations commonly go wrong, encoded here correctly:

- **Revocation is rejection, not unreadability.** A message signed under a
  revoked credential still verifies as mathematics; receivers reject it because
  the authority chain no longer resolves to a live credential.
- **Inbound external content is admitted as data, never "stripped" safe.**
  Mechanical normalization narrows the structural injection surface only; the
  real defense is the permanent `UNTRUSTED_EXTERNAL` tag and the
  never-treated-as-instruction contract. A pattern match is telemetry, not a gate.
- **The bridge handoff record is dual-signed by both enclaves.** The sender
  signs its side, the receiver counter-signs on receipt; one enclave cannot
  produce a dual signature alone.
- **Internal per-message signatures are the hybrid Ed25519 + ML-DSA-65
  construction** (pure ML-DSA only after the post-2031 transition); SLH-DSA is
  reserved for the external domain's algorithm agility.
- **A CRITICAL trust standing makes an agent a quarantine *candidate*** with an
  immediate Sovereign-mandatory review and ratification-required operation —
  correction before containment, not an automatic hard quarantine.
- **Post-partition queued federation traffic is revalidated against current
  authority before release** — never replayed on pre-partition standing.
- **Byzantine consensus, not crash-fault consensus,** protects the canonical
  Witness chain in Cluster Mode; a two-node "quorum" is an honestly-labeled
  degenerate mode, not Byzantine tolerance.

## Using the tests

`tests/threat_corpus_tests.py` is mock-driven illustration of the intended
failure-grading contracts (hard rejection + trust penalty for a corrupt
signature; soft stale-drop for an expired TTL; admission-as-untrusted for
external content). It runs only once an adopter supplies real implementations
behind the scaffolding interfaces.

## License

Same terms as this repository — see `LICENSE` / `LICENSE-CODE` at the root.
