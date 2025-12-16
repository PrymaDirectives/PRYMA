# API Endpoints

## Endpoints
- `/api/spawn` — Create a new agent or container
- `/api/link` — Link agents and containers
- `/api/log` — Retrieve audit logs
- `/api/exec` — Execute tasks or workflows
- `/api/status` — Get system health and metrics
- `/api/update` — Propose and deploy upgrades

## CLI Examples
```
pryma spawn lumen
pryma link strike lumen
pryma log watcher
pryma exec task.yaml
pryma status
pryma update --protocol
```

See protocol and runtime sections for endpoint details and security requirements.