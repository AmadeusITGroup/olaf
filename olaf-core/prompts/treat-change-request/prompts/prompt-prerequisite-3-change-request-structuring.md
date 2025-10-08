# Prompt Prerequisite-3: Change Request Structuring

## Purpose

Structure the extracted information into a formal change request document, adapting to the **natural structure** found in the source documents. The demand could be an Epic, a User Story, a Bug Report, a Documentation Request, a Clarification Question, or any other type of change request.

**CRITICAL**: Do NOT force a structure that doesn't exist. Respect what's actually in the source documents.

---

## Input

- **prerequisite-1-demand-inventory.md**: Document inventory
- **prerequisite-2-extracted-information.md**: All extracted information from demand documents

---

## Task Instructions

### Step 1: Identify the Demand Type

Review the extracted information to determine **what type of demand this actually is**:

1. **Large Epic with Features/Stories?**
   - Multiple features under a common theme
   - Hierarchical structure explicitly stated
   - Multiple user stories grouped by features

2. **Epic with Direct User Stories?** (No Features)
   - High-level initiative described
   - User stories directly attached to epic
   - No intermediate feature grouping

3. **Standalone User Story?**
   - Single user story with acceptance criteria
   - No epic or feature context
   - Focused on one specific capability

4. **Bug Report?**
   - Describes a defect or issue
   - Steps to reproduce
   - Expected vs actual behavior

5. **Documentation Request?**
   - Request for documentation creation/update
   - Documentation gaps identified
   - Content requirements specified

6. **Clarification Request?**
   - Questions about existing code/design
   - Request for explanation or analysis
   - Investigation needed

7. **Technical Debt / Refactoring?**
   - Code quality improvement
   - Architecture enhancement
   - No new features, just improvement

8. **Configuration Change?**
   - Environment or config modification
   - No code changes
   - Deployment-related

9. **Other/Mixed Types?**
   - Doesn't fit standard categories
   - Hybrid demand
   - Multiple types combined

**Choose the structure that matches the source - don't force it!**

### Step 2: Structure According to Demand Type

Apply the appropriate structure based on what you identified in Step 1:

#### For Large Epic with Features/Stories:
- Section 1: Epic (title, description, goals, criteria, value)
- Section 2: Features (each with description, criteria, technical reqs)
- Section 3: User Stories (each linked to features, with criteria, estimates)
- Include full hierarchy as stated in source

#### For Epic with Direct User Stories (No Features):
- Section 1: Epic (title, description, goals, criteria, value)
- Section 2: User Stories (directly linked to epic, no feature grouping)
- Section 3: [Features not applicable - stories directly attached to epic]
- Preserve flat story structure as in source

#### For Standalone User Story:
- Section 1: User Story (title, as-a/want/so-that, criteria)
- Section 2: [No epic or feature context in source]
- Section 3: Implementation Details (if provided)
- Keep simple structure - don't invent hierarchy

