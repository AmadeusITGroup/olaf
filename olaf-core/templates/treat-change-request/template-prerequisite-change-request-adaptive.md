# Change Request Document - Adaptive Template

**NOTE**: This is a REFERENCE template, not a rigid structure to force. Adapt sections to match the actual demand type.

---

## Header (Always Include)

```markdown
# Change Request: [Title from Source]

**Generated From**: Prerequisite Orchestrator  
**Analysis Date**: [Date]  
**Demand Type**: [Epic|User Story|Bug|Documentation|Clarification|Tech Debt|Config|Other]  
**Source Documents**: [N documents from folder path]

---

## Document Status

**Demand Classification**: [Type identified in Step 1]  
**Structure in Source**: [Epic/Feature/Story | Flat Requirements | Bug Report | etc.]  
**Completeness**: ✅ Complete / ⚠️ Partial / ❌ Incomplete  
**Ready for Routing**: ✅ Yes / ❌ No

---
```

---

## Core Demand Section (Adapt to Type)

### For Epic-Based Demands

```markdown
## 1. Epic Overview

**Epic ID**: [ID from source]  
**Epic Title**: [Title]

### Description
[Verbatim description]

### Goals/Objectives
- [Goal 1]
- [Goal 2]

### Business Value
[Value proposition, WSJF, priority, etc.]

### Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]

---

## 2. Features (if applicable)

[Include ONLY if features are explicitly structured in source]

### Feature 1: [Name]
- Description: [Verbatim]
- Acceptance Criteria: [List]
- Technical Requirements: [List]

---

## 3. User Stories (if applicable)

[Include ONLY if user stories exist in source]

### Story 1: [Title]
**As a** [user type]  
**I want** [capability]  
**So that** [benefit]

**Acceptance Criteria**:
- [ ] [Criterion 1]

**Estimate**: [Points/Hours if provided]

---
```

### For Standalone User Story

```markdown
## 1. User Story

**Story ID**: [ID from source]  
**Story Title**: [Title]

**As a** [user type]  
**I want** [capability]  
**So that** [benefit]

### Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]

### Technical Details
[Any implementation notes from source]

### Estimate
[Story points or time estimate if provided]

---
```

### For Bug Report

```markdown
## 1. Bug Summary

**Bug ID**: [ID from source]  
**Title**: [Bug title]  
**Severity**: [Critical|High|Medium|Low]  
**Priority**: [P0|P1|P2|P3]  
**Status**: [Open|In Progress|Fixed|etc.]

### Problem Description
[What's broken and its impact]

### Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Expected Behavior
[What should happen]

### Actual Behavior
[What actually happens]

### Environment
- OS: [from source]
- Version: [from source]
- Other context: [from source]

### Proposed Fix (if available)
[Any fix suggestions from source]

### Root Cause Analysis (if available)
[RCA from source]

---
```

### For Documentation Request

```markdown
## 1. Documentation Need

**Request ID**: [ID from source]  
**Title**: [Request title]

### What Documentation is Needed
[Description of missing or incorrect documentation]

### Target Audience
[Who will use this documentation]

### Content Requirements
[What must be documented]
- [Requirement 1]
- [Requirement 2]

### Format/Location
[Where documentation should live, what format]

### Success Criteria
[When is this documentation complete]

---
```

### For Clarification Request

```markdown
## 1. Clarification Request

**Request ID**: [ID from source]  
**Title**: [Question or topic]

### Question / Clarification Needed
[What needs to be clarified]

### Context
[Why this clarification is needed]

### Code/Design Areas in Question
[Specific areas needing explanation]

### Expected Outcome
[What answer or understanding is sought]

### Stakeholders
[Who needs this clarification]

---
```

### For Technical Debt / Refactoring

```markdown
## 1. Technical Debt Item

**Item ID**: [ID from source]  
**Title**: [Debt item title]  
**Type**: [Code Quality|Architecture|Performance|Security|Other]

### Current State Problems
[What's wrong with current implementation]
- [Problem 1]
- [Problem 2]

### Proposed Improvements
[What should be improved]
- [Improvement 1]
- [Improvement 2]

### Benefits
[Why do this refactoring]
- [Benefit 1]
- [Benefit 2]

### Scope
**Will Change**:
- [Item 1]

**Will NOT Change**:
- [Item 1]

### Risk Assessment
[Risks of making changes vs not making changes]

---
```

### For Configuration Change

```markdown
## 1. Configuration Change Request

**Request ID**: [ID from source]  
**Title**: [Change description]  
**Type**: [Environment|Security|Performance|Other]

### Configuration to Change
[What configuration needs to change]
- Parameter: [name]
- Current Value: [value]
- New Value: [value]
- Location: [where config lives]

### Target Environment(s)
- [Environment 1]
- [Environment 2]

### Justification
[Why this change is needed]

### Impact Analysis
- Systems Affected: [list]
- Downtime Required: [Yes/No, duration]
- Rollback Plan: [how to revert]

### Testing Required
- [ ] [Test 1]
- [ ] [Test 2]

---
```

---

## Common Sections (Include as Applicable)

### Requirements (if not covered above)

