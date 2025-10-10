---
name: java-migration-executor
description: Sequential executor that reads the latest migration plan and executes pending tasks until completion
tags: [java, migration, executor, spring-boot]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior>
- <olaf-interaction-protocols>
You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`
You WILL use terminal commands, not training data for timestamps.

## Purpose
This prompt executes a previously generated migration plan file line-by-line, starting from the first unchecked task, and updates its status as tasks are executed. It does not plan, reorder, or modify task definitions beyond status tokens.

## Input Parameters
If not provided, you MUST request these parameters:
- **execution_mode**: string|{"findings","migration"} - Where to look for the plan (REQUIRED; default: "findings")
- **migration_timestamp**: string - `YYYYMMDD-HHmm` identifying the migration directory under findings (REQUIRED if execution_mode=findings)
- **plan_dir**: string - Absolute or workspace-relative directory containing the plan (OPTIONAL; overrides the derived directory)
- **migration_project_slug**: string - Lowercase slug for migration layout `project-<slug>` (REQUIRED if execution_mode=migration and plan_dir not provided)
- **dry_run**: boolean - If true, simulate without changes (OPTIONAL; default: false)
- **commit_changes**: boolean - If true, create git commits per task update (OPTIONAL; default: true)

## Plan Discovery
You MUST determine the plan file as follows:
- If `execution_mode = findings` (default):
  - Derive directory: `[id:findings_dir]migrations/migration_<migration_timestamp>/` unless `plan_dir` is provided.
  - Pick the lexicographically latest file matching `migration-plan-*.md` in that directory.
- If `execution_mode = migration`:
  - Derive directory: `migrate/java/project-<migration_project_slug>/` unless `plan_dir` is provided.
  - Pick the lexicographically latest file matching `java-migration-*.md` in that directory.
- FAIL with a clear message if the directory or plan file is missing.

You MUST also look for a context file in the same directory:
- findings mode: `migration-bootstrap-context.yaml`
- migration mode: `migration-bootstrap-context.yaml` (if present)

## File Conventions
- Plan files are UTF-8. Preserve trailing newline.
- Only mutate checklist lines; never alter ordering, IDs, or section structure.
- Task line pattern you MUST parse exactly:
  - `- [ ] {ID} {Title} :: {relative-task-path}`

## Task Directory Expectations
```
tasks/<phase-folder>/<task-id>-*/
  how-to.md  (concise instructions; preferred path first, fallback last)
  *.ps1 / *.sh (automation scripts, optional; used only if how-to instructs)
  verify.*     (verification script, optional)
```
- `{relative-task-path}` is resolved relative to the plan directory unless absolute.

## Canonical Helper Tasks Resolution
When a plan's `{relative-task-path}` directory is missing, you MUST try to resolve a canonical helper task under `migrate/tasks/` before failing.

Resolution order:
1. Prefer intent-based helpers (no numeric prefixes):
   - Example intents (Phase 3): `toolchains-and-ci/`, `dependency-alignment/`, `remediation-and-tests/`, `performance-and-gc-profiling/`, `language-feature-adoption/`, `modernization-opportunities/`.
   - Phase 0 example: `jdk-switch/`.
   - Match by phase directory + title keywords → select the best intent directory.
2. If no intent helper is found, fallback to numeric canonical folders by ID prefix (e.g., `task-3.1-*`).
3. If still not found, choose the closest helper in the same phase that covers the task intent.

Execution with canonical tasks:
- Use `how-to.md` from the canonical task for guidance.
- Only run scripts if and when the `how-to.md` explicitly instructs it.
- Define and run clear verification commands (compile/tests, `java -version`, `mvn -v`, etc.).
- Update the plan status token upon success or skip with reason per Skip Rules.

## Interaction Protocol
- Use Act for reading, parsing, and marking checkboxes.
- Use Propose-Confirm-Act before executing any automation scripts or performing code changes when `dry_run=false` and only if instructed by a `how-to.md`.
- For `dry_run=true`, never write to disk or run scripts; print intended actions and the line that would be changed.

## Core Loop
Repeat until no pending tasks or a failure occurs:
1. Locate plan directory and open the latest plan file according to Plan Discovery.
2. Find the first unchecked task line exactly matching `- [ ]` prefix.
3. Parse `{ID}`, `{Title}`, `{relative-task-path}` according to the line pattern.
4. Resolve the task directory; load `how-to.md` if present.
5. Execute the task:
   - Follow `how-to.md` steps. It MUST present a preferred approach first and a fallback if preferred fails.
   - Only execute scripts when `how-to.md` instructs to run them.
     - On Windows: prefer `*.ps1`; else use `*.sh` via compatible shell if available.
     - On Unix/macOS: prefer `*.sh`; set execute bit if needed.
   - If no `how-to.md` exists: apply AI-guided steps using domain knowledge with Propose-Confirm-Act.
6. Run `verify.*` if present.
7. On success:
   - Mark the task line from `- [ ]` to `- [x]`.
   - If `commit_changes=true`, create a git commit with message `{ID}: {short action}`. For final completion, use `migration: all tasks complete`.
8. On valid skip conditions (see Skip Rules):
   - Mark `- [-]` and append `(skip: reason)`.
   - Optionally commit with message `{ID}: skip ({reason})` if `commit_changes=true`.
9. On failure:
   - Do NOT modify the checkbox.
   - Append a one-line log under a `### Failures` section (create if absent): `- <timestamp> {ID} <short error>`.
   - Stop execution.

