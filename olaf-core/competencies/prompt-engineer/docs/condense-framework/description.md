# Condense Framework

**Source**: olaf-core/competencies/prompt-engineer/prompts/condense-olaf-framework.md

## Overview

Condense Framework optimizes OLAF framework reference files by reducing token count while maintaining full functionality. It intelligently compresses verbose content, removes redundancy, and preserves critical structural markers to create efficient condensed versions suitable for LLM context windows.

## Purpose

LLM context windows are limited, and loading the full OLAF framework can consume significant tokens. This competency solves the challenge of fitting comprehensive framework guidance into constrained context budgets. It ensures the condensed framework retains all essential instructions, protocols, and patterns while dramatically reducing token consumption for faster loading and more efficient execution.

## Usage

**Command**: `condense olaf`

**Protocol**: Act

**When to Use**: Use this competency when updating OLAF framework components and need to regenerate the condensed version, when context window constraints require optimization, after adding new competencies that need to be included in the condensed framework, or when framework performance needs improvement.

## Parameters

### Required Inputs
- **source_framework_path**: Path to the full OLAF framework file to condense
- **target_output_path**: Where to save the condensed version

### Optional Inputs
- **compression_level**: How aggressively to compress ("conservative", "balanced", "aggressive") - default: "balanced"
- **preserve_sections**: Specific sections that must not be compressed
- **target_token_reduction**: Desired percentage reduction (e.g., 40 for 40% reduction)

### Context Requirements
- Read access to source framework files
- Write access to condensed framework output directory
- Understanding of framework structure and critical components
- Ability to validate condensed output maintains functionality

## Output

**Deliverables**:
- Condensed framework file with reduced token count
- Compression report showing token reduction achieved
- Validation checklist confirming all critical markers preserved
- Before/after comparison of key sections

**Format**: Markdown file saved to specified target_output_path, typically `olaf-core/reference/.condensed/olaf-framework-condensed.md`

## Examples

### Example 1: Standard Framework Condensation

**Scenario**: You've updated OLAF framework components and need to regenerate the condensed version

**Command**:
```
olaf condense olaf
```

**Input**:
- source_framework_path: "olaf-core/reference/olaf-framework-full.md"
- target_output_path: "olaf-core/reference/.condensed/olaf-framework-condensed.md"
- compression_level: "balanced"

**Result**: Reduced framework from 45,000 tokens to 18,000 tokens (60% reduction), preserved all XML markers and protocol definitions, maintained competency patterns, and validated that all critical instructions remain intact.

### Example 2: Aggressive Optimization for Mobile

**Scenario**: Creating ultra-compact version for mobile LLM deployment

**Command**:
```
olaf condense olaf
```

**Input**:
- source_framework_path: "olaf-core/reference/olaf-framework-full.md"
- target_output_path: "olaf-core/reference/.condensed/olaf-framework-mobile.md"
- compression_level: "aggressive"
- target_token_reduction: 70

**Result**: Achieved 72% token reduction (45,000 to 12,600 tokens), removed all examples and verbose explanations, preserved core protocols and patterns, maintained structural integrity, and validated functionality with test prompts.

## Related Competencies

- **Create Prompt**: Condensed framework is loaded when creating prompts to provide context
- **Check Prompt Compliance**: Uses condensed framework patterns for validation
- **Generate Workflow**: Condensed framework provides workflow templates and patterns
- **Select Competency Collection**: Triggers framework condensation when collections change

## Tips & Best Practices

- Always validate condensed framework with test prompts before deploying
- Use "balanced" compression for general use - it provides good reduction without sacrificing clarity
- Use "conservative" when framework changes are complex and need careful preservation
- Use "aggressive" only when token budget is extremely constrained
- Preserve critical XML markers and protocol definitions - they're essential for framework operation
- Test condensed framework with various competencies to ensure broad compatibility
- Keep backup of previous condensed version before regenerating
- Document any manual adjustments made after automated condensation

## Limitations

- Cannot add new functionality - only compresses existing content
- Aggressive compression may reduce clarity for human readers
- Requires validation to ensure no critical information lost
- May need manual refinement for optimal balance of size and functionality
- Cannot compress below certain threshold without losing essential instructions
- Effectiveness depends on redundancy and verbosity in source framework
