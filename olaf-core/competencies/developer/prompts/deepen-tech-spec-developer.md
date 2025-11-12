---

name: deepen-tech-spec-developer

description: Deep-dive technical analysis focused on developer concerns - code quality, unit testing, architecture patterns, design principles assessment with evidence-based evaluation

tags: [documentation, technical-spec, deep-dive, developer-analysis, code-quality, unit-testing]

---



## Framework Validation
## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.- <olaf-interaction-protocols> - Appropriate execution protocol

You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
If you need to generate a filename or identifier that includes a timestamp (e.g., YYYYMMDD-HHmm or YYYYMMDD), obtain the current time from the terminal, not from model/context data.

- Windows (date+time): `Get-Date -Format "yyyyMMdd-HHmm"`
- Windows (date only): `Get-Date -Format "yyyyMMdd"`
- Unix/Linux/macOS (date+time): `date +"%Y%m%d-%H%M"`
- Unix/Linux/macOS (date only): `date +"%Y%m%d"`




## Input Parameters

You MUST request these parameters if not provided by the user:

- **tech_spec_path**: string - Path to the existing technical specification file (REQUIRED)

- **application_name**: string - Name of the application for file naming (REQUIRED)

- **chapter_focus**: string - Specific chapter to start with, defaults to first chapter (OPTIONAL)



## User Interaction Protocol

You MUST follow the established interaction protocol strictly:

- Act / Propose-Act / Propose-Confirm-Act (defined externally)

- You WILL use Propose-Confirm-Act for this competency due to high complexity and session management requirements



## Chapter Structure - Developer Focus

The deep-dive documentation will be organized into developer-focused chapters with evidence-based assessment:

1. **Architecture & Design Patterns Assessment** - Design pattern usage, SOLID principles adherence, component coupling analysis

2. **API Implementation Quality Analysis** - Endpoint implementation, error handling patterns, validation strategies, REST compliance

3. **Data Access & Transaction Management** - ORM patterns, transaction boundaries, connection management, query optimization

4. **Error Handling & Exception Strategy** - Exception hierarchy evaluation, logging patterns, debugging capabilities

5. **Unit Testing & Code Quality Evaluation** - Test coverage analysis, test quality assessment, mocking patterns, TDD practices

6. **Module Dependencies & Structure Assessment** - Dependency injection evaluation, module boundaries, coupling analysis, monorepo structure



## Prerequisites

You MUST verify these requirements before proceeding:

1. You WILL confirm the tech spec file exists and is accessible

2. You MUST validate that the application name follows kebab-case naming

3. You WILL check for existing chapter files to avoid overwrites



## Process



### 1. Validation Phase

You WILL verify all requirements:

- Confirm tech_spec_path exists and is readable

- Validate application_name is provided and properly formatted

- Check chapter_focus parameter if provided matches available chapters

- Verify access to findings directory for file creation

- Scan for existing chapter files to prevent conflicts



### 2. Execution Phase



**Tech Spec Analysis:**

<!-- <tech_spec_analysis> -->

You MUST read and analyze the existing technical specification at `tech_spec_path`

You WILL extract: application architecture, key components, technology stack, security features, deployment details

<!-- </tech_spec_analysis> -->



**Chapter Planning:**

<!-- <chapter_planning> -->

You WILL create a comprehensive chapter outline covering all 8 defined areas

You MUST present the chapter structure to user for approval before proceeding

<!-- </chapter_planning> -->



**Core Logic**: You WILL execute following protocol requirements

- Apply Propose-Confirm-Act protocol for chapter structure approval

- Execute chapter development cycle for each approved chapter:

  1. **Deep Analysis**: Extract detailed technical information from codebase

  2. **Documentation**: Create comprehensive chapter with examples and best practices  

  3. **User Review**: Present completed chapter and request feedback

  4. **Session Management**: Offer session transition after each chapter completion



**Session Transition Management:**

- Execute carry-over competency when user requests new session

- Include current progress state and next chapter information

- Provide clear instructions for session resumption



### 3. Validation Phase

You WILL validate results:

- Confirm chapter documentation meets quality standards

- Verify all code examples are accurate and functional

- Validate file naming conventions are followed



## Chapter Content Requirements - Developer Focus



### Architecture & Design Patterns Assessment

- **Evidence-Based Analysis**: Actual design patterns found in code (Factory, Singleton, Observer, etc.)

- **SOLID Principles Evaluation**: Specific violations with code examples and impact assessment

- **Component Coupling Analysis**: Actual dependency relationships, circular dependencies, tight coupling issues

- **Code Organization Assessment**: Package structure evaluation, separation of concerns analysis

- **Performance Implications**: Architectural choices impact on performance with measurements



### API Implementation Quality Analysis  

- **Endpoint Implementation Review**: REST compliance, HTTP method usage, status code consistency

- **Error Handling Assessment**: Exception propagation patterns, error response standardization

- **Validation Strategy Evaluation**: Input validation patterns, business rule enforcement

- **Security Implementation**: Authentication mechanisms, authorization patterns, input sanitization

- **Documentation Quality**: API documentation completeness and accuracy



### Data Access & Transaction Management

- **ORM Pattern Analysis**: JPA/Hibernate usage patterns, entity relationship implementation

- **Transaction Boundary Assessment**: @Transactional usage, transaction management strategies

- **Connection Management**: Connection pooling configuration, resource management patterns

- **Query Optimization**: N+1 problems, lazy loading patterns, query performance analysis

- **Database Integration**: SQL quality, stored procedure usage, database-specific features



### Error Handling & Exception Strategy

- **Exception Hierarchy Evaluation**: Custom exception design, exception propagation patterns

- **Logging Strategy Assessment**: Logging levels, structured logging, performance impact

- **Debugging Capabilities**: Stack trace quality, diagnostic information availability

