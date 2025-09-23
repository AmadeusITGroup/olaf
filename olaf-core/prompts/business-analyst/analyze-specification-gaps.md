---
name: analyze-specification-gaps
description: Analyze existing specifications from multiple stakeholder perspectives to identify critical gaps and missing requirements for successful project delivery
tags: [gap-analysis, stakeholder-analysis, specification-review, multi-perspective]
---

## Framework Validation
- Validate user has provided specification document or detailed requirements
- Ensure multi-stakeholder perspective analysis is conducted systematically
- Confirm all stakeholder viewpoints are evaluated for completeness
- Validate actionable gap identification with specific remediation steps

## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

You WILL use terminal commands, not training data for timestamps.

## Parameters
- `specification_document` (required): Path or content of the specification to analyze
- `project_name` (required): Name of the project being analyzed
- `analysis_language` (optional): Language for conducting analysis - "english", "french", "spanish", "german" (default: "english")
- `stakeholder_focus` (optional): Stakeholder selection - "all", specific numbers "1,3,5", ranges "1-6", or mixed "1,3,7-9,12" (default: prompt user for selection)
- `output_format` (optional): "interactive" or "document" (default: "document")

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- Use Act for analysis generation and gap identification
- Use Propose-Act when recommending critical remediation actions

## Execution Phase

### Language Selection
You WILL determine analysis language at start:
- If `analysis_language` parameter provided, use specified language throughout
- If not provided, ask user: "Which language would you prefer for this analysis? (English/Français/Español/Deutsch)"
- If user doesn't respond or says "default", use English
- Adapt ALL analysis content, gap descriptions, and recommendations to selected language
- Maintain consistent language throughout entire analysis

### Stakeholder Selection
You WILL present stakeholder options for user selection:
- If `stakeholder_focus` parameter provided as specific numbers or "all", use that selection
- If not provided, present the following numbered list and ask user to select:

**Available Stakeholder Perspectives:**
1. Business Requester (ROI, success metrics, competitive advantage)
2. Business Analyst (requirements completeness, traceability)
3. Technical Writer (documentation, training materials, procedures)
4. Tester (test scenarios, acceptance criteria, performance benchmarks)
5. Architect (technical architecture, integration, security)
6. Project Manager (scope, resources, timeline, risks)
7. Developer (technical specs, APIs, data models, standards)
8. Database Administrator (data architecture, performance, backup)
9. Network Engineer (network security, connectivity, monitoring)
10. Sales Team (customer impact, sales process, revenue impact)
11. Marketing & Communication (brand alignment, launch strategy)
12. UI/UX Designer (user experience, accessibility, design systems)

**Selection Instructions:**
"Please select stakeholder perspectives to analyze:
- Enter 'all' for comprehensive analysis of all 12 perspectives
- Enter specific numbers (e.g., '1,3,5' for Business Requester, Technical Writer, and Architect)
- Enter number ranges (e.g., '1-6' for perspectives 1 through 6)
- Mix formats (e.g., '1,3,7-9,12' for custom selection)"

### Multi-Stakeholder Gap Analysis Framework

You WILL systematically analyze the specification from each stakeholder perspective:

#### 1. Business Requester Perspective
**Focus Areas:**
- Business case and ROI justification
- Success metrics and KPIs
- Market positioning and competitive advantage
- Budget and timeline expectations
- Risk tolerance and mitigation strategies

**Gap Analysis Questions:**
- Is the business value clearly articulated and quantified?
- Are success criteria measurable and time-bound?
- Is the competitive positioning strategy defined?
- Are budget constraints and ROI expectations specified?
- Are business risks and mitigation strategies outlined?

#### 2. Business Analyst Perspective
**Focus Areas:**
- Requirements completeness and traceability
- Stakeholder needs coverage
- Business process alignment
- Functional specification clarity
- Change impact assessment

