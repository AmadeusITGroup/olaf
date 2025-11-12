# Create Prompt

**Source**: olaf-core/competencies/prompt-engineer/prompts/create-prompt.md

## Overview

Create Prompt is a comprehensive competency that generates new structured prompts following OLAF's established template and best practices. It guides you through the entire prompt creation lifecycle, from initial requirements gathering to manifest updates and competency index reindexing.

## Purpose

Creating high-quality, consistent prompts is essential for maintaining OLAF's effectiveness and reliability. This competency solves the challenge of ensuring all prompts follow the same structure, use imperative language consistently, include comprehensive error handling, and integrate seamlessly with the OLAF framework. It eliminates the guesswork from prompt engineering by providing a structured, validated approach.

## Usage

**Command**: `create prompt`

**Protocol**: Propose-Confirm-Act

**When to Use**: Use this competency whenever you need to create a new prompt for any OLAF competency pack. It's particularly valuable when you want to ensure your prompt follows all OLAF standards, includes proper error handling, and integrates correctly with the manifest system.

## Parameters

### Required Inputs
- **user_request**: The requirement or task description that the new prompt should address
- **prompt_name**: Desired name for the prompt (max 4 words, kebab-case format)
- **target_competency**: The competency pack where the prompt will be created (selected from available options)

### Optional Inputs
None - all parameters are required for proper prompt creation

### Context Requirements
- Access to OLAF competencies directory structure
- Read access to prompt templates and prompting principles
- Write access to target competency's prompts folder and manifest file
- Terminal access for timestamp generation

## Output

**Deliverables**:
- Complete structured prompt file following OLAF template
- Updated competency manifest with new entry point
- Validation checklist confirming template compliance
- Optional: Updated competency index (if user approves reindexing)

**Format**: Markdown file with YAML frontmatter, saved to `[competencies_dir]/[target_competency]/prompts/[prompt_name].md`

## Examples

### Example 1: Creating a Code Review Prompt

**Scenario**: You need a new prompt for the developer competency that performs comprehensive code reviews

**Command**:
```
olaf create prompt
```

**Input**:
- user_request: "Create a prompt that reviews code for quality, security, and best practices"
- prompt_name: "review-code-quality"
- target_competency: "developer"

**Result**: Generated a complete prompt file with all required sections (Time Retrieval, Input Parameters, Process phases, Error Handling, Success Criteria), updated the developer manifest with the new entry point and aliases, and offered to reindex the competency collection.

### Example 2: Creating a Documentation Generator

**Scenario**: You want to add a documentation generation capability to the technical-writer competency

**Command**:
```
olaf create prompt
```

**Input**:
- user_request: "Generate API documentation from code comments and type definitions"
- prompt_name: "generate-api-docs"
- target_competency: "technical-writer"

**Result**: Created a structured prompt with comprehensive input validation, multi-phase execution process, and detailed error handling. Updated technical-writer manifest and reindexed the collection to make the new prompt immediately discoverable.

## Related Competencies

- **Convert Prompt**: Use this to migrate existing prompts to OLAF structure before creating new ones based on them
- **Check Prompt Compliance**: Run this after creating a prompt to validate it meets all quality standards
- **Generate Tutorial**: Create step-by-step tutorials for your newly created prompts to help users understand how to use them
- **Create Competency Package**: Use this when you need to create an entire new competency pack to house your prompts

## Tips & Best Practices

- Choose descriptive, action-oriented prompt names that clearly indicate what the prompt does
- Keep prompt names concise (max 4 words) to maintain readability and ease of invocation
- Review the target competency's existing prompts before creating to avoid duplication
- Always approve the reindexing step to make your new prompt immediately discoverable
- Use the Propose-Confirm-Act protocol to review the generated prompt before saving
- Ensure your user_request is clear and specific to get the best prompt generation results

## Limitations

- Requires write access to the target competency's directory structure
- Cannot create prompts in non-existent competency packs (use Create Competency Package first)
- Prompt names must follow kebab-case convention with max 4 words
- Reindexing requires Python environment and access to select_collection.py script
- Generated prompts still require human review for domain-specific logic accuracy
