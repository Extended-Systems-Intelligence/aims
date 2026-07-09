# Changelog

All notable changes to the XSI-AIMS specification are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.2 — Public Review] — July 2026

Editorial hygiene release. Removes internal drafting and process references from the published specification and function catalog so every reference resolves within the public document set: internal amendment identifiers, drafting/reconciliation annotations, internal verification-model file paths and run statistics (machine-checked assurance statements retained), dangling pointers to non-public companion documents and unpublished diagrams, and internal review bookkeeping. Substrate and product illustrations are generalized to vendor-neutral descriptors; industry-standard technical identifiers and scholarly citations are retained. **No normative change** — every requirement, definition, mechanism, and conformance obligation is identical to 2.1.1; an implementation conformant to 2.1.1 remains conformant against 2.1.2 at the same level.

## [2.1.1 — Public Review] — July 2026

Editorial redaction release. Removes novelty-claim framing from the specification text: the `(Novel)` section-heading tags on §§3.2, 3.4, 3.5, 3.6, 3.7, 3.8, 3.17, and 3.18, the associated `**Novel claim**` statements, and internal drafting annotations. **No normative change** — every normative requirement, definition, mechanism, and conformance obligation is identical to 2.1.0; an implementation conformant to the 2.1.0 public-review text remains conformant against 2.1.1 at the same level. Version identity advances with the live normative surface per this changelog's provenance convention.

## [2.1.0 — Public Review] — July 2026

Second public-review release of the XSI-AIMS specification. This release advances the current normative surface from 2.0; changes are additive and single-sourcing only — no 2.0 normative obligation is weakened or removed, and an implementation conformant to the 2.0 public-review text remains conformant against 2.1.0 at the same level. The specification remains a public-review draft; feedback gathered during the review window may produce further additive revisions before the release is finalized.

Version identity advances with the live normative surface; formal-verification and function-introduction records inside the specification and catalog retain their original version stamps as historical provenance.

How to engage: file an [Issue](../../issues) for defects, contradictions, or ambiguities; open a [Discussion](../../discussions) for design questions; and propose substantive changes through the RFC process described in [`CONTRIBUTING.md`](CONTRIBUTING.md). Git tags are the canonical reference point for any version pin.

### Review-window revision — 2026-07-06

Additive in-window revision. No 2.1.0 normative obligation is weakened or removed.

#### Added

- **SOVEREIGN Identity & Access Management (CIAM) interface contract** at §13.0.2.1, with a seven-operation inventory at §13.0.2.1.1 — a required in-seal local registry of principals and permissions (initialized at commissioning with a local administrative principal independent of any identity provider), an internal identity provider that is never externally exposed, and consume-not-host federation with registrable external identity providers.
- **Required-tool security floor** at §3.X.FUNC.7.2.1 — post-quantum seal support propagated into every required Tool-Stratum tool's contract, with a per-tool custody and floor-application table.
- **Function-set contract completeness standard** at §3.X.FUNC.7.2.2 — the eight disclosure dimensions every required tool's contract must satisfy, declarable per tool in the ConformanceManifest.
- **Post-quantum confidentiality floor and frontier classical tolerance** at §3.65.7; **credential non-exposure at the inference boundary** at §3.21.10; **credential-store post-quantum seal** at §3.21.11; conformance families §3.19.30–§3.19.31 and the corresponding §6.3 Witness events.
- **Execution cadence and witnessed operational timing** at §2.7 (informative).
- **Adapter-consolidation gate contract** at §13.7.5.8 — the minimal normative anchor for the required-when-present adapter trainer (gate topology, frozen-weights invariant, sealing, Witness events); behavioral specification remains with a future RFC.
- **Working-memory strategy-operation contracts** at §3.X.MEM.WM.4 — I/O, determinism class, witness events, and explicit cross-archetype access for the four context-engineering strategies.
- **External literature anchors** — field context on self-scaffolding model releases at §3.X.HGOV; memory-management-as-an-optimizable-skill at §3.X.MEM.SPA.7.
- **`outcome_informed: trained` provenance class** at §3.X.HGOV.0.2 — the activation predicate is now a two-class enum: deployment-derived (`true`, explicitly temporally agnostic — training-time consumption of the deployment's own outcome records does not launder provenance) and weights-internalized (`trained`, assigned deterministically at the admitting gate from the substrate's declared training provenance; undeclared provenance defaults to `trained`, fail-closed). Both classes activate the identical self-modification envelope.

