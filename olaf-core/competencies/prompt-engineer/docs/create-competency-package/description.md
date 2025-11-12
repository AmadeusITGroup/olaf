# Create Competency Package

**Source**: olaf-core/competencies/prompt-engineer/prompts/create-competency-package.md

## Overview

Create Competency Package builds complete, self-contained OLAF competency packages with proper structure, manifest, prompts, templates, scripts, and documentation. It guides you through the entire package creation process from initial concept to fully integrated, discoverable competency.

## Purpose

Creating well-structured competency packages is essential for OLAF's modularity and extensibility. This competency solves the challenge of ensuring new packages follow all OLAF conventions, include necessary components, integrate properly with the framework, and are immediately usable. It eliminates the complexity of manual package setup and ensures consistency across all competencies.

## Usage

**Command**: `create competency package`

**Protocol**: Propose-Confirm-Act

**When to Use**: Use this competency when creating entirely new competency domains, when packaging related prompts into a cohesive unit, when building specialized capabilities for specific personas or use cases, or when organizing scattered prompts into a structured package.

## Parameters

### Required Inputs
- **package_name**: Name for the competency package (kebab-case)
- **package_description**: Brief description of the package's purpose
- **category**: Category for organization (e.g., "development-tools", "documentation", "analysis")
- **target_users**: Primary and secondary user personas

### Optional Inputs
- **initial_prompts**: List of prompts to include in the package
- **required_templates**: Templates needed by the prompts
- **scripts**: Supporting scripts for automation
- **classification**: Package type ("kernel", "standard", "specialized")

### Context Requirements
- Write access to competencies directory
- Understanding of OLAF package structure
- Knowledge of target user needs and workflows
- Access to prompt and template creation tools

## Output

**Deliverables**:
- Complete competency package directory structure
- Properly formatted competency-manifest.json
- Placeholder or initial prompts in prompts/ folder
- Template files in templates/ folder
- Scripts in scripts/ folder (if applicable)
- Documentation structure in docs/ folder
- README.md with package overview

**Format**: Directory structure at `[competencies_dir]/[package_name]/` with all required components

## Examples

### Example 1: Creating a Database Administration Package

**Scenario**: Building a new competency for database management tasks

**Command**:
```
olaf create competency package
```

**Input**:
- package_name: "database-admin"
- package_description: "Database administration, optimization, and maintenance competencies"
- category: "infrastructure"
- target_users: {"primary": "dba", "secondary": ["sre", "developer"]}
- initial_prompts: ["optimize-queries", "backup-database", "analyze-performance"]

**Result**: Created complete package structure with manifest, 3 initial prompt files, templates for query analysis and backup reports, scripts for database connection utilities, and documentation structure with README.

### Example 2: Creating a Specialized Security Package

**Scenario**: Packaging security-focused prompts for security officers

**Command**:
```
olaf create competency package
```

**Input**:
- package_name: "security-audit"
- package_description: "Comprehensive security auditing and vulnerability assessment"
- category: "security"
- target_users: {"primary": "security-officer", "secondary": ["architect", "developer"]}
- classification: "specialized"
- initial_prompts: ["scan-vulnerabilities", "audit-dependencies", "review-security-config"]
- required_templates: ["vulnerability-report", "security-checklist"]

**Result**: Created specialized package with kernel classification, 3 security-focused prompts, 2 report templates, documentation structure, and manifest configured for security officer persona.

## Related Competencies

- **Create Prompt**: Use this to add prompts to your newly created package
- **Generate Tutorial**: Create tutorials for each entry point in your package
- **Select Competency Collection**: Add your package to appropriate collections
- **Import Prompts To Competency**: Analyze and plan migration of existing prompts into your package
- **Deploy Imported Prompts**: Execute batch import of prompts into your package

## Tips & Best Practices

- Choose descriptive package names that clearly indicate the domain or capability
- Define target users carefully - this affects how the package is discovered and used
- Start with core prompts and expand incrementally rather than trying to build everything at once
- Include templates for any structured outputs your prompts generate
- Add scripts for common automation tasks related to your competency
- Document your package thoroughly in the README and docs/ folder
- Use "kernel" classification only for essential framework components
- Test package integration by adding it to a collection and using its prompts
- Follow OLAF naming conventions (kebab-case) consistently

## Limitations

- Cannot automatically generate prompt logic - prompts need manual creation or import
- Requires understanding of OLAF structure and conventions
- Package quality depends on clarity of purpose and user needs
- Initial package creation is just the foundation - prompts need development
- Cannot automatically determine optimal package organization
- Requires manual testing and validation of package functionality
- Integration with collections requires separate collection update step
