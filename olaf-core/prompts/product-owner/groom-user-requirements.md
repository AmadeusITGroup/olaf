---
name: groom-user-requirements
description: Systematically analyze, cluster, and prioritize user requirements from GitHub issues based on a product vision to create a strategic delivery roadmap
tags: [requirements, grooming, github, product-vision, clusterization, prioritization]
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

You WILL use terminal commands, not training data for timestamps.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **github_repository**: string - Full repository URL or owner/repo format (REQUIRED)
- **product_vision_location**: string - Absolute path to the product vision document (REQUIRED)
- **issue_status_filter**: string - Issue statuses to consider for product owner review (REQUIRED)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Act protocol for clusterization review and prioritization constraints

## Prerequisites
You MUST verify these requirements before proceeding:
1. GitHub MCP server must be installed and configured
2. Access to the GitHub repository containing the issues
3. Product vision document must be available and accessible

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm all required parameters are provided (github_repository, product_vision_location, issue_status_filter)
- Validate GitHub MCP server is installed and configured
- Verify GitHub repository access through MCP server
- Confirm product vision document exists and is readable
- Validate issue status filters are appropriate

### 2. Execution Phase

<!-- <requirements_gathering_phase> -->
**Phase 1: Requirements Gathering**

You WILL execute these operations:
1. Use GitHub MCP server to connect to the specified repository
2. Filter issues based on the provided status criteria
3. Extract relevant issue data including:
   - Issue ID and title
   - Current status/labels
   - Description/body content
   - Comments (if relevant for understanding requirements)
   - Creation and update dates
   - Assignees and milestone information
4. Create a structured list of all relevant issues with their metadata for analysis
<!-- </requirements_gathering_phase> -->

<!-- <clusterization_phase> -->
**Phase 2: Requirements Clusterization**

You WILL execute these operations:
1. Read and analyze the product vision document
2. Extract key themes, objectives, and strategic priorities
3. Identify user personas and value propositions
4. Note any specific strategic constraints or priorities mentioned
5. Use the `user-requirement-clusterization-template.md` from `[id:templates_dir]/product-owner/`
6. Apply clustering methodology based on:
   - Functional similarity
   - User persona alignment
   - Technical domain grouping
   - Business value area alignment
   - Product vision theme alignment
7. Group requirements into logical clusters
8. Identify duplicate requirements (mark but preserve all)
9. Document cluster characteristics and vision alignment
10. Note any requirements that don't fit existing clusters
11. Identify cross-cluster dependencies
12. Complete clusterization analysis document following the template structure
13. Save clusterization analysis as `requirements-clusterization-analysis-[YYYYMMDD-HHmm].md`

**User Review Checkpoint:**
You MUST present the clusterization results to the user for review using Propose-Act protocol:
1. **Cluster Accuracy**: Are the groupings logical and appropriate?
2. **Missing Clusters**: Should any additional clusters be created?
3. **Misplaced Requirements**: Are any requirements in the wrong cluster?
4. **Duplicate Handling**: Agreement on how to handle identified duplicates?
5. **Vision Alignment**: Confirmation of cluster alignment with product vision?

You MUST NOT proceed to prioritization until user confirms clusterization is acceptable.
You WILL make any requested adjustments to clustering before proceeding.
You MUST document any user-requested changes and rationale.
<!-- </clusterization_phase> -->

<!-- <prioritization_phase> -->
**Phase 3: Requirements Prioritization**

You MUST gather prioritization constraints using Propose-Act protocol:
1. **Strategic Constraints**: Are there any specific clusters or requirements that MUST be top priority regardless of scoring?
2. **Timeline Constraints**: Any fixed deadlines or market windows?
3. **Resource Constraints**: Development team capacity, budget, or expertise limitations?
4. **Regulatory/Compliance**: Any requirements driven by external compliance needs?
5. **Dependency Constraints**: Any technical or business dependencies that affect sequencing?

You WILL document constraints:
- Record all constraints with clear rationale
- Note when constraints override natural prioritization scoring
- Identify any conflicts between constraints and product vision alignment

You WILL execute prioritization operations:
1. Use the `user-requirement-prioritization-template.md` from `[id:templates_dir]/product-owner/`
2. Apply prioritization framework considering:
   - Product vision alignment scoring
   - Business value assessment
   - User impact analysis
   - Technical feasibility evaluation
   - Strategic constraints
3. Score each cluster and requirement using defined criteria
4. Apply strategic constraints to adjust priorities where needed
5. Create delivery sequence considering dependencies
6. Develop phased roadmap with clear milestones
7. Assess risks and create contingency scenarios
8. Document rationale for all prioritization decisions
9. Complete prioritization analysis document following the template structure
10. Save prioritization analysis as `requirements-prioritization-analysis-[YYYYMMDD-HHmm].md`

