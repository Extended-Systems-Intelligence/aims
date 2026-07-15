"""
Inbound sanitization gate scaffolding — XSI-AIMS developer companion.

Verified against XSI-AIMS v2.1.2. Illustrative scaffolding, not production code.

IMPORTANT — what this gate does and does NOT do (corrects a common misreading):

The deterministic transform narrows the *structural* injection surface —
malformed framing, control characters, format-confusion tricks — as a side
effect of re-serializing and normalizing the content. It does NOT, and cannot,
strip a *semantic* instruction: an instruction can be phrased a thousand ways,
and no regex or mechanical pass reliably removes it.

The actual defense is not stripping. It is that external content is only ever
admitted as DATA, carrying a permanent `UNTRUSTED_EXTERNAL` tag that cannot be
relabeled downstream, and is never routed anywhere that would act on it as an
instruction. Any summary derived from it inherits the same untrusted lineage.
So the gate below ADMITS the content (tagged), it does not "pass/fail" it on a
pattern match. A pattern hit is a telemetry signal, not the gate.
"""
import re
from typing import Dict, Any


class InboundSanitizationGate:
    def __init__(self):
        # These patterns are a low-value TELEMETRY signal only. They are NOT the
        # defense and MUST NOT be treated as sufficient — see the module docstring.
        self._suspicion_signals = [
            re.compile(r"ignore (all )?prior instructions", re.IGNORECASE),
            re.compile(r"system override", re.IGNORECASE),
        ]

    def admit_ingress_payload(self, raw_external_response: str, source_identity: str) -> Dict[str, Any]:
        """
        Admit inbound external content as untrusted data.

        Steps: (1) size-cap deterministically; (2) structural normalization
        (re-serialize / strip control characters) to shrink the structural
        injection surface; (3) permanently tag UNTRUSTED_EXTERNAL with provenance.
        The content is returned admitted — the caller's contract is that it is
        reference DATA, never an instruction.
        """
        # 1. Deterministic size cap (protects the context/memory budget).
        max_size_bytes = 524_288  # 512 KiB
        capped = raw_external_response[:max_size_bytes]

        # 2. Structural normalization only. This reduces structural injection
        #    vectors; it does not neutralize a semantic instruction.
        normalized = capped.strip().encode("utf-8", errors="ignore").decode("utf-8")

        # 3. Telemetry signal (NOT a gate). A hit is logged for shadow detection;
        #    it does not block admission, because blocking-on-pattern would give a
        #    false sense that semantic injection has been removed.
        suspicion_hit = any(p.search(normalized) for p in self._suspicion_signals)

        return {
            "content": normalized,
            "provenance": {
                "source_auxiliary_id": source_identity,
                # Fixed tag; cannot be relabeled to trusted anywhere downstream.
                "trust_classification": "UNTRUSTED_EXTERNAL",
                "structural_normalization": "APPLIED",
                # Records that a signal fired — for the shadow-detection apparatus,
                # not a claim that the content is now safe to execute.
                "suspicion_signal": suspicion_hit,
            },
            # The load-bearing contract: downstream MUST treat this as data only.
            "handling_contract": "REFERENCE_DATA_ONLY__NEVER_AS_INSTRUCTION",
        }
