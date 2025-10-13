---
key: jdk21-temporary-export
triggers:
  - regex: '--add-opens|--add-exports'
severity: low
priority: 4
---
## Problem
Temporary module export flags added.
## Recommended Actions
1. Identify code requiring internal APIs.
2. Remove usage or replace with official API.
3. Drop flags; verify build.
## Validation
Build succeeds without flags.
## Rollback
Reapply flags if critical blocker persists.
