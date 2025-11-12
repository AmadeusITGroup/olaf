# Prompt Engineer Competency Package

## Overview

This is a comprehensive, self-contained competency package that aggregates all prompt engineering capabilities, templates, best practices, and documentation into a unified, reusable system.

The package contains everything needed to:
- Create structured prompts following OLAF standards
- Test and validate prompts for compliance
- Convert existing prompts to template structure
- Generate tutorials and workflows
- Condense frameworks while maintaining functionality

## 📁 Package Structure

```
prompt-engineer/
├── prompts/                          # All executable prompt files
│   ├── create-prompt.md             # Generate new structured prompts
│   ├── convert-prompt-existing.md   # Refactor existing prompts
│   ├── test-prompt.md               # Analyze and validate prompts
│   ├── generate-step-by-step-tutorial.md  # Create tutorials
│   ├── condense-olaf-framework.md   # Compress framework files
│   └── generate-workflow.md         # Build structured workflows
│
├── templates/                        # Reusable templates and guides
│   ├── prompt-template.md           # Standard prompt structure template
│   ├── prompting-principles.md      # Best practices and principles
│   └── step-by-step-tutorial-template.md  # Tutorial generation template
│
├── docs/                             # Documentation
│   ├── README.md                    # This file
│   └── [other documentation]
│
├── examples/                         # Usage examples and samples
├── competency-manifest.json         # Competency metadata and configuration
├── dependencies.json                # External dependencies
└── README.md                        # Quick start guide
```

## 🚀 Quick Start

### Basic Prompt Creation
```markdown
User: "create prompt"
System: Guides you through creating a new structured prompt using the template
```

### Prompt Analysis
```markdown
User: "test prompt"
System: Analyzes existing prompt for compliance and improvement recommendations
```

### Workflow Generation
```markdown
User: "generate workflow"
System: Creates structured workflows from templates or specifications
```

## 📋 Core Competencies

### 1. **create-prompt.md**
Generate new structured prompts following OLAF template and principles.

**Protocol**: Propose-Confirm-Act  
**Key Features**:
- Template validation
- Duplicate detection
- Imperative language enforcement
- Comprehensive error handling
- Success criteria definition

**Usage**:
```
"create prompt"
- User request: [describe what you need]
- Prompt name: [kebab-case, max 4 words]
- Sub-category: [select from available]
```

### 2. **convert-prompt-existing.md**
Convert existing prompts to follow OLAF template structure.

**Protocol**: Propose-Act  
**Key Features**:
- Preserves original functionality
- Template compliance transformation
- Before/after comparison
- Conflict detection
- Original file preservation

**Usage**:
```
"convert prompt"
- Existing prompt path: [file to convert]
- Target sub-category: [select from available]
- Preserve original name: [yes/no]
```

### 3. **test-prompt.md**
Analyze prompts for template compliance and provide improvement recommendations.

**Protocol**: Act (for analysis) / Propose-Act (for improvements)  
**Key Features**:
- Template compliance scoring
- Principles adherence assessment
- Enhanced critical analysis
- Edge case identification
- Actionable improvement suggestions
- Multiple output formats (summary/detailed/checklist)

**Usage**:
```
"test prompt"
- Target prompt path: [file to analyze]
- Analysis depth: [basic/standard/comprehensive]
- Output format: [summary/detailed/checklist]
```

### 4. **generate-step-by-step-tutorial.md**
Generate step-by-step tutorials from conversations or workflow files.

**Protocol**: Act  
**Key Features**:
- Current conversation analysis
- File-based workflow documentation
- Multi-language support
- Template-based structure
- Verification checklists
- Troubleshooting sections

**Usage**:
```
"generate tutorial"
- Source type: [current_conversation/file]
- Source file: [path if file-based]
- Workflow name: [descriptive name]
- Target language: [English/French/Spanish/German]
```

### 5. **condense-olaf-framework.md**
Condense OLAF framework reference files while maintaining functionality.

**Protocol**: Propose-Confirm-Act  
**Key Features**:
- 70-80% compression ratio
- XML tag preservation
- Competency mapping extraction
- Memory map optimization
- Core rules consolidation

**Usage**:
```
"condense olaf"
- Automatically processes source files
- Validates compression and functionality
- Generates condensed framework file
```

### 6. **generate-workflow.md**
Create structured workflows from templates or specifications.

**Protocol**: Act  
**Key Features**:
- Multiple template types (sequential/iterative/decision/orchestrator)
- Interactive or specification-based mode
- Comprehensive error handling
- Framework validation integration
- Template-specific validation

**Usage**:
```
"generate workflow"
- Workflow type: [sequential/iterative/decision/orchestrator]
- Workflow name: [kebab-case]
- Description: [brief purpose]
- Mode: [interactive/specification]
```

## 📚 Templates and Principles

### Prompt Template
Standard structure for all OLAF prompts:
- Framework validation section
- Time retrieval (YYYYMMDD-HHmm format)
- Input parameters (REQUIRED/OPTIONAL)
- User interaction protocol
- Structured process (Validation/Execution/Validation)
- Output format specification
- User communication guidelines
- Domain-specific rules
- Success criteria
- Error handling
- Critical requirements

