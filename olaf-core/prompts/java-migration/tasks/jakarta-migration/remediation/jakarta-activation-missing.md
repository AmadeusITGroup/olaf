---
key: jakarta-activation-missing
triggers:
  - regex: 'ClassNotFoundException: jakarta.activation'
severity: low
priority: 5
---
## Problem
Jakarta Activation API needed (mail, mime) not present after migration.
## Recommended Actions
1. Add dependency: `jakarta.activation:jakarta.activation-api` if required.
2. Verify no stale javax.activation usage remains.
3. Rebuild & test mail / mime features.
## Validation
No ClassNotFound for jakarta.activation; related features succeed.
## Rollback
Remove dependency if unused to reduce footprint.
