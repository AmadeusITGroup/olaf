---
key: orphaned-dependency
triggers:
  - regex: 'ClassNotFoundException'
  - regex: 'NoClassDefFoundError'
severity: medium
priority: 4
---
## Problem
Third-party / proprietary dependency lacks Jakarta / Boot 3 ready version.
## Recommended Actions
1. Identify groupId:artifactId and version.
2. Check vendor or repository for Jakarta-compatible release.
3. If none, plan shim or replacement library.
4. Document impact surface (features relying on it).
## Validation
Dependency strategy noted in readiness report.
## Rollback
None (analysis artifact).
