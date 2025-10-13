---
key: dependency-version-conflict
triggers:
  - regex: 'has different versions'
  - regex: 'dependency convergence'
severity: medium
priority: 3
---
## Problem
Conflicting dependency versions after BOM change.
## Recommended Actions
1. Run `mvn -q dependency:tree -Dincludes=<artifact>` to inspect.
2. Prefer BOM managed version; remove explicit versions.
3. If necessary, add <dependencyManagement> override with comment.
## Validation
No convergence warnings in build output.
## Rollback
Reapply prior explicit version only if regression persists.
