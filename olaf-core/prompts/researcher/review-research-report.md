---
name: review-research-report
description: Conduct systematic quality review of research reports against their original research plans
tags: [research, review, quality-assurance, validation]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.
 

## Input Parameters
You MUST request these parameters if not provided by the user:
- **research_plan_path**: string - Absolute path to original research plan document (REQUIRED)
- **research_report_path**: string - Absolute path to completed research report (REQUIRED)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for systematic review process

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm research plan file exists and is accessible
- Confirm research report file exists and is accessible
- Validate both files are readable and contain structured content

### 2. Execution Phase

**Document Analysis:**
<!-- <document_preparation> -->
You WILL read both documents completely:
- Extract research plan structure and requirements
- Map plan chapters to report sections
- Identify all deliverable requirements from plan
<!-- </document_preparation> -->

**Tasklist Generation:**
<!-- <tasklist_creation> -->
You WILL create comprehensive review tasklist using this structure:
```markdown
# Research Report Review Tasklist - [Report Name]
**Created**: YYYYMMDD-HHmm CEDT

## Overall Structure Analysis: [ ] Complete
## Chapter-by-Chapter Reviews:
- [ ] Chapter 1: [Title] - Style & Format
- [ ] Chapter 1: [Title] - Source Analysis
- [ ] Chapter 2: [Title] - Style & Format  
- [ ] Chapter 2: [Title] - Source Analysis
[Continue for all chapters]
## Final Compilation: [ ] Complete
```
<!-- </tasklist_creation> -->

**Chapter-by-Chapter Review:**
<!-- <systematic_review> -->
You WILL conduct dual analysis for each chapter:

**Style & Format Review:**
- You MUST search systematically for spelling/grammar issues using grep/search patterns
- You WILL check sentence structure, word choice, technical expression accuracy
- You MUST verify consistent terminology, voice, and formatting throughout chapter
- You WILL ensure accurate technical language and current terminology for 2025

**Content Structure Analysis:**
- You WILL evaluate overall clarity, conciseness, professional tone
- You MUST verify section organization and completeness vs. original plan requirements
- You WILL check technical accuracy, current tools, version numbers
- You MUST ensure appropriate complexity for target developer audience

**Source Analysis:**
- You WILL examine every source citation in the chapter
- You MUST verify specificity: URLs, documentation references, publication details
- You WILL check recency: All sources must demonstrate current 2025 data
- You MUST flag generic sources without specific attribution
- You WILL validate evidence of actual web research vs. training data
<!-- </systematic_review> -->

**Core Logic**: You WILL execute following protocol requirements
- You WILL process ONE chapter at a time systematically
- You MUST present findings directly in chat conversation
- You WILL document specific improvements in accumulated findings
- You MUST wait for user approval before proceeding to next chapter
- You WILL update both tasklist and improvement actions after each chapter

### 3. Validation Phase
You WILL validate review completeness:
- Confirm all chapters reviewed according to dual analysis criteria
- Verify all findings documented with specific improvement actions
- Ensure tasklist completion status accurately reflects progress

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Two tracking documents only
- Review Tasklist: `[report-name]-review-tasklist.md` in `[id:findings_dir]reports/`
- Improvement Actions: `[report-name]-improvement-actions.md` in `[id:findings_dir]reports/`
- Chat conversation: Direct presentation of chapter findings

## User Communication

### Progress Updates
- Confirmation when documents are successfully read and analyzed
- Confirmation when tasklist is generated and improvement actions document created
- Status updates after each chapter review completion
- Validation results for systematic review process

### Completion Summary
- Summary of total chapters reviewed and findings identified
- Location of tracking documents created
- Count of specific improvement actions documented
- Overall quality assessment of research report

### Next Steps
You WILL clearly define:
- Complete improvement actions list ready for implementation
- Tracking documents location: `[id:findings_dir]reports/`
- Systematic review process completed successfully
- Research report quality assessment finalized

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER create additional analysis files per chapter beyond the two tracking documents
- Rule 2: You MUST process chapters sequentially, one at a time
- Rule 3: You MUST wait for user approval before proceeding to next chapter
- Rule 4: You MUST flag ALL generic sources without specific attribution immediately
- Rule 5: You MUST use systematic search methods to identify language quality issues
- Rule 6: You MUST document specific, actionable improvements for each issue found
- Rule 7: You MUST present findings directly in chat conversation, not separate files
- Rule 8: You MUST maintain running list of LLM-implementable corrections

## Success Criteria
You WILL consider the task complete when:
- [ ] Both research plan and report successfully read and analyzed
- [ ] Comprehensive review tasklist generated with all chapters mapped
- [ ] Improvement actions document created for accumulating findings
- [ ] All chapters reviewed using dual analysis approach (style/format + sources)
- [ ] All findings presented in chat conversation with user approval
- [ ] Both tracking documents updated with completion status
- [ ] Final comprehensive summary provided with improvement actions list
- [ ] Systematic review process validated for completeness

## Required Actions
1. Validate all required input parameters and file accessibility
2. Execute systematic review following chapter-by-chapter approach
3. Generate tracking documents in specified format and location
4. Provide user communication and approval confirmations
5. Document specific improvement actions for each issue identified

## Error Handling
You WILL handle these scenarios:
- **File Access Issues**: Provide clear error message and request valid file paths
- **Invalid File Format**: Request properly structured research plan/report files
- **Missing Chapter Structure**: Adapt review approach and document limitations
- **User Approval Timeout**: Allow session restart and resume from last completed chapter
- **Generic Source Detection**: Flag immediately and document specific attribution requirements
- **Language Quality Issues**: Use systematic search patterns and document specific corrections
- **Incomplete Review**: Stop process and request user guidance on acceptable modifications

⚠️ **Critical Requirements**
- MANDATORY: Follow systematic chapter-by-chapter review approach
- MANDATORY: Wait for user approval before proceeding to next chapter
- NEVER create additional analysis files beyond two tracking documents
- NEVER proceed without user approval during iterative review process
- ALWAYS use systematic search methods for language quality analysis
- ALWAYS flag generic sources without specific attribution
- ALWAYS document specific, actionable improvements for LLM implementation
- ALWAYS present findings directly in chat conversation
