---
key: incompatible-plugin
triggers:
  - regex: 'UnsupportedClassVersionError'
  - regex: 'plugin version .* not compatible'
severity: high
priority: 3
---
## Problem
Build/test plugin version lacks Boot 3 / JDK 17+ compatibility.
## Recommended Actions
1. Identify plugin (surefire, failsafe, jacoco, spring-boot-maven-plugin).
2. Upgrade to recommended versions (surefire>=3.0.x, jacoco>=0.8.8, boot plugin aligned to 3.x on upgrade).
3. Re-run compile/tests.
## Validation
No compatibility errors; plugin shows updated version in logs.
## Rollback
Revert only if new version introduces unrelated regression.
