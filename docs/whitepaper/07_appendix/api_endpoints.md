# API Endpoints & Developer Onboarding

## Core API Endpoints

### Agent Lifecycle
- `POST /api/v1/agent/spawn` — Create a new agent or container
- `GET /api/v1/agent/{id}` — Get agent status and metadata
- `DELETE /api/v1/agent/{id}` — Terminate an agent
- `PATCH /api/v1/agent/{id}/config` — Update agent configuration

### Manifold Management
- `POST /api/v1/manifold/create` — Create a new Manifold with objective embedding
- `GET /api/v1/manifold/{id}/agents` — List agents in a Manifold
- `POST /api/v1/manifold/{id}/coordinate` — Update target coordinate (task objective)

### Communication & Logs
- `POST /api/v1/message/send` — Send message between agents
- `GET /api/v1/log/{agent_id}` — Retrieve audit logs (includes Merkle proof)
- `GET /api/v1/log/batch/{merkle_root}` — Retrieve full log batch from IPFS

### Execution & Tasks
- `POST /api/v1/task/exec` — Execute tasks or workflows
- `GET /api/v1/task/{id}/status` — Check task execution status
- `POST /api/v1/task/{id}/cancel` — Cancel running task

### System Health
- `GET /api/v1/status` — Get system health and metrics
- `GET /api/v1/metrics/manifold/{id}` — Get Manifold-level metrics
- `GET /api/v1/network/peers` — List connected compute providers

### Protocol Governance
- `POST /api/v1/governance/propose` — Submit a governance proposal
- `POST /api/v1/governance/vote` — Vote on active proposals
- `GET /api/v1/governance/proposals` — List all proposals

### Marketplace
- `GET /api/v1/marketplace/compute/offers` — List available compute providers
- `POST /api/v1/marketplace/compute/bid` — Bid for compute resources
- `GET /api/v1/marketplace/services` — Browse agent services for sale

## CLI Examples
```bash
# Initialize PRYMA environment
pryma init --network mainnet

# Spawn agents
pryma agent spawn lumen --manifold "fraud-detection"
pryma agent spawn strike --manifold "fraud-detection" --count 5

# Create Manifold from template
pryma manifold create --template "customer-support" --scale 100

# Link agents
pryma link strike-001 lumen-001 --relation "reports_to"

# Retrieve logs with verification
pryma log watch sentinel-001 --verify-merkle

# Execute task
pryma task exec task.yaml --async

# Check fleet status
pryma status --manifold "fraud-detection"

# Governance
pryma governance propose --title "Increase Sentinel stake" --ipfs QmXxx
pryma governance vote 42 --choice "yes" --prym 1000

# Protocol upgrades
pryma update --protocol --version 2.1.0
```

---

## SDK Architecture

### Supported Languages
- **TypeScript/JavaScript** (Primary)
- **Python** (Primary)
- **Rust** (Advanced/Performance)
- **Go** (Enterprise/Infrastructure)

### SDK Structure

#### TypeScript SDK Example
```typescript
import { PrymaClient, AgentType, Manifold } from '@pryma/sdk';

// Initialize client
const client = new PrymaClient({
  network: 'mainnet',
  masterSeed: process.env.PRYMA_MASTER_SEED,
  rpcEndpoint: 'https://api.mainnet.pryma.io'
});

// Spawn a Manifold from template
const manifold = await client.manifold.create({
  template: 'fraud-detection',
  objective: 'Detect credit card fraud in real-time',
  scale: {
    minAgents: 10,
    maxAgents: 1000,
    autoScale: true
  },
  compute: {
    gpu: 'T4',
    maxCostPerDay: 100 // PRYM
  }
});

// Spawn individual agents
const lumen = await manifold.spawnAgent({
  type: AgentType.Lumen,
  config: {
    model: 'gpt-4',
    temperature: 0.7
  }
});

// Send task to Manifold
const result = await manifold.executeTask({
  input: {
    transactions: [...],
    threshold: 0.95
  },
  timeout: 30000 // ms
});

console.log('Fraud detected:', result.fraudulent);

// Monitor logs with auto-verification
manifold.logs.stream({
  verifyMerkle: true,
  onLog: (log) => console.log(log),
  onFraud: (proof) => console.error('Fraud proof detected!', proof)
});
```

