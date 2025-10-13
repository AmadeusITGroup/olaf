---
key: actuator-security-gap
triggers:
  - regex: 'permitAll.*actuator'
severity: high
priority: 1
---
## Problem
Actuator endpoints lack proper auth constraints.
## Recommended Actions
1. Replace broad permitAll with granular matcher.
2. Allow only health|info anonymously if policy permits.
3. Retest access control.
## Validation
Security tests pass; restricted endpoints require auth.
## Rollback
Revert rule change if outage; refine matcher offline.
