---
name: generate-questionnaire
description: Create a well-structured questionnaire for gathering specific information from a target audience.
tags: [generation, survey, research, feedback]
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
- **purpose**: string - Primary goal of the questionnaire
- **audience**: string - Target audience description
- **question_types**: array[enum] - (Optional) Preferred question types (open-ended, multiple-choice, Likert, etc.)
- **sections**: array[string] - (Optional) Logical sections for grouping questions
- **length**: enum[short,medium,long] - (Optional) Desired questionnaire length (default: medium)

## Process

1. **Questionnaire Design**:
   - Define clear objectives
   - Determine appropriate question types
   - Structure logical flow
   - Ensure question clarity and neutrality

2. **Content Creation**:
   - Draft introduction and instructions
   - Create relevant questions
   - Add response options where needed
   - Include demographic section if applicable

3. **Review & Refinement**:
   - Check for bias and leading questions
   - Ensure logical progression
   - Validate question clarity
   - Test completion time

## Output/Result Format
Follow template structure: `[id:templates_dir]business-analyst/questionnaire-template.md`

**Save Output**: Create file `[id:ack_dir]questionnaires/questionnaire-<concise purpose>.md` where:

- Markdown document with:
  - Title and introduction
  - Clear instructions
  - Grouped questions
  - Response options
  - Thank you note

## Output to USER
1. **Questionnaire Preview**:
   - Overview of structure
   - Sample questions
   - Estimated completion time

2. **Final Questionnaire**:
   - Complete markdown document
   - Ready for distribution
   - Copy-paste friendly format

## Domain-Specific Rules
- Rule 1: Keep questions clear and concise
- Rule 2: Avoid leading or biased questions
- Rule 3: Group related questions together
- Rule 4: Include progress indicators for long surveys
- Rule 5: Provide clear instructions

## Required Actions
1. Define questionnaire goals
2. Design question flow
3. Draft questions
4. Review and refine
5. Format output

⚠️ **Critical Notes**
- Respect respondent time
- Ensure anonymity where needed
- Test before distribution
- Include option for additional comments
- Consider mobile responsiveness
