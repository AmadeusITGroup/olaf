---
key: path-matching-strategy
triggers:
  - regex: 'No handler found'
  - regex: '404'
severity: high
priority: 1
---
## Problem
After upgrading to 2.6.x certain endpoints return 404 due to path matching strategy differences.
## Recommended Actions
1. Confirm controller/request mapping annotations unchanged.
2. Set (if needed) `spring.mvc.pathmatch.matching-strategy=ant_path_matcher` temporarily.
3. Refactor to PathPatternParser: avoid ambiguous patterns, remove trailing wildcards.
4. Remove temporary compatibility property once all routes resolved.
## Validation
Endpoints return expected responses; no fallback 404 logs.
## Rollback
Re-add temporary property if urgent fix required; plan refactor.
