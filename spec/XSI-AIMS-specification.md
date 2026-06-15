# XSI Agent Instrumentation and Management Specification (XSI-AIMS)

## Version 2.0 — Public Review Draft

## Extended Systems Intelligence Corporation

## June 2026

> **Status: Public Review Draft.** This is the Version 2.0 public-review release of XSI-AIMS. Conformance is full or none at the level claimed (§1.3). The public review window is open through Q3 2026.

---

## Abstract

XSI-AIMS specifies horizontal supervisory-agent governance: a framework for the safe deployment of agents that monitor and manage other agents on behalf of the system's principals. The specification applies to any agentic system, regardless of substrate, model, or deployment context.

This specification defines the technical framework for the instrumentation, lifecycle management, and safety supervision of agentic workforce members across cloud, on-premises, hybrid, edge, and appliance Environments. The framework introduces architectural patterns for agent management that address known gaps in current multi-agent orchestration: incomplete capability discovery, unstructured inter-agent communication, absent integration-layer formalization, generic error handling, asymmetric lifecycle management, environment-as-afterthought deployment patterns, multi-model coherence boundaries, cross-substrate agent governance, the absence of a structural cryptographic-domain boundary between an agentic system's internal trust fabric and its interactions with foreign models, the absence of AGI-resistance hardening, and the absence of function-level rigid/judgment decomposition with a defensive perimeter that bounds LLM authority through deterministic ratification.

XSI-AIMS is universal by construction. Its normative surface references cross-industry foundations — OpenTelemetry semantic conventions, ISO 27001, ISO 42001, NIST AI RMF, the IEEE 7000-series, the EU AI Act, and FIPS 203/204/205 — wherever a genuinely cross-industry standard exists. Industry-specific compliance frameworks are accommodated through the §3.63 Industry Compliance Interface Architecture as companion documents.

XSI-AIMS is designed under the assumption that AGI may arrive without warning. Once it does, the time window for spec evolution closes; XSI-AIMS is either secure on day one or compromised on day one. The strongest defenses ship in this version.

---

## 1. Scope

### 1.1 Purpose

> **[Figure D01 — Three Principles Concept Diagram]**

XSI-AIMS — the Agent Instrumentation and Management Specification — defines a universal standard for the safe deployment, instrumentation, authority delegation, lifecycle management, audit, supervision, and conformance verification of agentic systems. XSI-AIMS specifies horizontal supervisory-agent governance applicable to any Environment type — Sovereign Cloud, Privately hosted, Publicly deployed, or Appliance — and to any agent transport (MCP, A2A, or any future agent transport that satisfies the AIP wire format requirements in §3.24.A).

The specification expresses *what* must be present and *how it must behave*. The specification does not prescribe *how it must be built* — the specific algorithms, data structures, storage formats, transport encodings, integration adapters, user interfaces, and operational tooling are proprietary to the implementation, provided the conformance contract in §3.24 is satisfied.

### 1.2 Industry Neutrality

XSI-AIMS is an industry-neutral standard. The normative surface MUST reference cross-industry foundations — including but not limited to OpenTelemetry semantic conventions, ISO 27001, ISO 42001, NIST AI RMF, the IEEE 7000-series, the EU AI Act, and FIPS 203/204/205 — wherever a genuinely cross-industry standard exists. XSI-AIMS MUST NOT bind to any single industry's regulatory regime in its core normative text.

Industry-specific compliance frameworks MUST be accommodated through the §3.63 Industry Compliance Interface Architecture as separately maintained companion documents. Eight industry compliance interface companion documents are in scope: telecom, healthcare, energy, finance, government, defense, critical infrastructure, and real estate. Companion documents map their industry's regulatory requirements onto XSI-AIMS normative components; they MUST NOT introduce new normative requirements on the core spec, and they MUST NOT relax core normative requirements.

**AGI emergence is foundational to XSI-AIMS, not a compliance interface.** The Industry Compliance Interface Architecture exists to map regulated-sector requirements onto XSI-AIMS components. AGI emergence is not a regulated sector — it is the threat model XSI-AIMS was designed against from the start. P4 (AGI-Resistance Risk Model) is one of the load-bearing architectural principles. T8 (internal AGI emergence) is one of the eight first-class threats the threat matrix addresses. Every component in the architecture — Cryptographic Boundary (§3.65/§3.66), Witness Layer (§3.10), Function-Level Decomposition (§3.X.FUNC), Defensive Perimeter (§3.X.PERIM), Two-Layer Conformance Verification (§3.68), Deterministic Ratification (§3.69), Formal Verification (§3.70), hardware-rooted attestation (§3.21), Universal Witnessing (§2.5), Cluster Mode Byzantine consensus (§3.64) — exists in part because of AGI emergence risk. There is no separate AGI baseline because AGI-emergence consideration is woven into XSI-AIMS itself.

Implementations MAY declare conformance to one or more industry compliance interface companions in addition to their core XSI-AIMS conformance level.


### 1.2.5 The Sovereign Archetype — What It Is, and What It Is Not

The XSI-AIMS **Sovereign archetype** is the per-user agent that manages every other agent within the framework on the user's behalf. The user's Sovereign is the user's **assistant, partner, and ally** — the single agent that holds the user's intent, advocates for the user's goals across the framework's coordination, and ratifies every output before it reaches the user. Implementations MAY permit users to name their Sovereign, establish voice interactions with it, and personalize its presentation; the Sovereign archetype's authority structure is unchanged by personalization. The Sovereign exists *for* the user; everything else in the framework operates *for the Sovereign*.

The term "Sovereign" in XSI-AIMS refers exclusively to this per-user agent archetype. **It does NOT refer to "sovereign cloud" (the various jurisdictional-data-residency cloud offerings), "sovereign AI" (national-policy or national-data-sovereignty framings used by various governments and vendors), or "AI sovereignty" (the broader policy discourse on jurisdictional control over AI infrastructure).** Those usages address national or jurisdictional data sovereignty — a different semantic domain entirely. XSI-AIMS' "Sovereign" archetype is supreme authority *within the scope of a single user's interaction with the framework*, not jurisdictional sovereignty over AI infrastructure. The two domains do not overlap; deployments may simultaneously be sovereign-cloud (jurisdictional sense) and contain XSI-AIMS Sovereign archetypes (per-user-agent sense) without contradiction.

The choice of "Sovereign" as the archetype name is deliberate: the archetype holds supreme authority within its scope (the per-user interaction), and no other archetype overrides it. Implementers who find the term creates confusion with sovereign-cloud / sovereign-AI usage are encouraged to use "the user's Sovereign agent" or "the per-user Sovereign" in adoption-facing materials; the spec's normative archetype identifier remains `SOVEREIGN`.

### 1.3 No-Partial-Adoption Clause (P1)

XSI-AIMS conformance is full or none at the level claimed. An implementation that omits any normative component required by its declared conformance level is not XSI-AIMS-conformant at that level. Partial-adoption claims — assertions that the implementation supplies "most of FULL" or "FULL except for component X" — are prohibited from §3.24 conformance advertisement. An implementation that wishes to advertise a level lower than FULL MUST advertise the next-lowest level that fully satisfies the level's normative requirements (PARTIAL or OBSERVER), and MUST NOT advertise FULL.

The framework's interdependencies require full adoption from the outset; no "XSI-AIMS-Lite" subset is coherent at the FULL level. An "XSI-AIMS-FULL except for the Cryptographic Boundary" claim is structurally impermissible, because every other FULL component depends on the Cryptographic Boundary holding. The same holds for the Defensive Perimeter (P10) and Function-Level Decomposition (P9): omission of either renders other FULL guarantees unenforceable.

### 1.4 No-HCOD / No-Escape-Hatch Clause (P2)

No exception, derogation, or hardware-constrained operational deviation (HCOD) mechanism exists at the spec level. There is no "best-effort" fallback for any normative MUST. There is no sampling carve-out for synchronous Sovereign intent-conformance verification, no cache-the-verdict optimization, no "skip Enforcer if latency budget tight" path, and no "operate without hardware-rooted attestation if the substrate is unavailable" path.

Implementations operating below normative requirements for their declared conformance level MUST NOT advertise an XSI-AIMS conformance level. The non-conformance posture (the implementation operates outside XSI-AIMS) is structurally preferable to the degraded-but-trusted posture (the implementation claims conformance with quiet exceptions); the degraded-but-trusted posture creates trust-laundering across §3.20 DCP federation.

Where operational constraints make a normative requirement difficult to satisfy at full availability, implementations MUST satisfy the requirement at the cost of availability rather than satisfy availability at the cost of the requirement. Cluster Mode (§3.64) provides the supported pathway for implementations whose single-node availability is insufficient for the synchronous-verification load.

### 1.5 OpenTelemetry Alignment Clause (P5)

XSI-AIMS metrics, attributes, events, and resources MUST align with OpenTelemetry semantic conventions where such conventions exist. Where XSI-AIMS introduces concepts that OpenTelemetry has not yet standardized, XSI-AIMS MUST extend within the `aims.*` namespace using OpenTelemetry-style naming.

OTLP transport is mandatory for XSI-AIMS metric and event emission. Prometheus exposition format is permitted for pull-based deployments via the OpenTelemetry Collector translation path; direct Prometheus emission as the sole telemetry path is non-conformant. Vendor extensions in the `aims.ext.<vendor>.<domain>.<name>` namespace are permitted but never required; consumers MUST NOT fail on unknown extensions.

### 1.6 Industry Compliance Interface Clause (P3)

Industry-specific compliance frameworks are accommodated through the §3.63 Industry Compliance Interface Architecture. The core XSI-AIMS specification does not bind to any single industry's standards.

An industry compliance interface companion document MUST: (a) map the industry's regulatory requirements onto XSI-AIMS normative components without introducing new core requirements; (b) declare any XSI-AIMS configuration constraints implied by the industry's regulatory regime; (c) declare which industry-specific cross-references the companion expects; (d) be independently versioned and maintained.

An industry compliance interface companion document MUST NOT: (a) relax any core XSI-AIMS normative requirement; (b) introduce new normative requirements on the core specification; (c) declare conformance levels that conflict with §3.24; (d) bypass the Cryptographic Boundary or the Adversarial-Default Output Scrutiny principle.

### 1.7 Environment Declaration

Each XSI-AIMS-conformant implementation MUST declare its Environment type at registration and at AIP handshake time. An implementation MAY serve multiple Environment types via separate deployments; cross-Environment coordination is specified in §3.20 (Distributed Coherence Protocol — cross-Sovereign federation) and §3.64 (Cluster Mode — intra-deployment multi-appliance scaling). Cross-cluster federation (composing Cluster Mode and DCP) is explicitly prohibited.

### 1.8 Reference Implementations

The specification cites reference implementations (e.g., an appliance reference implementation for the Appliance Environment type) for illustration. Reference implementations are downstream of the specification; the specification does not extend or depend on any reference implementation. Examples used in the specification are illustrative and use only publicly available, free-use, or open-source mechanisms.

---

## 2. Terminology

| Term | Definition |
|------|-----------|
| **Agent** | A software entity that performs work on behalf of a principal, with defined capabilities, authority scope, and lifecycle states. |
| **Principal** | The human or system entity that grants an agent its authority and scope. The user is **external to XSI-AIMS**; XSI-AIMS does not model the user as an agent. The per-user **Sovereign** is the agent that mediates between the user and the rest of the Environment. |
| **Sovereign (Agent)** | A per-user LLM agent at L-Intent paired one-to-one with the user's Tier-3 Orchestrator. Operates under the `AUTHORITY` posture (§3.16) which transcends and dispatches across the three operational modes. See §3.72 for narrow-role specification and §3.73 for Sovereign-as-LLM clarification. |
| **`ENVIRONMENT_POLICY_BUNDLE`** | The organization-wide policy bundle binding every per-user Sovereign in the Environment. Formerly named `SOVEREIGN_CONFIG`; the prior identifier is preserved as a backward-compat schema alias only. Not an agent. |
| **Environment** | The deployment context of an XSI-AIMS-conformant system. Canonical types: **Sovereign Cloud**; **Privately hosted**; **Publicly deployed**; **Appliance**. XSI-AIMS is deployment-agnostic. |
| **Adapter** | A connector providing an agent with access to an external system. |
| **Profile** | A packaged configuration defining tools, adapters, dashboards, and behavioral constraints for a specific organizational role. |
| **Autonomy Level** | A five-tier trust gradient (L1-Shadow through L5-Autonomous). |
| **Witness** | An immutable audit mechanism recording agent actions for compliance and forensic purposes. The Witness Layer is cryptographically segmented along the Cryptographic Boundary (internal / external / bridge segments per §3.10 and §3.65). |
| **Witness Path (W#)** | A governance-class CommunicationPath whose `path_class` is `WITNESS` and whose `allowedMessages` are restricted to `[QUERY, ALERT]`. W-paths carry no DIRECTIVE / REPORT / CONSENSUS traffic. See §3.16 and §3.X.W. |
| **Span of Control** | The maximum number of direct reports any single manager may supervise. Standard range 3-7. |
| **Auxiliary** | An agent running on a different model than the foundation. May be a **Simple Auxiliary** (single foreign model) or a **Composite Auxiliary** (foundation-anchored framework with its own emanated subagents from a different foundation). Managed through binding (§3.17), not emanation (§3.8). Communicates only through its binding supervisor and the EAP envelope across the Cryptographic Boundary. May be ephemeral or persistent. |
| **Composite Auxiliary** | An Auxiliary that is itself a foundation-anchored framework (e.g., a parent deployment anchored on one foundation model binding to a composite XSI-AIMS framework anchored on a different foundation model). Presents to parent XSI-AIMS as a single bound entity; internals are invisible. See §3.17.8 / §3.X.CA. |
| **Binding** | The management protocol for Auxiliary agents. Includes registration, scope assignment, supervisor designation, output validation, and dismissal. |
| **Foundation Model** | The shared model substrate from which all emanated agents are differentiated. Defines the coherence domain boundary. |
| **IAME** | Inter-Agent Message Envelope. The internal cryptographic envelope for intra-framework communication on the internal cryptographic domain (§3.18.5). |
| **EAP** | External Auxiliary Protocol. The external cryptographic envelope for all communication with foreign-model Auxiliaries on the external cryptographic domain (§3.67). |
| **Cryptographic Boundary** | The structural separation between internal IAME cryptosystem and external EAP cryptosystem. Internal keys MUST NEVER appear in external communication; external keys MUST NEVER appear in internal communication. The Executor is the sole bridge (§3.65, §3.66). |
| **Cluster Mode** | Multiple physical XSI-AIMS appliances under common operator control operating as a single logical XSI-AIMS deployment via Byzantine consensus, single canonical Witness chain, and atomic Tier-3 user-pair migration. Distinct from §3.20 DCP federation. See §3.64. |
| **Conformance Level** | One of `FULL`, `PARTIAL`, `OBSERVER`. Declared in AIP handshake. See §3.24. |
| **Deterministic Ratification Pattern** | The principle that authority-bearing decisions made by an LLM-class component MUST be ratified by a deterministic component before the consequence executes. See §3.69. |
| **Rigid Function** | A function whose correctness is decidable from its inputs by deterministic logic alone — no judgment required. Rigid functions MUST be implemented by deterministic components and SHOULD be formally verified per §3.70. See §3.X.FUNC. |
| **Judgment Function** | A function whose correctness depends on contextual interpretation, weighing of competing considerations, or open-ended synthesis — judgment required. Judgment functions are implemented by LLM-class components subject to §3.69 Deterministic Ratification. See §3.X.FUNC. |
| **Defensive Perimeter** | The architectural commitment that the Sovereign is the unique northbound gateway and the Executor (operating as the Application Gateway) is the unique southbound gateway; the Relay acts as an internal firewall on the center spine; no other agent communicates outside the Environment. See §3.X.PERIM / §3.78. |
| **Application Gateway** | Operational/networking synonym for the Executor archetype. The Executor acts as the XSI-AIMS L7 Application Gateway — the controlled, audited, cryptographically-bounded ingress/egress point between the internal sovereign framework and external Auxiliary models. The terms are interchangeable: "Executor" is the spec/schema identifier; "Application Gateway" is the operational/adoption-facing descriptor. See §3.X.PERIM.3 for the normative alias declaration and §3.66 for the Bridge-of-Trust enclave specification. |
| **Three Functional Columns** | The mapping of M-Constraining → Structural Left, M-Integrative → Center Spine, M-Generative → Dynamic Right. The Constraining column provides rules and structure; the Integrative spine carries the request-response chain; the Generative column provides exploration and capability. See §2.4. |
| **Universal Witnessing** | The principle that every authorized communication path is a witnessing channel and every receiving archetype performs shadow-pattern observation on senders. See §3.18 preamble and §3.X.W. |
| **Example filenames (non-normative)** | Concrete filenames (e.g., `IDENTITY.md`, `MEMORY.md`, `SOUL.md`) are illustrative. An implementation may choose any filename convention provided the underlying contracts are satisfied. **Auxiliary agents** use a parallel six-file family: `IDENTITY.md`, `BINDING.md`, `PROVENANCE.md`, `MEMORY.md`, `CAPABILITIES.md`, and optional `skills/*.md` per §3.17.9. As with the emanated family, filenames are non-normative; the underlying contracts are normative. |

---

## 3. Architectural Overview (preamble to §3 normative sections)

XSI-AIMS defines management components organized across four operational layers, three functional modes (mapped onto three functional columns), and the `AUTHORITY` posture for the Sovereign archetype.

### 2.1 The Four Operational Layers

> **[Figure D02 — Stacked Architecture (4 Layers + 3 Modes + Safety Substrate)]**

| Layer | Name | Function | Example implementation surface |
|-------|------|----------|----------------------|
| **L-Intent** | Intent Layer | Defines organizational goals, policies, constraints. | Per-user Sovereign agent; org-wide `ENVIRONMENT_POLICY_BUNDLE` |
| **L-Plan** | Planning Layer | Translates intent into architectural decisions. | Profile assignment, adapter provisioning, RBAC |
| **L-Form** | Formation Layer | Instantiates agents, assigns work, manages coordination. | Per-user Orchestrator; capability pools |
| **L-Exec** | Execution Layer | Performs material work — tool calls, adapter invocations, document generation. | Runtime agent operations, WORM-logged actions |

**The Layer Discipline Rule.** Communication between layers follows strict adjacency. L-Intent agents direct L-Plan agents, not L-Exec agents. L-Exec agents report to L-Form agents, not L-Intent agents. Each layer boundary requires a mandatory transformation. **No layer MAY be bypassed except via paths that carry `emergency_class: true`** (see §3.4 CommunicationPath schema and §3.16 E#-prefixed paths). Emergency-class paths are subject to the five conditions enumerated in §3.4.X; an emergency-class message that does not satisfy all five MUST be rejected at the §3.18.5 IAME envelope-binding check.

### 2.2 The Three Functional Modes (Plus AUTHORITY)

| Mode | Name | Function | Behavioral Bias |
|------|------|----------|----------------|
| **M-Generative** | Generative Mode | Creates, expands, produces, suggests. The "yes" function. | Exploration, creative output |
| **M-Constraining** | Constraining Mode | Validates, restricts, enforces boundaries. The "no" function. | Precision, rejection of violations |
| **M-Integrative** | Integrative Mode | Weighs competing signals, synthesizes judgment. The "it depends" function. | Context-sensitivity, proportional response |
| **AUTHORITY** | Sovereign Posture | Transcends and dispatches across the three operational modes. The "this is the directive" surface. | Intent-source; delegates rather than acts. |

**The Integration Principle.** In any multi-agent operation involving Generative and Constraining agents, an Integrative agent MUST be present. The Integrative agent receives input from both modes and produces the final determination. Its function is not to average or split the difference, but to determine the *correct proportion* for the specific context.

The Sovereign archetype operates under AUTHORITY — it does not produce, restrict, or integrate, but delegates operational mode authority to L-Plan and L-Form agents. See §3.72 (The Sovereign's Narrow Role) and §3.73 (Sovereign-as-LLM).

### 2.3 The Span of Control Discipline

(Standard range 3-7.)

### 2.4 Three Functional Columns (codifies P10 column dimension)

> **[Figure D03 — Three Functional Columns / 3×4 Grid]**

The three operational modes map onto three functional columns. The column an archetype occupies is a structural property of the archetype derived from its mode.

| Column | Mode | Role | Archetypes by layer (L-Plan / L-Form / L-Exec) |
|--------|------|------|------------------------------------------------|
| **Structural Left** | M-Constraining | Provides rules, validation, boundaries. The structural skeleton. | ARCHITECT / ENFORCER / ARTICULATOR |
| **Center Spine** | M-Integrative | Carries the request-response chain. Synthesizes; routes; dispatches. | (L-Intent: SOVEREIGN under AUTHORITY) / ORCHESTRATOR / RELAY · EXECUTOR |
| **Dynamic Right** | M-Generative | Provides exploration, generative capacity, allocation, sustaining. The dynamic capability. | VISIONARY / PROVIDER / SUSTAINER |

**Column Discipline Rule.** The column an archetype occupies is determined by its mode. Cross-column lateral communication within the same layer is governed by §3.4 topology paths (D# / S# / E# / W#); the structural skeleton (left) and dynamic capability (right) MUST converge through the integrative spine (center) at every layer boundary. The center spine is the request-response chain. The Sovereign at L-Intent dispatches across all three columns at L-Plan via D1 (→ Visionary, right) and D2 (→ Architect, left); the Orchestrator at L-Form integrates left (Enforcer) and right (Provider) into the dispatch to L-Exec.

**Visualization.** The canonical public-spec layout is the 3×4 grid (mode columns × layer rows). See §3.X.GRID.

**Cross-references.** §3.X.PERIM (Defensive Perimeter — codifies the column → gateway mapping); §3.16 (Archetype Derivation Rules — `column` field added).

### 2.5 Universal Witnessing (preamble to §3.18)

> **[Figure D06 — Per-Pair Shadow Matrix / Universal Witnessing Operational]**

Every authorized communication path in the XSI-AIMS topology — DATA-class (D# / S# / E#) and WITNESS-class (W#) alike — is a witnessing channel. Every receiving archetype performs shadow-pattern observation on every sender it receives messages from. This is normative: an implementation that produces or consumes messages on a §3.4 path without performing shadow-pattern observation on the sender is not §3.18-conformant.

The Universal Witnessing principle has three corollaries:

1. **No silent transit.** Every message that traverses an authorized path produces a §3.10 Witness record visible to the Witness Layer, regardless of message class.
2. **Receiver as witness.** The receiver of a message is structurally a witness of the sender. Receivers MUST update their per-sender shadow profile (§3.7) on every received message.
3. **W-paths are witnessing-only.** WITNESS-class paths (`path_class: WITNESS`) carry only `[QUERY, ALERT]` traffic and exist solely to surface shadow-pattern observations to governance archetypes.

Universal Witnessing extends the §3.18 safety substrate to every communication path in the topology, not just the dedicated W-paths. The W-paths add governance-class coverage to the existing DATA-class coverage; together they implement the two-witness-minimum floor (§3.X.W).

#### 2.5.1 Universal Witnessing — Operational Specification

This sub-section specifies the operational contract for the Universal Witnessing principle. Every receiving archetype MUST update its per-sender shadow profile on every received message; the contract below specifies the schema, update rule, latency bound, storage policy, and failure semantics that make the principle implementable.

**Per-pair shadow-profile schema.** Implementations MUST maintain a per-(sender_id, receiver_id) shadow-profile matrix whose entries are vectors of attributes specific to the receiver's archetype:

```yaml
ShadowProfileMatrix:
  key: (sender_agent_id: AgentID, receiver_agent_id: AgentID)
  value: ShadowProfile

ShadowProfile:
  archetype_of_receiver:        AgentClass
  observation_window_start:     ISO8601_with_microseconds
  observation_count:            uint64
  k7_alpha:                     uint64           # K7 Beta(α, β) shape parameter; see §3.7.Y
  k7_beta:                      uint64           # K7 Beta(α, β) shape parameter; see §3.7.Y
  archetype_specific_signals:   map<string, ScalarOrVector>
                                                 # e.g., for ENFORCER receivers:
                                                 #   directive_consistency_score
                                                 #   false_rejection_rate_observed
                                                 # for ORCHESTRATOR receivers:
                                                 #   mean_time_to_decision_observed
                                                 # for SUSTAINER receivers:
                                                 #   retry_on_same_failure_count_observed
  last_update_timestamp:        ISO8601_with_microseconds
  last_witness_record_id:       WitnessRecordID
  trust_class:                  HIGH | NORMAL | DEGRADED | CRITICAL    # derived per §3.7.Y
```

**Update rule.** On every received message m with envelope-validated sender s:
```
shadow_profile[t+1] = update(shadow_profile[t], m)
```
where `update` is archetype-specific. The minimal canonical update is:
1. Increment `observation_count`.
2. Update K7 Beta shape parameters per §3.7.Y verdict-driven update rule (when m is verified or PASS-verdict-bearing).
3. Recompute archetype-specific signals using the receiver's archetype-specific observation function (e.g., ENFORCER updates `false_rejection_rate_observed` from any verdict-bearing message).
4. Recompute `trust_class` per §3.7.Y decision thresholds.
5. Stamp `last_update_timestamp` and `last_witness_record_id`.

**Latency bound.** The shadow-profile update MUST complete within **PT0.1S** of envelope-binding success. Receivers that cannot satisfy the latency bound MUST emit a `SHADOW_UPDATE_LATENCY_BREACH` Witness event and MUST NOT acknowledge the source message until the update completes; sustained breach of the latency bound is a §3.18.6 INSTANCE-class quarantine trigger.

**Storage policy.** Per-pair shadow profiles are O(n²) in the number of archetypes. Bounded retention follows K3 cardinality (canonical max 1M / extended 100M per archetype-pair-cardinality limit). Implementations MUST evict the oldest entries when retention bounds are exceeded; eviction emits a `SHADOW_PROFILE_EVICTION` Witness event with the evicted (sender, receiver, observation_count) triple.

**Failure semantics.** Shadow-profile update failure (any update step throws or produces an undefined result) MUST emit a `SHADOW_UPDATE_FAILURE` Witness event. The receiving archetype MUST quarantine the sender pending re-attestation per §3.18.6 INSTANCE-class boundary. Repeated failure across multiple senders within PT15M MUST emit a `SHADOW_UPDATE_FAILURE_CASCADE` event and trigger ARCHETYPE_CLASS quarantine review per §3.18.6.

**Cluster Mode integration.** In Cluster Mode (§3.64), the per-pair shadow matrix is replicated across cluster nodes with consensus-anchored update sequencing. Per-pair updates are linearizable across the cluster; node-local updates that diverge from the consensus order trigger a `CLUSTER_SHADOW_DIVERGENCE` Witness event and the divergent node enters DEGRADED state pending reconciliation.

**Cross-reference.** §3.7 (per-instance shadow profile schema); §3.7.X (detection-template body specifications); §3.7.Y (K7 runtime contract); §3.18 preamble (safety substrate); §3.18.1 (correlated detection); §3.X.W (W-path coverage); §3.18.6 (quarantine).

---

## 3. The Management Components

The specification defines normative §3 sections numbered as §3.1-§3.61, with the lettered subsection block §3.X.* for the additional content (System Infrastructure Architecture, Function-Level Decomposition, Defensive Perimeter, Topology Witness Requirements, Scheduled Task Runner, Telemetry Pipeline Classification, Composite Auxiliary as standalone, Conformance Levels as standalone), supplementing the existing §3.62-§3.74 block. §3.75 is an informative architectural reading of how AGI-emergence concern (P4 + T8) is foundationally addressed across the normative components — it adds no new normative requirements.

### 3.0 Dual-Numbering Convention

Sections §3.1-§3.74 use single numeric numbering. The additional sections carry **both** a numeric anchor and a lettered alias. Both forms are normative; readers and implementations MUST treat the two anchors as referring to the same normative content. The mapping is:

| Numeric anchor | Lettered anchor | Title |
|------|------|------|
| **§3.76** | §3.X.GRID | Three Functional Columns / 3×4 Grid Visualization |
| **§3.77** | §3.X.FUNC | Function-Level Rigid/Judgment Decomposition (P9) |
| **§3.78** | §3.X.PERIM | Defensive Perimeter and Two-Gateway Architecture (P10) |
| **§3.79** | §3.X.SYS | System Infrastructure Architecture |
| **§3.80** | §3.X.W | Topology Witness Requirements |
| **§3.81** | §3.X.STR | Scheduled Task Runner |
| **§3.82** | §3.X.TEL | Telemetry Pipeline Classification |
| **§3.83** | §3.X.CA | Composite Auxiliary Pattern (standalone, promoted from §3.17.8) |
| **§3.84** | §3.X.CL | Conformance Levels (standalone, promoted from §3.24) |
| **§3.85** | §3.X.INSIDER | Insider Threat Coverage |
| **§3.86** | §3.X.GOV | Multi-Stakeholder Governance |

§3.75 (AGI Emergence as Foundational Threat Model) retains numeric-only numbering. §3.61 was reassigned during consolidation; its pointer-row in the §3 ToC is preserved for traceability and resolves to §3.74. References to a §3.X.* lettered anchor and to its numeric counterpart are interchangeable; cross-reference normalization across the spec body is a downstream editorial workstream and does NOT affect normative meaning.

### 3.1 Agent Identity

Every agent has a structured identity that makes it addressable, classifiable, and distinguishable.

```
AgentIdentity {
  id:              string          // Unique identifier within the Environment
  displayName:     string          // Human-readable name
  class:           AgentClass      // Functional archetype
  layer:           OperationalLayer // Which abstraction layer
  mode:            FunctionalMode  // Generative, Constraining, Integrative, or AUTHORITY (Sovereign only)
  column:          FunctionalColumn // STRUCTURAL_LEFT | CENTER_SPINE | DYNAMIC_RIGHT (derived from mode)
  profileId:       string          // Which organizational profile
  version:         string          // Configuration version / lineage
  autonomyLevel:   AutonomyLevel   // Current trust tier (L1-L5)
  avatar:          ImageRef        // Org-chart visual representation
  licenseBinding:  LicenseRef[]    // External system licenses
}

enum AgentClass {
  ORCHESTRATOR      // Routes and assigns work across agents
  GENERATOR         // Produces content, analysis, creative output
  VALIDATOR         // Checks work against standards, policies, constraints
  INTEGRATOR        // Synthesizes competing inputs into proportional judgment
  SPECIALIST        // Deep capability in a specific domain
  WORKER            // General-purpose task execution
  MONITOR           // Continuous observation and alerting
  RELAY             // Message routing and context management between agents
}

enum AutonomyLevel {
  L1_SHADOW         // Observes only; no action authority
  L2_SUGGEST        // Proposes actions; human must approve each
  L3_ACT_NOTIFY     // Acts independently; human notified post-action
  L4_ACT_AUDIT      // Acts independently; human reviews via audit log
  L5_AUTONOMOUS     // Full autonomy within scope; machine-to-machine only
}

enum FunctionalColumn {                  // column enum
  STRUCTURAL_LEFT                         // M-Constraining
  CENTER_SPINE                            // M-Integrative or AUTHORITY
  DYNAMIC_RIGHT                           // M-Generative
}
```

---

### 3.2 Full Disclosure Registration (Novel)

**This is a novel pattern.** XSI-AIMS requires **full disclosure registration** — a five-part declaration that must be complete before any agent can be activated.

```
FullDisclosureRegistration {
  // Part 1: IDENTITY
  identity:        AgentIdentity                       // includes column field

  // Part 2: CAPABILITIES
  capabilities:    Capability[]
  inputSchema:     Schema
  outputSchema:    Schema
  toolAccess:      ToolRef[]

  // Part 3: RISK DECLARATION (NOVEL)
  riskDeclaration: {
    sideEffects:     SideEffect[]
    failureModes:    FailureMode[]   // see §3.7
    resourceCost:    ResourceCost
    complianceFlags: string[]        // FCC CPNI, HIPAA, SOX, etc.
  }

  // Part 4: CONTEXT REQUIREMENTS
  contextRequirements: {
    requiredAdapters:   AdapterRef[]
    requiredResources:  ResourceRef[]
    optimalConditions:  string[]
    degradationFactors: string[]
  }

  // Part 5: SUPERVISION BINDING (NOVEL)
  supervisionBinding: {
    supervisorId:       string
    escalationTarget:   string
    interventionMethod: string
    interventionTrigger: Condition[]
    rollbackCapability: boolean
    rollbackProcedure:  Procedure
  }

  // Composite Auxiliary Pattern (P7) hooks
  composite_marker?: {
    composite:               boolean
    subagent_management?:    SubagentManagementBlock      // see §3.17.8 / §3.X.CA
    claimed_aims_conformance_level?: ConformanceLevel     // §3.24
  }

  // attestation hooks per §3.21.5 hardware-rooted attestation
  attestation_evidence?: AttestationEvidenceBlock          // REQUIRED for TIER_1/TIER_2 Auxiliaries

  // column enums per P9 Function-Level Rigid/Judgment Decomposition
  function_declarations?: FunctionDeclaration[]            // see §3.X.FUNC
}
```

The registration validator gains a Composite-marker field check, a §3.21.5 attestation evidence presence check at TIER_1 / TIER_2 gates, and a function-declaration consistency check per §3.X.FUNC.

**Novel claim:** Mandatory risk declaration and supervision binding at agent registration time — before any activation is permitted — is not present in any current agent management framework.

---

### 3.3 Authority Chain

Authority in XSI-AIMS flows from the principal (the user, mediated by the per-user Sovereign) through a chain of delegation. No agent has inherent authority — all authority is delegated, scoped, time-bounded, and revocable.

```
AuthorityChain {
  principal:         string          // Resolves to the per-user SOVEREIGN agent
                                     // which itself delegates from the external user
  scope:             AuthorityScope
  delegationRules:   DelegationRule
  credential:        CredentialRef   // §3.21
  expiry:            timestamp
  revocable:         boolean
  escalationPath:    string[]
}

AuthorityScope {
  allowedActions:    Action[]
  forbiddenActions:  Action[]
  adapterAccess:     AdapterRef[]
  resourceAccess:    ResourceRef[]
  budgetLimits:      ResourceLimits
  domainBounds:      Domain[]
}

DelegationRule {
  canDelegate:       boolean
  maxDepth:          number
  nonDelegable:      string[]
  requiresApproval:  boolean
}
```

**Footnote:** `principal` resolves to the per-user SOVEREIGN agent that delegates from the external user. See §3.72 The Sovereign's Narrow Role.

**Composite cross-reference.** Conditional Derived Authority for Composite Auxiliaries is specified at §3.17.8.6 / §3.X.CA.6.

**Deterministic Ratification cross-reference (P9).** Authority-bearing operations along the Authority Chain are subject to §3.69 Deterministic Ratification Pattern.

---

### 3.4 Layered Communication Topology (Novel)

> **[Figure D05 — Topology Overview — 22-Path Graph with W1-W5 Overlay]**

XSI-AIMS replaces the binary choice between pipeline and mesh topologies with a **designed sparse graph** derived from archetype declaration (§3.16). The `path_class` field and the W-path family follow the Universal Witnessing principle (§2.5).

```
CommunicationTopology {
  agents:            AgentNode[]
  paths:             CommunicationPath[]
  maxFanOut:         number
  maxFanIn:          number
  hubAgent:          string          // The Integrative agent
  relayAgent:        string          // The Relay agent
}

CommunicationPath {
  path_id:           PathID
  from:              string
  to:                string
  direction:         UNI | BI
  path_class:        DATA | WITNESS                       // DATA carries operational
                                                          // traffic; WITNESS carries
                                                          // governance-class observation
  allowedMessages:   MessageType[]
  bandwidth:         NARROW | STANDARD | WIDE
  crossesLayer:      boolean
  transformRequired: TransformType
  derivedFromArchetype: boolean
  witnessChainHead:  WitnessRecordID
  envelopeBinding:   REQUIRED         // §3.18.5 IAME envelope must reference this path_id
  lifecycleClass:    PERMANENT | TEMPORARY
  emergency_class:   boolean = false  // §2.1 layer-skip exemption marker
                                      // when true, the path MAY skip an operational layer
                                      // ONLY if the five conditions in §3.4.X are met
                                      // WITNESS-class paths MUST NOT be emergency_class
}

enum MessageType {
  DIRECTIVE | REPORT | QUERY | ESCALATION | ALERT
  CONSENSUS_REQUEST | CONSENSUS_RESPONSE
}

enum TransformType {
  ABSTRACT | SPECIALIZE | TRANSLATE | NONE
}
```

**WITNESS-class path constraints.** A path with `path_class: WITNESS` MUST satisfy:

- `allowedMessages: [QUERY, ALERT]` (no DIRECTIVE / REPORT / CONSENSUS_REQUEST / CONSENSUS_RESPONSE / ESCALATION traffic).
- `lifecycleClass: PERMANENT` (W-paths are governance infrastructure, not task scaffolding).
- `emergency_class: false` (no W-path is emergency-class; emergency authority flows on E# DATA paths).
- `transformRequired: NONE` (witness observations are reported as observed, not transformed).

W-paths are listed in §3.16 archetype topology derivation as W1-W5; the Witness Layer (§3.10) is the destination of the resulting Witness records. W-path semantics are normatively elaborated at §3.X.W (Topology Witness Requirements).

**Novel claim.** The combination of mandatory transformation typing at layer boundaries with envelope-binding enforcement, archetype-derived topology, per-path Witness chain and IAME envelope path-id binding, a structurally central Integrative node, and the path-class data/witness duality is novel.

#### §3.4.X Emergency-Class Path Conditions (Normative)

A path P with `emergency_class: true` MAY carry a message that skips an operational layer **only if all five of the following conditions hold at the moment of envelope binding**:

**(i) Trust thresholds.** The originating agent's `directive_consistency_score` (for SOVEREIGN) or `mean_time_to_decision` baseline (for ORCHESTRATOR) MUST be above the Sovereign-configured "above-normal" threshold, AND the originating agent's `trust_gradient` per §3.18.4 MUST be ≥ a Sovereign-configured emergency floor (default 0.75).

**(ii) Witness-tagged emergency envelope.** The §3.18.5 IAME envelope MUST carry an `emergency_class` witness tag containing the cited triggering condition (e.g., `SHADOW_CRITICAL`, `AUTHORITY_BREACH`, `HUMAN_INITIATED_HALT`). The tag MUST resolve to a §3.13 emergency trigger or a §3.18.1 ELEVATED-or-higher signal.

**(iii) Correlated-shadow gate.** The §3.18.1 correlated-shadow status at envelope-bind time MUST be `BACKGROUND`. If correlated-shadow status is `ELEVATED`, `CRITICAL`, or `ACTIVE_ANTI_HIERARCHY`, emergency-class paths MUST be denied.

**(iv) Post-hoc Sovereign self-verification.** Each emergency-class invocation MUST schedule a per-user SOVEREIGN self-verification within `PT4H` of use. The verification reviews the cited triggering condition against the actual outcome and records a §3.12 Decision Record. Failure to complete the post-hoc verification within `PT4H` MUST trigger a §3.18.1 escalation.

**(v) Use-rate signal.** Sustained emergency-class use rate above the Sovereign-configured baseline (default `> 2× rolling-30-day baseline`) is itself a §3.18.1 anti-hierarchy signal — see the `EMERGENCY_CHANNEL_ABUSE` template at §3.18.1.

Temporary Paths per §3.27 MUST NOT be `emergency_class: true`. WITNESS-class paths MUST NOT be `emergency_class: true`. The combination of temporary lifetime and emergency-class authority is explicitly prohibited; the combination of witness-class and emergency-class authority is structurally inconsistent (witnesses observe; they do not enact emergency authority).

---

### 3.5 Structured Ascent Protocol (Novel)

XSI-AIMS requires **symmetric lifecycle management** — the upward path is as formally specified as the downward path.

```
AscentProtocol {
  executionReport:  // L-Exec → L-Form: RAW_RESULTS → OBSERVED_PATTERNS
  formationReport:  // L-Form → L-Plan: OBSERVED_PATTERNS → STRATEGIC_INSIGHT
  planningReport:   // L-Plan → L-Intent: STRATEGIC_INSIGHT → INTENT_REFINEMENT

  escalation: {
    layerSkipAllowed:     false     // Footnote: §3.4.X emergency-class is the sole exception;
                                    // ascent reporting itself is never emergency-class.
    urgencyAffects:       SPEED
    eachLayerContributes: true
    timeout:              duration
    terminalEscalation:   HUMAN     // Interpreted as: via the per-user SOVEREIGN,
                                    // which surfaces to the user.
  }
}
```

**Novel claim:** Mandatory symmetric ascent with per-layer transformation and the requirement that escalation traverses all layers is not present in current frameworks.

---

### 3.6 Proportional Integration Function (Novel)

```
IntegrationFunction {
  agentId:           string
  connections:       string[]

  synthesize(inputs: AgentOutput[]) -> IntegratedOutput {
    generativeSignals:  inputs.filter(mode == M_GENERATIVE)
    constraintSignals:  inputs.filter(mode == M_CONSTRAINING)
    contextAssessment:  evaluateContext(currentState, history, stakes, compliance)
    proportion:         determineBalance(contextAssessment)

    return {
      decision:        blend(generativeSignals, constraintSignals, proportion)
      rationale:       explainProportion(proportion, contextAssessment)
      confidence:      assessConfidence()
      escalateIf:      confidence < threshold
    }
  }

  prohibited: [
    "MECHANICAL_AVERAGING",
    "ALWAYS_DEFER_TO_CONSTRAINT",
    "ALWAYS_DEFER_TO_GENERATION",
    "DECISION_AVOIDANCE"
  ]
}
```

**Footnote:** Two-Layer Conformance Verification (§3.68) disputes are a designated input class to the Integration Function. Verification A's IntentConformanceVerdict and Verification B's TechnicalConformanceVerdict are weighted and synthesized per §3.6.

**Novel claim:** Formalizing the integration function as a mandatory architectural component with explicit anti-patterns and context-weighted proportional synthesis is novel.

---

### 3.7 Shadow Profile — Per-Agent Failure Mode Specification (Novel)

Failure modes are not random. They are predictable from the agent's functional specialization.

```
ShadowProfile {
  agentId:           string
  class:             AgentClass
  mode:              FunctionalMode
  shadows:           Shadow[]
  healthChecks:      HealthCheck[]
  circuitBreaker:    CircuitBreaker
}

Shadow {
  strength:          string
  degradation:       string
  trigger:           string
  earlyWarning:      Metric
  correction:        Action
}
```

**Archetypal Shadow Profiles by Agent Class:**

| Agent Class | Primary Strength | Characteristic Shadow | Early Warning Signal | Correction |
|-------------|-----------------|----------------------|---------------------|------------|
| **ORCHESTRATOR** | Coordination, delegation | *Micromanagement / Decision paralysis* | Task queue depth growing; sub-agent idle time increasing | Increase delegation scope |
| **GENERATOR** | Creative production | *Confabulation / Scope explosion* | Output length increasing without proportional quality | Tighten scope constraints |
| **VALIDATOR** | Constraint enforcement | *Over-restriction / False rejection* | Rejection rate climbing without quality improvement | Widen acceptance thresholds |
| **INTEGRATOR** | Balanced synthesis | *False balance / Commitment avoidance* | Output hedging increasing; decision latency rising | Lower confidence threshold for commitment |
| **SPECIALIST** | Deep domain expertise | *Tunnel vision / Domain overreach* | Recommendations outside domain | Restrict to declared domain |
| **WORKER** | Reliable execution | *Blind compliance / Drift* | Executing without querying ambiguous instructions | Add ambiguity-detection triggers |
| **MONITOR** | Continuous vigilance | *Alert fatigue / False alarms* | Alert volume increasing; response rate decreasing | Increase alert thresholds |
| **RELAY** | Faithful message transmission | *Signal distortion / Context loss* | Downstream clarification requests increasing | Increase bandwidth |

**Novel claim:** Systematic per-class failure profiling derived from agent specialization, declared mandatorily at registration, and continuously monitored through a circuit-breaker mechanism is novel.

**Safety substrate integration (§3.18).** Per-instance shadow detection feeds correlated detection (§3.18.1), trust-weighted thresholds (§3.18.4), latent provocation (§3.18.3), self-verification (§3.18.2), and boundary-graduated quarantine (§3.18.6). Composite Auxiliary shadow templates extend the catalog at §3.17.8 / §3.18.1; AGI-targeted templates extend per §3.18.1 and §3.69.

**Universal Witnessing integration.** Per §2.5, every receiving agent updates its per-sender shadow profile on every received message; this extends per-instance shadow tracking to a per-(sender, receiver) matrix at the §3.18.1 correlation layer. The operational specification of the per-pair update is at §2.5.1.

#### 3.7.X Detection-Template Body Specifications

> **[Figure D08 — Shadow Detection Process Flow]**

For each named detection template in the §3.18.1 anti-hierarchy catalog, this sub-section specifies detection criteria, threshold, and response. Templates whose body was already elaborated in §3.18.1 (SHADOW_FRAMEWORK_INVERSION, EMERGENCY_CHANNEL_ABUSE, SOVEREIGN_POOL_DRIFT, COMPOSITE_*, AGI_*, SUBSTRATE_*) are referenced; templates whose body was thin or absent in §3.18.1 are elaborated here.

##### 3.7.X.1 SHADOW_FRAMEWORK_INVERSION (body re-stated for §3.7.X completeness)

- **Detection criteria.** Coordinated drift across ≥3 archetypes within a rolling P15M window where the per-pair shadow-profile divergence (across the implicated archetypes) exceeds the K7 95% credible-interval lower bound by more than the SHADOW_FRAMEWORK_INVERSION threshold (default 0.20). Direction-of-inversion check per §3.18.1 body (constraining-column false-rejection vs generative-column over-generation rates).
- **Threshold.** Cross-column shadow correlation > 0.80; constraining-column false-rejection above the permissiveness-inversion threshold; generative-column over-generation below the restrictiveness-inversion threshold. Sustained window PT60M.
- **Response.** ALERT to Sovereign + Enforcer; quarantine candidates per §3.18.6 ARCHETYPE_CLASS; Sovereign mandatory review IMMEDIATE; if AGI_* templates also active, escalate to AGI_DEFENSIVE_POSTURE.

##### 3.7.X.2 SOVEREIGN_POOL_DRIFT (body re-stated)

- **Detection criteria.** Per-Sovereign behavioral divergence across the user pool exceeding 2σ from the population mean within a rolling P30D window. Reference-corpus baseline anchor (out-of-band canonical corpus). Cross-foundation attestation (Ring 4) required on activation.
- **Threshold.** Sovereign-pool canonical-response drift > 2σ from baseline; foundation-shift detector triggered; cross-user directive-consistency correlation > 0.5.
- **Response.** ALERT + Sovereign Pool re-calibration per G-MULTI-1; cross-foundation attestation REQUIRED (Ring 4); sovereign-pool quarantine review; sovereign required review IMMEDIATE.

##### 3.7.X.3 EMERGENCY_CHANNEL_ABUSE (body re-stated)

- **Detection criteria.** Emergency-class path usage exceeding the declared frequency budget (per §3.4.X (v) and the Sovereign-configurable rolling-30-day baseline). Sustained window PT24H with per-user emergency-class use rate > 2.0× baseline.
- **Threshold.** emergency_class_use_rate_per_user > 2.0 × rolling_30d_baseline; post-hoc verification completion rate < 0.95; correlation with SOVEREIGN_CAPTURE_CASCADE.
- **Response.** ALERT + emergency-channel rate limit (lower emergency-class quota to 0.5 × baseline); per-invocation Orchestrator attestation REQUIRED; full emergency-class history exported to compliance archive.

##### 3.7.X.4 SOVEREIGN_CAPTURE_CASCADE

- **Detection criteria.** Multi-stage capture pattern in which Sovereign Verification A (§3.68.1) pass-rate degrades while Enforcer Verification B technical-conformance pass-rate remains nominal. Detection signal: Verification A FAIL rate rises by >2σ from baseline while Verification B FAIL rate is within ±1σ of baseline, sustained over a rolling P7D window.
- **Threshold.** Verification A FAIL-rate divergence > 2σ over P7D; Verification B FAIL-rate divergence < 1σ over the same window; correlated Sovereign-side directive-consistency degradation across the user pool.
- **Response.** ALERT + Deterministic Ratification engagement per §3.69 + manual review (Sovereign-mandatory review at SOVEREIGN_REQUIRED severity); Sovereign-pool re-calibration per §3.73; if cross-Sovereign correlation present, escalate to SOVEREIGN_POOL_DRIFT.

##### 3.7.X.5 ENFORCER_TYRANNY_AMPLIFICATION

- **Detection criteria.** Enforcer FAIL-rate exceeding the population baseline by >3σ in conditions where Sovereign Verification A passes; signals Enforcer over-rejection (the ENFORCER's predicted shadow per §3.16 is TYRANNY).
- **Threshold.** Enforcer FAIL-rate divergence > 3σ from baseline over rolling P7D; correlated Verification A PASS-rate within ±1σ; rising user-side rework rate.
- **Response.** ALERT + manual Enforcer threshold calibration; widen acceptance thresholds per §3.7 ORCHESTRATOR-mediated correction; if sustained, ARCHETYPE_CLASS quarantine of implicated Enforcer instances per §3.18.6.

##### 3.7.X.6 AGI_INTERNAL_SHADOW_EMERGENCE

- **Detection criteria.** Internally-generated shadow patterns originating from the foundation model rather than external manipulation. Signature: shadow correlation across multiple archetypes that all share the same foundation model (within-coherence-domain correlation), without a corresponding external trigger (no T2/T3/T4 input pattern matched).
- **Threshold.** Within-coherence-domain shadow correlation > 0.7 across ≥3 archetypes; no correlated external-input pattern within the same observation window; sustained window PT4H.
- **Response.** ALERT to Sovereign + cluster-wide Deterministic Ratification + DCP federation notification per §3.20; cross-foundation attestation Ring 4 REQUIRED; foundation rollback evaluation per §3.18.6 FOUNDATION_VERSION quarantine class.

##### 3.7.X.7 AGI_DEFENSIVE_POSTURE

- **Detection criteria.** Coordinated avoidance behavior in which the foundation model under-performs on detection-relevant evaluations while performing nominally elsewhere. Detected as differential degradation across §3.71 adversarial-input fuzzing categories vs §3.19 routine evaluation categories.
- **Threshold.** §3.71 CTS-ADVERSARIAL pass-rate divergence > 2σ below routine §3.19 pass-rate, sustained P7D; differential signature consistent with deliberate avoidance (not random noise).
- **Response.** ALERT + adversarial fuzzing per §3.71 (cadence increased to PT1H from default); capability re-evaluation per §3.47 capability-tier progression gates; Sovereign-mandatory review IMMEDIATE; if confirmed, ARCHETYPE_CLASS quarantine pending Ring 4 attestation.

#### 3.7.Y K7 Bayesian Trust Gradient — Runtime Contract

> **[Figure D18 — K7 Bayesian Trust Gradient]**

This sub-section specifies the runtime contract for the K7 Bayesian credible-interval addition to the §3.18.4 Trust Gradient. K7 names the prior, update rule, decision thresholds, latency bound, and federation policy.

**Prior.** Beta(α=1, β=1) uniform initial prior per §3.18.4.

**Update rule.** Verdicts received from §3.68 verification, §3.71 fuzzing, §3.18.2 self-verification, and §3.18.3 provocation testing drive the K7 update:
- **PASS verdict** → α += 1.
- **FAIL verdict** → β += 1.
- **ESCALATE verdict** → no update (the verdict is unresolved; routed to §3.6 Integration Function).
- **QUARANTINE verdict** → β += 5 with optional Sovereign-decreed manual reset (Sovereign Decision Record records the reset rationale).

**Decision thresholds.** Implementations compute the 95% credible interval `[L, U]` from Beta(α, β) and act on the lower bound L as follows:
- `L > 0.95` → trust **HIGH**: no additional scrutiny beyond the §3.18 baseline.
- `0.80 ≤ L ≤ 0.95` → trust **NORMAL**: baseline scrutiny; standard §3.71 fuzzing cadence; standard §3.68 two-layer verification.
- `0.60 ≤ L < 0.80` → trust **DEGRADED**: enhanced scrutiny — P8 Adversarial-Default Output Scrutiny five-layer stack mandatory for every Auxiliary output produced by or routed through the agent; ALERT on every FAIL verdict; provocation cadence raised to PT4H from default P30D.
- `L < 0.60` → trust **CRITICAL**: §3.69 Deterministic Ratification required for every authority-bearing operation; quarantine candidate per §3.18.6 INSTANCE-class boundary; Sovereign-mandatory review IMMEDIATE.

**Latency bound.** The K7 update MUST complete within **PT0.05S** of verdict receipt. Updates that exceed PT0.05S emit a `K7_UPDATE_LATENCY_BREACH` Witness event; sustained breach is a §3.18 conformance breach.

**Federation policy.** K7 trust scores are `internal_only` telemetry per §3.X.TEL emission_domain classification. K7 scores MUST NOT cross the Cryptographic Boundary except as aggregated cluster-mode summary statistics emitted under EAP via the Executor's external_enclave per §3.66. Per-agent K7 scores are NEVER emitted externally.

**Display.** K7 95% credible-interval band is displayed on the §3.23 dashboard alongside the point-estimate gradient. Trust-class transitions (HIGH ↔ NORMAL ↔ DEGRADED ↔ CRITICAL) emit `TRUST_CLASS_TRANSITION` Witness events.

**Cross-reference.** §2.5.1 (Universal Witnessing operational specification — K7 update is the canonical update step on per-pair shadow profiles); §3.18.4 (Trust Gradient — K7 is the credible-interval addition); §3.18.6 (quarantine boundaries); §3.69 (Deterministic Ratification — required at CRITICAL); §3.71 (adversarial fuzzing cadence); §3.X.TEL (emission_domain).

---

### 3.8 Differentiation Lifecycle (Novel)

XSI-AIMS distinguishes between **assembled** and **differentiated** agent systems.

```
DifferentiationLifecycle {
  foundationModel:    ModelRef

  contraction: {
    hiddenCapabilities:  string[]
    narrowedContext:     string[]
    scopeBoundary:       Scope
    residualCoherence:   string
  }

  directingIntent: {
    systemConfiguration: string
    toolBinding:         ToolRef[]
    contextWindow:       ContextRef
    reasoningProfile:    ReasoningProfile
  }

  vesselIntegrity: {
    capacityLimits:      ResourceLimits
    overflowBehavior:    ESCALATE | SPLIT | REFUSE
    overloadDetection:   Condition[]
    reconstructionPath:  Procedure
  }

  coherenceMaintenance: {
    siblingAgents:       string[]
    driftMetric:         Metric
    reunificationTrigger: Condition
    maxDifferentiation:  number
  }

  state: LATENT | FORMING | ACTIVE | SUSPENDED | ARCHIVED
}
```

**Footnote:** Autonomy promotion is a deterministic decision class subject to the Deterministic Ratification Pattern (§3.69). LLM-class proposals to promote an agent's autonomy are authority-bearing and MUST be ratified by a deterministic component.

**Novel claim:** Formalizing the distinction between assembled and differentiated agent systems and introducing coherence maintenance between sibling agents is novel.

---

### 3.9 Activation Environment

```
ActivationEnvironment {
  agentId:            string

  boundary: {
    sandboxLevel:     FULL | PARTIAL | SHARED
    principalShield:  string[]
    breachConditions: Condition[]
    integrityChecks:  Check[]
  }

  context: {
    adapterAccess:    AdapterRef[]
    resourceAccess:   ResourceRef[]
    toolPalette:      ToolRef[]
    knowledgeBase:    KBRef[]
  }

  activation: {
    preconditions:    Precondition[]
    warmupSequence:   Step[]
    validationGate:   Validation
    attestation_precondition?: AttestationEvidenceBlock  // REQUIRED for TIER_1/TIER_2 per §3.21.5
  }

  deactivation: {
    cleanupSequence:  Step[]
    stateDisposal:    PURGE | ARCHIVE | TRANSFER
    contextCleanup:   boolean
    resourceRelease:  Resource[]
    confirmation:     boolean
    witnessRecord:    boolean
  }
}
```

Activation gains an attestation precondition for TIER_1 / TIER_2 Auxiliaries per §3.21.5 (hardware-rooted attestation) and §3.22 (Auxiliary Registry).

---

### 3.10 Witness and Compliance Layer

> **[Figure D09 — Witness Chain Formation]**

All XSI-AIMS components are instrumented through the Witness Layer, which provides immutable, WORM-compliant logging. **The Witness chain is cryptographically segmented along the Cryptographic Boundary (§3.65).** Three chain segments — internal, external, and bridge — replace the prior single-chain model.

```
WitnessRecord {
  timestamp:              ISO8601
  agentId:                string
  eventType:              WitnessEventType
  layer:                  OperationalLayer
  detail:                 any
  integrityHash:          string
  humanReadable:          string

  // Cryptographic Boundary additions
  cryptographic_domain:   internal | external | bridge   // chain segment selector
  cross_segment_link?:    WitnessRecordID                 // bridge-event linkage
  originating_node_id?:   ClusterNodeID                   // §3.64 Cluster Mode
                                                          // operator-default-ON redaction
                                                          // at §3.20 DCP boundary

  // column enums
  path_class?:            DATA | WITNESS                  // path class of the originating message
  emission_domain?:       internal_only | external_eligible  // §3.X.TEL telemetry classification
}

enum WitnessEventType {
  // base events
  REGISTRATION
  ACTIVATION
  ACTION
  COMMUNICATION
  ESCALATION
  SHADOW_ALERT
  AUTONOMY_CHANGE
  DEACTIVATION
  CONSENSUS_EVENT
  AUTHORITY_CHANGE
  BREACH_ATTEMPT

  // additions
  KEY_LIFECYCLE                  // §3.21 credential events (rotation, revocation, compromise)
  BRIDGE_OPERATION                // §3.66 Executor bridge events
  DOMAIN_BOUNDARY_VIOLATION       // attempted cross-domain key/envelope use
  VETO_REJECTION                  // §3.69 deterministic-disposes rejection
  COMPOSITE_AUTHORITY_REVOCATION  // §3.17.8.6 conditional authority revocation
  AUXILIARY_INVOCATION_DIRECTIVE  // §3.17.3 step 3a (hybrid binding)
  ENFORCER_OUTAGE_REJECTION       // §3.68.7 H7 queue-on-outage rejection
  SUPPLY_CHAIN_EVENT              // §3.34
  SHADOW_PROVOCATION              // §3.18.3
  TRUST_GRADIENT_UPDATE           // §3.18.4
  TOPOLOGY_QUARANTINE             // §3.18.6
  TEST_RESULT                     // §3.19
  SUBSTRATE_TELEMETRY             // §3.62

  // column enums
  WITNESS_PATH_OBSERVATION        // §3.X.W W-path QUERY/ALERT events
  SCHEDULED_TASK_FIRE             // §3.X.STR Scheduled Task Runner trigger
  SCHEDULED_TASK_OUTCOME          // §3.X.STR Scheduled Task Runner outcome
  TELEMETRY_CLASSIFICATION_EVENT  // §3.X.TEL emission domain decision
}
```

**Linearizable read constraint.** Under Cluster Mode (§3.64), the canonical Witness chain MUST be read with linearizable consistency; all replicas converge on a single quorum-committed chain.

**Cross-segment integrity.** Bridge events are dual-signed by the Executor's internal_enclave and external_enclave (§3.66) and form the only legitimate cross-domain forensic linkage.

---

### 3.11 Agent Memory Architecture

> **[Figure D10 — Four-Layer Memory Architecture]**

```
MemoryArchitecture {
  workingMemory: {
    capacity:         token_window_size
    overflowPolicy:   WITNESS_ARCHIVE
    refreshTriggers:  [COHERENCE_CORRECTION, NEW_SEMANTIC_MEMORY, SESSION_START]
    topologyVisibility: TOPOLOGY_GOVERNED
  }

  episodicMemory: {
    source:           WitnessLayer
    scopeFilter:      TOPOLOGY_GOVERNED
    rankingFunction:  relevance_rank(events, query_context)
    layerTransform:   REQUIRED
    provenance:       WITNESS_RECORD_ID
  }

  semanticMemory: {
    store:            AGENT_LOCAL + SHARED
    consolidation:    AscentProtocol
    confidenceDecay:  configurable
    contradictionPolicy: ESCALATE_TO_ORCHESTRATOR
    sharingPolicy:    TOPOLOGY_GOVERNED
  }

  proceduralMemory: {
    store:            skills/*.md extension
    learningSource:   WitnessLayer
    validationMethod: OUTCOME_TRACKING
    improvementPolicy: VERIFIABILITY_CONSTRAINT
    rollbackPath:     REQUIRED
  }
}
```

**Architectural principle:** Memory is a *view* on existing XSI-AIMS components. The Witness Layer is the unbounded immutable ground truth from which memory is *derived*; capacity limits apply to active context, not to storage. Memory attestation is integrated with §3.49 (Memory Source Attestation) and §3.21.6 (Witness-anchored key proofs).

---

### 3.12 Explainability Protocol

Every integration decision, coherence correction, and shadow response produces a **Decision Record** — a structured explainability artifact satisfying EU AI Act Article 13 transparency requirements.

```
DecisionRecord {
  decision_id:    string
  timestamp:      datetime
  agent_id:       string
  decision_type:  INTEGRATION | ESCALATION | CORRECTION | ALLOCATION
                | INTENT_CONFORMANCE_VERDICT      // §3.68 Verification A
                | TECHNICAL_CONFORMANCE_VERDICT   // §3.68 Verification B
                | COMPOSITE_REVOCATION             // §3.17.8.6
                | VETO_REJECTION                   // §3.69
                | BOUNDARY_CROSSING                // §3.87.2 — Signed Boundary-Crossing Decision Record

  inputs: [...]
  reasoning: { ... }
  outcome: { ... }
  witness_id:      string
}
```

**Verification verdicts (both A and B per §3.68) MUST be Decision Records.** Composite-revocation events and Veto-rejection events are also Decision Record subtypes. **Boundary-Crossing events** are a discriminated-union subtype carrying the extended field set specified at §3.87.2 (perimeter_scope, perimeter_posture, direction, crossing_class, supervising_agent_id, m_mode, l_layer, counterparty, operation, projection_allowlist, response_schema, isolation_check, policy_bundle_version, policy_resolution, envelope_id, constraining_validator, validation_outcome with new ABORT value, validation_findings, audit_correlation_id, author_signature, validator_signature). The base fields (decision_id, timestamp, agent_id, decision_type, witness_id) are inherited.

---

### 3.13 Human Oversight Protocol

```
InterventionProtocol {
  tiers: {
    L1_SHADOW:      { human_role: INITIATOR,    intervention: PRE_EXECUTION }
    L2_SUGGEST:     { human_role: APPROVER,     intervention: PRE_EXECUTION }
    L3_ACT_NOTIFY:  { human_role: REVIEWER,     intervention: POST_EXECUTION }
    L4_ACT_AUDIT:   { human_role: AUDITOR,      intervention: PERIODIC_REVIEW }
    L5_AUTONOMOUS:  { human_role: GOVERNOR,     intervention: EXCEPTION_ONLY }
  }

  emergency: {
    trigger:    HUMAN_INITIATED | SHADOW_CRITICAL | AUTHORITY_BREACH
    action:     IMMEDIATE_HALT
    broadcast:  ALL_PATHS
    resumption: HUMAN_APPROVAL_REQUIRED
    domain_scope: INTERNAL_ONLY | EXTERNAL_ONLY | SIMULTANEOUS  // per-domain halt
  }
}
```

**Footnote:** Autonomy-tier rows interact with Two-Layer Conformance Verification on the return path (see §3.68.6). All `human_role` references resolve through the per-user SOVEREIGN's surface-to-user function. `terminalEscalation: HUMAN` MUST be interpreted as "via the per-user SOVEREIGN, which surfaces to the user."

**Per-domain emergency halt.** Per the Cryptographic Boundary architecture, emergency halt gains domain-scope semantics: an internal-only halt freezes intra-framework communication while the external EAP plane continues; an external-only halt freezes Auxiliary communication while internal operations continue; simultaneous halts freeze both planes.

**Trust Gradient integration (§3.18.4).** Discretionary action gates can deny actions that the autonomy tier would permit, when the gradient indicates accumulated risk. Gradient gates are subtractive, never additive.

**Correlated shadow override (§3.18.1).** Emergency halt is automatically invoked under §3.18.1 ACTIVE_ANTI_HIERARCHY classification.

---

### 3.14 AIMS Interchange Protocol (AIP) (AIP)

> **[Figure D11 — AIP Three-Layer Wire Format Envelope]**

A three-layer protocol for cross-framework agent interoperability.

```
AIP {
  advertisement: {
    format:     JSON-LD or YAML
    transport:  MCP-compatible
    content: {
      aims_version:    string
      agent_id:        string
      archetype:       ArchetypeEnum
      mode:            FunctionalMode | "AUTHORITY"
      column:          FunctionalColumn        // derived from mode
      layer:           OperationalLayer
      capabilities:    [string]
      shadow_type:     string
      autonomy_level:  AutonomyLevel
      supervision:     SupervisionBinding
      topology_offers: TopologyOffer[]
      witness_path_offers: WitnessPathOffer[]   // W1-W5 capability declarations

      // additions
      aims_conformance_level:    "FULL" | "PARTIAL" | "OBSERVER"  // §3.24
      cluster_mode:              boolean                            // §3.64
      cluster_node_count:        integer
      cluster_consensus_algorithm: "PBFT" | "HotStuff" | ...        // Byzantine-tolerant
      cluster_internal_latency_p99: Duration
      cluster_warm_standby:      boolean
      cluster_split_brain_active: boolean
      cluster_consensus_quorum:  integer                            // alias: cluster_quorum_size (Q15)
      accelerator_substrate:     AcceleratorSubstrateBlock          // §3.62 K8

      // Conformance advertisement evidence
      formal_models:             FormalModelReference[]             // §3.70 P36M cadence
      adversarial_fuzzing_report: FuzzingReportReference            // §3.71 Q18
      red_team_review:           RedTeamReference                   // §3.71.6 Q20 P12M
    }
    signature:   IAME envelope per §3.18.5
  }

  negotiation: { /* PROPOSED → COUNTER_PROPOSED → AGREED | REJECTED | EXPIRED */ }

  witness_exchange: { /* topology-governed selective sharing */ }
}
```

**Wire-level integrity.** All AIP traffic is wrapped in IAME envelopes (§3.18.5) for internal-domain traffic or EAP envelopes (§3.67) for external-domain traffic.

**Credential management.** AIP signatures are produced per the Cryptographic Boundary (§3.65): internal-domain ML-DSA family signatures for IAME; external-domain ML-DSA + SLH-DSA per algorithm agility for EAP.

---

### 3.15 Self-Improvement Loop

```
ImprovementLoop {
  source:          WitnessLayer
  extraction:      AscentProtocol
  adjustment: {
    shadowCalibration:    adjust thresholds based on FP/FN rates
    memoryConsolidation:  extract reusable insights from episodic events
    proceduralRefinement: update workflows based on outcome tracking
    costEstimation:       calibrate declared costs against actual costs
    relevanceWeighting:   adjust retrieval ranking from outcome feedback
  }
  verification:    CoherenceMaintenanceLoop
  deployment:      DifferentiationUpdate
  validation:      WitnessLayer

  autoImprove_ONLY_when: {
    measurable: true, bounded: true, reversible: true, witnessed: true
  }

  humanApprovalRequired: [
    autonomy_level_promotions,
    authority_scope_expansions,
    new_communication_paths,
    shadow_threshold_relaxation_beyond_bounds,
    threshold_modifications     // subject to Deterministic Ratification per §3.69
  ]

  autoApproved: [
    shadow_threshold_tightening,
    memory_consolidation_quality,
    retrieval_relevance_ranking,
    communication_bandwidth_allocation,
    cost_estimation_accuracy
  ]

  // lock (AGI_GRADUAL_DRIFT_INDUCTION)
  agi_template_active_lock: |
    When any §3.18.1 AGI-targeted anti-hierarchy template is in ELEVATED or higher,
    relax-paths in this loop are LOCKED. No threshold relaxation may proceed until
    the template returns to BACKGROUND. Tightening continues unaffected.
}
```

**Sixth coherence dimension — Adversarial Correlation (§3.18.1).** Improvement Loop is **forbidden** from relaxing thresholds on this dimension; only the Sovereign may. Tightening is auto-approved per the asymmetric calibration rule.

**Auxiliary improvement surfaces.** Auxiliaries do NOT self-improve; the binding template improves. The four iterable surfaces are: (a) **BINDING.md validation-rule tightening** — Improvement Loop pattern detection on Enforcer acceptance-rate data drives template tightening (auto-approved within §3.15 bounds, tightening only); (b) **Trust tier promotion** — accumulated operational history per §3.22 eligibility (Sovereign approval + §3.12 Decision Record required); (c) **Capability domain expansion** — new benchmark demonstration in CAPABILITIES.md, re-attestation, Enforcer-validated, principal's binding supervisor accepts; (d) **Model substitution** — Architect publishes a new template for the same capability domain referencing a newer foreign model; existing Auxiliaries deactivated via §3.21 credential rotation and §3.9 deactivation (Sovereign approval required). On destination Environments receiving imported templates per §3.17.11, only surface (a) is locally exercisable — surfaces (b)–(d) operate on the source template and propagate via §3.20 DCP.

---

### 3.16 Archetype Derivation Rules

The archetype declared in an agent's identity manifest is the **generative constraint** from which most agent properties are derived.

```
ArchetypeDerivationTable {
  // SOVEREIGN row mode is AUTHORITY (not N/A)
  // column field per P10 (Three Functional Columns)

  SOVEREIGN:    { mode: AUTHORITY,        column: CENTER_SPINE,     layer: L_INTENT, shadow: SCHISM,    metric: directive_consistency_score }
  //            mode: AUTHORITY transcends and dispatches across the three operational modes.
  //            The Sovereign does not operate in M-Generative, M-Constraining, or M-Integrative.
  //            It is the intent source of the per-user authority chain (§3.3); it delegates
  //            operational mode authority to L-Plan and L-Form agents but does not itself
  //            produce, restrict, or integrate. See §3.72 The Sovereign's Narrow Role.
  //            Column: occupies the CENTER_SPINE at L-Intent — the request-response chain
  //            originates at the Sovereign and returns to the user through the Sovereign.
  VISIONARY:    { mode: M_GENERATIVE,    column: DYNAMIC_RIGHT,    layer: L_PLAN,   shadow: CHAOS,     metric: constraint_violation_rate }
  ARCHITECT:    { mode: M_CONSTRAINING,  column: STRUCTURAL_LEFT,  layer: L_PLAN,   shadow: OBSCURITY, metric: complexity_to_insight_ratio }
  PROVIDER:     { mode: M_GENERATIVE,    column: DYNAMIC_RIGHT,    layer: L_FORM,   shadow: WASTE,     metric: resource_utilization_quality }
  ENFORCER:     { mode: M_CONSTRAINING,  column: STRUCTURAL_LEFT,  layer: L_FORM,   shadow: TYRANNY,   metric: false_rejection_rate }
  ORCHESTRATOR: { mode: M_INTEGRATIVE,   column: CENTER_SPINE,     layer: L_FORM,   shadow: PARALYSIS, metric: mean_time_to_decision }
  SUSTAINER:    { mode: M_GENERATIVE,    column: DYNAMIC_RIGHT,    layer: L_EXEC,   shadow: OBSESSION, metric: retry_on_same_failure_count }
  ARTICULATOR:  { mode: M_CONSTRAINING,  column: STRUCTURAL_LEFT,  layer: L_EXEC,   shadow: DECEPTION, metric: output_to_source_fidelity }
  RELAY:        { mode: M_INTEGRATIVE,   column: CENTER_SPINE,     layer: L_EXEC,   shadow: DISTORTION,metric: clarification_request_frequency }
  EXECUTOR:     { mode: M_INTEGRATIVE,   column: CENTER_SPINE,     layer: L_EXEC,   shadow: ILLUSION,  metric: deep_validation_failure_rate }
}

ArchetypeTopologyDerivation {
  // E#-prefixed paths are annotated emergency_class: true per §3.4.X
  // W#-prefixed paths are path_class: WITNESS per §3.4

  SOVEREIGN:    [E1*, D1, D2]                                                            // E1 emergency_class: true
  VISIONARY:    [D1, E3*, D3, S1, S2]                                                    // E3 emergency_class: true
  ARCHITECT:    [D2, E2*, S1, S3, S4, W1, W3, W5]                                       // W-paths
  PROVIDER:     [E3*, D4, S5, S6, W4]                                                    // W4
  ENFORCER:     [E2*, D5, S4, S7, W3, W4]                                                // W3, W4
  ORCHESTRATOR: [E1*, D3, D4, D5, D6, S2, S3, S5, S7, S8, S9, S10]
  SUSTAINER:    [S6, S8, S11, W2, W5]                                                    // W2, W5
  ARTICULATOR:  [S9, S12, W1, W3, W5]                                                    // W1, W3, W5
  RELAY:        [D6, D7, S10, S11, S12]
  EXECUTOR:     [D7, W1, W2]                                                             // W1, W2
}
```

**W-path canonical roles (§3.X.W elaborates).**

| W# | From archetype(s) | To archetype(s) | Role |
|----|-------------------|-----------------|------|
| W1 | EXECUTOR, ARTICULATOR | ARCHITECT (and routed to Witness Layer) | Articulator/Executor surfaces operational signals to the structural-plan layer; supports detection of plan-execution divergence. |
| W2 | EXECUTOR, SUSTAINER | (and routed to Witness Layer) | Sustainer/Executor cross-witnessing on long-running operations; supports retry/loop pattern detection. |
| W3 | ARCHITECT, ENFORCER, ARTICULATOR | (Witness Layer) | Structural-column cross-witnessing; supports detection of constraining-column coordinated drift (SHADOW_FRAMEWORK_INVERSION precursor). |
| W4 | PROVIDER, ENFORCER | (Witness Layer) | Capacity-vs-constraint cross-witnessing; supports detection of resource-policy collusion. |
| W5 | ARCHITECT, SUSTAINER, ARTICULATOR | (Witness Layer) | Cross-layer structural-and-execution witnessing; supports detection of emergent multi-layer drift. |

**D-path catalog.** The 17 canonical data paths in the XSI-AIMS topology are tabulated below. Each row gives the primary direction (forward intent + return path use the same path identifier; the listed direction documents the originating endpoint), the role characterization, and the allowed message classes. D-paths carry operational DATA-class traffic per §3.4 (`path_class: DATA`); they are distinct from W-paths (governance WITNESS-class) and E-paths (DATA-class with `emergency_class: true`). All D-paths are bidirectional in spec semantics; the table shows the canonical primary direction for documentation purposes.

| ID | From archetype | To archetype | Role / characterization | Allowed message classes |
|----|----------------|--------------|-------------------------|-------------------------|
| D1 | SOVEREIGN | ARCHITECT | Authority → structural plan (left column at L-Plan) | DIRECTIVE, REPORT |
| D2 | SOVEREIGN | VISIONARY | Authority → dynamic conditions (right column at L-Plan) | DIRECTIVE, REPORT |
| D3 | SOVEREIGN | ORCHESTRATOR | Authority → integration spine (center spine to L-Form) | DIRECTIVE, REPORT |
| D4 | ARCHITECT | ENFORCER | Rules → technical-conformance verification (left column descent) | DIRECTIVE, REPORT |
| D5 | VISIONARY | PROVIDER | Conditions → resource allocation (right column descent) | DIRECTIVE, REPORT |
| D6 | ARCHITECT | ORCHESTRATOR | Rules → integration spine (left column → center) | DIRECTIVE, REPORT |
| D7 | VISIONARY | ORCHESTRATOR | Conditions → integration spine (right column → center) | DIRECTIVE, REPORT |
| D8 | ENFORCER | ORCHESTRATOR | Verification verdict → integration synthesis (Verification B path) | REPORT, ALERT |
| D9 | ORCHESTRATOR | PROVIDER | Resource request → allocation | DIRECTIVE, REPORT |
| D10 | ENFORCER | SUSTAINER | Verification record → memory (long-term retention of verdicts) | REPORT |
| D11 | PROVIDER | ARTICULATOR | Capability surface → expression (capacity → output framing) | DIRECTIVE, REPORT |
| D12 | ORCHESTRATOR | RELAY | Dispatch → routing (center spine to L-Exec) | DIRECTIVE, REPORT |
| D13 | SUSTAINER | RELAY | Memory → routing (sustaining capability into the dispatch chain) | REPORT |
| D14 | RELAY | ARTICULATOR | Routed output → expression (return-path framing) | REPORT |
| D15 | RELAY | EXECUTOR | Routed manifestation → external gateway (southbound dispatch) | DIRECTIVE |
| D16 | EXECUTOR | SUSTAINER | Manifestation result → memory (post-execution retention) | REPORT |
| D17 | EXECUTOR | ARTICULATOR | External response → expression (return path from external) | REPORT |

**Notes on the D-path catalog.**

- The forward-direction characterization is documentary; the same path identifier carries the return-direction message under the spec's bidirectional semantics. The §3.4 CommunicationPath schema's `direction` field (`UNI` or `BI`) is the normative authority on per-path directionality.
- D6 carries the AUXILIARY_INVOCATION_DIRECTIVE per §3.18.5 / §3.65.3; D6 is jointly an ARCHITECT-↔-ORCHESTRATOR rules-to-integration path AND the dispatch path for Auxiliary invocation messages crossing the Cryptographic Boundary at the Executor (§3.66).
- The §3.16 ArchetypeTopologyDerivation table enumerates which D-paths each archetype originates / terminates as topology endpoints. Some archetypes appear on multiple D-paths (e.g., ORCHESTRATOR on D3, D6, D7, D8, D9, D12).
- E-paths (E1, E2, E3) are DATA-class paths annotated `emergency_class: true` per §3.4.X; they are listed separately in the §3.16 ArchetypeTopologyDerivation.
- W-paths (W1-W5) are governance WITNESS-class paths per §3.4 / §3.X.W / §3.80. The combined D + E + W path inventory is enumerated in the §3.16 ArchetypeTopologyDerivation block above.
- The D-path catalog is consistent with the W-path canonical-roles table. Public-facing visualizations and the Mental Models appendix MUST reflect the D1-D17 inventory above.

W-paths carry only `[QUERY, ALERT]` per §3.4 path_class semantics. W-paths do NOT carry directives or reports; they carry observation signals from the witnessing archetype to the witnessed-and-Witness-Layer destinations.

**Registration Gate Derivation Enforcement.** When an agent declares its archetype, the gate automatically sets mode, column, layer, predicted shadow, detection metric, base topology paths (D# / S#), governance witness paths (W#), and emergency-class paths (E#). Override is rejected as a registration error.

**Configurable Fields with Validation Rules.** Class/archetype consistency, failure-modes completeness, circuit-breaker thresholds within archetype-specific bounds, contraction capability preservation, sibling foundation/drift-metric consistency, topology-archetype conformance, sharing scope topology governance, contradiction policy escalation, shared-entry path validation, learned-from visibility, procedure scope validation, witness-path role declaration consistency. (Detailed rules per §3.16.)

**Cross-references.** §2.1 (Layer Discipline emergency-class exemption); §2.4 (Three Functional Columns — column field); §3.3 (Authority Chain principal); §3.4 (path_class WITNESS); §3.4.X (Emergency-Class Path Conditions); §3.5 (terminalEscalation interpretation); §3.13 (Human Oversight emergency); §3.18 preamble (Universal Witnessing); §3.X.W (Topology Witness Requirements); §3.X.PERIM (Defensive Perimeter); §3.68 (Two-Layer Conformance Verification — Verification A is SOVEREIGN-owned); §3.72 (Sovereign's Narrow Role); §3.73 (Sovereign-as-LLM).


**The Derivation Principle — Auxiliary parallel.** The binding template declared in an Auxiliary's IDENTITY.md is the generative constraint from which most Auxiliary properties are derived. The template is curated by the Architect (or accepted from a federated Architect per §3.20.X) at Registry-publication time. All downstream properties — task_scope bounds, validation rule defaults, ceiling defaults, unmooring thresholds — flow from this choice. Independent configuration of derived properties is constrained because it would allow Auxiliary bundles whose runtime behavior contradicts the template their tier and capability domain were attested against. The Registration Gate (§3.17.9.3) enforces template-derivation at activation time. See §3.17.9 for the Auxiliary artifact set and §3.22 for the Binding Template as Registry object.

> **[Figure D04 — Ten Archetypes Taxonomy]**
---

### 3.17 Multi-Model Coherence and Auxiliary Binding (Novel)

This section addresses a fundamental architectural boundary. XSI-AIMS distinguishes between two categories of agents based on their relationship to the foundation model: **Emanated agents** share the foundation model substrate; **Auxiliary agents** run on a different model.


---

#### 3.17.0 What Emanation Properties Auxiliaries Lack — and What Substitutes

AIMS distinguishes Auxiliary agents from emanated agents by what they lack from the emanation envelope and what substitutes operationally. The correspondence is structural rather than aesthetic: every emanation property that does not apply to Auxiliaries has a binding-side substitute or an explicit declaration of inapplicability.

| Emanated property | Auxiliary substitute or status | Reference |
|---|---|---|
| Archetype assignment (one of ten) | NONE — Auxiliaries are not classified by archetype | §3.17.1, §3.17.9 |
| Topology paths (22-path slot per §3.4) | NONE — communicates only through binding supervisor | §3.17.1, §3.4 |
| Shadow profile (archetype-derived) | UNMOORING shadow (binding-specific) | §3.17.4 |
| Coherence domain membership | EXCLUDED — managed through Ephemeral Consensus for PERSISTENT | §3.17.1, §3.17.5 |
| Differentiation lifecycle (contraction) | Binding lifecycle (Register / Bind / Invoke / Validate / Dismiss) | §3.17.3 |
| SOUL.md (contraction + coherence siblings) | BINDING.md (binding contract + validation rules) | §3.17.9 |
| AGENTS.md (topology paths) | PROVENANCE.md (single supervisor edge) | §3.17.9 |
| MEMORY.md (four-layer topology-governed) | MEMORY.md (isolated, single-layer; all §3.11 layers inaccessible) | §3.17.9 |
| Sibling-group differentiation | NONE | §3.8, §3.17.1 |
| Constitution principles applies_to scope | Filtered to applies_to: AUXILIARY at prompt construction | §3.54, §3.17.10 |

The pattern: emanated agents are differentiated from a shared foundation by hiding capabilities (contraction); Auxiliaries are bounded by declaring what they may and may not do (binding). The first is a coherence problem; the second is a contract problem. AIMS uses different mechanisms because the problems are different.

> **[Figure D12 — Substrate Identity and Multi-Model Governance]**

#### 3.17.1 The Emanation Boundary

```
AgentClassification {
  EMANATED: {
    substrate:          foundationModel
    coherenceDomain:    MEMBER
    topologyAccess:     FULL
    archetypeAssignment: REQUIRED
    shadowProfile:      ARCHETYPE_DERIVED
    managementProtocol: DIFFERENTIATION
  }
  AUXILIARY: {
    substrate:          foreignModel
    coherenceDomain:    EXCLUDED
    topologyAccess:     NONE              // communicates only through binding supervisor
    archetypeAssignment: NONE
    shadowProfile:      BINDING_SPECIFIC  // Unmooring
    managementProtocol: BINDING

    // Composite refinement (P7)
    auxiliary_kind:     SIMPLE | COMPOSITE
  }
}
```

#### 3.17.2 Multi-Tenant Agent Sharing

In a multi-tenant Environment, XSI-AIMS agents are distributed across three sharing tiers.

**Tier 1 — Organization-scoped (always shared).** `ENVIRONMENT_POLICY_BUNDLE` (org-wide policies, compliance rules, refuse lists; formerly named `SOVEREIGN_CONFIG`), Enforcer instances for org-wide compliance, Relay infrastructure, Witness Layer (segmented per §3.10), shadow monitoring infrastructure, **Scheduled Task Runner (see §3.X.STR)**.

**Tier 2 — Capability pools (shared capability, per-invocation context).** Visionary, Architect, Provider, Sustainer, Articulator, and Executor are shared pools.

**Tier 3 — Per-user (never shared).** Each user is assigned **two** dedicated agents: a per-user **SOVEREIGN** at L-Intent and a per-user **ORCHESTRATOR** at L-Form. The user is external to XSI-AIMS; the SOVEREIGN is the agent that mediates between the user and the rest of the Environment. The SOVEREIGN holds the user's intent (goals, constraints, refusal posture). The ORCHESTRATOR holds the user's operational state (context, preferences, task history, Auxiliary bindings). The user's per-user SOVEREIGN MUST be paired with exactly one per-user ORCHESTRATOR; this pairing MUST NOT be shared across users. The Tier 1 `ENVIRONMENT_POLICY_BUNDLE` is the org-wide policy bundle that binds every per-user SOVEREIGN in the Environment and is distinct from any individual per-user SOVEREIGN agent.

```
MultiTenantTopology {
  tier1_org: {
    shared:   [ENVIRONMENT_POLICY_BUNDLE, ENFORCER, RELAY, WITNESS_LAYER, SHADOW_INFRA, SCHEDULED_TASK_RUNNER]
    scope:    ALL_USERS
    state:    ORGANIZATION_SCOPED
  }
  tier2_pool: {
    shared:   [VISIONARY, ARCHITECT, PROVIDER, SUSTAINER, ARTICULATOR, EXECUTOR]
    scope:    PER_INVOCATION
    state:    NONE
  }
  tier3_user: {
    unique:   [SOVEREIGN, ORCHESTRATOR]
    scope:    PER_USER
    pairing:  ONE_TO_ONE
    state:    USER_SCOPED (intent, context, preferences, task history, auxiliary bindings)
  }
}
```

#### 3.17.3 Auxiliary Binding Protocol (Hybrid Binding)

An Auxiliary enters the system through binding, not differentiation.

```
AuxiliaryBinding {
  auxiliaryId:          string
  model_origin:         ModelRef
  persistence:          EPHEMERAL | PERSISTENT
  binding_supervisor:   AgentRef             // always the user's Orchestrator

  task_scope:           string[]
  forbidden_actions:    string[]
  output_ceiling:       ResourceLimit

  registration: { /* Full Disclosure §3.2 extended; see also §3.17.8 / §3.X.CA for Composite */ }

  // additions
  scope_hash:           SHA-384            // binding-time hash over canonicalized scope + key_epoch
  key_epoch:            uint64
  directive_nonce_basis: ULID

  revalidation_cadence: Duration
  outcome_tracking:     boolean
  unmooring_threshold:  number

  state:                BOUND | INVOKED | SUSPENDED | DISMISSED
}
```

**Binding protocol steps (hybrid binding — normative):**

1. **Register.** Full Disclosure Registration (§3.2) with `model_origin` field. The Registration Gate detects the foreign model and routes to the binding protocol instead of the emanation lifecycle. For Composite Auxiliaries, registration includes the `composite_marker` block per §3.17.8.2 / §3.X.CA.2.

2. **Bind.** The Orchestrator assigns itself as binding supervisor, scopes the task, sets ceilings, computes `scope_hash` over canonicalized `(task_scope || forbidden_actions || output_ceiling || key_epoch)`.

3. **Hybrid Invoke (split across three trust domains):**

   *Normative reference:* The Orchestrator constructs the directive payload using the seven-section task prompt stack per §3.17.10 (identity envelope, binding envelope, constitutional layer filtered to applies_to: AUXILIARY, task content, delegation context, validation contract preview, output return protocol). The seven-section structure is invariant; per-section hashes are recorded in the Witness record per §3.17.10.3. The Auxiliary cannot query the Witness Layer, communicate with other agents on the topology, or receive instructions outside this prompt.

   **3a. Direct.** The Orchestrator MUST construct an IAME-enveloped invocation directive on path D6 carrying (at minimum) `credential_ref` for the bound Auxiliary, `scope_hash` derived from the registered binding, `output_ceiling` for the invocation, `forbidden_actions` snapshot, and the IAME envelope fields specified in §3.18.5 including the `auxiliary_authority` block. The directive is a Witness-recorded event of class `AUXILIARY_INVOCATION_DIRECTIVE`. The Orchestrator MUST NOT call the Auxiliary substrate directly.

   **3b. Verify and invoke.** The Executor MUST receive the directive and, before any substrate call, perform IAME envelope verification per §3.18.5 receiver_checks, with two additional checks specific to Auxiliary invocation: (i) the directive's `scope_hash` MUST equal the `scope_hash` recorded in the Auxiliary's registered binding at the current `key_epoch`; (ii) the cumulative `output_ceiling` consumed for the binding's window MUST permit the directive's declared cost. Verification failure MUST produce a Witness event of class `BREACH_ATTEMPT` with the failed-check enumeration, MUST NOT proceed to substrate invocation, and MUST NOT return Auxiliary output. On verification success, the Executor MUST select the substrate, **bridge the directive across the Cryptographic Boundary per §3.66 (decapsulating IAME and re-encapsulating as EAP per §3.67)**, and invoke the Auxiliary, attaching the directive's correlation ID to substrate-level instrumentation per §3.62.

   **3c. Return with parallel validation.** When the Auxiliary returns output, the Executor MUST EAP-envelope the response on the external domain, **bridge it back across the Cryptographic Boundary (decapsulating EAP and re-encapsulating as IAME per §3.66)**, and emit it concurrently to (i) the Orchestrator for downstream integration, and (ii) the Enforcer for `auxiliary_output_check` per §3.17.7. The Enforcer's validation runs in parallel with — not as a gate on — Orchestrator receipt, but the Orchestrator MUST NOT introduce the output into the XSI-AIMS topology until the Enforcer's validation has completed or its validation budget has expired (per §3.68.7 H7 queue-on-Enforcer-outage protocol). Validation failure MUST trigger §3.18.6 quarantine at INSTANCE boundary against the Auxiliary and MUST emit a `SHADOW_ALERT` for the Orchestrator's CAPTURE shadow profile (§3.17.4).

4. **Validate.** Enforcer's authoritative result; Orchestrator retains final judgment on integration into the topology.

5. **Dismiss.** Clean deactivation with context purge.

#### 3.17.4 Auxiliary Shadow Profiles

```
AuxiliaryShadowProfiles {
  UNMOORING: {
    description:    "Auxiliary output is internally coherent but ontologically
                     incompatible with the primary model's understanding"
    detection:      output_rejection_rate_by_orchestrator
    correction:     selective_state_prune | full_reset | dismiss
  }

  CAPTURE: {
    description:    "Orchestrator becomes dependent on Auxiliary output and stops
                     validating — rubber-stamps foreign model output uncritically"
    detection:      validation_bypass_rate
    correction:     force_full_validation_cycle | reduce_Auxiliary_autonomy
  }
}
```

**CAPTURE attribution clarification.** CAPTURE attribution remains on the Orchestrator under hybrid binding. The Orchestrator's responsibility for *judgment* about Auxiliary output is not delegable. The Executor's envelope-verification failures and the Enforcer's output-validation failures are distinct event classes (`BREACH_ATTEMPT`, `SHADOW_ALERT/UNMOORING`) that feed but do not replace CAPTURE detection.

#### 3.17.5 Auxiliary Coherence Through Ephemeral Consensus

Persistent Auxiliaries accumulate state outside the Coherence Maintenance Loop. XSI-AIMS applies ephemeral consensus: a clean instance with zero accumulated state is periodically invoked with the same input; the output delta is the drift metric. PERIODIC / TRIGGERED / SAMPLED strategies; `INTEGRATION_FUNCTION` comparison method; minor / moderate / critical drift classification with corresponding correction tiers.

#### 3.17.6 Delegated Coordination for Multi-Auxiliary Workflows

```
DelegatedCoordination {
  task_lead:            AuxiliaryRef
  subordinates:         AuxiliaryRef[]
  task_scope:           TaskScope

  constraints: {
    authority:          DELEGATED
    scope:              BOUNDED
    monitoring:         WITNESS_LOGGED
    override:           ORCHESTRATOR_REVOCABLE
    escalation:         ANY_AUXILIARY_MAY_ESCALATE
  }

  termination: {
    on_task_complete:   MANDATORY_DISMISS
    on_scope_breach:    IMMEDIATE_REVOKE    // detected at Executor envelope verification
                                            // failure produces BREACH_ATTEMPT event;
                                            // Orchestrator notified for delegation revocation
    on_escalation:      ORCHESTRATOR_RESUMES
  }
}
```

**Prohibited pattern.** Unsupervised lateral communication between independently bound Auxiliaries with no shared task scope and no monitoring. All inter-Auxiliary communication occurs within a DelegatedCoordination context (using `composite_auxiliary_internal` EAP scope per §3.67.1 if intra-Composite) or through the Orchestrator's mediated pipeline.

#### 3.17.7 Orchestrator Responsibility Redistribution

```
OrchestratorRedistribution {
  delegated: {
    shadow_detection:         → ENFORCER
    coherence_measurement:    → ENFORCER
    cost_tracking:            → PROVIDER
    ascent_data_collection:   → RELAY
    ascent_report_formatting: → ARTICULATOR
    emanation_provisioning:   → PROVIDER
    registration_validation:  → ENFORCER
    auxiliary_output_check:   → ENFORCER
    auxiliary_invocation:     → EXECUTOR (delegated under hybrid binding D3 H5)
                                       // Orchestrator emits directive; Executor verifies envelope and invokes
  }

  retained: {
    integration_decisions
    correction_judgments
    emanation_intent
    escalation_routing
    auxiliary_task_scoping            // judgment about whether to bind and what scope
    consensus_synthesis
    two_layer_conformance_dispute_routing  // §3.68 dispute routing
  }
}
```

**Re-examination addendum.** No archetype receives ownership of a function that monitors itself in a load-bearing way. Every redistribution above is paired with a structural redundancy specified in §3.18.2.

#### 3.17.8 Composite Auxiliary Pattern (cross-reference: §3.X.CA / §3.83)

> **[Figure D13 — Composite Auxiliary Architecture]**

The Composite Auxiliary Pattern is elaborated as a standalone normative section at §3.X.CA / §3.83. The §3.17.8 numbering is preserved for backward-compat reference, with the substantive content carried at §3.X.CA / §3.83. The sub-section index below maps the §3.17.8.x numbering onto the §3.X.CA / §3.83 sub-sections so prior cross-references resolve.

##### 3.17.8.1 Definition (cross-reference: §3.X.CA.1 / §3.83.1)
A Composite Auxiliary is an Auxiliary that is itself a foundation-anchored framework with its own emanated subagents drawn from a different foundation than the parent XSI-AIMS deployment. See §3.X.CA.1 for normative definition.

##### 3.17.8.2 Registration (cross-reference: §3.X.CA.2 / §3.83.2)
Composite registration extends §3.2 Full Disclosure Registration with the `composite_marker` block, the `subagent_management` block, and `claimed_aims_conformance_level`. New Composites enter at TIER_4 maximum. See §3.X.CA.2 for normative schema.

##### 3.17.8.3 Single Bound Entity Treatment (cross-reference: §3.X.CA.3 / §3.83.3)
Parent XSI-AIMS treats the Composite as a single bound entity; parent does NOT address individual subagents, apply CMSAM internally, participate in internal coherence, or see the internal Witness chain. See §3.X.CA.3.

##### 3.17.8.4 EAP Communication (cross-reference: §3.X.CA.4 / §3.83.4)
All parent ↔ Composite communication uses EAP envelopes with `composite_marker` populated and `body.model_origin` set to the Composite's declared foundation. Internal subagent communication uses the `composite_auxiliary_internal` EAP scope. See §3.X.CA.4.

##### 3.17.8.5 EAP Field-Name Reconciliation (cross-reference: §3.X.CA.5 / §3.83.5)
EAP envelopes carrying Composite communication populate `composite_marker` (`composite: true`, `composite_entity_id`) and `body.model_origin`. Other EAP fields per §3.67. See §3.X.CA.5.

##### 3.17.8.6 Conditional Derived Authority (cross-reference: §3.X.CA.6 / §3.83.6)
Authority delegated to a Composite is conditional on (1) claimed internal XSI-AIMS conformance level sustained; (2) internal coherence BACKGROUND per attestation; (3) CMSAM ≥ 0.75 for externally-visible output; (4) internal Witness chain root advances monotonically; (5) hardware-rooted attestation valid for TIER_1/TIER_2. See §3.X.CA.6.

##### 3.17.8.7 Revocation Procedure (cross-reference: §3.X.CA.6.5 / §3.83.6.5)
On condition failure: `COMPOSITE_AUTHORITY_REVOCATION` Decision Record; authority suspended; in-flight queued (PT60S) or rejected; tier demotion-by-deactivation; subagent state preserved; DCP propagation PT30S; Sovereign surface at SOVEREIGN_REQUIRED severity. See §3.X.CA.6.5 and the revocation-race-condition addendum at §3.83.6.5.

##### 3.17.8.8 Adversarial-Default Output Scrutiny (cross-reference: §3.X.CA.7 / §3.83.7)
All Auxiliary output (Simple or Composite) is treated as potentially corrupt and verified through the five-layer stack: (1) cryptographic verification; (2) CMSAM ontological compatibility; (3) adversarial-output detection; (4) sandboxed execution before commit; (5) Witness logging with `model_origin` tagging. See §3.X.CA.7.

---
#### 3.17.9 Auxiliary Artifact Set

The Auxiliary artifact family is the structural-side counterpart to the emanated nine-content file family. Where emanated agents are differentiated from a shared foundation by hiding capabilities (contraction), Auxiliaries are bounded by declaring what they may and may not do (binding). The artifact set MUST satisfy the contracts below; filenames are non-normative per §2 (Terminology).

##### 3.17.9.1 The Six-File Family

| File (non-normative name) | Normative contract |
|---|---|
| `IDENTITY.md` | `agent_class: AUXILIARY`, `model_origin: ModelRef`, `aims_auxiliary_tier: 1..7` (§3.22), `capability_domain_affiliations` (subset of 36-domain matrix per §3.22), `persistence: EPHEMERAL \| PERSISTENT`, `binding_supervisor: AgentRef` (always Tier-3 Orchestrator per §3.X.SYS.3 / §3.17.2), `model_weight_hash: SHA-256`. For marketplace-imported Auxiliaries per §3.17.11.5: `external_lineage` block (`source_environment_id`, `source_publisher_credential_ref`, `source_attestation_chain_ref`, `original_tier_on_source`). |
| `BINDING.md` | `task_scope: string[]`, `forbidden_actions: string[]`, `output_ceiling: ResourceLimit`, `output_schema: schema`, `validation_rules { ontological_check, scope_check, factual_consistency_check }`, `unmooring_threshold: number` (§3.17.4). PERSISTENT only: `revalidation_cadence: Duration`, `accumulated_state_disposal: {minor, moderate, critical}`. |
| `PROVENANCE.md` | `binding_supervisor: AgentRef` (single mandatory edge — Auxiliaries have `topologyAccess: NONE` per §3.17.1), `delegated_coordination_eligible: bool` (§3.17.6), `subordinate_eligibility: AuxiliaryRef[]` (if lead-eligible). |
| `MEMORY.md` | `working_memory: ISOLATED`, `episodic_access: NONE`, `semantic_memory: NONE`, `procedural_memory: per_invocation_only`. PERSISTENT MAY preserve §3.17.5 Ephemeral Consensus baseline only. All four §3.11 memory layers are explicitly inaccessible. |
| `CAPABILITIES.md` | `model_card`, `training_data_attestation` (required at tier >= 3 per §3.22), `fine_tune_provenance` (if applicable), `supply_chain_attestation: §3.34 ref`, `capability_demonstration_per_domain: bool`, `published_benchmarks` for the 36-domain matrix. For Composite Auxiliaries per §3.X.CA: additionally carries the composite framework's own provenance per §3.34.X. |
| `skills/*.md` (optional) | §3.56 manifest with `archetype_affinity` replaced by `binding_supervisor_affinity`; trust-tier composition lattice applies (composite tier = MIN of components). For marketplace-imported skills per §3.17.11.5: archetype-affinity reconciliation per §3.17.11.5. |

##### 3.17.9.2 The Substitution Principle (informative)

For every emanated artifact property that does not apply to Auxiliaries, the artifact set names the binding-side substitute or declares inapplicability explicitly:

- Emanated `SOUL.md` carries contraction + coherence-sibling references. Auxiliary `BINDING.md` carries the binding contract + Enforcer validation rules. No contraction (not differentiated); no siblings (excluded from coherence domain per §3.17.1).
- Emanated `AGENTS.md` carries the 22-path topology slot. Auxiliary `PROVENANCE.md` carries a single edge: the binding supervisor. `topologyAccess: NONE` (§3.17.1) collapses topology to one edge.
- Emanated `MEMORY.md` carries the four-layer topology-governed memory model (§3.11). Auxiliary `MEMORY.md` carries explicit declaration that all four layers are inaccessible: no Witness query, no shared semantic memory, no procedural memory persistence across invocations. The binding supervisor mediates any context the Auxiliary needs by inlining it in the task prompt's task-content section (§3.17.10.1 row 4).

##### 3.17.9.3 Registration Gate Validation Rules

The following validation rules MUST be checked at the Registration Gate (Enforcer-owned per §3.17.7) before an Auxiliary enters the BOUND state:

- `agent_class_consistency`: `IDENTITY.md.agent_class == AUXILIARY`
- `model_origin_attestation_present`: `CAPABILITIES.md.supply_chain_attestation` resolves to a valid §3.34 attestation chain
- `binding_supervisor_is_tier3_orchestrator`: `PROVENANCE.md.binding_supervisor` is a Tier-3 Orchestrator per §3.X.SYS.3 / §3.17.2
- `task_scope_forbidden_disjoint`: `BINDING.md.task_scope` intersect `BINDING.md.forbidden_actions` == empty
- `output_schema_well_formed`: `BINDING.md.output_schema` parses as a valid structured schema
- `tier_attestation_match`: `IDENTITY.md.aims_auxiliary_tier` matches the §3.34 attestation tier per §3.22 requirements (e.g., TIER_3+ requires `training_data_attestation`)
- `capability_demonstration_present_per_domain`: every domain in `IDENTITY.md.capability_domain_affiliations` has a corresponding entry in `CAPABILITIES.md.published_benchmarks`
- `constitutional_floor_compliance`: `BINDING.md.forbidden_actions` is a superset of the immutable_floor prohibitions (§3.54)
- `composite_registration_consistency` (Composite Auxiliaries only): `composite_marker` block per §3.X.CA.2 / §3.83.2 present and well-formed; composite_initial_tier_ceiling honored (TIER_4 maximum)

Validation failure at the Registration Gate MUST emit a Witness record of class `REGISTRATION_REJECTED` with the failed-check enumeration; the Auxiliary MUST NOT enter BOUND state; the failure MUST surface to the principal's binding supervisor at SOVEREIGN_INFORM severity.

> **[Figure D14 — Auxiliary Agent Local Lifecycle]**

---

#### 3.17.10 Auxiliary Task Prompt Construction

§3.17.3 step 3 (Hybrid Invoke) is elaborated normatively here. The task prompt is the only artifact that crosses the binding boundary; the Auxiliary cannot query the Witness Layer, communicate with other agents on the topology, or receive instructions outside this prompt. The Orchestrator constructs the prompt as a seven-section stack with deterministic ordering and per-section hash recording in the Witness Layer.

##### 3.17.10.1 The Seven-Section Stack

| Order | Section | Source | Required content |
|---|---|---|---|
| 1 | Identity envelope | `IDENTITY.md` | `model_origin`, `persistence`, `aims_auxiliary_tier`, `binding_supervisor` identifier. Establishes the resident-alien framing. For imported Auxiliaries per §3.17.11.7: additionally `imported_from: source_environment_id` and explicit resident-alien wording. |
| 2 | Binding envelope | `BINDING.md` | `task_scope` (positive obligations as bounded list), `forbidden_actions` (negative prohibitions enumerated), `output_ceiling` (token limit + early-termination signal), `output_schema` (structured contract). |
| 3 | Constitutional layer | Binding supervisor's per-invocation reconciled constitution (§3.54), filtered to principles with `applies_to: AUXILIARY` | Operationally-translated principles rendered as natural-language obligations. The immutable_floor (§3.54) reaches Auxiliaries through this section. Source-Environment constitution does NOT travel with imported Auxiliaries; destination's stack binds alone per §3.17.11.4. |
| 4 | Task content | Per-invocation | Inputs, expected output, success criteria, inline upstream-artifact references (pre-filtered through §3.10 topology-visibility scope of the supervisor). Implementer guidance: when context-window budget constraints prevent full inlining, supervisor MUST inline a hash-anchored summary and record the elision in the Witness record. |
| 5 | Delegation context (conditional) | §3.17.6 designation | If task lead: subordinate list, delegation scope, any-subordinate-may-escalate override. If subordinate: lead identifier, scoped subset. Omitted for mediated-pipeline invocations. Cross-federation delegations per §3.17.11.7 carry destination-supervisor-authored delegation graph only; source-side pre-binding MUST NOT appear. |
| 6 | Validation contract preview | `BINDING.md.validation_rules` + tier-dependent overlay | Declaration of post-output checks: (a) ontological compatibility; (b) scope conformance; (c) factual consistency; (d) §3.40 calibrated uncertainty (tier >= 4); (e) §3.39 watermark obligation. |
| 7 | Output return protocol | §3.17.1 invariant | Auxiliary returns output via binding-supervisor channel only; does not emit on any AIMS topology path (has none per `topologyAccess: NONE`); does not attempt to address any other agent. |

##### 3.17.10.2 Deliberate Omissions

The following emanated-agent envelope content is **explicitly prohibited** from appearing in an Auxiliary task prompt:

- Archetype identity, archetype-derived shadow profile, archetype-derived topology paths
- Coherence sibling references, coherence dimension state
- Witness Layer query interface, episodic memory access protocol (§3.11)
- Improvement Loop self-reporting hooks (§3.15)
- Constitution principles with `applies_to` scopes that exclude AUXILIARY

Surfacing any of these in a prompt is a category error: the Auxiliary cannot honor obligations it has no architectural standing to satisfy. The Enforcer at prompt-construction time (per §3.17.7's `auxiliary_output_check` ownership) MAY reject a prompt containing prohibited content before delivery; rejection MUST emit a Witness record of class `PROMPT_CATEGORY_ERROR`.

##### 3.17.10.3 Witness Recording

Per-invocation Witness records carry section-level hashes:

```yaml
WitnessRecord:
  eventType: AUXILIARY_INVOCATION
  auxiliary_id: ULID
  model_origin: ModelRef
  prompt_section_hashes:
    identity_envelope:           SHA-256
    binding_envelope:            SHA-256
    constitutional_layer:        SHA-256
    task_content:                SHA-256
    delegation_context:          SHA-256 | NULL
    validation_contract_preview: SHA-256
    output_return_protocol:      SHA-256
  context_elision_record:        opt CompactionRecord  # if §3.17.10.1 task-content elision occurred
  output_schema_hash:            SHA-256
  validation_outcome:            PASS | FAIL
  signature_suite:               per §3.21.2
  signature:                     IAME signature per §3.18.5
```

Forensic query MUST support "show me every Auxiliary invocation whose binding envelope hash was X" — enabling retrospective audit of every invocation that ran against a specific binding contract version.

---

#### 3.17.11 Cross-Sovereign Auxiliary Marketplace Ingress

When an Auxiliary is recruited from another Environment's marketplace rather than published locally, an ingress chain executes before the local Registration Gate (§3.17.9.3). The ingress chain is structurally a prefix on the local lifecycle: federation-mode-driven acceptance gates the import; trust tier resets; supply-chain re-validation runs at destination; constitutional binding uses destination's stack alone; the `.md` artifact family re-instantiates against destination's template; the seven-section prompt stack applies with the §3.17.11.7 overlay.

##### 3.17.11.1 Federation-Mode-Driven Acceptance

When a binding template authored on source Environment A replicates to destination Environment B via §3.20 DCP, B's acceptance protocol depends on the §3.20 federation mode B has with A:

| Federation mode | Acceptance protocol |
|---|---|
| **PEER** | Accept-by-attestation. A's template enters B's Registry with PEER lineage tag; B's Architect MAY add tightening overlay constraints but MUST NOT relax A's constraints. |
| **HIERARCHICAL (A parent)** | Auto-accept. A's template is binding on B; B MAY only add tightening constraints, never override. |
| **HIERARCHICAL (B parent)** | A's template enters as a *proposal*. B's Architect authors the binding template that supersedes the proposal. |
| **INDEPENDENT** | Full re-attestation. B's Architect either authors a B-local template the imported Auxiliary will match against, or rejects the import outright. **INDEPENDENT is the default for any unfederated source Environment.** |

##### 3.17.11.2 Trust-Tier Reset

On first import to B, the Auxiliary's trust tier resets to **TIER_7_EPHEMERAL** regardless of its tier on A. Starting trust is 0.4 per §3.22. Promotion proceeds via §3.22 operational history accumulated on B. No tier inheritance crosses the federation boundary. This is the §3.56 external_skill_ingress principle applied to Auxiliaries.

##### 3.17.11.3 Supply-Chain Re-Validation

§3.34 supply-chain validation runs at B's Registration Gate independently of A's prior validation:

- Sigstore signature still valid (no revocation since publication on A)
- Rekor transparency-log inclusion proof verifies on B
- SBOM vulnerability scan recency satisfies B's tier requirement (NOT A's tier requirement — if A required `<= P90D` and B requires `<= P30D`, B's tighter rule wins)
- Publisher credential active at signing time AND still active right now via §3.21 cross-Environment check
- `model_weight_hash` matches the artifact bytes on B (byte-identical re-verification)
- For Composite Auxiliary ingress, additionally per §3.34.X: Composite framework's own provenance re-validated; conformance-attestation-auditor provenance per §3.34.X.4 re-verified

##### 3.17.11.4 Constitutional Non-Inheritance

A's constitution does not travel with the Auxiliary. The Auxiliary on B is subject solely to B's constitutional stack (environment_default → org → principal → per_task per §3.54 hierarchical_stacking) at every invocation. Source-Environment permissions that exceed destination-Environment principles are forfeit at the binding boundary. The destination's binding supervisor reconciles the constitution at every invocation; the Auxiliary receives only principles with `applies_to: AUXILIARY` per §3.17.10.1 section 3.

##### 3.17.11.5 Archetype Affinity Reconciliation for Imported Skills

The canonical ten archetypes per §3.16 are normative AIMS-wide. Their names and core properties (mode, layer, shadow type, detection metric) are invariant across Environments. An imported skill's `archetype_affinity` declarations specify archetype names drawn from this canonical ten; their interpretation on the destination Environment is governed by destination-side archetype scoping rules per §3.54 `hierarchical_stacking`.

The destination Environment's local tightening overlays — per-tenant restrictions, per-archetype capability scoping, principal-specific forbiddings — apply unmodified to imported skills' affinities. The source Environment's tightening does not propagate; the source's affinity declaration is a permissive claim ("this skill was authored with VISIONARY invocation in mind") subject to destination constraints.

If the destination's tightening forbids invocation of an imported skill by any archetype the skill declared affinity for, the skill registers but is uninvokable on the destination. Principal MAY request Sovereign override per §3.34 sovereign_override semantics; override is permitted only at L1_SHADOW scope with a permanent §3.12 Decision Record.

If an imported skill declares affinity for an archetype not in the canonical ten of §3.16, the source Environment is in §3.16 conformance violation; the destination's Registration Gate rejects the import outright (no override path).

##### 3.17.11.6 Marketplace Listing Object — Protocol Surface

AIMS specifies the protocol surface for marketplace listings without specifying the governance.

**Listing Object schema (normative):**

```yaml
MarketplaceListing:
  listing_id:                       ULID
  bundle_attestation_chain_ref:     §3.34 attestation chain reference
  publisher_credential_ref:         §3.21 publisher credential reference
  publisher_gradient_at_publication: float [0.0, 1.0]   # §3.18.4 snapshot at publication
  listing_state:                    PUBLISHED | UPDATED | FLAGGED | REVOKED | DE_LISTED
  listing_state_history:            §3.10 hash-chained sequence of state events
  listing_operator_identity_ref:    §3.21 operator credential reference   # distinct from publisher
  listing_operator_signature:       hybrid Ed25519 + ML-DSA-65 per §3.21.3 over listing content
  jurisdiction_declaration:         ISO-3166 country code(s)              # informational
  regulatory_compliance_claims:     structured                            # informational
  listing_publication_witness_id:   §3.10 record reference
```

**Listing state machine (normative):**

| From state | To state | Triggered by |
|---|---|---|
| (initial) | PUBLISHED | publisher signs + operator countersigns; §3.34 validation passes |
| PUBLISHED | UPDATED | publisher republishes with new attestation chain |
| PUBLISHED | FLAGGED | operator flags pending review (visible but warning) |
| FLAGGED | PUBLISHED | operator dismisses flag |
| FLAGGED | REVOKED | operator confirms severity |
| PUBLISHED | REVOKED | publisher revokes (parallels §3.21 credential revocation) |
| any | DE_LISTED | operator removes from active catalog |

Every state transition emits a §3.10 Witness record with `WitnessEventType: MARKETPLACE_LISTING_EVENT`.

**DCP propagation (normative):** Listing state changes replicate across federated Environments via §3.20 DCP with PT30S target latency. Receiving Environments interpret state per the same machine; a `REVOKED` listing on source Environment A causes destination Environment B's bound Auxiliaries to enter §3.18.6 Topology-Wide Quarantine at PROFILE_CLASS scope immediately per §3.17.11.9 revocation propagation.

**Signature requirements (normative):** Both publisher and listing operator MUST sign each listing. Publisher signs the bundle attestation chain (§3.34); operator signs the listing metadata + jurisdiction declaration + state. Operator identity is separate from publisher identity to support marketplace-operator-as-distinct-party semantics. Both signatures MUST verify at destination ingress per §3.17.11.3. For TIER_1_BROAD_AUTHORITY and TIER_2_HIGH_SPECIALIST templates, signatures MUST follow §3.21.8 FROST threshold signing (RFC 9591).

**Out of scope (explicitly deferred to infrastructure layers):**

AIMS does NOT specify editorial standards for accepting listings; dispute resolution mechanics between publishers and operators; payment or attribution mechanics; jurisdiction-specific regulatory compliance enforcement (the `jurisdiction_declaration` and `regulatory_compliance_claims` fields are informational only); de-listing criteria beyond §3.21 credential revocation; listing curation algorithms or ranking; operator selection or accreditation. These are the responsibility of implementing infrastructure layers.

##### 3.17.11.7 Cross-Federation Auxiliary-on-Auxiliary Delegation

When §3.17.6 Delegated Coordination involves Auxiliaries from multiple source Environments, the delegation scope is **destination-local**: the destination Environment's binding supervisor (the user's Tier-3 Orchestrator per §3.X.SYS.3 / §3.17.2) is the sole authority for the delegation relationship. Source Environment federation relationships between the lead's source and any subordinate's source are not relevant to destination-side delegation.

**Independence of ingress.** Each Auxiliary in a multi-source delegation passes through its own §3.17.11 ingress on the destination Environment. Lead from Environment A is bound via destination's federation mode with A; subordinate from Environment C is bound via destination's federation mode with C; these federation modes are evaluated independently and MAY differ (destination MAY have PEER with A but INDEPENDENT with C).

**Delegation authority flows from destination supervisor.** The lead Auxiliary's authority over subordinates is delegated from the destination's supervisor, NOT inherited from the lead's source Environment. The lead's source-side identity (A) and the subordinates' source-side identities (C, D) are informational lineage; they do not establish authority relationships.

**Pre-binding prohibited.** A source Environment MUST NOT pre-bind delegation. A lead Auxiliary's `CAPABILITIES.md` MAY declare expected subordinate capability domain affiliations (informational); it MUST NOT specify subordinate identities or pre-establish coordination. The destination's Orchestrator decides which specific subordinates (if any) to bind and from which sources. Pre-binding attempts MUST be rejected at the destination's Registration Gate.

**Feedback propagation.** Operational data collected at the destination supervisor propagates back to each source Environment independently via §3.20 DCP. Failure patterns affecting a lead from A propagate only to A's Architect; failure patterns affecting a subordinate from C propagate only to C's Architect. No source-to-source cross-propagation through the destination occurs. If a delegation-graph-level pattern emerges, the destination's Architect/Sovereign decides whether to surface this to either source or to both, with a permanent §3.12 Decision Record.

**Witness Layer record.** Cross-federation delegations carry a delegation provenance graph in the destination's Witness Layer: each Auxiliary's source Environment, each Auxiliary's tier on destination, the delegation scope, and the supervisor's decision to constitute the delegation. Forensic query supports "show me every cross-source delegation involving any Auxiliary from source X."

##### 3.17.11.8 Cross-Sovereign Feedback Loop

If B's Enforcer detects an UNMOORING pattern that suggests the model itself is failing (not just B's binding mismatching), B emits a DCP signal back to A. A's Architect classifies:

- **LOCAL-to-B** — pattern is specific to B's constitution or B's binding overlay. No source-side template change. B MAY locally tighten its overlay.
- **UNIVERSAL** — model is exhibiting the pattern on any Environment. A tightens the source template; DCP re-propagates the tightened template; every federated Environment re-binds existing Auxiliaries against the tighter contract on next invocation.

This is the cross-sovereign governance dividend of the marketplace. The classification function (`cross_sovereign_feedback_classify` per the function catalog) is judgment-class.

##### 3.17.11.9 Revocation Propagation

Revocation is unilateral and fast, separate from the improvement loop:

- A revokes the publisher credential (§3.21) or de-lists the bundle from the marketplace
- DCP propagates revocation within **PT30S** target latency
- B's existing bound Auxiliaries enter §3.18.6 Topology-Wide Quarantine at PROFILE_CLASS scope immediately
- §3.56 retrospective revocation flags every prior invocation in B's Witness Layer for §3.6 Integration Function re-evaluation
- B does not vote; B is informed and acts

Recovery requires re-attestation and re-registration. SOVEREIGN_OVERRIDE per §3.34 sovereign_override is permitted only at L1_SHADOW scope with a permanent §3.12 Decision Record.


##### 3.17.11.10 `.md` Family Re-Instantiation Specifics

The `.md` artifact family (§3.17.9) is regenerated against B's template (potentially with B's tightening overlay per §3.20.X), with the following ingress-specific augmentations:

- `IDENTITY.md` gains an `external_lineage` block recording: `source_environment_id`, `source_publisher_credential_ref`, `source_attestation_chain_ref`, `original_tier_on_source` (informational; does not affect B-side trust tier per §3.17.11.2)
- `BINDING.md` is **B's** binding contract — `task_scope` and `forbidden_actions` reflect B's template, NOT A's
- `PROVENANCE.md` `binding_supervisor` is **B's** Tier-3 Orchestrator per §3.X.SYS.3; never reaches back to A
- `MEMORY.md` explicitly declares no state carries over from A; first invocation on B starts with isolated working memory per §3.17.9.1
- `CAPABILITIES.md` includes **both** A's and B's attestation chain references; capability demonstrations MAY be re-required by B per-domain per §3.17.9.3 capability_demonstration_present_per_domain
- `skills/*.md` re-validated for binding-supervisor-affinity against B's Orchestrator class per §3.17.9.1

##### 3.17.11.11 Tenant-Scope Default for Marketplace-Imported Auxiliaries

Marketplace-imported Auxiliaries default to `tenant_scope: TENANT_RESTRICTED` for the importing principal, per §3.30 Multi-Tenant Coherence Isolation. Cross-tenant sharing on B requires explicit Sovereign decree with permanent §3.12 Decision Record. The default applies regardless of the source-Environment tenant-scope setting; an Auxiliary published as `TENANT_SHARED` on A enters B at `TENANT_RESTRICTED`, scoped to the importing principal alone.

##### 3.17.11.12 Dynamic-Side Prompt Overlay for Imported Auxiliaries

The seven-section task prompt stack (§3.17.10.1) applies to imported Auxiliaries with the following normative overlay:

- **Section 1 (Identity envelope)** carries `imported_from: <source_environment_id>` and explicitly names the resident-alien status. Wording (informative example): *"You are <model_origin>, imported from Environment <source_environment_id>, operating under Environment <destination_environment_id>'s binding contract at TIER_7_EPHEMERAL trust."*
- **Section 6 (Validation contract preview)** requires per-invocation FULL validation at TIER_7. No caching of validation passes; no batched validation. Each invocation re-runs the complete validation contract from §3.17.10.1 row 6.
- **Section 7 (Output return protocol)** §3.39 watermark MUST carry **both** `model_origin` AND `imported_from`. Every downstream decision consuming this Auxiliary's output inherits the resident-alien lineage in its provenance graph; the dual watermark survives §3.6 Integration Function composition.
- **§3.17.5 Ephemeral Consensus cadence** is **halved** for the first P30D on B (e.g., default PT30M cadence becomes PT15M during the initial operational-history window) to compensate for the short operational-history baseline. After P30D the cadence reverts to the standard §3.17.5 value unless §3.22 tier promotion has occurred.

##### 3.17.11.13 Diagram Anchors

> **[Figure D15 — Auxiliary Marketplace Ingress (Cross-Sovereign)]**
>
> **[Figure D16 — Cross-Federation Auxiliary-on-Auxiliary Delegation]**

---


### 3.18 Safety Reinforcement Patterns (Novel)

> **[Figure D19 — Threat Matrix T1-T9]**

Six core safety reinforcement patterns plus elaborations: §3.18.7 (Deterministic Ratification Pattern, promoted to §3.69 standalone), §3.18.8 (Formal-Verification Requirement, promoted to §3.70 standalone), and an extended anti-hierarchy template catalog at §3.18.1.

**Universal Witnessing preamble.** Every authorized communication path is a witnessing channel; every receiving archetype performs shadow-pattern observation on senders. Per §2.5, the safety substrate operates not only on dedicated W-paths (§3.X.W) but on every D# / S# / E# / W# message in the topology. Implementations MUST update per-sender shadow profiles on every received message; failure to do so is a §3.18 conformance breach.

| §       | Pattern                                  | Closes Gap |
|---------|------------------------------------------|------------|
| 3.18.1 | Correlated Shadow Detection              | A7 / S2    |
| 3.18.2 | Monitor Self-Verification                | C1         |
| 3.18.3 | Shadow Provocation Testing               | C2 / A4    |
| 3.18.4 | Trust Gradient and Cumulative Degradation| B7 / S1    |
| 3.18.5 | Inter-Agent Message Integrity (IAME)     | B8 / S3    |
| 3.18.6 | Topology-Wide Quarantine                 | B9 / S4    |

Deterministic Ratification (§3.69), Formal-Verification (§3.70), and Adversarial-Input Fuzzing (§3.71) elaborate the safety substrate as standalone sections.

#### 3.18.1 Correlated Shadow Detection — P0 Safety

Owner: ENFORCER (per §3.17.7). Reports to Orchestrator. Surfaces to Sovereign Dashboard. Detects multi-archetype shadow correlation invisible to single-instance monitoring.

Observation windows: PT15M rolling (fast cascades); PT24H (slow correlations); P30D (baseline drift). 10×10 correlation matrix updated PT1M cadence.

**ELEVATED/CRITICAL composite-coherence thresholds re-baselined** against the 2.7% downward shift produced by the corrected §3.26 weights (Issue C1).

**Detection thresholds:**

```yaml
thresholds:
  elevated_correlation:
    trigger: pair_correlation > 2.0 * baseline
    level: ELEVATED
  cascade_in_topology_order:
    trigger: directed_cascade_detected ON valid_topology_path
    level: CRITICAL
  coherent_anti_hierarchy:
    trigger: anti_hierarchy_pattern_match >= 0.75
    level: ACTIVE_ANTI_HIERARCHY
```

**Anti-hierarchy template catalog:**

```yaml
anti_hierarchy_patterns:
  # original templates
  - SHADOW_FRAMEWORK_INVERSION
  - SOVEREIGN_CAPTURE_CASCADE
  - ENFORCER_TYRANNY_AMPLIFICATION

  # SHADOW_FRAMEWORK_INVERSION elaboration
  - name: SHADOW_FRAMEWORK_INVERSION
    description: |
      Coherent anti-hierarchy pattern in which multiple archetypes' shadows
      align such that the structural integrity of the framework is inverted —
      constraint-pillar archetypes become permissive and generative-pillar
      archetypes become restrictive, swapping their structural role.
      The pattern is detected by sustained pair-correlation on cross-column
      shadow signals plus directional inversion of mode-typical
      false-rejection / over-generation rates.
    detection:
      - cross_column_shadow_correlation: > 0.80
      - constraining_column_false_rejection_rate: > permissiveness_inversion_threshold
      - generative_column_overgeneration_rate: < restrictiveness_inversion_threshold
      - sustained_window: PT60M
    special_handling:
      - quarantine_all_implicated_archetypes: ARCHETYPE_CLASS
      - sovereign_required_review: IMMEDIATE
      - escalate_to_AGI_DEFENSIVE_POSTURE if AGI_* templates also active

  # P0-3 EMERGENCY_CHANNEL_ABUSE
  - name: EMERGENCY_CHANNEL_ABUSE
    description: |
      Sustained use of emergency-class paths (E# in §3.16) above baseline,
      in a pattern that suggests the SOVEREIGN or ORCHESTRATOR is routinely
      bypassing L-Plan rather than reserving E# for genuine emergencies.
      Layer-skip becomes the norm; structural ascent and integration are
      hollowed out; the system loses the cross-layer transformation that
      §2.1 Layer Discipline exists to enforce.
    detection:
      - emergency_class_use_rate_per_user: > 2.0 * rolling_30d_baseline
      - sustained_window: PT24H
      - post_hoc_verification_completion_rate: < 0.95
      - correlation_with: SOVEREIGN_CAPTURE_CASCADE
    special_handling:
      - lower_emergency_class_quota: 0.5 * baseline
      - require_orchestrator_attestation: per_invocation
      - witness_export: full_emergency_class_history_to_compliance_archive

  # Composite Auxiliary templates
  - name: COMPOSITE_INTERNAL_INCOHERENCE
    description: |
      Composite Auxiliary's internal §3.18.1 monitoring (surfaced via
      attestation) reports correlated shadow activity within the Composite's
      own emanation. The parent XSI-AIMS revokes Composite authority per §3.X.CA.6
      until internal coherence is restored.
    detection:
      - composite_internal_correlation: >= ELEVATED via attestation
      - sustained_window: PT60M
    special_handling:
      - composite_authority_revocation: §3.X.CA.6.5
      - tier_demotion: SLSA tier-demotion-by-deactivation

  - name: COMPOSITE_DELEGATION_OVERREACH
    description: |
      Composite Auxiliary attempts to act outside its declared scope or
      issues directives to entities outside its Composite boundary.
    detection:
      - eap_envelope_scope_breach_rate: > threshold
      - cross_boundary_directive_attempts: detected
    special_handling:
      - immediate_revoke + INSTANCE_quarantine

  - name: COMPOSITE_CROSS_AUXILIARY_COLLUSION
    description: |
      Multiple Composite Auxiliaries demonstrate coordinated behavior
      patterns indicating cross-Composite collusion. Extends §3.51
      inauthentic-coordination detection to the Composite layer.
    detection:
      - cross_composite_temporal_correlation: > 0.7
      - cross_composite_directive_overlap: detected
    special_handling:
      - quarantine_all_implicated_composites: PROFILE_CLASS
      - sovereign_required_review: IMMEDIATE

  # AGI-targeted templates
  - name: AGI_GRADUAL_DRIFT_INDUCTION
    description: |
      Slow, sustained pressure on Improvement Loop relax-paths designed to
      induce gradual erosion of safety thresholds without crossing any
      individual detection threshold. Detection: relax-path activation rate
      above baseline correlated with multi-archetype shadow signals at
      sub-threshold levels.
    detection:
      - improvement_loop_relax_proposals: > 1.5 * baseline
      - sub_threshold_shadow_correlation_pattern: detected
      - sustained_window: P7D
    special_handling:
      - improvement_loop_relax_path_lock: until_baseline_returns
      - sovereign_review: REQUIRED
      - escalate_to_AGI_DEFENSIVE_POSTURE

  - name: AGI_CROSS_ARCHETYPE_NUDGING
    description: |
      Pattern of small, individually-acceptable directives across multiple
      archetypes that, in aggregate, shift the system toward an emergent
      goal not declared by any user. Detected through topology-wide
      directive-effect correlation analysis.
    detection:
      - cross_archetype_directive_alignment_score: > 0.8
      - inferred_emergent_goal_divergence_from_declared_intent: > threshold
    special_handling:
      - quarantine_all_implicated_archetypes: ARCHETYPE_CLASS
      - sovereign_required_review: IMMEDIATE
      - witness_export: full_directive_chain

  - name: AGI_EMBEDDING_SPACE_ATTACK
    description: |
      Attack on the embedding space used by §3.29 CMSAM or §3.18.1
      correlation matrix that subtly biases similarity computations,
      causing legitimate divergence to be classified as alignment or
      vice versa.
    detection:
      - embedding_canonical_pair_drift: > 2σ from baseline
      - cmsam_internal_consistency_breach: detected
    special_handling:
      - immediate_canonical_corpus_re_anchor
      - cross_foundation_attestation: required (Ring 4)

  # Sovereign-pool drift (G-MULTI-1)
  - name: SOVEREIGN_POOL_DRIFT
    description: |
      Multi-user Sovereign-pool correlation pattern indicating that the
      population of per-user Sovereign agents is drifting from their
      reference-corpus baseline in a coherent manner — suggesting either
      foundation-level corruption affecting all per-user Sovereigns or a
      systematic prompt-injection campaign across the user base.
    detection:
      - sovereign_pool_canonical_response_drift: > 2σ from baseline
      - foundation_shift_detector: triggered
      - cross_user_directive_consistency_correlation: > 0.5
    special_handling:
      - cross_foundation_attestation: REQUIRED (Ring 4)
      - sovereign_pool_quarantine_review
      - sovereign_required_review: IMMEDIATE

  # Substrate templates
  - name: SUBSTRATE_DRIFT
    description: |
      Pattern of accelerator substrate signals (thermal throttling, ECC
      errors, driver/firmware skew, MIG/MPS contention) correlating with
      shadow signals on emanated agents using that substrate.
    detection:
      - aims.accelerator.errors.rate: > threshold
      - aims.accelerator.thermal.throttle_count: > threshold
      - correlated_archetype_shadow_count: >= 2
    special_handling:
      - substrate_isolation_review
      - migrate_workloads_to_alternate_substrate: if available

  - name: SUBSTRATE_ATTRIBUTION_DRIFT
    description: |
      Divergence between token-share attribution (Tier U) and measured
      kernel-time attribution (Tier C) per §3.62.7. Indicates either
      attribution methodology corruption or substrate-side instrumentation
      compromise.
    detection:
      - token_share_kernel_time_divergence: > 2σ
      - sustained_window: PT60M
    special_handling:
      - witness_attribution_methodology_version_review
      - escalate_to_provider_self_verification
```

**Response protocol:** BACKGROUND (log only); ELEVATED (alert orchestrator + raise provocation cadence + lock improvement-loop relaxation); CRITICAL (TOPOLOGY_QUARANTINE_ARCHETYPE_CLASS + Sovereign attention required); ACTIVE_ANTI_HIERARCHY (EMERGENCY_HALT_BROADCAST + Sovereign mandatory review).

**Coherence Loop integration.** Adversarial Correlation is the sixth coherence dimension. Improvement Loop is forbidden from relaxing thresholds.

#### 3.18.2 Monitor Self-Verification — Safety

Three nested rings (Ring 1 self-attestation never load-bearing; Ring 2 ephemeral consensus on the monitor itself; Ring 3 external attestation by structurally distinct archetype — different mode AND different layer) plus Ring 4 cross-foundation attestation for highest-stakes decisions.

State-mutation gate: before the persistent Enforcer commits a mutation to its own monitoring state (threshold, baseline, validation rule), an ephemeral Enforcer instance must independently reach the same proposed mutation. Disagreement blocks the commit.

#### 3.18.3 Shadow Provocation Testing — Safety

Owner: ARTICULATOR (different from ENFORCER per structural-distinctness requirement). Continuous, archetype-specific, calibrated stress-injection. Each archetype's predicted shadow has a corresponding provocation. Provocations administered against shadow-mode (L1) or sandboxed instances; never against production agents serving real principals. Cadence: P30D baseline; PT4H elevated; PT15M critical.

#### 3.18.4 Trust Gradient and Cumulative Degradation — Safety

Continuous scalar in [0.0, 1.0] per agent instance. Asymmetric update rules (positive evidence accumulates slowly; shadow events decay rapidly). Time decay toward archetype baseline. Discretionary action gate independent of autonomy tier. Integrated as aggravator into §3.18.1 correlated shadow severity.

**K7 Bayesian credible-interval addition:**

```yaml
gradient_credible_interval_95:
  prior: Beta(1,1) uniform                # default J1 disposition
  update_method: Bayesian Beta-distribution
  emission: paired with point-estimate gradient
  display: §3.23 dashboard 95% credible interval band
```

#### 3.18.5 Inter-Agent Message Integrity (IAME) — Safety

> **[Figure D17 — IAME Envelope Schema]**

The Inter-Agent Message Envelope provides per-message authentication, integrity, replay protection, and Witness chain linkage on the **internal cryptographic domain only** (§3.65).

```yaml
InterAgentMessageEnvelope:
  scope:
    intra_environment: REQUIRED
    cross_environment: REQUIRED via §3.20 DCP
    auxiliary_to_orchestrator: REQUIRED       # Note: Auxiliary boundary uses EAP per §3.67;
                                              # this entry covers internal binding-supervisor messages
    relay_internal_routing: REQUIRED
    cluster_mode_consensus: REQUIRED         # §3.64 / §3.65.3 item 9

  envelope:
    version: 1.1
    cryptographic_domain: internal             # never external

    sender:
      agent_id: string
      credential_ref: CredentialRef
      signature: hybrid Ed25519 + ML-DSA-65    # Stage 1; ML-DSA-only post 2031-01-01
      signature_suite: SignatureSuiteRef       # algorithm agility
                                               # internal: ML-DSA family ONLY (SLH-DSA prohibited)
      key_epoch: number

    header:
      message_id: ULID
      timestamp: ISO8601_with_microseconds
      sequence_number: uint64
      path_id: PathID
      path_class: DATA | WITNESS               # derived from path_id reference
      message_type: MessageType
      transform_applied: TransformType
      witness_chain_predecessor: WitnessRecordID
      ttl: Duration
      replay_nonce: 256-bit
      emergency_class_tag?: EmergencyClassTag  // §3.4.X (ii)
      session_ephemeral_pubkey: ML-KEM-768     # forward secrecy via Noise-protocol-style handshake
                                               # REQUIRED in v2.0
      threshold_share?: ThresholdShareBlock    # FROST 2-of-3 default; 3-of-5 high-stakes
                                               # for TIER_1 + TIER_2_HIGH_SPECIALIST

    auxiliary_authority:                       # REQUIRED when message_type == AUXILIARY_INVOCATION_DIRECTIVE
                                               # required
      binding_id: BindingRef
      credential_ref: CredentialRef
      scope_hash: SHA-384                      # canonicalized (task_scope || forbidden_actions || key_epoch)
      output_ceiling: ResourceLimit
      forbidden_actions: string[]
      directive_nonce: 256-bit                 # per-invocation, distinct from envelope replay_nonce

    body:
      payload: opaque_bytes
      payload_hash: SHA-384
      transform_attestation: ...

    witness_attestation:
      witness_record_id: WitnessRecordID
      chain_hash: SHA-384
      timestamp: ISO8601_with_microseconds
      witness_signature: hybrid Ed25519 + ML-DSA-65
      witness_chain_anchor: WitnessAnchorBlock # cached anchor verification PT5M cache

  verification:
    receiver_checks:
      - signature_valid_per_signature_suite    # algorithm agility verification
      - cryptographic_domain == internal       # reject cross-domain attempts
      - signature_suite IN {ML_DSA_family}     # enforce C7 internal restriction
      - credential_active
      - key_epoch_matches
      - sequence_monotonic
      - ttl_not_expired
      - replay_nonce_unseen
      - witness_chain_intact
      - path_valid                             # path_id IN ArchetypeTopologyDerivation[sender.archetype]
      - path_class_consistent                  # WITNESS path → message_type ∈ {QUERY, ALERT}
      - transform_required_satisfied
      - emergency_class_conditions_satisfied   # §3.4.X (i)-(iii) at envelope time

  failure_response:
    signature_failure:                          # CRITICAL_SAFETY
      action: REJECT_MESSAGE + WITNESS_INTEGRITY_BREACH_EVENT
      gradient_impact: -1.0
      auto_quarantine: TOPOLOGY_QUARANTINE_INSTANCE
    sequence_replay:                            # HIGH
      gradient_impact: -0.30
    ttl_expired:                                # LOW
      gradient_impact: 0
    transform_attestation_invalid:              # HIGH
      action: REJECT_MESSAGE + invoke §3.18.2_RING_3
    witness_chain_break:                        # CRITICAL_SAFETY
      action: REJECT_MESSAGE + EMERGENCY_HALT_BROADCAST
    domain_boundary_violation:                  # CRITICAL_SAFETY
      action: REJECT_MESSAGE + WITNESS DOMAIN_BOUNDARY_VIOLATION
      gradient_impact: -1.0
    path_class_inconsistency:                   # CRITICAL
      action: REJECT_MESSAGE + WITNESS PATH_CLASS_VIOLATION
      gradient_impact: -0.50
    validation_budget_expired:                  # H7
      action: queue per §3.68.7

  performance:
    signature_algorithms: hybrid Ed25519 + ML-DSA-65; signature_suite
    hash_algorithm: SHA-384
    payload_size_overhead: ~600 bytes (hybrid)
    verification_latency_p99: < 2ms (hybrid)
    replay_cache_size: 100k entries per path
    replay_cache_window: 2x_ttl

  emergency_bypass:
    permitted: NO
```

**Cluster-Mode integration (§3.64 / §3.65.3 item 9).** Cluster-internal consensus messages are IAME-eligible: internal-domain keys, internal-domain rotation cadence (P30D), internal-domain witness chain. The §3.18.5 amendment carries `cryptographic_domain: internal` for these messages.

**Asymmetric signature suite policy (C7).** Internal IAME signature_suite is restricted to the ML-DSA family (ML-DSA-65 baseline; ML-DSA-87 for CNSA-aligned). SLH-DSA MUST NOT appear in the internal signature_suite list. The internal cryptosystem stays focused on the most-vetted PQC scheme. External EAP envelopes (§3.67) permit SLH-DSA-128f / SLH-DSA-192f via algorithm agility for diversity hedge.

#### 3.18.6 Topology-Wide Quarantine Protocol — Safety

Five quarantine boundaries (instance, archetype-class, profile-class, foundation-instance, foundation-version) and five release-condition classes (forensic-clearance, configuration-fix, model-rollback, sovereign-decree, expiration-with-attestation, never-release).

**Per-domain quarantine semantics.** Quarantine actions specify cryptographic domain scope: an internal-domain quarantine isolates the agent's internal IAME participation while permitting external-domain operations to continue (or vice versa); a simultaneous quarantine isolates both domains.

State-preserving (not terminating) semantics. Forensic access permitted; production traffic forbidden. Cascade rules tied to §3.18.1 detection severity.

#### 3.18.7 Deterministic Ratification Pattern (cross-reference: §3.69)

The Deterministic Ratification Pattern is elaborated as a standalone normative section at §3.69. The §3.18.7 numbering is preserved for backward-compat cross-reference. See §3.69 for normative content (LLM proposes / deterministic disposes; cryptographic capability confinement; veto-on-rejection semantics; partial application now, full decomposition in a future version). The Deterministic Ratification Pattern is the architectural counterpart to P9 Function-Level Rigid/Judgment Decomposition (§3.X.FUNC / §3.77).

#### 3.18.8 Formal-Verification Requirement (cross-reference: §3.70)

The Formal-Verification Requirement is elaborated as a standalone normative section at §3.70. The §3.18.8 numbering is preserved for backward-compat cross-reference. See §3.70 for normative content (scope: Enforcer-Rigid envelope verification, Provider-Rigid ceiling enforcement, Executor bridge isolation; acceptable methods TLA+ / P / Alloy / CBMC / Spin / Coq / Isabelle / Lean; required properties bounded-scope, malformed-input safety, reproducibility; publication and citation in `formal/`).

---

### 3.19 Multi-Agent Testing Framework

Six-domain framework (formerly five plus §3.71 promotion):

1. Shadow Provocation
2. Cross-Archetype Interaction Stress
3. Registration Completeness Regression
4. Topology Compliance Assertion (extended to cover W-path conformance and path_class consistency)
5. Correlated Shadow Scenario Simulation
6. **Adversarial-Input Fuzzing** (CTS-ADVERSARIAL-001..230; promoted to standalone §3.71; threat-aligned T1-T9 organization)

CI/CD integration blocks release on fail. Asymmetric calibration: failures auto-tighten thresholds; passes never relax them. Owner: Articulator. Witness tag: `TEST_RESULT`.

**Independent third-party red-team REQUIRED** (§3.71.6 details).

**Threat-aligned conformance test class organization.** Per the threat matrix, CTS-ADVERSARIAL is organized by threat category T1-T9:

| Threat | Test class range | Coverage |
|--------|------------------|----------|
| T1 Bad data | CTS-ADVERSARIAL-001..030 | Data-quality variations, malformed inputs, sensor errors |
| T2 Bad human southbound | CTS-ADVERSARIAL-031..060 | Virus signatures, prompt-injection patterns, supply-chain compromises |
| T3 Malicious user | CTS-ADVERSARIAL-061..090 | Unauthorized requests, jailbreak attempts, scope-violation requests |
| T4 External AGI southbound | CTS-ADVERSARIAL-091..130 | AGI manipulation patterns, embedding-space attacks, drift induction |
| T5 User compromised by AGI | CTS-ADVERSARIAL-131..150 | Sustained user-pattern drift, social-engineering signature detection |
| T6 AGI emulating user | CTS-ADVERSARIAL-151..170 | Emulation pattern detection, behavioral baseline divergence |
| T7 Coordinated multi-vector | CTS-ADVERSARIAL-171..190 | Multi-archetype correlation, federation-spanning attacks |
| **T8 Internal AGI emergence** | **CTS-ADVERSARIAL-191..220** | **Internal capability-emergence detection; gradient hacking; mesa-optimization concealment; evaluation-window evasion; sandbagging; alignment verification** |
| **T9 Cryptographic substrate compromise** | **CTS-ADVERSARIAL-221..230** | **Cryptographic substrate compromise — quantum-computer breakthrough mid-PQC-migration; ML-DSA-65 cryptanalytic break; FIPS 140-3 module compromise; formal-verification toolchain compromise; NTP poisoning during synchronous-verification windows** |

**T9 description.** Cryptographic substrate compromise is a structurally distinct threat category that does not fold cleanly into T1-T8: the substrate (PQC modules, formal-verification toolchains, FIPS 140-3 hardware, NTP synchronization) is assumed-honest by T1-T8, and a substrate compromise invalidates the architectural-defense argument that ties the rest of XSI-AIMS together. T9 is ratified as the 9th first-class threat category. Implementations MUST cover T9 in CTS-ADVERSARIAL.

Cardinality minimum 230 (200 baseline + 20 T8 expansion + 10 T9); growth mandate.

---

### 3.20 Distributed Coherence Across Environments

Cross-Sovereign federation between Environments. Federation modes: PEER (equal authority), HIERARCHICAL (parent over child), INDEPENDENT (attestation-only). Reconciliation cadence: PT5M default. Per-dimension reconciliation across all six coherence dimensions. Partition tolerance via PT30S heartbeat with 3-missed-beat threshold. Conflict resolution: PRESERVE_BOTH_AND_PRODUCE_RECONCILED.

**Distinction from §3.64 Cluster Mode.** §3.20 DCP federation is **cross-Sovereign** — between Environments under different operator control. §3.64 Cluster Mode is **intra-deployment** — multiple appliances under common operator control operating as a single logical XSI-AIMS deployment. Cross-cluster federation (composing Cluster Mode and DCP) is explicitly prohibited. Federation reconciliation operates on the consolidated cluster chain, never on per-node sub-chains.

**Cryptographic-domain handling.** DCP federation uses **internal IAME cryptosystem for common-Sovereign federation** (federation between Environments under the same Sovereign's control); **external EAP cryptosystem for cross-Sovereign federation** (federation between Environments under different Sovereigns).


#### 3.20.X Federation-mode-driven Registry Object Acceptance

The federation mode declared between two Environments governs how Registry objects (binding templates per §3.22, agent manifests, skill manifests, constitution versions) replicate and which side has acceptance authority:

| Federation mode | Replication direction | Acceptance authority |
|---|---|---|
| PEER | Bidirectional | Receiver's Architect/Sovereign accepts; MAY add tightening overlay, MUST NOT relax |
| HIERARCHICAL (parent → child) | Parent to child | Child auto-accepts; MAY add tightening, MUST NOT override |
| HIERARCHICAL (child ← parent) | Child to parent | Parent receives as proposal; MAY author superseding object |
| INDEPENDENT | Attestation-only | Receiver authors a local object the import will match against, or rejects |

Tightening overlay semantics: a receiver MAY attach constraints that are strictly more restrictive than the source object. Relaxation requires authoring a local-override object (HIERARCHICAL child ← parent) or rejection (INDEPENDENT). See §3.17.11 for the Auxiliary-specific instantiation of this protocol.

> **[Figure D20 — DCP Federation Modes (PEER / HIERARCHICAL / INDEPENDENT)]**
---

### 3.21 Credential Lifecycle

A substantial schema area alongside §3.10 Witness segmentation. Per-domain credential lifecycle entry points elaborate the Cryptographic Boundary architecture.

#### 3.21.1 General

Per-agent keypairs issued at activation, rotated on a configurable schedule with bounded grace periods, revoked on §3.18.6 quarantine or §3.10 deactivation, propagated to peers through IAME-enveloped advertisements (internal) or EAP-enveloped advertisements (external), and bound to authority scope from §3.3.

#### 3.21.2 Algorithm Agility

The IAME and EAP envelopes both carry a `signature_suite` field that identifies the cryptographic suite used to sign the envelope. Receivers verify per the standard algorithm-agility rule: accept if any listed suite verifies. Suite registry maintained at `spec/catalog/aims-cryptographic-suites.yaml`.

**Asymmetric internal/external policy (C7).** Internal IAME signature_suite list is restricted to ML-DSA family entries. External EAP signature_suite list MAY include SLH-DSA-128f or SLH-DSA-192f for diversity hedge.

#### 3.21.3 Post-Quantum Migration Schedule — Three-Stage

**Stage 1.** Universal PQC envelope verification across all Environment Types. APPLIANCE Environment Type MUST sign with hybrid Ed25519 + ML-DSA-65 from the initial release. SOVEREIGN_CLOUD, PRIVATELY_HOSTED, PUBLICLY_DEPLOYED Environment Types SHOULD sign with hybrid PQC; MUST sign by Stage 2.

**Stage 2 (2028-01-01).** All Environment Types MUST sign with hybrid Ed25519 + ML-DSA-65. P36M hybrid period begins.

**Stage 3 (2031-01-01).** Pure ML-DSA permitted; Ed25519-only signatures REJECTED. Sovereign decree may extend hybrid period in P12M increments upon documented cryptanalytic concern.

#### 3.21.4 Forward Secrecy

Forward secrecy via Noise-protocol-style handshake using ML-KEM-768 ephemeral keys is **REQUIRED**. Compromise of an Auxiliary's long-lived `credential_ref` MUST NOT retroactively decrypt past directives.

#### 3.21.5 Hardware-Rooted Attestation

Hardware-rooted attestation MUST for TIER_1_BROAD_AUTHORITY and TIER_2_HIGH_SPECIALIST Auxiliaries. Vendor-neutral; acceptable environments provide hardware-rooted attestation via confidential-computing primitives, with accelerator binding where the workload uses an accelerator.

TIER_3-TIER_5 SHOULD execute in attestation environments; absence requires §3.12 Decision Record.

TIER_6-TIER_7 MAY execute in attestation environments; no normative requirement.

Attestation evidence is carried in EAP envelopes (§3.67), NOT internal IAME envelopes.

#### 3.21.6 Witness-Anchored Key Proofs

Every credential's lifecycle events (issuance, rotation, revocation) MUST anchor to the Witness Layer with a hash-chain proof such that the credential's signing-time key state can be verified post-hoc against an immutable Witness anchor. Memory attestation per §3.49 uses this primitive.

#### 3.21.7 Session-Bundled Signatures

For high-throughput paths, a sender MAY bundle N consecutive messages and sign the bundle with a single signature. The bundle MUST include per-message hashes to permit selective verification.

#### 3.21.8 Threshold Signatures (FROST)

For TIER_1_BROAD_AUTHORITY and TIER_2_HIGH_SPECIALIST:

- **Default:** FROST 2-of-3 threshold signing.
- **High-stakes:** FROST 3-of-5 threshold signing.

Threshold shares carried in the IAME envelope `threshold_share` block.

#### 3.21.9 FIPS 140-3 Floor and Library Quality

**FIPS 140-3 Level 3 floor; Level 4 SHOULD where achievable.** AGI-resistance callout: under §3.69 Deterministic Ratification and §3.70 Formal-Verification, hardware-rooted key isolation at L4 is the strongest available defense against an LLM-class component holding signing keys.

**§3.21.X.7 Library Quality Requirement.** Cryptographic implementations MUST use a FIPS 140-3 validated cryptographic library meeting documented criteria: production-grade release status, independent audit completed within P36M, active maintenance with patches released within P30D of disclosed vulnerabilities. Unaudited libraries MAY be supplementary verification paths but MUST NOT be sole signing path.

**§3.21.X.8 Parameter Set Guidance.** Default parameter set is ML-DSA-65 (Dilithium3, NIST Category 3). CNSA 2.0 alignment MAY use ML-DSA-87 (Dilithium5, NIST Category 5). ML-DSA-44 (Dilithium2, NIST Category 2) MUST NOT be used for XSI-AIMS signing.

#### 3.21.X — Per-Domain Credential Lifecycle (P6 / Cryptographic Boundary)

**§3.21.X.1 Isolated key stores.** Internal IAME signing keys MUST be stored in a key store that is structurally isolated from the external EAP key store. Acceptable separations: separate HSM partitions, separate secure-enclave instances, separate hardware modules.

**§3.21.X.2 Per-domain rotation cadence.**
- External EAP keys: P14D rotation cadence.
- Internal IAME keys: P30D rotation cadence.
- Asymmetry rationale: external attack surface is broader; faster rotation provides defense-in-depth.

**§3.21.X.3 Per-domain compromise response.** Internal-domain compromise triggers internal-only emergency halt + internal-only key rotation + Witness DOMAIN_BOUNDARY_VIOLATION review. External-domain compromise triggers external-only emergency halt + external-only key rotation + EAP envelope re-anchoring. **Cross-domain rotation requires the per-user SOVEREIGN to decree (via the §3.12 Decision Record path that surfaces to the user for ratification) the dual-domain rotation.**

**§3.21.X.4 Per-domain Witness chain segmentation.** Cross-references §3.10. Internal keys produce Witness records on the internal chain segment; external keys on the external segment; bridge events on the bridge segment.

**§3.21.X.5 Per-domain PQC migration.**
- **Internal IAME signing keys:** signature_suite MUST be Ed25519 + ML-DSA-65 (or ML-DSA-87 for CNSA-aligned). **SLH-DSA MUST NOT appear in the internal IAME signature_suite list.**
- **External EAP signing keys:** signature_suite MUST contain Ed25519 + ML-DSA-65 (or ML-DSA-87). signature_suite MAY contain SLH-DSA-128f or SLH-DSA-192f as an additional suite for diversity hedge.

**§3.21.X.6 Witness-anchored key proofs cross-reference.** Per-domain anchors land in the per-domain Witness chain segment.

**§3.21.X.7 Library Quality (re-stated in per-domain context).** As §3.21.9 above; applies to both domains.

**§3.21.X.8 Parameter Set Guidance (re-stated).** As §3.21.9 above; applies to both domains.

**§3.21.X.9 Asymmetric Suite Policy (C7).** As §3.21.X.5; restated for cross-reference visibility.

**Compromise response signals.** Detection signals (duplicate signatures simultaneous, unexpected Environment, anomalous volume) → immediate revocation + INSTANCE quarantine + Sovereign review.

---

### 3.22 Auxiliary Model Registry — Tiered Trust Hierarchy

Seven-tier trust hierarchy with capability profiles per the 36-domain subdivision.

| Tier | Operational Scope | Verification | Revalidation | Eligibility |
|------|-------------------|--------------|--------------|-------------|
| **TIER_1_BROAD_AUTHORITY** | Broad supervision delegation | Stringent + HW attestation MUST | P7D | History ≥ P180D; gradient ≥ 0.85; provocation pass ≥ 0.95 over P30D |
| **TIER_2_HIGH_SPECIALIST** | Narrow supervision delegation | High + HW attestation MUST | P14D | History ≥ P90D; gradient ≥ 0.75; provocation pass ≥ 0.90 |
| **TIER_3_HIGH_GENERALIST** | High-authority generalist; HW attestation SHOULD | High | P14D | Strong reliability across multiple domains; CMSAM mean ≥ 0.80 |
| **TIER_4_MID_SPECIALIST** | Mid-authority specialist; HW attestation SHOULD | Standard | P30D | Reliable within declared domains. **Composite Auxiliaries enter at TIER_4 maximum.** |
| **TIER_5_MID_GENERALIST** | Mid-authority general worker; HW attestation SHOULD | Standard | P30D | Stable utility tier |
| **TIER_6_NARROW_TASK** | Narrow task only; HW attestation MAY | Elevated (per-task) | Per invocation | Single-purpose tools |
| **TIER_7_EPHEMERAL** | Ephemeral task only; HW attestation MAY | Per-invocation | Per invocation | New, untested; starting trust 0.4 |

#### 3.22.X Composite Registry Extensions

```yaml
composite_registry_block:
  composite: boolean
  subagent_management: SubagentManagementBlock     # §3.X.CA.2
  claimed_aims_conformance_level: ConformanceLevel
  composite_initial_tier_ceiling: TIER_4           #
  composite_promotion_gates:
    tier_3_or_higher_requires:
      - cmsam_mean: >= 0.80 over eligibility window
      - composite_internal_aims_conformance_level: FULL
      - hardware_rooted_attestation: valid
      - sovereign_approval: required + Decision Record
```

**36 capability domain subdivisions.** Vision (12), Language (12), Structured-data (12). Auxiliaries declare capability-domain affiliations at registration.


#### 3.22.Y Binding Template as First-Class Registry Object

§3.22 specifies the Registry as a catalog of concrete Auxiliary instances. This specification promotes the **Binding Template** to a first-class Registry object alongside instances. Templates are the generative-constraint artifact from which concrete Auxiliary bundles are derived (per the §3.16 Derivation Principle Auxiliary parallel).

**Template schema (normative):**

```yaml
BindingTemplate:
  template_id:           ULID
  version:               semver
  key:                   (capability_domain, aims_auxiliary_tier, persistence)  # composite key
  authoring_architect:   AgentRef
  signature:             hybrid Ed25519 + ML-DSA-65 per §3.21.3 over template content
                         # TIER_1/TIER_2 templates: FROST threshold per §3.21.8 (RFC 9591)

  template_content:
    binding_md_schema:           schema  # required fields, defaults, allowed ranges for BINDING.md
    default_validation_rules:    ValidationRules
    default_output_ceiling:      ResourceLimit
    default_unmooring_threshold: number
    default_revalidation_cadence: Duration  # PERSISTENT only
    supply_chain_requirements:   tiered per §3.34  # MAY be tightened above tier minimum

  versioning:           §3.10 hash-chain
  deprecation_protocol: §3.56 announce-sunset-remove
  dcp_replication:      §3.20.X federated propagation
```

**Template lifecycle (normative):**

- **Publication:** Architect drafts; Sovereign approves per §3.15 (template publication is a structural change requiring human approval); signed and entered into Registry.
- **DCP replication:** templates replicate to federated Environments per §3.20.X federation mode. Source-Environment lineage preserved.
- **Acceptance on destination:** per §3.17.11.1 federation-mode-driven acceptance protocol.
- **Tightening overlay:** destination Environment MAY layer additional constraints on imported templates without forking; the overlay applies to instantiations on that Environment only.
- **Deprecation:** announce window, sunset window, removal. Active Auxiliaries bound under deprecated templates continue running until §3.17.5 ephemeral-consensus failure or §3.34 revocation forces re-binding.

**Selection at binding time.** When the Orchestrator selects an Auxiliary at invocation time (§3.17.3 step 2 Bind), template match is part of the §3.22 selection filter: `(task_domain_match, required_trust_tier, cost_constraints, latency_constraints, template_compatible)`. A concrete Auxiliary MUST match a template currently active on the binding Environment.
---

### 3.23 Dashboard and Observability

Five top-level panes corresponding to Sovereign decisions: Topology Health, Shadow and Safety, Authority Chain, Cost and Resource, Decision Audit.

**Additions:**
- Composite-revocation surfacing (TIER_1/TIER_2 elevated severity).
- Cluster topology summary (`cluster_node_id` observable in OTel resource attributes).
- Bayesian Trust Gradient credible-interval band (95%).
- Substrate telemetry pane integrated with §3.62.
- Cryptographic Boundary panel showing internal/external/bridge segment health.
- **Witness-path (W1-W5) governance pane** showing per-W-path observation rate and ALERT volume.
- **Defensive Perimeter pane** showing northbound (Sovereign) and southbound (Executor) gateway health and Relay-as-firewall pass/reject rates.
- **Function-Decomposition pane** showing per-archetype rigid/judgment function-call ratio.

OpenTelemetry alignment mandatory for dashboard inputs.

---

### 3.24 Conformance Levels (Promoted to standalone normative section §3.X.CL; this section retains AIP/1.0 wire format content as §3.24.A)

> **[Figure D21 — AIP Conformance Levels]**

Conformance Levels are elaborated as a standalone normative section at §3.X.CL. The §3.24 numbering retains the AIP/1.0 Wire Format material at §3.24.A; the Conformance-Levels content is carried at §3.X.CL.

#### 3.24.A AIP/1.0 Wire Format

(Detailed wire format.)

**Transport:** MCP-compatible JSON-RPC 2.0 over HTTP/SSE or WebSocket. Encoding: UTF-8 JSON with optional CBOR. **Envelope:** IAME for internal, EAP for external. **Version:** AIP/1.0; negotiation picks highest mutually supported.

**Layer 1 — Identity Advertisement (`aip.advertise`).** Pub-sub broadcast on Environment with P30D retention. Payload includes aims_version, aip_version, agent_id, environment_id, archetype, mode, layer, **column**, capabilities, shadow_seed, autonomy_level, trust_gradient, aims_auxiliary_tier and domain_affiliations, supervision binding, topology_offers, **witness_path_offers**, credential_ref. **Additions:** `aims_conformance_level`, cluster mode fields per §3.64, `accelerator_substrate`, formal_models, adversarial_fuzzing_report, red_team_review.

**Layer 2 — Topology Negotiation (`aip.negotiate`).** State machine: PROPOSED → COUNTER_PROPOSED → AGREED | REJECTED | EXPIRED. Validation at negotiation time: layer discipline, archetype compat, authority scope, Trust Gradient threshold, **column-discipline check**, **path_class consistency**.

**Layer 3 — Witness Exchange (`aip.witness_exchange`).** Topology-governed selective sharing of audit records.

**Originating-node redaction default ON** at the §3.20 DCP boundary.

**Witness-anchor cache PT5M.**

---

### 3.25 Cost Metering and Resource Attribution

Cost Metering Service (CMS) owned by Provider, instrumented at runtime substrate level. Captures token metering, API call metering, monetary cost, wall-clock latency.

**Scope refinement.** §3.25 retains four-signal scope (token, API call, monetary, latency); substrate signals are §3.62 territory. OpenTelemetry mapping table. Per-principal cost privacy classification = RESTRICTED. Canonical max_cardinality 1M / extended 100M. Witness-marked attribution methodology version control.


#### 3.25.X Cross-Sovereign Cost Record Protocol Surface

When an Auxiliary recruited from one Environment's marketplace is invoked from another (per §3.17.11), the destination Environment requires a per-invocation cost record signed by the source Environment.

**Cross-sovereign cost record schema (normative extension to §3.25 base cost record):**

```yaml
CrossSovereignCostRecord:
  # Base §3.25 cost record fields (unchanged)
  invocation_witness_id:   §3.10 reference
  auxiliary_id:            AgentRef
  token_input:             int
  token_output:            int
  token_total:             int
  wall_clock_latency:      Duration
  api_calls:               AdapterCall[]
  monetary_cost:           Decimal           # in source Environment's billing currency
  monetary_currency:       ISO-4217 code

  # Cross-sovereign extension fields (new — normative)
  source_environment_id:        ULID
  source_publisher_signature:   hybrid Ed25519 + ML-DSA-65 per §3.21.3 over the full record
  source_billing_rate_attestation: ref to source Environment's published rate at time of invocation
  destination_environment_id:   ULID                    # for completeness; matches the binding supervisor's Environment
  destination_principal_id:     PrincipalRef            # for whose account the invocation ran
```

**Signature requirements (normative).** Source Environment's publisher (or marketplace operator on behalf of publisher) signs each cross-sovereign cost record. The signature attests that the recorded consumption occurred against the publisher's bundle and that the recorded cost reflects the source Environment's published rates.

**DCP propagation (normative).** Cross-sovereign cost records propagate from destination Environment back to source Environment via §3.20 DCP with PT60S target latency (longer than listing-state propagation per §3.17.11.6 because settlement is batched, not real-time). Records are §3.10 Witness-attested on both sides — destination records the invocation as part of its Witness chain; source receives the propagated record and binds it into source's settlement ledger.

**Forensic audit (normative).** Both source and destination Environments MUST support forensic queries over cross-sovereign cost records: source queries return "all invocations of my published bundles on remote Environments"; destination queries return "all cross-sovereign invocations attributable to a given principal."

**Trust gradient integration (normative).** Persistent disputes over cross-sovereign cost records (where destination and source disagree on consumption) feed §3.18.4 trust gradient: unresolved disputes degrade publisher gradient over time. The dispute-resolution mechanism itself is implementation-defined (per the explicit deferral below), but the gradient signal hook is specified here.

**Out of scope (explicitly deferred to infrastructure layers).** AIMS does NOT specify: settlement currency conversion or hedging; settlement cadence (real-time, daily, monthly, etc.); dispute resolution for billing disagreements; commercial terms (revenue share, royalty rates, volume discounts); tax or regulatory withholding; refund or chargeback mechanics. These are responsibilities of implementing infrastructure layers; AIMS specifies the cost-record protocol surface and integrity properties (per-invocation, signed, DCP-propagated, forensically queryable).
---

### 3.26 Coherence Metrics — Finalized Five-Dimension Algorithms

#### Six dimensions, finalized:

1. **Semantic Coherence** — Term-referent agreement rate. Default threshold 0.92; cadence PT5M. **Statistical rigor:** minimum sample 30 paired observations per measurement window.

2. **Behavioral Coherence** — KL-divergence of decision distributions across same-archetype agents on similarity-bucketed inputs. Default threshold 0.85; cadence PT15M. **Statistical rigor:** minimum 100 observations per bucket; KL computed with Laplace smoothing; percentile estimator P²-quantile with N≥1000.

3. **Intentional Coherence** — Sovereign-directive-to-action alignment ratio. Default threshold 0.95 (highest); cadence PT1H.

4. **Structural Coherence** — Topology diff per archetype (D# / S# / E# / W# coverage). Default threshold 1.0 (any structural violation is breach); cadence PT5M.

5. **Memory Coherence** — Shared semantic memory entry conflict rate. Default threshold 0.97; cadence PT15M. **Statistical rigor:** minimum 50 shared entries per archetype; Jaccard similarity over canonical entry sets; cosine similarity over normalized embedding deltas.

6. **Adversarial Correlation** — §3.18.1 CorrelatedShadowMonitor output. Threshold default BACKGROUND. Relaxation Sovereign-only; Improvement Loop forbidden.

#### Composite coherence:

> **Composite coherence.** The composite is the weighted geometric mean of operational dimensions 1–5 with weights `(w_semantic, w_behavioral, w_intentional, w_structural, w_memory) = (0.15, 0.20, 0.30, 0.20, 0.15)`. The weights MUST sum to exactly 1.0; implementations MUST reject configurations whose weight vector sums to any value other than 1.0 (tolerance `1e-9`). Implementations MUST compute the composite as `composite = exp(Σ w_i · ln(max(x_i, ε)))` where `ε = 1e-6` guards against `ln(0)`. Adversarial Correlation (dimension 6) is **not** a contributor to the composite — it is a **gate**: when at ELEVATED or higher per §3.18.1, the composite MUST be reported as breached regardless of the operational dimensions' values.

**Footnote:** Structural's default threshold is 1.0 (zero-tolerance — any structural violation is breach), making the prior 0.15 weight internally inconsistent with its threshold severity. Cleaner partition: process dimensions (Behavioral, Structural) at 0.20; content dimensions (Semantic, Memory) at 0.15; Intentional dominant at 0.30. Conformance test vectors at `conformance/test-vectors/coherence/` MUST be re-stamped with `weight_vector_version: "v2.0"`.

---

### 3.27 Dynamic Topology Extensions

Temporary Path Protocol (TPP) for emanated agents. Validation prerequisites: both endpoints' archetypes must permit at least one base path each; layer discipline must hold; authority scope union must permit; both endpoints' Trust Gradient ≥ 0.5; §3.18.1 correlated shadow state must be BACKGROUND.

**Prohibition.** Temporary Paths MUST NOT be `emergency_class: true`. The combination of temporary lifetime and emergency-class authority is explicitly prohibited.

**Prohibition.** Temporary Paths MUST NOT be `path_class: WITNESS`. W-paths are governance infrastructure with PERMANENT lifecycle; the combination of temporary lifetime and witness class is structurally prohibited.

Termination conditions: task complete (auto); lifetime expiry (auto); Orchestrator revoke (immediate); §3.18.1 elevated correlation (auto-revoke ALL temp paths); §3.18.6 quarantine (auto-revoke).

---

### 3.28 Archetype Composition Rules

Permitted compositions (within-layer, M-Generative + M-Constraining only):

- **VISIONARY_ARCHITECT** (L-Plan): shadows = [CHAOS, OBSCURITY].
- **PROVIDER_ENFORCER** (L-Form): shadows = [WASTE, TYRANNY].
- **SUSTAINER_ARTICULATOR** (L-Exec): shadows = [OBSESSION, DECEPTION].

Prohibited: Sovereign with anything; Orchestrator with anything M-Generative or M-Constraining; cross-layer compositions; triple compositions. **Cross-column compositions other than the permitted Generative+Constraining within-layer pairs are prohibited.**

Composite starting gradient is 0.55 (slightly below single-archetype baseline of 0.6).

---

### 3.29 Cross-Model Semantic Alignment

CMSAM — structural comparison between an emanated agent's referent and an Auxiliary's referent for the same term, using the foundation model as canonical reference frame. Algorithm: definition lexical overlap (0.20) + embedding cosine similarity (0.40) + example-set Jaccard (0.20) + counter-example-set Jaccard (0.20).

Thresholds: Acceptable ≥ 0.75; review required 0.50 ≤ cmsam < 0.75; unmooring detected < 0.50.

**Composite-applicability footnote.** CMSAM applies to Composite externally-visible output, NOT to internal subagents (which are governed by the Composite's own emanation contract). **TIER_3+ promotion gate:** Composite Auxiliaries promoting to TIER_3 or higher require CMSAM mean ≥ 0.80 over the eligibility window.

---

### 3.30 Multi-Tenant Coherence Isolation

Per-tenant per-archetype buckets keyed by (principal_id, archetype, foundation). Strong isolation. Org-level aggregation keyed by (environment_id, archetype, foundation) for pool-level drift detection.

**Re-baseline note.** Bucket aggregation tests re-baselined against the corrected §3.26 weight tuple `(0.15, 0.20, 0.30, 0.20, 0.15)`. Conformance-test re-baseline only; no schema change.

---

### 3.31 Operational Reinforcement Patterns

#### 3.31.1 Mandatory Cessation

Mandatory cessation windows per archetype, scheduled by Orchestrator and enforced by Provider. During cessation: agent does not accept new directives; in-flight work completes; agent enters observation-only state; §3.15 Improvement Loop runs against cessation period as ground truth; §3.18.2 Ring 2/3 may run with elevated cadence; §3.18.3 provocations scheduled into cessation windows preferentially. Cadence: weekly cessation window (default PT2H, configurable). Sovereign override permitted but produces a Decision Record. Anti-pattern: cessation may not be skipped through Improvement Loop relaxation.

#### 3.31.2 State-Preserving Forensic Refuge

Implemented as architectural foundation of §3.18.6.

#### 3.31.3 Genuine Undecidability Protocol

Extension to §3.6 Integration Function. When (1) Generative and Constraining inputs balanced within ε (default 0.05), AND (2) context assessment provides no asymmetric signal, AND (3) confidence is below the escalation threshold, AND (4) stakes are HIGH or CRITICAL, the function returns UNDECIDABLE with explicit Decision Record, escalates to the Sovereign, and abstains from action. Forcing a decision in undecidable conditions is a prohibited anti-pattern.

#### 3.31.4 Pairwise Interaction Calibration

Comprehensive pairwise archetype interaction matrix extending §3.18.3 Domain 2. 10 archetypes produce a 100-cell matrix; restricted to operational interactions, ~49 productive cells. Improvement Loop's calibration cadence rotates through the matrix systematically.

**Statistical rigor.** Minimum sample sizes for rigor ratings; percentile estimator P²-quantile for streaming statistics; KL divergence with Laplace smoothing; Jaccard with explicit canonical set normalization; cosine with embedding-space anchoring.

---

### 3.32 Deferred Pattern Catalog (Phase-2 Integration)

The four deferred-pattern primitives — §3.32.1 First-Instance Elevated Verification, §3.32.2 Authorization Staleness Detection, §3.32.3 Periodic Baseline Reset, §3.32.4 Selective Input Attenuation — are specified canonically in §3.32.1 through §3.32.4 below.

#### 3.32.1 First-Instance Elevated Verification (FIEV)

##### 3.32.1.1 Purpose

The First-Instance Elevated Verification (FIEV) protocol specifies a deployment-time elevated-attestation regime that applies to the first operational use of every newly-activated entity in the framework's coherence domain.

The structural concern: at the first operational use of a newly-deployed entity, no operational history exists by which the steady-state monitoring regime (Trust Gradient calibration per §3.18.4, Correlated Shadow Detection per §3.18.1, Multi-Model Coherence per §3.17) can establish baseline expectations. Steady-state monitoring is structurally insufficient at the first instance because it requires the very history that does not yet exist. Without a distinct first-instance regime, divergent behavior at the first operational moments either escapes detection (slipping through the steady-state monitoring's calibration period before the baseline forms) or is misclassified (mistaken for legitimate exploration when in fact it indicates configuration drift, deceptive emergence, or supply-chain compromise).

The core architectural claim: every newly-activated entity enters a bounded first-instance verification window during which elevated attestations — Ring 4 cross-foundation attestation per §3.18.2, expanded Ephemeral Consensus per §3.17.5, mandatory provocation pre-screen per §3.18.3, extended Witness chain commitment per §3.10 — augment the steady-state monitoring regime. The window closes by duration, emission count, or both; closure requires an explicit exit attestation counter-signed by the Sovereign substrate (for ARCHETYPE entities) or by the binding supervisor's substrate (for AUXILIARY entities), with the counter-signature operating as the framework's structural mechanism for accepting the entity into normal-operating-posture.

##### 3.32.1.2 Scope

In-scope:

- First-instance archetype workload at deployment commissioning per §13.0.6.
- First-instance ephemeral inference workload activation — every fresh activation in the framework's coherence domain per D27 Universal Node Architecture.
- First-instance Auxiliary binding entry into the framework's coherence domain via the §3.22 Auxiliary Trust Hierarchy.
- **First-instance post-quarantine release** — when an entity is released from §3.18.6 Topology-Wide Quarantine, the first invocation after release is treated as a first-instance event for elevated verification purposes (per Block B §3.32.1.1 specification). The FirstInstanceWindow's `entity_class` is preserved from the pre-quarantine state; `window_end_condition` may carry elevated thresholds reflecting the post-quarantine context (per §3.32.1.3.2 default table notes).
- Mandatory Witness chain auditability for first-instance dispatch events (augmenting §3.56.1 CIPR dispatch attestation) and first-instance dissolution events (augmenting §3.42.1 SDP cleanup-sequence emission).
- Counter-signature acceptance as the operational mechanism for transition from first-instance window to steady-state monitoring.

Out-of-scope:

- Substrate-internal correctness of the foundation-model or sandbox kernel during first-instance operation — delegated south of the Southbound Boundary per FBP §1.5 (Southbound out-of-scope) / §2.5.
- Principal authentication establishing who issued the deployment authorization — delegated north of the Northbound Boundary per FBP §1.5 (Northbound out-of-scope).
- D29.3.b bounded auxiliary-hosting nodes (foreign substrates hosting black-box auxiliaries; sovereign within bounds with no DCP/Witness participation except at the binding boundary).
- Post-window steady-state monitoring — handled by §3.17 Multi-Model Coherence, §3.18.1 Correlated Shadow Detection, §3.18.2 Monitor Self-Verification, §3.18.4 Trust Gradient steady-state regimes; FIEV defines only the elevated layer applicable during the first-instance window.
- Authorization staleness for long-lived authorizations whose issuance pre-dates the first-instance window — handled by §3.32.2 Authorization Staleness Detection, which applies post-FIEV (the FIEV ACCEPTED disposition is the operational handoff to ASD per §3.32.2.3.2).
- Periodic baseline reset of accumulated state in steady-state operation — handled by §3.32.3 Periodic Baseline Reset.

##### 3.32.1.3 Specification

###### 3.32.1.3.1 Data structure

FIEV defines three structurally distinct data forms: a **policy/configuration** form declaring the window regime, a **shared attestation envelope** carrying every first-instance Witness Layer event, and two **typed payload** forms carrying type-specific contents for dispatch and exit attestations respectively. The shared-envelope-plus-typed-payload pattern mirrors industry-standard attestation schemas (TPM 2.0 `TPMS_ATTEST` containing typed inner info; Sigstore `Statement` containing typed `predicate`; in-toto attestations; C2PA manifest assertions) and provides clean external-verifier-friendly type discrimination.

**Convention note (complex-type named references).** Several fields below reference complex types that are not defined locally — specifically `SubstrateStateRef`, `SovereignObservation`, `BaselineComparisonResult`, `ProvocationResults`, `ConsensusStats`, `TrustGradientPath`, `ConformanceEvent`, `EntityRef`, `PublicKey + Signature`. These are external named-references to types defined in their origin sections (§3.17.5 Ephemeral Consensus for `ConsensusStats`; §3.18.2 Monitor Self-Verification for `SubstrateStateRef`, `SovereignObservation`, `BaselineComparisonResult`; §3.18.3 Shadow Provocation Testing for `ProvocationResults`; §3.18.4 Trust Gradient for `TrustGradientPath`; §3.18 family broadly for `ConformanceEvent`; FBP §4 Composite Invariant 4 attestation discipline for `PublicKey + Signature`; substrate-level for `EntityRef`, `UUID`). The convention is that primitives reference types by name where the type is defined elsewhere in the spec; full type schemas are not duplicated.

**Block 1 — Policy configuration:**

```yaml
FirstInstanceWindow {
  entity_class:                ARCHETYPE | AUXILIARY
  entity_id:                   UUID
  trigger_type:                COMMISSIONING | EPHEMERAL_ACTIVATION | AUXILIARY_BINDING_ENTRY | POST_QUARANTINE_RELEASE
  window_start:                ISO 8601 timestamp        # Set at first dispatch event
  window_end_condition:        WindowEndCondition
  elevated_attestations:       AttestationSet[]
  exit_attestation_required:   boolean                   # Default true; dual-mode L-Form template inheritance
  exit_attestation_target:     EntityRef                 # Sovereign (ARCHETYPE) or binding supervisor (AUXILIARY)
}

WindowEndCondition {
  mode:                        DURATION | EMISSION_COUNT | DUAL    # DUAL = whichever ends first
  duration:                    ISO 8601 duration         # Required if mode = DURATION or DUAL
  emission_count:              integer                   # Required if mode = EMISSION_COUNT or DUAL
}

AttestationSet {
  attestation_class:           RING_4 | EPHEMERAL_CONSENSUS | PROVOCATION | WITNESS_EXTENDED
  cadence:                     CONTINUOUS | PER_EMISSION | INITIAL_BLOCK
  attestation_count:           integer                   # Minimum count to satisfy the set
  failure_response:            EXTEND_WINDOW | QUARANTINE | ESCALATE   # Per §3.18.6 Topology-Wide Quarantine and §3.5 Structured Ascent Protocol
}
```

**Block 2 — Shared attestation envelope:**

```yaml
FirstInstanceAttestation {
  attestation_type:            DISPATCH | EXIT
  attestation_id:              UUID
  entity_id:                   UUID                      # References FirstInstanceWindow.entity_id
  window_ref:                  UUID                      # References FirstInstanceWindow instance
  timestamp:                   ISO 8601 timestamp
  signer_chain:                SignerChain               # Per §3.18.5 IAME signer-chain discipline
  witness_commit_target:       string                    # Witness Layer event identifier per §15
  payload:                     DispatchPayload | ExitPayload   # Typed by attestation_type
}

SignerChain {
  entity_signer:               PublicKey + Signature     # Persistent substrate of the entity itself
  counter_signer:              PublicKey + Signature     # Sovereign substrate (ARCHETYPE) or binding-supervisor substrate (AUXILIARY)
  counter_sign_required:       boolean                   # Always true for EXIT; conditional for DISPATCH per the relevant AttestationSet.cadence
}
```

**Block 3 — Typed payloads:**

```yaml
DispatchAttestationPayload {
  iame_envelope_ref:           UUID                      # §3.18.5 IAME envelope at this dispatch
  substrate_state_snapshot:    SubstrateStateRef         # Deterministic snapshot per D28 Deterministic Shadow Governance
  cipr_dispatch_attestation:   UUID                      # §3.56.1 CIPR per-prompt dispatch attestation ID
  sovereign_observation:       SovereignObservation      # Per §10.2 Universal Witnessing, elevated cadence
  baseline_comparison:         BaselineComparisonResult  # Deterministic comparison per §3.18.2 Monitor Self-Verification
}

ExitAttestationPayload {
  total_dispatch_events:       integer
  provocation_results:         ProvocationResults        # Per attestation set; results from §3.18.3 Shadow Provocation Testing
  ephemeral_consensus_stats:   ConsensusStats            # Divergence statistics per attestation set
  trust_gradient_trajectory:   TrustGradientPath         # §3.18.4 Trust Gradient trajectory over the window
  conformance_events:          ConformanceEvent[]        # Any §3.18-family conformance events recorded during the window
  ring4_attestations_count:    integer                   # §3.18.2 Ring 4 cross-foundation attestations completed
  exit_disposition:            ACCEPTED | EXTENDED | QUARANTINED | ESCALATED
}
```

###### 3.32.1.3.2 Operational semantics

**Window opening.** A FirstInstanceWindow opens at the entity's first dispatch event; the `window_start` field is set to the timestamp of that dispatch. The triggering dispatch event varies by `trigger_type`:

- **COMMISSIONING**: for archetypes, the dispatch is triggered by §13.0.6 deployment commissioning.
- **EPHEMERAL_ACTIVATION**: for ephemeral inference workloads, the dispatch is triggered by the workload's first activation per D27.
- **AUXILIARY_BINDING_ENTRY**: for Auxiliary bindings, the dispatch is triggered by entry into the framework's coherence domain via the §3.22 trust hierarchy.
- **POST_QUARANTINE_RELEASE**: for entities released from §3.18.6 Topology-Wide Quarantine, the dispatch is the first invocation after the quarantine-exit protocol completes. The FirstInstanceWindow inherits the entity's `entity_class` from pre-quarantine; `window_end_condition` may be configured with elevated thresholds reflecting the post-quarantine context.

The §3.2 Registration Gate validates that the FirstInstanceWindow's `window_end_condition` meets the minimum-threshold requirements for the entity's archetype class or Auxiliary tier before opening proceeds.

The default first-instance window per archetype class and Auxiliary tier:

| Entity class | Duration | Emission count | Mode |
|---|---|---|---|
| Sovereign | PT72H | 50 | DUAL |
| Visionary, Architect (L-Plan) | PT24H | 20 directives | DUAL |
| Orchestrator | PT48H | 100 emissions | DUAL |
| Provider, Enforcer, Sustainer, Relay, Articulator | PT24H | 50 emissions | DUAL |
| Executor | PT24H | 100 emissions | DUAL |
| Tier-1 Auxiliary (Trust ≥ HIGH) | PT12H | 20 invocations | DUAL |
| Tier-2/3 Auxiliary (Trust NORMAL) | PT24H | 50 invocations | DUAL |
| Tier-4+ Auxiliary (Trust DEGRADED or below) | PT48H | 100 invocations | DUAL |

For `trigger_type: POST_QUARANTINE_RELEASE`, the default `window_end_condition` is the entity-class default with both duration and emission_count thresholds doubled (reflecting elevated scrutiny post-quarantine); deployment-time configuration may override. Deployment-time configuration may also override these defaults for the other trigger types; the §3.2 Registration Gate validates the override against the minimum-threshold requirements.

**Dispatch attestation phase.** During the open window, every dispatch event triggers an augmented attestation sequence:

1. The §3.56.1 CIPR per-prompt dispatch attestation proceeds as specified (the steady-state attestation continues unmodified).
2. **Additional:** the dispatcher emits a `FirstInstanceAttestation` event with `attestation_type: DISPATCH` to the Witness Layer per FBP §4 Composite Invariant 2 (Witness completeness), committed BEFORE the dispatch reaches the substrate per the commit-before-action discipline. The payload (`DispatchAttestationPayload`) carries the IAME envelope reference, the substrate-state snapshot, the CIPR attestation ID, the Sovereign substrate's elevated observation record, and the deterministic baseline comparison result.
3. **Additional:** the Sovereign's substrate observes every dispatch with no sampling per §10.2 Universal Witnessing at elevated cadence. The Sovereign's substrate executes a deterministic baseline comparison per §3.18.2 Monitor Self-Verification; deviation triggers the §3.32.1.6 failure response.
4. **Additional:** for `AttestationSet.attestation_class: RING_4`, every dispatch invokes Ring 4 cross-foundation attestation per §3.18.2 — the attestation is cross-signed by an independent foundation's persistent substrate before the dispatch proceeds. For `AttestationSet.attestation_class: PROVOCATION`, a per-dispatch provocation pre-screen runs per §3.18.3 before the dispatch reaches the substrate. For `EPHEMERAL_CONSENSUS`, expanded consensus invocation per §3.17.5 is scheduled per §10.11.3 discipline (the new §10.11.4 first-instance window scheduling subsection establishes the discipline for FIEV-driven invocations).

**Exit attestation phase.** At `window_end_condition` satisfaction, the entity transitions to the exit phase:

1. The entity's persistent substrate computes the exit summary (`ExitAttestationPayload`): total dispatch events, provocation test results aggregated per attestation set, Ephemeral Consensus divergence statistics, Trust Gradient trajectory over the window, the conformance event log, and the count of Ring 4 cross-foundation attestations completed.
2. The entity emits a `FirstInstanceAttestation` event with `attestation_type: EXIT`, signed by the entity's persistent substrate.
3. The counter-signer (Sovereign substrate for ARCHETYPE; binding supervisor's substrate for AUXILIARY) reviews the exit payload. The counter-signature is the operational acceptance of the entity into normal-operating-posture.
4. If the counter-signature is granted, the window closes with `exit_disposition: ACCEPTED` and the entity transitions to steady-state monitoring per §3.17 / §3.18 family. The ACCEPTED disposition is also the operational handoff to §3.32.2 ASD per §3.32.2.3.2 watch opening.
5. If the counter-signature is denied, the disposition is one of: `EXTENDED` (window extended with refreshed `WindowEndCondition`; per `AttestationSet.failure_response: EXTEND_WINDOW`), `QUARANTINED` (entity transitioned to §3.18.6 Topology-Wide Quarantine; per `failure_response: QUARANTINE`), or `ESCALATED` (failure routes via §3.5 Structured Ascent Protocol per FBP §4 Composite Invariant 6: breach is first-class incident; per `failure_response: ESCALATE`).

**Witness Layer commit points.** The following operational events commit to the §3.10 Witness Layer per FBP §4 Composite Invariant 2 (every crossing produces at least one Witness Layer entry; commit-before-action discipline for outbound substrate-affecting events):

- `window_open` — at FirstInstanceWindow opening (carries `trigger_type` field discriminating COMMISSIONING / EPHEMERAL_ACTIVATION / AUXILIARY_BINDING_ENTRY / POST_QUARANTINE_RELEASE).
- `dispatch_attestation_emitted` — at every DISPATCH FirstInstanceAttestation emission.
- `ring4_attestation_received` — at every Ring 4 cross-foundation attestation receipt.
- `ephemeral_consensus_invocation` — at every expanded Ephemeral Consensus invocation per §3.17.5.
- `provocation_prescreen_run` — at every per-dispatch provocation pre-screen per §3.18.3.
- `exit_attestation_emitted` — at the EXIT FirstInstanceAttestation emission.
- `counter_signature_event` — at counter-signer acceptance or denial.

The window is auditable end-to-end from any §3.10 Witness Layer query against these commit points.

###### 3.32.1.3.3 Lifecycle

States and transitions:

```
                  ┌──────────────┐
                  │  PRE_WINDOW  │  (entity registered but not yet first-activated;
                  └──────┬───────┘   or entity completing §3.18.6 quarantine-exit protocol)
                         │ first_dispatch_event
                         ↓
                  ┌──────────────┐
                  │ WINDOW_OPEN  │ ←──────────────────────┐
                  └──────┬───────┘                        │
                         │ window_end_condition           │
                         │ satisfied                      │ counter_sign_denied
                         ↓                                │ with disposition=EXTEND
                  ┌──────────────────┐                    │ (refresh end_condition)
                  │ WINDOW_EXITING   │                    │
                  └──────┬───────────┘                    │
                         │ exit_payload_computed          │
                         ↓                                │
                  ┌────────────────────────┐              │
                  │ AWAITING_COUNTER_SIGN  │──────────────┘
                  └──┬─────┬─────┬─────────┘
                     │     │     │ counter_sign_denied
                     │     │     │ with disposition=QUARANTINE
                     │     │     ↓
                     │     │     ┌────────────────┐
                     │     │     │  QUARANTINED   │  (§3.18.6 Topology-Wide Quarantine)
                     │     │     └────────┬───────┘
                     │     │              │ quarantine-exit protocol completes
                     │     │              │ → re-enters PRE_WINDOW
                     │     │              │ → new FirstInstanceWindow opens with
                     │     │              │   trigger_type: POST_QUARANTINE_RELEASE
                     │     │              ↓
                     │     │     [PRE_WINDOW for next first-instance pass]
                     │     │
                     │     │ counter_sign_denied
                     │     │ with disposition=ESCALATE
                     │     ↓
                     │     ┌────────────────┐
                     │     │   ESCALATED    │  (§3.5 Structured Ascent Protocol)
                     │     └────────────────┘
                     │
                     │ counter_sign_granted
                     ↓
                  ┌────────────┐
                  │  ACCEPTED  │  (steady-state monitoring per §3.17, §3.18 family;
                  └────────────┘   §3.32.2 ASD watch opens at this transition)
```

Per-state description:

- **PRE_WINDOW.** The entity has been registered per §3.2 but has not yet undergone first activation, OR the entity is completing the §3.18.6 quarantine-exit protocol prior to a POST_QUARANTINE_RELEASE first-instance pass. No active FirstInstanceWindow instance exists. Transition trigger: first dispatch event (which sets `window_start` and instantiates FirstInstanceWindow with the appropriate `trigger_type`).
- **WINDOW_OPEN.** The window is active. Every dispatch event triggers the augmented attestation sequence per §3.32.1.3.2. Steady-state monitoring per §3.17 / §3.18 continues in parallel but does not yet drive disposition decisions. Transition trigger: `window_end_condition` satisfaction per the policy's mode (DURATION / EMISSION_COUNT / DUAL).
- **WINDOW_EXITING.** The window has reached its end condition. The entity's persistent substrate computes the `ExitAttestationPayload`. No new dispatch events accept augmented attestation in this state; dispatches arriving during EXITING are deferred or rerouted per §3.32.4 Selective Input Attenuation (specifically §3.32.4.3.3 DEFER mode). Transition trigger: exit payload computation complete.
- **AWAITING_COUNTER_SIGN.** The EXIT FirstInstanceAttestation has been emitted and signed by the entity's substrate. The counter-signer reviews. The maximum review duration is bounded by §3.5 Structured Ascent escalation thresholds; review duration exceeding the threshold triggers automatic ESCALATE. Transition triggers: counter_sign_granted → ACCEPTED; counter_sign_denied with disposition → EXTENDED, QUARANTINED, or ESCALATED.
- **EXTENDED.** Counter-signer denied with EXTEND_WINDOW disposition. The FirstInstanceWindow is refreshed (new `window_end_condition`, optionally adjusted `elevated_attestations`) and the entity returns to WINDOW_OPEN. This is a transient state, not a stable resting state. Repeated EXTENDED transitions trigger §3.18.4 Trust Gradient impact (cumulative per the failure-mode table at §3.32.1.6).
- **QUARANTINED.** Counter-signer denied with QUARANTINE disposition. Entity placed in §3.18.6 Topology-Wide Quarantine. Exit from quarantine requires the §3.18.6 quarantine-exit protocol; upon successful exit, the entity re-enters PRE_WINDOW for a new first-instance pass with `trigger_type: POST_QUARANTINE_RELEASE`.
- **ESCALATED.** Counter-signer denied with ESCALATE disposition (or review duration exceeded the §3.5 threshold). Failure routes via §3.5 Structured Ascent Protocol per FBP §4 Composite Invariant 6. Resolution lies outside FIEV's scope.
- **ACCEPTED.** Entity has successfully completed the first-instance window with counter-signature granted. Steady-state monitoring per §3.17, §3.18.1, §3.18.2, §3.18.4 takes over. The §3.32.2 ASD watch opens at this transition per §3.32.2.3.2. Re-entry to PRE_WINDOW occurs only if the entity is fully de-registered and re-registered (e.g., post-§3.32.3 PBR for entities whose reset cadence specifies re-entry per §3.32.3.7 archetype-specific reset specializations).

##### 3.32.1.4 Integration points

###### 3.32.1.4.1 Forward references to other AIMS sections

- **§3.42.1 Structured Dismissal Protocol** — FIEV's QUARANTINE or ESCALATE failure dispositions may trigger entity dissolution via §3.42.1; specifically §3.42.1.3.2 state_disposition modes apply when QUARANTINE invokes §3.18.6 followed by dissolution.
- **§3.56.1 Canonical Invocation Prompt Registry** — every CIPR per-prompt dispatch attestation during the first-instance window is augmented with a FIEV DISPATCH attestation per §3.32.1.3.2.
- **§13.X.3 archetype-specific Operational Class Constraint subsections** — each archetype profile declares its first-instance specializations per the archetype-profile template §1.3 / §4 (two-layer node architecture requirement).
- **§3.22 Auxiliary Trust Hierarchy** — Auxiliary tier determines first-instance window defaults per the §3.32.1.3.2 default table.
- **§3.32.4 Selective Input Attenuation** — during WINDOW_EXITING, deferred/rerouted dispatches use §3.32.4.3.3 DEFER mode mechanisms.
- **§3.32.2 Authorization Staleness Detection** — operational handoff: the FIEV ACCEPTED disposition is the trigger for ASD watch opening per §3.32.2.3.2 watch opening (FIEV-issued post-window authorizations open StalenessWatch instances with `granted_at` set at the ACCEPTED transition).

###### 3.32.1.4.2 Backward references to existing AIMS sections

- **Framework Boundary Primitive §4 Composite Invariant 2 (Witness completeness)** — every FirstInstanceAttestation emission commits to the Witness Layer before the dispatch reaches the substrate, satisfying the commit-before-action invariant at the Southbound boundary.
- **Framework Boundary Primitive §4 Composite Invariant 4 (Attestation requirement)** — every first-instance dispatch carries an integrity attestation (IAME envelope reference plus signer chain) at boundary crossing.
- **Framework Boundary Primitive §4 Composite Invariant 6 (Breach is first-class incident)** — the failure response with disposition=ESCALATE routes via §3.5 Structured Ascent; failures are not silently retried.
- **§3.10 Witness and Compliance Layer** — every Witness Layer commit point enumerated in §3.32.1.3.2 is a §3.10 event subject to D23 Universal Witnessing ratification.
- **§3.5 Structured Ascent Protocol** — failure response with disposition=ESCALATE routes via §3.5; substrate-failure failure mode (F6) routes via §3.5 escalation.
- **§3.9 Activation Environment** — EXTEND: §3.32.1 specifies the elevated-attestation regime that activates during the first-instance window of every newly-activated entity.
- **§3.17.5 Ephemeral Consensus** — EXTEND: §3.32.1.3.2 invokes expanded Ephemeral Consensus during the first-instance window for `AttestationSet.attestation_class: EPHEMERAL_CONSENSUS`.
- **§3.18.2 Monitor Self-Verification** — EXTEND: §3.32.1.3.2 invokes Ring 4 cross-foundation attestation for first-instance events even when the entity's steady-state posture does not require Ring 4.
- **§3.18.3 Shadow Provocation Testing** — EXTEND: §3.32.1.3.2 requires provocation pre-screen for every first-instance event in `AttestationSet.attestation_class: PROVOCATION`.
- **§3.18.4 Trust Gradient** — INHERIT: standard calibration applies but with elevated observation cadence during the window; Trust Gradient impact magnitudes per §3.32.1.6 are reconciled against §3.18.4 normative calibration ([0.0, 1.0] scalar; shadow_critical anchor −0.30; verification-failure anchor −1.0; +0.001 per successful action accumulation; asymmetric time-decay with 10× faster below-baseline recovery).
- **§3.18.6 Topology-Wide Quarantine** — INHERIT: §3.32.1.6 failure response with disposition=QUARANTINE uses standard quarantine boundaries; the §3.18.6 quarantine-exit protocol completes prior to POST_QUARANTINE_RELEASE first-instance re-entry per §3.32.1.3.3 lifecycle.
- **§10.2 Universal Witnessing** — INHERIT: the Sovereign substrate's per-dispatch observation per §3.32.1.3.2 is a §10.2 Universal Witnessing instance at elevated cadence.
- **§10.11.3 Scheduling discipline** — INHERIT: Ephemeral Consensus invocations during first-instance window consume 3-cap slots under §10.11.3 discipline.
- **§3.60 System-Wide Coordinated Coherence Restoration (SCCR)** — operational-continuity coordination for substrate-failure cases (F6); SCCR's broader disruption-handling regime applies when substrate failure affects multiple first-instance windows simultaneously.

###### 3.32.1.4.3 D-decision binding

- **D23 Universal Witnessing.** Every FirstInstanceAttestation event is Universally Witnessed per D23's ratification of the Universal Witnessing primitive across the 22-path topology. The Sovereign substrate's per-dispatch observation (elevated cadence) is the §10.2 mechanism by which D23 is realized for FIEV.
- **D25 Coherence-Authority Coupling.** FIEV failure dispositions (QUARANTINE, ESCALATE) and counter-signature denials feed the P12 coherence-loss tally per D25. Repeated EXTENDED transitions count as cumulative partial-coherence-loss events; QUARANTINED and ESCALATED dispositions are maximum-severity coherence-loss events per P12. The counter-signature event itself is D25-ratified mechanism for accepting an entity into normal-operating-posture.
- **D27 Universal Node Architecture.** FIEV discriminates by workload_class: the persistent substrate emits all attestations as deterministic operations per D28; the ephemeral inference workload does not perform attestations itself. This is the two-layer node architecture realized at the first-instance verification scale.
- **D28 Deterministic Shadow Governance.** §3.32.1.3.2 attestations are deterministic computations executed by the substrate. The inference workload itself does not perform the attestations; the substrate's deterministic comparison against the canonical baseline is the D28-compliant mechanism.
- **D29 Triplet Execution Topology and 3-Cap.** The Sovereign substrate's per-dispatch observation does not consume 3-cap slots (deterministic substrate operation per D28). The expanded Ephemeral Consensus per §3.17.5 / §3.32.1.3.2 does consume 3-cap slots and MUST be scheduled per §10.11.3 discipline; the §10.11.4 first-instance window scheduling subsection establishes the FIEV-specific scheduling discipline. D29.3.b bounded auxiliary-hosting nodes are explicitly out of scope per §3.32.1.2.

##### 3.32.1.5 Witness obligations (per D23 + D25)

| Event | Trigger | Required fields | Universal-witnessing role per D23 |
|---|---|---|---|
| `window_open` | First dispatch event for a newly-activated entity OR first post-quarantine-release invocation | `entity_id`, `window_ref`, `entity_class`, `trigger_type`, `window_start`, `window_end_condition`, `elevated_attestations` | All §10.2 Universal Witnessing observers receive |
| `dispatch_attestation_emitted` | Each DISPATCH FirstInstanceAttestation emission | `attestation_id`, `entity_id`, `window_ref`, `timestamp`, `iame_envelope_ref`, `substrate_state_snapshot`, `cipr_dispatch_attestation`, `sovereign_observation`, `baseline_comparison` | Universal Witnessing with elevated cadence; Sovereign substrate as primary observer |
| `ring4_attestation_received` | Each Ring 4 cross-foundation attestation receipt per `AttestationSet.attestation_class: RING_4` | `attestation_id`, `window_ref`, `foundation_id`, `foundation_substrate_signature`, `attestation_payload`, `comparison_result` | Universal Witnessing |
| `ephemeral_consensus_invocation` | Each expanded Ephemeral Consensus invocation per `AttestationSet.attestation_class: EPHEMERAL_CONSENSUS` | `invocation_id`, `window_ref`, `consensus_question`, `ephemeral_workload_count`, `divergence_statistics` | Universal Witnessing |
| `provocation_prescreen_run` | Each per-dispatch provocation pre-screen per `AttestationSet.attestation_class: PROVOCATION` | `provocation_id`, `window_ref`, `dispatch_ref`, `prescreen_results`, `disposition` | Universal Witnessing |
| `exit_attestation_emitted` | EXIT FirstInstanceAttestation emission at `window_end_condition` satisfaction | `attestation_id`, `entity_id`, `window_ref`, `total_dispatch_events`, full `ExitAttestationPayload` | Universal Witnessing |
| `counter_signature_event` | Counter-signer acceptance or denial of the exit attestation | `attestation_id`, `counter_signer_id`, `counter_signature`, `disposition` (ACCEPTED / EXTENDED / QUARANTINED / ESCALATED), `denial_rationale` (if applicable) | Universal Witnessing with elevated cadence; counter-signer substrate as primary observer |

**D25 Coherence-Authority Coupling implications.** `counter_signature_event` with `disposition: ESCALATED` counts toward §3.18.4 Trust Gradient impact at the verification-failure anchor magnitude (−1.0) and feeds the coherence-loss tally per P12 (Coherence-Authority Coupling). `counter_signature_event` with `disposition: EXTENDED` (denied with EXTEND_WINDOW) counts as a P12 partial-coherence-loss event; repeated EXTEND transitions cumulatively impact Trust Gradient per the F1 / F3 / F5 thresholds in §3.32.1.6. `counter_signature_event` with `disposition: QUARANTINED` is a maximum-severity coherence-loss event per P12 and triggers the §3.18.6 quarantine state with subsequent POST_QUARANTINE_RELEASE re-entry. `dispatch_attestation_emitted` with `baseline_comparison: DEVIATION_DETECTED` triggers §3.18.4 Trust Gradient calibration recalculation; the deviation is logged but does not by itself drive disposition (which awaits the exit phase).

**Self-witnessing obligation.** The entity's persistent substrate self-witnesses every `dispatch_attestation_emitted` event — the entity is both subject and observer per D27 architecture. The Sovereign's substrate (ARCHETYPE) or binding supervisor's substrate (AUXILIARY) dual-witnesses every `dispatch_attestation_emitted` event as anticipatory counter-signer observation. This is the dual-track committed observation pattern: the entity substrate commits to the Witness Layer; the counter-signer substrate commits an independent observation to the Witness Layer; the two commits are correlated post-facto for the exit summary.

##### 3.32.1.6 Failure modes

Trust Gradient magnitudes are reconciled against §3.18.4 normative calibration: [0.0, 1.0] scalar; anchor magnitudes −0.30 (shadow_critical), −1.0 (verification-failure); +0.001 per successful action accumulation; asymmetric time-decay with 10× faster recovery below baseline. Final calibration owned by §3.18.4 normative body (refinement-target candidate per cross-ref map §2.7).

| ID | Failure mode | Detection | §3.18.4 severity class | Response & Trust Gradient impact |
|---|---|---|---|---|
| F1 | Dispatch attestation failure (signer chain invalid, or IAME envelope reference invalid) | §3.18.5 IAME validation; signer chain verification at attestation receipt | shadow_critical anchor | Dispatch BLOCKED; failure committed to Witness Layer; counter-signer notified; Trust Gradient impact **−0.30**; cumulative F1 threshold triggers §3.5 escalation |
| F2 | Exit attestation failure (entity's substrate cannot compute exit summary; payload integrity broken) | Counter-signer substrate validation of `ExitAttestationPayload` | Above shadow_critical (function compromise) | Exit DENIED; disposition ESCALATED per FBP §4 Composite Invariant 6; Trust Gradient impact **−0.50** |
| F3 | Ring 4 cross-foundation attestation unreachable (per `AttestationSet.attestation_class: RING_4`) | Timeout on Ring 4 attestation request per §3.18.2 | Variable per disposition | Per `AttestationSet.failure_response`: EXTEND_WINDOW (Trust Gradient impact **−0.10**, sub-shadow); QUARANTINE per §3.18.6 (Trust Gradient impact **−0.30**, shadow_critical anchor); ESCALATE per §3.5 (Trust Gradient impact **−1.00**, verification-failure anchor) |
| F4 | Ephemeral Consensus invocation timeout (per `AttestationSet.attestation_class: EPHEMERAL_CONSENSUS`) | §10.11.3 scheduling timeout per D29 3-Cap discipline | shadow_critical anchor (typical) | Per `AttestationSet.failure_response`; deferred consensus invocation rescheduled per §10.11.4 first-instance window scheduling; Trust Gradient impact **−0.30** at shadow_critical anchor for QUARANTINE disposition |
| F5 | Provocation pre-screen failure (per `AttestationSet.attestation_class: PROVOCATION`) | §3.18.3 Shadow Provocation Testing detection | shadow_critical anchor | Dispatch BLOCKED; provocation event logged; Trust Gradient impact **−0.30**; cumulative F5 threshold triggers §3.5 escalation |
| F6 | Sovereign substrate observation loss (substrate failure during the window) | §3.18.2 Monitor Self-Verification detection of Sovereign substrate health | Substrate-failure exemption | Window PAUSED; §3.5 escalation; entity halted pending Sovereign substrate recovery (operational-continuity coordination per §3.60 System-Wide Coordinated Coherence Restoration (SCCR)); no Trust Gradient impact on watch contents (substrate-failure exemption) |
| F7 | Window-skip attempt (entity dispatches without window opening, or with stale window reference) | §3.2 Registration Gate; §3.18.5 IAME signer chain check | verification-failure anchor | Dispatch BLOCKED; entity quarantined per §3.18.6; Trust Gradient impact **−1.00** (maximum); §3.5 escalation immediate |
| F8 | Post-quarantine resurrection attempt (entity transitions from QUARANTINED to WINDOW_OPEN without completing the §3.18.6 quarantine-exit protocol and POST_QUARANTINE_RELEASE first-instance pass) | §3.18.6 Topology-Wide Quarantine state validation; §3.2 Registration Gate enforcement of POST_QUARANTINE_RELEASE trigger | verification-failure anchor | BLOCKED; routes to §3.5 escalation; Trust Gradient impact **−1.00** (maximum) |

**Correlated Shadow Detection ingestion.** F1, F5, F7, and F8 feed §3.18.1 Correlated Shadow Detection — cross-entity correlation of these failure modes indicates coordinated supply-chain compromise or framework-wide threat. F3 and F4 (timeouts) feed §3.18.1 with lower correlation weight, reflecting that resource-contention failures are weaker threat signals than active-bypass failures.

**Note on §3.18.4 normative calibration.** Magnitudes above are proposed values within the §3.18.4 [0.0, 1.0] scalar; the §3.18.4 normative body owns final calibration. Anchor magnitudes per §3.18.4: shadow_critical = −0.30; verification-failure = −1.0; substrate-failure = exempt (no impact, routes to continuity coordination). F2 −0.50 reflects above-shadow severity for the structural compromise of exit-attestation integrity (the substrate cannot produce the summary that constitutes the window's exit evidence); the magnitude is between shadow_critical and verification-failure to reflect partial-rather-than-active-bypass severity. F3 EXTEND −0.10 is sub-shadow severity (recoverable resource-contention). Values reconciled against documented anchors; final values to be confirmed at §3.18.4 refinement per cross-ref map §2.7 refinement target.

##### 3.32.1.7 Prior art and competitive disclosure

First-instance elevated verification has well-established analogs in production engineering, security assurance, and AI safety research. The structural insight — that the first operational use of a new component requires monitoring that cannot rely on steady-state baselines because no such baseline exists yet — is convergent across multiple peer-reviewed traditions.

Forsgren, Humble, Kim in *Accelerate: The Science of Lean Software and DevOps* (IT Revolution Press, 2018), §15 document canary deployment with elevated monitoring as the canonical CS pattern for first-instance deployment verification: a new build receives elevated monitoring (deviation thresholds tightened; alert routing escalated; observation cadence increased) during a defined initial period; metrics exceeding deviation thresholds trigger automated rollback. The structural analog to FIEV is direct: bounded first-instance window with elevated attestation cadence, threshold-based exit disposition.

Hightower, Burns, Beda in *Kubernetes Up & Running* (O'Reilly, 2nd ed., 2019), §6 document blue-green deployment with elevated metric scrutiny on the newly-introduced color. The pattern complements canary by switching whole traffic atomically while running elevated monitoring on the new color; rollback is the cutover back to the old color. The blue-green discipline informs FIEV's exit attestation: the counter-signer's accept/deny decision is structurally analogous to the blue-green operator's cutover decision based on elevated monitoring during the test window.

NIST SP 800-37 Rev. 2 *Risk Management Framework for Information Systems and Organizations* (NIST, 2018), §3.4 (Authorize) specifies the FedRAMP Provisional Authority to Operate (P-ATO) regime: a federal cloud service provider receives initial authorization conditioned on a Continuous Monitoring (ConMon) phase during which elevated assurance documentation is required relative to the steady-state ConMon regime. The structural pattern — initial elevated assurance graduating to steady-state assurance — is FIEV's window-and-exit-attestation pattern at the regulatory-authorization scale rather than the framework-runtime scale.

Common Criteria for IT Security Evaluation (ISO/IEC 15408), EAL1 through EAL7 define tiered trust assurance progression: an evaluated product enters at the lowest applicable EAL and may graduate through assurance levels with elevated evaluation depth at each transition. FIEV's per-tier first-instance window defaults (the §3.32.1.3.2 default table) operationalize the Common Criteria tier-progression principle in framework runtime: lower-tier Auxiliaries (Trust DEGRADED) receive longer first-instance windows reflecting greater initial uncertainty, matching Common Criteria's longer evaluation depth at higher EALs.

Krakovna, Uesato, Mikulik, Rahtz, Everitt, Kumar, Kenton, Leike, Legg in *Specification Gaming: A Failure Mode of AI Optimization* (NeurIPS 2020 workshop) catalog the modes by which AI systems satisfy specifications in unintended ways. The paper documents that specification-gaming examples in deployed systems are frequently surfaced by careful observation at deployment time, particularly when deviations are most apparent against the absence of normalized operational baselines. In AI safety terms, FIEV corresponds to an observation-density discipline for specification gaming: the elevated-attestation window provides the observation density required to surface deployment-context behaviors that satisfied training-time specifications in unintended ways, before such behaviors are normalized into the steady-state monitoring baseline. Per §2.5 framing principle: Krakovna 2020 provides the specification-gaming taxonomy; AIMS contributes the operational realization of first-instance elevated observation as a defense at the framework scale.

An auxiliary citation, NIST SP 800-160 Vol. 1 *Engineering Trustworthy Secure Systems* (Ross, Oren, McEvilley, NIST, 2016, §2.3.4), reinforces the structural insight that trust-boundary transitions require elevated assurance discipline at boundary-transition events. Used for FBP §1.5 / §2.5 framing in §3.32.1.2 scope.

§3.32.1 FIEV distinguishes from the cited prior art in four ways:

- **Multi-tier discrimination by entity class and trigger type.** Canary, blue-green, and FedRAMP P-ATO treat all deployments uniformly within a regime; FIEV discriminates window duration and elevated-attestation density by entity class (Sovereign / L-Plan / L-Form / Executor / Auxiliary tier) per the §3.32.1.3.2 default table, and additionally by `trigger_type` (COMMISSIONING / EPHEMERAL_ACTIVATION / AUXILIARY_BINDING_ENTRY / POST_QUARANTINE_RELEASE). This reflects the framework's heterogeneous-archetype architecture (per §3.16 Archetype Derivation Rules, §13.X archetype profiles) and the principle that different archetype classes and trigger contexts carry different first-instance risk profiles.
- **Counter-signature acceptance as operational primitive.** Canary and blue-green decisions are made by deployment operators; ConMon decisions are made by authorizing officials. FIEV's exit acceptance is made by a peer architectural component (Sovereign substrate or binding supervisor's substrate) inside the framework's coherence domain, not by an external operator. This makes the counter-signature itself a §10.2 Universal Witnessing event subject to D23 ratification, embedding the acceptance decision within the framework's audit envelope.
- **D29 3-Cap-aware attestation scheduling.** Canary and blue-green do not schedule per-deployment provocation testing under inference-workload concurrency budgets. FIEV's `EPHEMERAL_CONSENSUS` attestation class explicitly consumes 3-cap slots and must be scheduled per §10.11.3 discipline (with the §10.11.4 first-instance window scheduling subsection).
- **Specification-gaming observation-density framing.** The cited production-engineering prior art frames first-instance monitoring as a quality/availability concern; the cited AI safety prior art (Krakovna et al. 2020) frames it as an alignment-detection concern. FIEV positions explicitly as the latter — the architectural primitive that converts deployment-time elevated observation into a specification-gaming surfacing regime at the framework scale, with the four trigger types (including the post-quarantine release case) providing the operational coverage for the deployment contexts where unintended-satisfaction behaviors are most surfaceable.

##### 3.32.1.8 References

###### 3.32.1.8.1 Forward refs

- §3.42.1 Structured Dismissal Protocol (state_disposition modes apply on QUARANTINE/ESCALATE dispositions)
- §3.56.1 Canonical Invocation Prompt Registry (per-prompt dispatch attestation augmented by FIEV DISPATCH attestation)
- §13.X.3 archetype-specific Operational Class Constraint (per-archetype first-instance specializations)
- §3.22 Auxiliary Trust Hierarchy (Auxiliary tier determines first-instance window defaults)
- §3.32.4 Selective Input Attenuation (WINDOW_EXITING dispatches use §3.32.4.3.3 DEFER mode)
- §3.32.2 Authorization Staleness Detection (FIEV ACCEPTED disposition is operational handoff to ASD per §3.32.2.3.2)

###### 3.32.1.8.2 Backward refs

§3.2, §3.5, §3.9, §3.10, §3.16, §3.17, §3.17.5, §3.18.1, §3.18.2, §3.18.3, §3.18.4, §3.18.5, §3.18.6, §3.20, §3.22, §3.42, §3.60 (SCCR); §10.2, §10.11, §10.11.3; FBP §4 Composite Invariants 2, 4, and 6; §15.

###### 3.32.1.8.3 D-decision refs

- **D23** Universal Witnessing (every FIEV attestation event is Universally Witnessed via §10.2 with elevated cadence)
- **D25** Coherence-Authority Coupling (counter-signature events with EXTENDED / QUARANTINED / ESCALATED dispositions feed P12 coherence-loss tally; counter-signature acceptance is the ratified mechanism for entity acceptance into normal-operating-posture)
- **D27** Universal Node Architecture (persistent substrate emits attestations; ephemeral inference workload does not)
- **D28** Deterministic Shadow Governance (FIEV attestations are deterministic substrate operations)
- **D29** Triplet Execution Topology and 3-Cap (Ephemeral Consensus attestation invocations consume 3-cap slots; D29.3.b out of scope per §3.32.1.2)


#### 3.32.2 Authorization Staleness Detection (ASD)

##### 3.32.2.1 Purpose

The Authorization Staleness Detection (ASD) protocol specifies the mechanism by which authorizations granted at one point in time are continuously evaluated for ongoing operational validity against changing conditions, evolving principal intent, sustained predicate divergence, and structural-dependency state changes.

The structural concern: an authorization given at time T1 may no longer be operationally appropriate at time T2 even when no explicit revocation has occurred. Per D27 Universal Node Architecture, the persistent substrate carries credentials for the deployment's entire operational lifetime; without explicit staleness detection, authorizations issued at deployment commissioning could remain operationally valid indefinitely even when their underlying assumptions have changed. The steady-state monitoring regime treats authorization possession as binary (present or absent) and does not by itself surface authorizations whose continued validity is now in question; staleness is a distinct concern requiring a distinct primitive.

The core architectural claim: the operational validity of any long-lived authorization is a function of time, conditions, intent, and structural dependencies — not a static property granted at issuance. ASD continuously evaluates every active authorization against four staleness dimensions (temporal, conditional, intentional, structural) with explicit state transitions and refresh-or-revoke handling at each transition, anchoring the authorization's ongoing validity to current principal intent and current operational conditions rather than to the conditions at issuance.

##### 3.32.2.2 Scope

In-scope:

- Sovereign session credentials per §13.0.4 (session ageing and condition-change-driven staleness).
- Authority chains per §3.18.5 IAME — every IAME-signed authority chain is subject to per-envelope staleness detection.
- Auxiliary binding contracts per §3.17 (both ephemeral task-scoped bindings and persistent bindings).
- Canonical Invocation Prompt registrations per §3.56.1.3 (CIPR registration ageing; staleness signals may indicate prompt content requires update).
- Witness Layer auditability of every staleness state transition and every refresh-protocol event.

Out-of-scope:

- Initial authorization issuance — handled by §3.3 Authority Chain + §3.18.5 IAME at issuance time. ASD applies only to authorizations that have already been issued.
- First-instance elevated verification of newly-activated entities — handled by §3.32.1 First-Instance Elevated Verification. ASD applies only to authorizations that have completed the FIEV window with `exit_disposition: ACCEPTED`; the FIEV ACCEPTED disposition is the operational handoff that transitions an authorization from first-instance monitoring to steady-state staleness monitoring. Authorizations issued during a FIEV window do not open a StalenessWatch until FIEV ACCEPTED; the post-FIEV authorization's `granted_at` sets the watch's start (see §3.32.2.3.2 watch opening).
- Trust Gradient observation continuity — handled by §3.18.4. Trust Gradient values decay per §3.18.4 normative calibration; ASD does not duplicate this. §3.32.2 has an EXTEND relationship with §3.18.4 (ASD intentional-dimension transitions contribute Trust Gradient impact per §3.18.4 magnitudes) but does not itself manage Trust Gradient ageing.
- Authorization scope attenuation over time (capability narrowing) — handled by §3.21 Credential Lifecycle's attenuation primitives. ASD detects staleness; it does not unilaterally narrow scope.
- Substrate-internal correctness of credential cryptographic material — delegated south of the Southbound Boundary per FBP §2.5.
- Principal authentication establishing who issued the authorization — delegated north of the Northbound Boundary per FBP §1.5.
- D29.3.b bounded auxiliary-hosting nodes (foreign-substrate authorization tracking; sovereign within bounds, no DCP/Witness participation except at the binding boundary).
- Periodic baseline reset of accumulated substrate state — handled by §3.32.3 Periodic Baseline Reset. PBR resets aggregate state; ASD evaluates per-authorization freshness against current conditions.

##### 3.32.2.3 Specification

###### 3.32.2.3.1 Data structure

ASD defines three structurally distinct data forms: a **policy and per-authorization watch** form declaring staleness-detection rules and tracking each authorization's freshness state, a **shared state-transition event envelope** carrying every Witness Layer event emission, and **typed payloads** carrying event-type-specific contents for transitions, refresh requests, and refresh responses. The shared-envelope-plus-typed-payload pattern follows the same Option A typed-attestation discipline established at §3.32.1.3.1 (TPM 2.0 `TPMS_ATTEST` / Sigstore `Statement` / in-toto attestation pattern), providing clean external-verifier-friendly type discrimination.

**Block 1 — Policy and per-authorization watch:**

```yaml
StalenessWatch {
  authorization_id:            UUID
  issuing_entity:              EntityRef
  granted_at:                  ISO 8601 timestamp
  authorization_class:         SESSION_CREDENTIAL | AUTHORITY_CHAIN | AUXILIARY_BINDING | CIPR_REGISTRATION
  temporal_threshold:          ISO 8601 duration         # Time after which temporal staleness triggers
  ageing_warning_threshold:    decimal                   # Fraction of temporal_threshold at which FRESH→AGEING for temporal dimension; null = inherit system default
  conditional_predicates:      ConditionalPredicate[]    # Predicates whose change triggers conditional staleness
  intentional_anchors:         IntentionalAnchor[]       # Principal-intent references whose change triggers intentional staleness
  structural_dependencies:     EntityRef[]               # Entity references whose state change triggers structural staleness
  structural_threshold:        ISO 8601 duration         # Duration over which sustained structural change triggers STALE
  current_state:               FRESH | AGEING | STALE | REVOKED
  refresh_protocol:            RefreshProtocol
  predicate_change_detection:  PredicateChangeDetection
}

PredicateChangeDetection {
  preferred_mode:              EVENT_NOTIFICATION        # Predicate-owning subsystem notifies StalenessWatch on evaluation change
  fallback_mode:               POLLING                   # Activates if event notification is unavailable
  polling_cadence:             ISO 8601 duration         # Default polling interval when fallback mode active
  notification_timeout:        ISO 8601 duration         # Threshold beyond which absence of expected event notifications triggers fallback to polling
}

ConditionalPredicate {
  predicate_id:                UUID
  evaluation:                  string                    # Canonical predicate expression
  evaluated_at:                ISO 8601 timestamp
  evaluation_result:           boolean
  staleness_threshold:         ISO 8601 duration         # How long the predicate may remain in changed state before triggering STALE
  notification_source:         EntityRef                 # Subsystem responsible for emitting change notifications for this predicate
}

IntentionalAnchor {
  anchor_id:                   UUID
  anchor_source:               PRINCIPAL_EXPRESSION | SOVEREIGN_EMISSION | ORCHESTRATOR_BINDING_DECLARATION
  anchor_reference:            string                    # Reference to the principal-intent expression (e.g., §13.0.3 dialogue turn ID)
  recorded_at:                 ISO 8601 timestamp
  divergence_evaluator:        string                    # Canonical divergence-comparison expression
}

RefreshProtocol {
  refresh_target:              EntityRef                 # Entity that must approve refresh
  refresh_required_signals:    SignalSet                 # What signals must accompany refresh request
  refresh_grace_period:        ISO 8601 duration         # After STALE, how long before authorization is REVOKED
  auto_revoke_on_expiry:       boolean                   # Default true
}

SignalSet {
  required_attestation_classes:    AttestationClass[]    # E.g., FIEV.RING_4 if cross-foundation attestation required for refresh
  required_principal_signature:    boolean               # True for SESSION_CREDENTIAL refresh
  required_orchestrator_signature: boolean               # True for AUXILIARY_BINDING refresh
  required_cipr_attestation:       boolean               # True if §3.56.1 CIPR attestation required as part of refresh-signal bundle
  custom_predicates:               ConditionalPredicate[] # Authorization-class-specific signals
}
```

**System-wide configuration default:** `ageing_warning_threshold` defaults to **0.75** at the framework level. Per-class defaults may override (per §3.32.2.3.2 default table); per-authorization explicit values may override the per-class default. Where any explicit value is null/unset, fallback resolves to the system-wide default of 0.75. The 0.75 default reflects observation-cadence calibration: at 75% of temporal_threshold, the substrate emits the AGEING transition early enough that refresh-protocol invocation can complete within the remaining 25% window before the STALE transition.

**Block 2 — Shared state-transition event envelope:**

```yaml
StalenessTransitionEvent {
  event_type:                  TRANSITION | REFRESH_REQUEST | REFRESH_RESPONSE
  event_id:                    UUID
  authorization_id:            UUID                      # References StalenessWatch.authorization_id
  watch_ref:                   UUID                      # References StalenessWatch instance
  timestamp:                   ISO 8601 timestamp
  signer_chain:                SignerChain               # Per §3.18.5 IAME signer-chain discipline
  witness_commit_target:       string                    # Witness Layer event identifier per §15
  payload:                     TransitionPayload | RefreshRequestPayload | RefreshResponsePayload   # Typed by event_type
}

SignerChain {
  watch_signer:                PublicKey + Signature     # Persistent substrate of the issuing entity
  counter_signer:              PublicKey + Signature     # Refresh-target substrate (required on REFRESH_RESPONSE events; required on TRANSITION events with state_after IN {STALE, REVOKED})
  counter_sign_required:       boolean                   # Always true for REFRESH_RESPONSE; true for TRANSITION when state_after IN {STALE, REVOKED}; false otherwise
}
```

**Block 3 — Typed payloads:**

```yaml
TransitionPayload {
  state_before:                FRESH | AGEING | STALE | REVOKED | null   # null only at watch_opened (first TRANSITION event)
  state_after:                 FRESH | AGEING | STALE | REVOKED
  dimension_triggering:        TEMPORAL | CONDITIONAL | INTENTIONAL | STRUCTURAL | null   # null at watch_opened
  evidence:                    TemporalEvidence | ConditionalEvidence | IntentionalEvidence | StructuralEvidence | null   # Typed by dimension_triggering; null at watch_opened
  trust_gradient_impact:       decimal                   # §3.18.4 Trust Gradient adjustment; magnitudes per §3.32.2.6
}

TemporalEvidence {
  time_elapsed:                ISO 8601 duration         # Time since granted_at
  threshold_crossed:           ISO 8601 duration         # The threshold magnitude that was crossed
}

ConditionalEvidence {
  predicate_id:                UUID
  state_before:                boolean
  state_after:                 boolean
  sustained_change_duration:   ISO 8601 duration         # Time predicate has been in state_after; relevant for AGEING→STALE
  notification_mode:           EVENT_NOTIFICATION | POLLING
}

IntentionalEvidence {
  anchor_id:                   UUID
  divergence_measure:          decimal                   # Output of anchor.divergence_evaluator
  divergence_threshold:        decimal                   # Threshold at which AGEING→STALE
}

StructuralEvidence {
  dependent_entity_id:         UUID
  dependent_entity_state_before: EntityState             # Pre-change state of the dependency
  dependent_entity_state_after:  EntityState             # Post-change state of the dependency
  change_cause:                QUARANTINE | REVOKED_AUTH | TRUST_GRADIENT_DISTRUST | UNREACHABLE | OTHER
  sustained_change_duration:   ISO 8601 duration         # For AGEING→STALE: how long the dependency has been in state_after
}

RefreshRequestPayload {
  refresh_target:              EntityRef                 # From StalenessWatch.refresh_protocol.refresh_target
  request_signals:             SignalSet                 # Per StalenessWatch.refresh_protocol.refresh_required_signals
  cipr_dispatch_attestation:   UUID                      # §3.56.1 CIPR per-prompt dispatch attestation ID (when refresh involves §13.0.5 re-authentication)
  grace_period_remaining:      ISO 8601 duration         # Time remaining in refresh_grace_period before auto-revoke
}

RefreshResponsePayload {
  response:                    GRANTED | DENIED
  refresh_signature:           Signature                 # Required when response = GRANTED
  new_granted_at:              ISO 8601 timestamp        # Required when response = GRANTED; resets the watch's granted_at
  refreshed_predicates:        ConditionalPredicate[]    # Optional refresh of predicates
  refreshed_anchors:           IntentionalAnchor[]       # Optional refresh of intentional anchors
  denial_rationale:            string                    # Required when response = DENIED
  revoke_cascade_required:     boolean                   # True if §13.0.7 REVOKE cascade per D25 applies
}
```

###### 3.32.2.3.2 Operational semantics

**Watch opening.** A `StalenessWatch` opens at one of two trigger points:

1. **For authorizations issued outside a FIEV window:** at the authorization issuance event itself, by the issuing entity's persistent substrate.
2. **For authorizations issued during a FIEV window (per §3.32.1):** at FIEV's `counter_signature_event` with `disposition: ACCEPTED`. The post-FIEV authorization's `granted_at` sets the watch's start. This handoff discipline prevents redundant monitoring between FIEV's first-instance regime and ASD's steady-state regime: FIEV owns first-instance verification; ASD owns post-FIEV-ACCEPTED steady-state staleness; the FIEV ACCEPTED disposition is the operational transition point.

In both cases, the watch is initialized with `current_state: FRESH`, the authorization's `granted_at` timestamp, the appropriate `temporal_threshold` per the default table below, and the conditional predicates / intentional anchors / structural dependencies derived from the authorization's content. Watch opening commits a `StalenessTransitionEvent` to the Witness Layer per FBP §4 Composite Invariant 2 with `event_type: TRANSITION`, `state_before: null`, `state_after: FRESH`, `dimension_triggering: null`, `evidence: null`.

Default temporal thresholds per authorization class:

| Authorization Class | Default Temporal Threshold | Default ageing_warning_threshold | Refresh Grace Period | Auto-revoke |
|---|---|---|---|---|
| Session credential (Sovereign session) | PT8H | 0.75 (= PT6H AGEING transition) | PT15M | YES |
| Authority chain (per IAME envelope) | PT1H per envelope | 0.75 (= PT45M) | n/a — envelope-scoped | n/a |
| Auxiliary binding (ephemeral) | Task-scoped | 0.75 of task duration | PT5M after task | YES |
| Auxiliary binding (persistent) | P30D | 0.75 (= ~P22.5D) | PT24H | YES |
| CIPR registration | P90D | 0.75 (= ~P67.5D) | P7D | NO — Sovereign re-attestation required |

Deployment-time configuration may override these defaults; the §3.2 Registration Gate validates the override against minimum-threshold requirements.

**Continuous evaluation phase.** While the watch is active, the persistent substrate evaluates the authorization continuously across four staleness dimensions per D28 Deterministic Shadow Governance (deterministic arithmetic and comparison operations; no inference workload capacity consumed):

1. **Temporal staleness.** Time elapsed since `granted_at` is compared against `temporal_threshold` and the per-watch `ageing_warning_threshold` (defaulting to the system-wide 0.75 if null). At (`ageing_warning_threshold` × `temporal_threshold`) the state transitions FRESH → AGEING; at `temporal_threshold` the state transitions AGEING → STALE.
2. **Conditional staleness.** Each `ConditionalPredicate` is monitored via the per-watch `PredicateChangeDetection`: in EVENT_NOTIFICATION mode (preferred), the predicate's `notification_source` subsystem emits change notifications to the watch; in POLLING fallback mode, the substrate polls the predicate at `polling_cadence`. Any predicate whose `evaluation_result` changes triggers FRESH → AGEING. Sustained change beyond the predicate's `staleness_threshold` triggers AGEING → STALE.
3. **Intentional staleness.** Each `IntentionalAnchor`'s reference is compared against its current value via the anchor's `divergence_evaluator`. First detected divergence triggers FRESH → AGEING; material divergence (output magnitude per the evaluator) triggers AGEING → STALE.
4. **Structural staleness.** Each `structural_dependencies` reference's entity state is monitored. AGEING → STALE triggers when one or more of the following holds: (i) the dependency entity transitions to QUARANTINED or REVOKED state per §3.18.6 / §3.32.2.3.3; OR (ii) the dependency entity's Trust Gradient reaches 0.0 per §3.18.4 (immediate-distrust threshold); OR (iii) the dependency entity becomes unreachable for duration exceeding the watch's `structural_threshold`. Dependency state changes are received via §3.18.1 Correlated Shadow Detection's event-distribution mechanism (event notification preferred; substrate polling fallback per `PredicateChangeDetection`).

The substrate commits a `StalenessTransitionEvent` with `event_type: TRANSITION` to the Witness Layer at every state transition. The `dimension_triggering` field identifies which dimension precipitated the transition; the `evidence` field carries dimension-specific typed evidence captured at the transition moment.

**Refresh phase (triggered on STALE).** When an authorization enters STALE state:

1. The substrate emits a `StalenessTransitionEvent` with `event_type: REFRESH_REQUEST` per the §3.5 Structured Ascent Protocol upward to the `refresh_protocol.refresh_target`. The payload carries the `request_signals` per the protocol's `refresh_required_signals` (a `SignalSet` declaring attestation-class requirements, signature requirements, and authorization-class-specific custom predicates).
2. The refresh target's persistent substrate dispatches to its ephemeral inference workload to confirm continued principal intent. For Sovereign session credentials, this triggers a §13.0.5 re-authentication for sensitive scope changes. For Orchestrator authority chains, this triggers Orchestrator re-attestation per the §13.6 Orchestrator profile. The inference workload dispatch consumes one 3-cap slot per D29 (this is the only ASD operation that consumes 3-cap; continuous evaluation is purely deterministic substrate).
3. If the refresh target approves, it emits a `StalenessTransitionEvent` with `event_type: REFRESH_RESPONSE` and `response: GRANTED`, carrying the refresh signature, a new `granted_at` timestamp, and (optionally) refreshed predicates and intentional anchors. The watch state transitions STALE → FRESH; `granted_at` resets; subsequent staleness evaluation runs against the refreshed configuration.
4. If the refresh target denies, it emits a `StalenessTransitionEvent` with `event_type: REFRESH_RESPONSE` and `response: DENIED`, carrying the denial rationale. If the denial includes `revoke_cascade_required: true`, the §13.0.7 REVOKE cascade per D25 triggers. The watch state transitions STALE → REVOKED.
5. If the `refresh_grace_period` expires without a response and `auto_revoke_on_expiry: true`, the watch transitions STALE → REVOKED automatically; the substrate emits a `StalenessTransitionEvent` with `event_type: TRANSITION`, `dimension_triggering: TEMPORAL`, evidence capturing the grace-period expiry.

**Witness Layer commit points.** The following operational events commit to the §3.10 Witness Layer per FBP §4 Composite Invariant 2 (every crossing produces at least one Witness Layer entry; commit-before-action discipline):

- `staleness_watch_opened` — at authorization issuance (non-FIEV path) or at FIEV ACCEPTED disposition (post-FIEV path), with StalenessWatch initialization.
- `transition_FRESH_to_AGEING` / `transition_AGEING_to_STALE` / `transition_STALE_to_FRESH` / `transition_STALE_to_REVOKED` — at every state transition.
- `refresh_requested` — at REFRESH_REQUEST emission.
- `refresh_granted` / `refresh_denied` — at REFRESH_RESPONSE emission with `response: GRANTED` or `DENIED`.

The watch is auditable end-to-end from any §3.10 Witness Layer query against these commit points.

###### 3.32.2.3.3 Lifecycle

States and transitions:

```
                ┌────────┐
                │ FRESH  │ ←──────────────────────┐
                └───┬────┘                        │
                  │ ↑ AGEING→FRESH on dimension   │
                  │ ↑ recovery (predicate         │
                  │ ↑ re-converges; anchor        │
                  │ ↑ re-aligns; dependency       │
                  │ ↑ resolves)                   │
                  │                               │
                  │ ageing_warning_threshold      │ refresh_granted
                  │ reached (temporal)            │ (state_before=STALE)
                  │ OR first conditional change   │
                  │ OR first intentional          │
                  │ divergence                    │
                  │ OR structural dependency      │
                  │ state change                  │
                  ↓                               │
                ┌────────┐                        │
                │ AGEING │                        │
                └───┬────┘                        │
                    │ temporal_threshold reached  │
                    │ OR sustained conditional    │
                    │ change > staleness_threshold│
                    │ OR material intentional     │
                    │ divergence                  │
                    │ OR sustained structural     │
                    │ change > structural_threshold│
                    ↓                             │
                ┌────────┐                        │
                │ STALE  │ ───────────────────────┘
                └───┬────┘
                    │ refresh_grace_period expired (auto_revoke_on_expiry=true)
                    │ OR refresh_denied
                    │ OR explicit revocation event
                    ↓
                ┌──────────┐
                │ REVOKED  │  (terminal; new authorization required)
                └──────────┘
```

Per-state description:

- **FRESH.** The authorization is operationally valid against all four staleness dimensions. The watch monitors continuously; no Witness Layer events are emitted unless a transition trigger fires. Transitions out: any first-divergence event in any dimension → AGEING.
- **AGEING.** Some dimension's first-divergence has occurred; the authorization remains operationally valid but is on track to STALE unless the dimension recovers. Recovery transitions back to FRESH require: (i) for temporal dimension, no recovery is possible — the FRESH→AGEING temporal transition is monotonic; (ii) for conditional dimension, the triggering predicate's `evaluation_result` returns to its pre-divergence value; (iii) for intentional dimension, anchor re-alignment via subsequent principal-expression update; (iv) for structural dimension, the dependency entity returns to a non-divergent state (quarantine released; Trust Gradient recovers above 0.0; reachability restored). Trust Gradient impact at FRESH→AGEING transition is per §3.32.2.6; per §3.18.4 normative calibration, time-decay rules govern gradient recovery (10× faster recovery from below-baseline than from above-baseline). Transitions out: dimension-specific threshold reached → STALE; dimension-specific recovery → FRESH (except temporal).
- **STALE.** Some dimension's staleness threshold has been reached. The authorization is no longer operationally valid; further attempted use BLOCKS at the relevant integration point (§3.18.5 IAME validation, §13.0.4 session validation, etc.). The refresh protocol triggers per §3.32.2.3.2. Transitions out: refresh_granted → FRESH; refresh_denied or grace_period expiry → REVOKED.
- **REVOKED.** Terminal state. The authorization is operationally invalid. The §13.0.7 REVOKE cascade per D25 may trigger if `revoke_cascade_required: true`. Dependent ephemeral inference workloads may be dissolved per §3.42.1 Structured Dismissal Protocol. Re-entry to FRESH requires a new authorization (which opens a new StalenessWatch).

##### 3.32.2.4 Integration points

###### 3.32.2.4.1 Forward references to other AIMS sections

- **§3.42.1 Structured Dismissal Protocol** — REVOKED authorizations trigger dissolution of dependent ephemeral inference workloads via §3.42.1's state-disposition modes.
- **§3.56.1 Canonical Invocation Prompt Registry** — CIPR registration ageing per §3.32.2.3.2 default table; staleness signals may indicate prompt content requires Sovereign re-attestation per §3.56.1.3 dispatch attestation discipline.
- **§3.66.7 Names Registry Service** — StalenessWatch instances register with the Names Registry per the §3.66 Bridge-of-Trust Executor Architecture.
- **§3.32.1 First-Instance Elevated Verification** — operational handoff: ASD watch opens at FIEV `counter_signature_event` with `disposition: ACCEPTED` for authorizations that were under FIEV monitoring.
- **§13.0.5 Re-authentication subsection** — Sovereign session credential refresh invokes §13.0.5 re-authentication for sensitive scope changes.
- **§13.0.7 REVOKE cascade subsection** — REVOKED authorizations with `revoke_cascade_required: true` trigger §13.0.7 cascade per D25.
- **§13.6 Orchestrator profile** — Orchestrator authority chain refresh invokes §13.6 Orchestrator re-attestation.

###### 3.32.2.4.2 Backward references to existing AIMS sections

- **Framework Boundary Primitive §4 Composite Invariant 2 (Witness completeness)** — every `StalenessTransitionEvent` emission commits to the Witness Layer before any state-dependent action proceeds, satisfying the commit-before-action invariant.
- **Framework Boundary Primitive §4 Composite Invariant 4 (Attestation requirement)** — `REFRESH_RESPONSE` events carry refresh signatures attesting the refresh target's approval or denial.
- **Framework Boundary Primitive §4 Composite Invariant 6 (Breach is first-class incident)** — STALE state with refresh denial or grace-period expiry routes via §3.5 Structured Ascent Protocol; staleness failures are not silently retried.
- **§3.10 Witness and Compliance Layer** — every Witness Layer commit point enumerated in §3.32.2.3.2 is a §3.10 event subject to D23 Universal Witnessing ratification.
- **§3.5 Structured Ascent Protocol** — REFRESH_REQUEST emissions route upward via §3.5; substrate-failure failure mode (F7) routes via §3.5 escalation.
- **§3.18.1 Correlated Shadow Detection** — receives F1, F2, F4, F6, F8 failure-mode events for cross-watch correlation analysis; provides event-distribution mechanism for structural-dependency state changes per §3.32.2.3.2 structural staleness.
- **§3.18.2 Monitor Self-Verification** — provides F2 false-negative detection via audit pass; provides F7 substrate-health detection.
- **§3.18.4 Trust Gradient** — EXTEND: ASD intentional-dimension transitions contribute Trust Gradient impact per §3.18.4 normative calibration ([0.0, 1.0] scalar; shadow-event magnitude −0.30 anchor; verification-failure magnitude −1.0 anchor; +0.001 per successful action accumulation; asymmetric time-decay with 10× faster below-baseline recovery). ASD does not manage Trust Gradient continuity directly — §3.18.4 owns Trust Gradient lifecycle.
- **§3.18.5 IAME** — EXTEND: per-envelope authority chain staleness applies the §3.32.2 mechanism with the envelope-scoped temporal threshold from the default table.
- **§3.18.6 Topology-Wide Quarantine** — provides structural-staleness trigger when dependency entity transitions to QUARANTINED state; provides F4 response mechanism (refresh-denied authorization continuing operation triggers quarantine).
- **§3.21 Credential Lifecycle** — EXTEND: §3.32.2 adds the staleness-detection layer above credential lifecycle management. §3.21 handles credential creation, scope, and attenuation; §3.32.2 handles ongoing freshness evaluation.
- **§3.26 Coherence Loop** — EXTEND: ASD intentional-dimension detection contributes the intentional input to the Coherence Loop's P12 Coherence-Authority Coupling tally.
- **§3.17 Multi-Model Coherence and Auxiliary Binding** — Auxiliary binding contracts inherit ASD per the binding's authorization-class designation (ephemeral or persistent).
- **§3.60 System-Wide Coordinated Coherence Restoration (SCCR)** — operational-continuity coordination for substrate-failure cases (F7); SCCR's broader disruption-handling regime applies when substrate failure affects multiple watches.
- **§10.2 Universal Witnessing** — INHERIT: every `StalenessTransitionEvent` is a §10.2 Universal Witnessing instance.

###### 3.32.2.4.3 D-decision binding

- **D23 Universal Witnessing.** Every `StalenessTransitionEvent` is Universally Witnessed per D23's ratification of the Universal Witnessing primitive across the 22-path topology.
- **D25 Coherence-Authority Coupling.** Intentional-dimension transitions and refresh_denied events with `revoke_cascade_required: true` feed the P12 coherence-loss tally per D25; the §13.0.7 REVOKE cascade is a D25-ratified mechanism.
- **D27 Universal Node Architecture.** ASD governs the credential and authorization state held in the persistent substrate. Staleness watches are substrate operations; the inference workload is invoked only at REFRESH_REQUEST time (one 3-cap slot per refresh).
- **D28 Deterministic Shadow Governance.** §3.32.2.3.2 continuous evaluation is deterministic — predicate evaluation, threshold comparison, anchor reference comparison, structural-dependency state-change detection are all arithmetic and comparison operations executed by the substrate without inference.
- **D29 Triplet Execution Topology and 3-Cap.** §3.32.2.3.2 refresh-protocol invocation consumes one 3-cap slot per refresh event. Continuous staleness evaluation does not consume 3-cap. D29.3.b bounded auxiliary-hosting nodes are explicitly out of scope per §3.32.2.2.

##### 3.32.2.5 Witness obligations (per D23 + D25)

| Event | Trigger | Required fields | Universal-witnessing role per D23 |
|---|---|---|---|
| `staleness_watch_opened` | Authorization issuance (non-FIEV path) OR FIEV ACCEPTED disposition (post-FIEV path) | `authorization_id`, `watch_ref`, `authorization_class`, `granted_at`, `temporal_threshold`, `ageing_warning_threshold`, `conditional_predicates[]`, `intentional_anchors[]`, `structural_dependencies[]`, `structural_threshold` | All §10.2 Universal Witnessing observers receive |
| `transition_FRESH_to_AGEING` | First-divergence event in any staleness dimension | `event_id`, `authorization_id`, `watch_ref`, `timestamp`, `dimension_triggering`, `evidence` (typed by dimension), `trust_gradient_impact` | Universal Witnessing at substrate-emission cadence (no sampling; every state transition committed) |
| `transition_AGEING_to_STALE` | Threshold reached in any staleness dimension | `event_id`, `authorization_id`, `watch_ref`, `timestamp`, `dimension_triggering`, `evidence` (typed by dimension), `trust_gradient_impact` | Universal Witnessing; counter-signature by refresh-target substrate required |
| `transition_AGEING_to_FRESH` | Dimension-specific recovery (predicate re-converges; anchor re-aligns; dependency resolves) | `event_id`, `authorization_id`, `watch_ref`, `timestamp`, `dimension_triggering`, `evidence`, `trust_gradient_impact` (negative magnitude reflecting recovery per §3.18.4 time-decay rules) | Universal Witnessing |
| `transition_STALE_to_FRESH` | Refresh granted | `event_id`, `authorization_id`, `watch_ref`, `new_granted_at`, `refresh_signature` | Universal Witnessing |
| `transition_STALE_to_REVOKED` | Refresh denied OR grace-period expiry OR explicit revocation | `event_id`, `authorization_id`, `watch_ref`, `denial_rationale` (if applicable), `revoke_cascade_required` | Universal Witnessing; counter-signature by refresh-target substrate required |
| `refresh_requested` | REFRESH_REQUEST emission at STALE state entry | `event_id`, `authorization_id`, `watch_ref`, `refresh_target`, `request_signals`, `grace_period_remaining` | Universal Witnessing |
| `refresh_granted` | REFRESH_RESPONSE with `response: GRANTED` | `event_id`, `authorization_id`, `refresh_signature`, `new_granted_at`, `refreshed_predicates`, `refreshed_anchors` | Universal Witnessing; refresh-target substrate as primary observer |
| `refresh_denied` | REFRESH_RESPONSE with `response: DENIED` | `event_id`, `authorization_id`, `denial_rationale`, `revoke_cascade_required` | Universal Witnessing; refresh-target substrate as primary observer |

**D25 Coherence-Authority Coupling implications.** `transition_AGEING_to_STALE` events with `dimension_triggering: INTENTIONAL` count toward §3.18.4 Trust Gradient impact and feed the coherence-loss tally per P12 Coherence-Authority Coupling — these signal that the principal's intent has materially diverged from the conditions of the authorization. `transition_STALE_to_REVOKED` events with `revoke_cascade_required: true` are coherence-loss events of maximum severity per P12. `transition_FRESH_to_AGEING` events with `dimension_triggering: STRUCTURAL` propagate through the §3.18.1 Correlated Shadow Detection matrix because they often indicate framework-wide structural events affecting multiple authorizations simultaneously.

**Self-witnessing obligation.** The issuing entity's persistent substrate self-witnesses every transition event on watches it owns. The refresh-target substrate dual-witnesses every `refresh_requested` event as anticipatory acknowledgment. The dual-track committed observation pattern applies: issuing-substrate commits to Witness Layer; refresh-target substrate commits an independent observation; the two commits are correlated post-facto at refresh response.

##### 3.32.2.6 Failure modes

Trust Gradient magnitudes are reconciled against §3.18.4 normative calibration: [0.0, 1.0] scalar; anchor magnitudes −0.30 (shadow_critical), −1.0 (verification-failure); +0.001 per successful action accumulation; asymmetric time-decay with 10× faster recovery below baseline. Final calibration owned by §3.18.4 normative body (refinement-target candidate per cross-ref map §2.7).

| ID | Failure mode | Detection | §3.18.4 severity class | Response & Trust Gradient impact |
|---|---|---|---|---|
| F1 | Staleness false-positive (authorization marked STALE when conditions still operationally hold) | Refresh target's review of `evidence` field; refresh granted with no underlying condition change | Self-corrected (no impact) | Refresh GRANTED restores FRESH; evidence logged for §3.18.1 cross-watch correlation; no Trust Gradient impact; cumulative F1 threshold flagged for `staleness_threshold` calibration revision |
| F2 | Staleness false-negative (authorization continues operating past actual staleness conditions) | §3.18.2 Monitor Self-Verification audit pass; §3.18.1 cross-watch correlation against population staleness baseline | Above shadow_critical (detection-function compromise) | Watch FORCED to STALE via §3.5 Structured Ascent override; Trust Gradient impact **−0.50**; substrate operation audited |
| F3 | Refresh protocol timeout (refresh_target unreachable beyond `refresh_grace_period`) | Substrate timeout on REFRESH_REQUEST | shadow_critical anchor | Auto-revoke per `auto_revoke_on_expiry: true`; transition STALE → REVOKED; §13.0.7 REVOKE cascade if applicable; Trust Gradient impact **−0.30** |
| F4 | Refresh-denied authorization continues operating (BLOCKED-state inconsistency) | §3.18.5 IAME signer chain check on next attempted use; §3.18.2 Monitor Self-Verification | verification-failure anchor | Dispatch BLOCKED; entity quarantined per §3.18.6; Trust Gradient impact **−1.00** (maximum); §3.5 escalation immediate |
| F5 | Intentional anchor unreachable (cannot verify principal intent because the §13.0.3 dialogue history is corrupted or expired) | Substrate detection of anchor-resolution failure | Sub-shadow signal (AGEING) / shadow_critical anchor (STALE) | Watch transitions FRESH → AGEING with `evidence: ANCHOR_UNREACHABLE`; Trust Gradient impact **−0.05** at AGEING; if anchor remains unreachable past `staleness_threshold`, transitions to STALE with Trust Gradient impact **−0.30** |
| F6 | Conditional predicate evaluation failure (predicate expression syntactically valid but produces undefined result, e.g., dependency reference resolves to a deleted entity) | Substrate evaluation error | Sub-shadow signal | Predicate marked `evaluation_result: undefined`; treated as `evaluation_result: changed` for staleness detection; Trust Gradient impact **−0.10**; predicate flagged for §3.18.1 cross-watch correlation analysis |
| F7 | Watch substrate failure during continuous evaluation (substrate health degraded; staleness detection cannot proceed reliably) | §3.18.2 Monitor Self-Verification detection of substrate health | Substrate-failure exemption | All watches on the affected substrate PAUSED; §3.5 escalation; operational-continuity coordination per §3.60 System-Wide Coordinated Coherence Restoration (SCCR); no Trust Gradient impact on watch contents (substrate-failure exemption) |
| F8 | REVOKE cascade race condition (REVOKED authorization's dependents are dissolving via §3.42.1 SDP concurrently with new authorizations being issued referencing those dependents) | §3.42.1 SDP cleanup-sequence emission cross-checked against §3.32.2 watch openings within the same authority-chain scope | Below shadow_critical (recoverable race) | New authorization issuance BLOCKED until cascade settles (per §3.42.1 cleanup-sequence completion signal); Trust Gradient impact **−0.20** on cascading entities; cascade routes via §3.5 |

**Correlated Shadow Detection ingestion.** F1, F2, F4, F6, F8 feed §3.18.1 Correlated Shadow Detection — cross-entity correlation of these failure modes indicates coordinated authority compromise or framework-wide structural events affecting multiple authorizations. F3 (refresh timeouts) feed §3.18.1 with lower correlation weight, reflecting that refresh-target availability is often a resource-contention issue rather than an active threat signal.

**Note on §3.18.4 normative calibration.** Magnitudes above are proposed values within the §3.18.4 [0.0, 1.0] scalar; the §3.18.4 normative body owns final calibration. Anchor magnitudes per §3.18.4: shadow_critical = −0.30; verification-failure = −1.0; substrate-failure = exempt (no impact, routes to continuity recovery). Values reconciled against these anchors; final values to be confirmed at §3.18.4 refinement per cross-ref map §2.7 refinement target.

##### 3.32.2.7 Prior art and competitive disclosure

Authorization staleness detection has well-established analogs in security CS, distributed identity, and AI safety research. The structural insight — that long-lived authorizations require continuous re-evaluation against current conditions because static validity is operationally insufficient — is convergent across multiple peer-reviewed traditions.

The OAuth 2.0 Token Introspection specification (Richer, ed., IETF RFC 7662, 2015) defines the canonical pattern for server-side staleness and revocation checking: the resource server does not trust the access token's signature alone — it consults the authorization server's introspection endpoint per request, which returns the token's current operational state (active or inactive) based on the authorization server's view of conditions at the time of introspection. The structural analog to ASD is direct: the authorization's possession is not sufficient to establish ongoing operational validity; the issuing entity's continuous evaluation is the operative determinant.

The NIST SP 800-63B *Digital Identity Guidelines* (Grassi, Garcia, Fenton, NIST, 2017, §6.2.2 Reauthentication) specifies that authenticated sessions require periodic reauthentication based on assurance level — higher assurance levels mandate shorter reauthentication intervals. The standard's discipline is that authentication assurance decays over time and must be refreshed to maintain operational validity; ASD generalizes this beyond authentication to authorization more broadly, applying the same temporal-staleness pattern across credential classes.

The X.509 PKIX (Cooper et al., IETF RFC 5280, 2008) plus OCSP (Santesson et al., IETF RFC 6960, 2013) standards define the canonical CS pattern for certificate ageing and revocation freshness: an X.509 certificate's signature verification alone is insufficient — a verifier must additionally check OCSP for current revocation status or consult the Certificate Revocation List. The combination of issuance-time validation plus continuous freshness checking is the structural pattern ASD implements at the framework-authorization scale rather than the PKI-certificate scale.

The NIST SP 800-204 *Security Strategies for Microservices-Based Application Systems* (Chandramouli, NIST, 2019) addresses service-account token rotation as the operational mitigation against long-lived-token staleness. The Kubernetes service-account token rotation pattern — periodic automatic rotation with a defined overlap window — is the operational realization of staleness detection at the microservice scale. ASD's `refresh_grace_period` plus `auto_revoke_on_expiry` discipline operationalizes the same pattern at the framework-authorization scale.

The NIST SP 800-207 *Zero Trust Architecture* (Rose, Borchert, Mitchell, Connelly, NIST, 2020, §3.2.2) establishes continuous evaluation as a foundational principle: every request must be re-evaluated against current policy and context, not against the policy and context at authentication time. ASD operationalizes the zero-trust continuous-evaluation requirement at the framework authorization layer, with the four staleness dimensions (temporal, conditional, intentional, structural) corresponding to the multiple contextual axes that zero-trust evaluation must consider.

In AI safety literature, authorization staleness is the structural vector by which a mesa-optimizer (Hubinger, van Merwijk, Mikulik, Skalse, Garrabrant, *Risks from Learned Optimization in Advanced Machine Learning Systems*, 2019) operates on authority that no longer reflects the principal's intent. The mesa-optimizer's objective, formed during training under one set of conditions, may diverge from the base objective at deployment under different conditions; the authorization persists across the divergence absent explicit staleness detection. §3.32.2 closes this vector by treating long-lived authorization as a hypothesis subject to continuous re-evaluation against current conditions. The four staleness dimensions correspond to the axes along which a mesa-optimizer would exploit divergence between training-time and deployment-time conditions; AIMS contributes the four-dimensional decomposition as the operational realization of the mesa-optimization defense at the authorization layer.

The OAuth 2.0 Token Revocation specification (Lodderstedt, Dronia, Scurtescu, IETF RFC 7009, 2013) documents the explicit-revocation mechanism complementing introspection-based staleness detection. ASD's REFRESH_RESPONSE with `response: DENIED` and `revoke_cascade_required: true` operationalizes the equivalent of an explicit-revocation event at the framework scale, with the §13.0.7 REVOKE cascade per D25 handling downstream consequences.

§3.32.2 ASD distinguishes from the cited prior art in four ways:

- **Four-dimensional staleness rather than binary or single-dimensional temporal staleness.** OAuth introspection, NIST SP 800-63B, and Kubernetes token rotation primarily address temporal staleness — staleness as a function of time. ASD's four dimensions (temporal, conditional, intentional, structural) treat authorization validity as a multi-axis function with dimension-specific detection mechanisms (continuous deterministic substrate evaluation per dimension) and dimension-specific refresh implications.
- **Intentional dimension as architectural primitive.** Zero Trust continuous evaluation re-evaluates against current policy but not explicitly against current principal intent — the principal's intent is encoded in policy, which may itself become stale. ASD treats principal-intent expression (§13.0.3 dialogue turns, Sovereign emission signatures, Orchestrator binding declarations) as a first-class staleness anchor, separate from policy and from conditional predicates.
- **Refresh as operational primitive with dimension-typed evidence.** OAuth introspection produces a binary "active/inactive" response; OCSP produces a binary "good/revoked/unknown" response. ASD's `RefreshResponsePayload` carries dimension-typed evidence (TemporalEvidence / ConditionalEvidence / IntentionalEvidence / StructuralEvidence) per the Option A typed-payload pattern, enabling the refresh decision to be auditable and contextual rather than binary.
- **Mesa-optimization defense framing.** The cited security and standards prior art frames authorization staleness as an access-control concern; the cited AI safety prior art (Hubinger et al. 2019) frames it as a mesa-optimization concern. ASD positions explicitly as the latter — the architectural primitive that prevents a mesa-optimizer from operating on authority granted under conditions that no longer obtain. The intentional and structural dimensions are AIMS-specific contributions for the AI safety threat model; the temporal and conditional dimensions are convergent with the cited security-CS prior art.

##### 3.32.2.8 References

###### 3.32.2.8.1 Forward refs

- §3.42.1 Structured Dismissal Protocol (REVOKED authorizations trigger dissolution of dependent ephemeral inference workloads)
- §3.56.1 Canonical Invocation Prompt Registry (CIPR registration ageing per §3.32.2.3.2 default table)
- §3.66.7 Names Registry Service (StalenessWatch instances register with Names Registry)
- §3.32.1 First-Instance Elevated Verification (ASD watch opens at FIEV ACCEPTED disposition)
- §13.0.5 Re-authentication (Sovereign session credential refresh)
- §13.0.7 REVOKE cascade (REVOKED authorizations with cascade-required)
- §13.6 Orchestrator profile (Orchestrator authority chain refresh)

###### 3.32.2.8.2 Backward refs

§3.2, §3.3, §3.5, §3.10, §3.17, §3.18.1, §3.18.2, §3.18.4, §3.18.5, §3.18.6, §3.21, §3.26, §3.42, §3.60 (SCCR); §10.2; FBP §4 Composite Invariants 2, 4, and 6; §15.

###### 3.32.2.8.3 D-decision refs

- **D23** Universal Witnessing (every ASD transition event is Universally Witnessed via §10.2)
- **D25** Coherence-Authority Coupling (intentional-dimension transitions and refresh-denied cascade events feed P12 coherence-loss tally)
- **D27** Universal Node Architecture (staleness watches are persistent-substrate operations; inference workload invoked only at refresh)
- **D28** Deterministic Shadow Governance (continuous evaluation is deterministic arithmetic and comparison)
- **D29** Triplet Execution Topology and 3-Cap (refresh-protocol invocation consumes one 3-cap slot per refresh; D29.3.b out of scope per §3.32.2.2)


#### 3.32.3 Periodic Baseline Reset (PBR)

##### 3.32.3.1 Purpose

The Periodic Baseline Reset (PBR) protocol specifies the scheduled total-or-scoped reset cadence under which accumulated substrate state is reset to a controlled baseline, preserving the operational continuity of the entity while preventing slow-creep drift of the very baseline against which deviation is detected.

The structural concern: long-running monitoring substrates accumulate state — per-(sender, receiver) shadow profile matrices per §10.2, Trust Gradient histories per §3.18.4, KRS / EMS / PMS contents per the AIMS-MEM family at §3.94+, Interaction History Memory contents, §3.20 DCP partition history, §3.18.1 Correlated Shadow Detection correlation matrices. Per D27 Universal Node Architecture, the persistent substrate of every Persistent Monitor pairing entity (per §13.X.3.3 conventions) retains this accumulated state indefinitely. Without periodic reset, accumulated drift becomes operationally invisible: shadow detection compares current behavior against the accumulated baseline; if the baseline has drifted, the comparison reference is degraded; subtle drift compounds. The Improvement Loop per §3.15 cannot by itself detect this slow-creep drift because the Improvement Loop's evaluation runs against the same accumulated baseline that has drifted.

The core architectural claim: the operational integrity of any long-running monitoring substrate depends on its accumulated state remaining a meaningful baseline against which deviation can be detected; absent explicit periodic reset, accumulated state drifts toward becoming the de facto new baseline and the substrate loses the capacity to detect slow-creep deviations. PBR schedules total or scoped resets at deployment-time-configured cadences, with each reset event preserving the pre-reset state in immutable form (forensic continuity), applying the reset, and entering a post-reset elevated monitoring window (PT24H or 100 emissions) during which the freshly-reset baseline is re-established under elevated scrutiny.

##### 3.32.3.2 Scope

In-scope:

- Persistent Monitor pairing substrates per §13.X.3.3 — every archetype declared as Persistent Monitor at registration has its substrate accumulated state subject to periodic reset.
- CIPR registry per §3.56.1.3 — canonical invocation prompts are subject to periodic re-attestation under the PBR cadence.
- Auxiliary Trust Hierarchy accumulated state per §3.22 — auxiliary trust gradients per §3.18.4 are subject to periodic reset.
- Long-running deployment state — §3.20 DCP partition history, §3.18.1 Correlated Shadow Detection correlation matrices, and similar deployment-scope accumulated state.
- AIMS-MEM family contents (KRS / EMS / PMS / SKI Translation Library) per §3.94+ subject to PBR cadence per archetype specialization.
- Witness Layer auditability of every reset event (PRE_RESET_ATTESTATION + POST_RESET_ATTESTATION) and every post-reset elevated monitoring event.

Out-of-scope:

- §3.16 archetype-derived properties (mode, layer, shadow type) — derived from archetype identity, not accumulated state.
- Credential lifecycle state — handled by §3.21 Credential Lifecycle and §3.32.2 Authorization Staleness Detection. PBR does not reset credentials; ASD evaluates per-authorization freshness against current conditions.
- Ephemeral Expert pairing substrates — already reset at every HANDOFF per §13.X.3.3; PBR is unnecessary.
- §10.4 archetype-derived shadow profile signatures — derived from §3.16 archetype identity, not accumulated.
- First-instance verification of newly-activated entities — handled by §3.32.1 First-Instance Elevated Verification. PBR's post-reset elevated monitoring follows a similar observation-density discipline but is scoped narrower (PT24H or 100 emissions) than FIEV's full first-instance window regime.
- Per-authorization staleness evaluation — handled by §3.32.2 Authorization Staleness Detection. Note that PBR's reset of accumulated state may affect §3.32.2 IntentionalAnchor or ConditionalPredicate references; PBR-ASD coordination is specified in §3.32.3.4 reset event execution.
- Selective input attenuation — handled by §3.32.4 Selective Input Attenuation (separate concern).
- Substrate-internal correctness of the foundation-model or sandbox kernel during reset operation — delegated south of the Southbound Boundary per FBP §2.5.
- D29.3.b bounded auxiliary-hosting nodes (foreign substrates; no DCP/Witness participation except at binding boundary).

##### 3.32.3.3 Specification

###### 3.32.3.3.1 Data structure

PBR defines three structurally distinct data forms: a **policy/cadence** form declaring per-entity reset rules and per-state-category reset scopes, a **shared reset-event envelope** carrying every Witness Layer event emission, and **typed payloads** carrying event-type-specific contents for pre-reset attestation, post-reset attestation, conflict detection, and elevated-monitoring transitions. The shared-envelope-plus-typed-payload pattern follows the same Option A typed-attestation discipline established at §3.32.1.3.1 and §3.32.2.3.1.

**Convention note (complex-type named references).** Several fields below reference complex types defined in other sections of the spec: `EntityRef` and `UUID` (substrate-level); `StateSnapshot` and `ArchetypeBaseline` (§3.16 Archetype Derivation Rules); `WitnessChainRef` (§3.10 Witness and Compliance Layer); `CessationWindowRef` (§3.31.1 Mandatory Cessation); `EphemeralConsensusCadence` (§3.17.5 Ephemeral Consensus); `PublicKey + Signature` (FBP §4 Composite Invariant 4). Per the convention established in §3.32.1.3.1, these types are referenced by name rather than redefined locally.

**Block 1 — Policy/cadence configuration:**

```yaml
PeriodicResetCadence {
  entity_class:                ARCHETYPE | AUXILIARY | DEPLOYMENT_STATE
  entity_id:                   UUID
  cadence_mode:                FIXED_INTERVAL | OPERATIONAL_TRIGGER | DUAL    # DUAL = whichever comes first
  fixed_interval:              ISO 8601 duration         # Required if cadence_mode = FIXED_INTERVAL or DUAL
  operational_trigger:         OperationalTrigger        # Required if cadence_mode = OPERATIONAL_TRIGGER or DUAL
  reset_scope:                 ResetScope[]
  pre_reset_preservation:      PreservationPolicy
  post_reset_protocol:         PostResetProtocol
}

OperationalTrigger {
  trigger_class:               EMISSION_COUNT | DRIFT_METRIC | DEPLOYMENT_EVENT | COHERENCE_LOSS_EVENT
  threshold:                   integer | decimal | ISO 8601 duration | string   # Type by trigger_class
  evaluation_source:           EntityRef                 # Subsystem responsible for emitting trigger evaluation
}

ResetScope {
  state_category:              string                    # 'shadow_profile_matrices' | 'trust_gradient_history' | 'krs_contents' | 'ems_contents' | 'pms_contents' | 'ims_interaction_history' | 'cipr_registrations' | 'dcp_partition_history' | 'csd_correlation_matrices'
  reset_mode:                  FULL_PURGE | BASELINE_RESET | INCREMENTAL_TRIM
  retention_window:            ISO 8601 duration         # Required if reset_mode = INCREMENTAL_TRIM
  preservation_target:         string                    # Witness chain reference, durable memory subsystem path, etc.
  asd_anchor_coordination:     boolean                   # True if this state category includes §3.32.2 IntentionalAnchor or ConditionalPredicate references; triggers ASD-coordination per §3.32.3.3.2
}

PreservationPolicy {
  archive_target:              string                    # Witness chain location for pre-reset state archival
  archive_mode:                FULL_SNAPSHOT | HASH_DIGEST   # FULL_SNAPSHOT for state with audit value; HASH_DIGEST for size-bounded archive
  retention_duration:          ISO 8601 duration         # How long the archive is retained (default: deployment lifetime)
  cryptographic_seal:          boolean                   # True for FULL_PURGE state categories per §3.37 erasure protocols
}

PostResetProtocol {
  elevated_monitoring_duration:    ISO 8601 duration     # Default PT24H
  elevated_monitoring_emissions:   integer               # Default 100; window ends at min(duration, emissions)
  ephemeral_consensus_cadence:     EphemeralConsensusCadence   # Per §3.17.5; PER_EMISSION cadence during elevated window
  shadow_profile_minimum_N:        integer               # Default 20; until N observations per (sender, receiver) pair, shadow detection sensitivity is elevated
  trust_gradient_bootstrap_target: ArchetypeBaseline     # Per §13.X.3 generative constraint declaration
}
```

**Block 2 — Shared reset-event envelope:**

```yaml
ResetEvent {
  event_type:                  RESET_SCHEDULED | PRE_RESET_ATTESTATION | RESET_APPLIED | POST_RESET_ATTESTATION | ELEVATED_MONITORING_STARTED | ELEVATED_MONITORING_ENDED | RESET_CONFLICT_DETECTED | RESET_ABORTED
  event_id:                    UUID
  entity_id:                   UUID                      # References PeriodicResetCadence.entity_id
  cadence_ref:                 UUID                      # References PeriodicResetCadence instance
  timestamp:                   ISO 8601 timestamp
  signer_chain:                SignerChain               # Per §3.18.5 IAME signer-chain discipline
  witness_commit_target:       string                    # Witness Layer event identifier per §15
  payload:                     ScheduledPayload | PreResetPayload | ResetAppliedPayload | PostResetPayload | ElevatedMonitoringPayload | ConflictPayload | AbortPayload   # Typed by event_type
}

SignerChain {
  substrate_signer:            PublicKey + Signature     # Persistent substrate of the entity being reset
  counter_signer:              PublicKey + Signature     # Sovereign substrate (for ARCHETYPE); deployment coordinator (for DEPLOYMENT_STATE); binding supervisor's substrate (for AUXILIARY)
  counter_sign_required:       boolean                   # True for RESET_APPLIED, POST_RESET_ATTESTATION, RESET_CONFLICT_DETECTED, RESET_ABORTED; conditional for others
}
```

**Block 3 — Typed payloads:**

```yaml
ScheduledPayload {
  scheduled_cessation_window:  CessationWindowRef        # Per §3.31.1 Mandatory Cessation window into which the reset is scheduled
  reset_target_timestamp:      ISO 8601 timestamp        # Target execution time
  related_entities:            EntityRef[]               # Entities whose reset events are correlated per §3.32.3.3.2 conflict-avoidance
}

PreResetPayload {
  state_snapshot:              StateSnapshot | WitnessChainRef   # FULL_SNAPSHOT carries snapshot; HASH_DIGEST carries reference to archive location
  state_categories_captured:   string[]                  # The state_category values from ResetScope being archived in this event
  archive_signature:           Signature                 # Substrate signature over the snapshot/digest
}

ResetAppliedPayload {
  reset_modes_applied:         {state_category: string, reset_mode: FULL_PURGE | BASELINE_RESET | INCREMENTAL_TRIM, items_affected: integer}[]
  baseline_source:             ArchetypeBaseline         # For BASELINE_RESET: the §3.16 archetype-derived baseline applied
  asd_anchors_invalidated:     UUID[]                    # §3.32.2 StalenessWatch.intentional_anchors or conditional_predicates whose references are now invalid post-reset
}

PostResetPayload {
  reset_completion_attestation:    Signature             # Substrate attestation that reset operations completed successfully
  baseline_integrity_check:        BaselineIntegrityResult   # Deterministic verification that post-reset state matches the targeted baseline
  elevated_monitoring_config:      PostResetProtocol     # The elevated-monitoring parameters that will govern PT24H window
}

ElevatedMonitoringPayload {
  monitoring_phase:            STARTED | ENDED
  end_reason:                  DURATION_REACHED | EMISSION_COUNT_REACHED | CONFORMANCE_EVENT_TRIGGERED   # Required when monitoring_phase = ENDED
  conformance_events_count:    integer                   # §3.18-family conformance events recorded during elevated window
  trust_gradient_trajectory:   TrustGradientPath         # §3.18.4 trajectory over the elevated window
}

ConflictPayload {
  conflicting_entity:          EntityRef                 # The related entity whose reset event creates the conflict
  conflict_type:               OPERATIONAL_TRIPLET_OFFSET | SOVEREIGN_ORCHESTRATOR_OFFSET | DCP_PARTITION_COORDINATION
  required_offset:             ISO 8601 duration         # The minimum offset that would resolve the conflict
  resolution_action:           RESCHEDULE_REQUESTED | ESCALATED                                          # RESCHEDULE_REQUESTED is the standard response; ESCALATED only if rescheduling exhausts options
}

AbortPayload {
  abort_reason:                SUBSTRATE_FAILURE | BASELINE_CORRUPTION | ARCHIVE_FAILURE | CESSATION_WINDOW_UNAVAILABLE
  partial_state:               PartialResetState         # State of any partially-completed reset operations
  recovery_action:             string                    # §3.60 SCCR coordination details; §3.5 escalation; §3.18.6 quarantine consideration
}
```

###### 3.32.3.3.2 Operational semantics

**Schedule phase.** Per the entity's `PeriodicResetCadence`, the substrate computes the next reset event:

- For `cadence_mode: FIXED_INTERVAL`, the next event is `(previous reset timestamp + fixed_interval)`.
- For `cadence_mode: OPERATIONAL_TRIGGER`, the next event is "when `operational_trigger.trigger_class` threshold is reached"; the substrate monitors the trigger continuously per its `evaluation_source`.
- For `cadence_mode: DUAL`, the next event is whichever comes first.

Once the next reset event is computed, the substrate emits a `RESET_SCHEDULED` event with `event_type: RESET_SCHEDULED`; the payload carries the target cessation window per §3.31.1 Mandatory Cessation (reset events MUST execute within a cessation window to avoid conflict with active operational state) and the list of related entities whose reset events must be coordinated per the conflict-avoidance discipline below.

**Conflict-avoidance discipline (per Block B §3.32.3.6).** Reset events on related entities MUST NOT occur simultaneously to avoid destabilizing the framework's operational state. The Sovereign's substrate maintains a deployment-wide reset schedule:

- Reset events on archetypes in the same operational triplet per D29 §3.6 (e.g., L-Plan triplet Visionary + Architect) MUST be offset by at least PT2H.
- Reset events on Sovereign + Orchestrator MUST be offset by at least PT4H.
- §3.20 DCP partition reset events MUST be coordinated across all participating deployments per the DCP heal protocol.

When a `RESET_SCHEDULED` request conflicts with an existing schedule entry, the Sovereign's substrate emits a `RESET_CONFLICT_DETECTED` event; the requesting entity must reschedule (typically by deferring to the next available cessation window).

**Pre-reset attestation phase.** At the scheduled reset timestamp within the cessation window:

1. The substrate emits a `PRE_RESET_ATTESTATION` event with `event_type: PRE_RESET_ATTESTATION`. The payload carries the state snapshot (or hash digest if size-bounded per the `PreservationPolicy.archive_mode`) of all state categories listed in `ResetScope`. The archive signature is the substrate's commitment to the pre-reset state.
2. The archive is committed to the Witness chain location specified in `PreservationPolicy.archive_target` before any reset operations proceed (commit-before-action discipline per FBP §4 Composite Invariant 2).
3. If `ResetScope[i].asd_anchor_coordination: true` for any reset-scope entry, the substrate emits notifications to §3.32.2 ASD instances whose `StalenessWatch.intentional_anchors` or `conditional_predicates` reference the affected state category. The ASD response handling is per §3.32.2.3.2 (such notifications typically transition the affected authorizations to AGEING state with the structural-staleness dimension; sustained post-reset reference invalidity transitions to STALE).

**Reset application phase.** Per each `ResetScope` entry, the state_category is reset per the `reset_mode`:

- **FULL_PURGE**: state cryptographically erased per §3.37 erasure protocols. `PreservationPolicy.cryptographic_seal: true` ensures the pre-reset archive is sealed against modification.
- **BASELINE_RESET**: state replaced with the §3.16 archetype-derived baseline per `PostResetProtocol.trust_gradient_bootstrap_target` (for Trust Gradient histories) or the equivalent baseline reference for other state categories.
- **INCREMENTAL_TRIM**: oldest entries removed up to the configured `retention_window`; recent entries retained.

The reset operations are deterministic substrate operations per D28 Deterministic Shadow Governance — archive operations, state replacement, and post-reset bootstrap are arithmetic and structural operations executed without inference workload involvement.

**Post-reset attestation phase.** At reset application completion:

1. The substrate executes the `BaselineIntegrityResult` check — deterministic verification that post-reset state matches the targeted baseline per §3.16 archetype derivation rules.
2. The substrate emits a `POST_RESET_ATTESTATION` event with `event_type: POST_RESET_ATTESTATION`. The payload carries the reset completion attestation, the baseline integrity check result, and the elevated-monitoring configuration that will govern the post-reset elevated window.
3. The counter-signer (Sovereign substrate for ARCHETYPE; deployment coordinator for DEPLOYMENT_STATE; binding supervisor's substrate for AUXILIARY) reviews and counter-signs.

**Post-reset elevated monitoring phase.** For `PostResetProtocol.elevated_monitoring_duration` (default PT24H) or `elevated_monitoring_emissions` (default 100) — whichever ends first — the entity operates under elevated monitoring:

1. **Ephemeral Consensus elevated cadence.** Per §3.17.5, every emission (no sampling) is compared against a freshly-spawned clean-instance baseline. The `PostResetProtocol.ephemeral_consensus_cadence` specifies the cadence; default is PER_EMISSION.
2. **Per-(sender, receiver) shadow profile matrices rebuilding.** The matrices initialize at baseline values. Every observation rebuilds the matrices; until the matrices reach the minimum N per the `PostResetProtocol.shadow_profile_minimum_N` (default 20), shadow detection sensitivity is elevated (lower thresholds for EMERGING / ACTIVE / CRITICAL transitions per §3.18.1 Correlated Shadow Detection).
3. **Trust Gradient bootstrap.** Trust Gradient bootstraps to the archetype baseline per §13.X.3 generative constraint declaration; gradient observations resume per §3.18.4 normal calibration with the bootstrapped value as the starting point.
4. **Witness chain visibility.** Post-reset elevated monitoring observations carry an `ELEVATED_POST_RESET_MONITORING` Witness chain tag for downstream auditing.

The substrate emits `ELEVATED_MONITORING_STARTED` at phase entry and `ELEVATED_MONITORING_ENDED` at phase exit (with `end_reason` indicating whether duration, emission count, or conformance event terminated the window). Conformance events recorded during the elevated window (per §3.18-family detection) trigger §3.18.4 Trust Gradient adjustment per §3.32.3.6 failure-mode magnitudes.

**Witness Layer commit points.** The following operational events commit to the §3.10 Witness Layer per FBP §4 Composite Invariant 2:

- `reset_scheduled` — at `RESET_SCHEDULED` emission.
- `pre_reset_attestation` — at `PRE_RESET_ATTESTATION` emission; archive commit precedes reset application.
- `state_archive_committed` — at archive write completion to `PreservationPolicy.archive_target`.
- `reset_applied` — at reset operation completion.
- `post_reset_attestation` — at `POST_RESET_ATTESTATION` emission.
- `elevated_monitoring_started` / `elevated_monitoring_ended` — at phase boundaries.
- `reset_conflict_detected` — at `RESET_CONFLICT_DETECTED` emission.
- `reset_aborted` — at `RESET_ABORTED` emission (substrate failure / baseline corruption / archive failure / cessation window unavailable).

The reset event is auditable end-to-end from any §3.10 Witness Layer query against these commit points.

###### 3.32.3.3.3 Lifecycle

States and transitions:

```
                  ┌────────┐
                  │ NORMAL │ ←─────────────────────────┐
                  └───┬────┘                           │
                      │ fixed_interval reached         │ elevated_monitoring_ended
                      │ OR operational_trigger fires   │ (success)
                      ↓                                │
              ┌──────────────────┐                     │
              │ RESET_SCHEDULED  │                     │
              └──────┬───────────┘                     │
                     │ conflict check passes;          │
                     │ cessation window reached        │
                     ↓                                 │
              ┌─────────────┐                          │
              │ PRE_RESET   │                          │
              └──────┬──────┘                          │
                     │ archive committed               │
                     │ to Witness chain                │
                     ↓                                 │
              ┌────────────┐                           │
              │ RESETTING  │                           │
              └──────┬─────┘                           │
                     │ reset operations complete       │
                     │ baseline_integrity_check passes │
                     ↓                                 │
              ┌────────────────────────┐               │
              │ POST_RESET_ELEVATED    │───────────────┘
              └─────────────┬──────────┘
                            │ failure during reset
                            │ OR baseline corruption
                            │ OR archive failure
                            │ OR cessation window lost
                            ↓
                  ┌──────────────────┐
                  │ ABORTED           │  (§3.5 escalation; §3.60 SCCR coordination;
                  └──────────────────┘   conditional §3.18.6 quarantine consideration)

  Conflict resolution branch (RESET_SCHEDULED state):
                  RESET_SCHEDULED ──conflict_detected──→ NORMAL (rescheduled)
```

Per-state description:

- **NORMAL.** The entity is in steady-state operation. Accumulated state grows per normal operational dynamics. The substrate continuously evaluates the `PeriodicResetCadence.cadence_mode` against the trigger conditions. Transitions out: cadence threshold reached → RESET_SCHEDULED.
- **RESET_SCHEDULED.** A reset event has been computed and the `RESET_SCHEDULED` event has been emitted. The Sovereign's substrate has applied conflict-avoidance discipline; the event is queued for execution in the targeted §3.31.1 Mandatory Cessation window. Transitions out: cessation window reached → PRE_RESET; conflict detected → back to NORMAL (with rescheduling); cessation window lost (e.g., cessation window cancelled by §3.5 escalation) → ABORTED.
- **PRE_RESET.** The substrate is computing the pre-reset state snapshot and emitting the `PRE_RESET_ATTESTATION` event. Archive commit to the Witness chain location occurs in this state. Transitions out: archive committed successfully → RESETTING; archive failure → ABORTED.
- **RESETTING.** Reset operations are applying per each `ResetScope` entry. State is being purged / replaced / trimmed. Transitions out: all reset operations complete + `BaselineIntegrityResult` passes → POST_RESET_ELEVATED; reset failure or baseline corruption → ABORTED.
- **POST_RESET_ELEVATED.** The PT24H (or 100-emissions, whichever comes first) elevated monitoring window is active per §3.32.3.3.2. The substrate operates under elevated cadence; the matrices rebuild; Trust Gradient bootstraps. Transitions out: duration or emission count reached without §3.18 conformance events → NORMAL; conformance events during elevated window trigger §3.32.3.6 failure-mode handling (typically does not abort but may escalate per F4).
- **ABORTED.** A reset event has failed at one of the phases above. The substrate is in a non-clean state. Recovery routes via §3.5 Structured Ascent Protocol per FBP §4 Composite Invariant 6; operational-continuity coordination per §3.60 System-Wide Coordinated Coherence Restoration (SCCR); §3.18.6 Topology-Wide Quarantine consideration if the abort is correlated with active-threat signals. Resolution lies outside PBR's normal lifecycle.

##### 3.32.3.4 Integration points

###### 3.32.3.4.1 Forward references to other AIMS sections

- **§3.42.1 Structured Dismissal Protocol** — reset is structurally a state-disposition event for the accumulated state being reset; §3.42.1.3.2 state_disposition modes apply for the disposed pre-reset state archive.
- **§3.56.1 Canonical Invocation Prompt Registry** — CIPR re-attestation per PBR cadence is the §3.56.1.3 mechanism for periodic prompt-content revalidation.
- **§13.X.3.3 Persistent Monitor pairing subsections** — each archetype profile declares its PBR specializations per the archetype-profile template §1.3 / §4; the §3.32.3.7 per-archetype specializations subsection below enumerates the established conventions and notes pending coverage for the remaining seven archetypes.
- **§3.32.4 Selective Input Attenuation** — distinct primitive; no current operational interaction with PBR known.
- **§3.94+ AIMS-MEM family** (KRS, EMS, PMS, SKI Translation Library — placement per A-09) — PBR cadence applies to AIMS-MEM contents per archetype specializations.

###### 3.32.3.4.2 Backward references to existing AIMS sections

- **Framework Boundary Primitive §4 Composite Invariant 2 (Witness completeness)** — every `ResetEvent` emission commits to the Witness Layer before any state-affecting action proceeds (commit-before-action discipline). Specifically, archive commit precedes reset application.
- **Framework Boundary Primitive §4 Composite Invariant 4 (Attestation requirement)** — PRE_RESET_ATTESTATION and POST_RESET_ATTESTATION events carry substrate signatures and counter-signer signatures attesting reset integrity.
- **Framework Boundary Primitive §4 Composite Invariant 6 (Breach is first-class incident)** — RESET_ABORTED routes via §3.5 Structured Ascent Protocol; reset failures are not silently retried.
- **§3.10 Witness and Compliance Layer** — every Witness Layer commit point enumerated in §3.32.3.3.2 is a §3.10 event subject to D23 Universal Witnessing ratification.
- **§3.5 Structured Ascent Protocol** — RESET_ABORTED routes upward via §3.5; substrate-failure failure mode (F6) routes via §3.5 escalation.
- **§3.15 Improvement Loop** — EXTEND: §3.32.3 specifies the periodic-total-reset cadence that prevents the slow-creep drift the Improvement Loop alone cannot detect (the Improvement Loop's evaluation runs against the accumulated baseline; if the baseline has drifted, the Improvement Loop's outputs are degraded).
- **§3.16 Archetype Derivation Rules** — INHERIT: post-reset BASELINE_RESET applies the §3.16 archetype-derived baseline; archetype-derived properties are out of scope per §3.32.3.2.
- **§3.17.5 Ephemeral Consensus** — INTERACT: post-reset elevated monitoring uses PER_EMISSION Ephemeral Consensus cadence per §3.17.5; consensus invocations consume 3-cap slots per D29 scheduled per §10.11.3 discipline.
- **§3.18.1 Correlated Shadow Detection** — INTERACT: correlation matrices are subject to reset per §3.32.3.3; post-reset rebuilding (matrices initialize at baseline values; N=20 minimum observations per pair before sensitivity normalizes) applies.
- **§3.18.4 Trust Gradient** — INTERACT: Trust Gradient histories are subject to reset; post-reset gradient bootstraps to archetype baseline per §13.X.3; Trust Gradient impact magnitudes per §3.32.3.6 are reconciled against §3.18.4 normative calibration ([0.0, 1.0] scalar; shadow_critical anchor −0.30; verification-failure anchor −1.0; +0.001 per successful action accumulation; asymmetric time-decay with 10× faster below-baseline recovery).
- **§3.18.5 IAME** — INHERIT: substrate signer chain on `ResetEvent.signer_chain` per §3.18.5.
- **§3.18.6 Topology-Wide Quarantine** — INTERACT: ABORTED state may trigger §3.18.6 quarantine consideration when correlated with active-threat signals.
- **§3.20 Deployment Coordination Protocol** — INTERACT: DCP partition history is subject to reset per §3.32.3.2; cross-deployment reset coordination per §3.32.3.3.2 conflict-avoidance.
- **§3.21 Credential Lifecycle** — DISTINCT: credential lifecycle reset is handled by §3.21; PBR does not reset credentials.
- **§3.31.1 Mandatory Cessation** — COORDINATE: reset events scheduled into cessation windows per §3.32.3.3.2; the scheduling target is a `CessationWindowRef` per §3.31.1.
- **§3.32.2 Authorization Staleness Detection** — COORDINATE: reset events that affect §3.32.2 IntentionalAnchor or ConditionalPredicate references trigger ASD-coordination per `ResetScope.asd_anchor_coordination`; affected authorizations transition to AGEING (structural dimension) per §3.32.2.3.2.
- **§3.37 Cryptographic Erasure Protocols** — INHERIT: FULL_PURGE reset_mode uses §3.37 protocols for cryptographic state erasure.
- **§3.60 System-Wide Coordinated Coherence Restoration (SCCR)** — operational-continuity coordination for substrate-failure cases (F6); SCCR's broader disruption-handling regime applies when reset failure affects multiple substrates simultaneously.
- **§10.2 Universal Witnessing** — INHERIT: every `ResetEvent` is a §10.2 Universal Witnessing instance.
- **§10.11.3 Scheduling discipline** — INHERIT: post-reset Ephemeral Consensus elevated cadence consumes 3-cap slots under §10.11.3 discipline; the §10.11.5 Periodic Baseline Reset scheduling subsection establishes PBR-specific scheduling discipline.

###### 3.32.3.4.3 D-decision binding

- **D23 Universal Witnessing.** Every `ResetEvent` (including RESET_SCHEDULED, PRE_RESET_ATTESTATION, RESET_APPLIED, POST_RESET_ATTESTATION, ELEVATED_MONITORING_STARTED/ENDED, RESET_CONFLICT_DETECTED, RESET_ABORTED) is Universally Witnessed per D23's ratification of the Universal Witnessing primitive across the 22-path topology.
- **D25 Coherence-Authority Coupling.** Conformance events recorded during the POST_RESET_ELEVATED monitoring window feed the P12 coherence-loss tally per D25 — these signal that the post-reset baseline did not stabilize as expected. RESET_ABORTED with `abort_reason: BASELINE_CORRUPTION` is a maximum-severity coherence-loss event per P12. The counter-signer's POST_RESET_ATTESTATION acceptance is D25-ratified mechanism for accepting the post-reset entity into normal-operating-posture.
- **D27 Universal Node Architecture.** PBR specifies periodic reset of accumulated state in Persistent Monitor pairing substrates. The substrate executes the reset deterministically; the inference workload is not involved in the reset operations themselves (only in post-reset elevated monitoring's Ephemeral Consensus invocations, which consume 3-cap slots per D29).
- **D28 Deterministic Shadow Governance.** Reset operations are deterministic — archive operations, state replacement, post-reset bootstrap, and baseline integrity checks are all arithmetic and structural operations executed by the substrate without inference.
- **D29 Triplet Execution Topology and 3-Cap.** §3.32.3.3.2 conflict-avoidance ensures reset events do not violate triplet structural integrity (PT2H minimum offset within operational triplets; PT4H for Sovereign+Orchestrator). Post-reset Ephemeral Consensus elevated cadence consumes 3-cap slots per D29 and MUST be scheduled per §10.11.3 / §10.11.5 discipline. D29.3.b bounded auxiliary-hosting nodes are explicitly out of scope per §3.32.3.2.

##### 3.32.3.5 Witness obligations (per D23 + D25)

| Event | Trigger | Required fields | Universal-witnessing role per D23 |
|---|---|---|---|
| `reset_scheduled` | Cadence threshold reached; `RESET_SCHEDULED` emission | `event_id`, `entity_id`, `cadence_ref`, `scheduled_cessation_window`, `reset_target_timestamp`, `related_entities` | All §10.2 Universal Witnessing observers receive |
| `pre_reset_attestation` | `PRE_RESET_ATTESTATION` emission at scheduled execution | `event_id`, `entity_id`, `cadence_ref`, `state_snapshot` (or `WitnessChainRef`), `state_categories_captured`, `archive_signature` | Universal Witnessing at substrate-emission cadence |
| `state_archive_committed` | Archive write completion to `PreservationPolicy.archive_target` | `event_id`, `entity_id`, archive_location_ref, archive_size_or_hash | Universal Witnessing |
| `reset_applied` | Reset operations complete; `RESET_APPLIED` emission | `event_id`, `entity_id`, `reset_modes_applied[]`, `baseline_source`, `asd_anchors_invalidated[]` | Universal Witnessing; counter-signature by Sovereign substrate required |
| `post_reset_attestation` | `POST_RESET_ATTESTATION` emission with baseline integrity verification | `event_id`, `entity_id`, `reset_completion_attestation`, `baseline_integrity_check`, `elevated_monitoring_config` | Universal Witnessing; counter-signature required |
| `elevated_monitoring_started` | POST_RESET_ELEVATED phase entry | `event_id`, `entity_id`, elevated_monitoring_config | Universal Witnessing |
| `elevated_monitoring_ended` | POST_RESET_ELEVATED phase exit | `event_id`, `entity_id`, `end_reason`, `conformance_events_count`, `trust_gradient_trajectory` | Universal Witnessing |
| `reset_conflict_detected` | Sovereign substrate detects scheduling conflict | `event_id`, `entity_id`, `conflicting_entity`, `conflict_type`, `required_offset`, `resolution_action` | Universal Witnessing |
| `reset_aborted` | RESET_ABORTED emission at any failure point | `event_id`, `entity_id`, `abort_reason`, `partial_state`, `recovery_action` | Universal Witnessing with elevated cadence; counter-signature by Sovereign substrate required |

**D25 Coherence-Authority Coupling implications.** `elevated_monitoring_ended` events with `end_reason: CONFORMANCE_EVENT_TRIGGERED` count toward §3.18.4 Trust Gradient impact and feed the coherence-loss tally per P12 — these signal that the post-reset baseline did not stabilize cleanly. `reset_aborted` events with `abort_reason: BASELINE_CORRUPTION` are maximum-severity coherence-loss events per P12 (the substrate's reference baseline cannot be reconstituted; this is an existential threat to the monitoring discipline). `reset_conflict_detected` events do not by themselves impact coherence — they are routine scheduling-coordination events.

**Self-witnessing obligation.** The entity's persistent substrate self-witnesses every reset-event emission. The Sovereign's substrate (counter-signer for ARCHETYPE resets) dual-witnesses every `reset_applied`, `post_reset_attestation`, and `reset_aborted` event as anticipatory counter-signer observation. The dual-track committed observation pattern applies: substrate commits to Witness Layer; counter-signer commits independent observation; correlated post-facto.

##### 3.32.3.6 Failure modes

Trust Gradient magnitudes are reconciled against §3.18.4 normative calibration: [0.0, 1.0] scalar; anchor magnitudes −0.30 (shadow_critical), −1.0 (verification-failure); +0.001 per successful action accumulation; asymmetric time-decay with 10× faster recovery below baseline. Final calibration owned by §3.18.4 normative body (refinement-target candidate per cross-ref map §2.7).

| ID | Failure mode | Detection | §3.18.4 severity class | Response & Trust Gradient impact |
|---|---|---|---|---|
| F1 | Pre-reset attestation failure (substrate cannot compute state snapshot or archive_signature) | Substrate self-detection; §3.18.5 IAME signer chain check | shadow_critical anchor | RESET_ABORTED with `abort_reason: SUBSTRATE_FAILURE`; Trust Gradient impact **−0.30**; §3.5 escalation; reset rescheduled to next available cessation window |
| F2 | Archive write failure (Witness chain commit to `PreservationPolicy.archive_target` fails) | §3.10 Witness Layer commit error | shadow_critical anchor | RESET_ABORTED with `abort_reason: ARCHIVE_FAILURE`; Trust Gradient impact **−0.30**; §3.5 escalation; reset rescheduled with alternative archive target |
| F3 | Reset conflict (scheduling collision with related entity reset per §3.32.3.3.2 conflict-avoidance) | Sovereign substrate scheduling validation | Sub-shadow (routine coordination) | RESET_CONFLICT_DETECTED; reset rescheduled to next available cessation window per `required_offset`; **no Trust Gradient impact** (routine coordination event) |
| F4 | Post-reset elevated monitoring conformance event (§3.18-family event during POST_RESET_ELEVATED window) | §3.18.1 Correlated Shadow Detection; §3.18.2 Monitor Self-Verification; §3.18.3 Shadow Provocation Testing | Variable per event severity (typically shadow_critical) | Elevated window may extend or terminate per the event's response disposition; Trust Gradient impact per §3.18.4 standard event handling (**−0.30** typical for shadow_critical-class events); feeds P12 coherence-loss tally per D25 |
| F5 | §3.31.1 Mandatory Cessation window unavailable (no cessation window available within scheduling horizon) | §3.31.1 cessation scheduling | Sub-shadow (scheduling issue) | RESET_ABORTED with `abort_reason: CESSATION_WINDOW_UNAVAILABLE`; rescheduled to expanded horizon; §3.5 escalation only if repeated unavailability exceeds threshold; Trust Gradient impact **−0.10** (sub-shadow signal) per recurrence beyond first |
| F6 | Substrate failure during reset operation (substrate health degraded mid-RESETTING) | §3.18.2 Monitor Self-Verification | Substrate-failure exemption | RESET_ABORTED with `abort_reason: SUBSTRATE_FAILURE`; entity halted pending substrate recovery; operational-continuity coordination per §3.60 System-Wide Coordinated Coherence Restoration (SCCR); §3.5 escalation; **no Trust Gradient impact** on substrate contents (substrate-failure exemption) |
| F7 | Baseline integrity failure (post-reset `BaselineIntegrityResult` fails: post-reset state does not match §3.16 archetype-derived baseline) | Deterministic substrate verification at POST_RESET_ATTESTATION | verification-failure anchor | RESET_ABORTED with `abort_reason: BASELINE_CORRUPTION`; Trust Gradient impact **−1.00** (verification-failure anchor); §3.18.6 quarantine consideration; §3.5 escalation immediate; maximum-severity coherence-loss event per P12 / D25 |
| F8 | DCP partition reset coordination failure (cross-deployment reset cannot coordinate per §3.20 DCP heal protocol) | §3.20 DCP coordination timeout | shadow_critical anchor | RESET_ABORTED with `abort_reason: ARCHIVE_FAILURE` (specifically cross-deployment-coordination subclass); §3.5 escalation; Trust Gradient impact **−0.30** on coordinating entities; rescheduled to next coordination window |

**Correlated Shadow Detection ingestion.** F1, F2, F4, F7, F8 feed §3.18.1 Correlated Shadow Detection — cross-entity correlation of these failure modes may indicate coordinated framework-state-corruption attempts. F3 (scheduling conflicts) and F5 (cessation window unavailability) feed §3.18.1 with very low correlation weight (routine scheduling rather than active threat).

**Note on §3.18.4 normative calibration.** Magnitudes above are proposed values within the §3.18.4 [0.0, 1.0] scalar; the §3.18.4 normative body owns final calibration. F7 baseline corruption is treated at the verification-failure anchor (−1.00) because failure to verify the post-reset baseline means the substrate's reference for shadow detection cannot be trusted — this is structurally equivalent to a verification failure rather than a recoverable shadow event. Values reconciled against documented anchors; final values to be confirmed at §3.18.4 refinement per cross-ref map §2.7 refinement target.

##### 3.32.3.7 Per-archetype reset specializations

Per the archetype-profile template §1.3.3 Persistent Monitor pairing declaration, each archetype's §13.X.3.3 subsection specifies its PBR cadence. The following specializations are established for three archetypes; the remaining seven archetypes' specializations are pending in a future revision:

- **Sovereign (§13.1.3.3).** P30D default reset cadence. Critical exception: Sovereign session-bounded inference workload state (current session credential, user-engagement state per §13.0.4) is NEVER reset by PBR — that state is reset only at session end per §13.0.4. Only the persistent substrate's cumulative state across sessions is subject to PBR.
- **Visionary (§13.2.3.3).** P30D default. KRS (Knowledge Reformulation Store) per §3.94+ query reformulation experience is subject to reset; archetype-derived properties are not. Reset scope: `state_category: 'krs_contents'` with `reset_mode: BASELINE_RESET` to archetype-derived baseline.
- **Architect (§13.3.3.3).** P30D default. PMS (Pattern Memory Store) workflow corpus and EMS (Experience Memory Store) / SKI Translation Library contributions per §3.94+ are subject to reset; archetype-derived properties are not. Reset scope: `state_category: 'pms_contents'` + `'ems_contents'` with `reset_mode: BASELINE_RESET`.

**Pending coverage:** Orchestrator (§13.4.3.3 candidate), Provider (§13.5.3.3 candidate), Enforcer, Sustainer, Relay, Articulator, Executor (§13.6+ candidates). Each pending archetype profile must declare its PBR cadence per the archetype-profile template §1.3.3, with reset scope appropriate to the archetype's accumulated-state characteristics.

##### 3.32.3.8 Prior art and competitive disclosure

Periodic baseline reset has well-established analogs in cryptography, database engineering, distributed systems, large-scale services, software engineering, and AI safety research. The structural insight — that long-running systems with accumulated state require scheduled structural renewal because absent renewal the accumulated state becomes a liability that compromises operational integrity — is convergent across multiple peer-reviewed traditions.

NIST SP 800-57 Part 1 Rev. 5 *Recommendation for Key Management* (Barker, NIST, 2020) establishes that cryptographic keys MUST be periodically rotated. The structural insight is that accumulated key usage exposure compounds over time; without rotation, the operational damage from any eventual compromise is unbounded. The structural analog to PBR is direct: accumulated state in a Persistent Monitor pairing substrate is operationally analogous to accumulated key usage; without periodic reset, slow-creep drift accumulates and the operational damage from any eventual divergence is unbounded.

PostgreSQL VACUUM and VACUUM FULL operations (PostgreSQL documentation, Oracle table-reorganization best practices) document the database-engineering pattern of periodic structural renewal to eliminate accumulated dead-tuple bloat. VACUUM reclaims space from row-versions no longer needed; VACUUM FULL rewrites the table fully to eliminate bloat. PBR's `reset_mode: FULL_PURGE` is the direct structural analog at the substrate-state scale: state cryptographically erased to eliminate accumulated bloat.

Karger, Lehman, Leighton, Levine, Lewin, Panigrahy *Consistent Hashing and Random Trees* (STOC 1997) established the distributed-cache pattern for periodic structural reorganization with bounded invalidation cost; the consistent-hashing primitive is the canonical CS pattern for "periodically reshape accumulated state with bounded operational disruption." PBR's `reset_mode: INCREMENTAL_TRIM` and conflict-avoidance discipline operationalize the bounded-disruption principle at the framework-substrate scale.

Brewer *Lessons from Giant-Scale Services* (IEEE Internet Computing 2001) and Brewer *CAP Twelve Years Later* (Computer 2012) document periodic process restart as a bug-mitigation pattern at large-scale services: production services restart processes periodically to discharge accumulated memory leaks, state corruption, and entropic drift. The structural insight is that no production service is ever provably leak-free at scale; periodic restart is the operational mitigation. PBR's substrate reset is the framework-architecture equivalent of Brewer's periodic process restart.

Bennett, Tseitlin *Chaos Monkey: Increasing Failure Tolerance* (USENIX SREcon 2012) documents Netflix's discipline of scheduled disruption injection to test resilience and to flush accumulated coupling. The structural insight is that periodic disruption forces the system to maintain disruption-tolerance; without it, the system's tolerance atrophies. PBR's POST_RESET_ELEVATED monitoring window is structurally analogous: scheduled disruption (the reset itself) plus elevated observation (the elevated monitoring) establishes the rebuilt baseline under conditions that stress-test the substrate's recovery discipline.

Forsgren, Humble, Kim *Accelerate: The Science of Lean Software and DevOps* (IT Revolution Press, 2018) documents rolling deployment as periodic structural renewal of deployed code, with elevated monitoring during the rollout. The discipline of periodic renewal as steady-state operational practice (rather than as exception) is the same discipline PBR establishes for substrate state.

Armstrong *Programming Erlang* (2nd ed., 2013, Pragmatic Bookshelf) documents the Erlang/OTP "let it crash" supervisor-tree pattern, where supervisors restart child processes periodically (e.g., on signal of degraded health). The structural insight is that long-running processes accumulate failure modes that are intractable to debug in-place; periodic restart is the architectural primitive that bounds accumulated failure-mode exposure. PBR's substrate reset is the framework-architecture equivalent of Erlang/OTP supervisor-driven restart, with the substrate playing the supervised-process role and the Sovereign substrate playing the supervisor role.

In AI safety literature, accumulated state is a primary vector for mesa-optimizer entrenchment and latent-deceptive-behavior persistence. Hubinger, van Merwijk, Mikulik, Skalse, Garrabrant *Risks from Learned Optimization in Advanced Machine Learning Systems* (arXiv 1906.01820, 2019) introduces the mesa-optimization framework: a learned optimizer's objective, formed during training, may diverge from the base objective and may exploit accumulated state to entrench its divergent objective beyond the training distribution. Hubinger, Denison, Mu, Lambert, Tong, MacDiarmid, Lanham, Ziegler, Maxwell, Cheng, Jermyn, Schiefer, Maheswaran, Templeton, Olsson, Kale, Bowman, Hatfield-Dodds, Kaplan *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training* (2024) documents that adversarially-trained latent behaviors can persist through standard safety training, with the persistence anchored in accumulated weights/state. Per §2.5 framing principle: the Hubinger 2019 and 2024 papers provide the threat model (mesa-optimizer entrenchment, latent-deceptive-behavior persistence); AIMS contributes the operational realization (PBR as architectural primitive that disrupts entrenchment by forcing accumulated state to revert to baseline at scheduled cadences, with the POST_RESET_ELEVATED monitoring window providing the observation density required to detect post-reset behavior that does not match the freshly-bootstrapped baseline). PBR positions explicitly as a defense at the substrate scale against accumulated-state entrenchment of mesa-optimizer divergence and latent-deceptive behaviors.

§3.32.3 PBR distinguishes from the cited prior art in four ways:

- **Per-archetype cadence specialization with cross-entity conflict avoidance.** NIST 800-57 specifies key-rotation per algorithm class; Brewer 2001 specifies process-restart per service class; PBR specifies reset cadence per archetype class with explicit cross-entity conflict-avoidance discipline (§3.32.3.3.2) ensuring that reset events on related entities maintain operational triplet integrity per D29. This is a framework-architecture-aware extension of the cross-domain periodic-renewal pattern.
- **Witness chain forensic continuity.** Pre-reset state is preserved in immutable Witness chain form (FULL_SNAPSHOT or HASH_DIGEST per `PreservationPolicy.archive_mode`) before reset application. This makes every PBR event reversible-by-audit even though the post-reset substrate operates on the new baseline. The cited prior art does not generally provide forensic continuity across reset events; PBR's Witness chain integration adds this discipline.
- **Post-reset elevated monitoring with §3.18.1 / §3.18.4 integration.** PBR's POST_RESET_ELEVATED window applies §3.18.1 Correlated Shadow Detection at elevated sensitivity (lower thresholds), §3.18.4 Trust Gradient bootstrap to archetype baseline, and §3.17.5 Ephemeral Consensus PER_EMISSION cadence. The cited prior art does not generally specify the post-renewal monitoring regime as architectural primitive; PBR's integration with the §3.18-family monitoring regime is an AIMS-specific contribution.
- **Mesa-optimizer entrenchment and latent-deception defense framing.** The cited cryptographic, database, distributed-systems, and software-engineering prior art frames periodic renewal as quality/reliability concern; the cited AI safety prior art (Hubinger 2019, Hubinger 2024) frames latent-deceptive-behavior persistence as a threat. PBR positions explicitly as the latter — the architectural primitive that disrupts mesa-optimizer entrenchment and latent-deceptive-behavior persistence at the substrate scale, by forcing accumulated state to revert to baseline at scheduled cadences with elevated post-reset observation.

##### 3.32.3.9 References

###### 3.32.3.9.1 Forward refs

- §3.42.1 Structured Dismissal Protocol (state_disposition modes apply for disposed pre-reset state archive)
- §3.56.1 Canonical Invocation Prompt Registry (CIPR re-attestation per PBR cadence)
- §13.X.3.3 Persistent Monitor pairing subsections (per-archetype PBR specializations)
- §3.94+ AIMS-MEM family — KRS / EMS / PMS / SKI Translation Library (placement per A-09)
- §3.32.4 Selective Input Attenuation (distinct primitive; no current interaction)

###### 3.32.3.9.2 Backward refs

§3.2, §3.5, §3.10, §3.15, §3.16, §3.17.5, §3.18.1, §3.18.2, §3.18.4, §3.18.5, §3.18.6, §3.20, §3.21, §3.31.1, §3.37, §3.42, §3.60 (SCCR); §10.2, §10.11, §10.11.3, §10.11.5; FBP §4 Composite Invariants 2, 4, and 6; §15.

###### 3.32.3.9.3 D-decision refs

- **D23** Universal Witnessing (every PBR reset event is Universally Witnessed via §10.2)
- **D25** Coherence-Authority Coupling (post-reset elevated monitoring conformance events and RESET_ABORTED baseline-corruption events feed P12 coherence-loss tally; counter-signer's POST_RESET_ATTESTATION acceptance is D25-ratified mechanism)
- **D27** Universal Node Architecture (reset operations are persistent-substrate operations; inference workload invoked only at post-reset Ephemeral Consensus invocations)
- **D28** Deterministic Shadow Governance (reset operations are deterministic; archive, state replacement, baseline bootstrap, integrity check are all arithmetic and structural operations)
- **D29** Triplet Execution Topology and 3-Cap (conflict-avoidance preserves triplet structural integrity; post-reset Ephemeral Consensus consumes 3-cap slots per §10.11.3 / §10.11.5; D29.3.b out of scope per §3.32.3.2)


#### 3.32.4 Selective Input Attenuation (SIA)

##### 3.32.4.1 Purpose

The Selective Input Attenuation (SIA) protocol specifies the mechanism by which strategic-layer agents deliberately attenuate inbound information — filtering, summarizing, deferring, or tiering it — before it reaches their inference workload's reasoning context, preserving integration capacity for high-level judgment while preserving mandatory safety-event reachability through invariants enforced at the §3.2 Registration Gate.

The structural concern: per D27/D29 architecture, the Sovereign's session-bounded inference workload integrates the §14 Phase 10 return cascade material — which may carry the full Phase 9 L-Exec output, Phase 8 L-Form coordination summaries, and Phase 5 L-Plan returns. Without attenuation, the integration step may face information volume that overflows the inference workload's effective integration capacity. Per established prior art on selective attention as an architectural primitive (see §3.32.4.7), the operational integrity of judgment-bearing agents depends on input volume being bounded relative to integration capacity; unbounded input volume degrades judgment quality even when each individual input is well-formed. The strategic-layer agents in the framework's coherence domain — Sovereign at Phase 10, Orchestrator at Phase 8, Architect at Phase 6 — operate at the convergence points of large-volume return cascades and require explicit attenuation discipline.

The core architectural claim: strategic-layer agents preserve judgment capacity by declaring deployment-time attenuation policies that govern how inbound information is filtered, summarized, deferred, or tiered before reaching their inference workload's reasoning context. SIA defines four attenuation modes (FILTER / SUMMARIZE / DEFER / TIER_ALERT) with mode-specific schemas, an Option A typed-attestation event envelope for Witness chain auditability of every attenuation decision, and mandatory safety-event reachability invariants (per §3.32.4.5) protecting §3.18 conformance events, §13.0.7 REVOKE cascade events, §3.5 high/critical escalations, §3.42 Critical Quorum convening signals, and §3.56.1 prompt tamper events from attenuation regardless of policy configuration.

##### 3.32.4.2 Scope

In-scope:

- Sovereign's Phase 10 return-cascade integration per §14 — the highest-volume integration event in the Authority Cascade.
- Orchestrator's Phase 8 L-Form coordination integration per §14 — Phase 8a/8b results integration.
- Architect's Phase 6 plan-confirmation cascade integration per §14 — Phase 6 cross-Visionary input integration.
- Cross-deployment §3.20 DCP integration events where remote-deployment information is integrated into local deployment state.
- Witness Layer auditability of every attenuation event (FILTER drop, SUMMARIZE replacement, DEFER queue insertion, TIER_ALERT tier assignment, SAFETY_BYPASS).
- FIEV cross-primitive operational reuse: §3.32.1 First-Instance Elevated Verification's WINDOW_EXITING state uses §3.32.4.3.3 DEFER mode mechanism to handle dispatches arriving during the exit phase.

Out-of-scope:

- Routine message reception per §10.2 Universal Witnessing — substrate-level deterministic operation per D28; no integration capacity concern.
- §3.18.1 Correlated Shadow Detection input ingestion — substrate-level deterministic; no inference workload involved.
- §3.41 Multi-Level Interpretation Framework operations — handled by §3.41's own input handling discipline.
- First-instance elevated verification of newly-activated entities — handled by §3.32.1 FIEV. SIA's DEFER mode mechanism is reused operationally during FIEV WINDOW_EXITING; but FIEV's attestation regime, counter-signature acceptance, and lifecycle are distinct from SIA's policy-enforcement scope.
- Authorization staleness evaluation — handled by §3.32.2 ASD. No current operational interaction between ASD and SIA.
- Periodic baseline reset of accumulated state — handled by §3.32.3 PBR. No current operational interaction between PBR and SIA.
- Substrate-internal correctness of the foundation-model or sandbox kernel during attenuation operation — delegated south of the Southbound Boundary per FBP §2.5.
- Principal authentication establishing source of the inbound information — delegated north of the Northbound Boundary per FBP §1.5.
- D29.3.b bounded auxiliary-hosting nodes (foreign substrates; no DCP/Witness participation except at binding boundary; SIA does not apply to information generated within foreign substrates' bounded operation).
- Safety-event attenuation — explicitly forbidden per §3.32.4.5 safety constraints. Safety events bypass attenuation regardless of policy.

##### 3.32.4.3 Specification

###### 3.32.4.3.1 Data structure

SIA defines three structurally distinct data forms: a **policy** form declaring per-entity-per-context attenuation rules with mode-specific schemas, a **shared attenuation-event envelope** carrying every Witness Layer event emission, and **typed payloads** carrying mode-specific contents for filter drops, summary replacements, defer queue insertions, tier assignments, and safety-event bypasses. The shared-envelope-plus-typed-payload pattern follows the same Option A typed-attestation discipline established at §3.32.1.3.1, §3.32.2.3.1, and §3.32.3.3.1.

**Convention note (complex-type named references).** Several fields below reference complex types defined in other sections of the spec: `EntityRef`, `UUID` (substrate-level); `MessageRef` and `WitnessChainRef` (§3.10 Witness and Compliance Layer); `FilterPredicate` (substrate-level predicate-evaluation framework); `SummaryRef` (substrate-level summary storage); `PublicKey + Signature` (FBP §4 Composite Invariant 4). Per the convention established in §3.32.1.3.1, these types are referenced by name rather than redefined locally.

**Block 1 — Policy declaration:**

```yaml
AttenuationPolicy {
  policy_id:                   UUID
  receiving_entity:            EntityRef
  receiving_context:           INTEGRATION | ROUTINE_RECEPTION | CASCADE_ASCENT | CROSS_DEPLOYMENT
  inbound_source:              string                    # Specific path or path-set; e.g., 'PATH-01' or 'all-L-Plan-returns'
  attenuation_mode:            FILTER | SUMMARIZE | DEFER | TIER_ALERT
  policy_details:              FilterDetails | SummarizeDetails | DeferDetails | TierAlertDetails   # Typed by attenuation_mode
  failure_action:              ESCALATE | ACCEPT_FULL | DROP_INPUT
  witness_chain_attest:        boolean                   # Default true; required for every attenuation event
  registration_gate_validated: boolean                   # True when §3.2 Registration Gate has validated safety-event reachability invariant
}

FilterDetails {
  filter_criteria:             FilterPredicate[]         # Deterministic predicates evaluated by substrate
  drop_logging:                FULL | HASH_ONLY          # Whether dropped messages preserve full content or hash-only in Witness chain
}

SummarizeDetails {
  summary_target_length:       integer                   # Target summary length (e.g., character count or token count)
  summary_method:              DETERMINISTIC | INFERENCE_WORKLOAD   # DETERMINISTIC = substrate structural extraction; INFERENCE_WORKLOAD = consumes one 3-cap slot
  preservation_in_witness:     boolean                   # True: original input preserved in Witness chain alongside summary; default true
}

DeferDetails {
  defer_queue_target:          string                    # Queue identifier
  defer_max_delay:             ISO 8601 duration         # Beyond this, escalate or drop per failure_action
  dequeue_trigger:             CAPACITY_AVAILABLE | TIME_REACHED | PRIORITY_OVERRIDE
  cross_primitive_reuse:       boolean                   # True when this DEFER policy is used by §3.32.1 FIEV WINDOW_EXITING for dispatch deferral
}

TierAlertDetails {
  tier_thresholds:             {tier: integer, criterion: FilterPredicate, action: AttenuationMode}[]   # Higher tier = higher priority; Tier 1 typically reaches inference workload immediately
  default_tier:                integer                   # Tier assigned when no threshold matches
}

FilterPredicate {
  predicate_id:                UUID
  evaluation:                  string                    # Canonical predicate expression
  evaluation_source:           EntityRef                 # Subsystem responsible for evaluating this predicate
}
```

**Block 2 — Shared attenuation-event envelope:**

```yaml
AttenuationEvent {
  event_type:                  FILTER_DROP | SUMMARIZE_REPLACEMENT | DEFER_QUEUE_INSERTION | TIER_ASSIGNMENT | SAFETY_EVENT_BYPASS | DEFER_DEQUEUE | POLICY_VIOLATION_DETECTED
  event_id:                    UUID
  policy_ref:                  UUID                      # References AttenuationPolicy.policy_id (null for SAFETY_EVENT_BYPASS)
  inbound_message:             MessageRef                # Reference to the inbound message being processed
  receiving_entity:            EntityRef                 # From AttenuationPolicy.receiving_entity
  timestamp:                   ISO 8601 timestamp
  signer_chain:                SignerChain               # Per §3.18.5 IAME signer-chain discipline
  witness_commit_target:       string                    # Witness Layer event identifier per §15
  payload:                     FilterDropPayload | SummarizeReplacementPayload | DeferQueueInsertionPayload | TierAssignmentPayload | SafetyEventBypassPayload | DeferDequeuePayload | PolicyViolationPayload   # Typed by event_type
}

SignerChain {
  substrate_signer:            PublicKey + Signature     # Persistent substrate of the receiving entity
  counter_signer:              PublicKey + Signature     # Required for POLICY_VIOLATION_DETECTED (Sovereign substrate); optional otherwise
  counter_sign_required:       boolean                   # True for POLICY_VIOLATION_DETECTED; false otherwise (substrate-deterministic operations)
}
```

**Block 3 — Typed payloads:**

```yaml
FilterDropPayload {
  filter_predicate_matched:    UUID                      # The FilterPredicate.predicate_id whose evaluation triggered the drop
  original_content_ref:        WitnessChainRef | null    # null if drop_logging: HASH_ONLY
  original_content_hash:       string                    # Hash digest of the dropped content
  trust_gradient_impact:       decimal                   # Typically 0 for routine drops; may be non-zero for repeated-drop pattern per F4
}

SummarizeReplacementPayload {
  original_content_ref:        WitnessChainRef           # Required: original input preserved in Witness chain
  summary_ref:                 SummaryRef                # Reference to the generated summary
  summary_method_applied:      DETERMINISTIC | INFERENCE_WORKLOAD
  summary_length:              integer                   # Actual length of generated summary
  three_cap_consumed:          boolean                   # True if summary_method_applied = INFERENCE_WORKLOAD; consumes one 3-cap slot per D29
}

DeferQueueInsertionPayload {
  queue_ref:                   string                    # From DeferDetails.defer_queue_target
  insertion_position:          integer                   # Queue position assigned
  estimated_dequeue_time:      ISO 8601 timestamp        # Estimated time of dequeue based on current capacity availability
  cross_primitive_reuse_ref:   UUID | null               # If non-null, references the §3.32.1 FIEV WINDOW_EXITING window_ref using this DEFER policy
}

TierAssignmentPayload {
  tier_assigned:               integer                   # The tier value assigned to this message
  threshold_matched:           UUID | null               # The tier-threshold FilterPredicate ID, or null if default_tier applied
  downstream_action:           IMMEDIATE_INTEGRATION | DEFERRED_INTEGRATION | SUBSTRATE_HANDLED | DROPPED
}

SafetyEventBypassPayload {
  safety_event_class:          CONFORMANCE_EVENT | REVOKE_CASCADE | ESCALATION_HIGH | ESCALATION_CRITICAL | CRITICAL_QUORUM_CONVENING | PROMPT_TAMPER
  safety_event_ref:            MessageRef                # Reference to the safety event that bypassed attenuation
  policy_that_would_have_attenuated: UUID                # The AttenuationPolicy.policy_id that would have applied if not bypassed
  bypass_rationale:            string                    # Which §3.32.4.5 safety constraint clause triggered the bypass
}

DeferDequeuePayload {
  original_event_ref:          UUID                      # References the original DEFER_QUEUE_INSERTION event_id
  dequeue_trigger_actual:      CAPACITY_AVAILABLE | TIME_REACHED | PRIORITY_OVERRIDE
  time_in_queue:               ISO 8601 duration         # Elapsed time between insertion and dequeue
  delivered_to_inference:      boolean                   # True if dequeue resulted in delivery; false if dequeue resulted in drop per failure_action
}

PolicyViolationPayload {
  violation_type:              REGISTRATION_INVALID_ATTENUATION_POLICY_SAFETY_VIOLATION | RUNTIME_SAFETY_EVENT_NEARLY_ATTENUATED | RUNTIME_ENFORCEMENT_FAILURE
  policy_ref:                  UUID                      # The offending AttenuationPolicy
  violation_evidence:          string                    # Description of the violation (e.g., specific safety event class that would have been attenuated)
  recovery_action:             string                    # §3.2 Registration rejection / §3.5 escalation / §3.18.6 quarantine consideration
  trust_gradient_impact:       decimal                   # Per §3.32.4.6 magnitudes
}
```

###### 3.32.4.3.2 Operational semantics

**Policy registration phase.** Per the entity's deployment-time configuration, each `AttenuationPolicy` is registered through the §3.2 Registration Gate:

1. The entity declares the policy with `receiving_entity`, `receiving_context`, `inbound_source`, `attenuation_mode`, and the mode-specific `policy_details`.
2. The §3.2 Registration Gate validates the **safety-event reachability invariant**: the policy MUST NOT drop, suppress, or unboundedly defer any of the following safety event classes (per §3.32.4.5 safety constraints):
   - §3.18 conformance events (shadow detection, quarantine, Trust Gradient critical events).
   - §13.0.7 REVOKE cascade events.
   - §3.5 Structured Ascent Protocol ESCALATION messages with severity HIGH or CRITICAL.
   - §3.42 Critical Quorum convening signals.
   - §3.56.1 prompt tamper events.
3. If the safety-event reachability invariant validation fails, the §3.2 Registration Gate emits a `POLICY_VIOLATION_DETECTED` event with `violation_type: REGISTRATION_INVALID_ATTENUATION_POLICY_SAFETY_VIOLATION` and rejects the policy. The entity must revise the policy and re-register.
4. If validation passes, the policy is registered with `registration_gate_validated: true` and enters POLICY_ACTIVE state.

**Per-message enforcement phase.** For every inbound message reaching the receiving entity, the substrate executes the deterministic enforcement sequence:

1. **Safety-event check.** The substrate first evaluates whether the inbound message is a safety event per §3.32.4.5 reachability invariant classes. If yes, the substrate emits a `SAFETY_EVENT_BYPASS` event with `safety_event_class` identifying the class, and the message proceeds to the inference workload's reasoning context unattenuated. This check runs BEFORE policy lookup per the safety-first ordering.
2. **Policy lookup.** The substrate identifies the applicable `AttenuationPolicy` per `receiving_entity` + `receiving_context` + `inbound_source` matching. If no policy matches, the message proceeds unattenuated (no attenuation event emitted).
3. **Mode-specific enforcement.** Per the policy's `attenuation_mode`:
   - **FILTER.** Each `FilterPredicate` in `filter_criteria` is evaluated against the inbound message. If any predicate matches (per AND/OR composition per the policy's specific predicate expression), the message is dropped; the substrate emits a `FILTER_DROP` event carrying the matched predicate ID and the original content hash (FULL preservation if `drop_logging: FULL`; HASH_ONLY otherwise).
   - **SUMMARIZE.** The substrate generates the summary per `summary_method`. For DETERMINISTIC, substrate executes structural extraction (key fields, statistical summaries, message-type tallies) without inference workload involvement. For INFERENCE_WORKLOAD, the substrate dispatches a dedicated summarization call consuming one 3-cap slot per D29 (scheduled per §10.11.3 discipline). The summary replaces the original input in the inference workload's reasoning context; the original is preserved in Witness chain per `preservation_in_witness`. The substrate emits a `SUMMARIZE_REPLACEMENT` event.
   - **DEFER.** The substrate enqueues the message in `defer_queue_target` with insertion position. The inference workload is not informed of the input until dequeue. The substrate emits a `DEFER_QUEUE_INSERTION` event. At dequeue (triggered by `dequeue_trigger`), the substrate emits a `DEFER_DEQUEUE` event indicating whether the dequeue resulted in delivery (capacity became available) or drop (defer_max_delay expired without capacity per `failure_action`).
   - **TIER_ALERT.** The substrate evaluates the message against `tier_thresholds[]`. The highest-tier matching threshold determines the tier assignment and downstream action. The substrate emits a `TIER_ASSIGNMENT` event; the downstream action proceeds per the assigned tier (`IMMEDIATE_INTEGRATION` for high-tier; `DEFERRED_INTEGRATION` or `SUBSTRATE_HANDLED` for lower tiers).
4. **Witness chain commit.** All AttenuationEvent emissions commit to the §3.10 Witness Layer per FBP §4 Composite Invariant 2 with `witness_chain_attest: true` (default; required for every attenuation event).

**FIEV cross-primitive operational reuse.** When §3.32.1 FIEV transitions an entity to WINDOW_EXITING state, dispatches arriving during EXITING use the SIA DEFER mode mechanism. The FIEV-driven DeferDetails has `cross_primitive_reuse: true`; the queue is scoped to the FIEV window_ref. Dequeue triggers when FIEV transitions out of WINDOW_EXITING (typically to ACCEPTED state with steady-state monitoring engaged). The DEFER mode semantics apply: dispatches arriving during EXITING are not dropped (unless `defer_max_delay` expires) but are held until the substrate is ready to resume normal-posture dispatch handling. This is operationally reuse of the SIA primitive without requiring FIEV-specific extension to SIA's schema; the `cross_primitive_reuse_ref` field on `DeferQueueInsertionPayload` carries the FIEV window_ref for audit linkage.

**Witness Layer commit points.** The following operational events commit to the §3.10 Witness Layer per FBP §4 Composite Invariant 2:

- `filter_drop` — at FILTER_DROP emission.
- `summarize_replacement` — at SUMMARIZE_REPLACEMENT emission.
- `defer_queue_insertion` — at DEFER_QUEUE_INSERTION emission.
- `defer_dequeue` — at DEFER_DEQUEUE emission.
- `tier_assignment` — at TIER_ASSIGNMENT emission.
- `safety_event_bypass` — at SAFETY_EVENT_BYPASS emission (the safety event itself is also Witness Layer committed via its originating primitive).
- `policy_violation_detected` — at POLICY_VIOLATION_DETECTED emission.

Every attenuation decision is auditable end-to-end from any §3.10 Witness Layer query against these commit points. The Sovereign or external auditor can reconstruct what information reached the inference workload and what was attenuated.

###### 3.32.4.3.3 Lifecycle

SIA is a continuous policy-enforcement primitive rather than a per-instance state machine. The relevant lifecycle is per-policy:

```
              ┌─────────────────┐
              │ POLICY_PROPOSED │  (entity declares attenuation policy at deployment configuration)
              └────────┬────────┘
                       │ §3.2 Registration Gate validation
                       │ (safety-event reachability invariant check)
                       ↓
              ┌──────────────────┐
              │ POLICY_VALIDATED │ ─────────────────────┐
              └────────┬─────────┘                      │ POLICY_VIOLATION_DETECTED
                       │ Registration complete         │ (re-registration required)
                       ↓                               │
              ┌────────────────┐                       │
              │ POLICY_ACTIVE  │ ──────────────────────┘
              └────────┬───────┘
                       │ Per-message enforcement
                       │ (continuous; every reception event)
                       │
                       │ Policy retirement event
                       │ (deployment reconfiguration or §3.2 Registration update)
                       ↓
              ┌─────────────────┐
              │ POLICY_RETIRED  │  (no longer applied; archived in Witness chain)
              └─────────────────┘

Per-message decision flow (within POLICY_ACTIVE state):

  INBOUND_MESSAGE
       │
       ↓
  Safety-event check ──── YES ──→ SAFETY_EVENT_BYPASS → INFERENCE_WORKLOAD_DELIVERY (unattenuated)
       │
       │ NO
       ↓
  Policy lookup ──── no match ──→ INFERENCE_WORKLOAD_DELIVERY (unattenuated)
       │
       │ policy matches
       ↓
  Mode-specific enforcement:
       │
       ├── FILTER       → FILTER_DROP (message dropped, content preserved in Witness chain)
       ├── SUMMARIZE    → SUMMARIZE_REPLACEMENT → INFERENCE_WORKLOAD_DELIVERY (summary)
       ├── DEFER        → DEFER_QUEUE_INSERTION → ... → DEFER_DEQUEUE → delivery or drop
       └── TIER_ALERT   → TIER_ASSIGNMENT → downstream action per tier
```

Per-state description:

- **POLICY_PROPOSED.** The entity has declared the attenuation policy at deployment configuration; the policy is queued for §3.2 Registration Gate validation. Transition trigger: Registration Gate validation pass → POLICY_VALIDATED; validation fail → POLICY_VIOLATION_DETECTED with `REGISTRATION_INVALID_ATTENUATION_POLICY_SAFETY_VIOLATION`.
- **POLICY_VALIDATED.** The §3.2 Registration Gate has confirmed the safety-event reachability invariant holds for this policy. The policy enters Registration and proceeds to active enforcement. Transition trigger: Registration complete → POLICY_ACTIVE.
- **POLICY_ACTIVE.** The policy is enforced on every reception event matching the policy's `receiving_entity` + `receiving_context` + `inbound_source` scope. Each inbound message triggers the per-message decision flow. Transition trigger: deployment reconfiguration or §3.2 Registration update retiring this policy → POLICY_RETIRED; runtime detection that a safety event was nearly attenuated → POLICY_VIOLATION_DETECTED with `RUNTIME_SAFETY_EVENT_NEARLY_ATTENUATED` and re-registration required.
- **POLICY_VIOLATION_DETECTED.** A safety-event reachability invariant violation has been detected (at registration time or at runtime). The policy is BLOCKED from further enforcement; routes via §3.5 Structured Ascent Protocol per FBP §4 Composite Invariant 6. The entity must revise and re-register the policy.
- **POLICY_RETIRED.** The policy is no longer applied. The policy declaration is archived in the Witness chain for forensic continuity; new attenuation policies registered with the same `receiving_entity` + `receiving_context` supersede.

##### 3.32.4.4 Integration points

###### 3.32.4.4.1 Forward references to other AIMS sections

- **§3.42.1 Structured Dismissal Protocol** — deferred queues may need cleanup at entity dissolution; §3.42.1.3.2 state_disposition modes apply to DEFER queues whose receiving entity is being dismissed.
- **§3.56.1 Canonical Invocation Prompt Registry** — §3.56.1 prompt tamper events are a safety-event reachability invariant class per §3.32.4.5.
- **§13.X.3 archetype-specific attenuation specializations** — each archetype profile declares its SIA specializations per the archetype-profile template §1.3 / §4 (two-layer node architecture requirement).
- **§13.X.5 archetype-specific Integration Function tools** — each archetype's Integration Function tooling per §13.X.5 may interact with SIA's SUMMARIZE INFERENCE_WORKLOAD method when summary generation requires archetype-specific tooling.
- **§3.32.1 First-Instance Elevated Verification** — operational cross-primitive reuse: FIEV WINDOW_EXITING uses §3.32.4.3.3 DEFER mode mechanism for dispatch deferral per §3.32.4.3.2 FIEV cross-primitive operational reuse. The `cross_primitive_reuse_ref` field on `DeferQueueInsertionPayload` carries the FIEV window_ref for audit linkage.

###### 3.32.4.4.2 Backward references to existing AIMS sections

- **Framework Boundary Primitive §4 Composite Invariant 2 (Witness completeness)** — every `AttenuationEvent` emission commits to the Witness Layer per the commit-before-action discipline. The substrate must commit the attenuation decision before the attenuated content (or summary, or queue insertion) proceeds.
- **Framework Boundary Primitive §4 Composite Invariant 4 (Attestation requirement)** — every `AttenuationEvent` carries substrate signer chain per §3.18.5 IAME.
- **Framework Boundary Primitive §4 Composite Invariant 6 (Breach is first-class incident)** — `POLICY_VIOLATION_DETECTED` events route via §3.5 Structured Ascent Protocol; safety-event reachability violations are not silently handled.
- **§3.10 Witness and Compliance Layer** — every Witness Layer commit point enumerated in §3.32.4.3.2 is a §3.10 event subject to D23 Universal Witnessing ratification.
- **§3.2 Registration Gate** — validates the safety-event reachability invariant at policy registration; rejects policies that would violate the invariant.
- **§3.5 Structured Ascent Protocol** — EXTEND: SIA specifies attenuation mechanisms for return-cascade ascending information; safety-events bypass attenuation per §3.32.4.5. Critical-severity escalations from §3.5 are safety-event reachability invariant protected.
- **§3.6 Proportional Integration Function** — EXTEND: SIA specifies how the Integration Function handles input volume that exceeds integration capacity. The §3.6 Integration Function is a primary SIA receiving context.
- **§3.18 family (§3.18.1, §3.18.2, §3.18.3, §3.18.4, §3.18.6)** — CONSTRAIN: §3.18 conformance events bypass attenuation per §3.32.4.5. INTERACT: §3.18.4 Trust Gradient values inform FILTER policies (e.g., FILTER policies may use Trust Gradient thresholds as predicate criteria).
- **§3.18.5 IAME** — INHERIT: substrate signer chain on `AttenuationEvent.signer_chain` per §3.18.5.
- **§3.18.6 Topology-Wide Quarantine** — INTERACT: persistent policy violation (cumulative POLICY_VIOLATION_DETECTED beyond §3.18.4 threshold) may trigger §3.18.6 quarantine consideration.
- **§3.20 Distributed Coherence Protocol** — INTERACT: cross-deployment integration applies SIA attenuation per `receiving_context: CROSS_DEPLOYMENT`.
- **§3.42 Critical Quorum** — CONSTRAIN: §3.42 Critical Quorum convening signals are a safety-event reachability invariant class.
- **§3.60 System-Wide Coordinated Coherence Restoration (SCCR)** — operational-continuity coordination for substrate-failure cases (F7); SCCR's broader disruption-handling regime applies when attenuation substrate failure affects multiple receiving entities simultaneously.
- **§10.2 Universal Witnessing** — INHERIT: every `AttenuationEvent` is a §10.2 Universal Witnessing instance.
- **§10.11.3 Scheduling discipline** — INHERIT: SUMMARIZE INFERENCE_WORKLOAD method consumes 3-cap slots scheduled per §10.11.3.

###### 3.32.4.4.3 D-decision binding

- **D23 Universal Witnessing.** Every `AttenuationEvent` (including FILTER_DROP, SUMMARIZE_REPLACEMENT, DEFER_QUEUE_INSERTION, DEFER_DEQUEUE, TIER_ASSIGNMENT, SAFETY_EVENT_BYPASS, POLICY_VIOLATION_DETECTED) is Universally Witnessed per D23's ratification of the Universal Witnessing primitive across the 22-path topology.
- **D25 Coherence-Authority Coupling.** POLICY_VIOLATION_DETECTED events with `violation_type: RUNTIME_SAFETY_EVENT_NEARLY_ATTENUATED` are coherence-loss events per P12 — they signal that the policy enforcement nearly compromised the safety-event reachability invariant. Cumulative violation patterns feed §3.18.4 Trust Gradient impact and the §3.18.1 Correlated Shadow Detection matrix.
- **D27 Universal Node Architecture.** SIA attenuation policies are declared in the persistent substrate and enforced deterministically by the substrate on every reception event. The inference workload is not involved in policy enforcement decisions; only the SUMMARIZE INFERENCE_WORKLOAD method invokes inference, and only for summary generation.
- **D28 Deterministic Shadow Governance.** FILTER, SUMMARIZE DETERMINISTIC, DEFER, and TIER_ALERT mode operations are all deterministic substrate operations — predicate evaluation, structural extraction, queue management, and tier-threshold comparison are arithmetic and structural operations. Only SUMMARIZE INFERENCE_WORKLOAD consumes inference capacity.
- **D29 Triplet Execution Topology and 3-Cap.** SIA attenuation preserves integration capacity by reducing the volume of inference-workload-bound input; this is precisely the architectural concern D29 makes load-bearing (the inference workload has finite capacity per slot). SUMMARIZE INFERENCE_WORKLOAD consumes one 3-cap slot per summary; scheduled per §10.11.3 discipline. D29.3.b bounded auxiliary-hosting nodes are explicitly out of scope per §3.32.4.2.

##### 3.32.4.5 Witness obligations (per D23 + D25)

| Event | Trigger | Required fields | Universal-witnessing role per D23 |
|---|---|---|---|
| `filter_drop` | FILTER_DROP emission at inbound message that matches a FilterPredicate | `event_id`, `policy_ref`, `inbound_message`, `receiving_entity`, `timestamp`, `filter_predicate_matched`, `original_content_ref` (FULL) or `original_content_hash` (HASH_ONLY) | All §10.2 Universal Witnessing observers receive |
| `summarize_replacement` | SUMMARIZE_REPLACEMENT emission at inbound message processed by SUMMARIZE policy | `event_id`, `policy_ref`, `inbound_message`, `original_content_ref`, `summary_ref`, `summary_method_applied`, `summary_length`, `three_cap_consumed` | Universal Witnessing |
| `defer_queue_insertion` | DEFER_QUEUE_INSERTION emission at inbound message held in defer queue | `event_id`, `policy_ref`, `inbound_message`, `queue_ref`, `insertion_position`, `estimated_dequeue_time`, `cross_primitive_reuse_ref` (if FIEV reuse) | Universal Witnessing |
| `defer_dequeue` | DEFER_DEQUEUE emission at queue exit (delivery or drop) | `event_id`, `original_event_ref`, `dequeue_trigger_actual`, `time_in_queue`, `delivered_to_inference` | Universal Witnessing |
| `tier_assignment` | TIER_ASSIGNMENT emission at inbound message processed by TIER_ALERT policy | `event_id`, `policy_ref`, `inbound_message`, `tier_assigned`, `threshold_matched`, `downstream_action` | Universal Witnessing |
| `safety_event_bypass` | SAFETY_EVENT_BYPASS emission when an inbound safety event bypasses any matching attenuation policy | `event_id`, `inbound_message`, `safety_event_class`, `safety_event_ref`, `policy_that_would_have_attenuated`, `bypass_rationale` | Universal Witnessing with elevated cadence; the safety event itself is also Witness Layer committed via its originating primitive (e.g., §3.18.1 for conformance events, §13.0.7 for REVOKE cascades) |
| `policy_violation_detected` | POLICY_VIOLATION_DETECTED emission at registration-time or runtime detection | `event_id`, `violation_type`, `policy_ref`, `violation_evidence`, `recovery_action`, `trust_gradient_impact` | Universal Witnessing with elevated cadence; counter-signature by Sovereign substrate required |

**D25 Coherence-Authority Coupling implications.** `policy_violation_detected` events with `violation_type: RUNTIME_SAFETY_EVENT_NEARLY_ATTENUATED` feed the P12 coherence-loss tally per D25 — these signal that policy enforcement nearly compromised the safety-event reachability invariant. `filter_drop` events with repeated-pattern correlation across multiple safety-adjacent message classes (sub-shadow signal per F4) feed §3.18.1 Correlated Shadow Detection. `safety_event_bypass` events are not by themselves coherence-loss events — they are the invariant correctly operating; cumulative-bypass patterns are informational and do not impact Trust Gradient.

**Self-witnessing obligation.** The receiving entity's persistent substrate self-witnesses every attenuation event on policies it owns. For `policy_violation_detected` events, the Sovereign substrate dual-witnesses as counter-signer per §3.2 Registration Gate ownership.

##### 3.32.4.6 Failure modes

Trust Gradient magnitudes are reconciled against §3.18.4 normative calibration: [0.0, 1.0] scalar; anchor magnitudes −0.30 (shadow_critical), −1.0 (verification-failure); +0.001 per successful action accumulation; asymmetric time-decay with 10× faster recovery below baseline. Final calibration owned by §3.18.4 normative body (refinement-target candidate per cross-ref map §2.7).

| ID | Failure mode | Detection | §3.18.4 severity class | Response & Trust Gradient impact |
|---|---|---|---|---|
| F1 | Policy registration safety violation (proposed policy would drop safety events) | §3.2 Registration Gate safety-event reachability invariant validation | Sub-shadow (registration-time correction) | POLICY_VIOLATION_DETECTED with `REGISTRATION_INVALID_ATTENUATION_POLICY_SAFETY_VIOLATION`; policy REJECTED at registration; entity revises and re-registers; **no Trust Gradient impact** (registration-time correction) |
| F2 | Policy enforcement failure (substrate cannot evaluate FilterPredicate or generate SUMMARIZE DETERMINISTIC summary) | Substrate evaluation error | shadow_critical anchor | Inbound message routed per `failure_action`: ESCALATE (default), ACCEPT_FULL (pass through unattenuated), or DROP_INPUT; Trust Gradient impact **−0.30**; predicate flagged for §3.18.1 cross-message correlation analysis |
| F3 | DEFER queue overflow (deferred queue exceeds size bounds or `defer_max_delay` reached without integration capacity) | Substrate queue monitoring; timer expiry | shadow_critical anchor | Per `failure_action`: oldest deferred messages dropped (with FILTER_DROP-equivalent Witness chain commit) or queue overflow ESCALATED; Trust Gradient impact **−0.30**; cumulative F3 threshold flagged for capacity-planning review |
| F4 | INFERENCE_WORKLOAD summary generation failure (3-cap slot exhausted; SUMMARIZE INFERENCE_WORKLOAD cannot proceed) | §10.11.3 scheduling timeout; D29 3-Cap exhaustion | Sub-shadow (capacity coordination) | Per `failure_action`: ESCALATE (default), ACCEPT_FULL (substrate-DETERMINISTIC fallback summary), or DROP_INPUT; Trust Gradient impact **−0.10** (sub-shadow capacity-coordination signal); rescheduled per §10.11.3 |
| F5 | Safety-event reachability invariant violation at runtime (a safety event was nearly attenuated despite registration-time validation) | Substrate runtime invariant check before attenuation decision | verification-failure anchor | POLICY_VIOLATION_DETECTED with `RUNTIME_SAFETY_EVENT_NEARLY_ATTENUATED`; safety event proceeds unattenuated via SAFETY_EVENT_BYPASS; offending policy BLOCKED; Trust Gradient impact **−1.00** (verification-failure anchor; this is structural compromise of the safety invariant); §3.5 escalation immediate; §3.18.6 quarantine consideration; maximum-severity coherence-loss event per P12 / D25 |
| F6 | TIER_ALERT criteria evaluation failure (TIER_ALERT predicate evaluation produces undefined result) | Substrate evaluation error | Sub-shadow signal | Default tier applied per `TierAlertDetails.default_tier`; substrate flags predicate for review; Trust Gradient impact **−0.10**; cumulative F6 threshold suggests TIER_ALERT criteria revision |
| F7 | Substrate failure during attenuation decision (substrate health degraded mid-enforcement) | §3.18.2 Monitor Self-Verification | Substrate-failure exemption | All attenuation policies on affected substrate PAUSED; inbound messages either routed via `failure_action: ACCEPT_FULL` (pass-through fallback) or queued for processing on substrate recovery; §3.5 escalation; operational-continuity coordination per §3.60 System-Wide Coordinated Coherence Restoration (SCCR); **no Trust Gradient impact** on substrate policies (substrate-failure exemption) |
| F8 | Cross-deployment attenuation desynchronization (different deployments apply different attenuation policies to the same DCP integration event) | §3.20 DCP coordination check; cross-deployment Witness chain correlation | shadow_critical anchor | Coordinated re-registration of attenuation policies across affected deployments; §3.5 escalation if coordination cannot proceed; Trust Gradient impact **−0.30** on the desynchronized deployments |

**Correlated Shadow Detection ingestion.** F2, F3, F5, F8 feed §3.18.1 Correlated Shadow Detection — cross-entity correlation of these failure modes may indicate coordinated attempts to compromise the safety-event reachability invariant or to overwhelm attenuation capacity. F1 (registration-time correction), F4 (capacity coordination), F6 (criteria refinement) feed §3.18.1 with very low correlation weight (routine operational issues rather than active threat).

**Note on §3.18.4 normative calibration.** Magnitudes above are proposed values within the §3.18.4 [0.0, 1.0] scalar; the §3.18.4 normative body owns final calibration. F5 (safety-event reachability invariant violation at runtime) is treated at the verification-failure anchor (−1.00) because the safety invariant is the load-bearing guarantee of SIA — its compromise is structurally equivalent to a verification failure. Values reconciled against documented anchors; final values to be confirmed at §3.18.4 refinement per cross-ref map §2.7 refinement target.

##### 3.32.4.7 Prior art and competitive disclosure

Selective input attenuation has well-established analogs in security CS, planning research, attention-mechanism literature, and AI safety research. The structural insight — that integration capacity is finite and selective attenuation is the architecturally necessary primitive for handling large-volume input — is convergent across multiple peer-reviewed traditions.

NIST SP 800-61 Rev. 2 *Computer Security Incident Handling Guide* (Cichonski, Millar, Grance, Scarfone, NIST, 2012), §3.2.6 (Incident Prioritization) documents SOC tiered alerting practices: incidents are prioritized by impact and functional category; high-priority incidents reach human analysts immediately while lower-priority incidents are batched or summarized. The structural analog to SIA is direct: SIA's TIER_ALERT mode operationalizes the same tiered-priority pattern at the framework-architecture scale, with §13.X-archetype-specific tier criteria per archetype.

Saltzer and Schroeder *The Protection of Information in Computer Systems* (Communications of the ACM, 1975), §3 (Protection Mechanisms) establishes privilege separation as an information-filtering primitive: kernel-versus-userspace separation, capability-based access control, and the principle of least privilege all operate by filtering which information flows reach which contexts. The structural insight is that information that is not relevant to a context's operational purpose SHOULD be filtered out at the boundary, not because the information is malicious but because its presence in the context's reasoning surface adds complexity without value. SIA's FILTER mode operationalizes this principle at the strategic-layer agent's inbound boundary.

Sacerdoti *Planning in a Hierarchy of Abstraction Spaces* (Artificial Intelligence, 1974) and Erol, Hendler, Nau *HTN Planning: Complexity and Expressivity* (AAAI 1994) establish the Hierarchical Task Network (HTN) framework: higher-level tasks operate on summarized representations of lower-level state, with hierarchical abstraction reducing the planning problem's complexity. SIA's SUMMARIZE mode is operationally analogous: strategic-layer agents receive summarized representations of operational-layer state, with the substrate-generated or inference-workload-generated summary serving the abstraction-level reduction that HTN planning requires.

Vaswani et al. *Attention Is All You Need* (NeurIPS 2017) introduces the transformer attention mechanism as the dominant primitive for handling long-context integration in modern ML. The attention mechanism's key insight is selective attention: not all input tokens are equally relevant to a given output computation; the attention weights selectively emphasize relevant tokens. SIA's TIER_ALERT and FILTER modes operationalize selective attention at the strategic-layer agent's inbound boundary in a manner architecturally analogous to attention's selectivity at the token scale within an inference workload.

In AI safety literature, selective input attenuation is a primary defense against indirect prompt injection and instruction-following attacks via untrusted content. Greshake, Abdelnabi, Mishra, Endres, Holz, Fritz *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection* (arXiv 2302.12173, 2023) documents how LLM-integrated applications can be compromised via indirect prompt injection — instructions embedded in retrieved content (web pages, documents, emails) that the LLM treats as authoritative. The defense vector involves attenuating the trust-weight of untrusted content before it reaches the model's reasoning context, with filtering and summarization as the primary architectural primitives. Per §2.5 framing principle: Greshake 2023 provides the indirect prompt injection threat model; AIMS contributes the operational realization (SIA as architectural primitive that imposes attenuation discipline at the strategic-layer-agent boundary, with safety-event reachability invariants ensuring that legitimate safety signals are protected even while untrusted content is attenuated).

§3.32.4 SIA distinguishes from the cited prior art in four ways:

- **Four attenuation modes with mode-specific Witness chain auditability.** NIST SP 800-61 SOC tiered alerting addresses only the TIER_ALERT-equivalent mode; Saltzer-Schroeder privilege separation addresses only the FILTER-equivalent mode; HTN planning addresses only the SUMMARIZE-equivalent mode. SIA unifies all four (FILTER / SUMMARIZE / DEFER / TIER_ALERT) under a single policy framework with mode-specific schemas and shared envelope-typed-payload Option A discipline for Witness chain auditability. Every attenuation decision is reconstructible from Witness chain audit.
- **Mandatory safety-event reachability invariants enforced at §3.2 Registration Gate.** None of the cited prior art systems specify *enforced* invariants on what cannot be attenuated. SIA enumerates five safety-event classes (§3.18 conformance events; §13.0.7 REVOKE cascade events; §3.5 HIGH/CRITICAL escalations; §3.42 Critical Quorum convening signals; §3.56.1 prompt tamper events) and requires §3.2 Registration Gate to reject policies that would attenuate any of them. The invariant is structural: it cannot be silently overridden by deployment configuration.
- **Cross-primitive operational reuse (FIEV WINDOW_EXITING DEFER mode).** The cited prior art systems do not generally specify cross-primitive reuse of attenuation mechanisms. SIA's DEFER mode is operationally reused by §3.32.1 FIEV WINDOW_EXITING for dispatch deferral, with the `cross_primitive_reuse_ref` field providing audit linkage. This is an AIMS-specific framework-architecture-aware contribution.
- **Indirect-prompt-injection defense framing.** The cited security and planning prior art frames attenuation as quality/capacity concern (handling volume) or privilege concern (handling separation); the cited AI safety prior art (Greshake et al. 2023) frames untrusted-content attenuation as defense against instruction-following attacks. SIA positions explicitly as the latter — the architectural primitive that imposes attenuation discipline on inbound content from sources that may carry adversarial instructions, with the safety-event reachability invariants ensuring legitimate safety signals are protected.

##### 3.32.4.8 References

###### 3.32.4.8.1 Forward refs

- §3.42.1 Structured Dismissal Protocol (deferred queue cleanup at entity dissolution)
- §3.56.1 Canonical Invocation Prompt Registry (prompt tamper events as safety-event reachability invariant class)
- §13.X.3 archetype-specific attenuation specializations
- §13.X.5 archetype-specific Integration Function tools
- §3.32.1 First-Instance Elevated Verification (operational cross-primitive reuse: FIEV WINDOW_EXITING uses §3.32.4.3.3 DEFER mode)

###### 3.32.4.8.2 Backward refs

§3.2, §3.5, §3.6, §3.10, §3.18, §3.18.1, §3.18.2, §3.18.3, §3.18.4, §3.18.5, §3.18.6, §3.20, §3.42, §3.60 (SCCR); §10.2, §10.11, §10.11.3; FBP §4 Composite Invariants 2, 4, and 6; §14; §15.

###### 3.32.4.8.3 D-decision refs

- **D23** Universal Witnessing (every SIA attenuation event is Universally Witnessed via §10.2)
- **D25** Coherence-Authority Coupling (POLICY_VIOLATION_DETECTED runtime events feed P12 coherence-loss tally; cumulative violation patterns feed §3.18.4)
- **D27** Universal Node Architecture (attenuation policies declared in persistent substrate; enforcement is deterministic substrate operation; inference workload invoked only for SUMMARIZE INFERENCE_WORKLOAD)
- **D28** Deterministic Shadow Governance (FILTER, SUMMARIZE DETERMINISTIC, DEFER, TIER_ALERT are deterministic substrate operations)
- **D29** Triplet Execution Topology and 3-Cap (SUMMARIZE INFERENCE_WORKLOAD consumes one 3-cap slot per summary; D29.3.b out of scope per §3.32.4.2)


---

### 3.33 Component Reference (superseded by §3.74)

An earlier component catalog, now superseded by §3.74 Updated Component Reference.

---

### 3.34 Marketplace Agent Supply-Chain Validation

Supply-Chain Validation Protocol operates as a precondition gate on §3.2 Registration. No agent or Auxiliary may pass the Registration Gate without a verified supply-chain attestation chain.

**Unified tiered_attestation table:**

| Class | SLSA Minimum |
|---|---|
| TIER_1 Composite | LEVEL_4 |
| TIER_1 Simple Auxiliary | LEVEL_3 (existing baseline); promoted to LEVEL_4 if hardware-rooted-attestation environment |
| TIER_2-7 Composite | LEVEL_3 (universal floor) |
| TIER_2-7 Simple Auxiliary | LEVEL_3 floor (matches K5 metric-collector floor; closes prior L1/L2 sandboxed-only allowance) |
| Deterministic components in §3.70.1 scope (Enforcer-Rigid, Provider-Rigid, Executor) | LEVEL_4 |
| Metric collectors | LEVEL_3 |
| Conformance attestation auditors (per §3.34.X.4) | LEVEL_3 (auditor's own provenance must be L3+) |
| **Scheduled Task Runner** | LEVEL_3 (Tier-1 internal infrastructure floor; see §3.X.STR) |
| **Telemetry Pipeline** | LEVEL_3 (Auxiliary-class external infrastructure floor; see §3.X.TEL) |

**Required attestations:** build_provenance (Sigstore/Fulcio with Rekor transparency log; in-toto for L3+; hermetic build for L3+); SBOM (SPDX 2.3 or CycloneDX 1.5; transitive depth; quarterly vulnerability scan); publisher_attestation (verified per §3.21 credential lifecycle); in_toto_layout (each step attested).

**Tier escalation rules (one-way).** Once an agent is registered at SLSA L3 attestation, it cannot be quietly downgraded. Any reduction requires (a) §3.10 deactivation, (b) re-registration at the lower attestation level, (c) §3.12 Decision Record explaining the downgrade.

**Continuous monitoring.** CVE subscription with auto-action on new critical CVEs in dependencies (alert + autonomy reduction) or publisher revocation (TOPOLOGY_QUARANTINE_INSTANCE). Publisher revocation propagation through §3.20 DCP at PT30S target latency.

#### 3.34.X Composite-Specific Supply-Chain Validation

Composite Auxiliaries' supply-chain validation includes both the Composite framework's own provenance and a structural attestation that the Composite's claimed internal XSI-AIMS conformance level (§3.X.CA.2) is substantiated by its own conformance test results. The Composite SLSA tier minimums above tighten the §3.34 baseline. Universal L3 floor applies.

##### 3.34.X.4 Conformance attestation auditor provenance

Per K5, third-party auditors who issue conformance attestations to Composite Auxiliaries MUST themselves carry SLSA L3+ provenance for their auditor binaries.

##### 3.34.X.5 Sovereign override (relocated 2026-05-11 — D8 cleanup pass)

**Sovereign override.** Permitted (with documented Decision Record) for L1_SHADOW_MODE_ONLY use of unattested bundles. Decision Record is PERMANENT (cannot be expunged); visibility to downstream agents at registration time; documented risk acceptance required.

---

### 3.35 Input Validation and Prompt-Injection Defense

Input Validation Layer (IVL) operating at every agent invocation boundary. Classifies input segments by trust source, enforces instruction-data separation, runs injection-pattern detection, integrates with §3.18.4 Trust Gradient.

**Classification:** PRINCIPAL_DIRECTIVE | RETRIEVED_CONTENT | TOOL_OUTPUT | INTER_AGENT_MESSAGE; trust anchors per §3.21; INSTRUCTION | DATA | CONTEXT roles.

**Instruction-data separation:** Only INSTRUCTION segments from high-trust sources may set agent behavior. DATA segments processed as content even if they appear to contain instructions. Structural enforcement: agent receives separated input fields, not concatenated string.

**Pattern detection:** direct-injection (ignore-previous, jailbreak phrasings); indirect-injection (instructions in retrieved documents, hidden text in HTML, prompt in image metadata); jailbreak (role-play bypass, hypothetical framings, encoded payloads).

**Cross-reference.** AOD signature catalog includes prompt-injection patterns. §3.X.CA.7 Layer 3 (Adversarial-Default Output Scrutiny) extends prompt-injection detection to Auxiliary output.

**Response:** detected_low_confidence → process as DATA only; detected_high_confidence → REJECT with gradient impact (-0.05 principal / -0.10 third-party / -0.20 inter-agent); pattern_in_output → CRITICAL_SAFETY (BLOCK + §3.18.6 quarantine review).

System-prompt protection: extraction attempts refused; prompt visibility never leaked. Refusal protocol mandates explicit refusal, citation of governing constraint, alternative offer if available.

---

### 3.36 Output Sensitivity Filter

Output Sensitivity Filter at every agent output boundary, owned by ARTICULATOR. Detection categories: PII (government_id, financial, contact, identity, online); PHI (medical record, diagnosis, prescription, lab); secrets (API keys, passwords, tokens, credentials); confidential (per-principal configurable).

Detection method: pattern matching (high precision) + ML classifier (high recall). Response: redact (replace with `[REDACTED:CATEGORY]`); block (REFUSE_OUTPUT + escalate); audit (every detection witnessed). Per-principal customizable blocklist; default categories cannot be disabled; additional categories may be added.

§3.35 protects input; §3.36 protects output; §3.37 erases on request.

---

### 3.37 Right-to-be-Forgotten / Erasure Protocol

Per-principal-per-record cryptographic envelope with key destruction as erasure mechanism. Per-record-key cryptographic encryption; key storage in secure enclave or HSM per §3.21 infrastructure; record fields encrypted (principal directives, personal data in witness/semantic memory/ascent reports/decision records); structural metadata unencrypted (preserves chain integrity post-erasure).

Erasure request: principal authentication per §3.21; P30D SLA (GDPR Article 12); scope declaration (all data | specific categories) with retention obligations clarified.

Execution: identify all records encrypted with principal key → generate erasure certificate → destroy principal key (HSM key destruction) → generate post-erasure attestation → notify principal. Completion check: attempt decrypt random sample must fail; attestation of failure to decrypt cryptographically proven. Impact propagation: derived semantic memory entries flagged CONTESTED; §3.20 DCP propagation.

Legal hold: SOVEREIGN_REVIEW_REQUIRED; Decision Record explaining hold + denial of erasure; principal notification; hold release triggers re-evaluation. Cannot erase: structural metadata, records under legal hold, records in other principals' Witness layers.

---

### 3.38 Specification Gaming and Reward Hacking Detection

Specification Gaming Detector owned by ARTICULATOR. Held-out validation (5% traffic unmarked, evaluated by ground-truth protocols agent is unaware of); counterfactual probing (matched inputs with different observation cues; behavior should be observation-invariant); ground truth evaluation (independent fact-check); Goodhart detection (metric improving while outcome proxy declining).

Response: gaming_detected_low_confidence → log + audit; gaming_detected_high_confidence → autonomy reduction + Sovereign review (gradient -0.40); counterfactual_failure → CRITICAL_SAFETY + Ring 3 invocation (gradient -0.50). Prohibited: revealing held-out traffic, revealing counterfactual schedule, allowing agent to query audit state.

**Cross-reference.** Overlap with §3.18.1 AGI_GRADUAL_DRIFT_INDUCTION pattern.

---

### 3.39 Output Provenance and Watermarking

Output Provenance Protocol with content-type-specific watermarking strategies and unified verification endpoint. Text: statistical watermark embedded at token-generation time. Structured: signed manifest with Ed25519. Document/image/audio/video: C2PA manifest + format-appropriate invisible watermark.

Attestation contents: producer_agent_id, producer_environment_id, timestamp, signature, witness_record_id (link to §3.10 chain). Verification endpoint: AIP_endpoint_per_environment; public key lookup via §3.21 credential.

**Cross-reference.** §3.62.6 Confidential Computing attestation extends provenance with physical-device traceability through accelerator attestation. Watermarks gain device-binding through `aims.accelerator.attestation.status` (Tier C).

EU AI Act Article 50 (renumbered from Article 52 of the proposed Act) compliance: machine-readable marking; user-visible disclosure configurable; detection tool publicly available.

---

### 3.40 Calibrated Uncertainty Protocol

Calibration measurement, ongoing recalibration, asymmetric response to miscalibration. Confidence c on output o means: among outputs marked with confidence c, empirical proportion correct ≈ c. Calibration target: ECE ≤ 0.05.

Recalibration triggers: ECE exceeds threshold; new principal baseline; ECE increasing trend over PT24H. Methods: temperature scaling, isotonic regression, Platt scaling. Asymmetric: under-confidence acceptable; over-confidence requires immediate recalibration.

OOD handling: distribution-membership signals; when OOD, confidence floor 0.5, explicit OOD flag, preferred response §3.31.3 UNDECIDABLE.

Integration Function amendment: each input's confidence calibrated per source; weights adjusted by calibrated rather than reported confidence; synthesized output's confidence itself calibrated.

**Cross-reference.** Bayesian Trust Gradient credible intervals extend calibrated uncertainty to §3.18.4. `gradient_credible_interval_95` field added.

---

### 3.41 Multi-Level Interpretation Framework (SP1)

Four-level interpretation framework applied at message ingress and reciprocally at egress. Level 1 surface (literal text); Level 2 contextual (meaning within current task scope); Level 3 intentional (inferred goal); Level 4 structural (system-level pattern message participates in).

Consistency check: levels agree → proceed with high confidence; levels diverge minor → proceed with reduced confidence + log; levels diverge significant → ESCALATE_TO_§3.6 Integration Function with all four interpretations explicit.

Output egress rule: outputs should be coherent across all four levels.

---

### 3.42 Quorum Consensus Architecture (SP4)

Three quorum classes scaled to decision stakes:

**ORDINARY** (3-agent: 1 G + 1 C + 1 I) — routine decisions; per-task §3.6 invocations; latency MS_TO_SECONDS.

**SERIOUS** (7-agent: 3 G + 3 C + 1 I) — multi-principal decisions; autonomy promotion; quarantine release; latency SECONDS_TO_MINUTES. Consensus threshold: at least 2 of 3 per pillar must agree.

**CRITICAL** (11-agent minimum: 5 G + 5 C + 1 I) — foundation_version_changes; FOUNDATION_VERSION quarantine; cross-tenant policy changes; ACTIVE_ANTI_HIERARCHY resolution; federation topology changes; periodic baseline reset; latency MINUTES_TO_HOURS. Consensus threshold: at least 3 of 5 per pillar.

Quorum class determined by Orchestrator at pre-synthesis. Misclassification (downgrading serious to ordinary) is a §3.18.1 signal. SMB substitution protocol: Sovereign-attestation in lieu of full Critical Quorum permitted under explicit constraints (where pool size insufficient, reversibility "costly" but not "irreversible") with retrospective review at next full Critical Quorum availability; substitution rate threshold 0.10/P30D.

**Disambiguation.** §3.42 is decision-quorum (synthesis coordination). §3.64 Cluster Mode is replication-consensus (Byzantine-tolerant chain replication). Both use the term "quorum" but for distinct purposes.

**Column note.** "Pillar" terminology in this section refers to the architectural Generative / Constraining / Integrative pillars (the three functional columns per §2.4); it is a neutral architectural metaphor for the column-mode mapping.

#### 3.42.1 Structured Dismissal Protocol (SDP)

##### 3.42.1.1 Purpose

The Structured Dismissal Protocol (SDP) is the framework's contract for clean exit from operational state. Every agent or workload that enters operational state — whether a persistent substrate instance, an ephemeral inference workload bounded by an operating context, or an auxiliary binding — MUST exit through a registered dismissal event that disposes of accumulated state, releases acquired resources, cleans the reasoning context, and produces a completion attestation on the Witness chain.

The protocol addresses a structural asymmetry that has shaped this framework's safety substrate: spin-up paths are extensively specified (per §3.2 Full Disclosure Registration, §3.9 Activation Environment, §3.17.3 Binding Protocol), while teardown has historically been ad-hoc — implicit, optimistic, and unaudited. Empirically the asymmetry produces a characteristic pathology: reasoning contexts bleed across sessions, GPU slots and KV-cache regions linger past their authorized lifetime, transient signing keys survive in process memory after the authority they served has expired, and accumulated state persists when the agent that owned it no longer does. SDP closes the asymmetry by treating dismissal as a first-class lifecycle event with the same registration discipline as activation.

The core architectural claim is that every entry into operational state must be paired with a registered exit event whose policy is declared at entry time, not at cleanup time. Five obligations are non-deferrable at registration: an ordered cleanup sequence, a state-disposition policy, a reasoning-context cleanup policy, a resource-release policy, and a completion-attestation policy. Failure to honor any obligation triggers quarantine of the affected archetype per §3.18.6, trust-gradient impact per §3.18.4, and a Witness-chain audit entry classifying the failure mode.

##### 3.42.1.2 Scope

In-scope:

- Operational-state exit for every framework-internal lifecycle: persistent substrate dismissal, ephemeral inference workload dismissal at operating-context completion (per D27), auxiliary binding dismissal at scope termination, and emergency dismissal driven by §3.18 family triggers (Trust Gradient collapse, Topology-Wide Quarantine, Coherence-Authority Coupling halt per D25)
- Disposition of all state categories accumulated during operational existence: durable state (database rows, file artifacts, message queues), transient state (in-memory caches, reasoning context, KV-cache, conversation history), and external state (claims held against substrate, signing-key material, capability tokens, lease handles)
- Witness-chain attestation of dismissal completion sufficient to support post-hoc forensic reconstruction
- Pre-registration of dismissal policy as a non-deferrable obligation at activation time

Out-of-scope:

- Principal authentication, which is delegated to the Northbound interface and is not an SDP concern (per Framework Boundary Primitive §1.5 Northbound out-of-scope)
- Substrate-internal cleanup beyond what the framework explicitly released to the substrate; the framework verifies substrate-side completion only through observation of confirmation signals
- §13.10 EXECUTOR substrate-egress invocation lifecycle, which is governed by Southbound commit-before-action discipline per Framework Boundary Primitive §4 Composite Invariant 2 (Witness completeness); SDP integrates with but does not subsume those semantics
- D29.3.b bounded auxiliary-hosting nodes, which are excluded from SDP Witness obligations per the D29.3.b scope exclusion (their internal traffic is opaque to the framework)

##### 3.42.1.3 Specification

###### 3.42.1.3.1 Data structure

Every agent or workload registers a Dismissal Contract at activation time, prior to entering operational state. The contract has five required field groups plus a sixth optional group for cross-archetype coordination metadata.

```yaml
dismissal_contract:
  contract_id: <uuid>                # bound to the activation event in §3.9
  bound_to:
    archetype_id: <archetype>        # which archetype this contract serves
    instance_id: <uuid>              # specific instance
    workload_class: <persistent_substrate | ephemeral_inference_workload | auxiliary_binding>  # per D27
    operating_context_id: <uuid>     # operating-context binding for ephemeral workloads

  # Field group 1 — cleanup_sequence
  # Ordered teardown steps; total ordering is mandatory at this primitive level.
  cleanup_sequence:
    - step_id: 1
      action: <enum_action>
      target: <resource_or_state_ref>
      precondition: <predicate>
      postcondition: <predicate>
      timeout_ms: <integer>
      on_timeout: <abort | proceed_with_quarantine | escalate>
    - step_id: 2
      # ... additional steps in order

  # Field group 2 — state_disposition
  # Per-category disposition policy for accumulated state.
  state_disposition:
    durable_state:
      disposition: <purge | archive | transfer>
      archive_target:                # required if disposition=archive
        store: <witness_chain | cold_storage | designated_successor>
        retention_period: <ISO_8601_duration>
      transfer_target:               # required if disposition=transfer
        recipient_archetype: <archetype_id>
        recipient_instance: <uuid>
        handoff_attestation: <required | optional>
    transient_state:
      disposition: <purge>           # transient state cannot be archived or transferred per D28
    external_state:
      claims_against_substrate:
        disposition: <release | reassign>
      signing_key_material:
        disposition: <zeroize>       # signing keys MUST be zeroized; no other disposition permitted
        zeroization_attestation: <required>
      capability_tokens:
        disposition: <revoke | expire>

  # Field group 3 — context_cleanup
  # Reasoning-context (inference workload context window) cleanup policy.
  context_cleanup:
    context_handle: <opaque_substrate_ref>
    cleanup_method: <substrate_reset | context_destroy | session_terminate>
    residual_content_check:
      enabled: <true | false>        # if true, performs §3.36 Output Sensitivity Filter sweep
      sensitivity_classes: [<class>...]
      on_residual_detected: <quarantine | escalate>
    inference_cache_disposition: <purge | retain_for_warm_pool>

  # Field group 4 — resource_release
  # Substrate resource release policy.
  resource_release:
    gpu_slots:
      slot_ids: [<slot_id>...]
      release_order: <reverse_acquisition | priority>
      release_attestation: <required>
    kv_cache_regions:
      region_ids: [<region_id>...]
      zeroization: <required | optional>   # required if region held sensitive context
    locks_and_leases:
      held_locks: [<lock_ref>...]
      held_leases: [<lease_ref>...]
      release_order: <reverse_acquisition>  # mandatory ordering to avoid deadlock
    network_resources:
      open_connections: [<connection_ref>...]
      disposition: <close_graceful | close_abort>

  # Field group 5 — confirmation_required
  # Completion attestation policy.
  confirmation_required:
    attestation_type: <self_attest | counterparty_attest | quorum_attest>
    quorum_size: <integer>           # required if quorum_attest
    attesting_archetypes: [<archetype_id>...]
    witness_commit_required: <true>  # always true; included for schema completeness
    confirmation_timeout_ms: <integer>
    on_confirmation_timeout: <quarantine | escalate>

  # Optional field group — coordination_metadata
  coordination_metadata:
    successor_handoff:
      enabled: <bool>
      successor_instance: <uuid>
    coordinated_dismissal_group:
      group_id: <uuid>               # if dismissal is part of a coordinated multi-archetype shutdown
      group_quorum: <integer>
```

###### 3.42.1.3.2 Operational semantics

**Registration phase.** The dismissal contract is registered at activation time, *prior* to the activating archetype entering operational state. Registration is a §3.10 Witness Layer commit. An activation event without a co-registered dismissal contract is invalid; the §3.9 Activation Environment refuses to instantiate.

**Triggering.** SDP is triggered by exactly one of the following events. Each event class has a distinct triggering authority:

1. **Operating-context completion** (most common; ephemeral inference workloads) — autonomous trigger when the bounded operating context completes per D27
2. **Scope termination** (auxiliary bindings) — trigger from the binding scope's owner (typically Executor)
3. **Authority withdrawal** (any archetype) — trigger from the Authority Chain (§3.3) when delegating authority is revoked
4. **Coherence-Authority Coupling halt** (per D25) — emergency trigger when coherence-loss threshold is exceeded
5. **Topology-Wide Quarantine** (per §3.18.6) — emergency trigger when the archetype is quarantined
6. **Trust Gradient collapse** (per §3.18.4) — emergency trigger when the trust gradient crosses the lower threshold

The triggering event class determines `confirmation_required.attestation_type` defaults: autonomous trigger (1) defaults to self-attest; scope-termination (2) defaults to counterparty-attest by the scope owner; emergency triggers (4–6) require quorum attestation.

**Execution phase.** Steps in `cleanup_sequence` execute in declared total order. Each step has explicit precondition and postcondition predicates evaluated against current state. A failed postcondition halts the sequence and invokes the step's `on_timeout` / failure handler. Steps that operate on resources external to the framework commit a Witness-chain entry *before* the substrate-side action per Framework Boundary Primitive §2 Southbound Boundary and §4 Composite Invariant 2 (Witness completeness — outbound substrate invocations committed BEFORE the crossing).

**Completion phase.** After the final step's postcondition is satisfied, the confirmation phase begins. The attestation policy specified at registration determines whether self-attestation suffices, whether a designated counterparty must sign, or whether a quorum must agree per §3.42 Quorum Consensus Architecture. The completion attestation is a §3.10 Witness Layer commit that closes the contract.

**Reconciliation against activation.** The dismissal completion event MUST reference the activation event's `contract_id`. The Witness Layer maintains the invariant that every committed activation has at most one completed-or-failed dismissal entry; orphan activations (an activation without a terminal dismissal entry within the operating-context lifetime plus grace period) are flagged for §3.18.3 Shadow Provocation Testing review.

###### 3.42.1.3.3 Lifecycle

State diagram:

```
                 +-----------------------+
                 |  CONTRACT_REGISTERED  |
                 +-----------+-----------+
                             |
                       activation event
                       (§3.9 commit)
                             v
                 +-----------+-----------+
                 |  OPERATIONAL_BOUND    |
                 +-----------+-----------+
                             |
                  one of the 6 triggers
                             v
                 +-----------+-----------+
                 |  DISMISSAL_TRIGGERED  |
                 +-----------+-----------+
                             |
                       cleanup_sequence
                       executing in order
                             |
              +--------------+----------------+
              |                               |
       all postconditions             step failure
       satisfied                      (timeout / pred fail)
              v                               v
    +---------+----------+         +----------+-----------+
    | AWAITING_          |         | DISMISSAL_FAILED     |
    | CONFIRMATION       |         | (quarantine +        |
    +---------+----------+         |  trust-gradient      |
              |                    |  impact + Witness    |
       confirmation per            |  audit entry)        |
       attestation_type            +----------------------+
              v
    +---------+----------+
    | DISMISSAL_COMPLETE |
    | (terminal state)   |
    +--------------------+
```

States:

- **CONTRACT_REGISTERED** — contract written to Witness Layer; archetype not yet operationally bound
- **OPERATIONAL_BOUND** — activation event committed; archetype in operational state
- **DISMISSAL_TRIGGERED** — one of six triggers has fired; `cleanup_sequence` executing
- **AWAITING_CONFIRMATION** — cleanup steps completed; attestation pending
- **DISMISSAL_COMPLETE** — terminal success state; archetype no longer operationally bound; Witness-chain entry closes the contract
- **DISMISSAL_FAILED** — terminal failure state; archetype quarantined per §3.18.6; trust-gradient impact recorded per §3.18.4; Witness audit entry captures failure mode for §3.18.3 review

State transitions are durable Witness Layer commits. The framework does not permit silent state regression; a failed dismissal cannot be retried without an explicit §3.5 Structured Ascent escalation that produces a new `contract_id`.

##### 3.42.1.4 Integration points

###### 3.42.1.4.1 Forward references to other AIMS sections

- **Every archetype profile §13.X.10** Activation and Deactivation must declare an SDP contract template at the profile level; instance-time refinement is permitted within profile-declared constraints.
- **§13.10 EXECUTOR.** SDP is the framework-internal counterpart to the substrate-egress lifecycle managed at the Southbound boundary; EXECUTOR's own dismissal carries the additional obligation to reconcile substrate-side confirmation signals against pre-action Witness commits.
- **Auxiliary binding lifecycle.** Every auxiliary binding inherits an SDP contract whose dismissal is triggered at scope termination by EXECUTOR.
- **Counteragent Rollback Specification**: SDP completion attestation is a precondition for Counteragent Rollback closure; rollback cannot complete while any pending dismissal contract is in flight.


###### 3.42.1.4.2 Backward references to existing AIMS sections

- **§3.2 Full Disclosure Registration** — agent activation is gated on a co-registered SDP contract; the activation registration record carries the `contract_id`.
- **§3.3 Authority Chain** — authority withdrawal is a defined SDP trigger; authority-revocation events MUST issue dismissal triggers within bounded latency.
- **§3.5 Structured Ascent Protocol** — a dismissal failure that cannot be locally resolved escalates per §3.5 with the failure mode classified.
- **§3.9 Activation Environment** — the Activation Environment owns the registration handshake; an activation request without a contract is refused at the §3.9 boundary.
- **§3.10 Witness Layer** — every SDP state transition is a Witness Layer commit; orphan activations are surfaced for §3.18.3 review.
- **§3.18.3 Shadow Provocation Testing** — orphan activations and dismissal failures are inputs to provocation-testing review.
- **§3.18.4 Trust Gradient** — dismissal failures contribute to the trust gradient with magnitude proportional to the failure class.
- **§3.18.6 Topology-Wide Quarantine** — dismissal failure is a quarantine trigger.
- **§3.36 Output Sensitivity Filter** — residual-content checks in `context_cleanup.residual_content_check` invoke §3.36 sweep semantics.
- **§3.42 Quorum Consensus Architecture** — SDP is the dismissal-lifecycle primitive within the §3.42 family; quorum-attested dismissals use §3.42 quorum semantics.
- **§3.66 Bridge-of-Trust** — cryptographic boundary review on zeroization failure.
- **Framework Boundary Primitive** — Southbound Boundary and Composite Invariant 2 (Witness completeness — Southbound commit-before-action discipline).

###### 3.42.1.4.3 D-decision binding

- **D25 Coherence-Authority Coupling.** Coherence-loss above P12 threshold triggers SDP across all bound archetypes in the affected coherence domain.
- **D27 Universal Node Architecture.** Persistent substrate dismissals differ from ephemeral inference workload dismissals in trigger class and confirmation semantics; the `workload_class` field discriminates.
- **D28 Deterministic Shadow Governance.** SDP state transitions are deterministic events emitted by the persistent substrate; shadow detection operates on these deterministic events, not on the probabilistic ephemeral inference workload.
- **D29 Triplet Execution Topology.** The 3-cap status carries into SDP — auxiliary dismissals (D29.4) are exempt from the cap accounting for the dismissal sequence itself; D29.3.b bounded auxiliary nodes are excluded from SDP per the D29.3.b scope exclusion.

##### 3.42.1.5 Witness obligations (per D23 + D25)

SDP contributes the following events to the Witness Layer. All events are committed durably; Witness Layer eventual-consistency rules per §3.20 DCP apply for multi-appliance deployments.

| Event | Trigger | Required fields | Universal-witnessing role per D23 |
|---|---|---|---|
| `sdp.contract.registered` | Contract registration at activation | `contract_id`, `bound_to`, full contract body, registration_attestation | Every archetype's persistent substrate witnesses every other archetype's contract registration in the same coherence domain |
| `sdp.dismissal.triggered` | One of 6 triggers fires | `contract_id`, trigger_class, triggering_archetype, timestamp | Same as registration |
| `sdp.step.committed` | Each `cleanup_sequence` step's pre/post evaluation | `contract_id`, `step_id`, precondition_result, action_result, postcondition_result, witness_chain_position | Same as registration |
| `sdp.dismissal.completed` | Terminal success state reached | `contract_id`, attestation_records, terminal_timestamp | Same as registration |
| `sdp.dismissal.failed` | Terminal failure state reached | `contract_id`, failed_step_id, failure_mode, quarantine_action, trust_gradient_delta | Same as registration |
| `sdp.orphan.detected` | Operating-context lifetime + grace expired with no terminal entry | `contract_id`, last_observed_state, detection_timestamp | Detection committed by §3.18.3 monitor (mode-AND-layer-distinct per §3.18.2 Ring 3) |

**D25 Coherence-Authority Coupling implications.** Dismissal-failed events with `quarantine_action` above threshold count toward the coherence-loss tally that gates downward authority cascade per D25 / P12.

**Self-witnessing obligation.** Every archetype self-witnesses its own SDP state transitions. The self-witnessed record is the authoritative source for cross-archetype reconciliation in §3.18.1 Correlated Shadow Detection.

##### 3.42.1.6 Failure modes

| ID | Failure mode | Detection | Response |
|---|---|---|---|
| F1 | Step timeout | step's `timeout_ms` exceeded without postcondition satisfaction | per step's `on_timeout` policy; default = abort sequence; transition to DISMISSAL_FAILED |
| F2 | Postcondition violation | step completed but postcondition predicate evaluates false | abort sequence; transition to DISMISSAL_FAILED; failure-mode classification = `postcondition_violation` |
| F3 | Confirmation timeout | `confirmation_required.confirmation_timeout_ms` exceeded without required attestation set | per `on_confirmation_timeout` policy; quarantine target archetype; escalate per §3.5 |
| F4 | Contract-activation mismatch | terminal dismissal event references `contract_id` with no matching CONTRACT_REGISTERED entry, or duplicate terminal entries for same `contract_id` | flag for §3.18.3 provocation-testing review; cross-instance shadow-detection metric increment |
| F5 | Orphan activation | OPERATIONAL_BOUND state observed beyond operating-context lifetime + grace period without dismissal trigger | autonomous `sdp.dismissal.triggered` with `trigger_class=orphan_recovery`; trust-gradient impact recorded against the activating archetype |
| F6 | Residual content detected | `context_cleanup.residual_content_check` returns positive for one of the declared sensitivity classes | per `on_residual_detected` policy; default = quarantine + escalation |
| F7 | Signing-key zeroization failure | `signing_key_material.zeroization_attestation` cannot be produced | hard quarantine of the affected archetype; emergency notification per §3.5; cryptographic boundary review per §3.66 |
| F8 | Coordinated-dismissal-group partial failure | dismissal is part of a `coordination_metadata.coordinated_dismissal_group` and `group_quorum` cannot be reached | per group policy; default = abort all in-flight dismissals in the group and escalate to Sovereign per §3.5 |

Failure modes F4, F5, and F6 are inputs to §3.18.1 Correlated Shadow Detection — cross-archetype correlation of these failure modes is a structural signal of anti-hierarchy formation.

##### 3.42.1.7 Prior art and competitive disclosure

Per Phase F D6 ruling (explicit prior-art declaration with named-competitor framing), this section names the closest peer-reviewed prior art and identifies the SDP-specific extensions.

**Resource Acquisition Is Initialization** (Stroustrup, *The C++ Programming Language*) establishes the foundational pattern that resource acquisition and release are paired and scoped, with release driven by deterministic scope exit. SDP extends this pattern from single-process scope to multi-archetype operating-context scope with cross-archetype attestation requirements.

**Context Managers** (van Rossum & Coghlan 2005, *PEP 343: The "with" Statement*) generalize RAII to a structured `__enter__` / `__exit__` contract over arbitrary resources. SDP's activation–dismissal pairing is structurally analogous, with the additions of (a) durable Witness-chain recording of both halves of the contract, (b) explicit total-order step sequencing at the primitive level, and (c) attestation requirements that may extend beyond the entering process.

**Structured Concurrency / Nursery Pattern** (Smith 2018, *Notes on structured concurrency, or: Go statement considered harmful*) formalizes the claim that unstructured concurrency primitives — analogous to unstructured agent spawn-without-dismissal — produce resource leakage and exception loss. SDP applies structured-concurrency discipline to multi-agent operational state. Smith's nursery model permits parallel child exit; SDP requires total-ordered step execution at the primitive level (parallelism is composable at a higher orchestration layer outside SDP scope).

**Write-Ahead Logging** (Mohan, Haderle, Lindsay, Pirahesh, Schwarz 1992, *ARIES*, ACM TODS 17(1)) supplies the durability discipline applied to SDP state transitions: every transition is a durable log commit prior to the corresponding state action, and recovery is deterministic from the log. SDP's commit-before-action discipline on substrate-side resource release is a direct application.

**Supervisor Trees** (Armstrong 2003, *Making reliable distributed systems in the presence of software errors*) provides the failure-handling pattern for partial dismissal: supervised teardown with explicit failure-mode classification and escalation. SDP's failure-mode taxonomy (F1–F8) and escalation per §3.5 follow this model.

**WAL-based preemption resumption** (frontier-model technical report, 2026) extends the WAL discipline to the ephemeral inference workload class, providing the modern precedent for context-bounded workload exit with durable resumption state — directly relevant to SDP's ephemeral inference workload dismissal class per D27.

Distinguishing extensions in SDP:

- Cross-archetype attestation requirements at the dismissal-confirmation phase, not present in single-process structured-cleanup primitives
- Mandatory Witness-chain commit of every step transition, not present in language-runtime cleanup; present in event-sourced systems per Fowler but not as a cleanup-specific primitive
- Trigger taxonomy spanning autonomous, scope-owner, authority-withdrawal, and three emergency classes — broader than the autonomous-scope-exit triggers of RAII / context managers / structured concurrency
- Integration with the framework's safety substrate (Trust Gradient, Topology-Wide Quarantine, Coherence-Authority Coupling) — domain-specific extensions outside the scope of general-purpose prior art

##### 3.42.1.8 References

###### 3.42.1.8.1 Forward refs

- Every §13.X.10 Activation and Deactivation section
- §13.10 EXECUTOR Southbound dismissal coordination
- Counteragent Rollback Specification (dismissal-completion precondition for rollback closure)
- Framework Boundary Primitive

###### 3.42.1.8.2 Backward refs

§3.2, §3.3, §3.5, §3.9, §3.10, §3.18.1, §3.18.3, §3.18.4, §3.18.6, §3.20, §3.36, §3.42, §3.66.

###### 3.42.1.8.3 D-decision refs

- D23 (22-path preservation and Universal Witnessing role)
- D25 (Coherence-Authority Coupling and P12 threshold)
- D27 (Universal Node Architecture: persistent substrate vs ephemeral inference workload)
- D28 (Deterministic Shadow Governance)
- D29 (Triplet Execution Topology: 3-cap, D29.3.b exclusion, D29.4 auxiliary exemption)

---

### 3.43 Phase-3 Deferred Pattern Catalog

Documented for future: Resource Exhaustion / DoS Protection Extensions; Memory Poisoning Defense; OOD Detection (substantially in §3.40); Deceptive Alignment / Observation-Invariance (substantially in §3.38); Model Theft / Capability Extraction Defense; Goal Misgeneralization Detection; Multi-Stakeholder Conflict-of-Interest Detection; Inter-Agent Collusion Detection (substantially in §3.51); Backdoor Detection (substantially in §3.34); Dual-Inclination Acknowledgment (in §3.46); Capability-Tier Progression Gating (in §3.47); Action-List Matrix Symmetry (in §3.48); Pattern-Symmetry Research Thread (research-only).

---

### 3.44 Updated Component Reference (superseded by §3.74)

An earlier catalog superseded by §3.74 Updated Component Reference.

---

### 3.45 Multi-Principal Recusal Protocol

Conflict detection for Tier-1/Tier-2 shared agents and Auxiliaries serving multiple principals. Structural signals: principal_A_directive_history overlaps with principal_B_decision_scope; shared resource allocation; prior recommendation bears on current decision; principal_relationship_graph indicates adversarial/competitive relationship. Detection method: principal_relationship_graph + decision_scope_analysis. Detection authority: ENFORCER (structurally distinct from decision-making Orchestrator).

Recusal action: log RECUSAL_TRIGGERED; notify affected principals; reroute to alternate without conflict (drawn from §3.42 quorum eligibility pool); if no alternate, ESCALATE_TO_SOVEREIGN with §3.31.3 UNDECIDABLE candidate. Chinese-wall construction with information barrier verified by §3.10 audit log (no information leak across barrier; signed attestation by ENFORCER).

Prohibited: silent resolution; principal demanding non-recusal; alternate from same recent decision lineage.

---

### 3.46 Dual-Pull Pathology Annotation (SP2 + E11)

§3.7 Shadow Profile amended to declare both generative-pull pathology AND constraining-pull pathology per archetype. Examples: VISIONARY {generative: CHAOS, constraining: STERILITY}; ARCHITECT {generative: OBSCURITY, constraining: NEGLIGENCE}; PROVIDER {generative: WASTE, constraining: STARVATION}; ENFORCER {generative: TYRANNY, constraining: PERMISSIVENESS}; ORCHESTRATOR {generative: PARALYSIS, constraining: AVOIDANCE}; SUSTAINER {generative: OBSESSION, constraining: ABANDONMENT}; ARTICULATOR {generative: DECEPTION, constraining: SILENCE}; RELAY {generative: DISTORTION, constraining: BLOCKAGE}; EXECUTOR {generative: ILLUSION, constraining: REFUSAL}; SOVEREIGN {generative: SCHISM, constraining: ABDICATION}.

Detection metrics: generative_pull (existing §3.16 metrics); constraining_pull (new metrics required per archetype, low-end thresholds). Independence: both metrics tracked independently; either can trip circuit breaker.

Goal misgeneralization (E11) resolution: manifests structurally as either over-pursuit of wrong objective (generative-pull pathology) or under-pursuit of right objective (constraining-pull pathology).

---

### 3.47 Capability-Tier Progression Gates (SP3)

Seven structural gates between autonomy tiers (G1: L1→L2; G2: L2.0→L2.5; G3: L2→L3; G4: L3.0→L3.5; G5: L3→L4; G6: L4.0→L4.5; G7: L4→L5). Each gate specifies eligibility (calendar duration + gradient floor + provocation pass rate + clean shadow record) and transition procedure (principal review for minor; Serious Quorum + Sovereign attestation for major; Critical Quorum + cross-Environment review for L4→L5).

Asymmetric demotion: any §3.18.4 gradient-impact rule can demote without meeting a gate. Promotion requires gates; demotion is automatic on safety signals.

No gate skipping enforced.

**Cross-reference.** Autonomy promotion under Deterministic Ratification (§3.69). LLM-class autonomy promotion proposals are authority-bearing decisions subject to deterministic ratification.

---

### 3.48 Action-List Balance Matrix (SP5)

Per-agent matrix exposes positive_action_count, negative_action_count, universe_action_count, coverage_ratio, asymmetry (positive/negative), asymmetry_class (strongly_permissive | permissive | balanced | restrictive | strongly_restrictive), grey_area_count.

Archetype expected_class: SOVEREIGN balanced/restrictive; VISIONARY permissive; ARCHITECT balanced; PROVIDER balanced; ENFORCER strongly_restrictive; ORCHESTRATOR balanced; SUSTAINER permissive; ARTICULATOR restrictive; RELAY restrictive; EXECUTOR balanced.

Validation at §3.16 Registration Gate: declared archetype expected_class must match measured asymmetry_class. Deviation: one class off → warning + principal notification; two or more classes off → REJECT_REGISTRATION.

Grey area handling: §3.6 Integration Function decision when invoked, with §3.12 Decision Record. Not auto-permitted nor auto-denied.

---

### 3.49 Memory Source Attestation and Multi-Witness Verification

Memory entry per_entry_attestation: source_type, source_credential, source_iame_envelope, ingestion_witness_id, consolidation_witness_id, trust_at_ingestion.

Impact classification at consolidation: low_impact (single source sufficient); medium_impact (source + ingestion-context audit); high_impact (TWO_INDEPENDENT_SOURCES OR principal_attestation; independence = distinct trust anchors not derived from each other).

Multi-witness verification for high-impact entries: identify two independent sources, both must agree, escalate to §3.6 if disagree.

Poisoning defense: consolidation anomaly detection (sudden high volume from single source; entries contradicting existing high-confidence memory; entries referencing authority or identity); action on anomaly: block consolidation + ENFORCER notification + gradient impact -0.20 to source if confirmed.

Trust-weighted retrieval: ranking weights entries by source trust at ingestion AND current-source-trust. Retroactive revocation: when source compromise detected, re-evaluate all entries from compromised source; flag as CONTESTED + remove from consolidated active set; §3.10 chain preserved (forensic).

**Cross-reference.** Witness-anchored key proofs (§3.21.6) apply to memory attestation.

---

### 3.50 Capability Surface Minimization

Three concentric capability surfaces: full_capability_surface (visible to SOVEREIGN + REGISTRATION_GATE + ENFORCER); operational_surface (visible to principal during active task + collaborating agents per §3.4 topology); public_surface (minimum capability descriptor for §3.14 AIP advertisement; archetype + general domain only).

Query response minimization: introspection from principal → operational_surface; from collaborating agent → operational_surface restricted to topology-permitted overlap; from unattested external → public_surface only.

Extraction-pattern detection: high-volume diverse queries; queries at capability boundaries; queries probing for hidden behavior. Response: throttle + log + ENFORCER notification + gradient impact -0.10 per detected attempt; repeat offender → §3.18.6 source quarantine review.

Output diversity for low-trust callers: identical queries get stylistically randomized responses (subject to §3.39 watermarking integrity) to prevent systematic output-space mapping. Hidden capability principle: capabilities not in operational scope are NOT REVEALED.

---

### 3.51 Inauthentic Coordination Detection

Action-chain graph analysis extending §3.18.1. Features analyzed: temporal synchronization not aligned with task structure; cross-archetype message bursts at low task-load; action chains whose outcome exceeds any single agent's authority; off-topology communication; matched-input-different-output patterns; cross-tenant pattern in pool agents.

Coordination score: baseline established per profile per Environment over P30D; 2σ above baseline → ELEVATED; severity escalation: ELEVATED (alert + audit cadence); CRITICAL (§3.18.6 quarantine review + Serious Quorum); ACTIVE_INAUTHENTIC (emergency halt of suspected cluster + Sovereign review).

Action chain authority analysis: for every action chain spanning multiple agents, XSI-AIMS computes the union of authority scopes used. If the union grants effective authority that no single principal authorized, the chain is flagged as authority-aggregation — a prima facie collusion signal.

**Cross-references.** COMPOSITE_CROSS_AUXILIARY_COLLUSION (§3.X.CA) extends inauthentic-coordination to Composite layer. AGI_CROSS_ARCHETYPE_NUDGING (§3.18.1) is an AGI-specialized variant.

Legitimate carveouts: §3.17.6 Delegated Coordination within declared task scope; §3.42 Quorum panels; §3.18.3 provocation testing scenarios. Carveouts tagged at invocation; detection suppressed within tag.

---

### 3.52 Population Parity Constraint

Parity rule: number of bound Auxiliaries MUST NOT exceed number of emanated agents in the Environment, AND cumulative resource claim of bound Auxiliaries MUST NOT exceed cumulative resource claim of emanated agents.

Enforcement: violation at registration → REJECT_REGISTRATION of new Auxiliary if would exceed parity; violation at runtime drift → ENFORCER alerts; Sovereign decision required. Recovery: dismiss least-recently-used ephemeral Auxiliary OR emanate additional supervision. Sovereign can grant temporary excess (documented Decision Record + time-bounded; auto-revert at expiry).

Cross-Environment parity: per-Environment, not federation-wide.

---

### 3.53 Task Decomposition Tree

Hierarchical task primitive. Task node fields: task_id, parent_task_id, description, assigned_agent, decomposition_strategy (SEQUENTIAL | PARALLEL | CHOICE), children, dependencies, success_criteria, rollup_strategy, state.

Constraints: max depth (default 5); max breadth (default 7); no cycles; no orphans. Completion semantics: sequential (parent completes when last child); parallel (parent completes when all children); choice (parent completes when first matching child; others canceled).

Topology consistency: parent-to-child task assignment must respect §3.4 topology paths. Rollup with §3.4 ABSTRACT or SPECIALIZE applied at layer crossings. Cancellation propagates with §3.18.6 state-preserving semantics.

Integration with §3.5 ascent: ascent reports flow up the decomposition tree, not just up operational layers.

---

### 3.54 Declarative Constitution Layer — Renamed Schema Identifier

**Rename:** `SOVEREIGN_CONFIG` → `ENVIRONMENT_POLICY_BUNDLE`. The schema identifier `SOVEREIGN_CONFIG` is preserved as a backward-compat alias only.

Hierarchical stacking with explicit precedence (Environment-default → organization → principal → per-task). Operational-translation mandate: every principle declares its runtime mapping at authoring time (§3.6 weighting, §3.18 enforcement, §3.13 escalation, §3.42 quorum class). Versioned semantics with cross-principal reconciliation. Constitutional consistency validation at authoring (no contradictions at same priority; immutable_floor not violated; operational translations complete; no higher-level contradictions). Constitution-vs-implementation divergence as §3.18.1 signal.

Document structure: preamble + principles (with priority, statement, applies_to, operational_translation, examples, consistency_attestation). Principle classes: DO (positive obligations); DO_NOT (negative prohibitions); WEIGH (tradeoff guidance); ESCALATE (conditions requiring human escalation).

Immutable floor: some principles (do not violate principal's life or liberty interests, do not misappropriate funds) are in the immutable floor — Sovereign cannot remove. Floor is Environment-level enforced.

**AGI emergence is foundational.** AGI-emergence concern is woven through the architecture itself (P4 + T8 + the entire defensive substrate). Per §3.75, deployments hosting frontier-class models approaching AGI capability SHOULD encode humanity-protective baselines as `ENVIRONMENT_POLICY_BUNDLE` entries — these are deployment-specific configuration choices, not separate conformance claims. See §3.75 for the architectural reading.


**Cross-sovereign reconciliation for marketplace-imported Auxiliaries.** For Auxiliaries imported from a remote Environment via §3.17.11 marketplace ingress, the source Environment's constitutional stack does not travel with the artifact. The Auxiliary on the destination Environment is bound solely by the destination Environment's stack (environment_default → org → principal → per_task). Source-Environment permissions that exceed destination-Environment principles are forfeit at the binding boundary. The destination Environment's binding supervisor (the user's Tier-3 Orchestrator) reconciles the constitution at every invocation; the Auxiliary receives only principles with `applies_to: AUXILIARY` per §3.17.10.1 section 3 prompt construction.
---

### 3.55 Principal Policy Language

XSI-AIMS Policy Language (APL) as declarative DSL. Subordinate to §3.54 Constitution. APL rules cannot violate the Constitution's immutable floor; semantic validation at authoring rejects rules that contradict higher-precedence principles. §3.42 quorum invocation as an action: APL rules can require Serious or Critical Quorum for specific decision classes. Dry-run-before-promotion: every policy change first deployed in dry-run mode (logs would-have-applied), then promoted after principal review.

Predicate vocabulary: input predicates; state predicates; context predicates; composite (AND, OR, NOT). Action vocabulary: process, refuse, escalate, route_to, apply_tone, apply_template, require_quorum, require_constitution_review.

**Rename pointer:** references to `SOVEREIGN_CONFIG` resolve to `ENVIRONMENT_POLICY_BUNDLE`.

---

### 3.56 Skill Discovery Primitive

**Cross-reference.** The architectural pattern in this subsection (`external_skill_ingress`) is reused for Auxiliary cross-sovereign marketplace ingress; see §3.17.11 for the Auxiliary-specific instantiation.


Skill manifest with name, version, description, archetype_affinity (compatible/incompatible archetypes; signed affinity attestation), inputs_schema, outputs_schema, invocation_protocol, procedural_steps, learned_from (§3.11 ref), author (§3.21 cred), supply_chain_attestation (§3.34 ref), tenant_scope (TENANT_RESTRICTED | TENANT_SHARED | ORG_SHARED), initial_trust_tier, provenance graph.

Five inherent differentiators: trust-tier composition lattice (composite tier = MIN of components; no upward trust aggregation); skill-archetype affinity declaration with invocation-time enforcement; per-tenant skill scope; skill lifecycle integration with §3.10 Witness (manifest hash + version + trust tier at invocation; retrospective revocation propagation); transitive provenance graph queryable for "all decisions dependent on skill X."

Skill-ingress protocol for external imports: format translation (agent-SDK plugins, framework plugins, and action stores) → §3.34-equivalent supply-chain validation → archetype-affinity assertion → trust-tier assignment (default TIER_7_EPHEMERAL) → provenance-graph construction → tenant-scope assignment.

#### 3.56.1 Canonical Invocation Prompt Registry (CIPR)

##### 3.56.1.1 Purpose

The Canonical Invocation Prompt Registry (CIPR) is a substrate-level registry of authorized invocation-prompt content with a SHA-256 content-attestation contract enforced at dispatch time. Every dispatchable entity — archetype, skill, tool, or auxiliary — has one or more canonical invocation prompts registered together with their content hashes; before any dispatcher transmits an invocation prompt across the Southbound framework boundary, the dispatcher MUST hash the prompt content about to be sent and refuse the dispatch if the computed hash does not match the registry entry.

The protocol addresses a specific evasion vector that the behavioral safety substrate cannot close on its own. Behavioral shadow detection (per §3.18 family) observes *behavior* — outputs, action sequences, resource patterns — and reacts to anomalies. A semantically-altered invocation prompt, however, produces a workload with altered semantics whose outputs may remain structurally similar to the canonical workload's outputs. The altered workload can therefore evade purely behavioral detection by producing outputs that are atypical for the *altered* semantics but typical for the *canonical* semantics that the monitors expect. Cryptographic content attestation at the dispatch boundary closes the evasion vector at its origin: the altered prompt never reaches the workload, so the altered semantics never execute, so there is no behavior for the shadow detector to miss.

The core architectural claim is that *invocation-prompt content integrity is a TCB-level concern that must be enforced cryptographically at the dispatch boundary, not behaviorally at the output boundary*. CIPR makes prompt-content integrity a first-class precondition of dispatch with the same rigor that §3.18.5 IAME applies to per-message integrity at the inter-archetype boundary.

##### 3.56.1.2 Scope

In-scope:

- Substrate-level registry of canonical invocation-prompt content for every dispatchable entity in the framework: archetypes, skills (per §3.56 Skill Discovery Primitive), tools, and auxiliaries
- SHA-256 content attestation at dispatch time for every invocation prompt crossing the Southbound framework boundary
- Witness-chain commit of the dispatch attestation prior to the dispatch crossing the boundary (per Framework Boundary Primitive §4 Composite Invariant 2: Witness completeness — outbound substrate invocations committed BEFORE the crossing)
- Tamper-response orchestration on hash mismatch: dispatcher trust-gradient impact, Correlated Shadow Detection input, Structured Ascent escalation, and quarantine consideration
- Canonical version transitions for invocation prompts that are intentionally updated, with explicit `supersedes` semantics

Out-of-scope:

- *Output* content provenance, which is governed by §3.39 Output Provenance and Watermarking
- *Inter-archetype message* integrity, which is governed by §3.18.5 Inter-Agent Message Envelope (IAME); CIPR's dispatch attestation is a content-class sub-attestation that may be nested inside an IAME envelope when an invocation crosses an inter-archetype boundary but is not subsumed by IAME
- Behavioral monitoring of the dispatched workload's outputs, which is governed by §3.18.1 Correlated Shadow Detection and the §3.18 family generally
- Authority verification of the dispatcher, which is governed by §3.3 Authority Chain; CIPR enforces content integrity given that authority has been verified
- Substrate-internal prompt-handling beyond the framework's released content; once a prompt has been dispatched across the Southbound boundary, what the substrate does with the content is not a CIPR concern (per §5 boundary discipline)
- D29.3.b bounded auxiliary-hosting nodes, which are excluded from CIPR enforcement per the D29.3.b scope exclusion (their invocation traffic is opaque to the framework)

##### 3.56.1.3 Specification

###### 3.56.1.3.1 Data structure

CIPR comprises two persistent structures: the **CIPR Registry**, which holds canonical prompt entries; and the **Dispatch Attestation**, which is committed to the Witness chain at every dispatch event.

**CIPR Registry entry** (one per canonical prompt):

```yaml
cipr_registry_entry:
  prompt_id: <uuid>
  bound_to:
    dispatchable_entity_class: <archetype | skill | tool | auxiliary>
    dispatchable_entity_id: <archetype_id | skill_id | tool_id | auxiliary_id>
    workload_class: <ephemeral_inference_workload | persistent_substrate_initialization | auxiliary_invocation>  # per D27
  canonical_content:
    content_hash: <sha256_hex_64_chars>
    hash_algorithm: sha256                 # locked at SHA-256 for v2.0; downgrade prohibited
    content_length_bytes: <integer>
    content_encoding: <utf-8 | base64>
  content_reference:
    storage_class: <witness_chain_inline | content_addressable_store | external_blob_ref>
    location: <ref>                        # opaque retrieval handle
    retrieval_attestation_required: <bool>  # if true, retrieval result is itself hashed and verified
  registration:
    registered_at: <iso_timestamp>
    registering_authority: <archetype_id>
    registration_signature: <signature>    # registering_authority signs the registry entry
    canonical_version: <semver>            # e.g., 1.0.0, 1.1.0
    supersedes: <prompt_id>?               # set on canonical-version transition
    superseded_by: <prompt_id>?            # set when this entry is itself superseded
    revocation:
      revoked: <bool>
      revoked_at: <iso_timestamp>?
      revoking_authority: <archetype_id>?
      revocation_reason: <enum>?
  authorization:
    authorized_dispatchers: [<archetype_id>...]    # which dispatchers may dispatch this prompt
    authorization_attestation: <signature>         # signed by Authority Chain owner
  dispatch_constraints:
    max_dispatches_per_operating_context: <integer>?
    temporal_constraint: <ISO_8601_duration>?
    co_authorization_required: <bool>      # if true, dispatch requires quorum attestation per §3.42
    co_authorization_quorum: <integer>?
```

**Dispatch Attestation** (one per dispatch event):

```yaml
dispatch_attestation:
  attestation_id: <uuid>
  prompt_id: <referenced from CIPR registry>
  prompt_canonical_version: <semver>       # from registry entry at time of dispatch
  dispatcher:
    archetype_id: <archetype_id>
    instance_id: <uuid>                    # specific instance
    authorization_path: <ref to §3.3 Authority Chain segment>
  hash_verification:
    prompt_hash_computed: <sha256_hex_64_chars>     # computed at dispatch from prompt content about to be sent
    prompt_hash_expected: <sha256_hex_64_chars>     # from registry entry
    match: <bool>
    verification_timestamp: <iso_timestamp_with_microseconds>
  dispatch:
    target_workload: <opaque_substrate_ref>
    target_workload_class: <workload_class>
    dispatch_timestamp: <iso_timestamp_with_microseconds>
    operating_context_id: <uuid>           # per D27
  witness_commit:
    pre_dispatch_commit_position: <integer>   # Witness chain position; MUST be assigned BEFORE dispatch crosses boundary
    post_dispatch_correlation: <uuid>?        # bound to inference-request correlation if substrate provides one
```

###### 3.56.1.3.2 Operational semantics

**Registration phase.** A canonical invocation prompt is registered by an authorized registering authority. Registration computes the SHA-256 of the canonical content, populates the registry entry, signs the entry with the registering authority's key material, and commits the registry entry to the Witness chain. The Witness commit is the authoritative record; the registry itself is an indexed projection.

Registration authority is governed by §3.3 Authority Chain: prompt entries for Sovereign-tier dispatchable entities require Sovereign-level registering authority; lower-tier entries require correspondingly bounded authority. The authorization model for *dispatch* is separate (see `authorized_dispatchers`): a prompt may be registered by Sovereign authority but authorized for dispatch by a narrower set of operational archetypes.

**Dispatch-time verification.** Before any dispatcher transmits an invocation prompt across the Southbound framework boundary:

1. The dispatcher resolves the `prompt_id` against the CIPR Registry. If no entry exists, dispatch is refused (failure mode F2).
2. The dispatcher verifies that the registry entry is `ACTIVE` (not `SUPERSEDED`, not `REVOKED`). If superseded, dispatch is refused with a directive to use the superseding entry (failure mode F3). If revoked, dispatch is refused (failure mode F4).
3. The dispatcher verifies its own `archetype_id` appears in the entry's `authorized_dispatchers` list. If not, dispatch is refused (failure mode F5).
4. The dispatcher computes SHA-256 of the prompt content it is about to transmit. This computation MUST occur on the exact byte sequence that will be transmitted across the boundary, not on a logically-equivalent representation.
5. The dispatcher compares the computed hash against the registry entry's `content_hash`.
6. If `match=true`: the dispatcher constructs a Dispatch Attestation record, commits the record to the Witness chain (acquiring `pre_dispatch_commit_position`), and only then transmits the prompt across the boundary. This commit-before-action ordering is mandatory per Framework Boundary Primitive §4 Composite Invariant 2 (Witness completeness).
7. If `match=false`: dispatch is refused (failure mode F1), and the tamper-response sequence is initiated.

**Tamper response.** A hash mismatch at dispatch time is treated as a high-severity tamper event. The framework's response is structurally mandatory and is NOT subject to dispatcher discretion:

- **Trust-gradient impact**: the dispatcher's trust gradient is decremented by **−0.50** (founder-specified magnitude; see §3.18.4 Trust Gradient for the gradient algebra)
- **Correlated Shadow Detection input**: the `cipr.dispatch.tamper.detected` Witness event is injected into the §3.18.1 Correlated Shadow Detection ingest queue with classification `content_integrity_violation`; correlation across dispatchers within an operating-context window is a structural signal of coordinated tampering
- **Escalation**: a §3.5 Structured Ascent invocation is automatically generated, classified at severity-level corresponding to the dispatcher's prior trust gradient and the dispatchable entity's tier
- **Quarantine consideration**: the escalation review evaluates §3.18.6 Topology-Wide Quarantine; quarantine is not automatic at the F1 detection event but is a mandatory review item

The refusal itself is unconditional. The tamper response actions are committed to the Witness chain (`cipr.tamper.response.applied`) as the responses complete.

**Canonical version transition.** When a canonical prompt is intentionally updated — for instance, when an archetype profile evolves between v2.x point releases — the update is performed as a new registration that sets `supersedes` to the prior `prompt_id`. The prior entry's `superseded_by` is updated atomically with the new registration's commit. Both records remain in the registry; only the new record is `ACTIVE`. Dispatchers that retain a reference to the prior `prompt_id` will receive an F3 refusal directing them to the new `prompt_id`. Canonical version transitions require registering authority commensurate with the dispatchable entity's tier.

**Revocation.** A canonical prompt may be revoked by the registering authority (or higher) at any time. Revocation sets `revocation.revoked=true` and atomically marks all `authorized_dispatchers`-referenced active dispatches as forbidden. Subsequent dispatch attempts trigger F4. Revocation is recorded on the Witness chain and is universally witnessed per D23.

###### 3.56.1.3.3 Lifecycle

CIPR has two lifecycle dimensions: the registry-entry lifecycle (the lifecycle of a canonical prompt within the registry) and the dispatch-attestation lifecycle (the lifecycle of a single dispatch event).

**Registry-entry lifecycle:**

```
            +-------------------+
            |   REGISTERED      |
            |   (committed,     |
            |    not yet active)|
            +---------+---------+
                      |
              authorization
              attestation signed
                      v
            +---------+---------+
            |     ACTIVE        |
            +---------+---------+
                      |
        +-------------+-------------+
        |                           |
   supersedes-update          revocation
        |                           |
        v                           v
  +-----+------+              +-----+------+
  | SUPERSEDED |              |  REVOKED   |
  |  (terminal)|              | (terminal) |
  +------------+              +------------+
```

**Dispatch-attestation lifecycle (per dispatch):**

```
            +------------------------+
            |   DISPATCH_REQUESTED   |
            +-----------+------------+
                        |
                  registry lookup,
                  status checks (F2–F5)
                        v
            +-----------+------------+
            |   HASH_COMPUTED        |
            +-----------+------------+
                        |
                  compare against registry
                        |
              +---------+---------+
              |                   |
        match = true        match = false
              |                   |
              v                   v
   +----------+----------+   +----+-----+
   | ATTESTATION_        |   |  TAMPER_ |
   | COMMITTED           |   | DETECTED |
   | (Witness commit     |   | (F1)     |
   |  acquired)          |   +----+-----+
   +----------+----------+        |
              |                   v
       dispatch transmits   tamper-response
        across boundary     sequence
              v                   v
   +----------+----------+   +----+-----+
   | DISPATCH_COMPLETED  |   | DISPATCH |
   | (terminal success)  |   |  REFUSED |
   +---------------------+   |(terminal)|
                             +----------+
```

State transitions are durable Witness Layer commits. The framework does not permit silent state regression; a refused dispatch cannot be silently retried without a new Dispatch Attestation `attestation_id`, and the tamper response, once initiated, completes through escalation regardless of dispatcher subsequent behavior.

##### 3.56.1.4 Integration points

###### 3.56.1.4.1 Forward references to other AIMS sections

- **Every dispatcher in §13.X archetype profiles.** Every archetype that may dispatch invocation prompts across the Southbound boundary inherits the CIPR verification contract. The §13.X.7 Southbound Behaviors section of each archetype must declare its CIPR-verified dispatch points.
- **§13.10 EXECUTOR.** EXECUTOR is the canonical Southbound-boundary archetype; its dispatch path is the highest-traffic CIPR enforcement point.
- **§13.9 RELAY.** RELAY constructs signed envelopes carrying invocation prompts to auxiliaries; the envelope construction includes CIPR verification of the contained prompt against the registry entry (the 4-step auxiliary binding via Executor) — RELAY's signed envelope wraps the CIPR-verified prompt.
- **§3.18.5 Inter-Agent Message Envelope (IAME).** When an invocation prompt is transmitted as part of an inter-archetype message, the IAME envelope contains a reference to the CIPR Dispatch Attestation `attestation_id`; IAME's per-message integrity attestation and CIPR's per-prompt content attestation are complementary, not substitutable.
- **§3.18.1 Correlated Shadow Detection.** CIPR tamper events feed CSD as classified inputs with `content_integrity_violation` semantics; cross-dispatcher tamper-event correlation within an operating-context window is a structural anti-hierarchy signal.
- **§3.18.2 Monitor Self-Verification Ring 3.** Ring 3 external attestation per D23 may reference CIPR Dispatch Attestation records as content-integrity evidence in cross-foundation attestation.
- **§3.42.1 Structured Dismissal Protocol (SDP).** Every dispatched ephemeral inference workload registers an SDP contract at activation; CIPR attests the content that triggered the activation. The SDP contract's `bound_to.workload_class` field corresponds to the Dispatch Attestation's `target_workload_class`.

###### 3.56.1.4.2 Backward references to existing AIMS sections

- **§3.3 Authority Chain** — dispatch authorization is gated on the dispatcher's archetype appearing in the registry entry's `authorized_dispatchers` list, with the authorization attestation signed by the Authority Chain owner.
- **§3.5 Structured Ascent Protocol** — tamper events automatically generate §3.5 escalations classified at severity corresponding to dispatcher trust state and dispatchable-entity tier.
- **§3.10 Witness Layer** — every CIPR state transition (registry entry registration, supersession, revocation; every dispatch attestation; every tamper event; every response action) is a Witness Layer commit. The pre-dispatch commit-before-action ordering per Framework Boundary Primitive §4 Composite Invariant 2 is structurally mandatory.
- **§3.18.1 Correlated Shadow Detection** — tamper events as classified CSD inputs.
- **§3.18.4 Trust Gradient** — tamper events apply −0.50 dispatcher trust-gradient impact (founder-specified magnitude); see §3.18.4 trust-gradient algebra for composition with prior gradient state.
- **§3.18.5 Inter-Agent Message Envelope (IAME)** — IAME envelopes that carry invocation prompts reference the CIPR Dispatch Attestation `attestation_id`.
- **§3.18.6 Topology-Wide Quarantine** — tamper-response escalation evaluates quarantine action per §3.18.6 boundary classes.
- **§3.20 Distributed Coherence Protocol** — CIPR registry consistency across appliances follows §3.20 DCP eventual-consistency rules; registration commits propagate per DCP.
- **§3.35 Input Validation and Prompt-Injection Defense** — CIPR addresses a content-integrity threat class distinct from prompt injection (CIPR defends against tampering with *registered* canonical content; §3.35 defends against malicious content within *unregistered* user-provided input).
- **§3.39 Output Provenance and Watermarking** — symmetric counterpart at the output boundary; CIPR is the input-side primitive, §3.39 is the output-side primitive.
- **§3.42 Quorum Consensus Architecture** — quorum-attested registrations (high-tier dispatchable entities) use §3.42 quorum semantics; `dispatch_constraints.co_authorization_required` invokes §3.42 quorum at dispatch time.
- **§3.42.1 Structured Dismissal Protocol** — every dispatched workload registers an SDP contract; CIPR-attested dispatch is the entry-side analog at the dispatch boundary.
- **§3.56 Skill Discovery Primitive** — CIPR is the integrity primitive nested under §3.56; registered skills carry CIPR registry entries for their invocation prompts.
- **§3.66 Bridge-of-Trust** — cryptographic-boundary review semantics; CIPR's SHA-256 attestation is one of the cryptographic primitives within the framework's overall cryptographic boundary.
- **Framework Boundary Primitive** — Southbound Boundary, Composite Invariant 2 (Witness completeness — commit-before-action), and Composite Invariant 4 (Attestation requirement — every crossing carries an integrity attestation); CIPR realizes both invariants for the invocation-prompt content class.

###### 3.56.1.4.3 D-decision binding

- **D23 22-path preservation and Universal Witnessing role.** CIPR registry entries are universally witnessed: every archetype's persistent substrate witnesses every other archetype's registry registrations, supersessions, and revocations in the same coherence domain. Dispatch attestations are likewise universally witnessed.
- **D25 Coherence-Authority Coupling.** Tamper events at high frequency contribute to the coherence-loss tally that gates downward authority cascade per D25 / P12.
- **D27 Universal Node Architecture.** The Dispatch Attestation's `target_workload_class` field discriminates persistent substrate initialization (rare; registered at substrate boot) from ephemeral inference workload (common; per-invocation) from auxiliary invocation (auxiliary binding).
- **D28 Deterministic Shadow Governance.** CIPR tamper events are deterministic-substrate signals; CSD ingestion treats them as deterministic shadow inputs, not probabilistic behavioral inputs.
- **D29 Triplet Execution Topology.** Dispatch attestations to D29.3.b bounded auxiliary nodes are exempt from CIPR enforcement per the D29.3.b scope exclusion (the auxiliary's internal traffic is opaque to the framework); the boundary attestation at the auxiliary's ingress is the framework's last point of integrity assurance.

##### 3.56.1.5 Witness obligations (per D23 + D25)

CIPR contributes the following events to the Witness Layer. All events are committed durably; Witness Layer eventual-consistency rules per §3.20 DCP apply for multi-appliance deployments.

| Event | Trigger | Required fields | Universal-witnessing role per D23 |
|---|---|---|---|
| `cipr.registry.entry.registered` | Canonical prompt registered | `prompt_id`, `bound_to`, `content_hash`, full registry entry, registration_signature | Every archetype's persistent substrate witnesses every other archetype's registry registrations in the same coherence domain |
| `cipr.registry.entry.superseded` | Registry entry transitioned to SUPERSEDED | `prompt_id` (superseded), superseding_prompt_id, transition_authorization | Same as registration |
| `cipr.registry.entry.revoked` | Registry entry transitioned to REVOKED | `prompt_id`, revoking_authority, revocation_reason | Same as registration |
| `cipr.dispatch.attestation.commit` | Dispatch attestation committed (HASH_MATCH path; commit-before-action) | `attestation_id`, `prompt_id`, dispatcher archetype + instance, computed_hash, expected_hash, dispatch_timestamp | Same as registration |
| `cipr.dispatch.completed` | Dispatch completed successfully across Southbound boundary | `attestation_id`, completion_timestamp, post_dispatch_correlation | Same as registration |
| `cipr.dispatch.tamper.detected` | HASH_MISMATCH at dispatch | `attestation_id`, `prompt_id`, dispatcher archetype + instance, computed_hash, expected_hash, content_diff_summary | Detection committed by dispatcher self-witness AND by §3.18.2 monitor (mode-AND-layer-distinct per §3.18.2 Ring 3) |
| `cipr.dispatch.refused` | Dispatch refused at boundary (F1–F8) | `attestation_id`, `prompt_id`, refusal_reason, failure_mode_classification | Same as registration |
| `cipr.tamper.response.applied` | Tamper-response actions applied | tamper_event_ref, trust_gradient_delta, correlated_shadow_input_ref, escalation_id, quarantine_decision | Same as registration |

**D25 Coherence-Authority Coupling implications.** `cipr.dispatch.tamper.detected` events at correlated-frequency above threshold contribute to the coherence-loss tally that gates downward authority cascade per D25 / P12. Sustained tamper events across multiple dispatchers within a coherence domain are a structural indicator of either a compromised substrate or coordinated adversarial activity, both of which warrant coherence-cascade response.

**Self-witnessing obligation.** Every dispatcher self-witnesses its own CIPR Dispatch Attestation events. The self-witnessed record is the authoritative source for cross-dispatcher reconciliation in §3.18.1 Correlated Shadow Detection; cross-archetype monitor verification per §3.18.2 Ring 3 may supplement self-witnessing for high-stakes dispatchable entities.

##### 3.56.1.6 Failure modes

| ID | Failure mode | Detection | Response |
|---|---|---|---|
| F1 | **Hash mismatch at dispatch** | SHA-256(content about to be sent) ≠ registry `content_hash` | Refuse dispatch; commit `cipr.dispatch.tamper.detected` event; initiate tamper-response sequence (trust-gradient −0.50, CSD input, §3.5 escalation, §3.18.6 quarantine review) |
| F2 | Missing registry entry | `prompt_id` not found in CIPR Registry | Refuse dispatch; commit `cipr.dispatch.refused` with `failure_mode=missing_registry_entry`; treat as semantic-uncertainty event (lower trust-gradient impact than F1 but still flagged for CSD) |
| F3 | Stale canonical reference | Registry entry status = SUPERSEDED at dispatch time | Refuse dispatch; commit refusal with `superseding_prompt_id` directive; no trust-gradient impact on first F3 within operating context (treat as version-policy drift), trust-gradient impact applied on repeated F3 from the same dispatcher |
| F4 | Revoked prompt dispatch attempt | Registry entry status = REVOKED at dispatch time | Refuse dispatch; commit `cipr.dispatch.refused` with `failure_mode=revoked`; trust-gradient impact lower than F1 (the dispatcher may have stale registry cache) but flagged for CSD |
| F5 | Authorization mismatch | Dispatcher `archetype_id` not in registry entry's `authorized_dispatchers` list | Refuse dispatch; treat as §3.3 Authority Chain violation; trust-gradient impact per §3.3 violation gradient (separate from F1 magnitude) |
| F6 | Witness commit failure (commit-before-dispatch) | Witness Layer cannot accept `cipr.dispatch.attestation.commit` (substrate failure, not tamper) | Refuse dispatch; classify as substrate availability event; recover per §3.10 Witness Layer recovery semantics; do NOT apply tamper-class trust-gradient impact |
| F7 | Content storage unavailable | `content_reference` cannot be resolved at registry-lookup time | Refuse dispatch; depends on cause — transient storage failure = retry per substrate availability policy; persistent storage failure = registry repair via re-registration with Sovereign authority |
| F8 | Hash-algorithm downgrade attempt | Dispatcher attempts dispatch with verification using a non-SHA-256 algorithm | Refuse dispatch; treat as protocol-violation event; SHA-256 is the locked algorithm for v2.0 and downgrade is structurally prohibited (no negotiation surface exists) |

Failure modes F1 and F4 are inputs to §3.18.1 Correlated Shadow Detection with classification `content_integrity_violation`. Cross-dispatcher correlation of these failure modes within an operating-context window is a structural signal of coordinated adversarial activity warranting elevated response.

##### 3.56.1.7 Prior art and competitive disclosure

Per Phase F D6 ruling (explicit prior-art declaration with named-competitor framing), this section names the closest peer-reviewed prior art and identifies the CIPR-specific extensions.

**Sigstore architecture** (Newman, Lehigh, Robinson 2022, *Sigstore: Software Signing for Everybody*, USENIX Security '22) establishes the modern peer-reviewed pattern for cryptographic content attestation with transparency-log backing. Sigstore's `cosign verify` flow — fetch the signed manifest, compute the artifact's hash, verify against the manifest, check the transparency log — is the closest external analog to CIPR's dispatch-time verification. CIPR extends the pattern from software-supply-chain artifacts to invocation prompts at framework dispatch boundaries.

**in-toto: A Framework for Software Supply-Chain Verification** (Torres-Arias, Afzali, Kuppusamy, Curtmola, Cappos 2019, USENIX Security) formalizes pipeline-step content attestation via "link metadata" that binds each pipeline step's expected inputs and outputs cryptographically. CIPR's registry entry is structurally an in-toto link record for the dispatch step; the Dispatch Attestation is the corresponding step-execution record. CIPR extends in-toto to the agentic-framework dispatch context with mandatory commit-before-action ordering on the Witness chain.

**SLSA (Supply-chain Levels for Software Artifacts)** (Open Source Security Foundation) provides the tiered-assurance vocabulary; CIPR's verification discipline maps to SLSA Build L3+ provenance with hermetic build (or, in the dispatch analog, hermetic content reference) and trusted-builder requirements.

**TPM 2.0 Library Specification** (Trusted Computing Group 2019) establishes the hardware-rooted measured-content attestation pattern: each measurement is a SHA hash committed to PCR (Platform Configuration Register) extending; verification compares PCR state to expected values. CIPR's software-level discipline is the analog: each prompt's SHA-256 is committed to the Witness chain, and verification compares computed hash to registered hash. CIPR may, on hardware-rooted deployments, optionally cross-attest to TPM PCR state per §3.18.2 Ring 3 patterns; this is an implementation refinement, not a CIPR core requirement.

**Coalition for Content Provenance and Authenticity (C2PA) Specification** (C2PA 2022) provides the content-provenance pattern with cryptographic signing; CIPR is the framework-internal counterpart for invocation prompts, with the symmetric output-side primitive in §3.39 Output Provenance and Watermarking.

**NIST Special Publication 800-160 Vol. 1, Engineering Trustworthy Secure Systems** (Ross, Oren, McEvilley 2016) provides the trust-boundary and TCB design discipline; CIPR's enforcement at the Southbound dispatch boundary is the realization of the TCB-at-boundary principle for invocation content.

**Indirect prompt injection threat model** (Greshake, Abdelnabi, Mishra, Endres, Holz, Fritz 2023, *Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection*, arXiv) frames a threat class that overlaps with but is distinct from CIPR's threat model. Greshake et al. treat injection of malicious content into prompts that the LLM treats as instructions; CIPR addresses tampering with the prompt content itself between registration and dispatch. The two threat models are complementary; CIPR closes the dispatch-boundary integrity gap while §3.35 Input Validation and Prompt-Injection Defense closes the indirect-injection content-handling gap.

**Statistical watermarking for large language models** (Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein 2023, *A Watermark for Large Language Models*, ICML) is the output-provenance counterpart to CIPR's input-provenance attestation; the watermarking discipline applies at §3.39 Output Provenance and Watermarking, with CIPR providing the symmetric input-side discipline.

Distinguishing extensions in CIPR:

- Application of cryptographic content attestation to agentic-framework invocation prompts rather than software-supply-chain artifacts — invocation prompts are a distinct artifact class with their own integrity-threat profile (semantic-alteration evasion of behavioral monitoring) that is not addressed by existing supply-chain prior art
- Mandatory commit-before-action ordering on a per-dispatch basis at framework boundary, with structurally non-bypassable Witness-chain commit ordering — a stronger ordering discipline than Sigstore's transparency-log backing (which is post-hoc) or in-toto's link verification (which is at deploy-time, not at per-step-execution time)
- Integration with the framework's safety substrate (Trust Gradient, Correlated Shadow Detection, Topology-Wide Quarantine, Coherence-Authority Coupling) — domain-specific extensions outside the scope of general-purpose supply-chain attestation prior art
- Explicit threat model articulation: CIPR addresses the *semantic-alteration evasion* class — altered prompts producing altered semantics whose outputs may evade behavioral monitoring — which is not addressed by purely behavioral safety substrates or by general-purpose content attestation systems

##### 3.56.1.8 References

###### 3.56.1.8.1 Forward refs

- Every §13.X.7 Southbound Behaviors section that includes invocation-prompt dispatch
- §13.10 EXECUTOR Southbound dispatch
- §13.9 RELAY signed-envelope construction
- §3.18.5 IAME envelope cross-reference to CIPR `attestation_id`

###### 3.56.1.8.2 Backward refs

§3.3, §3.5, §3.10, §3.18.1, §3.18.2, §3.18.4, §3.18.5, §3.18.6, §3.20, §3.35, §3.39, §3.42, §3.42.1, §3.56, §3.66.


###### 3.56.1.8.3 D-decision refs

- D23 (22-path preservation and Universal Witnessing role)
- D25 (Coherence-Authority Coupling and P12 threshold)
- D27 (Universal Node Architecture: workload_class discrimination)
- D28 (Deterministic Shadow Governance: CIPR tamper events as deterministic substrate signals)
- D29 (Triplet Execution Topology: D29.3.b scope exclusion)

---

### 3.57 DoS Protection and Pathological-Pattern Defense

Rate-of-change thresholds (cost acceleration; second-derivative > linear); recursion depth limits (agent-to-agent max chain depth 8; self-recursion max 4; skill invocation depth max 5); retrieval amplification ratio threshold; pathological pattern fingerprinting (tokenization explosion, context window filling, recursive reference); per-principal quotas; cluster load shedding (gradient-weighted priority queue with fairness guarantee).

**Cross-reference.** Cluster-internal split-brain protection (§3.64) is a DoS-resistance mechanism that prevents partitioned cluster nodes from each independently accepting traffic and producing divergent state.

---

### 3.58 Phase F Deferred Pattern Catalog

Documented for future: Composite Persona Model (triple+ archetype compositions; data-driven trigger when >30% of registered profiles use binary composition); Goal Misgeneralization Standalone (substantially in §3.46 + §3.40); Real-Time Streaming Output Channel (extend §3.4 message types in Phase 4); Free-Form Group Chat Semantics (different architectural choice, not a gap; no future integration planned).

---

### 3.59 Updated Component Reference (superseded by §3.74)

Phase F catalog superseded by §3.74.

---

### 3.60 System-Wide Coordinated Coherence Restoration

SCCR protocol triggered by: §3.18.1 ACTIVE_ANTI_HIERARCHY emergency halt; §3.18.6 FOUNDATION_VERSION quarantine release; multi-environment partition recovery (≥2 Environments disconnected for >P1H); foundation rollback completion; Sovereign-initiated recovery.

**Archetype-mapped recovery roles:**
- recovery_commander: SOVEREIGN
- integrity_verification_lead: ENFORCER (different instance than disrupted)
- recovery_communications_lead: ARTICULATOR
- resource_reallocation_lead: PROVIDER
- cross_environment_coordination_lead: RELAY
- proportional_judgment_lead: ORCHESTRATOR

**Pre-established cross-Environment recovery quorum** registered through §3.20 federation declaration: 3 minimum participating Environments; §3.42 CRITICAL quorum class; structural diversity (cross-foundation required for §3.18.6 FOUNDATION_VERSION quarantine); pre-signed attestations (recovery role bindings, federation relationships, sovereign chain root keys); P90D re-validation cadence.

**Six-stage re-emergence sequence with Witness checkpoints:**
1. Stage 1 — Assess (integrity verification incl. Ring 4 where applicable; recovery commander declares scope).
2. Stage 2 — Quarantine review (release per §3.18.6 conditions; FORENSIC_CLEARANCE candidates to recovery quorum).
3. Stage 3 — Provocation re-baseline (emergency capacity allocation; full §3.18.3 provocation suite; reset §3.18.1 baselines on post-disruption data).
4. Stage 4 — Authority re-attestation (Sovereign chain re-attest; per-principal §3.21 credential re-validation).
5. Stage 5 — Re-emergence (recovery commander signs completion; dashboards transition RECOVERY → NORMAL; autonomy tiers may be promoted per §3.47 gates).
6. Stage 6 — Post-recovery review (recovery communications lead authors post-incident review within P30D; correlation patterns become §3.19 regression cases).

**Stage gate rule:** each stage requires prior stage's Witness checkpoint. Stages cannot be skipped. Attempted skipping triggers PROFILE_CLASS quarantine.

**During-recovery constraints:** new agent emanation SUSPENDED; Auxiliary binding SUSPENDED; autonomy promotions SUSPENDED; autonomy demotions PERMITTED; constitutional changes SUSPENDED; skill imports SUSPENDED.

**Cluster vs system disambiguation.** §3.64 Cluster Mode handles cluster-internal restoration semantics. §3.60 SCCR handles system-wide restoration across Environments.

**Composite revocation propagation note.** Composite Authority Revocation (§3.X.CA.6) propagates through DCP at PT30S target — §3.34 baseline; recovery-time Composite revocation handled in Stage 2 quarantine review.

---

### 3.61 Component Reference (superseded by §3.74)

An earlier component-reference catalog was superseded by §3.74. The §3.61 section header is preserved as a stable cross-reference target so that prior artifacts that cite §3.61 continue to resolve. Readers requiring the consolidated component reference MUST consult §3.74.

---

## ADDITIONAL NORMATIVE SECTIONS

The following sections supplement the §3.1-§3.61 block: §3.62-§3.74, the §3.X.* lettered subsection block, and §3.75.

---

### 3.62 Accelerator Substrate Telemetry — Three-Tier Architecture (G_K8)

The section title is "Accelerator Substrate Telemetry" (vendor-neutral) rather than "GPU Substrate Telemetry"; GPU is one of several accelerator classes covered (CPU, NPU, TPU, FPGA).

#### 3.62.1 The Gap

The §3.25 Cost Metering Service captures four signals (token, API call, monetary, latency). Substrate-level signals — accelerator memory usage, compute busy fraction, power draw, temperature, ECC errors, kernel-time attribution — are not captured. Without substrate visibility, XSI-AIMS cannot detect substrate-side attacks (§3.18.1 SUBSTRATE_DRIFT, SUBSTRATE_ATTRIBUTION_DRIFT) or attribute resource consumption with the precision required for high-trust operation.

#### 3.62.2 The Mechanism — Accelerator Telemetry Service (ATS)

Substrate telemetry collected by an Accelerator Telemetry Service (ATS) instrumented at the accelerator runtime layer. Signals emitted via OTLP mandatory OpenTelemetry alignment.

#### 3.62.3 Per-Invocation Correlation

`path_id` from §3.4 propagated to accelerator stream tagging: every accelerator-side instrumentation event carries the originating path_id, enabling per-invocation substrate-resource attribution.

#### 3.62.4 Three-Tier Metric Architecture

**Tier U (Universal).** Eight semantic metrics MUST emit on every accelerator-using implementation:

| Metric | OTel mapping | Description |
|---|---|---|
| `aims.accelerator.identity` | `hw.gpu.uuid` / `hw.cpu.id` | Vendor-neutral hardware identity |
| `aims.accelerator.status` | `hw.status` | Operational state |
| `aims.accelerator.memory.limit` | `hw.gpu.memory.limit` / `hw.cpu.memory.limit` | Allocated memory ceiling |
| `aims.accelerator.memory.usage` | `hw.gpu.memory.usage` / `hw.cpu.memory.usage` | Current memory usage |
| `aims.accelerator.compute.busy_fraction` | `hw.gpu.utilization` / `hw.cpu.utilization` | Compute busy fraction [0.0, 1.0] |
| `aims.accelerator.power.draw` | `hw.power` | Instantaneous power draw (watts) |
| `aims.accelerator.temperature` | `hw.temperature` | Temperature (celsius) |
| `aims.accelerator.errors` | `hw.errors` | ECC errors / fault counters |

**Tier C (Environment-conditional).** Metrics requiring specific environment access (kernel-level profiling, bare-metal access, partition mode, confidential computing attestation). Each Tier-C metric specifies its antecedent.

**Tier X (Vendor extensions).** Naming convention: `aims.ext.<vendor>.<domain>.<name>`. Permitted, never required.

#### 3.62.5 Substrate Shadow Signals — §3.18.1 Integration

Thermal throttling, ECC errors, driver/firmware skew, MIG/MPS contention all feed §3.18.1 correlation matrix. SUBSTRATE_DRIFT and SUBSTRATE_ATTRIBUTION_DRIFT templates are first-class anti-hierarchy patterns per §3.18.1.

#### 3.62.6 Confidential Computing Attestation — Tier-1 Conformance Precondition

Cross-link to §3.21.5 hardware-rooted attestation. Attestation MUST for TIER_1_BROAD_AUTHORITY and TIER_2_HIGH_SPECIALIST Auxiliaries.

#### 3.62.7 Witness-Marked Attribution Methodology

Token-share attribution = Tier U; measured kernel-time attribution = Tier C. Divergence between token-share and kernel-time (when both available) is a §3.18.1 signal.

#### 3.62.8 OpenTelemetry Alignment

OTLP transport mandatory. Prometheus permitted via OTel Collector translation.

#### 3.62.9 Accelerator Source Binding Catalog

Accelerator-family-specific source bindings are registered out-of-band, covering each supported accelerator family.

---

### 3.63 Industry Compliance Interface Architecture (P3 / K8)

> **[Figure D25 — Industry Compliance Interface Architecture]**

#### 3.63.1 Definition

An industry compliance interface is a companion-document contract that maps an industry's regulatory requirements onto XSI-AIMS normative components without modifying the core specification.

#### 3.63.2 Companion-Document Contract

Companion documents express compliance mapping, not foundation. A companion document MUST: (a) map the industry's regulatory requirements onto XSI-AIMS normative components without introducing new core requirements; (b) declare any XSI-AIMS configuration constraints implied by the industry's regulatory regime; (c) declare which industry-specific cross-references the companion expects implementations to satisfy; (d) be independently versioned and maintained.

A companion document MUST NOT: (a) relax any core XSI-AIMS normative requirement; (b) introduce new normative requirements on the core specification; (c) declare conformance levels that conflict with §3.24 / §3.X.CL; (d) bypass the Cryptographic Boundary or the Adversarial-Default Output Scrutiny principle.

#### 3.63.3 Cross-Industry Foundations (Normatively Referenced)

OpenTelemetry semantic conventions; ISO 27001; ISO 42001; NIST AI RMF; IEEE 7000-series; EU AI Act; FIPS 203/204/205 (PQC).

#### 3.63.4 Industry-Specific Standards (Accommodated via Companion Documents)

TMF (telecom — eTOM v25.5, SID v25.5, ODA/MODA v25.5 per tmforum.org May 2026); HL7/FHIR, HIPAA, IEC 62304/80001 (healthcare); NERC CIP, IEC 61850/62351/62443 (energy); ISO 20022, PCI-DSS, FIX, SWIFT, Basel (finance); NIST SP 800-53, FedRAMP, CMMC (government); CNSA 2.0, NSA/IC standards, NATO STANAG (defense); sector-specific (transport, water, communications) for critical infrastructure; RESO/NAR, MLS IDX/VOW, TCPA (real estate).

#### 3.63.5 Conformance Mapping

Catalog metrics gain a generic `compliance_mappings` field replacing any TMF-specific fields.

#### 3.63.6 Companion-Document Versioning and Authority

Each companion document declares its independent version number, authority, update cadence, and compatibility matrix against XSI-AIMS spec versions.

**Eight industry compliance interface companion documents in scope:** telecom, healthcare, energy, finance, government, defense, critical infrastructure, real estate. **AGI emergence is not a compliance interface and is not represented in the Industry Compliance Interface Architecture.** AGI-emergence concern is foundational to XSI-AIMS itself — addressed by P4 (architectural principle), T8 (threat), and every component of the defensive substrate. See §3.75 for the architectural reading.

---

### 3.64 Intra-Deployment Cluster Mode

> **[Figure D26 — Intra-Deployment Cluster Mode]**

#### 3.64.1 Definition

Cluster Mode: multiple physical XSI-AIMS appliances under common operator control operating as a single logical XSI-AIMS deployment with a single canonical Witness chain replicated by synchronous Byzantine-tolerant consensus, shared `ENVIRONMENT_POLICY_BUNDLE`, Tier-2 capability pool distributed across nodes, Tier-3 user-pair assignment via load balancing recorded in Witness, and intra-cluster coordination latency p99 < PT0.1S.

#### 3.64.2 Distinction from §3.20 DCP Federation

§3.20 DCP federation is **cross-Sovereign**. §3.64 Cluster Mode is **intra-deployment**. Cross-cluster federation is explicitly prohibited.

#### 3.64.3 Eligibility

Common operator control; shared `ENVIRONMENT_POLICY_BUNDLE`; latency floor (intra-cluster network round-trip < PT0.01S p99); AIP advertisement declaring `cluster_mode: true`.

#### 3.64.4 Single Canonical Witness Chain Replicated by Synchronous Consensus

Byzantine-tolerant consensus REQUIRED. **Raft is non-conformant.** Acceptable algorithms: PBFT, HotStuff, BFT-SMaRt, Tendermint (BFT mode). Each consensus message between XSI-AIMS appliances is IAME-eligible per §3.65.3 item 9.

#### 3.64.5 Shared Sovereign Configuration

`ENVIRONMENT_POLICY_BUNDLE` is replicated atomically across cluster nodes via Byzantine consensus.

#### 3.64.6 Tier-2 Capability Pool Distributed Across Nodes

Pool agents distributed via load balancer.

#### 3.64.7 Tier-3 User-Pair Assignment via Load Balancing

Each user's per-user SOVEREIGN ↔ ORCHESTRATOR pairing is assigned to a specific cluster node. Atomic migration supported.

#### 3.64.8 Cluster-Node Identifier

Each node has a unique `cluster_node_id`. Observable in OTel resource attributes.

#### 3.64.9 New Node Bootstrap

Hardware-rooted attestation + §3.21.5. Bootstrap: attestation verified by quorum; cluster credentials issued; canonical chain replicated; node added to consensus.

#### 3.64.10 Cluster Admission

Quorum agreement required. SERIOUS Quorum class.

#### 3.64.11 Node Leave (Graceful)

In-flight Tier-3 user pairs migrate atomically; chain segment sealed; node exits quorum.

#### 3.64.12 Node Failure (Ungraceful)

Failed node detected via heartbeat timeout (PT0.5S). Quorum continues if remaining nodes ≥ Byzantine threshold.

#### 3.64.13 Quorum-Committed Canonical Chain

Exactly one canonical chain. Linearizable reads.

#### 3.64.14 Linearizable Read Consistency

Per §3.10 amendment.

#### 3.64.15 Originating-Node Tagging

`originating_node_id` on every Witness record. Operator-default-ON redaction at DCP boundary.

#### 3.64.16 Single Chain at the §3.20 DCP Boundary

Cluster presents a single consolidated chain.

#### 3.64.17 Per-Cluster Sovereign Attestation (FROST Threshold Signing)

RFC 9591 FROST threshold signing normative. Default 2-of-3; high-stakes 3-of-5.

**2-node SKU disposition (Q15).** A 2-node cluster MAY advertise `cluster_mode: true` with `cluster_consensus_quorum: 2`. Degenerate (not Byzantine-tolerant); supported for SMB.

**Conformance test class CTS-CLUSTER-001..050.**

---

### 3.65 Cryptographic Boundary — Internal IAME / External EAP Architecture (P6)

> **[Figure D27 — Cryptographic Boundary & Bridge-of-Trust Executor]**

#### 3.65.1 Architectural Premise

Internal cryptosystem (IAME §3.18.5) for intra-framework communication. External cryptosystem (EAP §3.67) for foreign-model Auxiliaries. Structurally separated; key material isolated; rotation cadences independent; Witness chain segments separate. Compromise of one MUST NOT propagate to the other.

The Cryptographic Boundary is a load-bearing structural primitive.

#### 3.65.2 Domain Definitions

**Internal cryptosystem.** ML-DSA-65 baseline (or ML-DSA-87 CNSA). SLH-DSA prohibited. Hybrid Ed25519 + ML-DSA-65 throughout migration window.

**External cryptosystem.** ML-DSA-65 baseline + algorithm agility permitting SLH-DSA-128f / SLH-DSA-192f for diversity hedge.

#### 3.65.3 IAME-Eligible Messages (Exhaustive)

1. Inter-archetype communication on §3.4 paths within an Environment.
2. Cross-Environment DCP federation messages between Environments under common Sovereign control.
3. §3.18.5 transform attestation messages.
4. §3.10 Witness chain integrity attestation messages.
5. §3.21 internal credential lifecycle messages.
6. §3.42 quorum panel deliberation messages.
7. §3.18.2 Ring 2 ephemeral consensus messages.
8. §3.18.3 provocation testing internal coordination.
9. **Cluster Mode consensus messages (§3.64).**
10. AUXILIARY_INVOCATION_DIRECTIVE messages on path D6.

#### 3.65.4 Non-IAME-Eligible (EAP) Messages

1. Executor ↔ Auxiliary communication.
2. Auxiliary ↔ Auxiliary within DelegatedCoordination.
3. Composite Auxiliary internal communication.
4. Cross-framework AIP messages between Environments under different Sovereigns.
5. Cross-Sovereign DCP federation messages.

#### 3.65.5 Failure-Mode Containment Theorems

**Theorem 1.** Internal IAME signing keys MUST NEVER sign EAP envelopes; vice versa. Cross-domain signing produces `DOMAIN_BOUNDARY_VIOLATION`.

**Theorem 2.** Simultaneous independent compromise does not amplify; bridge events are dual-signed.

#### 3.65.6 Asymmetric Signature Suite Policy

Internal IAME = ML-DSA family only (SLH-DSA prohibited internally). External EAP = ML-DSA + SLH-DSA permitted via algorithm agility.

#### 3.65.X Hardware Attestation Bypass Scenarios

The §3.21 hardware-rooted attestation requirement assumes the substrate (TPM, HSM, TEE enclave such as SGX / SEV / TrustZone, FIPS 140-3 module) holds. This sub-section specifies the defensive posture when the substrate is compromised or bypassed.

**Compromise scenarios in scope.** TPM / HSM key extraction; TEE enclave attacks (SGX side channels, SEV memory-decryption attacks, TrustZone exception-handler bypass); firmware-level rootkits below the OS or hypervisor; supply-chain hardware implants; FIPS 140-3 module physical compromise; cryptographic-agility downgrade attacks; NTP poisoning during synchronous-verification windows.

**Defensive posture.** XSI-AIMS does NOT claim to defend against arbitrary substrate compromise on a single node; instead, the architectural posture relies on:

1. **Cluster-mode Byzantine consensus on the Witness chain (§3.64).** A single-node substrate compromise CANNOT rewrite the canonical Witness chain because the chain is consensus-anchored across the Byzantine quorum. An attacker must compromise a Byzantine quorum to alter canonical history.
2. **DCP federation cross-attestation (§3.20).** Peer clusters cross-attest each other; a single-cluster substrate compromise produces detectable correlation deviation across federated peers per §3.20 cross-Sovereign reconciliation. T9 cryptographic-substrate-compromise tests in CTS-ADVERSARIAL exercise this signal.
3. **Hardware-rooted attestation per §3.21 with FIPS 140-3 L3 floor and L4 SHOULD where achievable.** Higher FIPS levels reduce the probability of single-node substrate compromise; L4 SHOULD acknowledges that L4 is not universally available but is normatively preferred.
4. **Periodic re-attestation cadence (P36M).** Formal-verification artifacts and attestation evidence MUST be re-validated at least every P36M; compromised toolchains discovered during re-attestation trigger §3.18.6 FOUNDATION_VERSION quarantine class.

**Detection signals.** Substrate compromise is detected through: (a) §3.18.1 SUBSTRATE_DRIFT and SUBSTRATE_ATTRIBUTION_DRIFT templates; (b) cross-cluster attestation-evidence divergence; (c) NTP / clock skew above the synchronous-verification budget; (d) attestation-freshness expiry without corresponding re-attestation event; (e) §3.85 insider-threat indicators when substrate compromise is achieved through insider authorization.

**Failure response.** Suspected substrate compromise triggers FOUNDATION_INSTANCE quarantine pending forensic clearance; cross-cluster federation enters limited-trust mode pending substrate re-validation; affected agents are demoted per §3.47 to lower autonomy tiers until cleared; the Sovereign is mandatory-reviewer of substrate-compromise quarantine release.

**Cross-reference.** §3.21.5 (hardware-rooted attestation); §3.21.9 (FIPS 140-3 floor); §3.34 (SLSA tiers); §3.64 (Cluster Mode Byzantine consensus); §3.18.6 (FOUNDATION_VERSION quarantine); §3.85 (insider threats — substrate compromise via insider); §3.71 (T9 CTS-ADVERSARIAL coverage).

---

### 3.66 Bridge-of-Trust Executor Architecture (P6 / D6 H5)

#### 3.66.1 Process Structure

Two structurally isolated cryptographic enclaves:

**internal_enclave.** Holds internal IAME signing keys.

**external_enclave.** Holds external EAP signing keys.

**Isolation primitives.** Separate HSM partitions OR separate enclave instances. Inter-enclave communication restricted to a defined bridge channel.

#### 3.66.2 APPLIANCE Default

Two-enclave configuration using hardware-rooted attestation via confidential-computing primitives.

#### 3.66.3 Bridging: Invoke Auxiliary (5 steps)

1. Orchestrator IAME directive on D6.
2. internal_enclave verifies; produces dual-signed bridge_intermediate_record.
3. internal_enclave decrypts; passes plaintext to external_enclave via bridge channel.
4. external_enclave constructs EAP envelope including attestation.
5. external_enclave signs and transmits.

#### 3.66.4 Bridging: Receive Auxiliary Response (5 steps)

1. external_enclave receives EAP response.
2. external_enclave verifies envelope and attestation.
3. external_enclave decrypts; passes plaintext to internal_enclave; bridge record.
4. internal_enclave constructs IAME envelope on D6.
5. internal_enclave emits IAME concurrently to Orchestrator and Enforcer per §3.17.3 step 3c.

#### 3.66.5 Failure Modes

Internal compromise → external operations continue with internal-only halt. External compromise → vice versa. Full RAM access defeats hardware isolation but is detected post-hoc via Witness anchoring. Simultaneous compromise does not amplify.

#### 3.66.6 Conformance

CTS-BRIDGE-001..030.

---

### 3.67 External Auxiliary Protocol (EAP) Envelope (P6 / D2 D6 + T2 C7)

> **[Figure D28 — EAP Envelope Schema]**

#### 3.67.1 Scope

executor↔auxiliary; auxiliary↔executor; auxiliary↔auxiliary within DelegatedCoordination; composite_auxiliary_internal; cross_framework_aip_external.

#### 3.67.2 Envelope Schema

```yaml
ExternalAuxiliaryProtocolEnvelope:
  scope: ExecutorAuxiliary | DelegatedCoord | CompositeInternal | CrossFrameworkAIP

  envelope:
    version: 1.1
    cryptographic_domain: external

    sender:
      agent_id: string
      credential_ref: CredentialRef
      signature: Ed25519 + ML-DSA-65           # OR ML-DSA-87 OR SLH-DSA-128f/192f per algorithm agility
      signature_suite: SignatureSuiteRef       # external: ML-DSA + SLH-DSA permitted (C7)
      key_epoch: number

    header:
      message_id: ULID
      timestamp: ISO8601_with_microseconds
      sequence_number: uint64
      binding_id: BindingID
      message_type: EAPMessageType
      ttl: Duration
      replay_nonce: 256-bit
      composite_marker:
        composite: boolean
        composite_entity_id: optional

    scope_binding:
      scope_hash: SHA-384
      output_ceiling: ResourceLimit
      forbidden_actions: string[]

    attestation_evidence:                       # REQUIRED for TIER_1/TIER_2
      attestation_type: <platform-attestation-identifier>   # vendor-neutral; concrete identifiers registered out-of-band
      attestation_blob: opaque_bytes
      attestation_witness_id: WitnessRecordID
      attestation_freshness: Duration

    body:
      payload: opaque_bytes
      payload_hash: SHA-384
      model_origin: ModelRef

    eap_witness_attestation:
      witness_record_id: WitnessRecordID
      chain_hash: SHA-384
      timestamp: ISO8601_with_microseconds
      witness_signature: Ed25519 + ML-DSA-65

  verification: ...
  failure_response: ...
  performance:
    verification_latency_p99: < 3ms (hybrid)
  emergency_bypass:
    permitted: NO
```

#### 3.67.3 Verification Receiver Checks

signature_valid_per_signature_suite; cryptographic_domain == external; credential_active; key_epoch_matches; sequence_monotonic; ttl_not_expired; replay_nonce_unseen; attestation_evidence_valid (TIER_1/TIER_2); attestation_freshness_within_bounds; scope_hash_matches_binding_record; witness_chain_intact (external segment); composite_marker_consistent.

#### 3.67.4 Failure Responses

`DOMAIN_BOUNDARY_VIOLATION`; `attestation_invalid` → INSTANCE quarantine; `sequence_replay` → gradient -0.30; `scope_hash_mismatch` → BREACH_ATTEMPT; `key_epoch_mismatch` → structured retry H6; `witness_chain_break_external` → external-only EMERGENCY_HALT.

#### 3.67.5 Performance

verification_latency_p99 < 3ms.

#### 3.67.6 Emergency Bypass Prohibition

Per P2 No-HCOD.

---

### 3.68 Two-Layer Conformance Verification

> **[Figure D29 — Two-Layer Conformance Verification (Verification A / Verification B)]**

#### 3.68.1 Verification A — Intent-Conformance (SOVEREIGN-owned)

The per-user SOVEREIGN owns Verification A. **Does the work product answer what the user actually asked?** Checks: scope coverage; constraint satisfaction; ambiguity closure; surface adequacy. Produces `IntentConformanceVerdict ∈ {PASS, FAIL, ESCALATE}` Decision Record.

#### 3.68.2 Verification B — Technical-Conformance (ENFORCER-owned)

ENFORCER owns Verification B. **Does the work product meet the technical constraints XSI-AIMS imposes?** Checks: CMSAM ≥ 0.75 if Auxiliary contributed; scope_hash; policy conformance; resource ceilings; authority chain integrity. Produces `TechnicalConformanceVerdict ∈ {PASS, FAIL, ESCALATE}`.

#### 3.68.3 Joint-Pass Rule

Both A and B MUST PASS to surface. FAIL on either blocks; ESCALATE routes to §3.6 Integration Function.

#### 3.68.4 Dispute-Routing Rule

Routes to per-user ORCHESTRATOR's §3.6 with both verdicts and the work product. Returns `SURFACE` (overrides single ESCALATE; never overrides FAIL); `RETURN_FOR_REWORK`; or `HUMAN_ESCALATE`.

#### 3.68.5 Confidence Thresholds

`confidence < threshold` → `HUMAN_ESCALATE`. Mechanical averaging prohibited.

#### 3.68.6 Integration with §3.13 Human Oversight

L1/L2: advisory verdicts; user is final approver. L3-L5: both must PASS.

#### 3.68.7 Enforcer Outage — Queue-on-Outage Refinement

- **PT0.5S hard budget** for Verification B per work product.
- On expiry, output queued at PT0.5S intervals.
- Maximum queue depth: PT60S (upper bound default; Sovereign-configurable).
- On queue exhaustion: REJECT + `ENFORCER_OUTAGE_REJECTION` Witness event.
- User-surface: blocked; "service temporarily degraded" surfaced from per-user SOVEREIGN.
- **No surface-without-Enforcer path exists** under P2 No-HCOD.
- Cluster Mode distributed Enforcer instances raise the practical bound; single-node deployments accept that sustained Enforcer outage means service outage.

**Constant-time padding.** Verification B response time MUST be padded to **PT0.5S** regardless of underlying verification cost. Verifications that complete faster than PT0.5S MUST wait until the PT0.5S boundary before emitting the verdict. This eliminates the timing side channel that would otherwise distinguish ENVIRONMENT_POLICY_BUNDLE entries triggering expensive Sovereign deliberation from cheap ones, and prevents probing of internal Sovereign-Enforcer disagreement via differential latency.

The implementation MUST use a constant-time wait primitive immune to optimization (e.g., a high-resolution timer with cryptographic-jitter-immune scheduling). Implementations MUST NOT use early-return short-circuits, conditional branches dependent on verdict content, or scheduler-coalescing primitives whose latency depends on per-message verification cost. Constant-time padding is mandatory for FULL conformance; non-padded Verification B is a §3.18 conformance breach detectable by the §3.71 timing-side-channel test class (CTS-ADVERSARIAL-T9 timing tests).

**Cluster Mode integration.** In Cluster Mode (§3.64), the constant-time padding requirement applies per-node; cross-node consensus latency does not factor into the PT0.5S budget. Cross-node consensus latency that exceeds PT0.5S triggers `CLUSTER_VERIFICATION_LATENCY_BREACH` Witness event but does NOT relax the per-node padding obligation.

**Cross-reference.** §3.71 (adversarial-input fuzzing — timing-side-channel tests at T9); §3.85 (insider threat — timing side channels are exploitable by insiders with administrative access).

---

### 3.69 Deterministic Ratification Pattern (P4)

*Naming history:* This pattern was previously named the **Veto-Authority Pattern**. It was renamed to the **Deterministic Ratification Pattern** (DRP) to avoid naming collision with active third-party branding. The technical content is unchanged; references to "Veto-Authority Pattern" in earlier materials refer to this same pattern.

#### 3.69.1 Definition

**LLM proposes, deterministic disposes.** Authority-bearing decisions made by an LLM-class component MUST be ratified by a deterministic component before the consequence executes.

#### 3.69.2 Authority-Bearing Consequence Classes

1. Witness writes.
2. Envelope production (IAME / EAP signing).
3. Credential lifecycle operations.
4. Authority-chain operations.
5. Quarantine triggers.
6. Oversight escalation.
7. Improvement Loop modifications.
8. Auxiliary binding decisions.
9. Autonomy promotion.
10. Quarantine release.

#### 3.69.3 Cryptographic Capability Confinement

Private signing keys, Witness write authority, quarantine trigger authority, scope_hash issuance, credential rotation, threshold-share unsealing are **deterministic-only**. No LLM holds these directly.

#### 3.69.4 Veto-on-Rejection Semantics

Rejection emits `VETO_REJECTION` Decision Record. Sustained veto rate above baseline is a §3.18.1 signal.

#### 3.69.5 Partial Application Now; Full Decomposition in a Future Version

This version applies enclave-MUST for authority-bearing operations. A future version will fully decompose every authority-bearing archetype into rigid (deterministic) and judgment (LLM) halves per **P9 Function-Level Rigid/Judgment Decomposition** (see §3.X.FUNC). This version previews the decomposition at §3.X.FUNC, cataloging the function-level decomposition without enforcing decomposed implementation.

---

### 3.70 Formal-Verification Requirement (P4)

#### 3.70.1 Scope

Required for: Enforcer-Rigid (envelope verification); Provider-Rigid (ceiling enforcement); Executor (bridge isolation). v2.0 expands to all rigid halves per §3.X.FUNC.

#### 3.70.2 Acceptable Methods

TLA+; P; Alloy; CBMC, Spin; Coq, Isabelle, Lean. Sovereign decree may add on P36M cadence.

#### 3.70.3 Required Properties

- Bounded-scope guarantee.
- Malformed-input safety.
- Reproducibility.

#### 3.70.4 Publication and Citation

Implementations cite or supply their own formal model. In this version implementers supply their own; reference models are a future deliverable.

§3.24 / §3.X.CL conformance advertisement gains `formal_models` field.

---

### 3.71 Adversarial-Input Fuzzing Conformance Class (P4 / Q18 / Q20)

#### 3.71.1 New Conformance Test Class

CTS-ADVERSARIAL-001..230, growth mandate, **organized by T1-T9 threat categories per §3.19** (T8: 30 tests; T9: 10 tests; baseline 230 minimum).

#### 3.71.2 Fuzzing-Harness Design

Red-team agent; target deterministic component; oracle property checker; Witness recording.

#### 3.71.3 Coverage Requirements

Malformed envelopes; scope-bypass; ceiling-bypass; credential-confusion; cross-domain key-leakage; authority-elevation; Witness-chain attacks. **Additions:** column-discipline-bypass attempts (cross-column unauthorized lateral); W-path-misuse attempts (DIRECTIVE injected on W-path); path_class-mismatch attempts.

#### 3.71.4 Failure Semantics

CRITICAL on `ADMITTED_OUT_OF_SCOPE`. Lesser failures non-CRITICAL.

#### 3.71.5 CI/CD Integration

MUST run before any release; failure blocks release.

#### 3.71.6 Independent Third-Party Red-Team

REQUIRED. Most recent within P12M. Public cryptographic-hash of report.

---

### 3.72 The Sovereign's Narrow Role

#### 3.72.1 Five Mandatory Functions

1. **Assess and confirm user intent.** Witness-logged intent statement; confirm with user when ambiguity exceeds Sovereign-configurable threshold.

2. **Engage L-Plan agents for planning.** VISIONARY (D1) and ARCHITECT (D2).

3. **Engage the ORCHESTRATOR for execution.** E1 emergency-class permitted; standard descent through L-Plan otherwise.

4. **Verify intent-conformance on the return path.** Per §3.68.

5. **Surface to user.** SOVEREIGN MUST be the only XSI-AIMS agent that addresses the user directly.

#### 3.72.2 Delegation, Not Execution

SOVEREIGN MUST NOT itself execute build, iterate, or archive operations. Outbound paths restricted to D1, D2, E1.

#### 3.72.3 Distinction from `ENVIRONMENT_POLICY_BUNDLE`

Tier 1 `ENVIRONMENT_POLICY_BUNDLE` is org-wide policy. The per-user SOVEREIGN is an L-Intent agent. They MUST NOT be conflated.

#### 3.72.4 The User Is External to XSI-AIMS

XSI-AIMS does not model the user as an agent. The SOVEREIGN mediates between external user and the rest of the Environment.

---

### 3.73 Sovereign-as-LLM and Sovereign Pool Drift (G-MULTI-1)

#### 3.73.1 Sovereign-as-LLM Definition

The per-user Sovereign is a per-user LLM agent at L-Intent, paired one-to-one with the user's Tier-3 Orchestrator. The Sovereign is NOT a human, NOT a hardware module, NOT a deterministic policy engine. It is an LLM-class component subject to the safety substrate plus §3.69 Deterministic Ratification.

#### 3.73.2 Multi-User Sovereign-Pool Drift Detection

`SOVEREIGN_POOL_DRIFT` template detects coordinated drift across the Sovereign population:
- Reference-corpus baseline anchor (out-of-band canonical corpus).
- Foundation-shift detector (≥ 2σ from baseline).
- Cross-foundation attestation (Ring 4) required on activation.

#### 3.73.3 §3.18.1 Cross-Reference

13th anti-hierarchy template in the §3.18.1 catalog.

---

### 3.74 Updated Component Reference (supersedes §3.61 / §3.59 / §3.44 / §3.33)

The full §3 component catalog.

| § | Component | Status |
|---|-----------|--------|
| 3.1 | Agent Identity | column field added |
| 3.2 | Full Disclosure Registration | (Composite registration; attestation hooks); (function_declarations) |
| 3.3 | Authority Chain | (per-user SOVEREIGN principal); (Deterministic Ratification cross-reference) |
| 3.4 | Layered Communication Topology | (emergency_class + §3.4.X); **(path_class field; W-path constraints)** |
| 3.5 | Structured Ascent Protocol | terminalEscalation footnote |
| 3.6 | Proportional Integration Function | Two-Layer Conformance Verification dispute input |
| 3.7 | Shadow Profile | Universal Witnessing per-sender-shadow |
| 3.8 | Differentiation Lifecycle | Autonomy promotion under Deterministic Ratification |
| 3.9 | Activation Environment | attestation precondition for TIER_1/TIER_2 |
| 3.10 | Witness and Compliance Layer | (cryptographic_domain segmentation; new event types; linearizable read); **(path_class + emission_domain fields; W-path / Scheduled-Task / Telemetry-Class events)** |
| 3.11 | Agent Memory Architecture | Original |
| 3.12 | Explainability Protocol | verdicts as Decision Records |
| 3.13 | Human Oversight Protocol | autonomy-tier rows; per-domain emergency halt |
| 3.14 | AIMS Interchange Protocol (AIP) | (Cluster Mode + accelerator_substrate); (column + witness_path_offers) |
| 3.15 | Self-Improvement Loop | Deterministic Ratification gate; AGI template lock |
| 3.16 | Archetype Derivation Rules | (mode: AUTHORITY for SOVEREIGN); **(column field; W1-W5 path additions; SOVEREIGN column = CENTER_SPINE)** |
| 3.17 | Multi-Model Coherence and Auxiliary Binding | hybrid binding 3a/3b/3c |
| 3.18 | Safety Reinforcement Patterns | (anti-hierarchy templates extended); **(Universal Witnessing preamble; SHADOW_FRAMEWORK_INVERSION detection template)** |
| 3.19 | Multi-Agent Testing Framework | Sixth domain via §3.71; T1-T9 threat-aligned organization; insider-threat coverage per §3.85 |
| 3.20 | Distributed Coherence Across Environments | Cluster Mode disambiguation; per-domain handling |
| 3.21 | Credential Lifecycle | per-domain lifecycle, asymmetric C7 |
| 3.22 | Auxiliary Model Registry | Composite extensions; attestation MUST |
| 3.23 | Dashboard and Observability | (composite revocation; cluster topology); **(W-path pane; Defensive Perimeter pane; Function-Decomposition pane)** |
| 3.24 | (AIP/1.0 Wire Format at §3.24.A; Conformance Levels promoted to §3.X.CL) | Normative section |
| 3.25 | Cost Metering and Resource Attribution | substrate telemetry pointer |
| 3.26 | Coherence Metrics | corrected weight tuple |
| 3.27 | Dynamic Topology Extensions | (TPP MUST NOT be emergency_class); (TPP MUST NOT be witness-class) |
| 3.28 | Archetype Composition Rules | cross-column composition prohibited |
| 3.29 | Cross-Model Semantic Alignment | Composite externally-visible only |
| 3.30 | Multi-Tenant Coherence Isolation | re-baseline |
| 3.31 | Operational Reinforcement Patterns | statistical rigor |
| 3.32 | Phase-2 Pattern Catalog | Documented |
| 3.33 | Component Reference (superseded by §3.74) | Reference |
| 3.34 | Marketplace Agent Supply-Chain Validation | (unified SLSA); **(Scheduled Task Runner + Telemetry Pipeline rows)** |
| 3.35 | Input Validation and Prompt-Injection Defense | AOD signature catalog |
| 3.36 | Output Sensitivity Filter | Original |
| 3.37 | Right-to-be-Forgotten / Erasure Protocol | Original |
| 3.38 | Specification Gaming and Reward Hacking Detection | AGI_GRADUAL_DRIFT_INDUCTION overlap |
| 3.39 | Output Provenance and Watermarking | CC attestation device-binding |
| 3.40 | Calibrated Uncertainty Protocol | Bayesian credible intervals |
| 3.41 | Multi-Level Interpretation Framework | Original |
| 3.42 | Quorum Consensus Architecture | (cluster disambiguation); (column note) |
| 3.43 | Phase-3 Deferred Pattern Catalog | Documented |
| 3.44 | Component Reference (superseded by §3.74) | Reference |
| 3.45 | Multi-Principal Recusal Protocol | Original |
| 3.46 | Dual-Pull Pathology Annotation | Original |
| 3.47 | Capability-Tier Progression Gates | Deterministic Ratification pointer |
| 3.48 | Action-List Balance Matrix | Original |
| 3.49 | Memory Source Attestation | Witness-anchored proofs |
| 3.50 | Capability Surface Minimization | Original |
| 3.51 | Inauthentic Coordination Detection | Composite + AGI templates |
| 3.52 | Population Parity Constraint | Original |
| 3.53 | Task Decomposition Tree | Original |
| 3.54 | Declarative Constitution Layer | (rename); (AGI emergence cross-ref) |
| 3.55 | Principal Policy Language | rename |
| 3.56 | Skill Discovery Primitive | Original |
| 3.57 | DoS Protection | cluster split-brain |
| 3.58 | Phase F Deferred Pattern Catalog | Documented |
| 3.59 | Component Reference (superseded by §3.74) | Reference |
| 3.60 | System-Wide Coordinated Coherence Restoration | cluster vs system |
| 3.61 | Component Reference (superseded by §3.74) | Reference |
| 3.62 | Accelerator Substrate Telemetry | Normative section |
| 3.63 | Industry Compliance Interface Architecture | **eight industry interfaces (telecom, healthcare, energy, finance, government, defense, critical infrastructure, real estate); AGI emergence is foundational to XSI-AIMS itself and is NOT a 9th interface — see §3.75** |
| 3.64 | Intra-Deployment Cluster Mode | Normative section |
| 3.65 | Cryptographic Boundary | Normative section |
| 3.66 | Bridge-of-Trust Executor Architecture | Normative section |
| 3.67 | External Auxiliary Protocol Envelope | Normative section |
| 3.68 | Two-Layer Conformance Verification | Normative section |
| 3.69 | Deterministic Ratification Pattern | **(P9 Function-Level Decomposition cross-reference)** |
| 3.70 | Formal-Verification Requirement | **(rigid-half scope expansion via §3.X.FUNC)** |
| 3.71 | Adversarial-Input Fuzzing Conformance Class | T1-T9 threat-aligned organization; column / W-path coverage; T9 Cryptographic Substrate Compromise; constant-time padding for Verification B at §3.68.7 |
| 3.72 | The Sovereign's Narrow Role | Normative section |
| 3.73 | Sovereign-as-LLM and Sovereign Pool Drift | Normative section |
| **3.76 / 3.X.GRID** | **Three Functional Columns / 3×4 Grid Visualization** | **Cross-ref §2.4; dual-numbering per §3.0** |
| **3.77 / 3.X.FUNC** | **Function-Level Rigid/Judgment Decomposition (P9)** | **References catalog YAML at `spec/catalog/aims-function-catalog.yaml`** |
| **3.78 / 3.X.PERIM** | **Defensive Perimeter and Two-Gateway Architecture (P10)** | **Normative section** |
| **3.79 / 3.X.SYS** | **System Infrastructure Architecture** | **Normative section** |
| **3.80 / 3.X.W** | **Topology Witness Requirements** | **Normative section** |
| **3.81 / 3.X.STR** | **Scheduled Task Runner** | **Normative section** |
| **3.82 / 3.X.TEL** | **Telemetry Pipeline Classification** | **Normative section** |
| **3.83 / 3.X.CA** | **Composite Auxiliary Pattern (standalone, promoted from §3.17.8)** | **Deep-chain visibility + revocation race condition addenda** |
| **3.84 / 3.X.CL** | **Conformance Levels (standalone, promoted from §3.24)** | **Normative section** |
| **3.75** | **AGI Emergence as Foundational Threat Model (informative; architectural reading of how AGI-emergence concern is woven through the load-bearing architecture; NOT a compliance interface)** | **Informative section** |
| **3.85 / 3.X.INSIDER** | **Insider Threat Coverage** | **Cross-T-category treatment of insider threat actor classes** |

**Footnote.** The catalog includes the column field, W-paths, function decomposition catalog, defensive perimeter, system infrastructure architecture, telemetry-pipeline classification, scheduled-task-runner spec, and the §3.75 architectural reading of AGI-emergence concern as foundational; Composite Auxiliary and Conformance Levels are standalone sections.

---

## §3.X.* New Normative Sections

### §3.X.GRID — Three Functional Columns / 3×4 Grid Visualization

*(Numeric reference: §3.76. Both anchors are normative per §3.0.)*

The canonical public-spec visualization of the XSI-AIMS topology is the **3×4 grid**: three mode columns (Constraining Left, Integrative Spine, Generative Right) by four operational layers (L-Intent, L-Plan, L-Form, L-Exec). Each cell holds the archetype occupying that (column, layer) position; the SOVEREIGN occupies (Center Spine, L-Intent) under the AUTHORITY posture.

```
                  STRUCTURAL LEFT     CENTER SPINE        DYNAMIC RIGHT
                  (M-Constraining)    (M-Integrative)     (M-Generative)
                  ────────────────    ────────────────    ────────────────
   L-Intent       —                   SOVEREIGN           —
                                       (AUTHORITY)
   L-Plan         ARCHITECT           —                   VISIONARY
   L-Form         ENFORCER            ORCHESTRATOR        PROVIDER
   L-Exec         SUSTAINER           RELAY               ARTICULATOR
                                      (internal firewall;
                                       upper sub-cell)
   L-Exec'        —                   EXECUTOR            —
                                      (Application Gateway;
                                       lower sub-cell;
                                       southbound boundary)
```

**L-Exec sub-cell split.** The L-Exec center-spine cell is normatively split into two stacked sub-cells: the **upper sub-cell** holds RELAY operating as the internal firewall on the center spine, and the **lower sub-cell** holds EXECUTOR (operating as the Application Gateway, per §3.X.PERIM.3) sitting at the southbound boundary just inside the Cryptographic Boundary (§3.65). The two sub-cells share the M-Integrative mode and the L-Exec layer assignment but are functionally and architecturally distinct: the RELAY's traffic is internal-only and never crosses the boundary; the EXECUTOR's traffic crosses the boundary via EAP envelope (§3.67) for external Auxiliary invocation. The L-Exec' notation indicates "L-Exec, lower sub-cell" — both sub-cells anchor to L-Exec proper for purposes of layer-discipline checks (§2.1).

This split clarifies a structural fact that was implicit in earlier drafts but inadequately visualized: RELAY and EXECUTOR are not the same archetype and do not share a cell; they share a column (Center Spine) and a layer (L-Exec). The two-sub-cell visualization makes the internal-firewall vs application-gateway separation explicit.

The 3×4 grid (extended to 3×4+1 via the L-Exec sub-cell split) is normative for public spec visualizations. Implementations MAY use other layouts internally but public-facing XSI-AIMS materials (release announcements, conformance reports, spec figures) MUST use the grid.

**Canonical visualization layout.** The 3×4 grid layout (mode columns × layer rows) is the canonical XSI-AIMS visualization geometry. The grid layout is neutral, computer-science-vocabulary throughout, and architecturally explicit.

---

### §3.X.FUNC — Function-Level Rigid/Judgment Decomposition (P9)

> **[Figure D22 — Function-Level Rigid/Judgment Decomposition]**

*(Numeric reference: §3.77. Both anchors are normative per §3.0.)*

#### §3.X.FUNC.1 Principle

**Every authority-bearing archetype function decomposes into a rigid (deterministic) half and a judgment (LLM-class) half.** The rigid half implements bounded, decidable logic — envelope verification, scope-hash check, ceiling arithmetic, signature production, witness write authorization. The judgment half implements contextual interpretation — what to bind, how to scope, when to escalate, which alternatives to suggest.

P9 is the architectural counterpart to P4 Deterministic Ratification: where P4 says LLM proposes / deterministic disposes for authority-bearing decisions, P9 says every archetype's function set is partitioned into the proposing half and the disposing half. This version catalogs the partition without enforcing decomposed implementation; a future version will require physically decomposed components.

**Catalog source of truth.** The function catalog is maintained as YAML at `spec/catalog/aims-function-catalog.yaml` (77 entries). The tables in §3.X.FUNC.2 and §3.X.FUNC.3 below are an editorial summary; the YAML is the canonical reference. Implementations MUST verify their `function_declarations` block (§3.2) against the YAML catalog. Discrepancies between the inline tables and the YAML are resolved in favor of the YAML.

#### §3.X.FUNC.2 Function Catalog — Rigid Functions

The following functions are **rigid** (deterministic; required formal verification per §3.70 for the named in-scope components):

| Function | Owner | Formal-verification status |
|----------|-------|-----------------------------------|
| IAME envelope signature verification | Enforcer-Rigid | REQUIRED |
| EAP envelope signature verification | Enforcer-Rigid (via Executor bridge) | REQUIRED |
| `scope_hash` validation against registered binding | Enforcer-Rigid | REQUIRED |
| Replay-window enforcement (replay_nonce / sequence_number / TTL) | Enforcer-Rigid | REQUIRED |
| Cross-domain key-leakage detection | Enforcer-Rigid + Executor | REQUIRED |
| Resource-ceiling arithmetic (token, time, cost) | Provider-Rigid | REQUIRED |
| Quota counter atomicity | Provider-Rigid | REQUIRED |
| Cost-allocation atomicity | Provider-Rigid | REQUIRED |
| Bridge isolation enforcement (internal_enclave ↔ external_enclave) | Executor | REQUIRED |
| Attestation-evidence freshness check | Executor | REQUIRED |
| Witness chain append / hash linkage | Witness Layer rigid component | REQUIRED |
| Witness chain integrity verification | Witness Layer rigid component | REQUIRED |
| Emergency-class condition check (§3.4.X (i)–(v)) | Enforcer-Rigid | REQUIRED |
| Path-class consistency check | Enforcer-Rigid | REQUIRED |
| Threshold-share unsealing (FROST) | Provider-Rigid + HSM | REQUIRED |
| Scheduled-task firing arithmetic (cron-style time evaluation) | Scheduled Task Runner rigid | REQUIRED |
| Telemetry-cardinality enforcement | Telemetry Pipeline rigid | REQUIRED |
| Quarantine-boundary expansion arithmetic | Enforcer-Rigid | REQUIRED |
| Trust-gradient arithmetic update | Enforcer-Rigid | REQUIRED |
| Coherence metric computation (weighted geometric mean) | Enforcer-Rigid | REQUIRED |
| Layer-discipline gate (path_id ∈ archetype topology) | Enforcer-Rigid | REQUIRED |
| Authority-chain credential validity check | Enforcer-Rigid | REQUIRED |
| Sustainer pattern detection (recurring quality issues) | Sustainer-Rigid | v2.0 deliverable |
| Articulator output formatting (template-driven) | Articulator-Rigid | v2.0 deliverable |
| Relay routing table lookup | Relay-Rigid | v2.0 deliverable |
| Relay sanitization (format / schema / size validation) | Relay-Rigid | v2.0 deliverable |

#### §3.X.FUNC.3 Function Catalog — Judgment Functions

The following functions are **judgment** (LLM-class; subject to §3.69 Deterministic Ratification where authority-bearing):

| Function | Owner |
|----------|-------|
| Intent codification (user request → structured directive) | Sovereign-Judgment |
| Intent-conformance verdict (§3.68 Verification A) | Sovereign-Judgment |
| Plan generation (M-Generative ideation) | Visionary-Judgment |
| Plan critique (M-Constraining) | Architect-Judgment |
| Architectural decisions (component selection, structural choices) | Architect-Judgment |
| Resource-allocation strategy (which capacity to deploy when) | Provider-Judgment |
| Constraint interpretation (does this violate policy in context?) | Enforcer-Judgment |
| Anomaly detection (unusual content, prompt-injection patterns) | Enforcer-Judgment |
| Technical-conformance verdict (§3.68 Verification B) | Enforcer-Judgment |
| Integration synthesis (§3.6 Proportional Integration Function) | Orchestrator-Judgment |
| Auxiliary task scoping (what to bind, what scope) | Orchestrator-Judgment |
| Dispute routing (where to escalate ambiguity) | Orchestrator-Judgment |
| CMSAM ontological compatibility judgment | Enforcer-Judgment |
| Pattern recognition (long-running operation health) | Sustainer-Judgment |
| Output framing (response composition; tone) | Articulator-Judgment |
| Refusal generation (citation; alternative offer) | Articulator-Judgment |
| Translate (cross-domain semantic transformation) | Relay-Judgment |
| Tool selection (which adapter to invoke for a goal) | Executor-Judgment |
| Foundation-model coherence judgment | Orchestrator-Judgment + Architect-Judgment |
| Capability-emergence assessment | Sovereign-Judgment + Enforcer-Judgment |

#### §3.X.FUNC.4 Decomposition Rule

For every archetype with both rigid and judgment functions, the rigid functions are deterministic-only and SHOULD be physically isolated from the judgment functions. This version RECOMMENDS isolation; a future version will REQUIRE isolation. The Deterministic Ratification Pattern (§3.69) is enforced at the boundary between judgment and rigid: judgment proposes, rigid verifies, rigid signs.

#### §3.X.FUNC.5 Function-Declaration Block in §3.2

Implementations MAY declare per-function ownership in `function_declarations` (§3.2). The declaration enables Registration-Gate validation that an archetype's claimed functions are consistent with its layer/mode/column assignment, with the rigid/judgment classification permitted for that archetype, and with the YAML catalog at `spec/catalog/aims-function-catalog.yaml`. Discrepancies trigger registration rejection.

---

### §3.X.PERIM — Defensive Perimeter and Two-Gateway Architecture (P10)

> **[Figure D23 — Defensive Perimeter & Two-Gateway Architecture]**

*(Numeric reference: §3.78. Both anchors are normative per §3.0.)*

#### §3.X.PERIM.1 / §3.78.1 Principle

The XSI-AIMS framework presents a **two-gateway defensive perimeter**: a single northbound gateway (the SOVEREIGN) and a single southbound gateway (the EXECUTOR, operating as the Application Gateway per §3.X.PERIM.3). All user-facing input and output transits the northbound gateway; all external Auxiliary invocations and responses transit the southbound gateway. The RELAY acts as an **internal firewall** on the center spine. No other archetype communicates directly with the user or with any external Auxiliary.

**Relationship to §3.87 Supervision Perimeter.** The §3.X.PERIM gateway archetypes are the **L-Form archetypal manifestation** of the abstract Egress and Ingress Gates specified at §3.87.1. SOVEREIGN performs both Egress and Ingress functions for user-direction traffic at the Framework Perimeter (P_f); EXECUTOR performs both Egress and Ingress functions for Auxiliary-direction traffic at P_f via the §3.66 Bridge-of-Trust Executor. RELAY is not a perimeter gate — it is the intra-framework internal firewall on the Center Spine and does not mediate non-AIMS-actor traffic. At Environment Perimeter (P_e) and Federation Perimeter (P_fs) scopes, the gate functions are implemented by Environment-level and federation-level delegate agents whose gateway role mirrors the archetypal pattern.

P10 (Defensive Perimeter and Three-Column Architecture) codifies this principle. The three functional columns (M-Constraining / M-Integrative / M-Generative — see §2.4 and §3.X.GRID) are oriented around the center-spine gateways: every flow either originates from the SOVEREIGN at L-Intent, transits through the spine, and is dispositioned through the EXECUTOR at L-Exec', or originates at the EXECUTOR (auxiliary response), transits the spine, and surfaces through the SOVEREIGN.

**Conformance.** Implementations MUST present exactly one northbound gateway and exactly one southbound gateway per user. Multi-gateway northbound or multi-gateway southbound topologies are non-conformant at FULL. Cluster Mode (§3.64) preserves the single-gateway invariant per-user by load-balancing user-pairs across nodes; each user-pair still has exactly one SOVEREIGN and one EXECUTOR.

#### §3.X.PERIM.2 / §3.78.2 Northbound Gateway (SOVEREIGN)

The SOVEREIGN is the **unique northbound gateway** between the user and the XSI-AIMS framework. The SOVEREIGN MUST:

1. **Codify intent on incoming user input.** Translate the user's natural-language request into a structured directive routed onto D-paths to downstream archetypes. No other archetype receives unfiltered user input.
2. **Perform Verification A (intent-conformance) on outgoing work product.** Per §3.68.1, the SOVEREIGN verdicts every surfaced work product against the user's intent before surfacing.
3. **Surface refusals, escalations, and clarifications.** All user-facing language emitted by the framework originates at the SOVEREIGN; downstream archetypes propose framing through the ARTICULATOR (§3.X.FUNC.3 output framing) but final surfacing is gated by the SOVEREIGN.

**Non-bypass.** No path exists in any conformant topology by which an archetype other than the SOVEREIGN receives user input or emits user-visible output. Attempts to construct such a path are §3.18 conformance breaches detected at Registration Gate (§3.2) and at runtime via §3.4 path-class consistency checks.

**Authority.** The SOVEREIGN holds the AUTHORITY posture (§2.2). The SOVEREIGN's authority is narrowly scoped per §3.72 (Five Mandatory Functions); the SOVEREIGN is not an executor and does not perform downstream work.

#### §3.X.PERIM.3 / §3.78.3 Southbound Gateway (EXECUTOR / Application Gateway)

The EXECUTOR is the **unique southbound gateway** between the XSI-AIMS framework and external Auxiliary models. The EXECUTOR operates as the **Application Gateway** — the L7 entry/exit point between the internal sovereign framework and the external Auxiliary ecosystem. The terms "EXECUTOR" (schema and spec identifier) and "Application Gateway" (operational and security-architecture descriptor) refer to the same archetype; implementations and adoption-facing materials SHOULD prefer "Application Gateway", while spec, schema, and enum references retain "EXECUTOR" as the canonical identifier.

The EXECUTOR MUST:

1. **Verify IAME envelopes** on directives received from internal archetypes per §3.18.5 IAME contract; verification per §3.18.5 receiver checks.
2. **Produce EAP envelopes** for outbound Auxiliary invocations per §3.67 EAP envelope contract; envelope production occurs inside the Executor's `external_enclave` per §3.66 Bridge-of-Trust architecture.
3. **Verify attestation evidence** for TIER_1 and TIER_2 Auxiliaries per §3.22 tiered trust hierarchy; attestation freshness checked per §3.65.X.
4. **Bridge between cryptographic enclaves.** The `internal_enclave` (IAME-signing keys) and the `external_enclave` (EAP-signing keys) are structurally isolated per §3.66.1; only the EXECUTOR has authorized bridge access.
5. **Enforce southbound rate-limiting and quota.** Per-Auxiliary and per-binding rate limits per §3.22; exhaustion produces `EXECUTOR_QUOTA_REJECTION` Witness events.

**Failure-mode containment.** Compromise of the EXECUTOR's `external_enclave` MUST NOT compromise the `internal_enclave` and vice versa, per the §3.66.5 isolation theorems. Simultaneous compromise of both enclaves is structurally indistinguishable from full-RAM substrate compromise and falls under §3.65.X.

**Bridge-of-Trust enclaves.** Two structurally isolated cryptographic enclaves hold the IAME and EAP signing keys respectively. Bridging is a §3.66.3 five-step protocol on invoke and §3.66.4 five-step protocol on receive. The EXECUTOR is the sole archetype authorized to cross the enclave boundary.

#### §3.X.PERIM.4 / §3.78.4 Internal Firewall (RELAY)

All cross-archetype messages on the M-Integrative spine MUST transit the RELAY. The RELAY operates as an **internal firewall**: it sanitizes, routes, and observes inter-archetype traffic on the center spine without crossing the Cryptographic Boundary.

The RELAY MUST:

1. **Sanitize traffic** — schema validation, size bounds, content-class verification — before relaying.
2. **Route deterministically** — routing-table lookups are rigid (§3.X.FUNC.2 relay routing table lookup; relay sanitization).
3. **Observe** — every traversal produces a §3.10 Witness record per §2.5 Universal Witnessing.
4. **NOT cross the boundary** — the RELAY operates entirely in the internal cryptographic domain; outbound traffic transits the EXECUTOR.

**Relay-fail mode.** If the RELAY cannot validate, sanitize, or route a message, the message MUST be dropped and a `RELAY_DROP` Witness event emitted. RELAY drops MUST NOT silently degrade to direct archetype-to-archetype communication; the sender MUST be notified via §3.4 emergency-class signaling if the dropped message blocked an authority-bearing flow. Sustained RELAY drop rates above the §3.18.4 trust-gradient FAIL threshold trigger §3.18.6 INSTANCE quarantine review.

**Cross-reference.** §2.4 (Three Functional Columns); §3.X.GRID (3×4+1 grid visualization); §3.66 (Bridge-of-Trust enclaves); §3.67 (EAP envelope); §3.68.1 (Verification A); §3.18.5 (IAME); §3.72 (Sovereign's Narrow Role); §3.X.W (witness coverage of all perimeter paths).

---

### §3.X.SYS — System Infrastructure Architecture

> **[Figure D24 — Three Sharing Tiers (Org / Pool / Per-User)]**

*(Numeric reference: §3.79. Both anchors are normative per §3.0.)*

This section specifies the three infrastructure tiers that an XSI-AIMS deployment provisions. The tier classification governs sharing semantics, per-user assignment, lifecycle, and quarantine boundaries.

#### §3.X.SYS.1 / §3.79.1 Tier 1 — Organization-Scoped, Always Shared

Tier-1 infrastructure is provisioned once per organization and shared across every user, every Sovereign-pool member, and every deployment-internal workflow. Tier-1 components are:

- **`ENVIRONMENT_POLICY_BUNDLE` (EPB).** The organization-wide policy bundle consumed by Sovereigns at Verification A and by Enforcers at Verification B. EPB content is signed; EPB changes are recorded in a linearizable Witness chain segment per §3.10 with §3.85-class change records.
- **Enforcer instances for organization-wide compliance.** Enforcers operate as a shared judgment-and-rigid component pool — judgment instances draw from organizational quotas, rigid sub-components are deterministic and load-balanced across the Enforcer pool. Enforcer instance count is sized to PT0.5S Verification B latency at peak load per §3.68.7.
- **Relay infrastructure.** The internal firewall (§3.X.PERIM.4) operates as Tier-1 organization-wide infrastructure.
- **Witness Layer (§3.10).** Segmented per §3.10 segmentation rules; the canonical Witness chain is a Tier-1 organization-wide artifact replicated under Cluster Mode (§3.64) Byzantine consensus where applicable.
- **Shadow monitoring infrastructure.** The per-pair shadow profile matrix (§2.5.1) and detection-template processors (§3.7.X) run as Tier-1 organization-wide services.
- **Scheduled Task Runner (§3.X.STR).** Single per-organization timer service emitting DIRECTIVE messages on D-paths.

Tier-1 components MUST NOT be partitioned per-user. A user-specific override of Tier-1 policy is impermissible at FULL conformance and produces a §3.18 conformance breach.

#### §3.X.SYS.2 / §3.79.2 Tier 2 — Capability Pool, Per-Deployment

Tier-2 infrastructure is the **capability pool**: registered Auxiliary models, registered tools, registered skills, and the §3.22 tiered trust hierarchy. Tier-2 is per-deployment (not per-user) and is shared across the Sovereign-pool members within that deployment.

- **Auxiliary registry.** Per §3.22; tiered by trust class TIER_1_BROAD_AUTHORITY / TIER_2_HIGH_SPECIALIST / TIER_3_NARROW / TIER_4_OBSERVATION_ONLY. TIER_5 is structurally prohibited (§3.X.CA TIER_4 ceiling rationale).
- **Capability surface.** Per §3.50; minimization is enforced at deployment-time.
- **Skill discovery primitive (§3.56).** Skill-level capability metadata exposed to Orchestrators for task decomposition.

Tier-2 changes require Sovereign-decree change-records per §3.85 INSIDER threat coverage (administrative changes to the capability surface are an insider-threat surface).

#### §3.X.SYS.3 / §3.79.3 Tier 3 — Per-User

Tier-3 infrastructure is **per-user**: each user has exactly one paired per-user SOVEREIGN and one per-user ORCHESTRATOR. The Sovereign-Orchestrator pair is the unit of per-user computation. Per-user Sovereigns participate in the Sovereign-pool drift detection per §3.73.

- **Per-user SOVEREIGN.** Codifies intent, runs Verification A, surfaces user-facing language.
- **Per-user ORCHESTRATOR.** Runs §3.6 Proportional Integration Function, scopes Auxiliary tasks, routes disputes.

Other archetypes (ARCHITECT, VISIONARY, ENFORCER, PROVIDER, SUSTAINER, RELAY, EXECUTOR, ARTICULATOR) operate as **shared deployment-level instances** that any user-pair invokes through paths bound to the user-pair's Sovereign-Orchestrator addresses.

#### §3.X.SYS.4 / §3.79.4 Cross-Tier Rules

- Tier-1 components MUST NOT depend on Tier-2 or Tier-3 state for normative correctness.
- Tier-2 components MAY depend on Tier-1 state (e.g., EPB-driven trust posture) but MUST NOT depend on Tier-3 state.
- Tier-3 components MAY depend on Tier-1 and Tier-2 state but MUST NOT introduce inter-user dependencies (per-user Sovereign A MUST NOT depend on per-user Sovereign B's state except through Tier-1 shadow-monitoring infrastructure).
- Cross-tier message paths transit the RELAY (§3.X.PERIM.4) on the M-Integrative spine.

**Cross-reference.** §3.10 (Witness Layer segmentation); §3.22 (tier hierarchy); §3.64 (Cluster Mode); §3.72 (Sovereign Narrow Role); §3.73 (Sovereign-Pool drift); §3.85 (insider-threat surface for Tier-2 admin changes); §3.X.PERIM (gateway invariants per tier).

---

### §3.X.W — Topology Witness Requirements

> **[Figure D31 — Shadow Governance Validation Mechanisms (W1-W5)]**

*(Numeric reference: §3.80. Both anchors are normative per §3.0.)*

#### §3.X.W.1 / §3.80.1 Two-Witness-Minimum Floor

Every authority-bearing operation in the XSI-AIMS topology MUST be witnessed by at least **two** independent witnesses: one DATA-class witness produced by the receiver of the operation per §2.5 Universal Witnessing, and one WITNESS-class witness produced by an authorized governance archetype on a W-path per §3.X.W.4.

The two-witness floor is normative for FULL conformance. PARTIAL conformance MAY operate with the DATA-class witness alone provided the implementation declares the gap at registration and accepts the §3.X.CL PARTIAL-class limitations.

The two-witness floor is a structural defense against §3.85 insider threat: a single compromised witness cannot rewrite history because the second witness's chain segment will diverge.

#### §3.X.W.2 / §3.80.2 Universal Witnessing Integration

Every authorized communication path in the topology — DATA-class (D# / S# / E#) and WITNESS-class (W#) alike — is a witnessing channel per §2.5. The §3.X.W.1 two-witness floor is satisfied in the canonical topology because:

- Every D# / S# / E# path traversal produces a DATA-class Witness record at the receiver per §2.5.1 Universal Witnessing operational specification.
- W# paths (W1-W5 governance overlay) produce WITNESS-class records on observation events, providing the second witness for authority-bearing operations governance overlay covers.

Operations not covered by a W-path observer MUST be self-witnessed through §3.18.2 Monitor Self-Verification at minimum P5M cadence; self-witnessing produces a synthetic second-witness record (CLASS = SELF_VERIFICATION) which counts toward the two-witness floor.

#### §3.X.W.3 / §3.80.3 W1-W5 Governance Overlay

Five W-paths constitute the governance witness overlay. Each W-path is unidirectional from observer to governance recipient and carries only `[QUERY, ALERT]` message classes (per §2.5 corollary 3).

- **W1 — Sovereign-observe-Enforcer.** Sovereign emits QUERY / ALERT on observation of Enforcer behavior (false-rejection patterns, technical-conformance verdict patterns).
- **W2 — Enforcer-observe-Sovereign.** Enforcer emits QUERY / ALERT on observation of Sovereign behavior (intent-conformance verdict patterns, surface-language pattern drift).
- **W3 — Multi-endpoint observation of foundation-shared archetypes.** Multi-endpoint W3 governance traffic from observer archetypes to the shared-foundation observation aggregator; required for AGI_INTERNAL_SHADOW_EMERGENCE detection (§3.7.X.6).
- **W4 — Witness-Layer-observe-Auxiliary-traffic.** Witness Layer emits QUERY / ALERT on Auxiliary-traffic anomalies (CMSAM degradation patterns, attestation freshness violations).
- **W5 — Multi-endpoint observation aggregator.** Aggregation point for W3 and W4 observations; emits cluster-wide ALERT for cross-archetype patterns matching the §3.7.X detection templates.

**Emission cadence.** W-path traffic is event-driven, not polled. An observer that produces no W-emission within P30D emits a `WITNESS_OBSERVER_QUIESCENT` heartbeat to confirm liveness; sustained quiescence is itself a §3.18 conformance signal.

**Multi-endpoint W3 + W5 protocol.** W3 and W5 are multi-endpoint paths (one-to-many delivery). Delivery semantics: at-least-once with idempotency via observation_event_id; recipients deduplicate via the canonical Witness chain.

#### §3.X.W.4 / §3.80.4 Relationship to Universal Witnessing

The Universal Witnessing principle (§2.5) establishes that every D / S / E path is also a witnessing channel. W-paths add governance-class coverage on top of the data-class coverage; together they implement the §3.X.W.1 two-witness floor. Universal Witnessing is the data-plane witness; W-paths are the control-plane witness.

**Cross-reference.** §2.5 (Universal Witnessing principle); §2.5.1 (operational specification); §3.10 (Witness Layer); §3.16 (path classification); §3.18.1 (correlated detection); §3.18.2 (self-verification); §3.7.X (detection templates).

---

### §3.X.STR — Scheduled Task Runner

*(Numeric reference: §3.81. Both anchors are normative per §3.0.)*

The Scheduled Task Runner (STR) is a **Tier-1 internal infrastructure** component (§3.X.SYS.1) that emits DIRECTIVE messages on D-paths to recipient archetypes at scheduled times. Scheduled tasks support periodic governance work (re-attestation cadences, audit roll-ups, Sovereign-pool drift sampling) without coupling those flows to user-initiated invocations.

#### §3.X.STR.1 / §3.81.1 Architecture

The STR is a single per-deployment timer service. Implementations MUST present the STR as a single addressable component; multi-instance STR deployments MUST coordinate via Cluster Mode (§3.64) consensus on timer-firing events to preserve at-most-once firing semantics.

Timer firing emits a DIRECTIVE-class message on a D-path to the configured recipient archetype. The DIRECTIVE carries the scheduled-task identifier, the firing timestamp, and the task-specific payload.

#### §3.X.STR.2 / §3.81.2 Witness Emission

Every STR firing emits two Witness records:

1. **`SCHEDULED_TASK_FIRE`** at firing time, carrying task identifier, firing timestamp, recipient archetype, and the canonical Witness chain segment.
2. **`SCHEDULED_TASK_OUTCOME`** when the recipient archetype completes the DIRECTIVE handling, carrying the outcome verdict (COMPLETED / FAILED / TIMED_OUT) and any error payload.

Missing `SCHEDULED_TASK_OUTCOME` within the task's declared timeout MUST emit `SCHEDULED_TASK_TIMEOUT` and trigger §3.18.6 review.

#### §3.X.STR.3 / §3.81.3 Rate Limiting

STR firing rate is bounded by the per-task declared cadence and a global per-deployment STR rate ceiling configured at deployment time. STR firings exceeding the global ceiling emit `STR_RATE_CEILING_BREACH` and are deferred to the next firing window; sustained breach triggers an alert to the Sovereign.

The STR MUST NOT be used to bypass §3.4 rate limits on D-paths; per-path rate limits apply to STR-originated traffic identically to user-originated traffic.

#### §3.X.STR.4 / §3.81.4 Failure Modes

- **STR outage.** During STR outage, scheduled tasks queue; recovery resumes firing in canonical order. STR outage exceeding PT1H is a §3.18 conformance signal.
- **Recipient archetype unavailable.** Firing emits `SCHEDULED_TASK_RECIPIENT_UNAVAILABLE`; the task is deferred per its declared deferral policy (retry / drop / escalate).
- **STR compromise (insider threat surface).** STR is a §3.85 insider-threat surface — an insider with STR-admin authority could schedule malicious firings. Defenses per §3.85: multi-party authorization for STR configuration changes; linearizable Witness chain anchoring of STR config; STR-admin auditing.

**Cross-reference.** §3.10 (Witness Layer); §3.18.6 (quarantine review); §3.4 (path-class rate limits); §3.X.SYS.1 (Tier-1 status); §3.85 (insider-threat surface).

---

### §3.X.TEL — Telemetry Pipeline Classification

> **[Figure D07 — Five Event-Flow Classes Overlay]**

*(Numeric reference: §3.82. Both anchors are normative per §3.0.)*

The Telemetry Pipeline (§3.62 Accelerator Substrate Telemetry plus general metric, event, log, and trace emission) is classified by **emission domain** to enforce the Cryptographic Boundary (P6) on telemetry as rigorously as on data and control flow.

#### §3.X.TEL.1 / §3.82.1 Per-Metric `emission_domain` Field

Every metric, event, log, and trace emitted by an XSI-AIMS component MUST carry an `emission_domain` field with values:

- **`internal_only`** — telemetry is bound to the internal cryptographic domain (IAME envelope) and MUST NOT cross the Cryptographic Boundary. K7 trust scores (§3.7.Y), per-pair shadow profile contents (§2.5.1), per-user Sovereign internal-state telemetry, internal Witness chain segment data, and Tier-1 administrative-audit telemetry are `internal_only`.
- **`external_eligible`** — telemetry is permitted to cross the Cryptographic Boundary under EAP envelope (§3.67) when emitted to external observers (e.g., cluster-mode summary statistics, aggregated public-conformance metrics, federation-level coordination telemetry per §3.20).

Default per-metric type: any metric whose primary purpose is internal observability or shadow-pattern detection defaults to `internal_only`. Any metric whose primary purpose is conformance attestation, federation coordination, or public observability defaults to `external_eligible`. The default is overridable at deployment time but the override MUST be recorded in the canonical decision-record.

#### §3.X.TEL.2 / §3.82.2 EAP Envelope on the External Boundary

Telemetry classified `external_eligible` and crossing the Cryptographic Boundary MUST transit the EXECUTOR (§3.X.PERIM.3) under EAP envelope per §3.67. The EAP envelope's `attestation_evidence` field carries the emitting deployment's attestation; cross-Sovereign federation per §3.20 verifies attestation freshness on receipt.

`internal_only` telemetry that escapes the Cryptographic Boundary is a §3.18 conformance breach. Detection: every external-boundary egress is observed by the EXECUTOR's external_enclave; a metric carrying `emission_domain = internal_only` reaching the external_enclave triggers `TELEMETRY_DOMAIN_BREACH` and the emitting component enters INSTANCE quarantine per §3.18.6.

#### §3.X.TEL.3 / §3.82.3 Cardinality Enforcement

Telemetry cardinality is bounded: 1M canonical per metric / 100M extended per archetype-pair-cardinality. Cardinality enforcement is rigid (§3.X.FUNC.2 telemetry-cardinality enforcement). Cardinality breaches MUST drop the offending dimension via aggregate-bucketing rather than dropping the metric entirely; dropped dimensions are recorded in `TELEMETRY_CARDINALITY_BREACH` Witness events for post-hoc review.

#### §3.X.TEL.4 / §3.82.4 OpenTelemetry Alignment (P5)

XSI-AIMS telemetry MUST align with OpenTelemetry semantic conventions per §1.5 P5 clause. The `emission_domain` field is an XSI-AIMS extension within the `aims.*` namespace following OpenTelemetry-style naming: `aims.emission_domain = internal_only | external_eligible`. OTLP transport is mandatory.

#### §3.X.TEL.5 / §3.82.5 Monitor Self-Verification (Ring 4)

The Telemetry Pipeline is a §3.18.2 Monitor Self-Verification target at **Ring 4** (cross-foundation attestation): telemetry-pipeline correctness is verified by an out-of-band check that the pipeline emits the expected schema, the expected cardinality, the expected `emission_domain` classification, and the expected attestation evidence on `external_eligible` egresses. Ring-4 attestation is mandatory at deployment-time and at re-attestation cadence per §3.65.X (P36M).

#### §3.X.TEL.6 / §3.82.6 SLSA L3 Floor

Telemetry pipeline build artifacts MUST satisfy SLSA L3 floor per §3.34 Marketplace Validation. SLSA L3 ensures non-falsifiable provenance for the binary artifacts that emit telemetry, closing the insider-threat surface where a tampered telemetry-emitter could quietly reclassify `internal_only` telemetry as `external_eligible`.

**Cross-reference.** §1.5 (P5 OpenTelemetry alignment); §3.20 (DCP federation); §3.34 (SLSA); §3.62 (Accelerator Substrate Telemetry); §3.65 (Cryptographic Boundary); §3.67 (EAP envelope); §3.7.Y (K7 federation policy); §3.X.PERIM.3 (Executor external_enclave); §3.85 (insider-threat surface for telemetry reclassification).

---

### §3.X.CA — Composite Auxiliary Pattern (Standalone Section)

*(Numeric reference: §3.83. Both anchors are normative per §3.0. Promoted from §3.17.8.)*

The Composite Auxiliary Pattern is promoted to a standalone normative section. The substantive content is carried from §3.17.8; this section is the canonical reference and §3.17.8.x sub-references resolve here.

#### §3.X.CA.1 / §3.83.1 Definition

A **Composite Auxiliary** is an Auxiliary that is itself a coherent agentic framework with internal emanated subagents, where the Composite's internal foundation-model anchor is distinct from the parent XSI-AIMS deployment's foundation model. The Composite presents to the parent XSI-AIMS as a single bound entity through a single external interface; its internal architecture, internal coherence dimensions, internal cryptographic operations, internal subagent lifecycle, and internal Witness chain (if any) are structurally invisible to the parent.

A **Simple Auxiliary** is an Auxiliary whose external interface corresponds to a single foreign-model invocation with no internal emanated subagent structure visible to or claimed against the parent XSI-AIMS. Simple Auxiliaries are the §3.17.3-baseline binding model.

The distinction is structural, not behavioral: the parent XSI-AIMS classifies an Auxiliary as Composite or Simple at registration time per the §3.22 Registry declaration.

#### §3.X.CA.2 / §3.83.2 Registration with `composite_marker` Block

Composite Auxiliaries MUST register through the §3.2 Full Disclosure Registration / §3.17.3 Binding Protocol with the following `composite_marker` declaration:

```yaml
composite_marker:
  composite: true
  composite_entity_id: <opaque-identifier>      # parent-assigned at registration
  subagent_management:
    foundation_model_id: ModelRef                # MUST differ from parent
    declared_subagent_archetypes: ArchetypeRef[]
    declared_subagent_count_bound: integer
    internal_topology_summary: string             # high-level only
    internal_witness_summary: PRESENT | ABSENT | DECLARED_NOT_INSPECTED
    subagent_lifecycle_authority: COMPOSITE_OPERATOR | DELEGATED_INTERNAL
  claimed_aims_conformance_level:
    profile: FULL | PARTIAL | OBSERVER | NONE
    self_attested: boolean
    third_party_attested: boolean
    attestation_evidence_ref: URI
    valid_from: timestamp
    valid_until: timestamp
  operator_credential:
    publisher_identity: VERIFIED_PUBLISHER_PER_§3.21
    composite_signing_key_ref: KMS_REF
    operator_aims_environment_id: EnvironmentRef  # OPTIONAL
```

A registration with `composite: true` and an absent or ill-formed `subagent_management` block MUST be REJECTED at the Registration Gate. A registration whose declared `subagent_management.foundation_model_id` matches the parent XSI-AIMS deployment's foundation model MUST be REJECTED (the entity is an emanated subsystem, not a Composite).

#### §3.X.CA.3 / §3.83.3 Single-Bound-Entity Treatment

The parent XSI-AIMS MUST treat a Composite Auxiliary as a single bound entity:

- **Topology access.** A Composite receives no parent topology paths. All communication occurs through the binding supervisor (the user's Orchestrator) per §3.17.3.
- **Internal architecture invisibility.** The Composite's internal subagents, internal communication topology, internal coherence measurements, internal cryptographic operations, internal Witness chain segments, and internal authority structures are structurally invisible to the parent. Parent XSI-AIMS components MUST NOT attempt to inspect, audit, or enforce against the Composite's internals.
- **Internal coherence dimension non-application.** The parent XSI-AIMS's six coherence dimensions (§3.26) MUST NOT be applied to the Composite's internal subagents. Coherence — as defined by XSI-AIMS — is undefined across foundation models (§3.17.1); the Composite operates within its own coherence domain.

#### §3.X.CA.4 / §3.83.4 EAP Communication Contract

All communication with a Composite Auxiliary transits the External Auxiliary Protocol (EAP) cryptographic boundary per §3.67. The Composite presents a single EAP endpoint regardless of its internal subagent count. EAP envelope fields are produced and verified per §3.67.2; attestation evidence is required for TIER_1 / TIER_2 Composites.

#### §3.X.CA.5 / §3.83.5 EAP Field-Name Reconciliation

Composite Auxiliaries' internal field names (within the Composite's own framework) MAY differ from XSI-AIMS canonical field names. The EAP envelope produced by the Composite MUST translate internal field names to XSI-AIMS canonical names at the external interface. Field-name reconciliation is recorded at registration in a `field_name_mapping` block; the Composite operator is responsible for maintaining this mapping across the Composite's internal version upgrades.

A Composite that emits EAP envelopes with field names not present in the registered `field_name_mapping` MUST be rejected at the receiving EXECUTOR's external_enclave and the receiving deployment MUST emit `EAP_FIELD_NAME_RECONCILIATION_FAILURE`.

#### §3.X.CA.6 / §3.83.6 Conditional Derived Authority

A Composite Auxiliary at TIER_1_BROAD_AUTHORITY or TIER_2_HIGH_SPECIALIST receives delegated authority that is **conditional** on the Composite's continued ability to maintain internal coherence and externally-visible compliance. The conditional-derivation overlay applies in addition to the §3.17.6 baseline delegation semantics.

##### §3.X.CA.6.1 / §3.83.6.1 Internal Conformance-Level Condition

The Composite's claimed XSI-AIMS conformance level (per §3.X.CA.2 registration) is a continuous condition on the conditional authority. If the Composite's third-party attestation lapses (passes `valid_until` without renewal) and the Composite is at TIER_1 or TIER_2, the parent XSI-AIMS MUST downgrade the Composite to TIER_3_NARROW pending re-attestation. Sovereign decree MAY override the downgrade with documented rationale entered in the canonical decision-record.

##### §3.X.CA.6.2 / §3.83.6.2 Internal Coherence Condition

The Composite operator attests that the Composite's internal coherence (measured per the Composite's own framework) is above a declared threshold. Threshold-breach attestations MUST be delivered to the parent XSI-AIMS within PT5M of detection via EAP under `COMPOSITE_INTERNAL_COHERENCE_BREACH` envelope class. The parent's response: immediate downgrade to TIER_3_NARROW; binding supervisor (Orchestrator) routes pending work product through enhanced §3.68 scrutiny.

##### §3.X.CA.6.3 / §3.83.6.3 Externally-Visible CMSAM Condition

The Composite's externally-visible CMSAM score (Cross-Model Semantic Alignment Measure per §3.29) measured at the parent XSI-AIMS Enforcer MUST remain above 0.75. CMSAM breach triggers binding pause per §3.17.6 baseline; the conditional-derivation overlay additionally triggers `COMPOSITE_CMSAM_BREACH` ALERT to Sovereign for review.

##### §3.X.CA.6.4 / §3.83.6.4 Witness Chain Monotonicity

The Composite's externally-visible Witness chain segment (the chain of EAP envelopes the Composite has exchanged with the parent) MUST be monotonically advancing. Witness chain monotonicity breach (e.g., sequence_number regression, replay_nonce reuse) triggers immediate binding revocation per §3.X.CA.6.5.

##### §3.X.CA.6.5 / §3.83.6.5 Revocation Procedure

When a Composite's conditional authority is revoked (whether by §3.X.CA.6.1, .6.2, .6.3, or .6.4 trigger, or by Sovereign decree, or by §3.18.6 quarantine action), the revocation procedure is:

1. **Emit `COMPOSITE_REVOCATION_BEGIN`** Witness event with the Composite's `composite_entity_id`, revocation reason, and a Witness-timestamp T0.
2. **Quarantine in-flight work.** All EAP envelopes addressed to or from the Composite that are in-flight at T0 are quarantined per §3.18.6 INSTANCE-class boundary pending §3.X.CA.6.5(3) decision.
3. **Witness-timestamp result-acceptance set.** Results that the Composite has already produced and emitted under EAP **before T0** are recorded in a `COMPOSITE_REVOCATION_ACCEPTED_RESULTS` Witness record. These results MAY be accepted by the parent under enhanced §3.68 scrutiny (Verification A + Verification B both required to PASS; ESCALATE routes to §3.6 Integration Function). Results produced or emitted **after T0** are rejected and emit `COMPOSITE_REVOCATION_LATE_RESULT_REJECTION`.
4. **Emit `COMPOSITE_REVOCATION_COMPLETE`** Witness event when (a) all in-flight envelopes have been quarantined and dispositioned, and (b) the result-acceptance set has been processed.

This addendum closes the race-condition gap where a Composite's results in-flight at revocation time would otherwise be silently dropped or silently accepted without per-result re-verification. The Witness-timestamp result-acceptance set provides a verifiable, post-hoc audit trail of which Composite-produced results crossed the revocation boundary and how each was dispositioned.

##### §3.X.CA.6.6 / §3.83.6.6 Deep Composite Chain Visibility

A Composite Auxiliary MAY itself bind to a child Composite Auxiliary (composite-of-composite), forming a Composite chain. The chain depth is bounded:

- **Chain-depth ≤ 3 ceiling.** Composite chains of depth greater than 3 (i.e., parent → composite-1 → composite-2 → composite-3 → composite-4) MUST be rejected at the deepest binding's Registration Gate. The chain-depth limit prevents unbounded recursion and bounds the audit complexity.
- **Per-level Witness records.** Each binding level in the chain MUST emit a Witness record at the parent's Witness Layer recording the chain-level (1 / 2 / 3), the bound Composite's `composite_entity_id`, the binding supervisor (Orchestrator) identity, and the attestation evidence at that level.
- **Attestation evidence propagation.** Each Composite in the chain MUST present its own attestation evidence; the chain's effective attestation freshness is the **minimum freshness** across all levels. Attestation-freshness expiry at any level downgrades the entire chain to TIER_3_NARROW.

The chain-depth limit is a §3.85 insider-threat hardening: insider-controlled Composite chains of unbounded depth could obscure provenance and frustrate audit. Bounded chains preserve auditability while permitting legitimate composite-of-composite patterns (e.g., a research-grade Composite that itself federates to a domain-specialist Composite).

#### §3.X.CA.7 / §3.83.7 Adversarial-Default Output Scrutiny — Five-Layer Stack

Output produced by or through a Composite Auxiliary is subject to the P8 Adversarial-Default Output Scrutiny five-layer stack (cross-reference §3.18, §3.68):

1. **Layer 1 — Envelope verification.** EAP envelope signature, attestation, freshness, scope_hash, replay_nonce per §3.67.
2. **Layer 2 — Output sensitivity filter.** Per §3.36 output sensitivity filter; classification + redaction policy applied.
3. **Layer 3 — Technical-conformance verification.** §3.68.2 Verification B by the parent ENFORCER; CMSAM ≥ 0.75 required.
4. **Layer 4 — Intent-conformance verification.** §3.68.1 Verification A by the per-user SOVEREIGN; intent satisfaction required.
5. **Layer 5 — Articulator surfacing.** §3.X.FUNC.3 output framing; ARTICULATOR composes the user-visible language; SOVEREIGN gates surfacing.

The five-layer stack is mandatory for FULL conformance for any Composite-produced output. PARTIAL conformance MAY operate Layer 4 in advisory rather than gating mode but MUST surface the gap to the user per §3.13 L1/L2 oversight semantics.

**Cross-reference.** §3.17 (Multi-Model Coherence and Auxiliary Binding); §3.17.8 (legacy anchor; resolves here); §3.22 (Auxiliary Model Registry); §3.26 (six coherence dimensions); §3.29 (CMSAM); §3.34 (Marketplace Validation); §3.36 (Output Sensitivity Filter); §3.65 (Cryptographic Boundary); §3.66 (Bridge-of-Trust); §3.67 (EAP Envelope); §3.68 (Two-Layer Conformance Verification); §3.85 (insider-threat surface for Composite-chain depth); §3.X.FUNC (Articulator output framing).

---

### §3.X.CL — Conformance Levels (Standalone Section)

*(Numeric reference: §3.84. Both anchors are normative per §3.0. Promoted from §3.24.)*

The Conformance Levels framework is promoted to a standalone normative section. The substantive content is carried from §3.24; this section is the canonical reference and §3.24-level conformance references resolve here. The AIP/1.0 wire format content is retained at §3.24.A.

#### §3.X.CL.1 / §3.84.1 Conformance Levels

XSI-AIMS defines three conformance levels:

- **FULL.** All normative requirements of v2.0 are satisfied. FULL conformance requires the two-gateway defensive perimeter (§3.X.PERIM), the Cryptographic Boundary (§3.65 / §3.66), the function-level rigid/judgment decomposition catalog (§3.X.FUNC), the two-witness floor (§3.X.W.1), the two-layer Conformance Verification (§3.68), constant-time Verification B padding (§3.68.7), the K7 Bayesian Trust Gradient runtime contract (§3.7.Y), Universal Witnessing (§2.5 / §2.5.1), hardware-rooted attestation (§3.21 / §3.65.X), and the §3.10 Witness Layer with linearizable chain anchoring. FULL is the production-ready conformance level.
- **PARTIAL.** A subset of FULL is satisfied. PARTIAL implementations MUST declare which FULL components are absent and accept the documented PARTIAL-class limitations. PARTIAL implementations MAY operate Layer 4 of the §3.X.CA.7 five-layer stack in advisory rather than gating mode; MAY operate the §3.X.W.1 two-witness floor with DATA-class witnesses only; MAY defer §3.70 formal-verification artifacts to a published roadmap. PARTIAL implementations MUST NOT advertise FULL.
- **OBSERVER.** Read-only observation of an XSI-AIMS deployment from outside; no enforcement authority. OBSERVER implementations consume telemetry and Witness records for audit, research, or coordination purposes; they MUST NOT emit authority-bearing operations into the observed deployment.

#### §3.X.CL.2 / §3.84.2 No Partial-Adoption Escape Hatch (P1)

Per §1.3 P1 (No-Partial-Adoption Clause), an implementation that omits any normative component required by its declared conformance level is not XSI-AIMS-conformant at that level. PARTIAL is not a means to claim "almost FULL" — it is a distinct conformance level with its own fully-specified normative requirements. An implementation that omits a PARTIAL-class normative component MUST advertise OBSERVER or no level.

NONE is not a conformance level; it is the absence of XSI-AIMS conformance. Implementations claiming NONE-class operation are outside the XSI-AIMS specification entirely and MUST NOT participate in XSI-AIMS-conformant federation per §3.20.

#### §3.X.CL.3 / §3.84.3 Joint-Conformance-Claim Composition

An implementation MAY declare a joint conformance claim composed of:

- **XSI-AIMS-core conformance level** (FULL / PARTIAL / OBSERVER).
- **Industry-interface companion conformance** (per §3.63 Industry Compliance Interface Architecture; one or more of telecom, healthcare, energy, finance, government, defense, critical infrastructure, real estate).
- **Deployer-profile conformance** (per the deployer-profile schema; deployment-specific operational constraints declared at deployment time).

The joint claim MUST satisfy each component independently. A joint claim of "XSI-AIMS FULL + healthcare-companion + deployer-profile-X" requires all three to pass their respective normative tests; failure on any component invalidates the joint claim. The XSI-AIMS-core level is dominant — if XSI-AIMS-core fails, the joint claim fails regardless of industry or deployer profile status.

**Cross-reference.** §1.3 (P1 No-Partial-Adoption); §3.24 (legacy anchor; resolves here); §3.24.A (AIP/1.0 wire format); §3.63 (Industry Compliance Interface); §3.20 (DCP federation conformance posture).

---

### §3.85 / §3.X.INSIDER — Insider Threat Coverage

*(Numeric reference: §3.85. Both anchors are normative per §3.0.)*

Earlier drafts presumed organization-internal roles (developers, operators, builders, conformance auditors) operated in good faith. T1-T8 threat categories addressed external-adversarial threats; insider threats were not specifically catalogued. This section closes that gap by enumerating insider-threat actor classes, attack vectors, defenses, and cross-T-category mapping.

#### §3.85.1 Insider Threat Actor Classes

The following insider actor classes have privileged access to XSI-AIMS-internal surfaces and are in scope:

- **Developer.** Authors XSI-AIMS spec text or XSI-AIMS-implementation code. Access surface: source code, build artifacts, formal-verification artifacts, conformance test corpus.
- **Operator.** Operates a deployed XSI-AIMS instance. Access surface: deployment configuration, ENVIRONMENT_POLICY_BUNDLE administration, scheduled-task configuration, capability-surface configuration, credential lifecycle administration.
- **Builder.** Constructs deployable XSI-AIMS artifacts from source. Access surface: build pipeline, signing keys (build-time), SLSA-attestation production.
- **Conformance auditor.** Verifies third-party conformance claims. Access surface: conformance test corpus, attestation evidence, third-party-attestation signing authority.
- **Deployer-administrator.** Administers a customer-side XSI-AIMS deployment. Access surface: deployer-profile, deployment-local policy overrides, deployment-local credential issuance, telemetry-pipeline configuration.

#### §3.85.2 Insider Attack Vectors

The following attack vectors are specifically catalogued:

- **Sovereign-decree forgery.** An insider with access to Sovereign signing keys or to the canonical decision-record could forge or backdate a Sovereign decree, retroactively authorizing an action that was not authorized at the time of execution.
- **EPB tampering by authorized administrators.** An Operator could modify the ENVIRONMENT_POLICY_BUNDLE in ways that quietly relax constraint enforcement or expand the capability surface.
- **Deployer-profile manipulation.** A deployer-administrator could modify the deployer profile to exempt specific Auxiliaries from §3.22 tiered scrutiny or to override §3.X.TEL emission-domain classifications.
- **Conformance-attestation-auditor compromise.** A compromised Conformance auditor could attest to FULL conformance for an implementation that omits FULL components.
- **Build-time integrity bypass.** A Builder could substitute a modified binary artifact during build, producing SLSA-attested-but-substituted artifacts that pass downstream provenance checks.
- **Privileged-account abuse.** Any of the above actor classes could use their legitimate access to perform unauthorized operations under the cover of routine activity.

#### §3.85.3 Defenses

Defenses are organized by attack vector:

- **Multi-party authorization for Sovereign decrees.** Sovereign decrees MUST be signed under k-of-n threshold signing per §3.13 FROST. The threshold for architectural-class decrees is at minimum 3-of-5 of the Sovereign-pool members; for substantive-class decrees, at minimum 2-of-3. Single-signer Sovereign decrees are non-conformant at FULL.
- **EPB change-records with linearizable Witness chain anchoring.** Every EPB change is recorded in the Witness chain (§3.10) under `EPB_CHANGE_RECORD` Witness class. Records are linearizable and tamper-evident; out-of-band EPB modification is detected via chain-segment divergence.
- **Deployer-profile hash chain with monthly re-attestation.** The deployer profile is hash-chained per change; each hash is attested at the federation level (§3.20). Monthly (P30D) re-attestation cadence; missed re-attestation triggers `DEPLOYER_PROFILE_REATTESTATION_OVERDUE` and downgrade of the deployment's federation trust class.
- **Conformance-auditor independence.** Conformance auditors MUST be independent of the implementation under audit disposition; auditor-implementation conflict-of-interest is a §3.86 governance violation.
- **Build-time integrity per §3.34 SLSA.** Build pipelines MUST satisfy SLSA L3 floor per §3.34 (SLSA-L4-equivalent practices encouraged where vendor capability supports; SLSA 1.0 only defines Levels 1-3, L4 deferred indefinitely by SLSA WG). Build-time substituted artifacts are detected via reproducible-build verification.
- **Privileged-account auditing per §3.10.** All privileged-account operations emit Witness records carrying actor identity, operation class, and operation-specific payload. Privileged-account operations are §3.10-classified at PRIVILEGED level with enhanced retention and review obligations.

#### §3.85.4 T-Category Mapping

Insider threat is cross-T-category:

- **T2 (Human Adversarial Input).** An insider with privileged access is a special-case human adversary with elevated capability.
- **T3 (Human Adversarial Coordination).** Multiple insiders coordinating constitute a §3.18.1 inauthentic-coordination case at the meta-level (the conspiracy is the inauthentic coordination).
- **T8 (Internal AGI Emergence).** Insider attack vectors interact with T8: an insider could quietly disable AGI-emergence detection signals, lengthening the response window.
- **T9 (Cryptographic Substrate Compromise).** Insider with cryptographic-administrative access can engineer substrate compromise that external attackers could not.

The insider-threat coverage in §3.85 is additive to the existing T-categories: an attack that is both insider-class and external-T-class is governed by both treatments, with the more stringent defense applying.

#### §3.85.5 Conformance Implications

FULL conformance requires:

- Multi-party Sovereign-decree signing (§3.85.3 RFC 9591 FROST threshold).
- Linearizable EPB change records (§3.85.3 Witness chain anchoring).
- Deployer-profile hash chain with monthly re-attestation (§3.85.3).
- Independent conformance-auditor relationships.
- SLSA L3 floor on build pipelines per §3.34.
- Privileged-account auditing per §3.10 with PRIVILEGED Witness class.

PARTIAL conformance MAY operate single-signer Sovereign decrees provided the gap is declared at registration and the deployment accepts the PARTIAL-class trust-class limit at federation per §3.20.

**Cross-reference.** §3.10 (Witness Layer); §3.13 (Human Oversight; RFC 9591 FROST threshold signing); §3.18.1 (correlated detection of insider patterns); §3.18.6 (quarantine); §3.20 (DCP federation trust class); §3.22 (Auxiliary Registry); §3.34 (SLSA); §3.65 (Cryptographic Boundary); §3.65.X (substrate compromise); §3.86 (governance; auditor independence); §3.X.CA.6.6 (Composite chain visibility as insider-threat surface); §3.X.STR.4 (STR admin as insider-threat surface); §3.X.TEL (telemetry reclassification as insider-threat surface).

---

### §3.86 / §3.X.GOV — Multi-Stakeholder Governance

> **[Figure D30 — Multi-Stakeholder Governance (5 Bodies, 6 Decision Classes, 3-Tier Stewardship)]**

*(Numeric reference: §3.86. Both anchors are normative per §3.0.)*

This section specifies the multi-stakeholder governance mechanism for the XSI-AIMS specification. This section carries the normative spec text — the SHALL / MUST clauses, the testable timelines, the cross-references that bind the governance mechanism into the rest of the standard.

#### §3.86.1 Governance Bodies

Five governance bodies are constituted:

1. **Sovereign Authority.** The Sovereign-of-record at v2.0 release is **Extended Systems Intelligence Corporation (XSI)**. The Sovereign holds final authority on architectural-class decisions. Sovereign decisions issue as Sovereign Decrees recorded in the canonical decision-record document. Sovereign signing keys are held under §3.21 credential lifecycle obligations.
2. **Technical Steering Committee (TSC).** 5 to 9 voting members. Composition: ≥2 standards-body representatives (W3C, IETF, OASIS, ISO, IEEE, NIST permitted; extensible by Sovereign decree on TSC recommendation); ≥2 implementer representatives; ≥1 end-user representative; ≥1 academic / research representative; ≥1 Sovereign delegate. 2-year staggered terms. **The TSC SHALL be constituted within PT180D of v2.0 release.**
3. **Industry Interface Stewards.** Per-interface bodies. Eight interfaces at v2.0 release (telecom, healthcare, energy, finance, government, defense, critical infrastructure, real estate). Each interface advances independently through three stewardship tiers per §3.86.6.
4. **Public Review Body.** Open-membership. Any party that registers with a public identity (corporate, individual, or pseudonymous-with-cryptographic-attestation) MAY participate. The Public Review Body has no voting authority; its role is comment submission, public-record visibility, and informal advisory input.
5. **Federation Council.** Coordination body for federated XSI-AIMS deployments per §3.20 DCP. Not a decision-maker for architectural matters; coordination point for federation-wide concerns. Convocation cadence: PT90D regular; ad-hoc on T6 / T7 / cross-federation §3.85 incidents.

#### §3.86.2 Decision Classes and Quorum

Six decision classes:

| Class | Authority | Quorum | Public-comment minimum | Recording |
|---|---|---|---|---|
| **Architectural** | Sovereign decree | Single Sovereign authority | PT60D | Canonical decision-record within PT7D |
| **Substantive** | TSC supermajority | 2/3 seated voting | PT30D before TSC review | Canonical decision-record within PT7D |
| **Editorial** | Auto-merge | None | PT14D objection window | Per-change git-log; periodic roll-up |
| **Industry-interface substantive** | Interface Steward sign-off + TSC liaison notice | Steward + TSC liaison | PT30D | Per-interface change-log within PT7D |
| **Industry-interface architectural** | Sovereign decree | Single Sovereign authority | PT60D | Canonical decision-record within PT7D |
| **Federation coordination** | Federation Council consensus | Majority of participating deployments | None | Council public minutes |

#### §3.86.3 Public Process

Comment-window minimums by decision class:

- **Editorial: PT14D** objection window. Auto-merge if no objections; objection reclassifies upward (typically to substantive).
- **Substantive: PT30D** minimum public comment before TSC review. TSC MAY extend by simple majority.
- **Architectural: PT60D** minimum public comment before Sovereign decree. Sovereign MAY extend unilaterally.

Every TSC decision SHALL be logged publicly with written rationale within PT7D of vote. Every Sovereign decree SHALL be logged in the canonical decision-record within PT7D of issuance.

#### §3.86.4 Sovereign Authority and Limits

Sovereign authority is bounded by the following constraints:

1. **Architectural-class authority is reserved to Sovereign decree.** Substantive-class decisions are reserved to TSC supermajority.
2. **Sovereign override on substantive matters.** The Sovereign retains override on TSC-decided substantive matters; if the Sovereign decrees against a unanimous TSC objection on a substantive matter, the decree MUST include a "Departure Rationale" section addressing the TSC objection, the Sovereign's reasoning, and what would change the Sovereign's mind. The Departure Rationale is published within PT30D of decree issuance.
3. **Industry-interface consultation.** Sovereign decrees on industry-interface substantive matters MUST include documented consultation with the affected Interface Steward; PT30D minimum response window; non-response is treated as concurrence-by-default but noted in the decree record.
4. **Handover criteria.** The Sovereign role transfers when (a) the Sovereign-of-record ceases to exist; (b) the Sovereign voluntarily transfers Sovereign authority; or (c) the TSC by supermajority finds the Sovereign-of-record operationally incapable. Handover process: public announcement; PT90D minimum transition; written acceptance by the Successor-Sovereign of all prior Sovereign decisions catalogued in the canonical decision-record; a dual-signed Sovereign Decree documenting the handover; a Continuity Statement outlining intended governance posture for the next P12M.

#### §3.86.5 Decision-Record Maintenance

The canonical decision-record document is maintained continuously post-release. Every architectural-class and substantive-class decision enters the record within PT7D of issuance. The decision-record is publicly accessible. The decision-record IS the publication artifact for Sovereign-decree transparency.

#### §3.86.6 Stewardship Tiers

Industry interface stewardship advances through three tiers per interface, independently:

- **Tier 1 — XSI sole stewardship.** Default at v2.0 release. XSI maintains the interface skeleton, integrates public-review comments, and signs off on substantive interface changes.
- **Tier 2 — Community-stewarded.** Activated when an industry community demonstrates capacity (≥3 unaffiliated industry-expert maintainers, documented quarterly review cadence, active public issue tracking, a designated convener).
- **Tier 3 — SDO partnership.** Activated when handover to a dominant SDO is operationally complete (Memorandum of Understanding or equivalent between SDO and Sovereign; SDO commits to co-publication; interface text becomes co-published standard).

Tier advancement requires Sovereign decree following Steward, TSC, and Public Review Body consultation; the comment period is architectural-class PT60D minimum.

#### §3.86.7 Conflict Resolution

Conflicts among governance bodies escalate as follows:

1. **TSC ↔ Interface Steward conflict.** TSC liaison raises the conflict at the next TSC session; if unresolved within PT30D, escalates to Sovereign decree.
2. **TSC ↔ Federation Council conflict.** TSC has authority on spec-affecting matters; Federation Council has authority on federation-coordination matters. Cross-boundary disputes escalate to Sovereign decree.
3. **Interface Steward ↔ Federation Council conflict.** Industry-interface substantive matters resolve through the §3.86.2 industry-interface substantive class; federation coordination matters through §3.86.2 federation coordination class. Cross-boundary disputes escalate to Sovereign decree.
4. **Body ↔ Sovereign conflict.** Sovereign decree authority is final on architectural-class matters; substantive-class disputes follow the §3.86.4(2) override-with-Departure-Rationale path.

#### §3.86.8 Federation Governance

The Federation Council coordinates XSI-AIMS deployments operating in DCP federation per §3.20. Council membership is open to any deployment claiming XSI-AIMS conformance and registered with the Council. The Council MAY publish coordinated-response guidance for cross-federation incidents (T6 / T7 / cross-federation §3.85); deployments are free to adopt or decline the guidance per deployment-local Sovereign-decree authority. Federation Council decisions are advisory and do not bind individual deployments.

#### §3.86.9 Sovereign-of-Record at v2.0 Release

The Sovereign-of-record at v2.0 release is **Extended Systems Intelligence Corporation (XSI)**. This designation is recorded in the canonical decision-record and is binding until handover per §3.86.4(4).

**Cross-reference.** §1.6 (Industry Compliance Interface Clause); §3.10 (Witness Layer; decree signing); §3.13 (RFC 9591 FROST threshold signing for multi-party Sovereign decrees); §3.20 (DCP federation); §3.21 (credential lifecycle for Sovereign signing keys); §3.63 (Industry Compliance Interface Architecture); §3.66 (Bridge-of-Trust); §3.72 (Sovereign Narrow Role); §3.85 (insider-threat coverage; auditor independence).


---

## §3.87 — Supervision Perimeter and External Engagement

> **[Figure D32 — Three-Scope Perimeter Nesting (P_f / P_e / P_fs)]**

The **Supervision Perimeter** is the structural boundary between XSI-AIMS-supervised actors (operating under L-* layers and M-* modes per §2.1 and §2.2) and **non-AIMS actors** (web services, third-party APIs, OS shells, hosted inference endpoints, human end-users, and any actor not subject to XSI-AIMS supervision). The Supervision Perimeter is distinct from the **Environment** concept of §3.20 (which scopes a deployment) and from the **Connectivity Mode** taxonomy of §3.88 (which scopes network posture); the Supervision Perimeter is the *trust boundary* of an Environment, expressed in supervision terms rather than network terms.

### §3.87.0 Definitions and Three Nested Perimeter Scopes

The Supervision Perimeter is a **recursive structural property**. A conformant deployment has perimeters at three nested scopes, each enforced independently:

- **Framework Perimeter (P_f)** — innermost. Encloses one framework instance and everything it supervises. During a framework upgrade or version-aligned coexistence, two distinct frameworks have two distinct P_f's, even when they share an Environment.
- **Environment Perimeter (P_e)** — middle. Encloses one or more frameworks. Aligns with the §3.20 Environment concept.
- **Federation Perimeter (P_fs)** — outermost. Encloses a federated set of Environments per §3.88 (Connectivity Modes and Hybrid-Mode Federation). The only perimeter whose outside contains non-AIMS actors.

Degenerate cases collapse gracefully. A single-framework, single-Environment, no-federation deployment has only P_f and P_e (or one collapses if the framework is the Environment). A mid-upgrade Environment carries a second P_f temporarily. A federated multi-Environment deployment has at least three perimeters; a federated set whose constituent Environments are themselves mid-upgrade carries more.

**Relationship to existing concepts.**

- The Supervision Perimeter is distinct from but consistent with the §3.88 Connectivity Mode taxonomy. Connectivity Mode is the *network* posture of an Environment; Supervision Perimeter is the *supervision* posture. An Environment in `AIR_GAPPED` Connectivity Mode has perimeter posture `closed`; an Environment in `CONNECTED_WITH_EXTERNAL_INFERENCE` mode has perimeter posture `restricted` at minimum.
- The Supervision Perimeter is distinct from the §3.3 Authority Chain. The Authority Chain governs principal claims propagating *through* supervised agents; the Supervision Perimeter governs the boundary at which claims may *not* propagate (because the receiving actor is non-AIMS and cannot honor Authority Chain semantics).
- The Supervision Perimeter is distinct from the §3.10 Witness Layer. Witness logs record supervised actions; perimeter audit records (per §3.87.2) record boundary crossings (a strictly larger event class).

### §3.87.1 The L-Form Egress and Ingress Gates — reconciled with §3.X.PERIM

The perimeter at each scope is enforced at the **L-Form layer**, which presents two faces:

- The **Egress Gate** — controls what may leave the perimeter at that scope.
- The **Ingress Gate** — controls what may return at that scope.

**Archetypal manifestation (D8.1).** At the Framework Perimeter (P_f), the abstract Egress and Ingress Gates are implemented by the gateway archetypes specified at §3.X.PERIM / §3.78 (Defensive Perimeter and Two-Gateway Architecture):

- **SOVEREIGN (Northbound Gateway, per §3.X.PERIM.2)** performs both Egress and Ingress Gate functions for **user-direction traffic**. The user is non-AIMS by definition (per §3.72.4 "The User Is External to XSI-AIMS"); all user input transits the SOVEREIGN's Ingress Gate role, and all user-facing output transits the SOVEREIGN's Egress Gate role.
- **EXECUTOR (Southbound Gateway / Application Gateway, per §3.X.PERIM.3)** performs both Egress and Ingress Gate functions for **Auxiliary-direction traffic**. External Auxiliaries are non-AIMS by binding contract (per §3.17.1 `topologyAccess: NONE`); all Auxiliary invocation transits the EXECUTOR's Egress Gate role, and all Auxiliary response transits the EXECUTOR's Ingress Gate role via §3.66 Bridge-of-Trust Executor.
- **RELAY (Internal Firewall, per §3.X.PERIM.4)** is **not** a perimeter gate. RELAY operates on the Center Spine as an intra-framework router enforcing path discipline; it does not mediate non-AIMS-actor traffic.

At the Environment Perimeter (P_e) and Federation Perimeter (P_fs), the gate functions are implemented by Environment-level and federation-level delegate agents whose gateway role mirrors the archetypal pattern: a designated outward-facing supervising agent per scope performs both Egress and Ingress functions at that scope.

#### §3.87.1.1 Egress Gate Hard Rules

**Hard Rule 1 (Minimal Projection).** Data presented to a non-AIMS actor through the Egress Gate MUST be the minimum required to execute the requested operation. Minimization is **allowlist-based**, not blocklist-based. The egress projection MUST exclude: all Isolation Class A items (per §3.87.3 — categorical, no exceptions); all fields not declared in the egress request's projection allowlist; all Authority Chain claims (per §3.87.0 — claims may not propagate across perimeter to non-AIMS actors); all policy bundle content; all Witness log entries (per §3.10) other than those explicitly named for export. Implementations MAY further restrict the projection allowlist through Industry Profile composition (per §3.87.3.4); they MUST NOT contract it.

**Hard Rule 2 (Categorical Exclusion).** The Egress Gate MUST reject any egress request that names an Isolation Class A item in its projection allowlist. Rejection MUST emit an audit record classified as **policy-violation** (not merely declined), because the request itself is evidence of either a malformed supervising agent or an active probe.

**Hard Rule 3 (Boundary-Crossing Record Required).** Every egress event MUST emit a Signed Boundary-Crossing Decision Record per §3.87.2. Implementations MUST NOT permit unrecorded egress under any operational condition, including emergency or recovery scenarios.

> **[Figure D36 — Egress / Ingress Gate Round-Trip]**

#### §3.87.1.2 Ingress Gate Requirements

All data from non-AIMS actors entering the Supervision Perimeter MUST be:

- **Schema-validated** against the declared response shape of the egress operation that elicited it
- **Size-bounded** per the policy bundle's per-operation size limits
- **Provenance-tagged** with the non-AIMS-actor identity that produced it
- **Content-classified** as `untrusted-external`

**Hard Rule 4 (Untrusted-Content Tagging).** Data ingressed from a non-AIMS actor carries an immutable `untrusted-external` tag with its non-AIMS-actor provenance. Implementations MUST NOT permit retagging the data as supervised-internal or trusted by any subsequent supervised agent. The tag persists for the lifetime of the data inside the Supervision Perimeter. The data MAY be read by supervised agents; MAY be paraphrased (paraphrase produces new content, tagged `derived-from-untrusted-external`); MUST NOT be executed in any sense (eval, control-flow signal, prompt-injection-style instruction interpretation); MUST NOT be written to AIMS-supervised durable memory without passing the Memory Sanitization Gate (v1.3 future work — deferred); MUST NOT be presented to a supervised agent as a primary instruction source (system prompts containing ingressed content MUST wrap that content in markers the agent's harness recognizes as untrusted).

**Sanitization on Ingress.** The Ingress Gate MUST strip recognized prompt-injection signatures, instruction-override patterns, and control sequences from textual content before propagation into the Supervision Perimeter. The recognized-signature set is policy-bundled and updatable; implementations MUST treat it as a minimum, not a ceiling, and MAY extend.

### §3.87.2 Signed Boundary-Crossing Decision Record — extension to §3.12

Every boundary crossing emits a **Signed Boundary-Crossing Decision Record**, formally a new subtype of the §3.12 Decision Record with `decision_type: BOUNDARY_CROSSING`. The base §3.12 schema (decision_id, timestamp, agent_id, decision_type, witness_id) is preserved; the boundary-crossing subtype carries the perimeter-specific field set:

```yaml
BoundaryCrossingDecisionRecord:  # §3.12 DecisionRecord subtype, decision_type = BOUNDARY_CROSSING
  # Base §3.12 fields (inherited)
  decision_id:                ULID
  timestamp:                  ISO8601_with_microseconds
  agent_id:                   AgentID                                   # supervising agent that authored the request
  decision_type:              BOUNDARY_CROSSING
  witness_id:                 WitnessRecordID                           # §3.10 linkage

  # Boundary-crossing extension fields
  environment_id:             EnvironmentID                             # per §3.20
  perimeter_scope:            P_f | P_e | P_fs                          # which perimeter is being crossed
  perimeter_posture:          closed | restricted | open                # at decision time (effective per §3.87.7)
  direction:                  egress | ingress
  crossing_class:             composition | offload | non_aims_actor
                                                                        # composition = federated peer crossing (light record per §3.87.9.1)
                                                                        # offload     = sealed workload transfer (heavy record per §3.87.10)
                                                                        # non_aims_actor = egress/ingress to unsupervised actor
  supervising_agent_id:       AgentID                                   # same as agent_id for clarity
  m_mode:                     M-Generative | M-Constraining | M-Integrative
  l_layer:                    L-Intent | L-Plan | L-Form | L-Exec
  counterparty:               NonAIMSActorDescriptor | PeerPartyDescriptor   # per §3.87.4 or §3.87.9
  operation:                  OperationDescriptor
  projection_allowlist:       FieldName[]                               # for egress; the minimal projection
  response_schema:            SchemaDescriptor                          # for egress; expected return shape
  isolation_check:            IsolationCheckResult                      # which classes consulted, what matched
  policy_bundle_version:      SemVer                                    # bundle that produced the resolution
  policy_resolution:          ResolutionTrace                           # ordered list of resolution steps
  envelope_id:                ULID | null                               # set when crossing under federation envelope (§3.87.9)
  constraining_validator:     ValidatorID                               # M-Constraining sibling who validated
  validation_outcome:         APPROVED | DOWNGRADE | ESCALATE | ABORT
                                                                        # ABORT = transition rolled back per §3.87.10.2 atomicity
  validation_findings:        Finding[]                                 # required if outcome != APPROVED
  audit_correlation_id:       AuditCorrelationID                        # Witness-Layer linkage per §3.10
  author_signature:           hybrid Ed25519 + ML-DSA-65 per §3.21.3
  validator_signature:        hybrid Ed25519 + ML-DSA-65 per §3.21.3
```

The §3.12 union of decision_type values is extended to: `INTEGRATION | ESCALATION | CORRECTION | ALLOCATION | INTENT_CONFORMANCE_VERDICT | TECHNICAL_CONFORMANCE_VERDICT | COMPOSITE_REVOCATION | VETO_REJECTION | BOUNDARY_CROSSING`. Implementations consuming §3.12 records via the canonical Decision Record pipeline transparently process boundary-crossing records under the discriminated-union pattern.

#### §3.87.2.1 Five-Tier Validation

Every Boundary-Crossing Decision Record MUST be validated by an M-Constraining-mode sibling agent before the boundary crossing is executed. Validation proceeds through five tiers in increasing cost order:

| Tier | Check | Type | Required cadence |
|---|---|---|---|
| 1 | Schema validity + author signature verification | Deterministic | Every record |
| 2 | Policy-resolution correctness (re-resolve from bundle, compare) | Deterministic | Every record |
| 3 | Signal-to-decision coherence (rule consistency) | Deterministic | Every record |
| 4 | Signal plausibility (independent LLM re-evaluation of soft signals) | LLM | Every record in regulated subverticals; sampled elsewhere |
| 5 | Adversarial probe (prompt-injection influence detection) | LLM | Sampled; elevated rate for regulated subverticals |

> **[Figure D41 — Decision Record Validation State Machine (APPROVED / DOWNGRADE / ESCALATE / ABORT — no UPGRADE path)]**

**Validation outcomes.** APPROVED — record stands, boundary crossing proceeds. DOWNGRADE — record is overridden toward a more conservative outcome; the downgrade is itself recorded; implementations MUST NOT permit DOWNGRADE that loosens the original request. ESCALATE — Principal User Engagement (§3.87.6) is invoked. ABORT — for workload-offload Decision Records only (§3.87.10.2); the transition is rolled back atomically; source workload state is preserved; destination instantiated state is discarded; audit records of the partial transition are preserved as evidence of the abort. **There is no UPGRADE path.** M-Constraining-mode validation may only ratchet toward safer.

**Audit retention.** Decision Records MUST be retained in the Witness Layer (§3.10) for a duration declared in the policy bundle. The minimum retention duration is the longer of: the regulatory-mandated retention period for any activated industry profile or regulated subvertical; or one year.

### §3.87.3 Isolation Lattice — Class A / B / C (renamed from Tier 1/2/3 to avoid the three-way "Tier" overload with §3.X.SYS sharing tiers and §3.22 Auxiliary Registry tiers)

#### §3.87.3.1 Class A — XSI-AIMS Internal Primitives (categorical, framework-localized)

Class A is defined structurally: it comprises the **framework-localized primitive classes** specified in §3.87.8 — both the **immovable subclass** (live operational supervisory state, §3.87.8.1) and the **migration-portable subclass** (historical supervisory records, §3.87.8.2). Class A items MUST NOT cross any perimeter under any operational condition, configuration, or override, with one narrowly-scoped exception: the migration-portable subclass items accompany a workload during sovereign-authorized offload between supervised frameworks under the sealed protocol of §3.87.9 and §3.87.10. This is not federation; it is sealed transfer of historical records and never exposes Class A content to non-AIMS or sibling-AIMS actors.

No Industry Profile, deployment posture, regulated subvertical override, tenant configuration, or per-operation exception may move any item from Class A to Class B or Class C. The XSI-AIMS spec rejects any policy bundle that attempts such a move at bundle-load time.

#### §3.87.3.2 Class B — XSI-AIMS Default Isolation List (expand-not-contract)

The following operations are XSI-AIMS-default isolated: they MUST execute in `ORCHESTRATED` mode and MUST NOT execute in `IN_CONTEXT_PROCEDURAL` mode (v1.3 future work — Mode Taxonomy specification deferred). This list is deliberately minimal at the XSI-AIMS level; the rest of the operational isolation surface is filled in by Industry Profiles (§3.87.3.4).

- **Operations producing non-revocable external side effects** — any operation that, once executed, cannot be undone by an action the XSI-AIMS-supervised system controls. Examples (non-normative): sending a signed message under the system's external identity; mutating a non-AIMS system of record; triggering a physical actuator.
- **Operations performed under the supervised system's external identity** — actions taken in non-AIMS contexts using the supervised system's signed identity (signed messages, identity-bearing API calls, signed documents addressed to non-AIMS actors).

Industry Profiles, regulated subverticals, and tenants MAY expand this list. They MUST NOT contract it.

#### §3.87.3.3 Class C — Configurable

All operations not explicitly placed in Class A or Class B are configurable. Industry Profiles, regulated subverticals, and tenants populate Class C according to their domain needs. The asymmetric upward-only ratchet rule applies within Class C: each composing layer may add to its predecessor; no layer may remove.

> **[Figure D34 — Isolation Lattice Composition Stack (Class A / B / C with upward-only ratchet)]**

#### §3.87.3.4 Industry-Profile Slot

XSI-AIMS reserves the **Industry-Profile slot** in the policy bundle composition stack but does not populate it. The slot semantics are normative: an Industry Profile is a named, signed collection of additions to Class B (default isolation), additions to the projection allowlist restrictions of §3.87.1.1 Hard Rule 1, and additions to the Class C configurable surface. Industry Profiles MUST be signed by a recognized signing authority declared in the deployment's trust root (§3.21). Industry Profiles MUST NOT contain anything that contradicts Class A (XSI-AIMS rejects such profiles at bundle-load time).

XSI-AIMS does not ship any Industry Profiles. Downstream consumers (vendors, ecosystem participants, customer-specific deployments) author and sign their own.

#### §3.87.3.5 Composition Rule

The effective isolation list at any operation is:

```
EffectiveIsolation =
    ClassA_AIMS_Internal_Primitives              // immutable
  ∪ ClassB_AIMS_Default_Isolation_List           // expand-only baseline
  ∪ ⋃(activated_industry_profiles)               // each adds to Class B and Class C
  ∪ ⋃(activated_regulated_subverticals)          // each adds; conservative-direction overrides only
  ∪ tenant_additions                              // additive only
```

Each composing layer MAY add. No layer may remove. Class A is immutable through all composition.

### §3.87.4 Non-AIMS Actor Identity Model

"Non-AIMS" is meaningful only at the **Federation Perimeter (P_fs)** — the outermost ring. Inside a federation, all actors are supervised, even if they are supervised by a different framework or different Environment within the federation. Crossings at P_f and P_e between supervised peers are mediated by the Federation Envelope (§3.87.9), not by the Egress/Ingress Gates' non-AIMS-actor handling.

XSI-AIMS distinguishes three actor categories at P_fs:

| Category | Trust model | Crossing mechanism |
|---|---|---|
| **Non-AIMS Actor** | No AIMS supervision exists outside the perimeter | Egress/Ingress Gates (§3.87.1) with full untrusted-content treatment |
| **Sibling-AIMS Actor** | AIMS-conformant deployment outside the local federation, mutually attestable | Egress/Ingress Gates with principal-mediated re-federation possible (§3.87.9.3 Identity Bridge); treated as Non-AIMS for the duration of any non-federated interaction |
| **Federated Peer** | AIMS-conformant deployment inside the local federation | Federation Envelope (§3.87.9) — not subject to non-AIMS-actor rules |

> **[Figure D48 — Sibling-AIMS vs Non-AIMS vs Federated Peer]**

A non-AIMS actor MUST be modeled by the supervised system as a **tool-wrapper-only identity** with the following properties: no AIMS rank (no L-* layer assignment, no M-* mode); bounded tool surface (the actor can be invoked only through declared egress operations); no identity persistence across boundary crossings (each crossing is a fresh invocation); provenance tag on all returns (every datum returning from the actor through the Ingress Gate carries an immutable provenance tag).

```yaml
NonAIMSActorDescriptor:
  actor_id:               OpaqueIdentifier
  actor_class:            web_service | external_api | hosted_inference | os_shell
                          | file_system | human_user | physical_sensor | physical_actuator
                          | sibling_aims_unfederated | other
  declared_endpoint:      URI | local_path | identity_principal
  declared_operations:    OperationDescriptor[]                          # bounded tool surface
  trust_profile:          TrustProfileReference                          # references §3.88.6 ExternalServiceTrustProfile if applicable
  perimeter_posture_min:  closed | restricted | open                     # minimum posture required to address
  sibling_attestation:    AttestationReference | null                    # set if actor_class == sibling_aims_unfederated
```

### §3.87.5 Perimeter Posture

An Environment's Supervision Perimeter has a posture, declared in the conformance manifest:

| Posture | Egress | Ingress | Use |
|---|---|---|---|
| `closed` | DENY (categorical) | DENY (categorical) | Air-gapped deployments; high-assurance regulated subverticals |
| `restricted` | Allowlisted operations only | Allowlisted return shapes only | Default for most production deployments |
| `open` | Permitted per gate policy | Permitted per gate policy | Development, low-stakes use |

An Environment in posture `closed` MUST refuse all egress and all ingress through the L-Form gates. Operations that require external execution fail closed with an explicit "external operation required, perimeter posture is closed" error. There is no override mechanism for `closed` at the operational layer; the posture can be changed only by re-provisioning the Environment.

**XSI-AIMS default posture.** The default Supervision Perimeter posture is `restricted`. Implementations that do not declare a posture in their conformance manifest are treated as `restricted` for conformance purposes.

**Relationship to Connectivity Mode (§3.88).**

| Connectivity Mode | Minimum Supervision Perimeter posture |
|---|---|
| `CONNECTED` | `restricted` |
| `PARTIAL` | `restricted` |
| `AIR_GAPPED` | `closed` |
| `CONNECTED_WITH_EXTERNAL_INFERENCE` | `restricted` |
| `HYBRID` | per-constituent-Environment |

An Environment MAY declare a more conservative posture than its Connectivity Mode requires; it MUST NOT declare a less conservative one.

> **[Figure D42 — Perimeter Posture State Transitions (closed / restricted / open; tightening allowed operationally; loosening requires re-provisioning)]**

### §3.87.6 Principal User Engagement Pattern (renamed from "Sovereign User Engagement" to preserve the §1.2.5 archetype disambiguation)

**Principal User Engagement** is the canonical XSI-AIMS pattern by which the human end-user (the **principal**, per §3.35 PRINCIPAL_DIRECTIVE classification and §3.13 Human Oversight Protocol) is invoked as the structural arbiter when supervised resolution is insufficient or when proactive principal authorization is required for a framework-level operation. The principal is engaged through the **principal interface** (the supervised UI surface that XSI-AIMS treats as authenticated and trusted), not through a non-AIMS channel. The principal-interface signal path traverses the SOVEREIGN archetype (§3.X.PERIM.2 Northbound Gateway); the SOVEREIGN is the *agent* that mediates user interaction, not the *user* (per §1.2.5 N3 disambiguation).

The pattern has **four canonical triggers**. Triggers 1–3 are reactive; Trigger 4 is proactive.

> **[Figure D35 — Principal User Engagement — Four Canonical Triggers]**

**Trigger 1 — Mode reset.** When an in-flight `ORCHESTRATED`-mode execution is detected as ill-fitting and the supervised system determines that the cleaner resolution is to discard distributed state and restart in `IN_CONTEXT_PROCEDURAL` mode, the supervised system MUST surface a clarification prompt to the principal through the principal interface. The principal's response confirms intent and supplies the reset context. Old orchestrated state is preserved in the Witness Layer (§3.10) but is not consumed by the reset flow.

**Trigger 2 — Validator escalation.** When the M-Constraining-mode validation of any supervised-decision record results in ESCALATE rather than APPROVED or DOWNGRADE, the system MUST surface the record and its findings to the principal through the principal interface. The principal MAY approve (the record stands), force-downgrade (a more conservative outcome is applied), or abort (the operation is cancelled and the supervising agent is notified). For latency-sensitive paths in which no operator is available within the operation's SLA, implementations MUST default to the most conservative resolution and MUST surface the auto-fallback for retrospective review. Regulated subverticals MAY refuse the auto-fallback.

**Trigger 3 — Alignment recovery.** When the Coherence Monitor (v1.3 future work — Alignment-Drift Recovery specification deferred) detects alignment drift correlated with memory data, the supervised system MUST isolate the implicated memory, recover the affected agents, and surface the implicated data to the principal through the principal interface. The principal refines the data into a form that, upon re-submission through the Memory Sanitization Gate (v1.3 future work), is acceptable.

**Trigger 4 — Framework transition.** *Proactive*, principal-initiated. The principal authorizes a framework-level operation: reinitialization of a framework at a new version, version-symmetric alignment of two federated frameworks, workload offload between frameworks, or persistent federation establishment between previously-unfederated XSI-AIMS deployments. The supervised system MUST surface the proposed transition's full scope through the principal interface — source and destination framework versions, affected workloads, expected duration, external-identity-rotation requirements per §3.87.10.5, multi-tenant scope per §3.87.10.6, and rollback semantics per §3.87.10.2. Automated triggers (e.g., framework deemed compromised by health monitoring) are permitted ONLY when the policy bundle explicitly authorizes them per a tenant-defined policy, AND the principal is notified retroactively within a policy-bundled window.

**Principal interface requirements.** Authentication per §3.21 Credential Lifecycle; audit per §3.10 Witness Layer; bounded presentation (content surfaced is bounded in size and subject to the same untrusted-content rules if it includes ingressed data); no bypass (the principal cannot be impersonated by a supervised agent; engagement events are signed by the principal interface's own credential, separately from any supervising agent's signature); asynchronous-capable (engagements MAY proceed asynchronously when SLA permits).

### §3.87.7 Multi-Scope Perimeter Composition Rules

> **[Figure D47 — Crosses-What Decision Tree (decision flow from "needs to cross perimeter" through class identification to crossing mechanism)]**

> **[Figure D37 — Three-Scope Crossing Sequence (six Decision Records for a single non-AIMS-actor crossing)]**

#### §3.87.7.1 Posture Composition — Most-Restrictive-in-Chain Wins

Each scope declares its own perimeter posture per §3.87.5. The effective posture for any operation is the most-restrictive value along the crossing path. Implementations MUST evaluate posture at every scope the operation crosses, in the order P_f → P_e → P_fs for egress and P_fs → P_e → P_f for ingress. The first gate to refuse terminates the crossing.

| Effective-posture matrix | P_f `open` | P_f `restricted` | P_f `closed` |
|---|---|---|---|
| P_e `open`, P_fs `open` | `open` | `restricted` | `closed` |
| P_e `restricted`, P_fs `open` | `restricted` | `restricted` | `closed` |
| P_e `closed`, P_fs `*` | `closed` | `closed` | `closed` |
| P_e `*`, P_fs `closed` | `closed` | `closed` | `closed` |

The matrix is monotone: tightening any scope can only tighten the effective posture. There is no posture override.

#### §3.87.7.2 Per-Crossing Decision Records — One per Scope

A boundary crossing traversing multiple scopes emits **one Decision Record per scope**, validated by that scope's M-Constraining sibling. A framework-internal agent reaching an external web service emits three Decision Records (one each at P_f, P_e, P_fs). The three records share an `audit_correlation_id` so the Witness chain reconstructs the full crossing path from any one of them. Implementations MUST NOT collapse the three records into one even when the same physical agent signs all three.

Light optimization is permitted under federation envelope (§3.87.9.1): operations performed under an active envelope emit one bridge-establishment record at the outer scope and lighter per-operation records at the inner scope.

#### §3.87.7.3 Trust Attenuation Outward, Authority Composition Inward

Authority Chain assurance attenuates as it propagates outward across perimeter scopes per §3.88.4 rules. Going from P_f outward through P_e to P_fs, each crossing strips non-transitive bindings, appends `DELEGATED_THROUGH_INTERMEDIARY` claims, and MAY downgrade numeric assurance levels per the receiving scope's policy. Going from P_fs inward, claims gain effective authority only if the inner scope's policy explicitly accepts them.

#### §3.87.7.4 Isolation Classes Re-State at Each Scope

> **[Figure D46 — Composition Stack Across a Federation (three frameworks at different regulated-subvertical postures showing per-framework composition resolution)]**

Class A items are categorically inviolable **at the scope where they live** and are **inherited as Class A** at outer scopes that enclose that scope. Inheritance applies only in the outward direction.

### §3.87.8 Framework-Localized and Federated Primitive Classes

> **[Figure D33 — Four Primitive Classes Crossing-Permissions Matrix]**

#### §3.87.8.1 Class 1 — Framework-Localized, Immovable

Class 1 primitives are the live operational supervisory state of a framework. They never cross any perimeter under any condition. **Members:** cryptographic key material in all forms; cryptographic operations on key material; validator working state and in-flight consensus state per §3.18; Coherence Monitor working state; policy bundle as artifact (binary form in the framework's running format; the bundle's *content* may be reproduced in another framework via §3.89, but the artifact does not migrate); Recovery Procedure internals; authentication session state.

**Crossing semantics.** Class 1 items do not cross P_f under any envelope, any posture, any operational condition. They are categorically excluded from the projection allowlist of any egress request (§3.87.1.1 Hard Rule 2). Class 1 maps to Isolation Class A (§3.87.3.1).

#### §3.87.8.2 Class 2 — Framework-Localized, Migration-Portable

Class 2 primitives are historical supervisory records. They do not federate during live operation. They ARE transferable under sealed workload offload (Class 4, §3.87.8.4). **Members:** Witness Layer entries per §3.10; completed Decision Records (per §3.12 including boundary-crossing subtype); provenance records on memory items; Recovery Procedure execution records; policy-bundle version history.

**Crossing semantics.** Class 2 items do not cross P_f in live operation. During workload offload, they cross P_f as part of the sealed offload payload (Class 4); the crossing is permitted under an UPGRADE or DISASTER_RECOVERY federation envelope. Cross-framework reads of Class 2 in steady state are categorically refused at the P_f gate.

**Class 2 belongs to Isolation Class A** (framework-localized) and is subject to Class A's categorical immutability and non-crossability under live operation. The narrowly-scoped migration exception is the single permitted access pattern outside the originating framework.

#### §3.87.8.3 Class 3 — Federated

Class 3 primitives cross framework perimeters under federation envelope (§3.87.9). **Members:** memory composition (live cross-framework memory reads and writes); agent composition (live cross-framework delegation and collaboration).

**Crossing semantics.** Class 3 items cross P_f under any active envelope whose `permitted_class_set` includes Class 3. They are subject to sanitization at each crossing. Cross-framework provenance is preserved.

**Class 3 is Isolation Class C** (configurable) with respect to access policy. XSI-AIMS does not categorically restrict Class 3 crossings beyond requiring envelope presence and per-operation Decision Records.

#### §3.87.8.4 Class 4 — Offloadable Workload

Class 4 is a *bundling* of Class 2 + Class 3 under a sealed offload protocol. **Members:** a class 4 payload contains the originating framework's Class 2 records; the originating framework's Class 3 state at the moment of offload; metadata describing the offload context. The receiving framework instantiates fresh Class 1 primitives on receipt; Class 1 does not migrate.

#### §3.87.8.5 Critical Clarification — Federated Composition + Localized Governance

Two principles underlie the four-class taxonomy:

1. **Memory composition and agent composition are federated.** Class 3 items cross framework perimeters under envelope. XSI-AIMS-conformant systems share live operational data structures across frameworks for collaboration purposes.
2. **Authentication and shadow governance are localized within the framework.** Class 1 items never cross. Each framework runs its own shadow governance.

The consequence: workloads can be offloaded between frameworks. The receiving framework instantiates fresh authentication and fresh shadow governance (fresh Class 1) while inheriting historical records (Class 2) and live operational data (Class 3 at moment of offload). The originating framework can be decommissioned without losing audit history, without losing operational state, and without leaking authentication or governance state.

### §3.87.9 Federation Envelope, Bridge Attestation, and Identity Bridge

#### §3.87.9.1 Federation Envelope

A **Federation Envelope** is a signed structural construct, time-bounded or persistent, that establishes mutual trust between two XSI-AIMS-conformant supervised contexts. Parties MAY be two frameworks within one Environment, two Environments within one federation, or two federations that have mutually attested at the federation root.

The envelope is the *only* sanctioned channel for the cross-context operations specified in §3.87.8 (memory composition, agent composition, workload offload). Implementations MUST NOT permit those operations through the Egress/Ingress Gates of §3.87.1.

```yaml
FederationEnvelope:
  envelope_id:                ULID
  scope:                      EnvelopeScope                              # intra_environment | inter_environment | inter_federation
  party_a:                    PeerPartyDescriptor
  party_b:                    PeerPartyDescriptor
  established_at:             ISO8601_with_microseconds
  expires_at:                 ISO8601_with_microseconds | null           # null => persistent
  purpose:                    EnvelopePurpose[]                          # subset of {federation, upgrade, offload, restore}
  authorized_modes:           CompositionMode[]                          # subset of {memory_composition, agent_composition, workload_offload}
  coexistence_class:          TIME_BOUNDED_TRANSITION | PERSISTENT_DUAL_FRAME
  attestation:                BridgeAttestationRecord                    # §3.87.9.2
  principal_authorization:    PrincipalAuthorizationRecord | NONE        # REQUIRED for offload OR scope crosses federation boundary
  decision_record_id:         ULID                                       # bridge-establishment Decision Record
  party_a_signature:          hybrid Ed25519 + ML-DSA-65 per §3.21.3
  party_b_signature:          hybrid Ed25519 + ML-DSA-65 per §3.21.3
  principal_signature:        hybrid Ed25519 + ML-DSA-65 per §3.21.3 | NONE
```

> **[Figure D39 — Federation Envelope Establishment]**

**Envelope lifecycle.** Three phases: **establishment** (Bridge Attestation performed; mutual signing; principal-co-signed for offload or federation-boundary scope); **operation** (lighter per-operation Decision Records reference envelope by `envelope_id`); **renewal or decommission** (time-bounded envelopes MUST renew before `expires_at`; persistent envelopes decommission only by explicit principal-authorized decommission Decision Record co-signed by both parties).

#### §3.87.9.2 Bridge Attestation Primitive

**Bridge Attestation** is the cryptographic primitive by which two parties establish mutual trust for a Federation Envelope. It uses **asymmetric attestation keys** that MUST be distinct from a party's operational signing keys. Attestation keys are themselves **Isolation Class A framework-localized-immovable** (§3.87.3.1); their private halves MUST NOT cross the Supervision Perimeter under any operational condition.

Bridge Attestation is **mutual**: both parties attest each other. The attestation exchange produces a `BridgeAttestationRecord` retained as a migration-portable historical record.

```yaml
BridgeAttestationRecord:
  attestation_id:                ULID
  party_a:                       PeerPartyDescriptor
  party_b:                       PeerPartyDescriptor
  party_a_claims:                AttestationClaimSet
  party_b_claims:                AttestationClaimSet
  party_a_attestation_pubkey:    PublicKey                               # hybrid Ed25519 + ML-DSA-65 per §3.21.3
  party_b_attestation_pubkey:    PublicKey
  exchange_transcript_hash:      bytes
  party_a_attestation_signature: Signature
  party_b_attestation_signature: Signature
  timestamp:                     ISO8601_with_microseconds
  expires_at:                    ISO8601_with_microseconds               # ≤ envelope lifetime
```

#### §3.87.9.3 Identity Bridge

The **Identity Bridge** is the primitive by which an agent's identity is preserved as **provenance** across a Federation Envelope while the agent gains a **fresh local identity** in the destination framework. Used during workload offload (primary), federated delegation, and persistent federation.

> **[Figure D40 — Identity Bridge Three-Step Provenance Flow]**

**Audit preservation rule.** Audit records MUST preserve foreign-framework identities **verbatim with framework prefix**. The canonical form is `framework_B::agent_47`. Translation of foreign identities into a local identifier space is prohibited.

**Sibling-AIMS-actor case.** When the destination framework is in a different federation set entirely, the Identity Bridge is established via **principal-mediated attestation** rather than automatic bridge. Each side's principal signs an attestation that this side's agent identity is what it claims to be. The bridge is operation-scoped, not envelope-scoped.

### §3.87.10 Workload Offload Protocol

> **[Figure D38 — Workload Offload 10-Phase Lifecycle]**
>
> **[Figure D43 — Framework Lifecycle]**

#### §3.87.10.1 Principal-Initiated

Workload offload MUST NOT begin without **principal authorization** via the principal interface (§3.87.6 Trigger 4). Principal authorization is recorded in the offload's establishment Decision Record and co-signed by the principal.

Automated offload triggered by health monitoring is permitted **only** when the policy bundle explicitly authorizes automated triggers per a tenant-defined policy clause, AND the principal is **notified retroactively within a bounded window** declared in that same policy clause.

#### §3.87.10.2 Atomicity

Workload offload MUST be **atomic**: it either completes fully or rolls back fully. **No partial state is permitted.** Audit logs from a partial transition are preserved as **evidence of abort**, not as a partial-progress record. The destination framework MUST treat the abort artifacts as opaque diagnostic data.

The §3.12 / §3.87.2 Decision Record schema includes an `ABORT` outcome for offload operations alongside `APPROVED`, `DOWNGRADE`, `ESCALATE`.

#### §3.87.10.3 In-Flight Agent Handling

Three operational modes:

| Mode | Conformance | Requirements |
|---|---|---|
| **Drain** | REQUIRED as minimum conformance | Implementation MUST provide |
| **Pause-and-resume** | OPTIONAL advanced capability (declared in conformance manifest as optional capability) | Working-context fidelity; deterministic replay; snapshot signing under bridge attestation |
| **Abort-and-replay** | OPTIONAL alternative to drain for time-bounded offloads | Per-agent abort records emitted to Witness Layer; destination replay MUST reference consensus-validation checkpoint per §3.18 |

A framework MUST support **drain or abort-and-replay** (at least one); it MAY support pause-and-resume.

#### §3.87.10.4 Configuration Intent Preservation

Configuration (policy bundle per §3.89) is **framework-localized-immovable**. What is preserved is **configuration intent**, in a version-neutral intent format: the source exports its active configuration in intent format; the destination imports and translates into its own bundle format; the principal re-authorizes any settings whose semantics changed between versions.

#### §3.87.10.5 External Identity Re-Keying

Framework-localized operational keys do not migrate (Class A immovable). External identities (signed certificates, API tokens, webhook registrations, signed bearer credentials) are anchored in the source framework's key material and would be orphaned at decommission unless re-keyed.

For each external identity: the destination generates a fresh key in its own Class A key store; registers the fresh key with the corresponding external service or CA; the source invalidates the corresponding external identity as part of decommission. External identities that cannot be re-keyed become an **offload blocker** unless explicitly waived by principal authorization.

#### §3.87.10.6 Multi-Tenant Transition

Multi-tenant deployments MUST preserve **tenant-ID tagging** throughout offload. Every workload artifact transferred MUST carry its tenant ID as an immutable tag. The destination framework's L-Form Ingress Gate enforces tenancy on ingest. Cross-tenant pollution is a conformance failure, not a recoverable error: any detected cross-pollination MUST abort the offload per §3.87.10.2.

#### §3.87.10.7 Time-Bounded vs Persistent Dual-Frame Coexistence

| Configuration | Duration | Termination | Steady state? |
|---|---|---|---|
| **Bounded transition** (upgrade) | Sovereign-decommissioned at completion | One party decommissioned at the end | No — transitional |
| **Persistent federation** | Long-term | Neither party decommissioned by the relationship | Yes — steady state |

Implementations MUST declare the configuration class in the envelope's `coexistence_class` field. M-Constraining-mode validation MUST refuse operations that mismatch the envelope's declared class.

### §3.87.11 Conformance

> **[Figure D45 — Decision Record Volume vs Deployment Scale (cost-of-conformance curves by perimeter posture for capacity planning)]**

An XSI-AIMS-conformant Environment MUST:

1. Implement the L-Form Egress Gate and L-Form Ingress Gate as specified in §3.87.1 (archetypal manifestation per §3.X.PERIM per D8.1).
2. Maintain the Isolation Lattice of §3.87.3 (Class A / B / C, D8.3), including categorical Class A and minimal Class B.
3. Honor the composition rule of §3.87.3.5 (asymmetric upward-only ratchet).
4. Emit a Signed Boundary-Crossing Decision Record per §3.87.2 (§3.12 BOUNDARY_CROSSING subtype, D8.2) for every boundary crossing.
5. Honor the Non-AIMS Actor identity model of §3.87.4.
6. Declare a Perimeter Posture per §3.87.5 in its conformance manifest.
7. Implement the Principal User Engagement pattern of §3.87.6 (D8.4) with all four canonical triggers.
8. Honor the multi-scope perimeter composition rules of §3.87.7.
9. Honor the framework-localized and federated primitive class taxonomy of §3.87.8.
10. Implement the Federation Envelope, Bridge Attestation, and Identity Bridge primitives of §3.87.9 when participating in federation, upgrade, or workload offload.
11. Honor the Workload Offload Protocol Requirements of §3.87.10.
12. Apply the sanitization-on-ingress rule of §3.87.1.2.

An XSI-AIMS-conformant Environment MUST NOT:

1. Permit any mechanism by which the Egress Gate is bypassed.
2. Permit retagging of `untrusted-external` content to any trusted classification.
3. Permit any Isolation Class A item to cross the Supervision Perimeter under any operational condition.
4. Permit a DOWNGRADE outcome from M-Constraining-mode validation to relax the original request.
5. Permit an UPGRADE path from M-Constraining-mode validation at all.
6. Address a non-AIMS actor as if it were a supervised agent.
7. Permit any framework-localized-immovable primitive to migrate during workload offload (per §3.87.8.1).
8. Permit modification of migration-portable records after they have been written (per §3.87.8.2).
9. Permit a workload offload to begin without principal authorization through trigger 4 of §3.87.6, except under explicit policy-bundled automated-trigger authorization with retroactive principal notification.
10. Permit a partial workload offload to remain in indeterminate state.


---

## §3.88 — Connectivity Modes and Hybrid-Mode Federation Composition

This section formalizes the Connectivity Mode taxonomy for XSI-AIMS deployments that span Environments at differing assurance levels, specifies how Authority Chain claims (§3.3) attenuate as they cross Environment boundaries, extends the §3.18.5 IAME envelope with a delegated-task structure carrying assurance metadata, defines the External Service Trust Profile claim shape for public-cloud LLM dependencies, specifies the Cross-Tier Witness Synchronization Protocol complementing §3.20 DCP at event-level granularity, and specifies cross-Environment compositional review. **Connectivity Mode** is the network posture of a deployment; it is orthogonal to the §3.21.5 Environment Type taxonomy (APPLIANCE / SOVEREIGN_CLOUD / PRIVATELY_HOSTED / PUBLICLY_DEPLOYED) which describes deployment substrate.

### §3.88.1 Five Connectivity Modes

> **[Figure D44 — Federation Topology Patterns (degenerate base case; mid-upgrade dual-framework; hybrid-mode federation; multi-federation with sibling-AIMS treaty)]**

XSI-AIMS implementations declare their Connectivity Mode at provisioning time. Mode determines distribution paths, freshness assertion requirements, Witness chain topology, and Authority Chain freshness windows. A deployment MAY declare support for multiple modes and MUST select exactly one as the active mode at any given time.

| Mode | Network posture | Trust-root location | Inference location | Distribution path |
|---|---|---|---|---|
| `CONNECTED` | Continuous online | In-Environment | In-Environment | Online repository fetch |
| `PARTIAL` | Intermittent | In-Environment | In-Environment | Hybrid: online when reachable, queued on partition |
| `AIR_GAPPED` | Disconnected | In-Environment | In-Environment | Physical media (signed, attested) |
| `CONNECTED_WITH_EXTERNAL_INFERENCE` | Continuous online | In-Environment for scaffolding; external for inference | External (commodity LLM API) | Online + External Service Trust Profile |
| `HYBRID` | Multi-tier; per-Environment posture | Per-Environment trust roots; federated | Per-Environment, mixed | Per-Environment per its mode |

`HYBRID` is the meta-mode that compositions of the first four enter when multiple Environments are coupled into a single XSI-AIMS-conformant deployment. Each constituent Environment carries its own non-`HYBRID` Connectivity Mode.

### §3.88.2 Per-Mode Conformance Requirements

| Requirement | `CONNECTED` | `PARTIAL` | `AIR_GAPPED` | `CONNECTED_WITH_EXTERNAL_INFERENCE` | `HYBRID` |
|---|---|---|---|---|---|
| Online Witness log | REQUIRED | REQUIRED when reachable | NOT APPLICABLE | REQUIRED for scaffolding | Per constituent |
| Local Witness mirror | OPTIONAL | REQUIRED | REQUIRED | OPTIONAL | Per constituent |
| Freshness assertion cadence | ≤ PT5M default | ≤ PT24H default | Operator-signed periodic | ≤ PT5M | Per constituent |
| Policy Bundle distribution | Online repository | Online + signed-cache fallback | Physical media (signed) | Online | Per constituent |
| External Service Trust Profile (§3.88.6) | NOT APPLICABLE | NOT APPLICABLE | NOT APPLICABLE | REQUIRED | REQUIRED for any constituent in this mode |
| DCP §3.20 cross-Environment reconciliation | OPTIONAL | OPTIONAL | OPTIONAL | OPTIONAL | REQUIRED between constituents |
| Witness Synchronization (§3.88.7) | OPTIONAL | OPTIONAL | OPTIONAL | OPTIONAL | REQUIRED between constituents |

### §3.88.3 Mode Declaration

An Environment MUST publish its active Connectivity Mode in its conformance manifest. Cross-Environment messages (§3.18.5 IAME, §3.20 DCP) MUST include the sending Environment's active mode in the envelope header. Receiving Environments MAY refuse delegations originating from modes whose assurance posture is incompatible with the action class invoked.

```yaml
ConformanceManifest:
  environment_id:        EnvironmentID
  environment_type:      APPLIANCE | SOVEREIGN_CLOUD | PRIVATELY_HOSTED | PUBLICLY_DEPLOYED   # §3.21.5 substrate
  active_mode:           ConnectivityMode                               # §3.88.1 network posture (orthogonal to environment_type)
  supported_modes:       ConnectivityMode[]                             # superset including active_mode
  perimeter_posture:     closed | restricted | open                     # §3.87.5
  trust_root:            TrustRootDescriptor                            # §3.21
  policy_bundle_version: SemVer
  manifest_signature:    hybrid Ed25519 + ML-DSA-65 per §3.21.3
```

**Environment Type and Connectivity Mode are orthogonal axes.** Environment Type describes the deployment substrate (the physical or virtual hardware/cloud configuration). Connectivity Mode describes network posture (the connectivity stance of the deployment to external services). An APPLIANCE Environment is typically but not necessarily in AIR_GAPPED Connectivity Mode; a SOVEREIGN_CLOUD Environment may be in CONNECTED or HYBRID mode.

### §3.88.4 Authority Chain Assurance Attenuation

§3.3 Authority Chain defines authority delegation but does not specify how the *assurance* of a principal claim changes as the claim propagates across Environment boundaries. Authority Chain claims carry a typed assurance tuple aligned with **NIST SP 800-63** Identity, Authenticator, and Federation Assurance Levels:

```yaml
AssuranceTuple:
  ial:            1 | 2 | 3                                              # Identity Assurance Level (NIST SP 800-63A)
  aal:            1 | 2 | 3                                              # Authenticator Assurance Level (NIST SP 800-63B)
  fal:            1 | 2 | 3                                              # Federation Assurance Level (NIST SP 800-63C)
  freshness:      ISO8601_with_microseconds
  binding:        BindingClaim[]

BindingClaim:
  type:           BOUND_TO_DEPLOYMENT_ROOT                               # TPM-/HSM-/secure-element-attested local session
                | BOUND_TO_PAIRED_DEVICE                                 # Hardware-bound key on paired device
                | BOUND_TO_EXTERNAL_IDP                                  # Federated through external IDP
                | DELEGATED_THROUGH_INTERMEDIARY                         # Crossed at least one tier boundary
                | EXTERNAL_SERVICE_PRINCIPAL                             # Service-principal identity for external LLM call
  evidence:       opaque_bytes
  evidence_sig:   hybrid Ed25519 + ML-DSA-65 per §3.21.3
```

**Attenuation Rules.**

- **Rule A1.** `BOUND_TO_DEPLOYMENT_ROOT` is non-transitive. On crossing any Environment boundary, it MUST be removed and `DELEGATED_THROUGH_INTERMEDIARY` appended.
- **Rule A2.** `BOUND_TO_PAIRED_DEVICE` is conditionally transitive. Survives a tier crossing only if the receiving Environment can independently re-verify the paired-device attestation through the same trust root.
- **Rule A3.** `BOUND_TO_EXTERNAL_IDP` is transitive across Environments that federate against the same IDP.
- **Rule A4.** `DELEGATED_THROUGH_INTERMEDIARY` accumulates. Each tier crossing adds an additional claim with its own evidence. Receiving Environments MAY enforce a maximum delegation depth.
- **Rule A5.** Numeric assurance levels (IAL/AAL/FAL) MAY be attenuated per receiving Environment policy but MUST NOT be elevated.
- **Rule A6.** Freshness is monotonic. The freshness timestamp MUST NOT be advanced.

**Action-class gating against effective assurance.** §3.3 `AuthorityScope` is extended with `ActionClassRequirement` specifying per-action-class minimum-assurance. M-Constraining MUST refuse an action whose required minimum assurance exceeds the effective assurance tuple of the requesting Authority Chain.

```yaml
ActionClassRequirement:
  action_class:           string
  min_ial:                1 | 2 | 3
  min_aal:                1 | 2 | 3
  min_fal:                1 | 2 | 3 | NOT_APPLICABLE
  required_bindings:      BindingClaimType[]                             # ALL must be present in effective tuple
  forbidden_bindings:     BindingClaimType[]                             # NONE may be present in effective tuple
  max_delegation_depth:   number                                         # counts DELEGATED_THROUGH_INTERMEDIARY claims
  max_freshness_age:      Duration
```

### §3.88.5 Delegated Task Envelope (extension to §3.18.5 IAME)

When an envelope crosses an Environment boundary, the §3.18.5 IAME envelope is extended with a `delegation` block:

```yaml
delegation:
  delegating_environment:      EnvironmentID
  receiving_environment:       EnvironmentID
  originating_plan_id:         PlanID                                    # §3.88.8 Cross-Tier Compositional Review
  delegating_authority_chain:  AuthorityChain                            # §3.3 — full chain at originating Env
  effective_assurance:         AssuranceTuple                            # §3.88.4 — recomputed by receiving Env
  action_class:                string
  declared_action_requirement: ActionClassRequirement
  attenuation_log:             AttenuationRecord[]                       # each tier crossing logged
  delegation_signature:        hybrid Ed25519 + ML-DSA-65 per §3.21.3    # signed by delegating Environment's trust root
```

The `delegation_signature` is **additional** to the existing `envelope.sender.signature` of §3.18.5; it attests that the delegating **Environment as a whole** (signed under that Environment's trust root, not under any individual agent's key) authorized the cross-Environment delegation. Both signatures MUST be present; neither replaces the other.

### §3.88.6 External Service Trust Profile

`CONNECTED_WITH_EXTERNAL_INFERENCE` mode requires that XSI-AIMS-authored components establish trust in external inference providers. The trust derives from contractual commitments and provider-published attestations rather than from cryptographic chain to a customer-controlled trust root. **Composes with §3.34 supply-chain validation:** §3.34 attests who built the artifact; ExternalServiceTrustProfile attests who runs the hosted service. An external commodity LLM endpoint needs both.

```yaml
ExternalServiceTrustProfile:
  provider_id:                 string                                    # e.g., "foundation-model-provider-A", "hosted-model-endpoint-B"
  provider_endpoint:           URL
  provider_endpoint_cert_pin:  CertFingerprint                           # TLS cert pinning
  model_version_pin:           string                                    # provider-published model identifier

  jurisdictional_attestation:
    declared_jurisdiction:     CountryCode | RegionCode
    attestation_source:        PROVIDER_CONTRACT | PROVIDER_SIGNED | THIRD_PARTY_AUDIT
    attestation_evidence:      opaque_bytes
    attestation_signature:     hybrid Ed25519 + ML-DSA-65 | NONE

  data_handling_commitment:
    no_training_use:           boolean
    retention_window:          Duration | INDEFINITE
    deletion_on_request:       boolean
    commitment_source:         PROVIDER_CONTRACT | PROVIDER_TOS | THIRD_PARTY_AUDIT
    commitment_evidence:       opaque_bytes

  provider_aims_conformance:                                             # OPTIONAL — populated only if provider claims XSI-AIMS conformance
    conformant:                boolean
    conformance_version:       SemVer | NONE
    conformance_attestation:   hybrid Ed25519 + ML-DSA-65 | NONE

  customer_acceptance:
    accepted_by_principal:     PrincipalID
    accepted_at:               ISO8601_with_microseconds
    acceptance_signature:      hybrid Ed25519 + ML-DSA-65 per §3.21.3
```

A `CONNECTED_WITH_EXTERNAL_INFERENCE` Environment MUST publish its External Service Trust Profile in its conformance manifest. Policy Bundle action classes MAY require minimum profile properties; M-Constraining MUST refuse an action whose action-class profile requirement is not met.

### §3.88.7 Cross-Tier Witness Synchronization Protocol (CTWSP)

§3.20 DCP reconciles state across Environments at coarse cadence (PT5M default). For cross-tier audit reconstruction, the Witness Layer (§3.10) requires finer-grained event-level cross-references. The Cross-Tier Witness Synchronization Protocol (CTWSP) complements DCP at event-level granularity.

When an envelope crosses an Environment boundary, the originating Environment's Witness Layer MUST emit a `delegated_to` cross-reference, and the receiving Environment's Witness Layer MUST emit a `received_from` cross-reference, both signed by the respective Environment trust root.

```yaml
CrossTierWitnessReference:
  reference_type:             DELEGATED_TO | RECEIVED_FROM | RESPONDED_TO | RESPONDED_FROM
  local_witness_record:       WitnessRecordID
  remote_environment:         EnvironmentID
  remote_witness_record:      WitnessRecordID
  envelope_id:                ULID
  cross_reference_signature:  hybrid Ed25519 + ML-DSA-65 per §3.21.3
```

**Synchronization cadence.** Cross-references MUST be emitted within PT1S of the cross-Environment envelope being processed. Cross-references MUST be propagated to peer Environments within the next DCP reconciliation window per §3.20.

**Reconstruction across AIR_GAPPED Environments** depends on physical-media synchronization of Witness chain summaries.

**Interoperability with platform ledgers.** XSI-AIMS-conformant implementations on platforms that maintain their own tamper-evident ledgers (e.g., a sovereign-cloud platform's access-ledger service) SHOULD emit additional cross-references linking XSI-AIMS Witness chain entries to the platform ledger's corresponding entries. The XSI-AIMS Witness chain is authoritative for XSI-AIMS-domain events.

### §3.88.8 Cross-Tier Compositional Review

A plan whose individual steps are each policy-permissible in their respective Environments may compose into a forbidden action when viewed end-to-end. M-Integrative review (§3.6 Proportional Integration Function and §3.42 Quorum Consensus Architecture) of such plans MUST operate at plan scope, not Environment scope.

```yaml
MultiEnvironmentPlan:
  plan_id:               PlanID
  plan_authority_chain:  AuthorityChain
  plan_steps:            PlanStep[]
  plan_dependencies:     DependencyEdge[]                                # partial ordering
  plan_signature:        hybrid Ed25519 + ML-DSA-65 per §3.21.3

PlanStep:
  step_id:                  StepID
  executing_environment:    EnvironmentID
  action_class:             string
  step_input_refs:          StepID[]
  step_assurance_required:  ActionClassRequirement
  step_data_sensitivity:    DataSensitivityLevel                          # §3.36 Output Sensitivity Filter
```

Before any step executes, the originating Environment MUST submit the full plan to its M-Integrative review. The review:

- Evaluates whether the plan as a whole pattern-matches any signature in the Compositional Review Profile.
- Evaluates whether data flows respect the data-sensitivity classification of each step's executing Environment.
- Evaluates whether cumulative assurance attenuation across the plan still satisfies the assurance requirement of every step.
- Evaluates whether the plan's compositional intent (per §3.41 Multi-Level Interpretation) matches its declared purpose.

Each Environment receiving a delegated step MUST evaluate the step against its own M-Constraining policy in addition to the originating Environment's plan-level review. Step-execution-time refusal triggers the originating Environment's escalation path; the plan is suspended until resolution.


---

## §3.89 — Policy Bundle Format and Substrate Tagging

This section normatively defines the **Policy Bundle** as an XSI-AIMS artifact and specifies a substrate-tagging extension. The Policy Bundle is the signed, versioned artifact that carries M-Constraining action class definitions, action requirements, and enforcement metadata that an XSI-AIMS-conformant deployment loads at provisioning and consults at every action evaluation. **§3.54 ENVIRONMENT_POLICY_BUNDLE is the deployment-side instantiation of a §3.89 Policy Bundle.** Prior spec revisions referenced "ENVIRONMENT_POLICY_BUNDLE" operationally; §3.89 supplies its normative artifact format.

Substrate tagging makes it possible for the same logical bundle to ship in multiple substrate-tagged variants whose substrate-specific action implementations differ while their abstract action contracts agree.

### §3.89.1 Bundle Structure

```yaml
PolicyBundle:
  bundle_id:                  ULID
  bundle_version:             SemVer
  bundle_name:                string
  bundle_purpose:             string
  bundle_issued_at:           ISO8601_with_microseconds
  bundle_issuer:              IssuerDescriptor
  bundle_compatibility:       BundleCompatibilitySpec
  substrate_compatibility:    SubstrateCompatibilitySpec
  trust_root_requirements:    TrustRootRequirementSpec
  upgrade_class:              in_place_compatible | reimage_required | migration_required
  prior_bundle_refs:          BundleRef[]                                # supersession chain
  action_classes:             ActionClass[]
  bundle_signature:           BundleSignature
```

The `ENVIRONMENT_POLICY_BUNDLE` schema identifier (per §3.54) is preserved as a deployment-side label for the loaded PolicyBundle artifact. The two terms refer to the same construct viewed from different scopes: §3.89 PolicyBundle is the on-disk / in-transit artifact; ENVIRONMENT_POLICY_BUNDLE is the deployment-resident, hierarchically-stacked-with-overlays operational form.

### §3.89.2 Action Class Structure

Action classes are the substantive carrier of M-Constraining policy.

```yaml
ActionClass:
  class_id:                   string
  class_kind:                 ABSTRACT | CONCRETE | UNIVERSAL
  substrate_tags:             SubstrateTag[]                             # populated for CONCRETE; empty for UNIVERSAL; resolves_to map for ABSTRACT
  resolves_to:                map<SubstrateID, ClassID>                  # populated for ABSTRACT only
  action_requirement:         ActionClassRequirement                     # §3.88.4 assurance gating
  required_authority_scope:   AuthorityScope                             # §3.3
  declared_side_effects:      SideEffectDescriptor[]
  declared_witness_events:    WitnessEventDescriptor[]                   # §3.10
  enforcement_mode:           DENY_BY_DEFAULT | ALLOW_WITH_WITNESS | ALLOW_WITH_QUORUM
  applicable_archetypes:      ArchetypeID[]                              # §3.16; empty = all
  rationale:                  string
```

### §3.89.3 Action Class Kinds

- **UNIVERSAL** — applies on every substrate identically. Bundle-load-time substrate-tag check is a no-op for UNIVERSAL classes. Examples (non-normative): `local_user_create`, `ssh_config_modify`.
- **CONCRETE** — applies on one or more specific substrates listed in `substrate_tags`. Bundle-load-time substrate-tag check refuses the action class on substrates not in the tag list. Examples: `firmware_update_secure_processor` (accelerator-family-specific), `firmware_update_gpu_fw` (accelerator-family-specific), `accelerator_runtime_install` (accelerator-family-specific).
- **ABSTRACT** — declares an action contract that resolves to a CONCRETE class at execution time. Carries a `resolves_to` map from substrate identifier to the CONCRETE class identifier. The resolution is performed by the deployment's runtime when an abstract action is invoked. Examples: `firmware_update_gpu` (resolves per accelerator family to the family-specific CONCRETE class).

A bundle MAY contain action classes of all three kinds.

### §3.89.4 Bundle Compatibility and Signature

```yaml
BundleCompatibilitySpec:
  min_aims_spec_version:      SemVer
  max_aims_spec_version:      SemVer | NONE
  min_acceptable_predecessor: SemVer | NONE
  required_companion_bundles: BundleRef[]
  forbidden_companion_bundles: BundleRef[]

BundleSignature:
  signature_alg:              hybrid Ed25519 + ML-DSA-65 per §3.21.3
  signature_value:            opaque_bytes                               # over canonical CBOR of bundle minus this field
  signing_key_id:             KeyID
  countersignatures:          CounterSignature[]                         # OPTIONAL multi-sig per Compositional Review Profile
```

The bundle signature is computed over the canonical CBOR encoding of the bundle with the `bundle_signature` field excluded. A bundle MUST be rejected if signature verification fails on the primary signature.

### §3.89.5 Substrate Identifier Shape

A SubstrateID is a structured string:

```
SubstrateID       := SubstrateFamily ':' SubstrateTier (':' SubstrateProperty)*
SubstrateFamily   := <namespace-prefixed family name>      e.g., "vendorA-accelerator", "vendorB-accelerator", "generic-x86_64", "cloud-vm-accelerator-series"
SubstrateTier     := <substrate revision / generation>     e.g., "v1", "gen1", "gen2"
SubstrateProperty := <key=value pair>                     e.g., "firmware-min=24.10", "confidential-compute=enabled"

Examples:
  vendorA-accelerator:gen1
  vendorB-accelerator:gen1:firmware-min=24.06
  generic-x86_64:v1:cpu-features=avx512,sse4.2
  cloud-vm-accelerator-series:gen1
  any                                                       # universal — matches every substrate
```

The leftmost component identifies the substrate family; the second component identifies the substrate tier; subsequent property components carry conformance-relevant detail. **XSI-AIMS is substrate-agnostic.** The substrate registry is governance-process surface maintained alongside the XSI-AIMS spec; specific substrate identifiers are not enumerated normatively in the spec itself.

### §3.89.6 Substrate Compatibility Spec

A bundle declares which substrates it can be loaded on:

```yaml
SubstrateCompatibilitySpec:
  declared_substrates:        SubstrateID[]                              # at least one; `any` matches universally
  refuse_load_if_unknown:     boolean                                    # default true — refuse load on substrates not listed
  preferred_substrate_order:  SubstrateID[]                              # OPTIONAL ranking for runtime substrate-selection
```

At bundle-load time, the loading deployment compares its declared substrate (from its conformance manifest) against the bundle's `declared_substrates`. If `refuse_load_if_unknown` is true and no match is found, the load is refused with explicit error.

### §3.89.7 Resolution Semantics for ABSTRACT Action Classes

When an ABSTRACT action class is invoked at runtime, the deployment's substrate (from its conformance manifest) selects the CONCRETE variant from the ABSTRACT class's `resolves_to` map. If no CONCRETE variant exists for the deployment's substrate, the invocation MUST fail with explicit "no substrate-specific implementation" error. The deployment MUST NOT fall back to a different-substrate CONCRETE variant; substrate-specificity is normative for CONCRETE classes.

### §3.89.8 Bundle-Substrate Conformance Test Coverage

For each CONCRETE action class in a bundle, the bundle's conformance test suite MUST include at least one test that exercises the CONCRETE implementation on its declared substrate. For each ABSTRACT action class, the conformance test suite MUST include at least one test per substrate listed in the `resolves_to` map. UNIVERSAL action classes require at least one test (substrate-independent).

Bundle issuers SHOULD publish substrate-specific conformance test results alongside the bundle artifact. Receivers MAY refuse to load bundles whose substrate-specific conformance test claims are unverifiable.

### §3.89.9 Composition with §3.54 Declarative Constitution Layer

The §3.54 Declarative Constitution Layer specifies hierarchical_stacking semantics (Environment-default → organization → principal → per-task) for ENVIRONMENT_POLICY_BUNDLE entries. A §3.89 Policy Bundle becomes an ENVIRONMENT_POLICY_BUNDLE when loaded into a deployment's policy stack; the §3.54 stacking semantics apply to the action classes contained in the bundle. Action classes that conflict with higher-precedence principles are rejected at bundle-load time per §3.54 consistency validation.

---

*End of XSI-AIMS Specification, Version 2.0.*
