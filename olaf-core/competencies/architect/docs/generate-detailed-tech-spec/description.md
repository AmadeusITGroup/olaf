# Generate Detailed Tech Spec

## Overview

This competency creates comprehensive technical specification documents with detailed code examples and source references from a general technical specification. It analyzes the codebase to extract relevant components, documents implementation patterns, and produces detailed section-specific specifications that serve as authoritative technical documentation.

## Purpose

General technical specifications often lack the detailed code examples and implementation context needed by developers. This competency bridges that gap by automatically analyzing source code, extracting relevant components, and generating detailed documentation that includes actual code examples, architecture diagrams, design decisions, and precise source file references.

## Usage

**Command**: `generate detailed tech spec`

**Protocol**: Propose-Act

**When to Use**: Use this competency when you have a general technical specification that needs detailed implementation documentation, when onboarding new developers who need deep technical context, when documenting complex systems for knowledge transfer, or when creating comprehensive technical documentation for compliance or audit purposes.

## Parameters

### Required Inputs
- **spec_path**: Path to the parent technical specification document
- **application_name**: Name of the application (for file naming)
- **sections**: List of sections to detail (e.g., ["Error Handling", "Configuration", "Authentication"])

### Optional Inputs
- **focus_areas**: Specific aspects to emphasize in the documentation
- **output_dir**: Directory to save the detailed specs (default: `olaf-data/findings/detailed-specs/`)

### Context Requirements
- Access to the source codebase for component extraction
- General technical specification document should be accessible
- Technical specification templates automatically referenced from competency templates

## Output

This competency produces a comprehensive documentation package with detailed technical specifications for each requested section.

**Deliverables**:
- Detailed specification documents saved to `olaf-data/findings/detailed-specs/<application_name>-spec/`
- Section-specific markdown files with code examples and diagrams
- Cross-reference index linking specifications to source files

**Format**: Structured markdown documents with component overviews, code examples with context, architecture diagrams, source file references, and implementation patterns.

## Examples

### Example 1: Error Handling Documentation

**Scenario**: A development team needs detailed documentation of the error handling strategy for a microservices application to ensure consistent implementation across services.

**Command**:
```
olaf generate detailed tech spec
```

**Input**:
```
spec_path: /path/to/general-spec.md
application_name: PaymentService
sections: ["Error Handling"]
```

**Result**: Generated detailed error handling specification including:
- Custom exception class hierarchy with code examples
- Error response format standards with JSON schemas
- Logging strategy with actual logger configurations
- Error propagation patterns across service boundaries
- Source file references for each error handling component

### Example 2: Multi-Section Technical Documentation

**Scenario**: An architect needs comprehensive technical documentation for a new team taking over a legacy application.

**Command**:
```
olaf generate detailed tech spec
```

**Input**:
```
spec_path: /path/to/legacy-app-spec.md
application_name: LegacyApp
sections: ["Configuration", "Authentication", "Database Access", "API Integration"]
focus_areas: ["Security patterns", "Performance optimization"]
```

**Result**: Complete documentation package with four detailed specifications, each containing component breakdowns, code examples, architecture diagrams, and implementation guidance focused on security and performance.

## Related Competencies

- **analyze-technical-stack**: Use before this to understand the overall technology stack
- **bootstrap-functional-spec-from-code**: Complements this by extracting functional specifications
- **review-code**: Use to validate code examples and patterns documented
- **deepen-tech-spec-developer**: Alternative approach for developer-focused deep dives

## Tips & Best Practices

- Start with a clear general specification to guide the detailed documentation
- Focus on the most critical or complex sections first
- Review generated code examples for accuracy and relevance
- Use focus_areas to emphasize specific concerns (security, performance, maintainability)
- Organize output by feature or architectural layer for easier navigation
- Keep documentation in sync with code changes through regular regeneration
- Include both typical usage patterns and edge case handling

## Limitations

- Quality depends on code organization and existing documentation
- Cannot infer design intent not evident in the code
- May miss undocumented architectural decisions or rationale
- Code examples are extracted from existing implementation (may include technical debt)
- Requires access to complete source code for comprehensive documentation
- Does not replace human review for accuracy and completeness

---

**Source**: `olaf-core/competencies/architect/prompts/generate-detailed-tech-spec.md`