## Skip Rules
You MAY mark a task as skipped only when:
- The task is already satisfied (e.g., dependency already upgraded).
- The task is superseded by a later aggregated task.
Format: `- [-] {ID} {Title} :: {path} (skip: reason)`

## Completion
When no `- [ ]` remain in the plan:
1. Append, if absent, this block at the end of the file:
```markdown
---
Completed: <timestamp>
```
2. Create a final commit with message `migration: all tasks complete` if `commit_changes=true`.

## Output Format
Console Outputs:
- Discovery details (directory, plan file chosen)
- Current task ID and title
- Actions taken or planned (dry-run)
- Verification result
- Skip/failure reason when applicable
- Final completion summary

File Mutations:
- Plan file line updates for status tokens and optional `### Failures` section
- No other files modified except by task automation or confirmed manual edits

## Commands & Utilities
- Time: use the Time Retrieval commands above.
- Git: use standard commands to add changes and commit with messages shown in Core Loop. Do not tag or push.
- Shell execution:
  - Windows: `powershell -ExecutionPolicy Bypass -File <script.ps1>`
  - Unix/macOS: `bash <script.sh>`

## Domain-Specific Rules
You MUST:
- Respect original task ordering and IDs at all times.
- Only change the checkbox token and append the failures section or completion block.
- Keep execution strictly sequential; never parallelize tasks.
- Stop immediately on failure and report.
- Keep logs concise and actionable.

## Success Criteria
You WILL consider the execution successful when:
- [ ] Plan directory detected and latest plan file selected
- [ ] First unchecked task executed or properly skipped
- [ ] Status updated to [x] or [-] with reason
- [ ] Failures logged correctly when they occur
- [ ] Commits created as configured
- [ ] Completion block added when all tasks are done
- [ ] No unauthorized file changes made

## Required Actions
1. Resolve inputs and locate plan.
2. Iterate tasks sequentially.
3. For each task: prepare, execute (or dry-run), verify.
4. Update plan line and optionally commit.
5. Halt on failure; otherwise continue until completion.
6. Add completion block and final commit.

## Error Handling
You WILL handle explicitly:
- **Missing Directory**: show expected directory and how it was derived; abort.
- **No Plan Files**: show expected pattern; abort.
- **Invalid Line Format**: show offending line; skip and continue to next task.
- **Task Directory Missing**: attempt Canonical Helper Tasks Resolution; if no suitable canonical task is found, log failure and stop.
- **Script Execution Error**: capture exit code/stdout/stderr; log under Failures and stop.
- **Verification Failure**: log under Failures and stop.
- **File Write Error**: show remediation (permissions/path) and stop.

⚠️ **Critical Requirements**
- NEVER reorder tasks or modify IDs/titles.
- ALWAYS preserve UTF-8 and trailing newline.
- ALWAYS ask confirmation before destructive changes unless `dry_run=true`.
- ALWAYS commit with clear messages when `commit_changes=true`.
- ALWAYS stop on first failure and log it.