#### Changed

- **The SOVEREIGN's identity function is in scope.** The prior text classified principal authentication as a deployment-supplied external concern outside the specification's scope; this revision corrects that across the required-tool map (§3.X.FUNC.7.2), the reconciliation notes (§3.X.FUNC.7.4), the Northbound Gateway duties (§3.X.PERIM.2), the identity-subsystem scope clarification (§3.66.7.3.2), the boundary-delegation notes, and the north-frontier text (§3.65.7.3). Only external end-customer commerce sign-in remains out of scope.
- **Required-tool contract extended to six dimensions** (§2.6, §3.X.FUNC.7.2) — security floor added to shape, interface, deployment property, cross-archetype access, and Witness obligation.

#### Fixed

- Three tool-name references in the memory-router text replaced with capability-class language, consistent with the specification's vendor-neutral naming discipline.

### Added

- **AGI-emergence threat model** authored as the foundational structural-safety statement, addressed across the normative components so the guarantee does not depend on post-emergence spec changes.
- **Surfacing-classification criteria and engagement format** inlined into the normative body (previously carried by reference).
- **Overlapping-grace-window ruling** — a calendar-promotion attempt while a prior grace window is open is refused and escalated to the SOVEREIGN principal.
- **`scope_hash` canonicalization ruling** — scope canonicalizes as an ordered JSON array; ordering is load-bearing.
- **Two functions added to the catalog** — `FN-426` (`extractive_topk`) and `FN-427` (`cross_sovereign_feedback_classify`); catalog 422 → 424 entries.
- **Reference-binding registry** at [`governance/reference-bindings.md`](governance/reference-bindings.md).

### Changed

- **Eight redundancy single-sourcings** — duplicated normative content collapsed to a single canonical statement with cross-references.
- **Self-containment** — normative content that previously resolved only by reference to companion artifacts is now inlined; the specification is fully self-contained.

## [2.0 — Public Review] — June 2026

The initial public-review release of the XSI-AIMS specification. The specification text and figures are stable enough to read, implement against, and pilot. This is a public-review draft: feedback gathered during the review window may produce additive, forward-compatible revisions before the release is finalized.

How to engage: file an [Issue](../../issues) for defects, contradictions, or ambiguities; open a [Discussion](../../discussions) for design questions; and propose substantive changes through the RFC process described in [`CONTRIBUTING.md`](CONTRIBUTING.md). Git tags are the canonical reference point for any version pin.

### Added

- The XSI-AIMS specification at [`spec/XSI-AIMS-specification.md`](spec/XSI-AIMS-specification.md).
- The function catalog at [`spec/catalog/`](spec/catalog/).
- Educational figures under [`docs/figures/`](docs/figures/).
- Conformance levels (FULL / PARTIAL / OBSERVER).
- The AIMS Interchange Protocol (AIP) wire format and the IAME envelope.
- The safety-pattern substrate.
- The archetype taxonomy.
- The Witness Layer and the layered memory architecture.
- The Trust Gradient.
- Governance and community materials: [`GOVERNANCE.md`](GOVERNANCE.md), [`governance/STEWARDSHIP.md`](governance/STEWARDSHIP.md), [`MAINTAINERS.md`](MAINTAINERS.md), [`CONTRIBUTING.md`](CONTRIBUTING.md), [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md), [`SECURITY.md`](SECURITY.md), [`SUPPORT.md`](SUPPORT.md), and [`TRADEMARKS.md`](TRADEMARKS.md).
