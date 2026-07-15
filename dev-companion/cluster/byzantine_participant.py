"""
Cluster Mode Byzantine participant scaffolding — XSI-AIMS developer companion.

Verified against XSI-AIMS v2.1.2. Illustrative scaffolding, not production code.

Cluster Mode presents many physical nodes under one operator as a single logical
deployment with one canonical Witness chain, replicated by Byzantine-tolerant
consensus (PBFT, HotStuff, BFT-SMaRt, or Tendermint in Byzantine mode). Crash-
fault-only protocols such as Raft are forbidden: a compromised node can lie, not
just go silent, and only a Byzantine-tolerant protocol keeps a replicated ledger
correct when a participant is actively malicious.
"""
import abc
import hashlib
from typing import Dict, Any, List, Set


class ClusterConsensusError(Exception):
    """Raised on attestation failure or a sub-quorum commit attempt."""


class NodeIdentity:
    def __init__(self, node_id: str, hardware_attestation_token: str):
        self.node_id = node_id
        self.attestation_token = hardware_attestation_token


def byzantine_quorum_size(n: int) -> int:
    """
    A Byzantine-tolerant quorum for n nodes: with f = floor((n-1)/3) tolerated
    faults, the commit quorum is 2f + 1.

    Degenerate cases the spec names openly:
      * n = 2  -> f = 0, quorum = 1. NOT Byzantine-tolerant in any meaningful
                  sense (a quorum of two cannot outvote one lying member). The
                  spec permits `cluster_mode: true, quorum=2` only as an honestly
                  labeled degenerate mode for an SMB that wants the availability/
                  migration machinery without genuine BFT.
      * n = 3  -> f = 0. Simple consensus; tolerates no Byzantine fault.
      * n >= 4 -> f >= 1. Genuine Byzantine tolerance begins here.
    """
    f = (n - 1) // 3
    return 2 * f + 1


class ByzantineClusterParticipant(abc.ABC):
    def __init__(self, node_id: str, cluster_nodes: Set[str]):
        self.node_id = node_id
        self.peers = set(cluster_nodes)
        self.is_active = False
        self.local_chain_replica: List[Dict[str, Any]] = []

    @property
    def quorum_threshold(self) -> int:
        return byzantine_quorum_size(len(self.peers))

    def bootstrap_node(self, target_node: NodeIdentity) -> bool:
        """
        Hardware-rooted bootstrap: a node clears attestation, verified by the
        existing quorum, BEFORE it replicates the canonical chain and is admitted
        into consensus. A node that leaves gracefully migrates its user-pairs
        atomically, seals its chain segment, and exits quorum cleanly.
        """
        if not self._verify_hardware_enclave_signature(target_node.attestation_token):
            raise ClusterConsensusError(
                f"Bootstrap aborted: node {target_node.node_id} failed hardware attestation.")
        self._sync_canonical_chain_to(target_node.node_id)
        self.peers.add(target_node.node_id)
        return True

    def propose_block_commit(self, proposed_transaction: Dict[str, Any],
                             validator_signatures: List[str]) -> bool:
        """
        Append-only commit into the canonical Witness chain, gated on a Byzantine
        quorum. A single compromised node or sub-quorum cannot commit — an
        attacker must compromise a quorum, which is far noisier than one box.
        """
        if len(set(validator_signatures)) < self.quorum_threshold:
            return False
        prev_hash = self.local_chain_replica[-1]["current_hash"] if self.local_chain_replica else "GENESIS"
        block_entry = {
            "index": len(self.local_chain_replica),
            "payload": proposed_transaction,
            "previous_hash": prev_hash,
            "signatures": sorted(set(validator_signatures)),
            "current_hash": None,
        }
        block_entry["current_hash"] = hashlib.sha256(str(block_entry).encode()).hexdigest()
        self.local_chain_replica.append(block_entry)
        return True

    @abc.abstractmethod
    def _verify_hardware_enclave_signature(self, token: str) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def _sync_canonical_chain_to(self, target_id: str) -> None:
        raise NotImplementedError
