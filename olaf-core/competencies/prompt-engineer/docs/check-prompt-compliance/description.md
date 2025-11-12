# Check Prompt Compliance

**Source**: olaf-core/competencies/prompt-engineer/prompts/check-prompt-compliance.md

## Overview

Check Prompt Compliance performs comprehensive analysis and validation of prompts against OLAF's template structure and prompting principles. It provides detailed compliance scoring, identifies gaps, and offers intelligent recommendations for improvement beyond basic template adherence.

## Purpose

Maintaining prompt quality and consistency is critical for OLAF's effectiveness. This competency solves the challenge of ensuring prompts meet all structural requirements, follow best practices, and provide excellent user experiences. It goes beyond simple checklist validation to provide intelligent analysis of execution feasibility, edge case coverage, and workflow integration.

## Usage

**Command**: `check prompt compliance`

**Protocol**: Act

**When to Use**: Use this competency after creating or modifying prompts to validate quality, during code reviews to ensure standards compliance, when troubleshooting prompt execution issues, or as part of regular quality assurance processes. It's essential for maintaining high standards across your prompt library.

## Parameters

### Required Inputs
- **target_prompt_path**: Path to the prompt file to analyze

### Optional Inputs
- **target_competency**: Competency the prompt belongs to (auto-detected from path if possible)
- **analysis_depth**: Level of detail ("summary", "detailed", "checklist") - default: "detailed"
- **output_format**: How to present results ("summary", "detailed", "checklist") - default: "detailed"

### Context Requirements
- Read access to target prompt file
- Access to OLAF prompt template and prompting principles
- Understanding of the prompt's intended use case for contextual analysis

## Output

**Deliverables**:
- Compliance score (0-100%) with category breakdown
- Detailed findings for each template section
- Principles adherence assessment with examples
- Enhanced critical analysis with intelligent recommendations
- Prioritized improvement roadmap

**Format**: Structured analysis report in markdown format, with format varying based on output_format parameter

## Examples

### Example 1: Quick Compliance Check

**Scenario**: You just created a new prompt and want to verify it meets basic standards

**Command**:
```
olaf check prompt compliance
```

**Input**:
- target_prompt_path: "olaf-core/competencies/developer/prompts/refactor-code.md"
- output_format: "summary"

**Result**: Received compliance score of 92%, identified that error handling section needs more edge cases, and confirmed all other template sections are present and well-structured.

### Example 2: Comprehensive Quality Audit

**Scenario**: Performing detailed review of a critical prompt before production release

**Command**:
```
olaf check prompt compliance
```

**Input**:
- target_prompt_path: "olaf-core/competencies/architect/prompts/design-system-architecture.md"
- analysis_depth: "detailed"
- output_format: "detailed"

**Result**: Generated comprehensive 5-page analysis including compliance score (88%), detailed section-by-section evaluation, principles adherence assessment, intelligent recommendations for improving user experience, edge case coverage analysis, and prioritized improvement roadmap with effort estimates.

## Related Competencies

- **Create Prompt**: Use this after creating prompts to validate they meet standards
- **Convert Prompt**: Run this after converting prompts to ensure conversion quality
- **Generate Tutorial**: Create tutorials for prompts that pass compliance checks
- **Condense Framework**: Use compliance checking to ensure condensed versions maintain quality

## Tips & Best Practices

- Run compliance checks immediately after creating or modifying prompts
- Use "summary" format for quick validation during development
- Use "detailed" format for comprehensive reviews before production deployment
- Pay special attention to enhanced analysis recommendations - they often identify non-obvious improvements
- Address high-priority compliance gaps before medium or low-priority enhancements
- Re-run compliance checks after making improvements to verify fixes
- Include compliance checking in your prompt review workflow

## Limitations

- Analysis is non-destructive and read-only (doesn't modify prompts)
- Cannot automatically fix identified issues (provides recommendations only)
- Quality of enhanced analysis depends on prompt's complexity and clarity
- Auto-detection of competency from path requires standard OLAF directory structure
- Cannot validate domain-specific logic accuracy (only structure and principles)
- Effectiveness depends on the clarity of the original prompt's intent
