# Governance

This document gives a concise overview of how XSI-AIMS is governed. The detailed, authoritative model — current arrangements, the intended trajectory toward broader stewardship, and the versioning and freeze conventions — lives in **[`governance/STEWARDSHIP.md`](governance/STEWARDSHIP.md)**. Where this overview and the stewardship document differ in detail, the stewardship document governs.

## Current state

XSI (Extended Systems Intelligence Corporation) is the **initial steward** of the XSI-AIMS specification. As founding author and current maintainer, XSI during the pre-2.0 phase:

- maintains this repository (issue triage, PR review, release tagging, branch protection);
- holds release authority on accepted changes through the v1.x cycle;
- records substantive decisions with their rationale in the project's governance records.

This role is **transitional by design**. The point of publishing the model openly is to make the conditions and mechanics of the eventual stewardship transition visible from the outset.

## Roles

- **Contributor** — anyone who files an Issue, opens a Discussion, submits a PR, or otherwise engages with the specification.
- **Reviewer** — a contributor with demonstrated subject-matter depth whose review carries weight on PRs in their area.
- **Maintainer** — holds review-and-merge authority and shares responsibility for releases. Maintainership is currently held by the XSI-AIMS Working Group (see [`MAINTAINERS.md`](MAINTAINERS.md)) and is expected to open to external maintainers as the community forms.
- **Steward** — currently XSI, holding release authority during the pre-2.0 phase. See [`governance/STEWARDSHIP.md`](governance/STEWARDSHIP.md) for how stewardship is intended to broaden.

## How decisions are made

**Substantive specification changes** — anything that changes normative behavior (the AIP wire format, the IAME envelope, conformance levels, the archetype taxonomy, a safety pattern) — go through the public **RFC process** described in [`CONTRIBUTING.md`](CONTRIBUTING.md): an Issue to gauge scope, a proposal under public comment for a stated review window, then a maintainer decision recorded with its rationale. During the pre-2.0 phase, XSI as steward holds the final release decision; the rationale for each decision is recorded in the project's governance records.

**Editorial and operational changes** — typo fixes, non-normative clarifications, repository operations — are handled by maintainer review without the full RFC process.

**Releases** follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Git tags are the canonical reference point for any version pin; the versioning and strict-freeze conventions are specified in [`governance/STEWARDSHIP.md`](governance/STEWARDSHIP.md).

## Path to multi-stakeholder governance

XSI's stated intent is to broaden stewardship as a community of implementers, researchers, and reviewers forms around XSI-AIMS — moving from sole stewardship, through a documented multi-organization maintainer structure and steering committee, toward shared multi-stakeholder governance and potential standards-body submission. The trajectory and its conditions are described in detail in [`governance/STEWARDSHIP.md`](governance/STEWARDSHIP.md). Changes to the stewardship model itself go through a dedicated Stewardship RFC with an extended comment period.

## Related documents

- [`governance/STEWARDSHIP.md`](governance/STEWARDSHIP.md) — the authoritative stewardship model (read this for detail).
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — the RFC and contribution process.
- [`MAINTAINERS.md`](MAINTAINERS.md) — who currently holds maintainership.
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — expectations for participation.
- [`SECURITY.md`](SECURITY.md) — reporting security-relevant issues.

## Contact

For governance questions outside the public RFC process, reach the steward team at **aims@xtendedsystems.com** (subject prefix: `Governance`).
