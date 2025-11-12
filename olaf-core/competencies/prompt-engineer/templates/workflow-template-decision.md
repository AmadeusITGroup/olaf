---
name: workflow-template-decision
description: Template for creating decision/switch-case workflows with conditional branching based on lookup tables
tags: [template, workflow, decision, conditional, branching, lookup-table]
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

Use terminal commands, not training data.

# Decision/Switch-Case Workflow Template

> **Note:** All files referenced below are either prompts located in `[id:competencies_dir][competency]/prompts/` or tools located in `[id:tools_dir]`, as specified in the memory map file.
> The solution to analyze is in `[id:core_dir]` and all new non-temporary created files are to be created in `[id:findings_dir]` folder.

# [WORKFLOW_NAME]: [WORKFLOW_DESCRIPTION]

## Template Variables
- `[WORKFLOW_NAME]`: Name of the workflow (kebab-case)
- `[WORKFLOW_DESCRIPTION]`: Brief description of workflow purpose
- `[decision_key_name]`: Name of the primary decision criteria
- `[previous-workflow-output-1]`, `[previous-workflow-output-2]`: Input files from previous workflows
- `[configuration-file]`: Configuration file for decision logic
- `[descriptive-decision-log-name]`: Name for decision log file
- `[descriptive-branch-output-name]`: Name for branch output file
- `[prompt-for-value1]`, `[prompt-for-value2]`, `[prompt-for-valueN]`: Branch-specific prompt names
- `[default-prompt]`: Default prompt when no match found
- `[source-file1]`, `[source-file2]`: Data source files for multi-criteria decisions

## Workflow Type
Decision/Switch-Case - Conditional branching based on data from previous workflow outputs using lookup tables

## Workflow Overview
[Brief description of what this workflow accomplishes through conditional logic]

## Prerequisites
- [List any required conditions before starting]
- [Dependencies on other workflows or files]
- [Required input files from previous workflows]

## Input Requirements
- **Decision Data Sources:** [List all files that contain decision criteria]
  - `[previous-workflow-output-1].[ext]` (JSON, CSV, XML, YAML, etc.)
  - `[previous-workflow-output-2].[ext]` (JSON, CSV, XML, YAML, etc.)
  - `[configuration-file].[ext]` (JSON, CSV, XML, YAML, etc.)
- **Decision Key:** `[specific-field-path-or-column]` from input files
- **Input Format:** Various formats supported (JSON, CSV, XML, YAML, text files)

## Output Specifications
- **Decision Log:** `[descriptive-decision-log-name].json`
- **Selected Branch Output:** `[descriptive-branch-output-name].json`
- **Output Location:** [id:findings_dir]

## Decision Logic

### Decision Lookup Table
```json
{
  "decision_table": {
    "[decision_key_name]": {
      "data_source": "[source-file].[ext]",
      "file_format": "[json|csv|xml|yaml|txt]",
      "field_path": "[path.to.decision.field]",
      "lookup_mappings": {
        "[value1]": {
          "prompt": "[id:competencies_dir][competency]/prompts/[prompt-for-value1].md",
          "description": "[What happens for value1]"
        },
        "[value2]": {
          "prompt": "[id:competencies_dir][competency]/prompts/[prompt-for-value2].md", 
          "description": "[What happens for value2]"
        },
        "[valueN]": {
          "prompt": "[id:competencies_dir][competency]/prompts/[prompt-for-valueN].md",
          "description": "[What happens for valueN]"
        },
        "default": {
          "prompt": "[id:competencies_dir][competency]/prompts/[default-prompt].md",
          "description": "[What happens when no match found]"
        }
      }
    }
  }
}
```

### Multi-Criteria Decision Table (Optional)
```json
{
  "multi_criteria_decision": {
    "criteria": [
      {
        "name": "[criterion1]",
        "data_source": "[source-file1].[ext]",
        "file_format": "[json|csv|xml|yaml|txt]",
        "field_path": "[path.to.field1]"
      },
      {
        "name": "[criterion2]", 
        "data_source": "[source-file2].[ext]",
        "file_format": "[json|csv|xml|yaml|txt]",
        "field_path": "[path.to.field2]"
      }
    ],
    "decision_matrix": {
      "criterion1_value_A__criterion2_value_X": {
        "prompt": "[id:competencies_dir][competency]/prompts/[prompt-for-combination-ax].md",
        "description": "[Description for criterion1=A and criterion2=X]"
      },
      "criterion1_value_A__criterion2_value_Y": {
        "prompt": "[id:competencies_dir][competency]/prompts/[prompt-for-combination-ay].md",
        "description": "[Description for criterion1=A and criterion2=Y]"
      },
      "criterion1_value_B__criterion2_value_X": {
        "prompt": "[id:competencies_dir][competency]/prompts/[prompt-for-combination-bx].md",
        "description": "[Description for criterion1=B and criterion2=X]"
      },
      "criterion1_value_B__criterion2_value_Y": {
        "prompt": "[id:competencies_dir][competency]/prompts/[prompt-for-combination-by].md",
        "description": "[Description for criterion1=B and criterion2=Y]"
      },
      "default": {
        "prompt": "[id:competencies_dir][competency]/prompts/[default-multi-criteria-prompt].md",
        "description": "[Default action when no combination matches]"
      }
    }
  }
}
```

