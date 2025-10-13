---
key: config-property-removed-boot3
triggers:
  - regex: 'Failed to bind'
  - regex: 'No setter found'
  - regex: 'Cannot resolve configuration property'
severity: medium
priority: 3
---
## Problem
Configuration property no longer exists or renamed in Boot 3.
## Recommended Actions
1. Cross-check release notes for new property name or removal rationale.
2. Update or delete outdated properties.
3. Run minimal startup (or context load test) to confirm.
## Validation
No binding errors for that property.
## Rollback
Reinstate property only if removal breaks critical behavior; investigate alternative.
