# Contributing to XSI-AIMS

XSI-AIMS is a specification, not a product. It improves when implementers and reviewers engage with it. This document covers how to file issues, propose substantive changes through the RFC process, contribute figures or pointers to your implementation, and a few operational guardrails everyone is asked to honor.

## Ways to contribute

- **Report bugs and request clarifications.** Open an [Issue](../../issues) when you find a contradiction, an unclear definition, an unimplementable specification surface, or an ambiguity that two careful readers could interpret differently.
- **Propose substantive specification changes via RFC.** Anything that would change normative behavior — the AIP wire format, the IAME envelope, conformance levels, the archetype taxonomy, a safety pattern — goes through the RFC process described below. Start by opening an Issue or a Discussion to lay out the proposal.
- **Submit new educational figures.** Diagrams that help newcomers understand a concept are welcome. Follow the visual conventions of the existing figure set under `docs/figures/` so the set stays consistent.
- **Add a pointer to your XSI-AIMS implementation.** If you build a system that conforms to XSI-AIMS at any level, open a Discussion describing it. Implementation pointers are community-contributed; XSI does not vet or maintain them.
- **Improve documentation.** Companion docs, README clarifications, glossary expansions — all welcome.

## RFC process

The RFC (Request for Comments) process is the mechanism for substantive changes to the specification. It is intentionally lightweight:

1. **Open an Issue first** to gauge interest and confirm scope. This step prevents the disappointment of sinking time into a proposal that turns out to overlap with existing work or fall outside the spec's mission. For open-ended design exploration, a [Discussion](../../discussions) is the right starting point.
2. **Write up the proposal.** A complete proposal covers motivation, design, drawbacks, alternatives, prior art, and unresolved questions. Attach it to the Issue (or to a PR, if you are also proposing the corresponding spec text). Proposals are numbered by the maintainers when they are accepted.
3. **Public comment period.** A public review window opens once the proposal is ready for review. Substantive concerns are addressed in revisions; trivial drift is handled in the thread.
4. **Maintainer decision.** During the pre-2.0 phase, XSI holds release authority — the maintainers either accept the proposal, defer it, or close it as withdrawn, with the rationale recorded in the project's governance records. As governance moves toward broader community stewardship, this decision path broadens; see [`governance/STEWARDSHIP.md`](governance/STEWARDSHIP.md).
5. **Land in the next release.** Accepted proposals are merged into the specification in the version that follows their acceptance, per the versioning policy below.

> **Note:** This repository publishes the specification and its process, not the draft RFCs themselves. Route all proposals through Issues, Discussions, or email (`aims@xtendedsystems.com`) — do not expect an `rfcs/` directory in this release.

## Versioning policy

The specification follows semantic versioning (`MAJOR.MINOR.PATCH`):

- **MAJOR** — breaking changes to the AIP wire format or to core archetype semantics. Implementations conforming to version `N.x` may not interoperate with version `(N+1).x` without changes.
- **MINOR** — additive clarifications, new normative sections that preserve backward compatibility, and new conformance test cases.
- **PATCH** — typos, editorial fixes, and non-normative clarifications.

Implementations declare the AIMS version they target in their AIP handshake and in their public documentation.

## What's in scope

- Specification clarifications, ambiguity resolution, and defect fixes.
- Gap closures — surfaces of the spec that need additional detail before an implementer can proceed.
- New conformance test cases that strengthen the test suite for the published conformance levels.
- New educational figures that follow the locked visual style.
- Pointers to XSI-AIMS implementations, shared via Discussions.
- Roadmap input on the multi-year themes (post-quantum encryption, dedicated-model training for sovereign management and coherence validation, AGI-era alignment scaling).

## What's out of scope

- **Vendor-specific extensions** that bind the specification to one product's particulars.
- **Commercial product roadmaps.** AIMS is the substrate, not a product. If you implement AIMS in a commercial product, the product roadmap belongs in your own repository.
- **Individual implementation specifics.** AIMS describes patterns and protocols; the internals of any specific implementation belong with that implementation.

## Code of Conduct

Please see [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). All participation in this project is governed by it.

## License of contributions

Two licenses govern this repository: **CC-BY 4.0** for the specification text, companion documents, and figures (see [`LICENSE`](LICENSE)), and **MIT** for embedded code samples, pseudocode, schema fragments, and reference snippets (see [`LICENSE-CODE`](LICENSE-CODE)). Contributions are accepted inbound under the same license that governs the artifact being modified — prose contributions land under CC-BY 4.0, code-sample contributions land under MIT.

## Sign-off (DCO)

We use the lightweight **Developer Certificate of Origin** (DCO). There is no contributor license agreement (CLA). Each commit must carry a `Signed-off-by:` trailer affirming you have the right to contribute the work under the project's license:

```
Signed-off-by: Your Name <your.email@example.com>
```

Most git clients automate this with `git commit -s`. The DCO text is at `https://developercertificate.org/`. Pull requests with unsigned commits will be asked to amend.

## Acknowledgement

Accepted contributors are credited in the release notes for the version their work lands in. Tell us in the PR or Issue how you'd like to be credited (name, affiliation, handle, or uncredited — all are fine).

## Questions

For specification questions and design conversations, please use [GitHub Discussions](../../discussions) — that's where the community gathers and where most "how do I think about this?" threads belong. For matters that don't fit Discussions, you can reach the maintainers at `aims@xtendedsystems.com`.
