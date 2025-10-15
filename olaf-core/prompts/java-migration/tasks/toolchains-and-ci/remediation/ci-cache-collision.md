---
key: ci-cache-collision
triggers:
  - regex: 'cache.*corrupt'
severity: low
priority: 4
---
## Problem
Build cache shared incorrectly across JDK versions.
## Recommended Actions
1. Add java version to cache key.
2. Purge old cache entries.
3. Re-run pipeline.
## Validation
Cache restored per JDK version.
## Rollback
Disable cache temporarily if instability persists.
