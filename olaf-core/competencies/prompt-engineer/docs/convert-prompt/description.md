# Convert Prompt

**Source**: olaf-core/competencies/prompt-engineer/prompts/convert-prompt-existing.md

## Overview

Convert Prompt transforms existing prompts from any format into OLAF's standardized template structure. It analyzes the original prompt's intent, extracts key components, and restructures them to follow OLAF conventions while preserving the original functionality and improving clarity.

## Purpose

Many teams have valuable existing prompts that don't follow OLAF's structured format. This competency solves the challenge of migrating legacy prompts without losing their effectiveness. It ensures consistency across your prompt library by converting diverse prompt styles into a unified, maintainable structure that includes proper error handling, success criteria, and user communication patterns.

## Usage

**Command**: `convert prompt`

**Protocol**: Propose-Act

**When to Use**: Use this competency when you have existing prompts that need to be migrated to OLAF format, when importing prompts from external sources, or when refactoring old prompts to meet current OLAF standards. It's particularly useful during initial OLAF adoption or when consolidating prompts from multiple sources.

## Parameters

### Required Inputs
- **source_prompt_path**: Path to the existing prompt file that needs conversion
- **target_competency**: The competency pack where the converted prompt will be saved
- **new_prompt_name**: Desired name for the converted prompt (kebab-case, max 4 words)

### Optional Inputs
- **preserve_original**: Whether to keep the original prompt file (default: true)
- **conversion_notes**: Specific aspects to preserve or modify during conversion

### Context Requirements
- Read access to source prompt file
- Write access to target competency's prompts folder
- Access to OLAF prompt template and prompting principles
- Understanding of the original prompt's purpose and usage

## Output

**Deliverables**:
- Converted prompt file following OLAF template structure
- Conversion report detailing changes made
- Updated competency manifest with new entry point
- Original prompt preserved (if preserve_original=true)

**Format**: Markdown file with YAML frontmatter, saved to `[competencies_dir]/[target_competency]/prompts/[new_prompt_name].md`

## Examples

### Example 1: Converting a Simple Task Prompt

**Scenario**: You have a basic prompt that generates unit tests but lacks structure

**Command**:
```
olaf convert prompt
```

**Input**:
- source_prompt_path: "legacy-prompts/test-generator.txt"
- target_competency: "developer"
- new_prompt_name: "generate-unit-tests"

**Result**: Converted the simple prompt into a structured OLAF prompt with proper phases (Validation, Execution, Validation), added comprehensive error handling, created success criteria checklist, and integrated it into the developer competency manifest.

### Example 2: Migrating External Prompt Library

**Scenario**: Importing a well-designed prompt from another framework

**Command**:
```
olaf convert prompt
```

**Input**:
- source_prompt_path: "external/code-analyzer.md"
- target_competency: "architect"
- new_prompt_name: "analyze-code-structure"
- conversion_notes: "Preserve the detailed analysis sections and add OLAF error handling"

**Result**: Successfully migrated the external prompt while preserving its analytical depth, added OLAF-standard error handling scenarios, restructured into proper phases, and updated the architect manifest.

## Related Competencies

- **Create Prompt**: Use this when you need to create entirely new prompts rather than converting existing ones
- **Check Prompt Compliance**: Run this after conversion to validate the converted prompt meets all OLAF standards
- **Import Prompts To Competency**: Use this for batch analysis and planning when converting multiple prompts
- **Deploy Imported Prompts**: Use this for batch conversion of multiple prompts following an approved mapping plan

## Tips & Best Practices

- Review the original prompt thoroughly before conversion to understand its intent and usage patterns
- Preserve the core logic and domain expertise from the original prompt
- Use conversion_notes to specify particular aspects that must be maintained
- Always validate the converted prompt with Check Prompt Compliance after conversion
- Test the converted prompt with real use cases to ensure functionality is preserved
- Keep the original prompt file for reference during testing and validation

## Limitations

- Cannot automatically infer missing information (e.g., proper error handling if not in original)
- Requires human judgment for complex prompts with ambiguous instructions
- May need manual refinement for prompts with highly specialized domain logic
- Cannot convert prompts that rely on framework-specific features not available in OLAF
- Conversion quality depends on the clarity and structure of the original prompt
