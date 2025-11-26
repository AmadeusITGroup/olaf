# Tester Competency Package

Comprehensive tester competency package for test planning, test case generation, and quality assurance with specialized workflows for testing strategy and validation.

## Quick Start

1. **Generate Test Plan**:

   ```bash
   "generate test plan" with specification="[path]" application="[name]"
   ```

## What's Included

### 🎯 Core Competencies (1 total)

| Competency | Entry Point | Purpose |
|------------|-------------|---------|
| Generate Test Plan | `generate-test-plan` | Create comprehensive test plans based on specifications |

### 📁 Structure

```text
tester/
├── README.md                        # This file
├── competency-manifest.json         # Package metadata
├── dependencies.json                # Tool dependencies
├── docs/
│   └── generate-test-plan/
│       ├── description.md
│       └── tutorial.md
├── prompts/
│   └── generate-test-plan.md
└── templates/
    └── test-plan-template.md
```

## Key Capabilities

✅ **Test Planning** - Create comprehensive test plans with strategy and approach  
✅ **Test Case Design** - Generate test cases in Gherkin format with clear criteria  
✅ **Requirements Analysis** - Identify testable requirements from specifications  
✅ **Test Strategy** - Define test levels, types, and execution approach  
✅ **Risk Management** - Plan risk-based testing and defect management  
✅ **Resource Planning** - Allocate resources and schedule test cycles  

## Integration with Other Competencies

- **Business Analyst**: Requirements analysis and user story validation
- **Developer**: Code review and unit test augmentation
- **Architect**: Technical stack analysis and specification generation
- **Project Manager**: Decision records and progress tracking

## Usage Examples

### Example 1: Create Test Plan from Functional Specification

```bash
"generate test plan"
with specification="/path/to/functional-spec.md"
with application="PaymentService"

# The competency will:
# 1. Analyze functional specification
# 2. Identify testable requirements
# 3. Define test objectives and strategy
# 4. Create test cases in Gherkin format
# 5. Plan test execution approach
# 6. Document entry/exit criteria
# 7. Generate comprehensive test plan
```

### Example 2: Test Plan with Specific Test Types

```bash
"generate test plan"
with specification="/path/to/spec.md"
with application="MobileApp"
with test_levels=["unit", "integration", "system", "acceptance"]
with test_types=["functional", "performance", "security", "usability"]
with coverage_target=85

# The competency will:
# 1. Focus on specified test levels and types
# 2. Target 85% test coverage
# 3. Include performance and security testing strategies
# 4. Plan usability testing approach
# 5. Create test cases for each level
# 6. Document resource and environment needs
```

## Requirements

- **Git**: ≥2.30 (for test artifact version control)
- **LLM**: Claude Sonnet 4.5 or higher recommended
- **Platforms**: Windows, Linux, macOS
- **Optional Tools**: 
  - cucumber for BDD testing
  - jest for JavaScript testing
  - pytest for Python testing

## Technical Documentation

For detailed technical documentation and advanced usage patterns, see:

- `docs/generate-test-plan/` - Full documentation and tutorials
- `templates/` - Available template files for test plans
- `competency-manifest.json` - Complete competency metadata
- `dependencies.json` - Detailed tool requirements

## Support

For issues or questions, refer to the OLAF Framework documentation or contact the QA team.
