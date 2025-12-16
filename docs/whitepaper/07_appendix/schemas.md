# Schemas

## Container Manifest (YAML)
```yaml
container:
	id: <uuid>
	role: <agent_type>
	keypair:
		public: <hex>
		private: <hex>
	resources:
		cpu: 2
		memory: 4GB
		storage: 20GB
	permissions:
		- read
		- write
		- execute
```

## Personality Template (JSON)
```json
{
	"reasoning": "deductive",
	"temperament": "stoic",
	"alignment": "lawful-neutral",
	"creativity": "high",
	"strategy": ["long-term", "adaptive"],
	"self_reflection": true,
	"emergent_behavior": true
}
```

## Security Policy (YAML)
```yaml
security:
	audit: enabled
	sandbox: true
	allowed_roles:
		- Sentinel
		- Shade
	logging:
		level: verbose
		destination: /logs/security.log
```

## Technical Notes
All schemas are versioned and validated at runtime. See protocol and runtime sections for more details.