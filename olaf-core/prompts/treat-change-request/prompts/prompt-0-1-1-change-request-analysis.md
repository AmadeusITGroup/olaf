# Prompt 0-1-1: Change Request Analysis

## Purpose

Extract and document all business context, requirements, and stakeholder information from the change request source (JIRA ticket, issue, or requirement document).

---

## Input

- **Source Document**: JIRA ticket ID (e.g., SACP-172207) OR business requirement document
- **Access Methods**: 
  - Direct JIRA or Github Issue or else content (if provided by user)
  - Issue specification markdown file
  - Business requirement doc

---

## Task Instructions

### Step 0: Check for Prerequisite Change Request (MANDATORY)

**BEFORE doing any analysis, check if prerequisites already created a change request:**

1. **Check for file**: `olaf-works/demand/<DEMAND-ID>-analysis/prerequisite-3-change-request.md`
   
2. **If file EXISTS and is complete** (contains Epic, Features, MVP Scope, Open Questions):
   - ✅ **SKIP creating `1-change-request-summary.md`** (avoid duplication!)
   - ✅ **Log validation**: "Prerequisite change request found: prerequisite-3-change-request.md (complete)"
   - ✅ **Proceed directly to Step 1.2**: Go to `prompt-0-1-2-technical-scope-analysis.md`
   - ✅ **Exit this prompt**: No need to recreate 90% duplicate content
   
3. **If file DOES NOT EXIST or is incomplete**:
   - ❌ **STOP ROUTER EXECUTION**
   - ❌ **Return error message**: "Prerequisites not complete. Please run prerequisite phase first to create change request (prerequisite-3-change-request.md)."
   - ❌ **Provide guidance**: "Run: `olaf-works/orchestrators/orchestrator-prerequisites.md` before invoking Router."
   - ❌ **Do NOT proceed** to Step 1

**Rationale**: Prerequisites already extract comprehensive change request from JIRA/Issues. Router should not duplicate this work (90% overlap). Router's value is in **technical scope analysis** and **risk assessment**, not business requirements extraction.

---

### Step 1: Extract Business Context (DEPRECATED - Skip if Prerequisites Complete)

**⚠️ WARNING: This step should only execute if Step 0 determined prerequisite-3 does not exist (rare case).**

Analyze the source document and extract:

1. **Problem Statement**
   - What business problem is being solved?
   - What is the current situation?
   - What is the desired future state?

2. **Business Objectives**
   - Why is this change needed?
   - What business value does it provide?
   - What are the success criteria?

3. **User Impact**
   - Who are the end users affected?
   - How many users/teams are impacted?
   - What is the user experience change?

### Step 2: Identify Stakeholders

Document:

1. **Requestor**
   - Who requested this change?
   - Which team/department?

2. **Product Owner**
   - Who owns this feature/product area?

3. **Affected Teams**
   - Which development teams are involved?
   - Which operations teams need to be consulted?

4. **External Dependencies**
   - Are external teams or systems involved?

### Step 3: Analyze Requirements

Extract and categorize:

1. **Functional Requirements**
   - What features/capabilities must be delivered?
   - What are the user stories?
   - What is in scope for MVP?

2. **Non-Functional Requirements**
   - Performance requirements
   - Security requirements
   - Compliance requirements
   - Scalability needs

3. **Acceptance Criteria**
   - How will we know this is complete?
   - What are the testable conditions?

### Step 4: Identify Dependencies

Document:

1. **Blocking Issues**
   - What must be completed before this starts?

2. **Related Issues**
   - What other changes are related?
   - Are there linked JIRA tickets?

3. **External Dependencies**
   - Are there third-party systems involved?
   - Are there external data sources?

### Step 5: Extract Timeline Information

Capture:

1. **Due Date**: When is this needed?
2. **Priority**: Critical / High / Medium / Low
3. **Sprint/Release Target**: Which sprint or release?
4. **Business Deadlines**: Are there regulatory or contractual deadlines?

---

## Output Format

Generate file: `1-change-request-summary.md`

Use **../templates/template-change-request-summary.md** to structure the output.

---

## Success Criteria

**If prerequisite-3-change-request.md EXISTS:**
- [x] Prerequisite change request validated (complete with Epic, Features, MVP, Open Questions)
- [x] Duplication avoided (did NOT create redundant 1-change-request-summary.md)
- [x] Logged validation message confirming prerequisite found
- [x] Ready to proceed to Step 1.2 (Technical Scope Analysis)

**If prerequisite-3-change-request.md DOES NOT EXIST (rare fallback):**
- [ ] All business context extracted from source
- [ ] Problem statement is clear and specific
- [ ] All stakeholders identified
- [ ] Requirements categorized (functional vs non-functional)
- [ ] MVP scope clearly defined
- [ ] Acceptance criteria are testable
- [ ] Dependencies documented
- [ ] Timeline information captured
- [ ] Output follows template exactly

---

## Tools to Use

- **read_file**: Read JIRA specification or requirement document
- **grep_search**: Search for related issues or dependencies in codebase
- **semantic_search**: Find related features or similar past changes

---

## Exit Criteria

**If prerequisite-3 exists:**
Declare: **"✅ Prerequisite change request validated: prerequisite-3-change-request.md (complete). Skipping 1-change-request-summary.md creation to avoid duplication. Proceeding to Step 1.2 (Technical Scope Analysis)."**

**If prerequisite-3 does NOT exist:**
STOP and declare: **"❌ Prerequisites incomplete. prerequisite-3-change-request.md not found. Please run prerequisite phase first. Router cannot proceed without complete change request."**

---

## Version History

- **v1.0** (2025-01-08): Initial prompt creation from orchestrator-0-router.md v1.0

---

**Next Prompt**: `prompt-0-1-2-technical-scope-analysis.md`
