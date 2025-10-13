---
key: actuator-property-removal
triggers:
  - regex: 'deprecated actuator property'
  - regex: 'Invalid property'
severity: medium
priority: 2
---
## Problem
Actuator property removed or renamed in 2.7.
## Recommended Actions
1. Check release notes for replacement name or removal rationale.
2. Update or delete property lines in configuration files.
3. Re-run minimal startup test.
## Validation
No warnings/errors for that property on startup.
## Rollback
Reintroduce only if required; document issue for later review.
