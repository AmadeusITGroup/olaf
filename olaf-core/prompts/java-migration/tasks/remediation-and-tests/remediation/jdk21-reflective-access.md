---
key: jdk21-reflective-access
triggers:
  - regex: 'illegal reflective access'
severity: medium
priority: 2
---
## Problem
Illegal reflective access warnings (future failure risk).
## Recommended Actions
1. Replace reflection with supported API.
2. If unavoidable add opens flag (temporary) & log DEFERRED.
3. Track removal plan.
## Validation
Warning removed or documented.
## Rollback
Retain flag until refactor complete.
