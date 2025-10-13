---
key: rewrite-plugin-failure
triggers:
  - regex: '(RewriteExecutionException|MojoExecutionException:.*rewrite)'
severity: high
priority: 1
---

## Problem
Dry run fails due to plugin execution error.

## Recommended Actions
1. Inspect stacktrace; isolate missing dependency or config.
2. Upgrade/downgrade plugin to closest stable version.
3. Ensure `rewrite.yml` syntactically valid (YAML lint).
4. Retry dry run.

## Validation
Dry run completes without exceptions.

## Rollback
Disable plugin temporarily (log DEFERRED issue with rationale).