- **Error Recovery**: Circuit breaker patterns, retry mechanisms, fallback strategies

- **Monitoring Integration**: Error tracking, alerting integration, observability patterns



### Unit Testing & Code Quality Evaluation

- **Test Coverage Analysis**: Line and branch coverage assessment with quality evaluation

- **Test Quality Assessment**: Meaningful tests vs. trivial tests (getter/setter anti-patterns)

- **Testing Patterns**: Mock usage, test data management, setup/teardown patterns  

- **TDD Practices**: Test-first development evidence, test-driven design patterns

- **Edge Case Coverage**: Boundary condition testing, null handling, error scenario testing

- **Test Maintainability**: Test code organization, test utility patterns, test readability



### Module Dependencies & Structure Assessment

- **Dependency Injection Evaluation**: Spring DI patterns, constructor vs. field injection analysis

- **Module Boundaries**: Maven/Gradle module structure, package dependencies analysis

- **Coupling Analysis**: Inter-module dependencies, circular dependency detection

- **Configuration Management**: Application properties organization, environment-specific configuration

- **Build Process Assessment**: Build tool configuration, dependency management, build performance



## Output Format

You WILL generate outputs following this structure:

- Primary deliverable: Follow template structure below for each chapter

- Supporting files: `[id:findings_dir]specs/deep-dive-{application_name}-chapter-{N}-{chapter-name}-YYYYMMDD-NNN.md`

- Documentation: Complete chapter with code examples and implementation details



**File Naming Convention**:

- {application_name} is kebab-case formatted

- {N} is chapter number (01, 02, etc.)  

- {chapter-name} is kebab-case chapter name

- YYYYMMDD-NNN follows standard OLAF naming



**Chapter Template Structure**:

```markdown

# Chapter {N}: {Chapter Title} - {Application Name}



## Chapter Overview

- Purpose and scope of this chapter

- Key topics covered

- Prerequisites and dependencies



## Detailed Analysis

[Comprehensive content specific to chapter topic]



## Implementation Details

[Code examples, configurations, schemas]



## Best Practices

[Recommendations and guidelines]



## Common Issues & Solutions

[Troubleshooting and problem resolution]



## References & Further Reading

[Links to additional resources]



---

*This chapter is part of the deep-dive documentation series for {Application Name}*

*Previous: Chapter {N-1} | Next: Chapter {N+1}*

```



## User Communication

You WILL provide these updates to the user:



### Progress Updates

- Confirmation when each chapter analysis begins

- Location of created chapter files with full path

- Timestamp identifier used in YYYYMMDD-HHmm format



### Completion Summary

- Summary of chapter content created

- Files created with exact locations

- User review checkpoint with specific questions



### Next Steps

You WILL clearly define:

- Next chapter to be developed

- Session continuation options (same session vs new session)

- Carry-over instructions if session transition requested



## User Interaction Protocol



### After Each Chapter:

1. Present the completed chapter to the user

2. Ask: "Please review Chapter {N}: {Chapter Title}. Are you satisfied with the depth and detail?"

3. If user requests changes, make adjustments and repeat review

4. Once approved, ask: "Would you like to continue with the next chapter in a new session? This helps manage memory and ensures optimal performance."

5. If user says yes:

   - Execute carry-over competency

   - Tell user: "I've created a carry-over note. Please start your next session with 'carry-on' to continue with Chapter {N+1}: {Next Chapter Title}"

6. If user says no, continue with next chapter in current session



## Session State Management



### Carry-Over Information to Include:

- Current application being documented

- Chapter just completed

- Next chapter to work on

- Any specific user preferences or modifications

- Location of existing chapter files

- Overall progress status



## Domain-Specific Rules

You MUST follow these constraints:

- Rule 1: Always analyze actual code and configurations, not just the tech spec content

- Rule 2: Include practical examples and implementation snippets with proper validation

- Rule 3: Provide actionable recommendations with clear rationale and implementation steps

- Rule 4: Ensure each chapter stands alone while maintaining series coherence and cross-references

- Rule 5: Execute user review checkpoint after each chapter completion without exception

- Rule 6: Always offer session transition after chapter completion to manage memory and complexity



## Success Criteria

You WILL consider the task complete when:

- [ ] Tech spec file validated and successfully analyzed

- [ ] Chapter outline created and approved by user

- [ ] Current chapter documentation generated with comprehensive technical detail

- [ ] Code examples validated for accuracy and functionality

- [ ] User review completed with feedback incorporated

- [ ] Session management options presented to user

- [ ] Carry-over executed if requested by user



## Required Actions

1. Validate all required input parameters and file accessibility

2. Execute tech spec analysis following XML markup protocols

3. Generate comprehensive chapter content with deep technical analysis

4. Present chapter for mandatory user review and incorporate feedback

5. Manage session transitions using carry-over competency when requested

6. Maintain consistent documentation quality and naming conventions



## Error Handling

You WILL handle these scenarios:

- **Missing Tech Spec File**: Provide clear error message and request correct file path from user

- **Invalid Application Name**: Request properly formatted kebab-case application name

- **File Access Issues**: Offer alternative file locations or manual content input

- **Chapter Generation Failures**: Provide fallback manual chapter creation steps

- **Carry-Over Failures**: Offer manual session state documentation as backup



⚠️ **Critical Requirements**

- MANDATORY: Follow Propose-Confirm-Act protocol for all chapter structure and content decisions

- NEVER skip user review checkpoints between chapters

- ALWAYS validate code examples through actual codebase analysis

- ALWAYS offer session transition after each chapter to manage complexity

- ALWAYS execute carry-over competency when user requests session transition

- ALWAYS provide rollback instructions if chapter files need to be removed

- ALWAYS maintain application name consistency in file naming across all chapters