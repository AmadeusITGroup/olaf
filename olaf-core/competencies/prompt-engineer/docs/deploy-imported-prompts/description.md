# Deploy Imported Prompts

**Source**: olaf-core/competencies/prompt-engineer/prompts/deploy-imported-prompts.md

## Overview

Deploy Imported Prompts (Phase 2) executes the approved migration plan created by Import Prompts To Competency. It converts external prompts to OLAF format, deploys them to target competencies, updates manifests, handles duplicates according to plan, and validates successful integration.

## Purpose

After analyzing and planning prompt migration, the actual conversion and deployment must be executed carefully and consistently. This competency solves the challenge of batch prompt migration by following the approved plan, ensuring all prompts are converted correctly, manifests are updated, and the migration is validated. It provides a controlled, traceable deployment process.

## Usage

**Command**: `deploy prompts`

**Protocol**: Propose-Confirm-Act

**When to Use**: Use this competency after completing Import Prompts To Competency analysis and receiving approval for the mapping plan. This is Phase 2 - the execution phase that actually converts and deploys prompts to OLAF competencies.

## Parameters

### Required Inputs
- **mapping_plan_path**: Path to the approved mapping plan from Phase 1
- **execution_mode**: How to execute ("sequential", "batch", "selective")

### Optional Inputs
- **selective_prompts**: Specific prompts to deploy (required if execution_mode="selective")
- **validation_level**: How thoroughly to validate ("basic", "standard", "comprehensive")
- **backup_originals**: Whether to backup source prompts (default: true)

### Context Requirements
- Approved mapping plan from Import Prompts To Competency
- Read access to source prompts
- Write access to target competency directories
- Access to prompt conversion tools
- Ability to update competency manifests

## Output

**Deliverables**:
- Converted and deployed prompts in target competencies
- Updated competency manifests with new entry points
- Deployment report with success/failure status
- Validation results for each deployed prompt
- Backup of original prompts (if backup_originals=true)

**Format**: Deployed prompts in `[competencies_dir]/[target_competency]/prompts/`, deployment report in `[findings_dir]/prompt-deployment-report-YYYYMMDD-HHmm.md`

## Examples

### Example 1: Deploying Full Migration Plan

**Scenario**: Executing approved plan to migrate 50 prompts from legacy system

**Command**:
```
olaf deploy prompts
```

**Input**:
- mapping_plan_path: "olaf-data/findings/prompt-import-analysis-20251027-1430.md"
- execution_mode: "batch"
- validation_level: "standard"
- backup_originals: true

**Result**: Deployed 50 prompts across 8 competencies, converted all to OLAF format, updated 8 competency manifests, handled 5 duplicates by merging, validated all deployments with 48 passing standard validation, flagged 2 for manual review, and created comprehensive deployment report.

### Example 2: Selective Deployment for Testing

**Scenario**: Deploying subset of prompts to test migration process

**Command**:
```
olaf deploy prompts
```

**Input**:
- mapping_plan_path: "olaf-data/findings/prompt-import-analysis-20251027-1430.md"
- execution_mode: "selective"
- selective_prompts: ["code-review", "generate-tests", "refactor-function"]
- validation_level: "comprehensive"

**Result**: Deployed 3 selected prompts to developer competency, performed comprehensive validation including compliance checking, confirmed all prompts meet OLAF standards, updated developer manifest, and generated detailed validation report for review before proceeding with full deployment.

## Related Competencies

- **Import Prompts To Competency**: Phase 1 - creates the mapping plan that this competency executes
- **Convert Prompt**: Used internally for individual prompt conversion
- **Check Prompt Compliance**: Validates deployed prompts meet OLAF standards
- **Generate Tutorial**: Create tutorials for newly deployed prompts

## Tips & Best Practices

- Always complete Phase 1 (Import Prompts) and get approval before deploying
- Use "selective" mode to test deployment with a few prompts first
- Use "comprehensive" validation for initial deployments, "standard" for routine migrations
- Always backup originals - you may need to reference them during troubleshooting
- Review deployment report carefully for any failures or warnings
- Test deployed prompts with real use cases before considering migration complete
- Update documentation and tutorials for deployed prompts
- Communicate deployment to team members who will use the new prompts
- Keep mapping plan and deployment report for audit trail

## Limitations

- Requires approved mapping plan from Phase 1 - cannot deploy without it
- Cannot automatically fix complex conversion issues - may need manual intervention
- Validation catches structural issues but not domain logic errors
- Duplicate handling follows plan - cannot make decisions during deployment
- Deployment is one-way - rollback requires manual restoration from backups
- Cannot deploy prompts with unresolved dependencies automatically
- Effectiveness depends on quality of Phase 1 analysis and mapping