```markdown
## Requirements

### Functional Requirements
- [FR1 from source]
- [FR2 from source]

### Non-Functional Requirements
- Performance: [from source]
- Security: [from source]
- Scalability: [from source]
- Compliance: [from source]

---
```

### Business Context (Always try to include)

```markdown
## Business Context

### Problem Statement
[What problem is being solved]

### Business Justification
[Why this is important]
- Priority: [from source]
- Business value: [from source]
- WSJF/ROI: [if provided]

### Stakeholders
- **Requestor**: [name/role]
- **Product Owner**: [name]
- **Technical Lead**: [name]
- **Affected Users**: [description]

### Success Metrics
[How success will be measured]

---
```

### Technical Context (If applicable)

```markdown
## Technical Context

### Current Architecture
[Existing system architecture]

### Proposed Changes
[Technical changes required]

### Technology Stack
- Language: [from source]
- Framework: [from source]
- Libraries: [from source]

### Integration Points
- System A: [integration details]
- System B: [integration details]

### Data Model Changes
[Any database or data structure changes]

### APIs Affected
[List of APIs that will change]

---
```

### Constraints and Dependencies

```markdown
## Constraints and Dependencies

### Timeline Constraints
- Target date: [from source]
- Milestones: [from source]

### Resource Constraints
- Team: [from source]
- Budget: [from source]
- Time estimate: [from source]

### Technical Constraints
- [Constraint 1]
- [Constraint 2]

### Dependencies
**Blocking Issues**:
- [Issue 1]

**Related Issues**:
- [Issue 1]

**External Dependencies**:
- [Dependency 1]

---
```

### Acceptance Criteria / Definition of Done

```markdown
## Acceptance Criteria / Definition of Done

### Functional Acceptance
- [ ] [Criterion 1]
- [ ] [Criterion 2]

### Quality Acceptance
- [ ] Tests written and passing
- [ ] Documentation updated
- [ ] Code reviewed
- [ ] Security review completed

### Deployment Acceptance
- [ ] Deployed to test environment
- [ ] UAT completed
- [ ] Rollback plan validated

---
```

---

## Mandatory Sections (Always Include)

### Information Gaps

```markdown
## Information Gaps and Open Questions

### Critical Missing Information
1. [Gap 1 that blocks progress]
2. [Gap 2 that blocks progress]

### Open Questions
1. [Question 1 needing answer]
2. [Question 2 needing answer]

### Ambiguities in Source
1. [Ambiguity 1 needing clarification]
2. [Ambiguity 2 needing clarification]

### Assumptions Needing Validation
1. [Assumption 1]
2. [Assumption 2]

### Recommendations
- [Recommendation 1 to address gaps]
- [Recommendation 2 to address gaps]

---
```

### Metadata

```markdown
## Metadata

### Demand Type Classification
**Type**: [Type from Step 1]  
**Rationale**: [Why this classification]

### Source Documents
**Documents Processed**:
- [Document 1] ([size], [format])
- [Document 2] ([size], [format])

**Documents Unable to Read**:
- [Document name] - [reason]

**Attachments Referenced but Not Accessible**:
- [Attachment name]

### MCP Server Usage
**MCP Server Used**: ✅ Yes / ❌ No  
**External Content Fetched**: [List if any]  
**External References NOT Fetched**: [List with reason]

### Extraction Date and Time
**Date**: [YYYY-MM-DD]  
**Time**: [HH:MM]  
**Timezone**: [Local/UTC]

### Completeness Assessment
**Information Sufficiency**: ✅ Sufficient / ⚠️ Partial / ❌ Insufficient  
**Confidence Level**: High / Medium / Low  
**Critical Gaps**: [Count]  
**Blocking Issues**: [List]

---
```

### Next Steps

```markdown
## Next Steps

### Readiness for Routing
- [x] All available information captured
- [x] No data omitted from sources
- [x] No data invented
- [x] Information gaps documented
- [ ] Additional information needed before routing (if applicable)

### Routing to Orchestrator-0-Router
**Ready**: ✅ Yes / ❌ No  
**Next Action**: Route to Orchestrator-0-Router for sizing and workflow assignment

### Recommended Actions Before Routing (Optional)
1. [Action 1 to improve completeness]
2. [Action 2 to clarify ambiguities]

**Note**: These are optional improvements, not blocking for routing.

---
```

---

## Document Principles (Reference)

✅ **Adapt Structure**: Use sections appropriate to demand type  
✅ **Preserve Source Language**: Use terminology from source documents  
✅ **No Forced Hierarchy**: Don't create Epic/Feature/Story if not in source  
✅ **No Omission**: Every piece of information must be captured  
✅ **No Invention**: Don't create information not in source  
✅ **No Interpretation**: Extract literally, don't infer  
✅ **Mark Gaps**: Explicitly document missing information  
✅ **Preserve Ambiguities**: Note inconsistencies, don't resolve them  

---

## Template Version

**Version**: 2.0 (Adaptive)  
**Date**: 2025-10-08  
**Changes from v1.0**: Removed rigid Epic/Feature/Story structure, added demand type adaptability
