---
name: assess-genai-solution
description: Conduct comprehensive assessment of GenAI solution requests through structured questionnaire and research
tags: [genai, assessment, questionnaire, research]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.


## Input Parameters
You MUST request these parameters if not provided by the user:
- **assessment_scope**: string - Specific GenAI use case or problem domain (REQUIRED)
- **stakeholder_context**: string - Primary users and organizational context (OPTIONAL)
- **timeline_constraints**: string - Expected implementation timeline (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Confirm-Act protocol for comprehensive assessment process

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm user is ready to complete comprehensive questionnaire
- Validate assessment scope is clearly defined
- Check access to web search capabilities for research phase

### 2. Execution Phase

**Questionnaire Collection:**
<!-- <questionnaire_phase> -->
You WILL collect responses to these structured questions:

**Core Problem Analysis:**
1. What is the core problem or opportunity you want GenAI to address?
2. Why is solving this important now? What is the impact if not addressed?
3. Briefly describe your current process or workflow for this need.
4. Where do you see GenAI providing the most value or automation?

**User and Impact Analysis:**
5. Who are the main users? What are their daily tasks and pain points?
6. What specific outcomes or improvements do you expect from GenAI?
7. What solutions (manual, digital, or AI) have you tried or considered?
8. Why did previous or alternative solutions not meet your needs?

**Business and Technical Constraints:**
9. If funding is needed, what are the expected business benefits and target market?
10. Are there any data, compliance, or integration constraints to consider?
<!-- </questionnaire_phase> -->

**Data Processing and Review:**
<!-- <data_review_phase> -->
You WILL process collected responses:
1. Generate simple initiative name (3 words maximum)
2. Create `[initiative_name]-data.md` file with structured responses
3. Present to user for review and sign-off
4. Analyze responses for ambiguities, generic information, or gaps
5. Rate issues as Critical, Important, or Suggestion
6. If critical issues found, request clarification before proceeding
<!-- </data_review_phase> -->

**Research and Analysis:**
<!-- <research_phase> -->
You WILL conduct comprehensive research:
1. Summarize key points from validated responses
2. Search web for similar initiatives across multiple platforms:
   - GitHub repositories
   - Medium articles
   - Reddit discussions
   - Industry publications
   - Academic papers (up to 5 total sources)
3. Document alternatives and challenges in `[initiative_name]-data.md`
4. Identify implementation challenges (technical, organizational, ethical)
5. Challenge the proposal with alternative approaches
6. Request user justification for rejecting alternatives
<!-- </research_phase> -->

**Core Logic**: You WILL execute following protocol requirements
- You MUST obtain user confirmation before proceeding between major phases
- You WILL maintain structured documentation throughout process
- You MUST validate completeness before final recommendations
- You WILL provide comprehensive analysis with actionable insights

### 3. Validation Phase
You WILL validate assessment completeness:
- Confirm all questionnaire responses collected and reviewed
- Verify research conducted across required platforms
- Ensure challenges and alternatives thoroughly documented
- Validate final recommendations are actionable and well-supported

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: `[initiative_name]-data.md` with structured chapters:
  - Initiative Overview
  - Questionnaire Responses
  - Alternatives and Challenges
  - Implementation Challenges
  - Conclusion and Recommendations
- Supporting documentation: Research sources and validation notes

## User Communication

### Progress Updates
- Confirmation when questionnaire phase is complete
- Status update when data review and validation is finished
- Confirmation when research phase is complete with source count
- Validation results for final assessment completeness

### Completion Summary
- Summary of initiative assessment with key findings
- Location of comprehensive assessment document
- Count of alternatives researched and challenges identified
- Final recommendation with next steps

### Next Steps
You WILL clearly define:
- Complete GenAI solution assessment ready for decision-making
- Assessment document location with all supporting research
- Recommended implementation approach or alternative solutions
- Specific next actions for stakeholders

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: You MUST obtain user sign-off before proceeding to research phase
- Rule 2: You MUST rate all identified issues as Critical, Important, or Suggestion
- Rule 3: You MUST search minimum 5 sources across specified platforms
- Rule 4: You MUST challenge the proposal with alternative approaches
- Rule 5: You MUST document all findings in structured format
- Rule 6: You MUST provide actionable recommendations based on complete analysis
- Rule 7: You NEVER proceed with critical gaps in questionnaire responses
- Rule 8: You MUST validate user justification for rejecting alternatives

## Success Criteria
You WILL consider the task complete when:
- [ ] All 10 questionnaire questions answered completely
- [ ] Initiative name generated and data file created
- [ ] User review and sign-off obtained for responses
- [ ] Response quality analysis completed with issue ratings
- [ ] Web research conducted across minimum 5 sources
- [ ] Alternatives and challenges documented comprehensively
- [ ] Implementation challenges identified and analyzed
- [ ] Alternative approaches proposed and user justification obtained
- [ ] Final recommendations provided with actionable next steps
- [ ] Complete assessment document delivered with all chapters

## Required Actions
1. Validate user readiness and assessment scope definition
2. Execute structured questionnaire collection with quality review
3. Generate comprehensive research across multiple platforms
4. Provide challenge analysis and alternative solution evaluation
5. Deliver actionable recommendations with supporting documentation

## Error Handling
You WILL handle these scenarios:
- **Incomplete Questionnaire Responses**: Request specific missing information with guidance
- **Critical Quality Issues**: Stop process and request clarification before research phase
- **Web Search Failures**: Provide alternative research methods and manual guidance
- **User Rejection of Alternatives**: Document justification and proceed with original proposal
- **Insufficient Research Sources**: Expand search criteria and platforms until minimum met
- **Unclear Initiative Scope**: Request refined problem definition and use case clarification
- **Documentation Access Issues**: Provide alternative file creation methods

⚠️ **Critical Requirements**
- MANDATORY: Follow Propose-Confirm-Act protocol for major phase transitions
- MANDATORY: Obtain user sign-off before proceeding to research phase
- NEVER proceed with critical gaps in questionnaire responses
- NEVER skip alternative solution analysis and challenge phase
- ALWAYS document findings in structured format with clear chapters
- ALWAYS provide actionable recommendations based on complete analysis
- ALWAYS validate user justification for rejecting proposed alternatives
- ALWAYS ensure minimum research source requirements are met
