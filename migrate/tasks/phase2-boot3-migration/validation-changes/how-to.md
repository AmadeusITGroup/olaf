# Validation API Changes — Phase 2

## Preferred approach
1. Replace `javax.validation` with `jakarta.validation` imports.
2. Update constraints and validator setup as needed.

## Backup option
- If third-party libs still depend on javax, use compatibility layers temporarily and plan replacement.

## Verify
- Validation tests pass with Jakarta validation.
