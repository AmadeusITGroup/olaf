---
key: plugin-version-incompatible
triggers:
  - regex: '(Unsupported major.minor|requires Java)'
severity: high
priority: 1
---
## Problem
Build plugin not compatible with Boot 3 / JDK version.
## Recommended Actions
1. Upgrade plugin to supported version.
2. Remove redundant explicit version if BOM manages.
3. Re-run build.
## Validation
Plugin executes cleanly.
## Rollback
Revert plugin bump if unrelated failures appear.
