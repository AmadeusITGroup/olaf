---
key: integration-endpoint-mismatch
triggers:
  - regex: '404.*expected'
severity: medium
priority: 2
---
## Problem
Expected endpoint returns 404 after migration.
## Recommended Actions
1. Check controller mappings & path pattern strategy.
2. Update test base path or mapping.
3. Re-run affected test class.
## Validation
Endpoint returns expected status.
## Rollback
Restore previous mapping if external clients depend.
