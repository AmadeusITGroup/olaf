---
key: servlet-endpoint-mapping
triggers:
  - regex: '404|No handler found'
severity: medium
priority: 2
---
## Problem
Endpoint mapping broken after namespace change.
## Recommended Actions
1. Inspect controller annotations & path strategy.
2. Adjust patterns / enable compatibility flag temporarily.
3. Add test covering mapping.
## Validation
Endpoint returns expected response.
## Rollback
Reapply previous mapping pattern; schedule refactor.
