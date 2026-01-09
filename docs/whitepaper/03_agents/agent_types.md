# Agent Types

PRYMA agents are the living protocols of the ecosystem, each embodying a mythic archetype and a technical function. Their diversity ensures resilience, creativity, and strategic depth.

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

## Agent Archetypes

| Agent      | Mythic Archetype         | Technical Function                                      |
|------------|-------------------------|---------------------------------------------------------|
| **Lumen**     | The Light-Bringer        | Central reasoning, logic, and orchestration             |
| **Strike**    | The Hand of Action      | Task execution, deployment, workflow management         |
| **Echo**      | The Voice               | Communications, I/O, message translation                |
| **Sentinel**  | The Shield              | Security, monitoring, threat response                   |
| **Sage**      | The Mind                | Strategic planning, optimization, scenario analysis     |
| **Archive**   | The Memory              | Knowledge storage, retrieval, auditability              |
| **Spirit**    | The Spark Within        | Micro-agents, emergent behaviors, creative tasks        |
| **Shade**     | The Shadow              | Adversarial sandbox, red teaming, stress testing        |

### Technical and Mythic Descriptions

- **Lumen**: The system’s sun, illuminating all reasoning and decision-making. Coordinates other agents for coherence and purpose.
- **Strike**: The executor, turning plans into reality through precise action and deployment.
- **Echo**: The communicator, ensuring every message is signed, verified, and delivered with integrity.
- **Sentinel**: The guardian, enforcing security policies and responding to anomalies.
- **Sage**: The strategist, architecting long-term success through simulation and optimization.
- **Archive**: The historian, preserving knowledge and enabling retrieval and audit.
- **Spirit**: The creative force, spawning micro-agents and emergent behaviors.
- **Shade**: The adversary, providing a safe space for testing and strengthening the system.