## Template Validation
- All `[id:...]` references must exist in memory map
- Decision lookup tables must be properly structured
- All referenced prompt files must exist in `[id:competencies_dir][competency]/prompts/`
- Decision criteria fields must be accessible in input files
- Default branch must be defined for unmatched cases
- Multi-criteria decision matrices must cover all combinations
- JSON paths in lookup tables must be valid

## Workflow Steps

### Step 1: Decision Data Extraction
- **Action:** Read and extract decision criteria from input files
- **Input:** All specified decision data sources
- **Output:** `[decision-extraction].json`
- **Description:** Extract relevant decision values from previous workflow outputs

### Step 2: Decision Resolution
- **Action:** Apply lookup table logic to determine branch
- **Input:** `[decision-extraction].json` + Decision lookup table
- **Output:** `[decision-result].json`
- **Description:** Match extracted values against lookup table to select appropriate prompt/workflow

### Step 3: Branch Execution
- **Action:** Execute the selected prompt/workflow based on decision
- **Input:** Original workflow inputs + decision context
- **Output:** `[branch-execution-output].json`
- **Description:** Run the specific prompt or sub-workflow determined by the decision logic

## Decision Log Format
```json
{
  "decision_timestamp": "2025-07-28T14:00:00Z",
  "decision_criteria": {
    "[criterion1]": "[extracted_value1]",
    "[criterion2]": "[extracted_value2]"
  },
  "data_sources": [
    {
      "file": "[source-file1].[ext]",
      "format": "[json|csv|xml|yaml|txt]",
      "field": "[path.to.field]",
      "value": "[extracted_value]"
    }
  ],
  "selected_branch": {
    "lookup_key": "[matched_key]",
    "prompt": "[selected_prompt].md",
    "description": "[branch_description]"
  },
  "execution_result": {
    "success": true,
    "output_file": "[branch-output].json"
  }
}
```

## Data Flow Diagram
```
[Input Files] → [Extract Decision Data] → [Apply Lookup Table] → [Select Branch] → [Execute Branch] → [Branch Output]
     ↓                    ↓                       ↓                  ↓              ↓
[File1.json]      [Decision Data]        [Lookup Result]     [Selected Prompt]  [Final Output]
[File2.json]      [Extracted Values]     [Branch Choice]     [Branch Context]   [Decision Log]
[FileN.json]
```

## Error Handling
- **Missing Decision Data:** [What to do if required decision fields are missing]
- **No Lookup Match:** [How to handle values not in lookup table - use default]
- **Branch Execution Failure:** [What to do if selected branch fails]
- **Invalid Input Files:** [How to handle corrupted or missing input files]

## Common Error Patterns
- **Missing input files:** Check that previous workflows completed successfully
- **Unsupported file format:** Verify file format is supported (JSON, CSV, XML, YAML, TXT)
- **Invalid field paths:** Verify decision criteria paths exist in source files (adjust for file format)
- **Lookup table incomplete:** Ensure all possible values have corresponding branches
- **Prompt not found:** Verify all branch prompts exist in `[id:competencies_dir][competency]/prompts/`
- **Permission errors:** Check file access rights for input and output files
- **Invalid memory map ID:** Check reference exists in memory map file
- **Multi-criteria combination missing:** Ensure decision matrix covers all value combinations
- **Default branch not defined:** Always provide fallback for unmatched cases
- **File parsing errors:** Handle malformed files gracefully

## Validation
- [ ] All decision data sources accessible
- [ ] Decision criteria successfully extracted
- [ ] Lookup table match found (or default used)
- [ ] Selected branch executed successfully
- [ ] Decision log created and complete

## Next Steps
- [What happens after this workflow completes]
- [How the branch output feeds into subsequent workflows]