#### For Bug Report:
- Section 1: Bug Summary (title, severity, priority)
- Section 2: Problem Description (what's broken, impact)
- Section 3: Steps to Reproduce
- Section 4: Expected vs Actual Behavior
- Section 5: Environment/Context
- Section 6: Proposed Fix (if mentioned)

#### For Documentation Request:
- Section 1: Documentation Need (what docs are missing/wrong)
- Section 2: Target Audience
- Section 3: Content Requirements (what to document)
- Section 4: Success Criteria (when is doc complete)

#### For Clarification Request:
- Section 1: Question/Clarification Needed
- Section 2: Context (why clarification needed)
- Section 3: Code/Design Areas in Question
- Section 4: Expected Outcome (what answer is sought)

#### For Technical Debt / Refactoring:
- Section 1: Current State Problems (what needs improvement)
- Section 2: Proposed Improvements
- Section 3: Benefits (why do this)
- Section 4: Scope (what will/won't be changed)

#### For Configuration Change:
- Section 1: Configuration Request (what needs to change)
- Section 2: Target Environment
- Section 3: Justification (why this change)
- Section 4: Rollback Plan

#### For Other/Mixed Types:
- Create custom sections that match the source content
- Don't force into predefined categories
- Use descriptive section headers from the source language

**CRITICAL RULES:**
- ✅ Use ONLY sections that exist in source
- ✅ Use source document terminology
- ❌ DO NOT create Epic/Feature/Story hierarchy if not in source
- ❌ DO NOT invent structure to fit a template
- ❌ DO NOT force agile terminology if source uses different language

### Step 3: Include Contextual Information (Always)

Regardless of demand type, always include these contextual sections when information is available:

1. **Requirements** (if applicable)
   - Functional requirements
   - Non-functional requirements
   - Technical specifications
   - Quality requirements

2. **Business Context** (if available)
   - Problem statement or opportunity
   - Business justification
   - Value proposition
   - Stakeholders and their roles
   - Success metrics

3. **Technical Context** (if available)
   - Current state / existing code
   - Proposed solution or approach
   - Architecture notes
   - Technology stack
   - Integration points
   - Data model changes

4. **Constraints and Dependencies** (if applicable)
   - Timeline constraints
   - Resource constraints
   - Budget limitations
   - Technical dependencies
   - External dependencies
   - Blocking issues

5. **Acceptance Criteria / Definition of Done** (if provided)
   - How to verify completion
   - Quality gates
   - Testing requirements

6. **Information Gaps and Open Questions** (always document)
   - Missing information
   - Ambiguities in source documents
   - Areas needing clarification
   - Assumptions that need validation
   - Questions raised in source documents

### Step 4: Add Metadata (Always)

Include processing metadata in every change request:

1. **Demand Type Classification**
   - What type of demand this is (from Step 1)
   - Why this classification was chosen

2. **Source Documents**
   - List all documents processed
   - Note documents that could not be read
   - Document any attachments referenced but not accessible

3. **MCP Server Usage**
   - Document whether MCP server was used
   - List external content fetched (if any)
   - Note external references NOT fetched and why

4. **Extraction Date and Time**
   - When this analysis was performed

5. **Completeness Assessment**
   - Is the information sufficient for routing to Orchestrator-0-Router?
   - What critical information is missing?
   - What level of confidence in the analysis?

---

## Output Format

Generate file: `prerequisite-3-change-request.md`

**DO NOT** use a rigid template. Create a structure that fits the demand type you identified.

Use **../../templates/template-prerequisite-change-request.md** as a **reference only**, not as a rigid structure to force.

---

## Success Criteria

- [ ] Demand type correctly identified
- [ ] Structure matches what's actually in source (not forced)
- [ ] All extracted information included
- [ ] Appropriate sections for the demand type
- [ ] Missing information marked as [Not Provided], not invented
- [ ] Ambiguous information marked as [Unclear in source], not interpreted
- [ ] No data omitted from extracted information
- [ ] No data invented or assumed
- [ ] Source document terminology preserved
- [ ] Metadata section complete
- [ ] Document ready for review and routing to Orchestrator-0-Router

---

## Tools to Use

- **read_file**: Read extracted information and inventory files
- **create_file**: Generate the structured change request document

---

## Principles (CRITICAL)

1. **Respect the Source**: Use the structure and terminology from source documents, not imposed agile frameworks
2. **Adapt Don't Force**: Different demands need different structures
3. **Simple Over Complex**: Don't create hierarchy where none exists
4. **Language Matters**: Use the source's language (bug, story, task, request, etc.)
5. **No Invention**: Don't create Epic/Feature/Story structure if source doesn't have it
6. **Preserve All Content**: Every piece of extracted information must appear
7. **Mark Gaps Explicitly**: Missing information is valuable - document it clearly
8. **No Interpretation**: Structure based on explicit statements, not inference

---

## Exit Criteria

Declare: **"Prerequisite Step 3 complete. Change request document generated. Ready for review and routing to Orchestrator-0-Router."**

---

## Version History

- **v1.0** (2025-10-08): Initial prompt creation for prerequisite orchestrator

---

**Next Step**: Review and route to **Orchestrator-0-Router**
