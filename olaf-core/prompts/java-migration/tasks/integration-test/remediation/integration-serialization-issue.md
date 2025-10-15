---
key: integration-serialization-issue
triggers:
  - regex: 'JsonMappingException|HttpMessageNotReadable'
severity: medium
priority: 3
---
## Problem
JSON/XML serialization failures in integration tests.
## Recommended Actions
1. Compare model changes vs payload.
2. Adjust Jackson config / annotations.
3. Re-run failing test with trace logging.
## Validation
Payload round-trips successfully.
## Rollback
Revert serializer config tweak if regression.