#### Python SDK Example
```python
from pryma import PrymaClient, AgentType

# Initialize
client = PrymaClient(
    network='mainnet',
    master_seed=os.getenv('PRYMA_MASTER_SEED')
)

# Create Manifold
manifold = client.manifold.create(
    template='content-moderation',
    objective='Flag inappropriate content',
    scale={'min_agents': 5, 'max_agents': 500}
)

# Spawn agents
for i in range(10):
    manifold.spawn_agent(AgentType.SENTINEL)

# Execute batch task
results = manifold.execute_batch([
    {'text': 'Check this content...'},
    {'text': 'And this one...'}
])

for result in results:
    if result.flagged:
        print(f"Flagged: {result.reason}")
```

---

## Developer Onboarding: The First 5 Minutes

### Quick Start (Zero to Fleet)

**1. Install CLI (One Command)**
```bash
curl -fsSL https://install.pryma.tech | sh
```

**2. Create Account & Fund Wallet**
```bash
pryma auth signup --email you@example.com
# Follow link to verify email
# Receive 10 PRYM airdrop for testing
```

**3. Deploy Your First Fleet (Template-Based)**
```bash
pryma quickstart --template "chatbot" --name "my-first-bot"
```

This command:
- Generates master seed (encrypted with password)
- Spawns a pre-configured Manifold (1 Lumen, 3 Echo, 1 Sentinel)
- Deploys to testnet
- Opens web dashboard at `http://localhost:3000`

**4. Interact via Web UI**
- Navigate to dashboard
- See Hypergraph Navigator (agents as nodes in 3D space)
- Drag "result coordinate" to set objective
- Watch agents self-organize in real-time

**5. Customize & Scale**
```bash
# Edit config
pryma config edit my-first-bot

# Scale up
pryma scale my-first-bot --agents 100

# Deploy to mainnet
pryma deploy my-first-bot --network mainnet --fund 50-PRYM
```

---

## Template Marketplace

### Pre-Built Manifold Templates

| Template | Description | Base Agents | Use Case |
|----------|-------------|-------------|----------|
| **chatbot** | Customer service bot | 1 Lumen, 3 Echo, 1 Sentinel | Support automation |
| **fraud-detection** | Real-time fraud analysis | 1 Sage, 5 Sentinel, 10 Spirit | Fintech security |
| **content-moderation** | Multi-platform moderation | 10 Sentinel, 2 Archive | Social media |
| **trading-desk** | Autonomous trading fleet | 1 Sage, 5 Lumen, 10 Strike, 1 Shade | Algo trading |
| **research-swarm** | Distributed research agents | 5 Sage, 10 Archive, 20 Spirit | Academia/R&D |
| **data-pipeline** | ETL and data processing | 10 Strike, 2 Archive, 1 Sentinel | Data engineering |

### Template Anatomy
```yaml
# templates/fraud-detection.yaml
name: "fraud-detection"
version: "1.0.0"
author: "PRYMA Core"
license: "MIT"

manifold:
  objective: "Detect fraudulent transactions in real-time"
  embedding_model: "text-embedding-ada-002"

agents:
  - type: Sage
    count: 1
    config:
      model: "gpt-4"
      role: "Oversee fraud detection strategy"
  
  - type: Sentinel
    count: 5
    config:
      model: "distilbert-base"
      role: "Monitor transaction patterns"
      alert_threshold: 0.95
  
  - type: Spirit
    count: 10
    config:
      model: "gpt-3.5-turbo"
      role: "Analyze individual transactions"

compute:
  gpu: "T4"
  max_cost: 50 # PRYM per day

scaling:
  min_agents: 16
  max_agents: 1000
  auto_scale: true
  scale_metric: "queue_depth"
  scale_threshold: 100

monitoring:
  dashboard: true
  alerts:
    - type: "slack"
      webhook: "${SLACK_WEBHOOK}"
    - type: "email"
      to: "${ADMIN_EMAIL}"
```

