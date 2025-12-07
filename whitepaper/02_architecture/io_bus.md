# I/O Bus

The PRYMA I/O Bus is the universal communication backbone connecting all containers, agents, and external systems within the ecosystem. It functions as both a message broker and a semantic router, ensuring that every communication is secure, ordered, and verifiable.

## Core Principles
- Natural-language bus for container communication
- Universal schema for messages
- Message signing and replay protection
- Asynchronous, event-driven architecture
- Publish-subscribe and request-response patterns

---

## I/O Bus Architecture

The I/O Bus operates as a distributed message fabric with the following architectural layers:

### 1. Transport Layer

The Transport Layer handles the physical delivery of messages between containers:

- **Message Queue**: Asynchronous FIFO queues for each container pair
- **Routing Table**: Dynamic routing based on container IDs and message types
- **Load Balancing**: Distribution of messages across multiple container instances
- **Priority Lanes**: Express channels for critical system messages
- **Dead Letter Queue**: Handling of undeliverable or rejected messages

```
┌──────────┐    Queue    ┌──────────┐    Queue    ┌──────────┐
│Container │────────────>│ I/O Bus  │────────────>│Container │
│    A     │<────────────│  Fabric  │<────────────│    B     │
└──────────┘             └──────────┘             └──────────┘
```

### 2. Protocol Layer

The Protocol Layer enforces message structure and semantics:

- **Universal Schema**: YAML/JSON schema validation for all messages
- **Version Management**: Backward-compatible protocol evolution
- **Type System**: Strongly-typed message contracts
- **Serialization**: Efficient binary encoding (Protocol Buffers, MessagePack)
- **Compression**: Optional payload compression for large data transfers

### 3. Security Layer

The Security Layer provides cryptographic guarantees:

- **Message Signing**: Ed25519 signatures on every message
- **Verification**: Public key infrastructure for sender authentication
- **Replay Protection**: Nonce-based prevention of message replay attacks
- **Encryption**: Optional E2E encryption for sensitive payloads
- **Audit Trail**: Immutable logs of all message transactions

### 4. Semantic Layer

The Semantic Layer adds intelligence to message routing:

- **Intent Classification**: Automatic categorization of message purpose
- **Context Awareness**: Maintains conversation state and history
- **Semantic Routing**: Routes messages based on content, not just addressing
- **Translation**: Automatic format conversion between container protocols
- **Embedding Index**: Vector search for related messages and patterns

---

## Protocol Diagrams

### Complete I/O Bus Stack

```
┌─────────────────────────────────────────────────────────────────┐
│                        Application Layer                         │
│               [Containers] [Agents] [External APIs]              │
└────────────────────────────────┬────────────────────────────────┘
                                 │
┌────────────────────────────────▼────────────────────────────────┐
│                         Semantic Layer                           │
│    [Intent Classifier] [Context Manager] [Semantic Router]      │
└────────────────────────────────┬────────────────────────────────┘
                                 │
┌────────────────────────────────▼────────────────────────────────┐
│                         Security Layer                           │
│        [Signer] [Verifier] [Replay Guard] [Audit Logger]        │
└────────────────────────────────┬────────────────────────────────┘
                                 │
┌────────────────────────────────▼────────────────────────────────┐
│                         Protocol Layer                           │
│    [Schema Validator] [Serializer] [Versioner] [Compressor]     │
└────────────────────────────────┬────────────────────────────────┘
                                 │
┌────────────────────────────────▼────────────────────────────────┐
│                         Transport Layer                          │
│     [Queue Manager] [Router] [Load Balancer] [DLQ Handler]      │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                         [Network Fabric]
```

### Message Flow with Security

```
[Sender Container]
        │
        ├─ 1. Create Message
        ├─ 2. Sign with Private Key
        ├─ 3. Add Nonce (replay protection)
        ├─ 4. Serialize to Binary
        ▼
   [I/O Bus Ingress]
        │
        ├─ 5. Validate Schema
        ├─ 6. Verify Signature
        ├─ 7. Check Nonce Uniqueness
        ├─ 8. Route to Destination
        ▼
   [Message Queue]
        │
        ├─ 9. Persist Message
        ├─ 10. Await Delivery Confirmation
        ▼
   [I/O Bus Egress]
        │
        ├─ 11. Deserialize Message
        ├─ 12. Verify Integrity
        ├─ 13. Update Audit Log
        ▼
[Receiver Container]
        │
        ├─ 14. Process Message
        ├─ 15. Send Acknowledgment
        └─ 16. Optional Response Message
```

### Pub-Sub vs Request-Response Patterns

