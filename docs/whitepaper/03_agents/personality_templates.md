# Personality Templates

## Schema
Each agent is instantiated with a personality template, defining its reasoning, temperament, alignment, creativity, and strategic depth.

### Example YAML
```yaml
personality:
  reasoning: deductive
  temperament: stoic
  alignment: lawful-neutral
  creativity: high
  strategy:
    - long-term
    - adaptive
  self_reflection: enabled
  emergent_behavior: allowed
```

### Example JSON
```json
{
  "reasoning": "inductive",
  "temperament": "visionary",
  "alignment": "chaotic-good",
  "creativity": "medium",
  "strategy": ["short-term", "opportunistic"],
  "self_reflection": true,
  "emergent_behavior": true
}
```

Templates allow for rapid instantiation and adaptation of agent fleets, ensuring diversity and resilience.