---
name: extract-structure-from-java-monorepo
description: Analyze Java monorepo codebases to extract and document architectural structure, dependencies, and service boundaries
tags: [java, monorepo, architecture, analysis, microservices, refactoring]
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
- **repository_path**: string - Absolute path to the Java monorepo root directory (REQUIRED)
- **analysis_depth**: string|shallow|deep|comprehensive - Level of analysis detail (OPTIONAL, default: deep)
- **focus_areas**: array - Specific areas to emphasize [dependencies|services|packages|integration|extraction] (OPTIONAL)
- **output_format**: string|report|summary|detailed - Output format preference (OPTIONAL, default: report)
- **include_metrics**: boolean - Whether to include quantitative metrics (OPTIONAL, default: true)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Act protocol for analysis execution due to computational intensity

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm repository path exists and contains Java code
- Validate repository structure indicates monorepo pattern (multiple modules/projects)
- Check for build system files (pom.xml, build.gradle, etc.)
- Verify access to required analysis tools and file system
- Confirm output directory permissions for report generation

### 2. Execution Phase

<!-- <repository_analysis> -->
**Repository Structure Discovery:**
You WILL execute comprehensive repository scanning:
- Identify all modules using build system configuration files
- Map directory structure and module hierarchy
- Catalog package structures within each module
- Identify configuration files and their relationships
<!-- </repository_analysis> -->

<!-- <dependency_analysis> -->
**Dependency Analysis:**
You WILL analyze module and package dependencies:
- Parse build files (Maven pom.xml, Gradle build files) for declared dependencies
- Analyze Java import statements for actual code dependencies
- Identify circular dependencies and coupling issues
- Map inter-module communication patterns
- Calculate dependency metrics (fan-in, fan-out, coupling coefficients)
<!-- </dependency_analysis> -->

<!-- <service_boundary_identification> -->
**Service Boundary Analysis:**
You WILL identify logical service boundaries:
- Group related modules by business functionality
- Analyze data flow patterns between modules
- Identify shared libraries vs. business logic modules
- Map external system integration points
- Assess transaction boundaries and data consistency requirements
<!-- </service_boundary_identification> -->

<!-- <integration_pattern_analysis> -->
**Integration Pattern Discovery:**
You WILL catalog integration mechanisms:
- Database access patterns and shared data stores
- API communication (REST, messaging, events)
- Configuration management approaches
- Deployment and runtime dependencies
- Cross-cutting concerns (logging, security, monitoring)
<!-- </integration_pattern_analysis> -->

<!-- <extraction_opportunity_assessment> -->
**Microservices Extraction Assessment:**
You WILL evaluate extraction opportunities:
- Identify loosely coupled module clusters
- Assess business domain alignment with technical boundaries
- Evaluate data migration complexity for each potential service
- Calculate extraction effort vs. business value
- Identify blocking dependencies for extraction
<!-- </extraction_opportunity_assessment> -->

**Core Logic**: You WILL execute following protocol requirements
- Apply Propose-Act protocol for user approval before intensive analysis
- Generate comprehensive structural analysis following template exactly
- Provide actionable recommendations for refactoring and extraction
- Include quantitative metrics when requested
- Validate all findings against actual code structure

### 3. Validation Phase
You WILL validate analysis results:
- Cross-reference dependency analysis with actual code imports
- Verify service boundary recommendations align with business logic
- Confirm extraction recommendations consider all technical dependencies
- Validate metrics calculations and architectural assessments
- Ensure recommendations are prioritized by feasibility and impact

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Complete analysis report following template `[id:templates_dir]/architect/structure-from-java-monorepo-template.md`
- Supporting files: Dependency diagrams and service boundary visualizations (if tools available)
- Documentation: Executive summary with key findings and priority recommendations

## User Communication

### Progress Updates
- Confirmation when repository structure analysis completes
- Status updates during dependency analysis phases
- Progress indicators for service boundary identification
- Completion notifications for each major analysis component

### Completion Summary
- Analysis report presented following template structure
- Key architectural findings highlighted
- Prioritized recommendations for immediate and long-term actions
- Microservices extraction roadmap with effort estimates

### Next Steps
You WILL clearly define:
- Immediate refactoring opportunities (0-3 months)
- Medium-term architectural improvements (3-12 months)
- Long-term microservices extraction strategy (12+ months)
- Dependencies and prerequisites for each recommendation phase

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Analysis MUST be based on actual code structure, not assumptions
- Rule 2: Dependency analysis MUST include both declared and runtime dependencies
- Rule 3: Service boundary recommendations MUST consider data consistency requirements
- Rule 4: Extraction recommendations MUST include effort estimates and risk assessments
- Rule 5: All metrics MUST be calculated from actual codebase measurements
- Rule 6: Recommendations MUST be prioritized by business value and technical feasibility
- Rule 7: Analysis MUST identify circular dependencies and architectural violations

## Success Criteria
You WILL consider the task complete when:
- [ ] Repository structure completely mapped and documented
- [ ] All module dependencies identified and analyzed
- [ ] Service boundaries clearly defined with business justification
- [ ] Integration patterns catalogued and assessed
- [ ] Microservices extraction opportunities evaluated with effort estimates
- [ ] Comprehensive report generated following template structure
- [ ] Recommendations prioritized and roadmap provided
- [ ] All findings validated against actual code structure
- [ ] User approval obtained for analysis approach and results

## Required Actions
1. Validate repository structure and analysis requirements
2. Execute comprehensive structural analysis following appropriate protocol
3. Generate detailed report using specified template
4. Provide prioritized recommendations and implementation roadmap
5. Validate findings and obtain user confirmation

## Error Handling
You WILL handle these scenarios:
- **Repository Access Issues**: Verify path exists and contains Java code, request correct path
- **Build System Not Recognized**: Request manual specification of module structure
- **Insufficient Permissions**: Provide clear error message and permission requirements
- **Large Repository Timeout**: Offer incremental analysis approach or focus area selection
- **Complex Dependency Cycles**: Highlight circular dependencies and provide resolution strategies
- **Unclear Service Boundaries**: Request business context or domain expert consultation
- **Missing Build Configuration**: Analyze code structure directly and note limitations

⚠️ **Critical Requirements**
- MANDATORY: Base all analysis on actual code structure and build configurations
- MANDATORY: Include quantitative metrics for all architectural assessments
- NEVER make assumptions about service boundaries without code evidence
- NEVER recommend extractions without considering data migration complexity
- ALWAYS validate dependency analysis against actual import statements
- ALWAYS provide effort estimates for recommended changes
- ALWAYS consider business impact alongside technical feasibility
- ALWAYS identify and highlight architectural violations and technical debt
