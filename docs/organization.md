# Project Organization

## Prompt and Template Organization

OLAF organizes prompts and templates into structured categories to improve discoverability, maintainability, and user experience. The categorization follows two main approaches:

### User Profile-Based Categories

These categories are organized around common user personas and their typical responsibilities:

#### **architect/**

- **Purpose**: Architectural analysis, system design, and technical strategy
- **Example Prompts**:
  - `analyze-technical-stack.md` - Analyze project technology stack and dependencies
- **Example Templates**:
  - `tech-stack-template.md` - Standardized technology stack documentation

#### **business-analyst/**

- **Purpose**: Business requirements analysis, functional specifications, and stakeholder communication
- **Example Prompts**:
  - `analyze-business-requirements.md` - Extract and analyze business requirements
  - `bootstrap-functional-spec-from-code.md` - Generate functional specifications from existing code
  - `generate-questionnaire.md` - Create stakeholder questionnaires
- **Example Templates**:
  - `functional-specification-template.md` - Structured functional specification format
  - `requirements-analysis-report-template.md` - Business requirements analysis output

#### **developer/**

- **Purpose**: Code development, review, testing, and technical implementation
- **Example Prompts**:
  - `review-code.md` - Comprehensive code review analysis
  - `evolve-code-iteratively.md` - Iterative code improvement workflow
  - `improve-cyclomatic-complexity.md` - Code complexity reduction
- **Example Templates**:
  - `code-review-template.md` - Standardized code review format
  - `unit-test-template.md` - Unit test documentation structure

#### **project-manager/**

- **Purpose**: Project coordination, documentation, and progress tracking
- **Example Prompts**:
  - `create-job.md` - Create structured project jobs/tasks
  - `review-progress.md` - Analyze project progress and status
  - `store-conversation-record.md` - Document conversation outcomes
- **Example Templates**:
  - `job-template.md` - Project job documentation format
  - `progress-review-template.md` - Progress assessment structure

### Category Selection Guidelines

**Use User Profile Categories When:**

- The workflow aligns with a specific professional role
- Multiple people with the same role would use similar prompts
- The workflow requires role-specific expertise or perspective

**Use Intent-Based Categories When:**

- The workflow is highly specialized or technical
- It represents a complete multi-phase process
- It requires specific tools, scripts, or specialized templates
- It's used across multiple user profiles

### Benefits of This Organization

1. **Discoverability**: Users can quickly find prompts relevant to their role or specific technical need
2. **Maintainability**: Related prompts and templates are co-located for easier updates
3. **Consistency**: Templates within categories follow similar patterns and structures
4. **Scalability**: New prompts can be easily categorized using established patterns
5. **Tool Integration**: Scripts and templates are organized alongside their related prompts

## Centralized Documentation

All project-related documentation, including architectural decision records, changelogs, and reports, is stored in a structured manner under `.olaf/olaf-data/product/documentations`.

Note: the idea with `olaf-data` is to avoid "polluting" the project folder with OLAF artifacts. But you could also decide to use a different folder part of the project repository.

## olaf-data folder structure

This folder structure is designed to store work artifacts, such as:

- `olaf-data/findings` : a temporary folder to store findings that require further action (e.g., results from code reviews). The USER is responsible for moving these findings to their final destination or deleting them.
- `olaf-data/people` : stores information about the human team members participating in the project
- `olaf-data/practices` : documents the practices used in the project
- `olaf-data/projects` : stores information about the projects and tasks being worked on, referred to as "jobs"
- `olaf-data/product` : stores product-related artifacts, such as specifications and documentation
- `olaf-data/product/decision-records` : stores decision records related to the project

While this structure is extensible, it is not mandatory to use it. However, many competencies rely on it to provide context to the LLM or to produce artifacts. And it is mapped into the memory-map.md file. So be careful to update this one if you wish to adapt the structure.

Note: OLAF is not a project management framework and does not aim to replace existing project management tools. It is designed to assist in project management tasks and can be used in conjunction with other tools and frameworks.
