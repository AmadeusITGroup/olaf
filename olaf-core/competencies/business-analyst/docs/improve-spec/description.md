# Improve Spec

## Overview

This competency enhances functional specifications by adding visual diagrams, detailed data definitions, and comprehensive terminology sections. It transforms text-heavy specifications into more accessible, visually clear documents that improve understanding and reduce ambiguity for all stakeholders.

## Purpose

Functional specifications often rely heavily on text descriptions, making them difficult to understand and prone to misinterpretation. This competency addresses this by systematically enhancing specifications with Mermaid diagrams for complex processes, structured data object tables with detailed attributes, and comprehensive glossaries that standardize terminology. The result is clearer communication and reduced implementation errors.

## Usage

**Command**: `improve spec`

**Protocol**: Propose-Act

**When to Use**: Use this competency when specifications are complete but difficult to understand, before sharing specifications with new team members or stakeholders, when preparing specifications for technical review, or when data models and terminology need standardization across the team.

## Parameters

### Required Inputs
- **spec_path**: Path to the existing functional specification to enhance

### Optional Inputs
- **output_path**: Path to save the enhanced specification (default: appends "_enhanced" to input filename)
- **focus_areas**: Specific aspects to enhance (diagrams, data_models, terminology; default: all)
- **mermaid_theme**: Theme for Mermaid diagrams (default: "default")

### Context Requirements
- Existing functional specification must be accessible
- Specification should have core content defined
- Works best with specifications that have clear structure and sections

## Output

This competency produces an enhanced version of the specification with visual and structural improvements.

**Deliverables**:
- Enhanced specification document saved to `olaf-data/findings/` with "_enhanced" suffix
- Embedded Mermaid diagrams for processes, architecture, flows, and state machines
- Structured data object tables with attributes, types, constraints, and examples
- Comprehensive terminology section with definitions and consistent usage

**Format**: Enhanced markdown document maintaining original structure but with added visual elements, formatted data tables, and glossary section. Includes enhancement report summarizing changes made.

## Examples

### Example 1: Complex Workflow Visualization

**Scenario**: A specification describes a multi-step approval workflow in text, but stakeholders struggle to understand the flow and decision points.

**Command**:
```
olaf improve spec
```

**Input**:
```
spec_path: olaf-data/specs/approval-workflow-spec.md
focus_areas: [diagrams]
```

**Result**: Added 4 Mermaid diagrams including workflow flowchart, state diagram for approval status, sequence diagram for system interactions, and context diagram showing external integrations. Specification readability significantly improved.

### Example 2: Data Model Documentation

**Scenario**: Specification mentions various data objects but lacks detailed attribute definitions, causing confusion during implementation.

**Command**:
```
olaf improve spec
```

**Input**:
```
spec_path: olaf-data/specs/customer-portal-spec.md
focus_areas: [data_models, terminology]
```

**Result**: Documented 8 data objects with complete attribute tables including types, constraints, validation rules, and example values. Added glossary defining 25 domain-specific terms and acronyms. Eliminated terminology inconsistencies across the document.

## Related Competencies

- **extend-specification**: Use before improving to ensure specification completeness
- **bootstrap-functional-spec-from-code**: Generate initial specification, then improve with visuals
- **analyze-business-requirements**: Validate requirements before investing in visual enhancements
- **create-architecture-diagram** (architect): Create complementary technical architecture diagrams

## Tips & Best Practices

- Focus on diagrams for complex processes that are hard to describe in text
- Use consistent diagram styling across all visuals in the specification
- Include example values in data tables to clarify expected formats
- Define acronyms and jargon on first use, then compile in glossary
- Maintain original content meaning—enhancements should clarify, not change
- Test diagram rendering in your markdown viewer before finalizing
- Use flowcharts for processes, sequence diagrams for interactions, state diagrams for status flows
- Keep data tables concise—use separate detailed documentation for complex data models
- Update terminology section as specification evolves to maintain consistency

## Limitations

- Cannot fix unclear or incorrect original content—only enhances presentation
- Diagram quality depends on clarity of original process descriptions
- May require manual diagram adjustments for optimal layout and readability
- Does not validate data model correctness or completeness
- Cannot infer missing information—only visualizes what's already documented
- Mermaid diagram complexity is limited—very complex diagrams may need external tools
- Does not replace technical data modeling or architecture documentation

---

**Source**: `olaf-core/competencies/business-analyst/prompts/improve-spec.md`
