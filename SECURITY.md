# Security Policy

XSI-AIMS is an open **specification**, not a running service. There is no hosted endpoint, deployed binary, or package to compromise here. "Security" for this repository means the integrity of the specification text and its reference materials — and, most importantly, whether the specification can be read in good faith and still produce an insecure or unsafe implementation.

This policy explains what to report, how to report it, and what to expect in return.

## What's in scope

A security report against XSI-AIMS is appropriate when you find any of the following:

- **Specification ambiguities with security impact.** A normative passage that two careful implementers could read in incompatible ways, where at least one reasonable reading produces an insecure, unsafe, or governance-bypassing implementation. (Plain clarity bugs without a security dimension belong in a normal Issue — see [`SUPPORT.md`](SUPPORT.md).)
- **Unsafe-by-default normative requirements.** A `MUST` / `SHOULD` that, if implemented exactly as written, weakens authority chaining, witness integrity, conformance-level guarantees, or any other safety surface the specification is meant to uphold.
- **Conformance-test gaps.** A way for an implementation to claim a conformance level (FULL / PARTIAL / OBSERVER) while still violating a security-relevant invariant the level is supposed to guarantee — i.e., the spec asserts a property the conformance criteria do not actually enforce.
- **Protocol-level weaknesses** in the AIMS Interchange Protocol (AIP) wire format or the IAME envelope — for example, a described handshake or trust-attenuation step that is exploitable as specified.
- **Integrity issues in the published materials** — a figure, code sample, or companion document that contradicts the normative text in a way that would lead an implementer toward an insecure design.

## What's out of scope

- Vulnerabilities in a *specific implementation* of XSI-AIMS (including XSI's own reference deployments). Report those to that implementation's maintainers, not here.
- General typos, editorial defects, and non-security clarifications — open a normal Issue instead.
- Theoretical concerns with no path to an insecure or unsafe implementation.

## How to report

Email **security@xtendedsystems.com** with the details. If that address is unavailable to you, use **aims@xtendedsystems.com** as a fallback and put `SECURITY` in the subject line so it is routed correctly.

Please include, to the extent you can:

- the specification version or git tag you are referring to (see [`CHANGELOG.md`](CHANGELOG.md));
- the section number(s) and exact passage(s) at issue;
- the insecure or unsafe reading, and why it is reasonable;
- a suggested correction or mitigation, if you have one.

**Do not open a public Issue or Discussion for a security-relevant report.** Use email first so a fix or clarification can be coordinated before the weak reading is broadcast.

## What to expect

- **Acknowledgement within 5 business days** of receipt.
- An initial assessment of scope and severity, and an indication of whether we agree it is security-relevant, in the same window where practical.
- For confirmed issues, a coordinated fix: an errata note, a clarified passage, or a conformance-criteria change, landed under the versioning policy in [`CONTRIBUTING.md`](CONTRIBUTING.md). Spec changes follow the normal RFC and release process, so a security clarification may land as a PATCH (editorial/non-normative) or, if it changes required behavior, as a MINOR or MAJOR revision.
- Credit in the changelog and/or release notes if you would like it — tell us how you'd prefer to be named, or to stay anonymous.

These are best-effort targets from a small steward team, not a contractual SLA.

## Coordinated disclosure

We practice coordinated disclosure. We ask that you give us a reasonable opportunity to clarify or correct the specification before you publish the weak reading. We will work with you on timing and will not take legal action against good-faith security research conducted under this policy. Because this is a specification rather than a service, there is no standing embargo clock; we will agree on a disclosure timeline with you per report.

## No bug bounty

XSI does not operate a bug-bounty program and does not offer monetary rewards for reports. We genuinely appreciate responsible reports and will acknowledge contributors publicly where they wish to be named.

---

*This policy covers the XSI-AIMS specification repository only. For general help and non-security questions, see [`SUPPORT.md`](SUPPORT.md).*