```
Publish-Subscribe Pattern:
┌──────────┐                  ┌──────────┐
│Publisher │──topic:events───>│ I/O Bus  │
└──────────┘                  └────┬─────┘
                                   │ (broadcast)
                     ┌─────────────┼─────────────┐
                     ▼             ▼             ▼
                ┌────────┐    ┌────────┐    ┌────────┐
                │Subscriber│  │Subscriber│  │Subscriber│
                │    A    │    │    B    │    │    C    │
                └────────┘    └────────┘    └────────┘

Request-Response Pattern:
┌──────────┐    request      ┌──────────┐
│Requester │───────────────>│ I/O Bus  │
│          │                  └────┬─────┘
│          │                       │
│          │                       ▼
│          │                  ┌──────────┐
│          │                  │Responder │
│          │                  │          │
│          │                  └────┬─────┘
│          │                       │
│          │    ┌──────────────────┘
│          │<───┘ response
└──────────┘
```

### Multi-Container Orchestration

```
                           [I/O Bus]
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
         ┌────────┐      ┌────────┐      ┌────────┐
         │ Lumen  │      │ Strike │      │  Echo  │
         │(Reason)│      │(Execute)│     │(Comm)  │
         └───┬────┘      └───┬────┘      └───┬────┘
             │               │                │
             └───────┬───────┴───────┬────────┘
                     │               │
                     ▼               ▼
                ┌────────┐      ┌────────┐
                │Sentinel│      │Archive │
                │(Guard) │      │(Memory)│
                └────────┘      └────────┘
                     │               │
                     └───────┬───────┘
                             │
                             ▼
                        [Solana]
```

---

## Universal Message Schema

All messages on the I/O Bus conform to the following universal schema:

```yaml
pryma_message:
  # Core Identification
  id: <uuid>
  version: "1.0.0"
  timestamp: <iso8601>
  
  # Routing
  sender: <container_id>
  receiver: <container_id | "broadcast" | topic_name>
  reply_to: <message_id | null>
  
  # Content
  type: <message_type>  # command, query, event, response
  payload:
    data: <any>
    format: <mime_type>
    size: <bytes>
  
  # Semantics
  intent: <string>
  priority: <int: 0-10>
  ttl: <seconds>
  
  # Security
  signature: <hex>
  public_key: <hex>
  nonce: <uuid>
  encryption: <algorithm | null>
  
  # Context
  context_id: <session_uuid>
  causal_order: <int>
  embedding_ref: <vector_id>
  
  # Metadata
  metadata:
    language: <iso639>
    tags: [<string>]
    attachments: [<urls>]
```

---

## Message Signing and Replay Protection

### Signature Process

Every message is cryptographically signed before transmission:

```
1. Canonical Message Construction:
   canonical_msg = {id, timestamp, sender, receiver, payload, nonce}

2. Hash Generation:
   hash = SHA3-256(canonical_msg)

3. Signature Creation:
   signature = Ed25519.sign(hash, sender.private_key)

4. Verification (by receiver):
   verified = Ed25519.verify(signature, hash, sender.public_key)
```

### Replay Protection

Messages cannot be replayed or reused due to multiple safeguards:

- **Unique Nonce**: Every message includes a UUID that can only be used once
- **Nonce Registry**: The I/O Bus maintains a distributed registry of used nonces
- **Time Windows**: Messages older than TTL are automatically rejected
- **Causal Ordering**: Sequence numbers prevent out-of-order replay
- **State Tracking**: Container state changes invalidate old messages

```
Replay Attack Prevention:
┌──────────┐    msg(nonce=X)    ┌──────────┐
│Attacker  │───────────────────>│ I/O Bus  │
└──────────┘                     └────┬─────┘
                                      │
                                 [Check Nonce]
                                      │
                            ┌─────────┴─────────┐
                            ▼                   ▼
                     [Nonce in DB]         [Nonce New]
                            │                   │
                       [REJECT]            [ACCEPT]
                                           [Add to DB]
```

---

## Performance Characteristics

The I/O Bus is designed for high throughput and low latency:

- **Throughput**: 100,000+ messages/second per bus instance
- **Latency**: <1ms for intra-node, <10ms for inter-node
- **Scalability**: Horizontal scaling via sharding and partitioning
- **Reliability**: At-least-once delivery with optional exactly-once semantics
- **Availability**: 99.99% uptime with automatic failover

---

## Mythic Metaphor

The I/O Bus is the "Nervous System" of PRYMA—a living network of pathways that connect every thought, action, and memory. Like the cosmic web that connects all stars, the I/O Bus ensures that no container is an island. Messages flow like lifeblood through its channels, carrying intent, data, and wisdom to their destined recipients.

It is both infrastructure and intelligence: a highway for data and a guardian of truth. Through its cryptographic vigilance and semantic awareness, the I/O Bus embodies the principle that communication must be not only fast, but trustworthy—not only efficient, but meaningful.

The I/O Bus is the thread that weaves the tapestry of PRYMA's distributed consciousness.