# Generate Tutorial

**Source**: olaf-core/competencies/prompt-engineer/prompts/generate-step-by-step-tutorial.md

## Overview

Generate Tutorial creates comprehensive step-by-step tutorial documents from conversations, workflow files, or prompt files. It extracts workflow steps, identifies prerequisites, and structures them into clear, actionable tutorials following OLAF's tutorial template with verification checklists and troubleshooting guidance.

## Purpose

Documentation is essential for user adoption and success, but creating detailed tutorials is time-consuming. This competency solves the challenge of transforming technical workflows and conversations into structured, user-friendly tutorials. It ensures consistency across all OLAF documentation while capturing the practical knowledge embedded in actual usage patterns.

## Usage

**Command**: `generate tutorial`

**Protocol**: Propose-Act

**When to Use**: Use this competency after creating new prompts or workflows to document their usage, when onboarding new team members who need step-by-step guidance, after completing complex tasks that should be repeatable, or when consolidating tribal knowledge into formal documentation.

## Parameters

### Required Inputs
- **source_type**: Source of workflow to document ("current_conversation" or "file")
- **workflow_name**: Name of the workflow/process being documented
- **source_file**: Path to file containing workflow (required if source_type="file")

### Optional Inputs
- **target_language**: Language for tutorial content (English, French, Spanish, German) - default: English
- **tutorial_title**: Custom title for the tutorial (auto-generated if not provided)

### Context Requirements
- Access to source content (current conversation or specified file)
- Read access to tutorial template
- Write access to findings directory for output
- Terminal access for timestamp generation

## Output

**Deliverables**:
- Complete step-by-step tutorial following OLAF template
- Prerequisites section with setup requirements
- Verification checklist with measurable success criteria
- Troubleshooting section for common issues
- Timeline expectations based on workflow complexity

**Format**: Markdown file saved to `[findings_dir]/[workflow-name]-tutorial-YYYYMMDD-HHmm.md`

## Examples

### Example 1: Documenting a Prompt Creation Workflow

**Scenario**: You just completed creating a new prompt and want to document the process

**Command**:
```
olaf generate tutorial
```

**Input**:
- source_type: "current_conversation"
- workflow_name: "creating-custom-prompts"
- target_language: "English"

**Result**: Generated a comprehensive tutorial with 8 steps covering prompt creation from requirements gathering to manifest updates, including verification checklist, troubleshooting tips for common issues, and estimated 30-minute completion time.

### Example 2: Creating Tutorial from Workflow File

**Scenario**: You have a documented workflow for setting up OLAF and need a user-friendly tutorial

**Command**:
```
olaf generate tutorial
```

**Input**:
- source_type: "file"
- source_file: "docs/workflows/olaf-setup-workflow.md"
- workflow_name: "olaf-installation-setup"
- target_language: "English"
- tutorial_title: "Getting Started with OLAF: Complete Setup Guide"

**Result**: Created a detailed tutorial with prerequisites (Python 3.6+, Git, IDE), 12 step-by-step instructions with specific commands, verification checklist for each major milestone, troubleshooting section for installation issues, and 45-minute estimated completion time.

## Related Competencies

- **Create Prompt**: Generate tutorials for newly created prompts to document their usage
- **Generate Workflow**: Create workflows first, then generate tutorials from them
- **Check Prompt Compliance**: Ensure prompts are compliant before documenting them in tutorials
- **Create Competency Package**: Generate tutorials for all entry points in new competency packages

## Tips & Best Practices

- Use "current_conversation" source when you've just completed a workflow interactively
- Use "file" source when you have pre-documented workflows or specifications
- Provide descriptive workflow names that clearly indicate what the tutorial covers
- Review generated tutorials for accuracy and completeness before sharing
- Include specific commands, file paths, and expected outputs for clarity
- Test tutorials with new users to identify gaps or unclear instructions
- Update tutorials when workflows change to keep documentation current

## Limitations

- Quality depends on clarity and completeness of source content
- Cannot infer missing steps or prerequisites not present in source
- Requires human review for domain-specific accuracy
- Auto-generated troubleshooting may not cover all edge cases
- Timeline estimates are approximate and may vary by user experience level
- Limited to supported languages (English, French, Spanish, German)
