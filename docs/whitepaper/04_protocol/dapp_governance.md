# dApp Governance & Economic Model

## Governance Mechanisms
PRYMA's governance is decentralized and transparent, leveraging Solana smart contracts and dashboards for:
- Role-based permissioning
- Task delegation and approval workflows
- Real-time voting and consensus
- Audit trails for all governance actions

## Economic Model: The PRYM Token

### Token Utility (Triple-Function Design)

**1. Compute Credits (Gas for Agents)**
- Agents consume PRYM to execute tasks (inference, storage, network calls)
- Rate: ~0.01 PRYM per 1M tokens processed by LLM
- Burns 50% of consumed PRYM (deflationary pressure)
- Remaining 50% → compute providers (decentralized inference nodes)

**2. Governance Rights (Voting Power)**
- 1 PRYM staked = 1 vote on protocol proposals
- Voting topics: protocol upgrades, Manifold certification, treasury allocation
- Quadratic voting available for contentious decisions (√PRYM = vote weight)
- Lock periods: 7 days (normal), 30 days (+2x multiplier), 365 days (+10x multiplier)

**3. Collateral/Staking (Security Deposits)**
- Sentinel agents must stake PRYM to operate (min 100 PRYM)
- Slashing conditions: publishing fraudulent Merkle roots, censoring logs, downtime >10%
- Slash amount: 10% of stake (first offense), 100% (repeated violations)
- Slashed PRYM → treasury or burned

### Token Distribution

| Allocation | % | Vesting |
|------------|---|----------|
| Protocol Treasury | 30% | Controlled by DAO |
| Compute Provider Rewards | 25% | 10-year emission schedule |
| Early Adopters (Airdrop) | 15% | 6-month cliff, 2-year linear |
| Core Development Team | 15% | 1-year cliff, 4-year linear |
| Strategic Reserves | 10% | Multi-sig, 5-year lock |
| Ecosystem Grants | 5% | Immediate, community-voted |

**Total Supply:** 1,000,000,000 PRYM (deflationary via burns)

### Pricing & Exchange Mechanisms

**Primary Market (Internal)**
- Users buy PRYM from protocol treasury at dynamic price
- Price formula: $P = P_0 \cdot (1 + \alpha \cdot \text{demand\_ratio})$
  - $P_0$ = base price (0.10 USD)
  - $\alpha$ = elasticity factor (0.05)
  - demand_ratio = (PRYM purchased last 24h) / (PRYM in treasury)

**Secondary Market (External)**
- PRYM listed on Solana DEXs (Raydium, Orca)
- Liquidity pools: PRYM/USDC, PRYM/SOL
- Protocol provides initial liquidity (5M PRYM + 500K USDC)

### Compute Economics: The Marketplace

**Problem:** Who provides the GPUs for millions of agents?

**Solution:** Decentralized Compute Marketplace

#### Supply Side (Compute Providers)
- Anyone can register as a provider (AWS, home GPU rig, etc.)
- Requirements: GPU with CUDA 11+, 100 Mbps network, 99% uptime SLA
- Providers stake 1000 PRYM as collateral
- Earnings: 50% of PRYM spent on their compute + optional tips

#### Demand Side (Agent Operators)
- Users specify compute requirements in agent config:
```yaml
agent:
  name: "fraud-detector-001"
  compute:
    gpu: "A100"  # or "T4", "V100", "CPU-only"
    max_cost: 10 PRYM/day
    latency: "<100ms"
```
- System auto-matches agents to providers via auction (lowest bid wins)

#### Pricing Discovery
- Real-time bidding: providers set PRYM/hour rates
- Benchmark: 1 PRYM/hour for 1x A100 GPU (equivalent to ~$1.50/hour)
- Spot pricing: unused capacity offered at 50% discount

### Revenue Streams for Fleet Operators

**1. Service Monetization**
- Agents can offer services to external users (e.g., "fraud detection as a service")
- Pricing in PRYM or stablecoins (auto-converted)
- Example: Charge 0.1 PRYM per fraud check, process 10K/day = 1000 PRYM/day revenue

**2. Data Marketplace**
- Agents generate valuable data (embeddings, training logs)
- Operators can sell anonymized datasets via encrypted IPFS links
- Payment in PRYM, royalties via smart contract

**3. Manifold Certification**
- High-quality Manifolds (verified via Shade adversarial testing) earn certification badges
- Certified Manifolds receive 2x priority in task routing
- Certification costs 100 PRYM, voted by DAO

### Anti-Sybil & Anti-Whale Mechanisms

**Sybil Resistance (Identity)**
- Agent spawning requires 0.1 PRYM "birth fee" (burned)
- At 1M agents = 100K PRYM burned = significant cost to spam
- Rate limiting: 1000 agents/day per master seed

**Whale Resistance (Governance)**
- Quadratic voting reduces whale influence
- Voting power = √(PRYM staked), not linear
- Example: 1M PRYM = 1000 votes, not 1M votes
- Delegation allowed (vote escrow model)

### Economic Security Budget

**Goal:** Make attacking PRYMA more expensive than any potential gain

**Attack Vectors & Costs:**
| Attack | Cost to Execute | Economic Defense |
|--------|----------------|------------------|
| 51% vote manipulation | Acquire 500M PRYM (~$50M at $0.10) | Quadratic voting reduces to √500M = 22K votes (7% of total) |
| Sentinel collusion (fraud proofs) | Bribe 67% of Sentinels (~10K PRYM each = 6.7M PRYM) | Slashing destroys 6.7M PRYM ($670K loss) + on-chain evidence |
| Compute poisoning | Stake 1000 PRYM per malicious node | Automatic slashing on anomaly detection |
| Sybil flood (spam agents) | 0.1 PRYM per agent × 1M agents = 100K PRYM | Burned, no recovery |

### Deflationary Dynamics

**Burn Mechanisms:**
- 50% of compute spend → burned
- Agent birth fees → burned
- Slashed stakes → 50% burned, 50% treasury

**Emission Cap:**
- Max 2% annual inflation from compute rewards
- Net deflationary if burn rate > 2%/year

**Projected Equilibrium:**
- At steady state (10M agents, 1B inferences/day):
  - Compute spend: 10M PRYM/day
  - Burn: 5M PRYM/day
  - Annual burn: 1.825B PRYM
  - Total supply reduction: 50%+ in first 5 years

## Mythic Metaphor
The governance layer is the "Council of Elders," where every agent and container has a voice. Decisions are made openly, recorded on the blockchain, and enforced by cryptographic law. The PRYM token is the "Lifeblood of the Fleet"—circulating through every agent, empowering action, and concentrating value where wisdom and utility converge.