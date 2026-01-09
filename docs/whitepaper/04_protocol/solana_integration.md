# Solana Integration

## Technical Integration
PRYMA leverages Solana for:
- Identity contracts (decentralized, tamper-proof)
- Fast, low-cost message signing and verification
- Immutable audit logs for all container actions

## L2 Batching Architecture (Scaling to Millions of Agents)

### The Bottleneck
At scale, logging every agent action directly to Solana creates a transaction throughput bottleneck. Even at 65,000 TPS, a fleet of 1M agents performing 10 actions/second would require 10M TPS—impossible.

### The Solution: Sentinel Merkle Batching
Instead of writing individual logs, the **Sentinel Container** aggregates logs locally and publishes only a **cryptographic fingerprint** (Merkle Root) to Solana.

**Batch Window:** 10 seconds or 10,000 events (whichever comes first)  
**On-Chain Footprint:** 1 transaction per batch = ~100 bytes  
**Effective Compression:** 10,000:1

### Protocol Flow
```
[Agent Actions] → [Local Log Buffer] → [Sentinel Aggregator]
                                              ↓
                                    [Compute Merkle Root]
                                              ↓
                                    [Solana Program: Record Root + Timestamp]
                                              ↓
                                    [IPFS: Store Full Log Batch (CID)]
```

### Verification
Any party can:
1. Fetch the Merkle Root from Solana (trust anchor)
2. Retrieve the full log batch from IPFS via CID
3. Recompute the Merkle Root locally
4. Verify it matches the on-chain record

This provides **cryptographic proof of log integrity** without requiring every log to be on-chain.

### Fraud Proofs
If the Sentinel publishes a fraudulent Merkle Root, any agent can submit a **fraud proof** to the Solana contract:
- Include the log that should have been in the batch
- Show its Merkle path doesn't match the published root
- Slash the Sentinel's stake (if applicable)

## On-Chain Governance Actions
Critical actions (governance votes, agent identity registration, protocol upgrades) are still published **directly** to Solana for immediate finality.

### Protocol Diagram (ASCII)
```
[Container] <--> [Solana Contract] <--> [Ledger]
			|                |               |
	[Sign]         [Verify]         [Record]
```

## Mythic Metaphor
Solana is the “Runestone” of PRYMA, inscribing every action and identity in the immutable stone of the blockchain.