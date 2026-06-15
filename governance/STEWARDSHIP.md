# Stewardship

This document describes how the XSI-AIMS specification is stewarded today and how stewardship is intended to broaden over time. It is the authoritative companion to [`GOVERNANCE.md`](../GOVERNANCE.md); where the two differ in detail, this document governs.

## Initial stewardship

XSI-AIMS is published and initially stewarded by Extended Systems Intelligence Corporation (XSI), the specification's founding author. During the pre-2.0 phase the steward:

- maintains this repository — issue triage, pull-request review, release tagging, branch protection;
- runs the public RFC process described in [`CONTRIBUTING.md`](../CONTRIBUTING.md);
- holds release authority on accepted changes;
- records substantive decisions together with their rationale.

This arrangement is **transitional by design**. Publishing the model openly makes the conditions and mechanics of the eventual stewardship transition visible from the outset.

## Versioning and freeze conventions

- Releases follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html). **Git tags are the canonical reference point for any version pin.**
- A released version's normative text is frozen at its tag; corrections land in a subsequent version rather than mutating a published tag.
- Public-review drafts may receive additive, forward-compatible revisions during their review window before the version is finalized.

## Path to multi-stakeholder governance

The intent is to broaden stewardship as a community of implementers, researchers, and reviewers forms:

1. **Sole stewardship (current)** — a single steward operating a transparent public process.
2. **Multi-organization maintainers** — external maintainers are invited as they demonstrate sustained, trusted engagement (see [`MAINTAINERS.md`](../MAINTAINERS.md)).
3. **Shared multi-stakeholder governance** — a documented maintainer structure and steering process, with potential submission to a recognized standards body.

Changes to the stewardship model itself go through a dedicated **Stewardship RFC** with an extended public comment period.

## Related documents

- [`GOVERNANCE.md`](../GOVERNANCE.md) — governance overview and roles.
- [`MAINTAINERS.md`](../MAINTAINERS.md) — current maintainership.
- [`CONTRIBUTING.md`](../CONTRIBUTING.md) — the RFC and contribution process.
