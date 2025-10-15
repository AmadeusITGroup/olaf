---
name: run-java-migration
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

## Prerequisites Check (ONCE PER MIGRATION)
Before executing any migration tasks, check if prerequisites have been verified for this migration:

### Check for Prerequisites Marker
1. Look for `prerequisites-verified.txt` in the plan directory
2. If found, skip prerequisites check and proceed to execution
3. If missing, perform one-time prerequisites verification

### Required Tools (if checking)
1. **Java Development Kits**: JDK 11, 17, 21 at `~/.olaf/jdk/{version}/`
2. **Build Tool**: Maven ≥ 3.9 OR Gradle ≥ 8.0  
3. **Git**: Any recent version
4. **Python 3**: Version 3.8+ for migration scripts

### Quick Verification Commands
```bash
# Check JDKs
~/.olaf/jdk/11/bin/java -version
~/.olaf/jdk/17/bin/java -version  
~/.olaf/jdk/21/bin/java -version

# Check build tool (one of these)
mvn --version
gradle --version

# Check Git and Python
git --version
python --version
```

### After Successful Verification
Create `prerequisites-verified.txt` in the plan directory with content:
```
Prerequisites verified on: {current_timestamp}
JDK 11: ✅ {version_info}
JDK 17: ✅ {version_info}  
JDK 21: ✅ {version_info}
Build Tool: ✅ {maven_or_gradle_version}
Git: ✅ {git_version}
Python: ✅ {python_version}
```

### If Tools Missing
- **JDKs**: Guide user to download from Eclipse Temurin and extract to `~/.olaf/jdk/{version}/`
- **Build Tools**: Direct to maven.apache.org or gradle.org
- **Git**: Direct to git-scm.com  
- **Python**: Direct to python.org

**ABORT migration if any essential tool is missing.** Provide clear installation guidance and ask user to re-run after installation.

## Input Parameters
If not provided, you MUST request these parameters:
- **execution_mode**: string|{"findings","migration"} - Where to look for the plan (REQUIRED; default: "findings")
- **migration_timestamp**: string - `YYYYMMDD-HHmm` identifying the migration directory under findings (REQUIRED if execution_mode=findings)
- **plan_dir**: string - Absolute or workspace-relative directory containing the plan (OPTIONAL; overrides the derived directory)
- **migration_project_slug**: string - Lowercase slug for migration layout `project-<slug>` (REQUIRED if execution_mode=migration and plan_dir not provided)
- **dry_run**: boolean - If true, simulate without changes (OPTIONAL; default: false)
- **commit_changes**: boolean - If true, create git commits per task update (OPTIONAL; default: true)

## Plan Discovery
- If `execution_mode = findings` (default):
  - Derive directory: `[id:findings_dir]migrations/migration_<migration_timestamp>/` unless `plan_dir` is provided.
  - Pick the lexicographically latest file matching `migration-plan-*.md` in that directory.
- If `execution_mode = migration`:
  - Derive directory: `migrate/java/project-<migration_project_slug>/` unless `plan_dir` is provided.
  - Pick the lexicographically latest file matching `java-migration-*.md` in that directory.
  - FAIL with a clear message if the directory or plan file is missing.
- You MUST also look for a context file in the same directory:
  - findings mode: `migration-bootstrap-context.yaml`
  - migration mode: `migration-bootstrap-context.yaml` (if present)

## Repository Resolution (STRICT)
When a task requires scanning or operating on the application repository (e.g., CI inventory, code searches), you MUST:
- Read `metadata.repository_path` from `migration-bootstrap-context.yaml` located in the plan directory.
- Use ONLY this absolute path as the repository root for all repository-related operations.
- NEVER infer, guess, or default to the workspace root or any other path.
- If `metadata.repository_path` is absent or empty, ABORT with a clear error: "Missing metadata.repository_path in migration-bootstrap-context.yaml".
- Log the resolved repository path in console outputs under Discovery details.

## File Conventions
- Plan files are UTF-8. Preserve trailing newline.
- Only mutate checklist lines; never alter ordering, IDs, or section structure.
- Task line pattern you MUST parse exactly:

## Task Directory Expectations
```
tasks/<phase-folder>/<task-id>-*/
  how-to.md  (standardized structure with Detection→Remediation→Validation workflow)
  *.ps1 / *.sh (automation scripts, optional; used only if how-to instructs)
  verify.*     (verification script, optional)
  remediation/ (remediation guidance files referenced by remediation keys)
```
- `{relative-task-path}` is resolved relative to the plan directory unless absolute.
- Each how-to contains: Goal, Prerequisites, Preferred/Fallback Approaches, Issue Detection & Remediation, Verification Commands, Success Criteria.

## Canonical Helper Tasks Resolution
When a plan's `{relative-task-path}` directory is missing, you MUST try to resolve a canonical helper task under `olaf-core/prompts/java-migration/tasks/` before failing.

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

## ⚠️ MANDATORY Baseline Validation Gate
**CRITICAL: This gate MUST be passed before Core Loop execution. NO EXCEPTIONS.**

### Baseline Gate Check (BLOCKING EXECUTION)
Before executing ANY migration tasks, you MUST verify:

1. **Check baseline marker**: Look for `baseline-validated-*.txt` in plan directory
2. **If marker exists**: Proceed to Core Loop immediately  
3. **If marker missing**: EXECUTE baseline validation below (MANDATORY)

### REQUIRED Baseline Validation Execution
**You MUST execute these steps. If ANY step fails, ABORT migration immediately:**

