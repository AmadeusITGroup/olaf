---
key: validation-risk
triggers:
  - regex: 'import javax.validation'
severity: medium
priority: 2
---
## Problem
Bean Validation javax imports must switch to jakarta.validation; annotations may relocate.
## Recommended Actions
1. Count and list classes with javax.validation annotations.
2. Check for custom constraint validators needing package update.
3. Plan migration order (move after Boot upgrade to 3.x).
## Validation
List produced; no missing validator classes.
## Rollback
Not applicable.
