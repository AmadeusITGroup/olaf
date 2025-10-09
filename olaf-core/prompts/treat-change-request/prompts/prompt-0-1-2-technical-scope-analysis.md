---
name: analyze-technical-scope-and-impact
description: Analyze technical scope and impact of change requests across codebase, estimating files, modules, LOC, and identifying API/database changes
tags: [technical-analysis, scope-estimation, api-changes, database-impact]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

You WILL use terminal commands, not training data for timestamps.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **change_request_summary_path**: string - Path to the change request summary file (REQUIRED)
- **workspace_path**: string - Path to the codebase workspace (REQUIRED)
- **analysis_output_path**: string - Path for technical scope analysis output (OPTIONAL, default: "2-technical-scope-analysis.md")
- **search_tools_available**: array - Available search tools (OPTIONAL, default: ["semantic_search", "grep_search", "file_search", "list_dir"])

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for technical scope analysis due to systematic nature

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm change request summary file exists and is accessible
- Validate workspace path contains valid codebase structure
- Check availability of required search tools
- Verify write access to output location

<!-- <prerequisite_validation> -->
**Change Request Summary Validation:**
You MUST validate the input change request summary:
1. You WILL read and parse the change request summary file
2. You MUST extract key requirements and feature keywords
3. You WILL identify business functionality to be implemented
4. You MUST validate completeness of requirements before proceeding
<!-- </prerequisite_validation> -->

### 2. Execution Phase

**Module and Service Identification:**
<!-- <module_identification> -->
You WILL identify all affected modules and services:

1. **Primary Module Discovery**:
   - You MUST use semantic_search to find modules related to feature keywords
   - You WILL use grep_search to locate specific classes/interfaces mentioned
   - You MUST use list_dir to explore and document module structure
   - You WILL categorize modules as primary (core changes) or secondary (supporting changes)

2. **Evidence Collection**:
   - You MUST document exact module names with evidence
   - You WILL count total number of modules affected
   - You MUST provide reasoning for primary vs secondary classification
   - You WILL include search results and file paths as evidence

3. **Module Impact Assessment**:
   - You WILL analyze business logic modules (core functionality)
   - You MUST examine persistence modules (database interactions)
   - You WILL review API/DTO modules (interface contracts)
   - You MUST assess UI modules (user interface components)
   - You WILL evaluate supporting modules (testing, deployment, notifications)
<!-- </module_identification> -->

**File and Code Estimation:**
<!-- <code_estimation> -->
You WILL estimate files and lines of code systematically:

1. **File Count Analysis**:
   - You MUST use grep_search with relevant keywords to find affected files
   - You WILL search for entity classes, services, controllers, DTOs
   - You MUST count Java classes, TypeScript components, test files
   - You WILL document search patterns and results

2. **Lines of Code Estimation**:
   - You MUST estimate new code (new classes/functions to be created)
   - You WILL estimate modified code (changes to existing files)
   - You MUST estimate test code (typically 40-60% of production LOC)
   - You WILL provide ranges (minimum-maximum estimates)

3. **File Category Breakdown**:
   - You WILL categorize by file type (Java, TypeScript, configuration)
   - You MUST separate production code from test code
   - You WILL identify documentation and configuration files
   - You MUST provide evidence-based justification for estimates
<!-- </code_estimation> -->

**API Impact Analysis:**
<!-- <api_analysis> -->
You WILL analyze all API changes comprehensively:

1. **New API Requirements**:
   - You MUST identify new REST endpoints needed
   - You WILL document HTTP methods and URL paths
   - You MUST define request/response structures
   - You WILL specify authentication and authorization requirements

2. **Existing API Modifications**:
   - You MUST identify which existing endpoints require changes
   - You WILL assess whether changes are breaking or backwards compatible
   - You MUST document versioning strategy for breaking changes
   - You WILL specify migration path for API consumers

3. **API Deprecation Analysis**:
   - You WILL identify any APIs being retired
   - You MUST document deprecation timeline and strategy
   - You WILL specify replacement APIs or migration paths
   - You MUST assess impact on existing API consumers

4. **API Documentation Requirements**:
   - You WILL specify OpenAPI/Swagger documentation updates
   - You MUST identify integration testing requirements
   - You WILL document API contract validation needs
<!-- </api_analysis> -->

**Database Impact Assessment:**
<!-- <database_analysis> -->
You WILL analyze database changes systematically:

1. **Schema Changes**:
   - You MUST identify new tables required with column specifications
   - You WILL document new columns in existing tables
   - You MUST specify index requirements and strategy
   - You WILL define foreign key relationships and constraints

2. **Data Migration Requirements**:
   - You MUST assess if historical data migration is required
   - You WILL estimate number of records affected
   - You MUST evaluate migration complexity and risks
   - You WILL specify rollback strategies for migrations

3. **Query and Performance Analysis**:
   - You MUST identify new queries required
   - You WILL assess query optimization needs
   - You MUST specify index strategy for performance
   - You WILL evaluate potential performance bottlenecks

4. **Database Security and Compliance**:
   - You WILL assess data privacy and security requirements
   - You MUST identify audit trail and logging needs
   - You WILL specify backup and recovery considerations
<!-- </database_analysis> -->

**Integration Point Mapping:**
<!-- <integration_analysis> -->
You WILL identify and document all integration impacts:

1. **Internal System Integrations**:
   - You MUST identify which internal modules/services are called
   - You WILL document event/message bus interactions
   - You MUST analyze shared data structures and contracts
   - You WILL assess workflow and process integrations

