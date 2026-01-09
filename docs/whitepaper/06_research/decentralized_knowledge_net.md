# Decentralized Knowledge Net

## System Design
PRYMA's knowledge net is a distributed, resilient system for storing, sharing, and synchronizing information across all agents and containers. At scale (millions of agents), this requires a **three-tier storage topology** that balances speed, cost, and permanence.

## The Storage Triad

### 1. Hot State (Agent-Local Vector Memory)
**Technology:** Embedded vector databases (Qdrant, Weaviate, or custom WASM-based stores)  
**Purpose:** Immediate working memory for each agent container  
**Scope:** 
- Current task context (active embeddings)
- Real-time sensor data and environment state
- Frequently accessed knowledge fragments

**Characteristics:**
- Sub-millisecond latency
- Lives in container RAM/disk
- Ephemeral (can be reconstructed from Warm/Cold layers)
- Size: ~100MB-10GB per container

### 2. Warm Context (Fleet-Shared Immutable Storage)
**Technology:** IPFS (content-addressed) + Arweave (permanent archive)  
**Purpose:** Shared knowledge, model weights, and cryptographic audit trails  
**Scope:**
- Pre-trained model snapshots
- Signed audit logs (batch fingerprints)
- Historical decision trees and reasoning chains
- Inter-agent shared memories

**Characteristics:**
- Content-addressed (CID-based retrieval)
- Immutable once written
- Replicated across IPFS fleet nodes
- Arweave for permanent archival (pay-once, store-forever)
- Latency: ~100ms-1s

### 3. Cold Memory (Distributed Hash Table Sharding)
**Technology:** Kademlia-style DHT (similar to BitTorrent/IPFS routing layer)  
**Purpose:** Long-term distributed memory across the entire fleet  
**Scope:**
- Inactive agent memories (agents can "hibernate" and store state in DHT)
- Historical embeddings and learned patterns
- Compressed archives of past reasoning sessions

**Characteristics:**
- Each agent stores shards of other agents' memories (redundancy via erasure coding)
- Retrieval via DHT lookup (O(log n) hops)
- Lazy reconstruction (fetch only when needed)
- Latency: ~1-10s

## Scaling Properties
- **Write Path:** Agent → Hot (local) → Async batch to Warm (IPFS) → Periodic migration to Cold (DHT)
- **Read Path:** Check Hot → Check Warm (CID cache) → Query Cold (DHT lookup)
- **Failure Recovery:** If a container dies, its Hot state is lost but can be reconstructed from Warm + Cold within minutes.

### Features
- **Distributed Embeddings**: Knowledge is encoded as high-dimensional vectors, enabling advanced search and reasoning.
- **Resilient Storage**: Data is replicated and encrypted across the fleet, ensuring availability and privacy.
- **Consensus Graphs**: Agents reach agreement on facts, strategies, and updates via graph-based consensus protocols.

## Mythic Metaphor
The knowledge net is the “Web of Fate”—an ever-expanding tapestry where every thread is a piece of wisdom, and every node is a guardian of truth.