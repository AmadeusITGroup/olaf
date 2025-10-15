---
key: ci-missing-jdk21
triggers:
  - regex: 'could not download.*jdk 21'
severity: medium
priority: 2
---
## Problem
CI environment lacks JDK 21 distribution.
## Recommended Actions
1. Add setup action / tool installer entry for 21.
2. Validate checksum / vendor.
3. Cache distribution if supported.
## Validation
JDK 21 appears in `java -version` step.
## Rollback
Temporarily remove 21 from matrix until available.
