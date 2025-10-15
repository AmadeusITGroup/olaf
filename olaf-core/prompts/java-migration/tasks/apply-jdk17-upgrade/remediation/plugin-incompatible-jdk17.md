---
key: plugin-incompatible-jdk17
triggers:
  - regex: 'UnsupportedClassVersionError'
  - regex: 'java.lang.NoSuchMethodError: (.*)Unsafe'
  - regex: 'Illegal reflective access'
severity: medium
priority: 4
---

## Problem
Build/test plugin version lacks JDK 17 support (e.g., surefire, jacoco, spotbugs).

## Recommended Actions
1. Check plugin versions vs documented JDK 17 support matrix.
2. Upgrade: surefire >= 3.0.x, jacoco >= 0.8.8, spotbugs >= 4.7.x.
3. Remove obsolete JVM args added for older versions.
4. Clean + re-run compile/test.

## Validation
Build succeeds; no plugin compatibility stack traces.

## Rollback
Revert only specific plugin version if new issues unrelated to JDK arise; otherwise keep upgrade.
