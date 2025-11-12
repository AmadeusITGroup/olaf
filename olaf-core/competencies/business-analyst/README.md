# Business Analyst Competency Package

Comprehensive business analyst competency package for requirements gathering, specification management, and user story validation with specialized workflows for product and business analysis.

## Quick Start

1. **Analyze Business Requirements**:

   ```bash
   "analyze business requirements" with stakeholder_input="[description of business needs]"
   ```

2. **Review User Story**:

   ```bash
   "review user story" with user_story="[user story to review]"
   ```

3. **Generate Questionnaire**:

   ```bash
   "generate questionnaire" with topic="[topic for requirements gathering]"
   ```

## What's Included

### 🎯 Core Competencies (6 total)

| Competency | Entry Point | Purpose |
|------------|-------------|---------|
| Analyze Requirements | `analyze-business-requirements` | Requirements gathering and analysis |
| Bootstrap Spec | `bootstrap-functional-spec-from-code` | Extract specifications from code |
| Extend Specification | `extend-specification` | Enhance existing specifications |
| Generate Questionnaire | `generate-questionnaire` | Create requirements questionnaires |
| Improve Spec | `improve-spec` | Refine and validate specifications |
| Review User Story | `review-user-story` | User story validation and refinement |

### 📁 Structure

```text
business-analyst/
├── README.md                        # This file
├── competency-manifest.json         # Package metadata
├── dependencies.json                # Tool dependencies
├── docs/
│   └── business-analyst-competency.md   # Full documentation
├── prompts/
│   ├── analyze-business-requirements.md
│   ├── bootstrap-functional-spec-from-code.md
│   ├── extend-specification.md
│   ├── generate-questionnaire.md
│   ├── improve-spec.md
│   └── review-user-story.md
├── templates/
│   ├── business-terms-acronyms-template.md
│   ├── contact-recommendation-template.md
│   ├── feature-hierarchy-template.md
│   ├── functional-specification-template.md
│   ├── product-overview-template.md
│   ├── questionnaire-template.md
│   ├── requirements-analysis-report-template.md
│   └── user-story-review-template.md
└── tools/
    └── TOOL-INVENTORY.md
```

## Key Capabilities

✅ **Requirements Analysis** - Gather, analyze, and document business requirements  
✅ **Specification Management** - Create and maintain comprehensive specifications  
✅ **User Story Validation** - Review and refine user stories for clarity and completeness  
✅ **Questionnaire Generation** - Create structured questionnaires for systematic requirements gathering  
✅ **Spec Extraction** - Bootstrap specifications from existing implementations  
✅ **Spec Enhancement** - Extend and improve specifications with new requirements  

## Integration with Other Competencies

- **Architect**: Technology evaluation and technical specification review
- **Developer**: Requirements clarification for implementation
- **Researcher**: Market research and competitive analysis
- **Project Manager**: Requirements tracking and traceability
- **Technical Writer**: Documentation from specifications
- **PDF Analysis**: Document analysis for requirements

## Usage Examples

### Example 1: Gather Requirements from Stakeholders

```bash
"analyze business requirements"

# The competency will:
# 1. Ask clarifying questions about business needs
# 2. Document stakeholder requirements
# 3. Identify ambiguities and conflicts
# 4. Create requirements analysis report
# 5. Generate recommendations for specification
```

### Example 2: Review and Improve User Story

```bash
"review user story"
with user_story="As a user, I want to..."

# The competency will:
# 1. Validate story structure and clarity
# 2. Check acceptance criteria completeness
# 3. Identify missing details or assumptions
# 4. Suggest improvements
# 5. Provide refined user story
```

### Example 3: Create Questionnaire for Requirements

```bash
"generate questionnaire"
with topic="Mobile app feature requirements"

# The competency will:
# 1. Design questionnaire structure
# 2. Create specific, targeted questions
# 3. Include validation and ranking scales
# 4. Generate questionnaire document
# 5. Provide analysis framework for responses
```

## Requirements

- **Git**: ≥2.30 (for requirements tracking)
- **LLM**: Claude Sonnet 4.5 or higher recommended
- **Platforms**: Windows, Linux, macOS
- **Communication**: Access to stakeholders and project documentation

## Technical Documentation

For detailed technical documentation and advanced usage patterns, see:

- `docs/business-analyst-competency.md` - Full technical documentation
- `templates/` - Available template files for common patterns
- `competency-manifest.json` - Complete competency metadata
- `dependencies.json` - Detailed tool requirements

## Support

For issues or questions, refer to the OLAF Framework documentation or contact the Business Analysis team.
