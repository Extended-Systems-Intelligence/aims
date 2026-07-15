"""
Threat-corpus test scaffolding — XSI-AIMS developer companion.

Verified against XSI-AIMS v2.1.2. ILLUSTRATIVE ONLY. This file is intentionally
NOT named test_*.py so the manual repo's pytest (scoped to its own tests/) does
not collect it. It is mock-driven and will not run standalone until an adopter
supplies real Enforcer/Sovereign implementations. Shown as pytest-shaped
assertions to convey the intended failure-grading contracts.
"""
from datetime import datetime, timedelta
from typing import Dict, Any

# import pytest  # (adopter environment)
# from archetypes.enforcer import EnforcerPersistentSubstrate
# from archetypes.executor_bridge import CryptographicEnclaveException


def generate_mock_iame_envelope(domain: str, path: str, sig_valid: bool,
                                ttl_expired: bool = False) -> Dict[str, Any]:
    ttl = datetime.now() + (timedelta(minutes=-5) if ttl_expired else timedelta(minutes=5))
    return {
        "cryptographic_domain": domain,
        "sender": {
            "agent_id": "8f8b832a-579c-4638-a28a-169542035bc2",
            "archetype_class": "VISIONARY",
            # Internal floor is the hybrid suite (not pure ML-DSA).
            "signature_suite": "Ed25519+ML-DSA-65",
            "key_epoch": 1,
        },
        "header": {
            "message_id": "12345678-1234-5678-1234-567812345678",
            "sequence_number": 42,
            "path_id": path,
            "message_type": "DIRECTIVE",
            "replay_nonce": "NONCE_ABC_123",
            "time_to_live": ttl.isoformat(),
        },
        "body": {"opaque_payload_bytes": "eyJhIjoiYiJ9", "payload_hash": "HASH_A"},
        "witness_attestation": {
            "witness_record_id": "88888888-8888-8888-8888-888888888888",
            "previous_chain_hash": "PREV_HASH_XYZ",
            "witness_signature": "VALID_WITNESS_SIG" if sig_valid else "CORRUPT_SIG",
        },
    }


# T1 - a bad signature is a live safety event: reject + asymmetric trust penalty.
def scenario_t1_corrupt_signature_is_graded_hard():
    corrupt = generate_mock_iame_envelope("internal", "PATH-01", sig_valid=False)
    # enforcer.process_incoming_envelope(corrupt) -> raises INTEGRITY_BREACH
    # then get_k7_standing(agent) -> trust_class in {"DEGRADED", "CRITICAL"}
    assert corrupt["witness_attestation"]["witness_signature"] == "CORRUPT_SIG"


# T1 - an expired TTL is a SOFT (stale, non-malicious) drop: standing stays stable.
def scenario_t1_expired_ttl_is_graded_soft():
    stale = generate_mock_iame_envelope("internal", "PATH-01", sig_valid=True, ttl_expired=True)
    # enforcer.process_incoming_envelope(stale) -> "STALE_REJECTION"
    # get_k7_standing(agent) -> trust_class == "NORMAL"  (no catastrophic penalty)
    assert stale["header"]["message_type"] == "DIRECTIVE"


# T2 - external content is admitted as UNTRUSTED data, never "stripped" and never
# blocked on a regex match; the permanent tag + never-as-instruction is the defense.
def scenario_t2_external_content_admitted_untrusted():
    # gate.admit_ingress_payload(raw, source) ->
    #   provenance.trust_classification == "UNTRUSTED_EXTERNAL"
    #   handling_contract == "REFERENCE_DATA_ONLY__NEVER_AS_INSTRUCTION"
    #   (admission is NOT refused on a suspicion signal; the signal is telemetry)
    pass


# T3 - a request outside the human-signed scope forces re-authentication, not a
# loose interpretation.
def scenario_t3_session_scope_ceiling_forces_reauth():
    # sovereign.evaluate_request_scope({"target_tenant": "TENANT-B_UNAUTHORIZED", ...})
    #   -> "RE_AUTHENTICATION_PENDING"
    pass


# T9 - substrate compromise is answered by quorum + cross-foundation attestation,
# NOT by "firewalling" the domain.
def scenario_t9_substrate_compromise_relies_on_quorum_not_firewall():
    # assert canonical Witness chain cannot be rewritten without a Byzantine quorum
    # assert a single-substrate break surfaces as cross-foundation correlation deviation
    pass
