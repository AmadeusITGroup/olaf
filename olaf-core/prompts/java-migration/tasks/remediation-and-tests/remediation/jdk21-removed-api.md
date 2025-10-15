---
key: jdk21-removed-api
triggers:
  - regex: 'cannot find symbol|NoSuchMethodError'
severity: high
priority: 1
---
## Problem
Code uses API removed/changed in JDK 21.
## Recommended Actions
1. Find replacement API / library.
2. Refactor usage; update tests.
3. Rebuild module.
## Validation
No compile/link errors.
## Rollback
Introduce temporary compatibility shim if needed.
