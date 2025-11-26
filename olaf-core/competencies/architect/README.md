# Architect Competency Package

Comprehensive architect competency package for technical stack analysis, architecture design, and technical specification generation with specialized workflows for system architecture and technology evaluation.

## Quick Start

1. **Analyze Technical Stack**:

   ```bash
   "analyze technical stack" with project_root="[path]" project_name="[name]"
   ```

2. **Generate Detailed Tech Spec**:

   ```bash
   "generate detailed tech spec" with spec_path="[path]" application_name="[name]"
   ```

## What's Included

### 🎯 Core Competencies (2 total)

| Competency | Entry Point | Purpose |
|------------|-------------|---------|
| Analyze Technical Stack | `analyze-technical-stack` | Chapter-based technical stack analysis with automated discovery |
| Generate Detailed Tech Spec | `generate-detailed-tech-spec` | Create comprehensive technical specifications with code examples |

### 📁 Structure

```text
architect/
├── README.md                        # This file
├── competency-manifest.json         # Package metadata
├── dependencies.json                # Tool dependencies
├── docs/                            # Documentation
├── prompts/
│   ├── analyze-technical-stack.md
│   └── generate-detailed-tech-spec.md
└── templates/
    └── tech-stack-template.md
```

## Key Capabilities

✅ **Technical Stack Analysis** - Automated discovery and analysis of technology stacks  
✅ **Architecture Design** - Design and document system architectures  
✅ **Technical Specification** - Create comprehensive technical specifications with code examples  
✅ **Technology Evaluation** - Assess and evaluate technology choices  
✅ **Chapter-Based Workflows** - Multi-session analysis with incremental progress  
✅ **Automated Discovery** - Scan codebases to identify components and dependencies  

## Integration with Other Competencies

- **Business Analyst**: Requirements analysis and specification management
- **Developer**: Code review and technical specification extraction
- **Researcher**: Technology research and competitive analysis
- **Project Manager**: Decision records and progress tracking
- **Technical Writer**: Architecture documentation

## Usage Examples

### Example 1: Analyze Technical Stack (Chapter-Based)

```bash
"analyze technical stack"
with project_root="/path/to/project"
with project_name="MyApp"

# The competency will:
# Chapter 1: Discovery
# - Scan directory structure and identify project type
# - Parse package manager files
# - Detect frameworks and libraries
# - Identify build tools and configuration
# - Discover database and ORM usage
# - Find CI/CD configuration
# - Detect containerization setup

# Chapter 2: Analysis
# - Identify versions and compatibility
# - Check for vulnerabilities
# - Assess maintenance status
# - Evaluate performance characteristics
# - Analyze dependency relationships

# Chapter 3: Assessment
# - Evaluate architecture patterns
# - Identify technical debt
# - Assess security posture
# - Evaluate scalability
# - Check test coverage
# - Analyze deployment readiness

# Chapter 4: Reporting
# - Generate executive summary
# - Compile detailed analysis
# - Create recommendations
# - Document migration paths
# - Include visual diagrams
```

### Example 2: Generate Detailed Technical Specification

```bash
"generate detailed tech spec"
with spec_path="/path/to/general-spec.md"
with application_name="MyApp"
with sections=["Error Handling", "Configuration", "Authentication"]

# The competency will:
# 1. Analyze source code for relevant components
# 2. Extract code examples and patterns
# 3. Generate detailed documentation for each section
# 4. Include architecture diagrams
# 5. Document design decisions
# 6. Link to source files
# 7. Validate accuracy and completeness
```

## Requirements

- **Git**: ≥2.30 (for version control and code analysis)
- **LLM**: Claude Sonnet 4.5 or higher recommended
- **Platforms**: Windows, Linux, macOS
- **Optional Tools**: 
  - mermaid-cli for diagram generation
  - dependency-cruiser for dependency analysis
  - jq for JSON parsing

## Technical Documentation

For detailed technical documentation and advanced usage patterns, see:

- `docs/` - Full technical documentation
- `templates/` - Available template files for common patterns
- `competency-manifest.json` - Complete competency metadata
- `dependencies.json` - Detailed tool requirements

## Support

For issues or questions, refer to the OLAF Framework documentation or contact the Architecture team.
