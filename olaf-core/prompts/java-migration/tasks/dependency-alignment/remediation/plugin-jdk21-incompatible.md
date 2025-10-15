---
key: plugin-jdk21-incompatible
triggers:
  - regex: 'requires Java [0-9]+'
severity: medium
priority: 2
---
## Problem
Build plugin lacks JDK 21 support.
## Recommended Actions
1. Update plugin version.
2. Remove stale explicit dependencies conflicting.
3. Re-run build on 21.
## Validation
Plugin tasks succeed.
## Rollback
Fallback to earlier version; log follow-up.
