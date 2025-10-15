---
key: jdk21-lib-incompatible
triggers:
  - regex: 'Unsupported class file major version'
severity: high
priority: 1
---
## Problem
Third-party lib incompatible with JDK 21.
## Recommended Actions
1. Upgrade / substitute library.
2. Confirm license & security posture.
3. Retest failing scenarios.
## Validation
Build & tests succeed.
## Rollback
Revert upgrade with documented block.
