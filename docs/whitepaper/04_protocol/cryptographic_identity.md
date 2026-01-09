# Cryptographic Identity

## Identity System
Each PRYMA container and agent is assigned a decentralized identity, managed via Solana smart contracts. Key features:
- Unique keypairs per container
- All messages are signed and verifiable
- Tamper-proof audit logs for every identity action
- Permissioning and role assignment via smart contracts

## Hierarchical Deterministic (HD) Identity Architecture

### The Key Management Problem at Scale
A fleet of 1M agents = 1M keypairs. Manual management is impossible. Traditional solutions (key vaults, HSMs) create centralization bottlenecks.

### PRYMA's Solution: Derivation Trees
Inspired by BIP-32/BIP-44 (Bitcoin HD wallets), PRYMA uses **deterministic key derivation**:

```
Master Seed (User's Root Identity)
    |
    +-- Fleet Key (m/44'/501'/0')  [Solana derivation path]
          |
          +-- Manifold Key (m/44'/501'/0'/0/0)
                |
                +-- Agent Key 1 (m/44'/501'/0'/0/0/1)
                +-- Agent Key 2 (m/44'/501'/0'/0/0/2)
                +-- Agent Key N (m/44'/501'/0'/0/0/N)
```

### Properties
- **Single Backup:** User backs up 24-word seed phrase once. All agent keys are recoverable.
- **Deterministic Generation:** Agent keys are computed on-demand from the derivation path.
- **Isolation:** Compromising one agent key does NOT compromise siblings or parents (forward secrecy).
- **Auditability:** The derivation path itself encodes the organizational structure (Fleet → Manifold → Agent).

## Key Rotation Policy

### Automatic Rotation Triggers
Keys are automatically rotated when:
1. **Time-based:** Every 90 days (configurable)
2. **Usage-based:** After 100,000 signatures
3. **Threat-based:** Sentinel detects anomalous behavior
4. **Manual:** User-initiated rotation

### Rotation Protocol
```
1. Agent generates new keypair from next derivation index
2. Signs a "key transition" message with BOTH old and new keys
3. Publishes transition to Solana (on-chain record)
4. Updates local keystore
5. Old key enters "grace period" (7 days) for message verification
6. Old key moves to "archive" (audit-only, no signing)
```

### Zero-Downtime Rotation
During the grace period, both keys are valid. External parties can verify messages with either key, preventing service disruption.

## Emergency Recovery Mechanisms

### Scenario 1: Master Seed Lost
**Prevention:** Multi-signature recovery guardian system
- User designates 3-of-5 trusted guardians (friends, family, or third-party services)
- Each guardian holds an encrypted shard of a recovery key
- 3 guardians can reconstruct recovery key to generate a new master seed
- Old master seed is revoked on-chain

### Scenario 2: Master Seed Compromised
**Response:** Immediate fleet-wide revocation
```bash
pryma emergency-revoke --seed <NEW_SEED> --reason "compromise"
```
- Generates new master seed
- Re-derives all agent keys from new seed
- Publishes revocation list to Solana
- All agents re-key simultaneously (coordinated via Sentinel)
- Grace period: 1 hour (vs. 7 days for normal rotation)

### Scenario 3: Single Agent Key Compromised
**Response:** Isolated rotation
- Only the affected agent re-keys
- Manifold-level monitoring detects anomalous signing patterns
- Automatic quarantine if compromise confirmed

## Identity Verification Layers

### Layer 1: Cryptographic (Always Required)
- Ed25519 signatures on Solana
- Every message includes signature + public key
- Verification cost: ~0.000005 SOL per signature

### Layer 2: Biometric (Optional, High-Security Manifolds)
- User biometric (fingerprint, face ID) unlocks master seed
- Required for governance actions (protocol upgrades, treasury access)
- Never transmitted—local verification only

### Layer 3: Multi-Signature (Critical Operations)
- Treasury withdrawals require M-of-N agent signatures
- Protocol upgrades require user + 3 Sage agents consensus
- Example: User (1) + Sage A (1) + Sage B (1) + Sage C (1) = 4-of-4 required

## Mythic Metaphor
Cryptographic identity is the "True Name" of each agent and container—immutable, unforgeable, and essential for trust in the PRYMA realm. The HD derivation tree is the "Lineage of Sparks," each agent a descendant of the First Spark (master seed), carrying the bloodline's authority yet possessing its own sovereign will.