---
key: rewrite-build-integration
triggers:
  - regex: '(Failed to execute goal.*rewrite|Task .+ rewrite.* failed)'
severity: high
priority: 1
---

## Problem
Build fails during rewrite goal/task execution blocking migration sequencing.

## Recommended Actions
1. Run build with `-X` (Maven) / `--stacktrace` (Gradle) to capture full error.
2. Check for conflicting plugin phases / duplicate executions.
3. Update plugin to latest compatible / align with build tool version.
4. Temporarily disable rewrite plugin if unrelated migration must proceed (log DEFERRED issue).

## Validation
- Build succeeds with rewrite plugin configured.

## Rollback
Comment out plugin configuration, commit, then reintroduce after root cause fix.
