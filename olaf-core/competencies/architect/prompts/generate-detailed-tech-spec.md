---
name: generate-detailed-tech-spec
description: Create comprehensive technical specification documents with code examples and source references from a general technical specification.
tags: [documentation, technical-spec, code-documentation, development]
---


## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

Use terminal commands, not training data.

Use terminal commands, not training data.

## Input Parameters
**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **spec_path**: string - Path to the parent technical specification
- **sections**: array[string] - List of sections to detail (e.g., ["Error Handling", "Configuration"])
- **application_name**: string - Name of the application (for file naming)
- **focus_areas**: array[string] - (Optional) Specific aspects to emphasize in the documentation
- **output_dir**: string - (Optional) Directory to save the detailed specs (default: `[id:findings_dir]detailed-specs/`)

## Process

1. **Initial Setup**:
   - Create job for tracking documentation work
   - Set up directory structure for outputs
   - Initialize documentation templates

2. **Source Code Analysis**:
   - Scan codebase for relevant components
   - Identify key classes and functions
   - Map relationships and dependencies
   - Extract code examples and patterns

3. **Documentation Generation**:
   - Create detailed section specifications
   - Include comprehensive code examples
   - Add architecture diagrams
   - Document design decisions
   - Link to source files

4. **Quality Assurance**:
   - Validate all code examples
   - Verify accuracy of references
   - Ensure consistency with general spec
   - Check for completeness

## Output/Result Format
- Markdown documents with:
  - Section overview and purpose
  - Component breakdowns
  - Code examples with context
  - Architecture diagrams
  - Source file references
  - Implementation patterns

## Output to USER
1. **Documentation Package**:
   - Main specification document
   - Supporting diagrams and assets
   - Code example repository
   - Cross-reference index

2. **Generation Report**:
   - Sections documented
   - Files analyzed
   - Issues encountered
   - Recommendations

## Domain-Specific Rules
- Rule 1: Include complete code examples
- Rule 2: Reference source files precisely
- Rule 3: Document design decisions
- Rule 4: Maintain traceability to requirements
- Rule 5: Use consistent terminology

## Required Actions
1. Analyze source code
2. Extract relevant components
3. Generate documentation
4. Validate accuracy
5. Package deliverables

## Documentation Structure
```
{output_dir}/
  ├── {application_name}-spec/
  │   ├── overview.md
  │   ├── section-1/
  │   │   ├── index.md
  │   │   ├── examples/
  │   │   └── diagrams/
  │   └── section-2/
  └── assets/
      ├── diagrams/
      └── code-samples/
```

## Code Example Format
````markdown
### Component: {ComponentName}

**Purpose**: Brief description of the component's role

**Source File**: `path/to/component.js`

**Implementation**:
```javascript
// Example code with comments
export class ComponentName {
  // Implementation details
}
```

**Key Points**:
- Important notes about the implementation
- Performance considerations
- Dependencies and relationships
````

⚠️ **Critical Notes**
- Never expose sensitive information in examples
- Keep documentation in sync with code
- Include version information
- Document assumptions and limitations
- Provide context for complex implementations   