---
key: container-image-jdk-upgrade
triggers:
  - regex: '(?i)(eclipse-temurin|openjdk).*:(8|11)([^0-9]|$)'
severity: medium
priority: 3
---

## Problem
CI pipeline uses a base container image pinned to legacy Java 8 or 11, blocking upgrade validation and introducing security risk.

## Recommended Actions
1. Replace fixed image tag with variable or matrix (e.g., JAVA_VERSION=17 then 21).
2. Update all Dockerfile stages (builder, runtime) to new tag `eclipse-temurin:17` (later `:21`).
3. Regenerate caches (change FROM line) to avoid stale classpath artifacts.
4. Align CI workflow (e.g., GitHub Actions, Jenkins agents) to same JDK to avoid mismatch.

## Validation
Logs show pulling image tag :17 or :21; build + tests succeed; no remaining :8 or :11 references.

## Rollback
Revert Dockerfile / workflow commit restoring previous image if failures occur.
