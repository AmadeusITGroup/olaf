# Prompt 1.1: Initial Specification

## Purpose
Define **WHAT** needs to be built with complete functional and non-functional requirements, focused on business and user needs without implementation details.

## Instructions

Please create a comprehensive specification document based on the provided requirements:

### Input Required
- JIRA ticket or requirements document
- Business context and objectives
- User stories or use cases
- Target system information

### Task
Create a detailed specification document with the following structure:

1. **Executive Summary**
   - Project context and objectives
   - High-level feature description
   - Business value and impact

2. **Functional Requirements (FR-001 through FR-020)**
   - User stories with acceptance criteria
   - Feature descriptions and behaviors
   - Business rules and constraints
   - Input/output specifications

3. **Non-Functional Requirements (NFR-001 through NFR-015)**
   - Performance requirements
   - Security requirements
   - Reliability requirements
   - Scalability requirements
   - Maintainability requirements
   - Usability requirements

4. **Data Model Specification**
   - Conceptual data entities
   - Entity relationships
   - Data validation rules
   - Data lifecycle requirements

5. **Integration Specification**
   - External system dependencies
   - Integration points and interfaces
   - Data exchange formats
   - Communication protocols

6. **Workflow Specification**
   - Business process flows
   - User interaction flows
   - System behavior scenarios
   - Error handling workflows

7. **Constraints and Assumptions**
   - Technical constraints
   - Business constraints
   - Assumptions about environment
   - Risk factors and mitigation

8. **Requirement Traceability Matrix**
   - Mapping requirements to business objectives
   - Priority levels
   - Dependencies between requirements

### Output Format
- **Document Name**: `SPECIFICATION_<PROJECT-ID>.md`
- **Template Reference**: Use `../templates/template-specification.md` as the structure template
- **Length**: As concise as possible while covering all requirements thoroughly
- **Language Style**: Business-oriented, implementation-agnostic descriptions
- **Focus**: WHAT to build, not HOW to build it

### Success Criteria

- All functional requirements have clear acceptance criteria
- Non-functional requirements are measurable
- Requirements are traceable to business objectives
- Document follows the template structure exactly
- Ready for codebase validation in next step

### 🔒 MANDATORY EXIT DECLARATION

Upon completion, you MUST declare:

**"Step 1.1 (Initial Specification) is complete. Proceeding to Step 1.2 (Codebase Validation)."**

⚠️ **YOU MUST NOT:**
- Say "specification is ready for finalization"
- Say "ready for design phase"
- Skip to Step 1.3 or 1.4
- Ask user if they want to proceed to design

**NEXT STEP IS ALWAYS 1.2 - NO EXCEPTIONS**
