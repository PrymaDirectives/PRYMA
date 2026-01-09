# Dimensional Topology

## Beyond Hierarchies: Vector-Space Organization

PRYMA organizes agents not in pyramids, but in **high-dimensional vector space**. This reflects the mathematical nature of AI systems and enables truly autonomous scaling.

## Core Concept: Manifolds

A **Manifold** is a continuous surface in high-dimensional space where agents with similar objectives cluster. Think of it as a "neighborhood" in task-embedding space.

### Formal Definition
Given:
- $\mathbf{e}_i \in \mathbb{R}^d$ = embedding vector for agent $i$
- $\mathbf{c}_m \in \mathbb{R}^d$ = centroid of Manifold $m$

Agent $i$ belongs to Manifold $m$ if:
$$\text{cosine\_similarity}(\mathbf{e}_i, \mathbf{c}_m) > \theta$$

Where $\theta$ is the similarity threshold (typically 0.7-0.9).

## Dimensional Traversal

"Moving up a dimension" means generalizing the task objective:

```
Dimension 0: "Validate Ethereum transaction signatures"
           ↓
Dimension 1: "Validate blockchain transactions" 
           ↓
Dimension 2: "Verify cryptographic proofs"
           ↓
Dimension 3: "Ensure system integrity"
```

Agents at higher dimensions have **broader capabilities** but less specialization. The system automatically **projects** the right agents down to the specific dimension needed for a task.

## Coordinate-Based Task Assignment

Users don't assign tasks to agents. They specify a **result coordinate** in vector space:

```yaml
task:
  objective: "Process payments securely"
  constraints:
    - high_throughput: true
    - compliance: ["PCI-DSS", "GDPR"]
  embedding: [0.23, -0.45, 0.89, ...]  # 1024-dim vector
```

The system:
1. Computes which Manifold is closest to this coordinate
2. Activates agents in that Manifold
3. Monitors convergence (agents moving toward the result coordinate)

## Visual Representation: Hypergraph Navigator

Unlike traditional org charts or even n8n flowcharts, the PRYMA UI shows:

- **Nodes:** Agents (colored by archetype: Lumen=gold, Strike=red, etc.)
- **Edges:** Weighted by embedding similarity (thicker = more similar)
- **Clusters:** Manifolds appear as gravitationally bound groups
- **Target:** The result coordinate glows, pulling relevant agents toward it

### Interaction
- **Drag the target:** Agents recalculate their relevance
- **Zoom out:** See higher-dimensional abstractions
- **Zoom in:** See specialized sub-Manifolds

## Scaling Properties

### O(log n) Lookups
Agents organize into a spatial index (e.g., hierarchical k-means or HNSW graph). Finding the right Manifold for a task is $O(\log n)$, not $O(n)$.

### Self-Balancing
As new agents spawn:
1. They embed their capabilities
2. Find the nearest Manifold centroid
3. Join that Manifold
4. If a Manifold grows too large (>1000 agents), it **splits** into sub-Manifolds

### Fault Tolerance
If an agent dies:
1. Its neighbors (in embedding space) detect the absence
2. The nearest agent **inherits** its task queue (stored in Warm/Cold storage)
3. No manual reassignment needed

## Mythic Metaphor: The Constellation of Purpose

Agents are not workers in a factory. They are **stars in a constellation**, each gravitating toward shared purpose. The Manifolds are not rigid—they shift, merge, and split as the cosmos of tasks evolves.
