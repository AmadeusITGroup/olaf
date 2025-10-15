---
key: dependency-temp-override
triggers:
  - regex: 'temporary override'
severity: low
priority: 4
---
## Problem
Temporary explicit version override retained.
## Recommended Actions
1. Track override in findings with rationale & removal target.
2. Periodically test without override.
## Validation
Override removed when upstream fix lands.
## Rollback
Reinstate override if conflict reappears.
