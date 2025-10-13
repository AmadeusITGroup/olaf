---
key: perf-gc-pause-regression
triggers:
  - regex: 'GC pause.*increased'
severity: medium
priority: 2
---
## Problem
GC pause times higher on JDK 21.
## Recommended Actions
1. Compare GC algorithm selection.
2. Tune heap / region sizes minimally.
3. Investigate allocation hotspots via JFR.
## Validation
Pause metrics within baseline threshold.
## Rollback
Revert GC tuning flags.
