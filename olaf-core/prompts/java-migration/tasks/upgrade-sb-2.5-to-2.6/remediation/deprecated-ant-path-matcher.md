---
key: deprecated-ant-path-matcher
triggers:
  - regex: 'AntPathMatcher'
  - regex: 'deprecated'
severity: low
priority: 3
---
## Problem
Usage of AntPathMatcher flagged; future removal risk.
## Recommended Actions
1. Inventory Ant path patterns in security & MVC configs.
2. Begin migrating to PathPatternParser-friendly patterns (no complex ** overlaps).
3. Remove any explicit AntPathMatcher beans unless strictly required.
## Validation
No deprecation warnings in logs; endpoint tests pass.
## Rollback
Keep AntPathMatcher temporarily if complex patterns; record DEFERRED.
