---
key: compile-failure-missing-module
triggers:
  - regex: 'error: module [^ ]+ not found'
  - regex: 'package [^ ]+ does not exist'
severity: medium
priority: 2
---

## Problem
Compilation fails due to removed/relocated packages or missing module dependency after JDK 17 switch.

## Recommended Actions
1. Add missing dependency (check Maven Central / Spring Boot BOM alignment).
2. For javax→jakarta issues: defer to Jakarta migration phase (mark DEFERRED) unless blocking.
3. Run `mvn -q dependency:tree -Dincludes=<groupId>:<artifactId>` to confirm presence.
4. Check shading/relocation if using fat jars.

## Validation
Compile step succeeds; missing module/package errors gone.

## Rollback
Temporarily revert dependency version changes if they introduced conflicts.
