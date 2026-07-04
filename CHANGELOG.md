# Changelog

All notable changes to the XSI-AIMS specification are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0 — Public Review] — July 2026

Second public-review release of the XSI-AIMS specification. This release advances the current normative surface from 2.0; changes are additive and single-sourcing only — no 2.0 normative obligation is weakened or removed, and an implementation conformant to the 2.0 public-review text remains conformant against 2.1.0 at the same level. The specification remains a public-review draft; feedback gathered during the review window may produce further additive revisions before the release is finalized.

Version identity advances with the live normative surface; formal-verification and function-introduction records inside the specification and catalog retain their original version stamps as historical provenance.

How to engage: file an [Issue](../../issues) for defects, contradictions, or ambiguities; open a [Discussion](../../discussions) for design questions; and propose substantive changes through the RFC process described in [`CONTRIBUTING.md`](CONTRIBUTING.md). Git tags are the canonical reference point for any version pin.

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
