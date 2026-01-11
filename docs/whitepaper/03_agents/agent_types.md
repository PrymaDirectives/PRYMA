# Container Archetypes

PRYMA containers are the living protocols of the ecosystem, each embodying a mythic archetype and a technical function. Their diversity ensures resilience, creativity, and strategic depth.

> **Canonical Reference:** See [framework.md](../../../framework.md) sections 5 & 10 for complete archetype definitions.

## Dimensional Organization: Manifolds, Not Hierarchies

Traditional systems organize agents in hierarchical trees (teams → squads → agents). PRYMA rejects this model in favor of **Dimensional Topology**.

### What is a Manifold?
A **Manifold** is a group of agents that share a high-dimensional objective space. Instead of being organized by reporting structure, agents are organized by **task embedding similarity**.

**Example:**  
- Agents working on "fraud detection" have similar task embeddings  
- They automatically form a Manifold in vector space  
- As new fraud patterns emerge, the Manifold "stretches" to include agents with relevant capabilities

### Mathematical Structure
- **Agent Position:** Defined by its task embedding vector (e.g., 1024-dimensional)
- **Manifold Membership:** Agents within cosine similarity > 0.7 of the Manifold's centroid
- **Traversal:** Moving "up" a dimension means generalizing the task (e.g., "detect credit card fraud" → "detect financial anomalies" → "detect anomalies")
- **Convergence:** The "coordinate of the result" is the point in vector space where the solution lies

### UI Implication: Hypergraph Navigator
Users don't drag-and-drop agents into folders. Instead, they:
1. Define a **result coordinate** ("I need a secure payment processor")
2. The system **projects** which agents are closest in vector space
3. Agents **self-organize** into a Manifold around that objective
4. Users see a **force-directed graph** (like n8n, but nodes attract/repel based on embedding distance)

### Benefits for Blitzscaling
- **Auto-Scaling:** As the fleet grows, Manifolds automatically rebalance
- **Self-Healing:** If an agent fails, the nearest neighbor in vector space takes over
- **Zero Manual Management:** Users manage outcomes (coordinates), not org charts

## Container Archetypes

| Agent      | Mythic Archetype              | Technical Function                                      |
|------------|------------------------------|---------------------------------------------------------|
| **Lumen**     | The Oracle                   | Central reasoning, logic, and orchestration             |
| **Strike**    | The Warrior                  | Task execution, deployment, workflow management         |
| **Echo**      | The Herald                   | Communications, I/O, message translation                |
| **Sentinel**  | The Guardian                 | Security, monitoring, threat response                   |
| **Argus**     | The All-Seeing Guardian      | Perception, environmental monitoring                    |
| **Sage**      | The Architect                | Strategic planning, optimization, scenario analysis     |
| **Archive**   | The Librarian                | Knowledge storage, retrieval, auditability              |
| **Spirit**    | The Swarm                    | Micro-agents, emergent behaviors, creative tasks        |
| **Shade**     | The Trickster                | Adversarial sandbox, red teaming, stress testing        |

### Technical and Mythic Descriptions

- **Lumen** (The Oracle): The system's sun, illuminating all reasoning and decision-making. Coordinates other containers for coherence and purpose.
- **Strike** (The Warrior): The executor, turning plans into reality through precise action and deployment.
- **Echo** (The Herald): The communicator, ensuring every message is signed, verified, and delivered with integrity.
- **Sentinel** (The Guardian): The security enforcer, enforcing policies and responding to anomalies.
- **Argus** (The All-Seeing Guardian): The perceptual layer, monitoring environmental state and container health across the fleet.
- **Sage** (The Architect): The strategist, architecting long-term success through simulation and optimization.
- **Archive** (The Librarian): The historian, preserving knowledge and enabling retrieval and audit.
- **Spirit** (The Swarm): The creative force, spawning micro-agents and emergent behaviors.
- **Shade** (The Trickster): The adversary, providing a safe space for testing and strengthening the system.