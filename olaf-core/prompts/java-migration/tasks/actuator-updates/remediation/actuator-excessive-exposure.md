---
key: actuator-excessive-exposure
triggers:
  - regex: 'exposed endpoints.*sensitive'
severity: high
priority: 1
---
## Problem
Sensitive actuator endpoints exposed publicly.
## Recommended Actions
1. Restrict exposure list to required endpoints.
2. Add security rules limiting access.
3. Verify unauthorized access blocked.
## Validation
403/401 for restricted endpoints externally.
## Rollback
Temporarily re-add endpoint if operational need; log DEFERRED.