**Gap Analysis Questions:**
- Are all functional requirements clearly specified and testable?
- Is stakeholder impact comprehensively mapped?
- Are business processes and workflows completely defined?
- Is requirements traceability established?
- Are acceptance criteria unambiguous?

#### 3. Technical Writer Perspective
**Focus Areas:**
- User documentation requirements
- Administrative procedures
- Training material needs
- Help system specifications
- Localization requirements

**Gap Analysis Questions:**
- Are user roles and permissions clearly documented for manual creation?
- Are all user workflows documented with step-by-step procedures?
- Are administrative tasks and procedures specified?
- Are error scenarios and troubleshooting procedures defined?
- Are training and onboarding requirements specified?

#### 4. Tester Perspective
**Focus Areas:**
- Test scenario coverage
- Acceptance criteria clarity
- Performance benchmarks
- Security testing requirements
- Integration testing needs

**Gap Analysis Questions:**
- Are all functional scenarios testable with clear pass/fail criteria?
- Are performance requirements quantified for testing?
- Are security requirements testable and measurable?
- Are integration points and data flows specified for testing?
- Are edge cases and error conditions documented?

#### 5. Architect Perspective
**Focus Areas:**
- Technical architecture requirements
- Integration specifications
- Performance and scalability needs
- Security architecture
- Technology stack decisions

**Gap Analysis Questions:**
- Are non-functional requirements (performance, scalability, availability) specified?
- Are integration requirements and data flows clearly defined?
- Are security requirements and compliance needs documented?
- Are technology constraints and preferences specified?
- Is the deployment architecture and infrastructure defined?

#### 6. Project Manager Perspective
**Focus Areas:**
- Scope definition and boundaries
- Resource requirements
- Timeline and milestones
- Risk management
- Stakeholder communication plan

**Gap Analysis Questions:**
- Is project scope clearly bounded with inclusions/exclusions?
- Are resource requirements and skill sets identified?
- Are dependencies and critical path items specified?
- Are project risks and mitigation strategies defined?
- Is the stakeholder communication and approval process outlined?

#### 7. Developer Perspective
**Focus Areas:**
- Technical specifications
- API requirements
- Data model specifications
- Development standards
- Third-party integrations

**Gap Analysis Questions:**
- Are technical specifications detailed enough for implementation?
- Are data models and database requirements specified?
- Are API specifications and integration requirements clear?
- Are coding standards and development guidelines defined?
- Are third-party dependencies and constraints documented?

#### 8. Database Administrator Perspective
**Focus Areas:**
- Data architecture requirements
- Performance specifications
- Backup and recovery needs
- Security and access control
- Data migration requirements

**Gap Analysis Questions:**
- Are data volume and growth projections specified?
- Are backup, recovery, and disaster recovery requirements defined?
- Are database security and access control requirements specified?
- Are data migration and synchronization requirements clear?
- Are database performance and optimization requirements documented?

#### 9. Network Engineer Perspective
**Focus Areas:**
- Network architecture requirements
- Security and firewall needs
- Performance and bandwidth
- Integration connectivity
- Monitoring requirements

**Gap Analysis Questions:**
- Are network security requirements and protocols specified?
- Are bandwidth and performance requirements quantified?
- Are integration connectivity requirements documented?
- Are network monitoring and alerting needs defined?
- Are disaster recovery and failover requirements specified?

#### 10. Sales Team Perspective
**Focus Areas:**
- Customer impact and benefits
- Sales process integration
- Customer communication needs
- Competitive positioning
- Revenue impact

**Gap Analysis Questions:**
- Are customer benefits and value propositions clearly articulated?
- Is the impact on sales processes and customer relationships defined?
- Are customer communication and change management strategies outlined?
- Is competitive differentiation and positioning strategy specified?
- Are revenue impact projections and sales targets defined?

#### 11. Marketing & Communication Perspective
**Focus Areas:**
- Brand alignment
- Customer communication strategy
- Launch and adoption plan
- Success story development
- Market positioning

