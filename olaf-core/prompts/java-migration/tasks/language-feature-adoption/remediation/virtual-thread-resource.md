---
key: virtual-thread-resource
triggers:
  - regex: 'Too many .* virtual threads'
severity: high
priority: 1
---
## Problem
Unbounded virtual thread creation causing resource pressure.
## Recommended Actions
1. Limit executor scope; ensure blocking calls appropriate.
2. Apply backpressure / semaphore.
3. Monitor thread count metrics.
## Validation
Stable throughput; resource usage controlled.
## Rollback
Disable virtual thread feature flag.
