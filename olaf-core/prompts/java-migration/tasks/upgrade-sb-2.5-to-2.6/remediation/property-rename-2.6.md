---
key: property-rename-2.6
triggers:
  - regex: 'Deprecated configuration property'
  - regex: 'Failed to bind'
severity: medium
priority: 2
---
## Problem
Property names changed or deprecated in 2.6 causing warnings or binding failures.
## Recommended Actions
1. Check release notes & migration guide for new property equivalents.
2. Replace deprecated keys; remove unused ones.
3. Re-run tests to ensure no binding warnings.
## Validation
Startup/bind logs clean; tests pass.
## Rollback
Restore previous key if new key causes regression; investigate further.
