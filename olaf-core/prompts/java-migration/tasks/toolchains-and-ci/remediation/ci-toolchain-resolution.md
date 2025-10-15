---
key: ci-toolchain-resolution
triggers:
  - regex: 'toolchain.*not found'
severity: medium
priority: 2
---
## Problem
CI cannot resolve configured JDK toolchain.
## Recommended Actions
1. Ensure JDK 21 distribution installed.
2. Correct toolchains.xml or Gradle toolchain version.
3. Re-run CI job.
## Validation
Build picks correct JDK.
## Rollback
Fallback to explicit JAVA_HOME export.
