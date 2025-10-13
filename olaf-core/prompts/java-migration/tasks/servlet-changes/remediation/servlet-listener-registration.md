---
key: servlet-listener-registration
triggers:
  - regex: 'Listener.*not fired'
severity: low
priority: 4
---
## Problem
Servlet listener not triggered.
## Recommended Actions
1. Ensure @Component / registration bean.
2. Verify web application type not reactive-only.
3. Re-run startup.
## Validation
Listener events recorded.
## Rollback
Fallback to manual registration class.