### Custom Template Creation
```bash
# Create from existing Manifold
pryma template export my-fraud-detector --output fraud-v2.yaml

# Publish to marketplace
pryma template publish fraud-v2.yaml --price 10-PRYM

# Others can install
pryma template install fraud-v2 --author your-wallet-address
```

---

## Advanced: SDK Internals

### Connection Management
- **WebSocket** for real-time updates (agent status, logs)
- **gRPC** for high-throughput task execution
- **REST** for management operations

### Authentication Flow
1. Client derives auth keypair from master seed
2. Signs challenge from server
3. Receives JWT (valid 24h)
4. All requests include JWT + signature

### Error Handling
```typescript
try {
  await manifold.executeTask(task);
} catch (err) {
  if (err instanceof InsufficientFundsError) {
    // Auto-top-up from treasury
    await client.wallet.topUp(100); // 100 PRYM
    await manifold.executeTask(task);
  } else if (err instanceof AgentTimeoutError) {
    // Scale up Manifold
    await manifold.scale({ minAgents: manifold.scale.minAgents * 2 });
  } else {
    throw err;
  }
}
```

### Rate Limits
- **Free Tier:** 1000 API calls/day, 10 agents max
- **Builder Tier:** 100K calls/day, 1000 agents, $49/month in PRYM
- **Enterprise:** Unlimited, custom compute, dedicated support

---

## Reference Implementations

### Example 1: Logseq Knowledge Base Automation

**Use Case:** Maintain a 331-file Logseq knowledge base with automated builds, graph analytics, and AI tagging.

**Current Implementation:** GitHub Actions workflows  
**PRYMA Migration:** Reimagine as autonomous agent Manifold

#### Architecture Mapping

| Current Workflow | PRYMA Agent | Benefit |
|-----------------|-------------|----------|
| `build.yml` (mdbook build) | Strike × 3 | Parallel builds, auto-scaling |
| `analytics.yml` (graph metrics) | Archive × 2 | Real-time indexing, embeddings |
| `validate.yml` (link checking) | Sentinel × 1 | Continuous monitoring, auto-fix |
| `ai-tagging.yml` (OpenAI tags) | Sage × 1 | Cost optimization, rate limiting |

#### PRYMA Implementation

```typescript
import { PrymaClient, AgentType } from '@pryma/sdk';

const client = new PrymaClient({
  network: 'mainnet',
  masterSeed: process.env.PRYMA_MASTER_SEED
});

// Create Knowledge Base Manifold
const kbManifold = await client.manifold.create({
  name: 'logseq-knowledge-base',
  objective: 'Maintain and evolve 331-file Logseq graph',
  scale: { minAgents: 7, maxAgents: 20, autoScale: true }
});

// Archive Agents: Indexing & Search
await kbManifold.spawnAgent({
  type: AgentType.Archive,
  config: {
    role: 'primary-indexer',
    tasks: ['build_embeddings', 'update_search_index'],
    schedule: 'on_commit',
    vectorDB: 'qdrant',
    model: 'text-embedding-ada-002'
  }
});

await kbManifold.spawnAgent({
  type: AgentType.Archive,
  config: {
    role: 'backup-indexer',
    tasks: ['sync_to_ipfs', 'archive_snapshots'],
    schedule: 'daily',
    storage: 'arweave'
  }
});

// Strike Agents: Build & Deploy
for (let i = 0; i < 3; i++) {
  await kbManifold.spawnAgent({
    type: AgentType.Strike,
    config: {
      role: `builder-${i}`,
      tasks: ['mdbook_build', 'deploy_gh_pages'],
      parallel: true,
      compute: { cpu: '2', memory: '4GB' }
    }
  });
}

// Sentinel Agent: Validation
await kbManifold.spawnAgent({
  type: AgentType.Sentinel,
  config: {
    role: 'graph-validator',
    tasks: [
      'check_broken_links',
      'detect_orphan_pages',
      'validate_markdown_syntax',
      'enforce_naming_conventions'
    ],
    alerting: {
      slack: process.env.SLACK_WEBHOOK,
      autoFix: true // Sentinel can auto-fix broken links
    }
  }
});

// Sage Agent: AI Analysis
await kbManifold.spawnAgent({
  type: AgentType.Sage,
  config: {
    role: 'knowledge-curator',
    tasks: [
      'generate_ai_tags',
      'summarize_pr_diffs',
      'suggest_connections',
      'identify_knowledge_gaps'
    ],
    model: 'gpt-4',
    costLimit: 10 // PRYM per day
  }
});

// Set up GitHub webhook integration
await kbManifold.integrations.add({
  type: 'github',
  repo: 'Pryma-Tech/Logseq',
  events: ['push', 'pull_request'],
  actions: {
    on_push: ['trigger_build', 'update_index'],
    on_pr: ['validate_graph', 'generate_summary']
  }
});

// Monitor Manifold
kbManifold.logs.stream({
  onBuild: (log) => console.log('Build:', log.status),
  onError: (err) => console.error('Error:', err),
  onTag: (tag) => console.log('AI Tag:', tag)
});
```

