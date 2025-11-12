# Import Prompts To Competency

**Source**: olaf-core/competencies/prompt-engineer/prompts/import-prompts-to-competency.md

## Overview

Import Prompts To Competency (Phase 1) analyzes external prompt collections and generates detailed mapping recommendations for OLAF competency integration. It examines prompt structure, identifies target competencies, detects duplicates, and creates a comprehensive migration plan for batch import operations.

## Purpose

Migrating multiple prompts from external sources or legacy systems is complex and error-prone. This competency solves the challenge of planning large-scale prompt migrations by providing intelligent analysis and mapping recommendations. It ensures prompts are organized correctly, duplicates are identified, and the migration plan is comprehensive before any changes are made.

## Usage

**Command**: `import prompts`

**Protocol**: Propose-Confirm-Act

**When to Use**: Use this competency when migrating prompt libraries from other frameworks, when consolidating prompts from multiple sources, when onboarding external prompt collections, or when planning large-scale reorganization of existing prompts. This is Phase 1 - analysis and planning only.

## Parameters

### Required Inputs
- **source_directory**: Path to directory containing prompts to import
- **analysis_scope**: What to analyze ("structure", "content", "both")

### Optional Inputs
- **target_competencies**: Suggested competencies for mapping (auto-detected if not provided)
- **duplicate_handling**: How to handle duplicates ("skip", "merge", "rename")
- **naming_convention**: Source naming convention to help with parsing

### Context Requirements
- Read access to source prompt directory
- Access to OLAF competencies directory for duplicate detection
- Understanding of source prompt structure and purpose
- Write access for generating mapping report

## Output

**Deliverables**:
- Comprehensive mapping report with recommendations
- Prompt-to-competency mapping table
- Duplicate detection results
- Conversion complexity assessment
- Estimated effort and timeline
- Approved migration plan ready for Phase 2 execution

**Format**: Markdown report saved to `[findings_dir]/prompt-import-analysis-YYYYMMDD-HHmm.md`

## Examples

### Example 1: Analyzing External Prompt Library

**Scenario**: Importing 50 prompts from a previous AI assistant framework

**Command**:
```
olaf import prompts
```

**Input**:
- source_directory: "external-prompts/legacy-assistant/"
- analysis_scope: "both"
- duplicate_handling: "merge"

**Result**: Generated comprehensive analysis identifying 50 prompts, mapped to 8 different OLAF competencies, detected 5 duplicates with existing OLAF prompts, assessed conversion complexity (12 simple, 28 moderate, 10 complex), estimated 40 hours for full migration, and created detailed mapping plan with recommendations.

### Example 2: Consolidating Team Prompts

**Scenario**: Bringing together prompts from 3 different team members into OLAF

**Command**:
```
olaf import prompts
```

**Input**:
- source_directory: "team-prompts/"
- analysis_scope: "both"
- target_competencies: ["developer", "architect", "tester"]
- duplicate_handling: "skip"

**Result**: Analyzed 35 prompts from team members, identified 8 duplicates across team members, mapped prompts to specified competencies, flagged 3 prompts needing new competency creation, generated mapping table with confidence scores, and created prioritized migration plan.

## Related Competencies

- **Deploy Imported Prompts**: Phase 2 - execute the migration plan created by this competency
- **Convert Prompt**: Used internally for individual prompt conversion during deployment
- **Create Competency Package**: Create new packages for prompts that don't fit existing competencies
- **Check Prompt Compliance**: Validate imported prompts after deployment

## Tips & Best Practices

- Analyze prompts thoroughly before attempting migration - planning prevents issues
- Use "both" analysis scope for comprehensive understanding
- Review duplicate detection carefully - some "duplicates" may have subtle differences
- Validate mapping recommendations against your understanding of prompt purposes
- Adjust target competencies if auto-detection seems incorrect
- Consider creating new competency packages for clusters of related prompts
- Document any special handling requirements in the mapping plan
- Get stakeholder approval on mapping plan before proceeding to Phase 2
- Use this for batch operations - for single prompts, use Convert Prompt directly

## Limitations

- Analysis only - does not modify or import prompts (use Deploy Imported Prompts for Phase 2)
- Quality of mapping depends on clarity of source prompt structure
- Cannot automatically determine optimal competency for ambiguous prompts
- Duplicate detection based on similarity - may miss semantic duplicates
- Requires human review and approval of mapping recommendations
- Cannot handle prompts with framework-specific dependencies automatically
- Effectiveness depends on source prompt documentation quality
