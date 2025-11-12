# Generate Questionnaire

## Overview

This competency creates well-structured questionnaires for gathering specific information from target audiences. It designs clear, unbiased questions organized into logical sections, with appropriate question types and response options tailored to the questionnaire's purpose and audience.

## Purpose

Gathering quality information from stakeholders, users, or team members requires carefully designed questionnaires that avoid bias, maintain clarity, and respect respondent time. This competency solves the challenge of questionnaire design by applying best practices to create effective surveys that yield actionable insights while ensuring questions are neutral, well-organized, and appropriate for the target audience.

## Usage

**Command**: `generate questionnaire`

**Protocol**: Propose-Act

**When to Use**: Use this competency when gathering requirements from stakeholders, collecting user feedback on features, conducting research for product decisions, assessing team satisfaction, or gathering information for any business analysis activity that benefits from structured data collection.

## Parameters

### Required Inputs
- **purpose**: Primary goal of the questionnaire (e.g., "gather user feedback on new dashboard design")
- **audience**: Target audience description (e.g., "enterprise software users", "internal development team")

### Optional Inputs
- **question_types**: Preferred question types (open-ended, multiple-choice, Likert scale, ranking, etc.)
- **sections**: Logical sections for grouping questions (e.g., ["Demographics", "Current Experience", "Feature Preferences"])
- **length**: Desired questionnaire length (short, medium, or long; default: medium)

### Context Requirements
- Clear understanding of information needs and objectives
- Questionnaire template is automatically loaded from competency templates
- Consider distribution method when designing (email, web form, interview)

## Output

This competency produces a ready-to-use questionnaire document.

**Deliverables**:
- Questionnaire document saved to `olaf-data/ack/questionnaires/questionnaire-<purpose>.md`
- Markdown-formatted questionnaire with title, introduction, instructions, grouped questions, and thank you note

**Format**: Structured markdown document following the questionnaire-template with clear sections, numbered questions, response options where applicable, and copy-paste friendly formatting for easy distribution.

## Examples

### Example 1: User Feature Feedback

**Scenario**: Product team needs to gather feedback from beta users about a new reporting feature before general release.

**Command**:
```
olaf generate questionnaire
```

**Input**:
```
purpose: gather beta user feedback on new reporting feature
audience: enterprise customers in beta program
question_types: [multiple-choice, Likert, open-ended]
sections: [Usage Patterns, Feature Satisfaction, Improvement Suggestions]
length: medium
```

**Result**: Generated 15-question questionnaire with 5 questions per section, including Likert scales for satisfaction ratings, multiple-choice for usage patterns, and open-ended questions for improvement suggestions. Estimated completion time: 8-10 minutes.

### Example 2: Requirements Gathering Interview Guide

**Scenario**: Business analyst needs structured questions for stakeholder interviews about a new workflow automation project.

**Command**:
```
olaf generate questionnaire
```

**Input**:
```
purpose: gather requirements for workflow automation
audience: department managers and process owners
question_types: [open-ended]
sections: [Current Process, Pain Points, Desired Outcomes, Constraints]
length: short
```

**Result**: Generated interview guide with 8 open-ended questions designed to elicit detailed responses about current workflows, challenges, and automation goals. Structured for 30-minute interviews.

## Related Competencies

- **analyze-business-requirements**: Use questionnaire responses as input for requirements analysis
- **autonomous-comprehensive-research** (researcher): Complement questionnaire data with broader research
- **review-research-report** (researcher): Analyze and synthesize questionnaire results
- **generate-user-personas** (product-owner): Use questionnaire data to create user personas

## Tips & Best Practices

- Start with clear objectives—know what decisions the questionnaire will inform
- Keep questionnaires as short as possible while gathering necessary information
- Test the questionnaire with a small group before wide distribution
- Use Likert scales for quantifiable satisfaction or agreement measurements
- Place demographic questions at the end to avoid respondent fatigue
- Include progress indicators for longer questionnaires
- Provide "Other" or "Additional comments" options for flexibility
- Avoid double-barreled questions that ask about multiple things at once
- Use neutral language—avoid leading questions that bias responses
- Consider mobile-friendly formatting if distributed electronically

## Limitations

- Cannot guarantee response rates or data quality—depends on audience engagement
- Does not analyze or synthesize responses—only creates the questionnaire instrument
- May require iteration based on pilot testing results
- Cannot replace in-depth interviews for complex or sensitive topics
- Question effectiveness depends on clear understanding of information needs
- Does not handle questionnaire distribution or response collection logistics

---

**Source**: `olaf-core/competencies/business-analyst/prompts/generate-questionnaire.md`
