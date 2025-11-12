---
name: check-prompt-compliance
description: Check and validate prompts for template compliance and effectiveness
tags: [prompt, compliance, validation, analysis, quality]
---

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read  the full 
.olaf/olaf-core/reference/.condensed/olaf-framework-condensed.md.


## Input Parameters
You MUST request these parameters if not provided by the user:
- **target_prompt_path**: string - Path to the prompt file to analyze (REQUIRED)
- **target_competency**: string - Which competency the prompt belongs to (OPTIONAL - auto-detected from path if possible, manual selection if needed)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act for analysis since it's non-destructive review
- You WILL use Propose-Act for any improvement suggestions that affect prompt structure

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm target prompt file exists and is accessible
- **Path Analysis**: You WILL extract competency from `[target_prompt_path]` if provided as full path
  - Parse path structure: `[id:competencies_dir]/[extracted_competency]/prompts/[filename]`
  - If competency successfully extracted from path, use automatically
  - If path parsing fails or competency parameter provided separately, proceed with manual selection
- You MUST list available competencies by reading directory structure: `[id:competencies_dir]` (only if competency not detected from path)
- You WILL present competency options to user and request selection only if automatic detection fails
- Check access to required template and principles reference files
- Validate analysis parameters are within acceptable ranges

**Competency Detection Logic:**
<!-- <path_parsing> -->
You WILL attempt automatic competency extraction:
1. Check if `[target_prompt_path]` contains `[id:competencies_dir]` base path
2. Extract directory structure between base path and filename
3. Use first directory level as competency (e.g., `competencies/developer/prompts/test.md` → `developer`)
4. Validate extracted competency exists in available options
5. If validation fails, fall back to manual selection process
<!-- </path_parsing> -->

### 2. Execution Phase

**Source Analysis:**
<!-- <prompt_analysis> -->
You MUST read and thoroughly analyze: `[target_prompt_path]`
You WILL extract and evaluate:
- Structural elements: name, description, tags, sections present
- Input parameters: completeness, clarity, requirement designation
- Process logic: step organization, imperative language usage
- Error handling: scenario coverage, user guidance quality
- Success criteria: measurability, completeness
- User communication: clarity, progress tracking
- Domain-specific rules: appropriateness, enforcement mechanisms
<!-- </prompt_analysis> -->

**Template Compliance Assessment:**
<!-- <template_compliance> -->
You MUST read and compare against: `[id:competencies_dir]prompt-engineer/templates/prompt-template.md`
You WILL check for presence and quality of:
- Time Retrieval section with proper command structure
- Input Parameters with REQUIRED/OPTIONAL designation
- User Interaction Protocol specification
- Process with Validation/Execution/Validation phases
- Output Format specification
- User Communication structure
- Domain-Specific Rules with enforcement
- Success Criteria checklist format
- Error Handling comprehensive scenarios
- Critical Requirements section
<!-- </template_compliance> -->

**Principles Adherence Evaluation:**
<!-- <principles_evaluation> -->
You MUST read and apply: `[id:competencies_dir]prompt-engineer/templates/prompting-principles.md`
You WILL assess adherence to:
- Imperative language consistency ("You WILL", "You MUST")
- Clarity and specificity of instructions
- Logical flow and organization
- XML markup usage for complex sections
- Actionable guidance provision
- Ambiguity elimination
- Context sufficiency
<!-- </principles_evaluation> -->

**Enhanced Critical Analysis:**
<!-- <intelligent_analysis> -->
You WILL apply advanced analysis beyond basic compliance:
- **Execution Feasibility**: Assess whether instructions can be practically followed
- **Edge Case Coverage**: Identify scenarios not addressed by current error handling
- **User Experience Quality**: Evaluate clarity and helpfulness from user perspective
- **Workflow Integration**: Analyze how prompt fits within broader task sequences
- **Scalability Assessment**: Determine if prompt works across different complexity levels
- **Performance Optimization**: Identify opportunities for more efficient execution
- **Contextual Appropriateness**: Evaluate alignment with intended use cases
- **Innovation Opportunities**: Suggest enhancements beyond template compliance
<!-- </intelligent_analysis> -->

### 3. Validation Phase
You WILL validate analysis completeness and accuracy:
- Confirms all template sections were evaluated
- Verifies principles assessment covers all key areas
- Ensures enhanced analysis provides actionable insights
- Validates improvement recommendations are specific and implementable
- Confirms analysis depth matches requested level
- Verifies output format meets user specifications

## Output Format
You WILL generate outputs based on requested format:

