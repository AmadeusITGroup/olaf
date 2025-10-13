---
key: validation-thirdparty-javax
triggers:
  - regex: 'javax.validation.*from dependency'
severity: low
priority: 5
---
## Problem
Third-party library retains javax validation dependency.
## Recommended Actions
1. Attempt upgrade to Jakarta-ready version.
2. If none, isolate usage; avoid leaking javax imports.
3. Track issue for removal.
## Validation
App uses jakarta API internally only.
## Rollback
N/A (monitor vendor updates).
