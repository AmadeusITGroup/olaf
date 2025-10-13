---
key: rewrite-plugin-version
triggers:
  - regex: 'rewrite.*(plugin|mojo).*version.*(error|incompatible)'
severity: medium
priority: 2
---

## Problem
OpenRewrite plugin version incompatible or missing, preventing configuration or execution.

## Recommended Actions
1. Identify latest compatible plugin version (Spring Boot + Maven/Gradle docs).
2. Update build file plugin declaration; remove shadowed duplicate versions.
3. Run `mvn -q rewrite:help` (or Gradle dry run) to confirm load.
4. Commit with concise chore message.

## Validation
- Plugin help command succeeds.
- No duplicate plugin declarations.

## Rollback
Revert plugin version line if build becomes unstable; re-attempt with next lower stable version.
