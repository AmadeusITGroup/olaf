# Review User Story

## Overview

This competency reviews user stories against standard templates to ensure quality, clarity, and completeness. It systematically evaluates story components including title, description, acceptance criteria, and supporting details, then provides constructive feedback and clarifying questions to improve the story before development begins.

## Purpose

User stories often suffer from ambiguity, incomplete acceptance criteria, or untestable requirements that lead to misunderstandings and rework during development. This competency addresses this by applying a structured evaluation framework to assess story quality, identify specific weaknesses, and generate actionable questions that guide story authors toward clearer, more implementable user stories.

## Usage

**Command**: `review user story`

**Protocol**: Act

**When to Use**: Use this competency during backlog refinement sessions, before sprint planning to validate story readiness, when developers report unclear requirements, or as part of a quality gate before stories are approved for development.

## Parameters

### Required Inputs
- **user_story_content**: The user story text to be reviewed (can be provided inline or as file reference)

### Optional Inputs
- **template_reference**: Specific template to use for evaluation (uses default user story template if not specified)
- **review_depth**: Depth level for review (basic, thorough, or comprehensive; default: thorough)

### Context Requirements
- User story should follow standard format (title, description, acceptance criteria)
- User story review template is automatically loaded from competency templates
- Best results when story has at least basic structure defined

## Output

This competency produces a structured review report with assessment and improvement recommendations.

**Deliverables**:
- User story review report saved to `olaf-data/findings/user-story-reviews/user-story-review-YYYYMMDD-NNN.md`
- Overall quality assessment and rating
- Identified strengths and areas requiring improvement
- Specific clarifying questions for story author

**Format**: Markdown document with standardized sections covering overall assessment, component-by-component evaluation, identified issues, and actionable recommendations for improvement.

## Examples

### Example 1: Sprint Planning Story Validation

**Scenario**: During sprint planning, the team wants to validate that a user story about password reset functionality is ready for development.

**Command**:
```
olaf review user story
```

**Input**:
```
user_story_content: |
  As a user, I want to reset my password so I can access my account if I forget it.
  
  Acceptance Criteria:
  - User can request password reset
  - User receives email with reset link
  - User can set new password
```

**Result**: Review identified that acceptance criteria lack specificity (no timeout for reset link, no password complexity requirements, no error handling scenarios). Generated 8 clarifying questions about edge cases, security requirements, and user feedback mechanisms. Recommended story not ready for development without enhancements.

### Example 2: Backlog Refinement Quality Check

**Scenario**: Product owner has written several user stories for a new feature and wants quality feedback before backlog refinement meeting.

**Command**:
```
olaf review user story
```

**Input**:
```
user_story_content: [file reference to story document]
review_depth: comprehensive
```

**Result**: Comprehensive review highlighting strong business value statement and clear user persona, but identifying missing acceptance criteria for error states, unclear definition of "done", and testability concerns. Provided specific recommendations for improving each section.

## Related Competencies

- **analyze-business-requirements**: Use for reviewing complete requirements documents containing multiple stories
- **extend-specification**: Enhance specifications that user stories are derived from
- **generate-questionnaire**: Create questionnaires to gather missing information for incomplete stories
- **create-unit-tests** (developer): Validate that acceptance criteria are testable by attempting to write tests

## Tips & Best Practices

- Review stories early in the refinement process to allow time for improvements
- Use review findings as discussion points in refinement sessions, not as criticism
- Focus on testability—if you can't write a test for it, the criteria needs clarification
- Ensure acceptance criteria are specific, measurable, and observable
- Check that the story follows INVEST principles (Independent, Negotiable, Valuable, Estimable, Small, Testable)
- Validate that the story includes the "who, what, why" (persona, capability, benefit)
- Look for missing error handling, edge cases, and non-functional requirements
- Ensure story size is appropriate—large stories may need splitting
- Review related stories together to identify inconsistencies or gaps

## Limitations

- Cannot validate business value or priority—focuses on story quality and clarity
- Does not assess technical feasibility or implementation complexity
- Cannot determine if story is appropriately sized without team context
- May identify issues that are acceptable trade-offs for the team's context
- Does not replace collaborative refinement discussions with the team
- Cannot verify that acceptance criteria match actual business needs without stakeholder input
- Review quality depends on the completeness of the provided story content

---

**Source**: `olaf-core/competencies/business-analyst/prompts/review-user-story.md`
