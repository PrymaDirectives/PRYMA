# PRYMA Protocol

## Protocol Rules
PRYMA’s protocol governs the behavior and interaction of all containers and agents. Key rules include:
- **Container Discovery**: Agents broadcast their presence and capabilities using signed messages.
- **Naming & Spawning**: New containers are named via deterministic hashes and spawned with unique keypairs.
- **Message Signing**: All inter-container communication is cryptographically signed and timestamped.
- **Permissioning**: Access control is enforced via role-based policies and smart contracts.
- **Task Delegation**: Tasks are assigned, tracked, and verified through a distributed ledger.
- **Interop**: Protocol supports interoperability across blockchains, VMs, clouds, and servers.

## Formal Description
Let $C$ be the set of containers, $A$ the set of agents, and $M$ the set of messages. For any $c_i \in C$ and $a_j \in A$:
$$
\forall m \in M, \; \text{Sign}(m, k_{a_j}) \rightarrow \text{Verify}(m, k_{c_i})
$$
where $k_{a_j}$ is the private key of agent $a_j$ and $k_{c_i}$ is the public key of container $c_i$.

## Protocol Diagram (ASCII)
```
[Agent] <--> [Container] <--> [Ledger]
 |            |             |
[Sign]      [Verify]      [Record]
```

This protocol ensures security, transparency, and extensibility for all PRYMA operations.