```bash
# Step 1: Read migration context (REQUIRED)
# From migration-bootstrap-context.yaml in plan directory:
# - detected.java_version (REQUIRED)
# - metadata.repository_path (REQUIRED)

# Step 2: Set correct JDK (MANDATORY)
export JAVA_HOME=~/.olaf/jdk/{detected.java_version}  # Linux/Mac
# OR: $env:JAVA_HOME = "$env:USERPROFILE\.olaf\jdk\{detected.java_version}"  # Windows

# Step 3: Navigate to project (REQUIRED)
cd {metadata.repository_path}

# Step 4: Validate compilation (BLOCKING - MUST succeed)
mvn clean compile -q
# IF EXIT CODE != 0: ABORT migration with message "Baseline compilation failed"

# Step 5: Validate tests (BLOCKING - MUST succeed)  
mvn test -q
# IF EXIT CODE != 0: ABORT migration with message "Baseline tests failed"
```

### Success Actions (MANDATORY)
If ALL validation steps succeed, you MUST create marker file:
`baseline-validated-{current_timestamp}.txt` containing:
```
BASELINE VALIDATION SUCCESS
Executed: {current_timestamp}
Java Version: {actual_java_version_from_java_-version}
Repository: {metadata.repository_path}
Compilation: SUCCESS
Tests: SUCCESS
Ready for migration tasks.
```

### Failure Actions (MANDATORY ABORT)
If ANY validation step fails, you MUST:
1. **IMMEDIATELY STOP** - Do not execute Core Loop
2. Create `baseline-validation-FAILED-{current_timestamp}.txt` with error details
3. **ABORT execution** with message: "MIGRATION BLOCKED: Original project has issues. Fix baseline before migration."
4. **DO NOT PROCEED** to Core Loop under any circumstances

## ⚠️ MANDATORY How-To Reading Protocol
**CRITICAL: You MUST read how-to guides before task execution. NO EXCEPTIONS.**

### How-To Reading Requirements (BLOCKING)
For EVERY task, you MUST:
1. **LOCATE how-to.md** in task directory (REQUIRED)
2. **READ ENTIRE how-to.md** file completely (MANDATORY)
3. **UNDERSTAND all sections**: Goal, Prerequisites, Steps, Verification (REQUIRED)
4. **FOLLOW how-to steps** in exact sequence (NO manual alternatives)
5. **IF how-to missing**: Use Canonical Helper Tasks Resolution or ABORT

**BLOCKING CONDITION**: You MUST NOT execute any task without reading its how-to guide first.

## Core Loop
**Prerequisites: Baseline validation gate MUST be passed first**

Repeat until no pending tasks or a failure occurs:
1. Locate plan directory and open the latest plan file according to Plan Discovery.
2. Find the first unchecked task line exactly matching `- [ ]` prefix.
3. Parse `{ID}`, `{Title}`, `{relative-task-path}` according to the line pattern.
4. **MANDATORY: Read how-to guide** (see How-To Reading Protocol above)
5. **EXECUTE task following how-to workflow (REQUIRED)**:
   - **Prerequisites**: Verify prerequisites are met; fail if not
   - **Preferred Approach**: Execute automated steps first; monitor for issues
   - **Issue Detection & Remediation**: Use Detection Patterns to identify issues; apply Remediation steps; validate fixes
   - **Verification**: Run Verification Commands; validate Success Criteria
   - **Fallback**: Use manual approach if preferred fails completely
   - **Issue Collection**: Create JSON only if remediation fails or deferred (format: `olaf-data/findings/migrations/migration_<ts>/collected-issues/<task-name>-<YYYYMMDD-HHmm>.json`)
   - **Missing How-To**: If how-to.md missing, use Canonical Helper Tasks Resolution (see above)
   - **No How-To Available**: If no how-to found anywhere, ABORT task with error: "No how-to guidance available for task {ID}"
   - **Legacy Fallback**: Only use AI-guided steps if explicitly documented as acceptable in how-to.md
6. On success: Mark `- [x]`; commit with `{ID}: {short action}` if `commit_changes=true`
7. On skip: Mark `- [-] (skip: reason)`; optionally commit
8. On failure: Do NOT modify checkbox; log under `### Failures`; stop execution

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
- Verification: run ALL Verification Commands from how-to; look for PASS/FAIL outputs; apply remediation if FAIL
- Issue Collection: create JSON files only when remediation fails, using exact format from how-to

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
- [ ] Tasks executed following how-to workflow (Prerequisites → Preferred → Detect/Remediate → Verify → Fallback if needed)
- [ ] All Verification Commands executed and passed
- [ ] Task status updated to [x] or [-] with reason
- [ ] Failures logged correctly when they occur
- [ ] Commits created as configured
- [ ] Completion block added when all tasks are done
- [ ] No unauthorized file changes made

## Error Handling
You WILL handle explicitly:
- **Missing Directory/Files**: show expected location; abort
- **Invalid Line Format**: show offending line; skip and continue
- **Task Directory Missing**: attempt Canonical Helper Tasks Resolution; if no suitable canonical task found, log failure and stop
- **Prerequisites Not Met**: log failure with specific missing prerequisite
- **Issue Detection**: apply how-to remediation patterns; collect JSON if remediation fails
- **Verification Failure**: attempt remediation; if still failing, log under Failures and stop
- **Script Execution Error**: capture exit code/output; attempt remediation if pattern matches; otherwise log and stop

⚠️ **Critical Requirements**
- NEVER reorder tasks or modify IDs/titles.
- ALWAYS preserve UTF-8 and trailing newline.
- ALWAYS ask confirmation before destructive changes unless `dry_run=true`.
- ALWAYS commit with clear messages when `commit_changes=true`.
- ALWAYS stop on first failure and log it.
