# Reference Binding Registry

This document is the registry of AIMS Reference Bindings. It is a maintainer-team artifact, maintained under the same stewardship arrangements described in `STEWARDSHIP.md`.

## What a Reference Binding is

A Reference Binding registers a normative mapping from a specific upstream toolchain or substrate onto an AIMS contract — for example, the mapping from a Deterministic Telemetry Tier (rules engine + alerting mechanism) onto the AIMS Event Promotion Payload consumed by the Event Promotion Gateway (§3.X.TEL.7 / §3.82.7). Each binding carries an identifier, a field mapping, and a set of conformance assertions that a binding-conformant implementation MUST satisfy (see §3.X.TEL.11 / §3.82.11 for the assertions attached to the binding registered below).

A Reference Binding never confers conformance on the substrate it binds. Conformance claims are made only by a deployed implementation as a whole, per §4; a binding-catalog registration is not evidence of a conformance level.

## Registered bindings

| Identifier | Substrate | Spec anchors | Catalog entry | Status |
|---|---|---|---|---|
| `mimir.alertmanager.v1` | Grafana Mimir + Prometheus Alertmanager (Grafana Alloy translation tier) | §3.X.TEL.11 / §3.82.11; Gateway contract §3.X.TEL.7–14 / §3.82.7–14 | `spec/catalog/aims-telemetry-bindings.yaml` | ACTIVE |

At v2.1.0, `mimir.alertmanager.v1` is the single registered binding, per the registry clause of §3.X.TEL.11 (V10):

> Reference Binding registry maintained at `xsi-aims/governance/reference-bindings.md` (maintainer-team artifact, future). At v2.0 the single registered binding is `mimir.alertmanager.v1`; future bindings (OpenTelemetry events native, log-source DTTs, custom CEP frameworks like Apache Flink with deterministic windowing, §3.62 ATS direct) MAY be registered through subsequent AIMS RFCs.

## Pending registration

The following bindings exist as drafts and are **not registered**. They carry no normative force and MUST NOT be cited as registered bindings until they are ratified and land in the catalog through the RFC process.

| Identifier (proposed) | Substrate | Status |
|---|---|---|
| `aims.binding.maf.csm.v1` | Microsoft Agent Framework (CapabilitySurfaceManifest companion, §13.4.5.6) | DRAFT — pending ratification; not registered |
| `aims.binding.lodestone.helm.v1` | Helm-packaged capability model (registration / policy / lifecycle / supply-chain surfaces) | DRAFT — pending ratification; not registered |

## Registration procedure

- This registry is a maintainer-team artifact. Changes are made by the maintainer team listed in `.github/CODEOWNERS` and recorded here.
- New bindings MAY be registered through subsequent AIMS RFCs, per the §3.X.TEL.11 registry clause quoted above and the RFC process at `rfcs/` (30-day default comment period; maintainer decision recorded in `governance/decisions/`).
- Updates to an existing binding require an RFC unless they are purely additive, non-normative clarifications.
- A registration adds one row to the table above and a corresponding entry in the binding catalog file; the catalog entry is the machine-readable source of the binding's field mappings and conformance assertions.

---

*Last updated: 2026-07-03 (initial registry, v2.1.0).*