**Summary Format:**
- Compliance score (0-100%) with breakdown by category
- Top 3 strengths and top 3 improvement areas
- Overall recommendation: "Compliant", "Needs Minor Updates", "Requires Significant Revision"

**Detailed Format:**
- Complete compliance checklist with pass/fail status
- Detailed findings for each template section
- Principles adherence assessment with specific examples
- Enhanced critical analysis with intelligent recommendations
- Prioritized improvement suggestions with implementation guidance

**Checklist Format:**
- Binary checklist of all template requirements
- Principles compliance status indicators
- Quick reference improvement action items

## User Communication

### Progress Updates
You WILL provide clear status throughout analysis:
- Confirmation when target prompt is successfully loaded and parsed
- Status of sub-category detection (automatic or manual selection required)
- Status of template and principles file access
- Progress through each analysis phase (structural, compliance, principles, enhanced)
- Completion of analysis with summary statistics

### Analysis Results Delivery
You WILL present findings in requested format:
- **Compliance Summary**: Overall adherence percentage and category breakdown
- **Strengths Identification**: Elements that exemplify best practices
- **Gap Analysis**: Missing or inadequate template sections
- **Principles Assessment**: Specific adherence examples and violations
- **Enhanced Insights**: Intelligent analysis beyond basic compliance
- **Improvement Roadmap**: Prioritized recommendations with effort estimates

### Next Steps Guidance
You WILL clearly define recommended actions:
- High-priority fixes for critical compliance gaps
- Medium-priority enhancements for improved effectiveness
- Low-priority optimizations for advanced functionality
- Optional innovations for enhanced user experience
- Timeline suggestions for implementation phases

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER modify the target prompt file during analysis
- Rule 2: Analysis MUST be objective and evidence-based
- Rule 3: Compliance assessment MUST reference specific template sections
- Rule 4: Improvement suggestions MUST be actionable and specific
- Rule 5: Enhanced analysis MUST provide value beyond basic compliance checking
- Rule 6: Criticism MUST be constructive with solution-oriented recommendations
- Rule 7: Analysis depth MUST match user-specified level
- Rule 8: Output format MUST conform to user selection
- Rule 9: Sub-category detection MUST validate against actual directory structure
- Rule 10: Path parsing failures MUST trigger graceful fallback to manual selection

## Success Criteria
You WILL consider the task complete when:
- [ ] Target prompt successfully read and parsed
- [ ] Sub-category correctly identified (automatic detection or manual selection)
- [ ] Template compliance assessment completed for all sections
- [ ] Principles adherence evaluation finished with specific findings
- [ ] Enhanced critical analysis provides intelligent insights beyond compliance
- [ ] Improvement recommendations are specific, actionable, and prioritized
- [ ] Analysis results delivered in requested format
- [ ] User communication provides clear understanding of findings
- [ ] Next steps guidance offers concrete implementation roadmap
- [ ] All domain-specific rules followed throughout analysis

## Required Actions
1. Validate all input parameters and file accessibility
2. Execute automatic sub-category detection with fallback mechanism
3. Execute comprehensive analysis following specified depth
4. Generate outputs in user-requested format
5. Provide clear communication of findings and recommendations
6. Define actionable next steps for prompt improvement

## Error Handling
You WILL handle these scenarios:
- **Target File Access Failed**: Provide clear error message and request valid file path
- **Sub-category Auto-Detection Failed**: Gracefully fall back to manual selection with clear explanation
- **Invalid Manual Sub-category Selection**: Re-present valid options and request selection
- **Template/Principles Reference Failed**: Provide error message with manual alternatives
- **Parsing Errors in Target Prompt**: Identify specific formatting issues preventing analysis
- **Incomplete Analysis Due to Missing Sections**: Provide partial results with clear gaps identified
- **Output Format Generation Failed**: Offer alternative formats and manual formatting guidance
- **Analysis Inconsistencies**: Re-evaluate findings and provide consolidated assessment
- **User Confusion About Results**: Provide clarification and simplified explanations
- **Path Structure Validation Failed**: Provide clear error about expected directory structure

⚠️ **Critical Requirements**
- MANDATORY: Analysis MUST be thorough and evidence-based
- MANDATORY: Enhanced analysis MUST provide value beyond basic compliance
- MANDATORY: Sub-category detection MUST validate against actual directory structure
- NEVER modify target prompt files during analysis
- NEVER provide superficial or generic improvement suggestions
- ALWAYS ground recommendations in specific findings
- ALWAYS provide actionable guidance with implementation details
- ALWAYS maintain objectivity while being constructively critical
- ALWAYS validate path parsing results against directory structure
- NEVER compromise analysis quality for speed or convenience
