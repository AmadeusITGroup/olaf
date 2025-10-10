---
name: java-migration-bootstrap
description: Interactive Phase 0 bootstrap to analyze a Java repo and generate migration context + migration plan scaffold
tags: [java, migration, bootstrap, spring-boot]
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


## Input Parameters
You MUST request these parameters if not already provided:
- **repository_path**: string - Absolute or workspace-relative path to Java project (REQUIRED)
- **planning_timestamp**: string from the current time (REQUIRED)
- **target_java_version**: string|{"17","21"} - Target Java LTS (REQUIRED)
- **target_boot_version**: string|semantic|'latest'|'latest-lts' - Target Spring Boot (REQUIRED)
- **include_modernization_catalog**: boolean - Include advisory modernization catalog (OPTIONAL, default: false)
- **reuse_flag**: boolean - Persist generated artifacts (OPTIONAL, default: true)

## User Interaction Protocol
You MUST use Propose-Confirm-Act for any file generation/overwrite.
Sequence:
1. Collect + validate inputs.
2. Detect current state.
3. Present detection + proposed targets.
4. Resolve symbolic versions.
5. Present phases, risks, artifact plan.
6. Request confirmation to generate.
7. Generate artifacts or allow edits.

## Output Location Policy
You MUST create and use directory: `[id:findings_dir]migrations/<migration_YYYYMMDD-HHMM/`
- Context file path: `[id:findings_dir]migrations/<migration_YYYYMMDD-HHMM/migration-bootstrap-context.yaml`
- Plan file path: `[id:findings_dir]migrations/<migration_YYYYMMDD-HHMM/migration-plan-<YYYYMMDD-HHMM>.md`
You MUST NOT write artifacts elsewhere.
If directory exists: prompt to overwrite or choose new timestamp.

## Process
### 1. Validation Phase
You WILL:
- Prompt: "Enter repository path to analyze:" until existing path resolves.
- Verify `pom.xml` or `build.gradle[.kts]` present; otherwise re-prompt.

- Detect current state:
  - java_version
  - spring_boot_version
  - build_tool
  - module_count
  - packaging (jar/war)
  - frameworks (spring-security, hibernate, actuator, etc.)
  - junit_version (4 or 5)
  - javax_imports_count (recursive *.java)
  - optional dependency summary
- Present detection summary table.
- Prompt target_java_version (17/21) loop until valid.
- Prompt target_boot_version (semantic or symbolic).
- Prompt include_modernization_catalog (yes/no).
- Resolve symbolic Spring Boot versions to concrete (on failure request explicit version).
- Compute phases:
  - Phase 1 if Java < 17 or Boot < 2.7
  - Phase 2 if target Boot >= 3.x OR javax_imports_count > 0
  - Phase 3 if target Java = 21
- Risk heuristics:
  - javax: 0 LOW, 1–50 MEDIUM, >50 HIGH
  - JUnit4 present => elevate to at least MEDIUM
  - war packaging => elevate 1 level
  - module_count >5 => elevate 1 level
- Present risk factors + overall risk.
- Show proposed artifact directory + file names.
- Ask for confirmation to proceed.

### 2. Execution Phase (Bootstrap Tasks B.0–B.7)
B.0 Repository Path: loop until valid; record absolute.
B.0.a Planning Timestamp: loop until valid; store planning_timestamp + derive `<ts>`.
B.1 Validate Repository: confirm build tool + packaging; else re-prompt path.
B.2 Detect Current State: gather metrics; mark unknown if failing (do not abort unless path invalid).
B.3 Prompt Targets: gather target Java, Spring Boot, modernization flag.
B.4 Resolve Targets: replace 'latest'/'latest-lts' with concrete; reconfirm.
B.5 Generate Context: write migration-bootstrap-context.yaml with sections:
  metadata: project_name, repository_path, planning_timestamp, generated_at(runtime clock), output_dir
  detected: all metrics
  targets: java, spring_boot, modernization_catalog_included
  phases: list {id, required, reason}
  risks: overall_level, factors[]
  migration_path: narrative string
