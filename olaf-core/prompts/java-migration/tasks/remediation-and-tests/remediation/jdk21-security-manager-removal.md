---
key: jdk21-security-manager-removal
triggers:
  - regex: 'SecurityManager.*deprecated|removed'
severity: medium
priority: 3
---
## Problem
Code relies on deprecated SecurityManager features.
## Recommended Actions
1. Remove SecurityManager checks.
2. Implement alternative sandboxing (process/container isolation).
3. Update tests expecting security exceptions.
## Validation
Functionality intact; no reliance on SecurityManager.
## Rollback
N/A—feature deprecated; plan mitigation only.
