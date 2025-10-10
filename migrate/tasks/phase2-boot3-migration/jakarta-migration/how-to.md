# Jakarta Migration (javax → jakarta) — Phase 2

## Preferred approach
1. Ensure project compiles first on current baseline.
2. Apply OpenRewrite recipes for Jakarta migration where applicable.
3. Manually adjust remaining imports/APIs not handled by recipes.
4. Rebuild and test.

## Backup option
- If OpenRewrite cannot apply (project not compiling), perform targeted manual refactors; then retry recipes.

## Verify
- No `javax.*` imports remain; application builds and tests pass.
