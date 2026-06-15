# AIMS Implementation Diagrams — Staging Directory

**Status:** Set complete — D01 pilot 2026-04-29 + D02–D11 generated 2026-04-29 against the locked visual style.
**Sanitization rule:** canonical AIMS engineering lexicon only.

These diagrams are **educational / implementation aids** intended for distribution alongside the public AIMS specification — design partners, NIST CAISI, standards bodies, downstream implementers.

## Diagram set (11 diagrams)

| ID | Title | Type | Status |
|---|---|---|---|
| D01 | AIMS Stacked Architecture | Stacked Architecture | **Pilot complete** |
| D02 | AIP Wire Format Envelope | Record Layout | **Complete** |
| D03 | IAME Envelope | Record Layout | **Complete** |
| D04 | The Ten Archetypes Taxonomy | Taxonomy Tree | **Complete** |
| D05 | Witness Chain Formation | Sequence Diagram | **Complete** |
| D06 | Trust Gradient | Concept + Decision Flow | **Complete** |
| D07 | Shadow Detection Process Flow | Process Flow | **Complete** |
| D08 | AIP Conformance Levels | Comparison Table | **Complete** |
| D09 | Substrate Identity & Multi-Model Governance | Block Diagram | **Complete** |
| D10 | Three Principles Concept Diagram | Concept Diagram | **Complete** |
| D11 | Four-Layer Memory Architecture | Stacked Architecture | **Complete** |

## Recommended reading sequence in the AIMS spec appendix

D10 → D01 → D04 → D09 → D11 → D02 → D03 → D05 → D06 → D07 → D08

(Three Principles → Architecture → Archetypes → Substrate Identity → Memory → AIP wire format → IAME envelope → Witness chain → Trust gradient → Shadow detection → Conformance levels.)

## Notes

- D01 reflects the **canonical AIMS structure**: 4 operational layers (L-Intent / L-Plan / L-Form / L-Exec) + 3 functional modes (M-Generative / M-Constraining / M-Integrative) + 6-pattern safety substrate. The earlier informal phrasing of "8 functional layers" does not match the spec — the canonical count is 4 layers + 3 modes.
- Style: black-only strokes, sans-serif labels, no fills.
- D02–D11 generated 2026-04-29 against the same `viewBox="0 0 850 1100"` US Letter geometry, unique `arrow_dNN` marker IDs per file (no clashes if embedded together), header pattern matching D01 (`DXX` 18pt bold + italic title + source-section line), numerals placed outside component boxes, and ASCII-only content with the single carryover `§` glyph (matching D01's pilot precedent — renders cleanly via xmllint + ImageMagick).
- All 10 SVGs validate via `xmllint --noout` and render to PNG via ImageMagick `convert`. Rendered PNGs are written to `rendered/` for visual review.

## Generation history

- 2026-04-29 — D01 pilot generated and visual style locked (numeral placement outside boxes, hash-arrow channel routing, ASCII-only constraint to avoid Write-tool unicode truncation, single-`§` carryover for spec section references).
- 2026-04-29 — D02–D11 generated in a single session against the locked style. All files xmllint-clean, terminate with `</svg>\n`, and render via ImageMagick. Sanitization clean: only canonical AIMS engineering lexicon (`L-Intent` / `L-Plan` / `L-Form` / `L-Exec`, `M-Generative` / `M-Constraining` / `M-Integrative`, `IAME`, `AIP`, `Trust Gradient`, `aims_auxiliary_tier`, `domain_affiliations`, `path_id`, `shadow_seed.archetype`, `Three Principles`).
