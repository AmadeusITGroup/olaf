---
key: outdated-jdk-reference
triggers:
  - regex: '(?i)java.?version[:= ]*(8|11)'
severity: medium
priority: 2
---

## Problem
Pipeline references older JDK version in workflow configuration.

## Recommended Actions
1. Introduce variable (JAVA_VERSION) or matrix entry for target versions 17 and 21.
2. Update tool installer or container tags to eclipse-temurin:17 then later 21.
3. Adjust caching keys to include new JDK version to avoid stale artifacts.

## Validation
Scan finds only target versions (17 or 21); build succeeds on updated JDK.

## Rollback
Restore previous workflow file revision if unforeseen failures.
