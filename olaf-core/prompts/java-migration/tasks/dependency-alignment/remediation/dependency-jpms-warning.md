---
key: dependency-jpms-warning
triggers:
  - regex: 'automatic module name'
severity: low
priority: 5
---
## Problem
Automatic module / JPMS warning under JDK 21.
## Recommended Actions
1. Evaluate need for explicit module naming.
2. If not modularizing now, log DEFERRED.
## Validation
Warning documented or eliminated.
## Rollback
N/A.
