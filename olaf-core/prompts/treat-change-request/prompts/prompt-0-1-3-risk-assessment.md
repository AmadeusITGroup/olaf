---
name: assess-change-request-risks
description: Evaluate risks across all dimensions (Business, Technical, Security, Operational) to inform sizing decisions and identify mitigation strategies
tags: [risk-assessment, business-analysis, technical-analysis, security-analysis, operational-analysis]
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
- **change_request_summary_path**: string - Path to 1-change-request-summary.md file (REQUIRED)
- **technical_scope_analysis_path**: string - Path to 2-technical-scope-analysis.md file (REQUIRED)
- **output_template_path**: string - Path to template-risk-assessment.md template (OPTIONAL, default: "../templates/template-risk-assessment.md")

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for risk assessment due to analytical nature and low modification risk

## Prerequisites (if applicable)
If this prompt is part of a workflow chain:
1. You MUST verify the preceding phase/action was completed
2. You WILL validate expected outcomes from previous step:
   - **1-change-request-summary.md** (from Prompt 0-1-1) must exist and be accessible
   - **2-technical-scope-analysis.md** (from Prompt 0-1-2) must exist and be accessible
   - Both files must contain complete analysis data for risk evaluation

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm all required input files are provided and accessible
- Validate prerequisites are met (previous workflow steps completed)
- Check access to risk assessment template file
- Verify current timestamp retrieval capability

### 2. Execution Phase

**Source Analysis:**
<!-- <input_analysis> -->
You MUST read and analyze the input files:
- **1-change-request-summary.md**: Extract business context, user impact, and change scope
- **2-technical-scope-analysis.md**: Extract technical complexity, integration points, and implementation details
<!-- </input_analysis> -->

**Risk Assessment Execution:**
<!-- <risk_evaluation> -->
You WILL execute comprehensive risk assessment across four dimensions:

**Step 1: Business Risk Assessment**
You MUST evaluate business impact and continuity risks:

1. **User Impact Risk Analysis**
   - You WILL determine affected user count and criticality
   - You MUST assess customer-facing impact severity
   - You WILL evaluate production failure consequences
   - You MUST apply rating guide: High (>1000 users, critical functionality, customer-facing), Medium (100-1000 users, internal teams), Low (<100 users, admin tools)

2. **Rollback Complexity Evaluation**
   - You WILL assess rollback feasibility and complexity
   - You MUST identify database migration reversibility constraints
   - You WILL evaluate external system dependency complications
   - You MUST apply rating guide: High (irreversible migrations, no rollback plan), Medium (coordinated rollback possible), Low (code-only, easy rollback)

3. **Business Continuity Impact**
   - You WILL determine deployment failure business impact
   - You MUST identify available workarounds
   - You WILL establish Recovery Time Objective (RTO) requirements
   - You MUST apply rating guide: High (no workaround, <1hr RTO), Medium (workaround available, <4hr RTO), Low (easy workaround, >4hr acceptable)

**Step 2: Technical Risk Assessment**
You MUST evaluate technical complexity and unknowns:

1. **Technical Complexity Analysis**
   - You WILL assess implementation complexity level
   - You MUST count affected systems and modules
   - You WILL identify architectural change requirements
   - You MUST apply rating guide: High (novel architecture, >5 modules, unknowns), Medium (3-5 modules, standard patterns with variations), Low (1-2 modules, well-known patterns)

2. **Technology Unknowns Evaluation**
   - You WILL identify new technologies being introduced
   - You MUST assess team familiarity with technology stack
   - You WILL evaluate third-party dependency risks
   - You MUST apply rating guide: High (new technology, team unfamiliar, unproven libraries), Medium (some unknowns, partial familiarity), Low (known technology, team expert)

3. **Integration Complexity Assessment**
   - You WILL count and evaluate integration points
   - You MUST identify external system involvement
   - You WILL assess event-driven communication complexity
   - You MUST apply rating guide: High (>5 integration points, external systems, async complexity), Medium (3-5 points, internal systems), Low (<3 points, synchronous, simple)

