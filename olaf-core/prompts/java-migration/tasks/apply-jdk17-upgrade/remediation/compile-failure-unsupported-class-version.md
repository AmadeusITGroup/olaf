---
key: compile-failure-unsupported-class-version
triggers:
  - regex: 'Unsupported class file version'
severity: high
priority: 1
---

## Problem
A dependency or compiled class targets a higher JDK than currently selected OR build tool still using older bytecode toolchain during upgrade.

## Recommended Actions
1. Ensure JAVA_HOME actually points to JDK 17 (`java -version`).
2. Update plugin/toolchain config (Maven toolchains.xml or Gradle toolchain) to 17.
3. Rebuild or upgrade offending dependency to a version compatible with JDK 17.
4. Clean build (`mvn clean`) to remove stale class artifacts.

## Validation
Re-run compile: no Unsupported class file version errors.

## Rollback
Revert java.version change temporarily if dependency upgrade blocked; document deferral.
