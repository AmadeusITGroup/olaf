---
key: actuator-property-rename
triggers:
  - regex: 'deprecated.*management|Unknown property'
severity: medium
priority: 3
---
## Problem
Deprecated / renamed actuator or management property still used.
## Recommended Actions
1. Identify new key via Boot 3 release notes / error hint.
2. Replace old property; remove deprecated alias.
3. Re-run health endpoint tests.
## Validation
No warning for property; config binds successfully.
## Rollback
Revert single property change if regression observed.
