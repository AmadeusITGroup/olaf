---
name: verify-competency-compliance
description: Comprehensive verification of competency compliance with OLAF framework standards and templates
protocol: Analyze-Report
category: validation
tags: [compliance, verification, competency, standards]
---

# Verify Competency Compliance

## Objective

Perform comprehensive compliance verification of any competency within any competency pack to ensure adherence to OLAF framework standards, templates, and organizational requirements.

## Context

You are performing a thorough compliance check of a competency to validate that it follows all OLAF framework standards. This includes prompt compliance, manifest structure, documentation organization, and consistency between components.

## Inputs

**Required:**
- **Competency Path**: Full path to the competency directory to verify (e.g., `olaf-core/competencies/straf`)
- **Competency Name**: Name of the competency being verified

**Optional:**
- **Specific Check Focus**: Focus on specific compliance areas if needed (prompt, manifest, docs, consistency)

## Verification Process

### 1. Prompt Compliance Verification

For each prompt file in the competency's `prompts/` directory:
- Use the `check-prompt-compliance` competency from the prompt-engineer pack
- Verify each prompt follows OLAF prompt template structure
- Check for required metadata (name, description, protocol, category, tags)
- Validate protocol specification and format compliance
- Report any non-compliant prompts with specific issues

### 2. Manifest Template Compliance

Verify the competency manifest against the exact template:
- **Template Reference**: `olaf-core/competencies/competency-creation/templates/competency-manifest-template.json`
- Check all required fields are present
- Validate competencies array matches actual prompt files
- Verify entry_points array has entries for each competency
- Check protocol specifications in entry_points
- Validate aliases and descriptions format
- Confirm dependencies structure compliance

### 3. Documentation Structure Verification

For each competency listed in the manifest:
- Verify corresponding subfolder exists in `docs/` directory
- Check that subfolder name exactly matches competency ID from manifest
- Validate presence of required files in each subfolder:
  - `description.md` - must exist
  - `tutorial.md` - must exist

### 4. Description Template Compliance

For each `description.md` file:
- **Template Reference**: `olaf-core/competencies/olaf-specific-tools/templates/competency-description-template.md`
- Verify structure follows template exactly:
  - Overview section (2-3 sentences)
  - Purpose section (problem solved)
  - Usage section (command and protocol)
  - Parameters section (required/optional inputs)
  - Output section (deliverables and format)
  - Examples section (concrete examples)
  - Related Competencies section
  - Tips & Best Practices section
  - Limitations section
- Check that command matches entry_point file reference
- Validate protocol matches manifest entry

### 5. Tutorial Template Compliance

For each `tutorial.md` file:
- **Template Reference**: `olaf-core/competencies/prompt-engineer/templates/step-by-step-tutorial-template.md`
- Verify structure follows template:
  - Prerequisites section
  - Step-by-step instructions with numbered steps
  - User Action and System Response patterns
  - Verification checklist
- Check tutorial references correct competency command

### 6. Consistency Verification

Perform cross-component consistency checks:
- **Count Matching**: Verify same number of:
  - Prompt files in `prompts/` directory
  - Entries in `competencies` array in manifest
  - Subfolders in `docs/` directory
  - Entries in `entry_points` array in manifest

**If counts don't match**, analyze and categorize:
- **Orchestrator Pattern**: Check if competency uses orchestrator pattern with main entry point and implementation detail prompts
- **Implementation Details**: Identify prompts that are internal/utility functions not exposed as main competencies
- **Missing Documentation**: Identify competencies with prompts but missing docs
- **Orphaned Documentation**: Identify docs without corresponding prompts

## Output Format

Generate a comprehensive compliance report with the following structure:

```markdown
# Competency Compliance Report: [Competency Name]

**Verification Date**: [Date]
**Competency Path**: [Full Path]
**Overall Status**: [COMPLIANT | NON-COMPLIANT | PARTIALLY COMPLIANT]

## Summary

[Brief overview of compliance status and key findings]

## 1. Prompt Compliance Results

### Compliant Prompts ✅
- [prompt1.md]: All checks passed
- [prompt2.md]: All checks passed

### Non-Compliant Prompts ❌
- [prompt3.md]: 
  - Missing required metadata field: protocol
  - Description format non-compliant
- [prompt4.md]:
  - Invalid protocol specification

## 2. Manifest Compliance Results

**Status**: [COMPLIANT | NON-COMPLIANT]

### Issues Found:
- [Issue 1 with specific field reference]
- [Issue 2 with specific section]

## 3. Documentation Structure Results

**Status**: [COMPLIANT | NON-COMPLIANT]

### Missing Documentation:
- [competency-id]: Missing docs/[competency-id]/ directory
- [competency-id]: Missing description.md file

### Orphaned Documentation:
- docs/[folder-name]/: No corresponding prompt or manifest entry

## 4. Description Template Compliance

### Compliant Descriptions ✅
- [competency-id]: Follows template structure

### Non-Compliant Descriptions ❌
- [competency-id]:
  - Missing Overview section
  - Usage section format incorrect

## 5. Tutorial Template Compliance

### Compliant Tutorials ✅
- [competency-id]: Follows step-by-step template

### Non-Compliant Tutorials ❌
- [competency-id]:
  - Missing Prerequisites section
  - Step format non-standard

## 6. Consistency Analysis

**Prompt Files Count**: [X]
**Manifest Competencies Count**: [Y]
**Documentation Folders Count**: [Z]
**Entry Points Count**: [W]

### Analysis:
[If counts match: "All counts match - consistent structure"]
[If counts don't match: Detailed analysis of discrepancies and patterns]

### Competency Organization Pattern:
- **Pattern Detected**: [Standard | Orchestrator | Mixed]
- **Explanation**: [Details about organization approach]

## Recommended Actions

### Critical (Must Fix):
1. [Critical issue 1 with specific action]
2. [Critical issue 2 with specific action]

### Important (Should Fix):
1. [Important issue 1]
2. [Important issue 2]

### Optional (Nice to Have):
1. [Enhancement suggestion 1]
2. [Enhancement suggestion 2]

## Compliance Score

**Overall Score**: [X]/100
- Prompt Compliance: [X]/25
- Manifest Compliance: [X]/25  
- Documentation Structure: [X]/25
- Consistency & Organization: [X]/25
```

## Execution Notes

1. **Read All Files**: Access and analyze all relevant files within the competency
2. **Template References**: Always reference the exact template files mentioned above
3. **Cross-Reference**: Verify consistency between manifest, prompts, and documentation
4. **Pattern Recognition**: Identify organizational patterns and explain discrepancies contextually
5. **Actionable Recommendations**: Provide specific, implementable fixes for non-compliance

## Related Tools

- `check-prompt-compliance` (prompt-engineer): For individual prompt validation
- `validate-olaf-artifacts` (olaf-specific-tools): For broader OLAF artifact validation
- `generate-validation-report` (olaf-specific-tools): For reporting utilities