---
key: perf-startup-regression
triggers:
  - regex: 'startup time regression'
severity: low
priority: 4
---
## Problem
Startup slower on JDK 21.
## Recommended Actions
1. Profile class loading (JFR) & bean initialization.
2. Lazy-init non-critical beans.
3. Evaluate AOT/native hints feasibility.
## Validation
Startup delta <15% vs baseline.
## Rollback
Revert lazy-init if side effects arise.
