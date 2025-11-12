# Select Competency Collection

**Source**: olaf-core/competencies/prompt-engineer/prompts/select-competency-collection.md

## Overview

Select Competency Collection allows users to choose and activate specific OLAF competency collections based on their persona or team needs. It updates the framework to load only relevant competencies, optimizing context usage and improving discoverability of appropriate capabilities.

## Purpose

OLAF contains numerous competencies across many domains, but users typically need only a subset relevant to their role. This competency solves the challenge of managing competency visibility and framework efficiency by allowing persona-based or custom collection selection. It ensures users see only relevant capabilities while maintaining optimal framework performance.

## Usage

**Command**: `select collection`

**Protocol**: Act

**When to Use**: Use this competency during initial OLAF setup to configure your persona, when switching between different roles or projects, when creating custom collections for team-specific needs, or when optimizing framework performance by reducing loaded competencies.

## Parameters

### Required Inputs
- **collection_name**: Name of the collection to activate (or "custom" for custom selection)

### Optional Inputs
- **custom_competencies**: List of specific competencies to include (required if collection_name="custom")
- **update_index**: Whether to regenerate competency index after selection (default: true)

### Context Requirements
- Access to collection definitions
- Write access to framework configuration files
- Python environment for running select_collection.py script
- Understanding of available collections and competencies

## Output

**Deliverables**:
- Updated framework configuration with selected collection
- Regenerated competency index (if update_index=true)
- Updated condensed framework with relevant competencies
- Collection activation confirmation

**Format**: Updated configuration files and regenerated framework components

## Examples

### Example 1: Selecting Developer Collection

**Scenario**: Setting up OLAF for software development work

**Command**:
```
olaf select collection
```

**Input**:
- collection_name: "developer"
- update_index: true

**Result**: Activated developer collection including developer, architect, tester, git-assistant, and common competencies. Regenerated competency index with only relevant entry points. Updated condensed framework to include developer-focused patterns. Reduced framework size by 40% by excluding irrelevant competencies.

### Example 2: Creating Custom Collection for DevOps Team

**Scenario**: Building specialized collection for DevOps workflows

**Command**:
```
olaf select collection
```

**Input**:
- collection_name: "custom"
- custom_competencies: ["developer", "sre", "security-officer", "architect", "common"]
- update_index: true

**Result**: Created custom collection combining development, operations, and security competencies. Generated personalized competency index. Updated framework to load only specified competencies. Saved custom collection definition for team reuse.

### Example 3: Switching to Documentation Mode

**Scenario**: Transitioning from development to documentation tasks

**Command**:
```
olaf select collection
```

**Input**:
- collection_name: "technical-writer"

**Result**: Switched to technical-writer collection including technical-writer, researcher, developer (for code understanding), and common competencies. Reindexed framework to prioritize documentation-related capabilities. Updated query competency index for documentation-focused searches.

## Related Competencies

- **Create Competency Package**: Create packages that can be added to collections
- **Create Prompt**: Prompts in active collection are immediately discoverable
- **Condense Framework**: Collection changes trigger framework condensation
- **Generate Tutorial**: Document collection usage for team onboarding

## Tips & Best Practices

- Choose collections that match your primary role or project focus
- Use custom collections for specialized team workflows
- Always update the index after changing collections to ensure discoverability
- Review available collections before creating custom ones - standard collections may suffice
- Document custom collections for team consistency
- Switch collections when transitioning between different types of work
- Smaller collections improve framework performance and reduce context usage
- Test collection changes with common workflows to ensure needed competencies are included

## Limitations

- Requires Python environment and select_collection.py script
- Collection changes require framework reindexing (takes 1-2 minutes)
- Cannot have multiple collections active simultaneously
- Custom collections need manual maintenance when competencies change
- Switching collections doesn't preserve session context
- Collection definitions must exist before selection
- Some competencies (kernel) are always loaded regardless of collection
