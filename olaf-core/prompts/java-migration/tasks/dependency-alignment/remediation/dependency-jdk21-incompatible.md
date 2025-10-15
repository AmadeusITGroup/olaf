---
key: dependency-jdk21-incompatible
triggers:
  - regex: 'Unsupported class file major version|IllegalAccessError'
severity: high
priority: 1
---
## Problem
Library incompatible with JDK 21.
## Recommended Actions
1. Upgrade to JDK 21 compatible release.
2. If unavailable, replace or shade alternative.
3. Log DEFERRED if vendor ETA known.
## Validation
Error gone; tests pass on 21.
## Rollback
Revert upgrade if critical regression; mark blocked.