**Step 3: Security Risk Assessment**
You MUST evaluate security implications:

1. **Authentication & Authorization Analysis**
   - You WILL identify auth/authz changes required
   - You MUST assess new permission requirements
   - You WILL evaluate RBAC impact and privilege escalation risks
   - You MUST apply rating guide: High (new auth mechanism, RBAC changes, privilege escalation), Medium (new permissions, existing auth modified), Low (no auth changes or simple additions)

2. **Data Protection Evaluation**
   - You WILL identify sensitive data involvement
   - You MUST assess PII (Personal Identifiable Information) concerns
   - You WILL evaluate encryption requirements (rest/transit)
   - You MUST apply rating guide: High (PII/sensitive data, encryption changes, compliance requirements), Medium (some sensitive data, existing encryption), Low (no sensitive data, no encryption changes)

3. **Compliance & Audit Assessment**
   - You WILL identify regulatory requirements (GDPR, SOX, etc.)
   - You MUST assess audit logging requirements
   - You WILL determine compliance approval needs
   - You MUST apply rating guide: High (regulatory compliance, new audit requirements, legal review), Medium (enhanced logging, compliance documentation), Low (no compliance impact, standard logging)

**Step 4: Operational Risk Assessment**
You MUST evaluate deployment and operational concerns:

1. **Deployment Complexity Analysis**
   - You WILL assess deployment process complexity
   - You MUST identify database migration requirements
   - You WILL determine downtime requirements
   - You MUST apply rating guide: High (downtime required, multi-phase deployment, coordination needed), Medium (zero-downtime with complexity, migration scripts), Low (simple deployment, no downtime, single-step)

2. **Monitoring & Observability Evaluation**
   - You WILL identify new monitoring metric requirements
   - You MUST assess issue detection capabilities
   - You WILL determine alerting requirements
   - You MUST apply rating guide: High (new metrics required, poor visibility, alerting gaps), Medium (some new metrics, good visibility), Low (existing metrics sufficient, excellent visibility)

3. **Support & Maintenance Assessment**
   - You WILL evaluate post-deployment support complexity
   - You MUST determine runbook requirements
   - You WILL assess on-call impact
   - You MUST apply rating guide: High (complex support, new runbooks, high on-call risk), Medium (moderate support, runbook updates), Low (easy to support, existing runbooks, minimal on-call risk)
<!-- </risk_evaluation> -->

**Risk Aggregation and Prioritization:**
<!-- <risk_aggregation> -->
You WILL aggregate risk levels for each dimension:
- **Business Risk Level**: High if any High, Medium if any Medium, else Low
- **Technical Risk Level**: High if any High, Medium if any Medium, else Low  
- **Security Risk Level**: High if any High, Medium if any Medium, else Low
- **Operational Risk Level**: High if any High, Medium if any Medium, else Low

You MUST identify and prioritize top 5 risks with specific mitigation strategies.
You WILL create comprehensive risk matrix showing all assessed risks.
<!-- </risk_aggregation> -->

### 3. Validation Phase
You WILL validate the risk assessment meets all requirements:
- Confirm all 4 risk dimensions assessed completely
- Verify each dimension has clear risk level (High/Medium/Low)
- Ensure risk assessments are specific to the change request (not generic)
- Validate mitigation strategies are actionable and realistic
- Confirm top 5 risks are properly prioritized
- Verify risk matrix is complete and accurate
- Ensure output follows template structure exactly

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Complete risk assessment using **../templates/template-risk-assessment.md** structure
- Risk dimension summaries: Business, Technical, Security, Operational with clear ratings
- Top 5 prioritized risks with specific mitigation strategies
- Comprehensive risk matrix showing all identified risks
- Actionable recommendations for risk mitigation

## User Communication

