# CI Pipeline Inventory — Phase 1

## Preferred approach
1. List all CI workflows and pipelines (GitHub Actions, Jenkins, etc.).
2. Capture Java/Build matrices, caching, and artifacts.
3. Note where Java version is set and how it is installed.
4. Produce `ci_inventory.md` with findings and current gaps.

## Backup option
- If workflows are complex, sample one representative pipeline end-to-end and extrapolate.

## Verify
- `ci_inventory.md` exists and references all active pipelines and Java setup points.