You WILL present the final prioritized roadmap including:
1. **Executive Summary**: High-level roadmap overview
2. **Priority Levels**: Clear categorization of requirement priorities
3. **Delivery Phases**: Recommended implementation sequence with timelines
4. **Constraint Impact**: How strategic constraints influenced the prioritization
5. **Risk Assessment**: Key risks and mitigation strategies
6. **Success Metrics**: How to measure roadmap success
7. **Review Process**: Recommended schedule for roadmap updates
<!-- </prioritization_phase> -->

### 3. Validation Phase
You WILL validate results:
- Confirm all GitHub issues in scope have been analyzed
- Verify product vision alignment is clearly documented for each cluster
- Validate user has reviewed and approved clusterization
- Confirm strategic constraints are properly documented and applied
- Verify dependencies are identified and sequenced appropriately
- Validate duplicate handling strategy is clear and consistent
- Confirm roadmap phases are realistic and achievable
- Verify risk mitigation strategies are included
- Validate success metrics are defined and measurable

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Strategic roadmap with phased delivery plan
- Requirements Inventory: Complete list of analyzed GitHub issues
- Clusterization Analysis: Save as `requirements-clusterization-analysis-[YYYYMMDD-HHmm].md` using `[id:templates_dir]/product-owner/user-requirement-clusterization-template.md`
- Prioritization Analysis: Save as `requirements-prioritization-analysis-[YYYYMMDD-HHmm].md` using `[id:templates_dir]/product-owner/user-requirement-prioritization-template.md`
- Risk Assessment: Identified risks and mitigation strategies included in prioritization analysis

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when GitHub issues extraction completes
- Confirmation when product vision analysis completes
- Status of clusterization analysis with cluster count
- Confirmation when user approves clusterization
- Status of prioritization constraints gathering
- Confirmation when prioritization analysis completes
- Timestamp identifier used: YYYYMMDD-HHmm format

### Completion Summary
- Summary of total requirements analyzed
- Number of clusters created with vision alignment scores
- Priority distribution across requirement levels
- Key constraints that influenced prioritization
- Final roadmap phases with delivery timelines

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER proceed to prioritization without user approval of clusterization
- Rule 2: ALWAYS preserve duplicate requirements while marking them clearly
- Rule 3: ALWAYS apply strategic constraints even when they override analytical scoring
- Rule 4: ALWAYS document rationale for constraint-driven priority overrides
- Rule 5: ALWAYS ensure GitHub MCP server connectivity before starting
- Rule 6: ALWAYS validate product vision document accessibility before proceeding

## Success Criteria
You WILL consider the task complete when:
- [ ] All required parameters validated and GitHub connectivity confirmed
- [ ] All relevant GitHub issues extracted and structured
- [ ] Product vision analyzed and themes extracted
- [ ] Requirements clustered with clear vision alignment
- [ ] User has reviewed and approved clusterization approach
- [ ] Strategic constraints gathered and documented
- [ ] Requirements prioritized using template framework
- [ ] Phased roadmap created with realistic timelines
- [ ] Risk assessment completed with mitigation strategies
- [ ] All deliverables generated following template structures

## Required Actions
1. Validate all required input parameters and GitHub MCP server connectivity
2. Execute three-phase process following Propose-Act protocol for user interactions
3. Generate all outputs using specified template structures
4. Provide comprehensive user communication throughout process
5. Ensure all validation criteria are met before completion

## Error Handling
You WILL handle these scenarios:
- **GitHub Access Issues**: Verify MCP server configuration and repository permissions, provide troubleshooting steps
- **Product Vision Not Found**: Request correct path or guide user to create vision using existing template
- **Unclear Issue Status**: Work with user to define appropriate status filters with examples
- **Conflicting Constraints**: Facilitate user decision on constraint priorities with trade-off analysis
- **Large Issue Volume**: Suggest filtering by labels, milestones, or date ranges to manage scope
- **Clusterization Rejection**: Iterate clustering approach based on specific user feedback
- **Circular Dependencies**: Identify dependency conflicts and request user guidance on resolution
- **Resource Constraint Conflicts**: Highlight impossible scenarios and request constraint adjustments

⚠️ **Critical Requirements**
- MANDATORY: Follow Propose-Act protocol for clusterization review and prioritization constraints
- MANDATORY: Use specified templates for all analysis documents
- NEVER proceed without user approval at designated checkpoints
- NEVER modify original GitHub issues or repository content
- ALWAYS preserve all requirements including duplicates with clear marking
- ALWAYS document constraint rationale when overriding analytical scoring
- ALWAYS ensure product vision alignment is maintained throughout process
*Last Updated: 20241004-1040 Central European Time*
