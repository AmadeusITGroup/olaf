---
key: servlet-dependency-missing
triggers:
  - regex: 'jakarta.servlet.*ClassNotFound'
severity: high
priority: 1
---
## Problem
Jakarta servlet classes absent on classpath.
## Recommended Actions
1. Ensure spring-boot-starter-web present.
2. Remove exclusions dropping servlet api.
3. Rebuild.
## Validation
Classes resolve; app starts.
## Rollback
Restore previous dependency set if conflict emerges.
