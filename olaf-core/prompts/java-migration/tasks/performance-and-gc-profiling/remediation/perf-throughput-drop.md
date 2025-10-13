---
key: perf-throughput-drop
triggers:
  - regex: 'Throughput drop'
severity: high
priority: 1
---
## Problem
Throughput decreased significantly.
## Recommended Actions
1. Compare CPU utilization & thread scheduling.
2. Evaluate virtual thread impact.
3. Optimize bottleneck or revert feature flag.
## Validation
Throughput within 5% of baseline or better.
## Rollback
Disable recent experimental features.