2. **External System Integrations**:
   - You MUST identify external systems involved
   - You WILL document API calls to external services
   - You MUST assess authentication/authorization changes
   - You WILL evaluate third-party service dependencies

3. **Integration Testing Requirements**:
   - You WILL specify integration test scenarios
   - You MUST identify mock/stub requirements
   - You WILL document end-to-end testing needs
   - You MUST assess integration failure handling
<!-- </integration_analysis> -->

**Architecture Impact Evaluation:**
<!-- <architecture_analysis> -->
You WILL assess architectural considerations:

1. **Design Pattern Analysis**:
   - You MUST identify new patterns to be introduced
   - You WILL assess modifications to existing patterns
   - You MUST evaluate pattern consistency across codebase
   - You WILL specify refactoring requirements

2. **Architectural Layer Impact**:
   - You MUST analyze presentation layer changes
   - You WILL assess business layer modifications
   - You MUST evaluate persistence layer impacts
   - You WILL identify cross-cutting concern changes

3. **Technology Stack Assessment**:
   - You WILL identify new libraries/frameworks needed
   - You MUST assess technology upgrade requirements
   - You WILL evaluate compatibility and dependency conflicts
   - You MUST specify learning curve and training needs

4. **Non-Functional Requirements Impact**:
   - You WILL assess performance implications
   - You MUST evaluate security impact
   - You WILL analyze scalability considerations
   - You MUST assess maintainability and supportability
<!-- </architecture_analysis> -->

### 3. Validation Phase
You WILL validate the technical scope analysis:
- Confirm all affected modules identified with concrete evidence
- Verify file and LOC estimates are based on actual codebase search results
- Validate API changes inventory is complete and categorized correctly
- Ensure database changes are fully specified with migration considerations
- Confirm all integration points are mapped with testing requirements
- Verify architecture impact assessment covers all relevant concerns

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Technical scope analysis file using template `../templates/template-technical-scope-analysis.md`
- Supporting documentation: Evidence files with search results and analysis details
- Estimation summary: Quantified impact metrics (modules, files, LOC, APIs, database changes)
- Integration map: Visual or structured representation of all integration points

## User Communication

### Progress Updates
- Confirmation when change request summary is successfully parsed
- Status updates for each module identification phase
- Progress on file and code estimation with preliminary numbers
- Completion status for API, database, and integration analysis
- Validation results for technical scope completeness

### Completion Summary
- Total modules affected (primary vs secondary breakdown)
- File and LOC estimates with confidence ranges
- API changes summary (new, modified, deprecated counts)
- Database changes summary (tables, columns, migrations)
- Integration points identified (internal and external counts)
- Architecture impact assessment summary

### Next Steps
You WILL clearly define:
- Technical scope analysis ready for risk assessment phase
- Files created and their locations
- Dependencies for next phase: `prompt-0-1-3-risk-assessment.md`
- Recommendations for technical review and validation

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: ALL estimates MUST be based on actual codebase search results, not assumptions
- Rule 2: Module identification MUST include concrete evidence (file paths, search results)
- Rule 3: API changes MUST be categorized as new, modified, or deprecated
- Rule 4: Database changes MUST include migration strategy and rollback plans
- Rule 5: Integration points MUST distinguish between internal and external systems
- Rule 6: Architecture impact MUST cover all layers (presentation, business, persistence)
- Rule 7: Estimates MUST provide ranges (minimum-maximum) with confidence levels
- Rule 8: All analysis MUST be traceable to requirements in change request summary

## Success Criteria
You WILL consider the task complete when:
- [ ] Change request summary successfully parsed and analyzed
- [ ] All affected modules identified with concrete evidence
- [ ] File and LOC estimates provided with evidence-based justification
- [ ] Complete API changes inventory (new, modified, deprecated)
- [ ] Comprehensive database impact analysis with migration strategy
- [ ] All integration points mapped (internal and external)
- [ ] Architecture impact assessed across all layers
- [ ] Output file generated following template structure exactly
- [ ] Validation confirms analysis completeness and accuracy

## Required Actions
1. Validate change request summary and extract technical requirements
2. Execute systematic technical scope analysis using available search tools
3. Generate comprehensive technical scope analysis in specified format
4. Provide evidence-based estimates with confidence ranges
5. Prepare for next phase with clear handoff documentation

## Error Handling
You WILL handle these scenarios:
- **Change Request Summary Access Failed**: Provide clear error message and request valid file path
- **Workspace Access Failed**: Validate workspace path and request correct codebase location
- **Search Tool Unavailable**: Adapt analysis method and document limitations
- **Incomplete Module Discovery**: Flag gaps and request manual module specification
- **Estimation Uncertainty**: Document assumptions and provide confidence ranges
- **Template Access Failed**: Use standard structure and continue with technical analysis
- **Integration Point Discovery Failed**: Request manual integration mapping from stakeholders
- **Architecture Analysis Blocked**: Document constraints and proceed with available information

**Critical Requirements**
- MANDATORY: Use Act protocol for systematic technical analysis
- MANDATORY: Base ALL estimates on actual codebase search results
- NEVER make assumptions about technical implementation without evidence
- NEVER proceed without validating change request summary completeness
- ALWAYS provide evidence trails for module and file identification
- ALWAYS include confidence levels and ranges for estimates
- ALWAYS validate that technical scope aligns with business requirements
- NEVER skip integration point analysis or architecture impact assessment