### Progress Updates
You WILL provide these status confirmations:
- Confirmation when input files are successfully read and analyzed
- Confirmation when each risk dimension assessment is completed
- Status update when risk aggregation and prioritization is finished
- Validation results confirming assessment completeness and accuracy

### Completion Summary
You WILL provide comprehensive completion summary:
- Risk assessment results with clear risk levels for all dimensions
- Top 5 prioritized risks with mitigation strategies
- Overall risk profile for the change request
- Specific recommendations for proceeding with implementation
- Confirmation of workflow step completion: "Step 1.3 complete. Workflow 0-1 finished. Ready for Workflow 0-2 (Size Evaluation)."

### Next Steps
You WILL clearly define:
- Risk assessment deliverable ready for use in sizing decisions
- Transition to next workflow: `../workflows/workflow-0-2-size-evaluation.md`
- Risk mitigation actions required before proceeding
- Stakeholder communication requirements for high-risk items

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER provide generic risk assessments - all assessments MUST be specific to the analyzed change request
- Rule 2: Risk ratings MUST follow the provided rating guides exactly (High/Medium/Low criteria)
- Rule 3: Each risk dimension MUST be assessed independently before aggregation
- Rule 4: Top 5 risks MUST include risks from multiple dimensions when applicable
- Rule 5: Mitigation strategies MUST be actionable and specific (not theoretical)
- Rule 6: Risk matrix MUST include all identified risks, not just the top 5
- Rule 7: Output MUST follow the template structure exactly without deviation
- Rule 8: Assessment MUST be based on information from required input files

## Success Criteria
You WILL consider the task complete when:
- [ ] All 4 risk dimensions assessed (Business, Technical, Security, Operational)
- [ ] Each dimension has a clear risk level (High/Medium/Low) with specific justification
- [ ] Risk assessments are specific to the change request (not generic)
- [ ] Mitigation strategies are actionable and realistic
- [ ] Top 5 risks are prioritized with clear ranking rationale
- [ ] Risk matrix is complete showing all identified risks
- [ ] Output follows template structure exactly
- [ ] Assessment is based on actual input file content
- [ ] Validation confirms 100% completeness and accuracy
- [ ] Workflow completion declared: "Step 1.3 complete. Workflow 0-1 finished. Ready for Workflow 0-2 (Size Evaluation)."

## Required Actions
1. Validate all required input parameters and file accessibility
2. Execute comprehensive risk assessment across all four dimensions
3. Generate outputs in specified template format
4. Provide user communication and workflow completion confirmation
5. Declare readiness for next workflow phase

## Error Handling
You WILL handle these scenarios:
- **Input File Access Failed**: Provide clear error message and request valid file paths for 1-change-request-summary.md and 2-technical-scope-analysis.md
- **Template File Access Failed**: Provide clear error message and use embedded template structure as fallback
- **Incomplete Input Data**: Request additional information needed for comprehensive risk assessment
- **Risk Rating Ambiguity**: Apply conservative approach (higher risk level) and document assumptions
- **Mitigation Strategy Gaps**: Research and provide industry-standard mitigation approaches
- **Risk Matrix Complexity**: Break down complex risks into component parts for clearer assessment
- **Template Compliance Validation Failed**: Iterate output formatting to match template exactly
- **Workflow Transition Requirements Not Met**: Identify missing elements and request completion before proceeding

WARNING: **Critical Requirements**
- MANDATORY: All 4 risk dimensions MUST be assessed completely
- MANDATORY: Risk levels MUST follow provided rating guides exactly  
- NEVER provide generic risk assessments - all MUST be change-request specific
- NEVER skip mitigation strategies - all high and medium risks require actionable mitigation
- ALWAYS base assessment on actual input file content, not assumptions
- ALWAYS validate output against template structure before completion
- ALWAYS declare workflow completion status clearly
- NEVER proceed to next workflow without completing all success criteria