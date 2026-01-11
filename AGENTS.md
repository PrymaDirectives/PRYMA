# PRYMA Agent Architecture

## Overview
PRYMA agents are autonomous, cryptographically-governed AI containers organized into Manifolds (vector-space neighborhoods) that execute tasks across distributed infrastructure.

## Core Agent Types
See the full whitepaper: [docs/whitepaper/03_agents/agent_types.md](docs/whitepaper/03_agents/agent_types.md)

### Archetypes
- **Lumen**: The Oracle — Central reasoning, logic, orchestration
- **Strike**: The Warrior — Task execution, deployment, workflow management
- **Echo**: The Herald — Communications, I/O, message translation
- **Sentinel**: The Guardian — Security, monitoring, threat response
- **Argus**: The All-Seeing Guardian — Perception, environmental monitoring
- **Sage**: The Architect — Strategic planning, optimization, scenario analysis
- **Archive**: The Librarian — Knowledge storage, retrieval, auditability
- **Spirit**: The Swarm — Micro-agents, emergent behaviors, creative tasks
- **Shade**: The Trickster — Adversarial sandbox, red teaming, stress testing

## Reference Implementation: WSDM (Wisdom Storage Distributed Metarepo)

The WSDM knowledge base automation system (see [WSDM/AUTOPROMPT.md](WSDM/AUTOPROMPT.md)) is a **proto-PRYMA system** that demonstrates agent-like behavior:

- **Archive Agents**: Graph analytics, knowledge indexing, embeddings generation
- **Strike Agents**: CI/CD workflows, static site builds, file generation
- **Sentinel Agents**: PR validation, graph integrity checks, orphan detection
- **Sage Agents**: AI-assisted tagging, semantic analysis, diff summarization
- **Argus Agents**: Fleet monitoring, analytics dashboard, environmental observation

### Migration Path to PRYMA
The current GitHub Actions workflows could be reimplemented as a PRYMA Manifold:

```yaml
# WSDM Knowledge Base Manifold
manifold:
  objective: "Maintain and evolve WSDM knowledge base"
  
agents:
  - type: Archive
    count: 2
    role: "Index markdown files, build search embeddings"
  
  - type: Strike  
    count: 3
    role: "Execute mdbook builds, deploy to GitHub Pages"
  
  - type: Sentinel
    count: 1
    role: "Validate graph integrity, check for broken links"
  
  - type: Sage
    count: 1
    role: "Generate AI tags, summarize knowledge diffs"
```

See [docs/whitepaper/07_appendix/reference_implementations.md](docs/whitepaper/07_appendix/reference_implementations.md) for the full implementation guide.

## Quick Start

### Using PRYMA SDK
```bash
# Install PRYMA CLI
curl -fsSL https://install.pryma.tech | sh

# Deploy WSDM automation as a Manifold
pryma manifold create --template "knowledge-base" \
  --repo "Pryma-Tech/WSDM" \
  --webhook "https://github.com/Pryma-Tech/WSDM"
```

### Using GitHub Actions (Current)
See existing workflows in `WSDM/.github/workflows/`

## Documentation

- **PRYMA Whitepaper**: [docs/whitepaper/README.md](docs/whitepaper/README.md)
- **Agent Architecture**: [docs/whitepaper/03_agents/](docs/whitepaper/03_agents/)
- **API & SDK**: [docs/whitepaper/07_appendix/api_endpoints.md](docs/whitepaper/07_appendix/api_endpoints.md)
- **WSDM Automation**: [WSDM/AUTOPROMPT.md](WSDM/AUTOPROMPT.md)
- **WSDM Repository**: [https://github.com/Pryma-Tech/WSDM](https://github.com/Pryma-Tech/WSDM)