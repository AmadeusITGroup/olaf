---
key: perf-latency-regression
triggers:
  - regex: 'Latency regression'
severity: high
priority: 1
---
## Problem
Latency increase beyond threshold.
## Recommended Actions
1. Identify slow endpoints via tracing.
2. Analyze DB calls / blocking sections.
3. Optimize and retest with same load.
## Validation
Latency back within SLA.
## Rollback
Revert change set causing regression.
