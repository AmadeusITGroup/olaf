---
key: modernization-dependency-conflict
triggers:
  - regex: 'conflicts with existing plan'
severity: medium
priority: 3
---
## Problem
Modernization candidate blocked by dependency ordering.
## Recommended Actions
1. Identify prerequisite tasks.
2. Re-order or split candidate.
3. Update catalog status.
## Validation
Conflict removed; candidate rescheduled.
## Rollback
Restore previous ordering if unintended side effects.
