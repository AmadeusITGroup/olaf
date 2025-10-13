---
key: validation-dependency-missing
triggers:
  - regex: 'jakarta.validation.*ClassNotFound'
severity: high
priority: 1
---
## Problem
Jakarta validation API/provider not present.
## Recommended Actions
1. Ensure spring-boot-starter-validation added.
2. Remove old javax validation libs.
3. Rebuild.
## Validation
Validation classes resolve; basic constraint test passes.
## Rollback
Reinsert prior dependency temporarily if severe conflict.