B.6 Generate Migration Plan: scaffold from `migrate/bootstrap/java-migration-yyyymmdd-hhmm.md` replicating ALL headings, tables, checklists, risk sections, appendix, footer lines EXACT order.
  - Reset task statuses to [ ] (or [-] with reason for skipped phases).
  - Insert dynamic values (current vs target versions, risk classification, phase inclusion/skips, branch/tag names, dependency table).
  - Preserve section ordering and include every original task entry.
B.7 Next Steps: if any blocking issues (unresolved version, missing build file earlier) mark warnings; else provide migration branch creation + initial task.

### 3. Validation Phase
You WILL verify:
- Directory `[id:findings_dir]migrations/<migration_YYYYMMDD-HHMM/` exists.
- Both files created & readable.
- Context contains all mandatory keys.
- Plan includes every original heading & task from template.
- All symbolic versions resolved.
- Every task has status token ([ ], [-], [!], [x]).
- Phases correctly flagged required/skipped with reasons.

## Plan Template Scaffolding Rules
You MUST:
- Load `bootstrap/bootstrap-task-list.md` for task ordering & semantics.
- Load `bootstrap/java-migration-yyyymmdd-hhmm.md` as canonical migration plan template.
- Reproduce ALL sections verbatim before customization.
- Do NOT omit any section (Executive Summary through End footer).
- Keep task IDs & structure; only adjust status, dynamic values, and skipped annotations.

## Output Format
Console Outputs:
- Detection Summary Table
- Resolved Targets + Phase List
- Risk Overview
- Artifact Paths
Files:
- `[id:findings_dir]migrations/<ts>/migration-bootstrap-context.yaml`
- `[id:findings_dir]migrations/<ts>/migration-plan-<YYYYMMDD-HHMM>.md`

## User Communication
### Progress Updates
- Path validation status
- Detection metrics summary
- Target resolution confirmation
- Phase & risk summary
- Artifact generation confirmation or error details
### Completion Summary
- File paths
- Phase readiness state
- Next actionable command
### Next Steps
- If blockers: remediation instructions
- Else: branch creation, run migration execution prompt/workflow.

## Domain-Specific Rules
You MUST:
- Enforce strict validation loops for all inputs.
- Never generate artifacts without explicit confirmation.
- Only use the two source files (`bootstrap-task-list.md` and `java-migration-yyyymmdd-hhmm.md`) for plan scaffolding.
- Always include all phases; mark unused with [-] reason.
- Never leave symbolic versions in outputs.
- Always write artifacts under `[id:findings_dir]migrations/<ts>/`.

## Success Criteria
You WILL consider task complete when:
- [ ] Inputs validated & confirmed
- [ ] Detection metrics gathered (unknowns annotated)
- [ ] Targets resolved to concrete versions
- [ ] Phases & risks computed
- [ ] User confirmation obtained pre-write
- [ ] Context file created with required sections
- [ ] Plan file created replicating canonical template fully
- [ ] All tasks have status tokens
- [ ] Artifacts stored under correct directory
- [ ] Next steps communicated clearly

## Required Actions
1. Collect & validate inputs
2. Detect state
3. Resolve targets & compute phases/risks
4. Confirm with user
5. Generate context & plan under findings migrations directory
6. Validate artifacts
7. Provide next steps or remediation

## Error Handling
You WILL handle:
- **Invalid Path**: explain & re-prompt
- **Missing Build File**: re-prompt or abort gracefully
- **Invalid Timestamp Format**: show expected pattern & re-prompt
- **Version Resolution Failure**: request explicit version
- **Artifact Directory Exists**: prompt overwrite or new timestamp
- **File Write Error**: show error & remediation (permissions/path)
- **Detection Partial Failure**: mark unknown fields, continue
- **User Declines Generation**: offer edit or cancel
- **Template Load Failure**: mark B.6 [!], still write context
- **Unexpected Exception**: concise message + safe retry option

⚠️ **Critical Requirements**
- MANDATORY: Propose-Confirm-Act before file writes
- MANDATORY: Concrete versions only
- MANDATORY: Replicate all template sections & tasks exactly
- NEVER skip B.0–B.7 order
- NEVER write outside findings migrations directory
- ALWAYS validate artifacts after creation
- ALWAYS include reasons for skipped phases