**Gap Analysis Questions:**
- Is brand alignment and messaging strategy defined?
- Are customer communication and launch plans specified?
- Is the adoption and change management strategy outlined?
- Are success metrics for marketing and communication defined?
- Is market positioning and competitive messaging strategy documented?

#### 12. UI/UX Designer Perspective
**Focus Areas:**
- User experience requirements
- Accessibility standards
- Design system specifications
- Usability testing needs
- Multi-device support

**Gap Analysis Questions:**
- Are user personas and journey maps clearly defined?
- Are accessibility requirements and standards specified?
- Are design system and branding guidelines documented?
- Are usability testing requirements and success criteria defined?
- Are multi-device and responsive design requirements specified?

## Output Format

### Document Mode (Default)
Generate comprehensive gap analysis document with the following structure:

#### Executive Summary
- Overall specification maturity assessment
- Critical gaps requiring immediate attention
- Stakeholder readiness evaluation
- Risk assessment for project success

#### Stakeholder-Specific Gap Analysis
For each stakeholder perspective:
- **Completeness Score** (0.0-1.0)
- **Critical Gaps Identified** (prioritized list)
- **Specific Missing Elements** (detailed descriptions)
- **Impact Assessment** (project risk if unresolved)
- **Recommended Actions** (specific next steps)
- **Required Stakeholder Engagement** (who to involve)

#### Consolidated Action Plan
- **Immediate Blockers** (must resolve before project start)
- **Phase 1 Requirements** (needed for development start)
- **Ongoing Clarifications** (can be resolved during development)
- **Future Enhancements** (post-MVP considerations)

#### Workshop Preparation
- **Stakeholder-Specific Question Sets** (ready for workshops)
- **Recommended Workshop Formats** (interviews, sessions, reviews)
- **Prioritized Engagement Schedule** (order of stakeholder engagement)
- **Success Criteria** (how to validate gap resolution)

### Language Adaptations
- **English**: Use template structure as-is
- **French**: Translate section headers and adapt content (e.g., "Gap Analysis" → "Analyse des Lacunes")
- **German**: Translate section headers and adapt content (e.g., "Stakeholder" → "Interessengruppen")
- **Spanish**: Translate section headers and adapt content (e.g., "Requirements" → "Requisitos")

### File Output
- Save to `[id:findings_dir]/specification-analysis/{project-name}-gap-analysis-YYYYMMDD-HHmm.json`
- Generate stakeholder-specific summary reports in markdown format
- Include workshop preparation materials as separate files
- Auto-generate unique analysis ID using timestamp format

## Success Criteria
You WILL consider the gap analysis complete when:
- [ ] All 12 stakeholder perspectives systematically evaluated
- [ ] Critical gaps identified with specific impact assessment
- [ ] Actionable remediation steps provided for each gap
- [ ] Stakeholder engagement plan created with specific next steps
- [ ] Workshop preparation materials generated and ready for use
- [ ] Overall project risk assessment completed
- [ ] Prioritized action plan created with clear timelines
- [ ] Completeness scores assigned for each stakeholder perspective

## Error Handling
- If specification is incomplete: Focus analysis on available content and flag missing sections
- If stakeholder perspective unclear: Use industry standard expectations for that role
- If language preference ambiguous: Default to English and note language selection
- If output format not specified: Generate comprehensive document mode analysis

## Critical Requirements
- MANDATORY: Analyze from ALL 12 stakeholder perspectives systematically
- MANDATORY: Provide specific, actionable gap identification with remediation steps
- NEVER skip stakeholder perspectives even if specification seems complete
- ALWAYS provide workshop preparation materials for gap resolution
- ALWAYS include impact assessment for identified gaps
- ALWAYS maintain focus on project delivery success across all stakeholder needs
- ALWAYS generate prioritized action plans with clear next steps
- ALWAYS assign realistic completeness scores based on stakeholder-specific needs
