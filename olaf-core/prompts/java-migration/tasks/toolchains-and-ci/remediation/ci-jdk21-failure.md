---
key: ci-jdk21-failure
triggers:
  - regex: 'job failed.*21'
severity: high
priority: 1
---
## Problem
CI job failing only on JDK 21.
## Recommended Actions
1. Compare logs vs JDK 17 job.
2. Capture diff in dependencies / flags.
3. Apply targeted fix.
## Validation
Both matrix jobs green.
## Rollback
Mark JDK 21 lane experimental; allow failure temporarily.
