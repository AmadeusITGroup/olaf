---
key: servlet-api-change
triggers:
  - regex: 'method .* in class .* cannot be applied'
  - regex: 'HttpServletRequest'
severity: medium
priority: 3
---
## Problem
Servlet API signature differences after migration.
## Recommended Actions
1. Re-check method parameters for updated types (e.g., jakarta.servlet.*).
2. Remove outdated imports; rely on Boot 3 provided servlet API.
3. Adjust filter/initializer registration code to new API.
## Validation
Servlet-related classes compile; web smoke test passes.
## Rollback
Revert specific method refactor if incorrect; re-evaluate signature.
