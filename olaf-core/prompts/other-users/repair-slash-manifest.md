---
name: repair-slash-manifest
description: Detect and repair orphaned manifest entries by validating competency references and cleaning broken links
tags: [slash-commands, repair, validation, cleanup]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

You WILL use terminal commands, not training data for timestamps.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **target_manifest**: string - Specific manifest to repair (OPTIONAL - will repair all if not provided)
- **dry_run**: boolean - Show what would be repaired without making changes (OPTIONAL, default: false)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for dry run analysis
- You WILL use Propose-Confirm-Act protocol for actual repairs due to file modification impact

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Check manifest directory exists: `[id:reference_dir].manifests/`
- Validate competency index access: `[id:competency_index]`
- Verify prompts directory structure: `[id:prompts_dir]`
- Scan for manifest files to process

### 2. Execution Phase

**Manifest Discovery:**
<!-- <manifest_scanning> -->
You WILL identify manifests to repair:
- Scan `[id:reference_dir].manifests/` for all `.json` files
- Filter to target_manifest if specified
- Validate JSON structure of each manifest
- Create repair queue with manifest priorities
<!-- </manifest_scanning> -->

**Competency Reference Validation:**
<!-- <competency_validation> -->
You WILL validate each manifest entry against competency index:
- Load current competency index: `[id:competency_index]`
- Extract all valid competency workflow paths
- Cross-reference manifest entries with valid paths
- Identify orphaned entries (manifest references non-existent competencies)
- Identify missing entries (competencies not in manifest but should be)
<!-- </competency_validation> -->

**Platform File Consistency Check:**
<!-- <platform_consistency> -->
You WILL verify platform file alignment:
- Check `.github/prompts/` for command files referenced in manifests
- Check `.windsurf/workflows/` for corresponding command files
- Identify missing platform files for manifest entries
- Identify orphaned platform files not in any manifest
- Report platform consistency issues
<!-- </platform_consistency> -->

**Repair Analysis:**
<!-- <repair_analysis> -->
You WILL categorize repair actions needed:
1. **Orphaned Manifest Entries**: Remove entries referencing non-existent competencies
2. **Missing Platform Files**: Regenerate missing command files
3. **Orphaned Platform Files**: Remove files not referenced in any manifest
4. **Corrupted Manifest Structure**: Fix JSON structure issues
5. **Inconsistent Naming**: Align command names with conventions
<!-- </repair_analysis> -->

**Repair Execution (if not dry run):**
<!-- <repair_execution> -->
You WILL execute repairs following user confirmation:
1. **Manifest Cleanup**: Remove orphaned entries from manifest files
2. **Platform File Cleanup**: Remove orphaned command files
3. **File Regeneration**: Create missing platform files from valid manifest entries
4. **Structure Validation**: Ensure all manifests have valid JSON structure
5. **Naming Consistency**: Apply correct naming conventions throughout
<!-- </repair_execution> -->

**Core Logic**: Execute following protocol requirements
- Apply appropriate interaction protocol based on dry_run parameter
- Provide comprehensive analysis before any modifications
- Execute repairs systematically with validation at each step
- Maintain backup information for rollback if needed

### 3. Validation Phase
You WILL validate repair results:
- Confirm all manifest entries reference valid competencies
- Verify platform file consistency across .github and .windsurf
- Check JSON structure validity of all repaired manifests
- Validate naming convention compliance

## Output Format
You WILL generate outputs following this structure:
- **Repair Analysis Report**: Detailed breakdown of issues found
- **Action Summary**: Specific repairs performed or recommended
- **Validation Results**: Post-repair consistency confirmation

## User Communication

### Progress Updates
- Manifest discovery and validation progress
- Competency reference checking status
- Platform consistency analysis results
- Repair execution progress (if not dry run)
- Timestamp identifier used: [YYYYMMDD-HHmm format]

### Completion Summary
- **For Dry Run**: Complete analysis of issues found without modifications
- **For Actual Repair**: Summary of repairs performed and validation results
- Manifest files processed and their status
- Platform files cleaned up or regenerated
- Overall system health assessment

### Next Steps
You WILL clearly define:
- System ready for normal slash command operations
- Recommendations for preventing future orphaned entries
- Suggested maintenance schedule for repair operations
- Instructions for manual verification if needed

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER remove entries from manifests without competency validation
- Rule 2: Platform file cleanup MUST maintain .github and .windsurf consistency
- Rule 3: Manifest JSON structure MUST be preserved during repairs
- Rule 4: Backup information MUST be available for rollback operations
- Rule 5: Naming convention repairs MUST follow established patterns
- Rule 6: Default manifest MUST be treated with extra caution

## Success Criteria
You WILL consider the task complete when:
- [ ] All manifest files scanned and validated
- [ ] Competency references verified against current index
- [ ] Platform file consistency confirmed
- [ ] Orphaned entries identified and processed
- [ ] Repair actions completed (if not dry run)
- [ ] Post-repair validation confirms system integrity
- [ ] User provided with comprehensive repair summary

## Required Actions
1. Discover and validate all manifest files in system
2. Cross-reference manifest entries with competency index
3. Analyze platform file consistency and identify issues
4. Execute repairs following appropriate interaction protocol
5. Validate system integrity post-repair

## Error Handling
You WILL handle these scenarios:
- **Manifest Directory Missing**: Report error and suggest system initialization
- **Corrupted Manifest JSON**: Attempt structure repair or request manual intervention
- **Competency Index Unavailable**: Report dependency issue and suggest resolution
- **Platform Directory Missing**: Create directories and report structural issues
- **File Permission Issues**: Provide specific error details and manual alternatives
- **Backup Creation Failures**: Warn user and request confirmation before proceeding
- **Partial Repair Completion**: Report incomplete operations and provide recovery steps
- **Validation Failures Post-Repair**: Rollback changes and request manual review

⚠️ **Critical Requirements**
- MANDATORY: Always validate competency references before removing manifest entries
- MANDATORY: Maintain platform consistency between .github and .windsurf
- NEVER remove manifest entries without confirming competency non-existence
- ALWAYS provide dry run analysis before actual repairs
- ALWAYS maintain backup information for rollback capability
- ALWAYS validate system integrity after repair operations
- ALWAYS report specific issues found and actions taken