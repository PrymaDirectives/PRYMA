# PRYMA Agent Architecture

## Overview
PRYMA agents are autonomous, cryptographically-governed AI containers organized into Manifolds (vector-space neighborhoods) that execute tasks across distributed infrastructure.

## Core Agent Types
See the full whitepaper: [docs/whitepaper/03_agents/agent_types.md](docs/whitepaper/03_agents/agent_types.md)

### Archetypes
- **Lumen**: Central reasoning, logic, orchestration
- **Strike**: Task execution, deployment, workflow management
- **Echo**: Communications, I/O, message translation
- **Sentinel**: Security, monitoring, threat response
- **Sage**: Strategic planning, optimization, scenario analysis
- **Archive**: Knowledge storage, retrieval, auditability
- **Spirit**: Micro-agents, emergent behaviors, creative tasks
- **Shade**: Adversarial sandbox, red teaming, stress testing

## Reference Implementation: Logseq Automation

The Logseq knowledge base automation system (see [Logseq/AUTOPROMPT.md](Logseq/AUTOPROMPT.md)) is a **proto-PRYMA system** that demonstrates agent-like behavior:

- **Archive Agents**: Graph analytics, knowledge indexing, embeddings generation
- **Strike Agents**: CI/CD workflows, static site builds, file generation
- **Sentinel Agents**: PR validation, graph integrity checks, orphan detection
- **Sage Agents**: AI-assisted tagging, semantic analysis, diff summarization

### Migration Path to PRYMA
The current GitHub Actions workflows could be reimplemented as a PRYMA Manifold:

```yaml
# Logseq Knowledge Base Manifold
manifold:
  objective: "Maintain and evolve Logseq knowledge base"
  
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

# Deploy Logseq automation as a Manifold
pryma manifold create --template "knowledge-base" \
  --repo "Pryma-Tech/Logseq" \
  --webhook "https://github.com/Pryma-Tech/Logseq"
```

### Using GitHub Actions (Current)
See existing workflows in `Logseq/.github/workflows/`

## Documentation

- **PRYMA Whitepaper**: [docs/whitepaper/README.md](docs/whitepaper/README.md)
- **Agent Architecture**: [docs/whitepaper/03_agents/](docs/whitepaper/03_agents/)
- **API & SDK**: [docs/whitepaper/07_appendix/api_endpoints.md](docs/whitepaper/07_appendix/api_endpoints.md)
- **Logseq Automation**: [Logseq/AUTOPROMPT.md](Logseq/AUTOPROMPT.md)