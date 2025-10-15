---
key: dependency-removed-api
triggers:
  - regex: 'NoSuchMethodError|NoSuchFieldError'
severity: medium
priority: 3
---
## Problem
Removed/changed API usage after upgrade.
## Recommended Actions
1. Inspect release notes; apply replacement API.
2. Adjust code & tests.
3. Re-run failing tests only.
## Validation
No linkage errors.
## Rollback
Temporary reflection shim if necessary (log).
