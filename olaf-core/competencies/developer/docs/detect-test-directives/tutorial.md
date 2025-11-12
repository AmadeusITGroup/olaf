# Tutorial: Detect Test Directives (Step-by-Step)

This tutorial shows how to use the `detect-test-directives` prompt to discover a repository’s unit test stack, mine test patterns, and generate two persistent practice docs. It follows the OLAF step-by-step tutorial style.

## Prerequisites
- Git repository cloned locally
- Windows PowerShell available
- Access to OLAF in your IDE/workbench

## Goal
- Generate and maintain two persistent docs (kebab-case) under `olaf-data/practices/`:
  - `how-to-run-tests.md`
  - `unit-test-patterns.md`
- Produce a temporary `recent-tests-report.md` during the run (deleted at the end)

## Inputs
- `repo_path`: absolute path to the repo root (required)
- `branch`: optional (defaults to currently checked out)
- `sample_limit`: optional (default 30)

## Steps
1. Open OLAF and run the prompt
   - Invoke: `detect test directives` (or open `developer/prompts/detect-test-directives.md`)
   - Provide required inputs when asked
2. Validation
   - Prompt verifies repository, detects dominant language and test framework
3. Analyze recent changes (Git)
   - Creates an ephemeral `recent-tests-report.md` to guide sampling
4. Sample tests and mine patterns
   - Looks at representative tests (controller/service/unit/integration)
   - Extracts directives: annotations/markers, mocking, assertions, fixtures, naming
5. Generate persistent docs (kebab-case)
   - `olaf-data/practices/how-to-run-tests.md`
   - `olaf-data/practices/unit-test-patterns.md`
6. Optional: run tests with coverage (upon approval)
   - Prompt proposes stack-appropriate commands
7. Cleanup
   - Deletes `recent-tests-report.md`

## Expected Results
- Two updated practice docs with concrete, repo-specific content
- Clear commands to run tests and coverage
- Summarized directives and validated snippet examples

## Conventions & Policies
- All generated filenames are lowercase kebab-case
- Legacy uppercase/underscore variants are auto-renamed
- `recent-tests-report.md` is always deleted at the end

## Tips
- If tests are not under `src/test`, specify alternative paths (e.g., `tests`, `__tests__`)
- Keep the docs short and precise; include exact commands and report locations

## Next Steps
- Commit `olaf-data/practices/how-to-run-tests.md` and `olaf-data/practices/unit-test-patterns.md`
- Re-run the prompt occasionally to refresh patterns after significant changes
