# Container-to-Container Interaction

## PRYMA I/O Interface
All container interactions are mediated by the PRYMA I/O Interface, which enforces universal schemas and cryptographic guarantees.

### Message Schema (YAML)
```yaml
message:
	id: <uuid>
	sender: <container_id>
	receiver: <container_id>
	timestamp: <iso8601>
	payload: <data>
	signature: <hex>
	embedding_ref: <vector_id>
	causal_order: <int>
	replay_protection: true
```

### Protocol Diagram (ASCII)
```
[Container A] <--> [I/O Interface] <--> [Container B]
			|                |                |
	[Sign]         [Schema]         [Verify]
```

This system ensures secure, ordered, and replay-protected communication across the PRYMA ecosystem.