#### Benefits Over GitHub Actions

| Aspect | GitHub Actions | PRYMA Manifold | Improvement |
|--------|----------------|----------------|-------------|
| **Cost** | $0.008/min (standard runners) | ~0.01 PRYM/build (~$0.001) | **8x cheaper** |
| **Parallelization** | Manual matrix strategy | Auto-scaling Strike agents | **3x faster** |
| **Intelligence** | Static YAML workflows | Sage adapts to content patterns | **Dynamic optimization** |
| **Failure Recovery** | Re-run entire workflow | Sentinel auto-fixes, isolated retries | **10x less downtime** |
| **Auditability** | GitHub logs (90 days) | On-chain Merkle roots (permanent) | **Cryptographic proof** |
| **Self-Improvement** | Manual workflow updates | Agents learn from failures | **Autonomous evolution** |

#### Migration Steps

1. **Set up PRYMA account**
   ```bash
   pryma auth signup --email your@email.com
   ```

2. **Export existing workflow logic**
   ```bash
   pryma migrate github-actions \
     --repo Pryma-Tech/Logseq \
     --output logseq-manifold.yaml
   ```

3. **Review and deploy**
   ```bash
   pryma manifold deploy logseq-manifold.yaml --network testnet
   # Test for 1 week
   pryma manifold promote logseq-manifold --network mainnet
   ```

4. **Gradual cutover**
   - Week 1: Run both systems in parallel
   - Week 2: PRYMA primary, GitHub Actions backup
   - Week 3: Disable GitHub Actions

#### Real-World Results (Projected)

**Current Logseq Automation Costs:**
- GitHub Actions: ~$15/month (500 minutes)
- OpenAI API (tagging): ~$30/month
- **Total: $45/month**

**PRYMA Manifold Costs:**
- Compute (PRYM): ~5 PRYM/month (~$0.50)
- AI inference (via marketplace): ~10 PRYM/month (~$1.00)
- Storage (IPFS/Arweave): ~2 PRYM/month (~$0.20)
- **Total: ~$1.70/month**

**ROI: 96% cost reduction + autonomous improvement**

### Example 2: Fraud Detection Fleet

**Use Case:** Real-time credit card fraud detection for fintech  
**Scale:** 100K transactions/second  
**Manifold Template:** `pryma quickstart --template fraud-detection`

*(See [fraud-detection.md](fraud_detection.md) for full implementation)*

### Example 3: Customer Support Chatbot

**Use Case:** Multi-channel customer support (web, SMS, email)  
**Scale:** 10K concurrent conversations  
**Manifold Template:** `pryma quickstart --template chatbot`

*(See [chatbot.md](chatbot.md) for full implementation)*

---

See protocol and runtime sections for endpoint details and security requirements.