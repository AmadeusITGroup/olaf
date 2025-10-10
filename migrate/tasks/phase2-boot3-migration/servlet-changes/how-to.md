# Servlet API Changes — Phase 2

## Preferred approach
1. Review servlet usage; adapt to Jakarta Servlet 6 (package names, APIs).
2. Update configuration and filters accordingly.

## Backup option
- If servlet layer is heavy, isolate and migrate module-by-module.

## Verify
- Integration tests pass for servlet endpoints.