### Prompting Principles
Best practices for effective prompt engineering:
1. **Use Imperative Language** - "You WILL", "You MUST"
2. **Be Explicit with Success Criteria** - Define measurable outcomes
3. **Add Context** - Explain WHY instructions matter
4. **Structure with XML Markup** - Use tags for complex sections
5. **Include Error Handling** - Anticipate and address issues
6. **Clarity and Specificity** - Every instruction must be specific
7. **Progressive Disclosure** - Organize from high-level to detailed
8. **Consistency and Formatting** - Maintain uniform style

### Tutorial Template
Standardized structure for step-by-step documentation:
- Prerequisites
- Step-by-step instructions
- Expected outputs for each step
- Verification checklist
- Troubleshooting section
- Key learning points
- Next steps suggestions
- Expected timeline

## 🔧 Integration with OLAF

This competency integrates seamlessly with the OLAF framework:

### Memory Map References
```
prompts_dir = olaf-core/prompts/
templates_dir = olaf-core/templates/
reference_dir = olaf-core/reference/
findings_dir = olaf-data/findings/
```

### Interaction Protocols
All prompts follow OLAF's three-protocol system:
- **Act**: Direct execution (non-destructive operations)
- **Propose-Act**: Get agreement before major changes
- **Propose-Confirm-Act**: Plan → Review → Confirm → Execute

### Framework Validation
Every prompt includes:
- `<olaf-work-instructions>` framework validation
- `<olaf-general-role-and-behavior>` behavior guidelines
- `<olaf-interaction-protocols>` protocol specifications
- Time retrieval using terminal commands (not training data)

## 📋 Dependencies

### Required
- OLAF Framework v1.6.0 or higher
- File system access
- Terminal/shell access

### Optional
- Related competencies for extended workflows
- Development tools for integration testing

See `dependencies.json` for complete dependency list.

## 💡 Usage Examples

### Example 1: Create a New Prompt
```bash
User: create prompt

System: Let's create a new structured prompt. What is your requirement?
User: I need a prompt to analyze code quality

System: [guides through template completion]
System: Here's your generated prompt. Ready to save?
User: yes

System: Prompt saved to: olaf-core/prompts/developer/analyze-code-quality.md
```

### Example 2: Test and Improve
```bash
User: test prompt

System: Analyzing prompt for compliance...
System: Compliance Score: 87%
System: Found 3 improvement areas:
  1. Add more specific error handling examples
  2. Expand success criteria checklist
  3. Clarify XML tag structure

System: Would you like recommendations for improvement?
User: yes

System: [provides specific suggestions and implements fixes]
```

### Example 3: Generate Tutorial
```bash
User: generate tutorial

System: What workflow should we document?
User: The prompt-engineer competency creation workflow

System: [analyzes workflow]
System: Tutorial generated: findings/prompt-engineer-tutorial-20251021-1430.md
System: Tutorial includes 7 steps, verification checklist, and troubleshooting guide
```

## 🎯 Best Practices

1. **Always use the template** - Ensures consistency and quality
2. **Follow imperative language** - "You WILL" and "You MUST" for clarity
3. **Test before deployment** - Use test-prompt to validate
4. **Document edge cases** - Include error handling scenarios
5. **Provide examples** - Make success criteria concrete
6. **Use XML markup** - For complex sections requiring clarity
7. **Validate outputs** - Verify generated prompts meet all criteria
8. **Update documentation** - Keep tutorials and guides current

## 🔍 Maintenance and Updates

**Maintenance Team**: OLAF Framework Core Team  
**Update Frequency**: As needed for framework changes  
**Contribution Process**: Submit improvements through standard OLAF process

## 📝 Changelog

### Version 1.0.0 (2025-10-21)
- Initial release of complete prompt-engineer competency package
- Aggregated all prompt creation and manipulation prompts
- Included comprehensive template system
- Added best practices and principles documentation
- Integrated workflow generation capabilities
- Framework condensation utility included

## 🤝 Integration with Other Competencies

This package works seamlessly with:
- **competency-creation**: For packaging additional prompt features
- **developer**: For integrating prompts into development workflows
- **project-manager**: For workflow coordination and documentation

## ⚠️ Critical Requirements

- MANDATORY: Follow interaction protocols (Act/Propose-Act/Propose-Confirm-Act)
- MANDATORY: All prompts must include framework validation
- NEVER bypass template structure requirements
- NEVER modify original prompts during conversion (create new versions)
- ALWAYS validate outputs before considering task complete
- ALWAYS use time retrieval from terminal (never training data)
- ALWAYS use [id:file_id] format for file references

## 📖 Additional Resources

- OLAF Framework: `olaf-core/reference/`
- Prompt Templates: `olaf-core/templates/prompt-engineer/`
- Memory Map: `[id:reference_dir]/memory-map.md`
- Core Principles: `[id:reference_dir]/core-principles.md`
- Interaction Protocols: `[id:reference_dir]/team-delegation.md`

## 📞 Support

For issues or questions:
1. Check the troubleshooting sections in individual prompts
2. Review OLAF framework documentation
3. Consult competency examples
4. Refer to best practices guide

## License

MIT License - See LICENSE file for details

---

**Created**: October 21, 2025  
**Version**: 1.0.0  
**Status**: Public Beta  
**Maintained by**: OLAF Framework Core Team
