"""
Bridge-of-Trust Executor scaffolding — XSI-AIMS developer companion.

Verified against XSI-AIMS v2.1.2. Illustrative scaffolding, not production code.

The Executor is the sole Execution-layer archetype and the only one that reaches
anything outside the seal. It isolates two cryptographically separated enclaves —
InternalEnclave (internal-domain keys) and ExternalEnclave (external-domain keys)
— joined only by a narrow Bridge across which nothing but plaintext ever passes,
and only after the crossing is verified and witnessed.
"""
import abc
import hashlib
from typing import Dict, Any, Tuple


class CryptographicEnclaveException(Exception):
    """Raised when a domain boundary or enclave constraint is violated."""


class InternalEnclave:
    """Houses internal-domain signing keys; verifies directives from the Orchestrator."""

    def __init__(self, internal_key_store: Dict[str, Any]):
        self._keys = internal_key_store

    def verify_and_sign_handoff(self, iame_envelope: Dict[str, Any]) -> Tuple[Dict[str, Any], str]:
        """
        Bridge step 2: verify the internal envelope, then sign THIS enclave's
        side of the handoff record.

        The handoff record is *dual*-signed, but one enclave cannot produce a
        dual signature alone: the internal enclave signs its side here, and the
        external enclave counter-signs on receipt (see
        ExternalEnclave.countersign_handoff). Only the pair of signatures proves
        the directive actually crossed the bridge.
        """
        if iame_envelope.get("cryptographic_domain") != "internal":
            raise CryptographicEnclaveException(
                "Domain boundary violation: expected an internal envelope.")
        # [deterministic internal-signature validation would occur here]
        payload = iame_envelope["body"]["opaque_payload_bytes"]
        internal_half_sig = "INT_SIG_" + hashlib.sha256(payload.encode()).hexdigest()[:16]
        return iame_envelope["body"], internal_half_sig


class ExternalEnclave:
    """Houses external-domain keys; handles counter-signing, attestation, and egress."""

    def __init__(self, external_key_store: Dict[str, Any]):
        self._keys = external_key_store

    def countersign_handoff(self, plaintext_payload: Dict[str, Any], internal_half_sig: str) -> str:
        """
        Bridge step 3 (completion): the receiving (external) enclave counter-signs
        the moment it takes the plaintext. internal_half_sig + this counter-sign
        together form the dual-signed handoff record, witnessed at the time it
        happens rather than asserted by one side.
        """
        external_half_sig = "EXT_HANDOFF_SIG_" + hashlib.sha256(
            (internal_half_sig + str(plaintext_payload)).encode()).hexdigest()[:16]
        return f"{internal_half_sig}::{external_half_sig}"  # the completed dual signature

    def construct_external_envelope(self, plaintext_payload: Dict[str, Any],
                                    binding_ctx: Dict[str, Any]) -> Dict[str, Any]:
        """
        Bridge steps 4 & 5: minimal-disclosure wrap in the external wire format,
        attach hardware-rooted attestation, and sign with external-domain keys.
        """
        # Minimal disclosure: only what the operation named leaves; live operating
        # state, authority claims, policy config, and the audit trail are excluded.
        sanitized_body = {
            "task_input": plaintext_payload.get("task_input"),
            "scope_restriction_hash": binding_ctx["scope_hash"],
        }
        external_envelope = {
            "cryptographic_domain": "external",
            "sender": {
                "executor_instance_id": "EXE-01",
                # The more conservative post-quantum scheme (SLH-DSA) is an
                # EXTERNAL-domain algorithm-agility option, never internal.
                "signature_suite": "SLH-DSA-128f",
                "hardware_attestation_token": "FIPS-140-3-LEVEL-3-TOKEN",
            },
            "header": {
                "binding_reference": binding_ctx["binding_reference"],
                "output_ceiling_tokens": binding_ctx["output_ceiling_tokens"],
            },
            "body": sanitized_body,
            "signature": None,
        }
        external_envelope["signature"] = "EXT_SIG_" + hashlib.sha256(
            str(sanitized_body).encode()).hexdigest()
        return external_envelope


class BridgeOfTrustExecutor(abc.ABC):
    """Coordinates the five-step outbound bridge crossing between the isolated domains."""

    def __init__(self, internal_keys: Dict[str, Any], external_keys: Dict[str, Any]):
        self.internal_enclave = InternalEnclave(internal_keys)
        self.external_enclave = ExternalEnclave(external_keys)

    def outbound_bridge_crossing(self, orchestrator_directive: Dict[str, Any],
                                 binding_ctx: Dict[str, Any]) -> Dict[str, Any]:
        """The five-step outbound sequence; each step closes a specific gap the prior one leaves open."""
        try:
            # 1. Directive arrives from the Orchestrator path.
            # 2. Internal verification + the internal half of the handoff signature.
            verified_payload, internal_half_sig = \
                self.internal_enclave.verify_and_sign_handoff(orchestrator_directive)
            # 3. The bridge handoff: plaintext crosses; the external enclave
            #    counter-signs on receipt, completing the dual-signed record.
            dual_signed_record = self.external_enclave.countersign_handoff(
                verified_payload, internal_half_sig)
            _ = dual_signed_record  # witnessed at crossing time
            # 4 & 5. External envelope construction (attestation) + external signature + egress.
            return self.external_enclave.construct_external_envelope(verified_payload, binding_ctx)
        except Exception as exc:
            # Failure fails closed: quarantine + hand instance control to the Sovereign,
            # never a soft retry loop.
            self.trigger_emergency_quarantine_halt(reason=str(exc))
            raise

    @abc.abstractmethod
    def trigger_emergency_quarantine_halt(self, reason: str) -> None:
        """Suspend southbound dispatch and hand instance control to the Sovereign."""
        raise NotImplementedError
