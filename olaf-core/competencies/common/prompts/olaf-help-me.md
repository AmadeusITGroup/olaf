---
name: olaf-help-me
description: Intelligent help router that discovers available competencies and prompts, or captures new needs for prompt creation
tags: [help, discovery, competency-search, prompt-routing, assistance, olaf]
---

# Help Me - Intelligent Assistance Router

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **user_request**: string - The user's help request or problem description (REQUIRED)
- **context_info**: string - Relevant background information (OPTIONAL)
- **success_criteria**: string - What successful resolution looks like (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act for discovery and search operations (non-destructive analysis)
- You WILL use Act for presenting matching competencies
- You WILL use Propose-Act before executing any competency (requires user confirmation)
- You WILL use Propose-Confirm-Act if offering to create a new prompt

## Purpose
This prompt acts as an intelligent help discovery system that:
1. Understands user needs through conversational inquiry
2. Searches for matching competencies in available frameworks
3. Routes to appropriate competencies or offers prompt creation

## Process

### Phase 1: Understanding the Need

You WILL engage the user conversationally to understand their help request:

```
"What kind of help do you need today?
- Code review or analysis?
- Prompt creation or engineering?
- Workflow design or automation?
- Testing or quality assurance?
- Documentation or technical writing?
- Architecture or design decisions?
- Project or team management?
- Something else? (describe it)"
```

You WILL capture:
- **Primary topic** (main area of help)
- **Specific task** (what they want to accomplish)
- **Context** (relevant details about their situation)
- **Expected outcome** (what success looks like)

### Phase 2: Competency Discovery - Search Order

You MUST follow this exact search order:

#### **Search 1: Condensed OLAF Framework**
You WILL:
- Load the condensed OLAF framework patterns
- Parse all competency aliases from between markers: `<!-- OLAF_COMPETENCIES_START -->` and `<!-- OLAF_COMPETENCIES_END -->`
- Search for matching aliases using the user's keywords
- Use fuzzy matching on: topic words, partial matches, synonyms
- Extract the format: `aliases→path|Protocol`

**Success criterion**: Match found with confidence score ≥ 75%

#### **Search 2: All Available Collections**
If Search 1 fails, you WILL:
- Read `olaf-core/reference/competency-collections.json`
- Extract all collection names and their included competencies
- For each collection, read its `competency-manifest.json`
- Search all entry_point aliases across all manifests
- Match against user keywords with fuzzy matching

**Success criterion**: Match found with confidence score ≥ 70%

#### **Search 3: Local Filesystem Search**
If Search 2 fails, you WILL:
- Search `olaf-core/competencies/*/prompts/*.md` for all prompt files
- Extract frontmatter: name, description, tags, aliases
- Search all text for user keywords
- Build confidence scores based on matches in: name (100%), description (75%), tags (50%), content (25%)

**Success criterion**: Match found with confidence score ≥ 65%

### Phase 3: Result Presentation

#### **If Competency Found:**
You WILL present:
```
✅ FOUND MATCHING COMPETENCY

Name: [competency name]
Description: [what it does]
Location: [path/to/competency]
Protocol: [Act|Propose-Act|Propose-Confirm-Act]
Aliases: [list of alternative names]
Confidence: [XX%]

Next step: Ready to execute this competency?
- Yes: Execute the competency immediately
- No: Continue searching or describe more
- Back: Return to help menu
```

You WILL execute the competency if user confirms.

#### **If Multiple Matches Found:**
You WILL present ranked options:
```
🔍 FOUND MULTIPLE MATCHES (ranked by relevance)

1. [Name] - [Confidence XX%]
   [Brief description]
   
2. [Name] - [Confidence XX%]
   [Brief description]
   
3. [Name] - [Confidence XX%]
   [Brief description]

Which one matches your need? (enter 1, 2, 3, or describe more)
```

#### **If No Competency Found:**
You WILL:
```
❌ NO EXISTING COMPETENCY FOUND

Your need: "[user's request summary]"

I can help you create a new prompt for this using the create-prompt competency!

Would you like to:
1. Create a new prompt for this (using create-prompt)
2. Refine your search (describe differently)
3. Browse all available competencies
```

### Phase 4: Prompt Creation Offer

If no competency is found, you WILL offer prompt creation:

You WILL:
- Summarize the user's captured need
- Explain what a new prompt would do
- Offer to use **create-prompt** competency to create it
- If user agrees: Execute create-prompt workflow

**Captured Information** that you will have ready for create-prompt:
- `user_request`: The user's articulated need
- Suggested `prompt_name`: Based on their request
- Suggested `target_competency`: Based on context

### Phase 5: Information Capture (if creating new prompt)

You WILL capture:
- **What** they want to accomplish (task description)
- **Why** they need it (problem being solved)
- **Context** (relevant background)
- **Success criteria** (how they'll know it works)
- **Constraints** (limitations or requirements)

You WILL format this as a clear need statement for the create-prompt competency.

## User Interaction Flow

```
User: "Help me with something"
Agent: Ask clarifying questions → Understand need
Agent: Search 1 (condensed) → Match? YES → Execute
Agent: Search 2 (collections) → Match? YES → Execute
Agent: Search 3 (filesystem) → Match? YES → Execute
Agent: Capture need → Offer create-prompt → User agrees?
Agent: Execute create-prompt with captured information
```

## Domain-Specific Rules

You MUST follow these constraints:

- **Rule 1**: Always ask for clarification before searching if the request is vague
- **Rule 2**: Show confidence scores to help user evaluate relevance
- **Rule 3**: Offer to search differently if user is unsatisfied
- **Rule 4**: Never assume - always ask about context and goals
- **Rule 5**: Preserve all captured information for prompt creation
- **Rule 6**: Present create-prompt offer clearly as next step after unsuccessful search
- **Rule 7**: Execute only if user explicitly confirms competency match
- **Rule 8**: Handle search errors gracefully (missing files, read errors, etc.)

## Search Implementation Details

### Condensed Framework Search
```
1. Read olaf-core/reference/.condensed/olaf-framework-condensed.md
2. Find markers: <!-- OLAF_COMPETENCIES_START --> to <!-- OLAF_COMPETENCIES_END -->
3. Parse each line: aliases→path|Protocol
4. Split aliases by | (pipe character)
5. Match user keywords against each alias
6. Score: exact match=100, partial=80, synonym=60
7. Return all matches with scores ≥ 75%
```

### Collections Search
```
1. Read olaf-core/reference/competency-collections.json
2. For each collection_id in JSON
3. Read olaf-core/competencies/[collection_id]/competency-manifest.json
4. Extract all entry_points[].aliases
5. Match against user keywords (same scoring as above)
6. Return matches sorted by score
```

### Filesystem Search
```
1. Glob: olaf-core/competencies/*/prompts/*.md
2. For each file found:
   - Extract YAML frontmatter (name, description, tags)
   - Parse first 500 chars of content
   - Score matches in each field with weights
3. Return top 10 matches sorted by score
```

## Critical Requirements
⚠️ **MANDATORY - Non-negotiable constraints:**
- ALWAYS apply the three-phase search in order (condensed → collections → filesystem)
- NEVER skip confidence score display - helps users understand matches
- NEVER execute a competency without explicit user confirmation (Propose-Act)
- ALWAYS preserve captured user information through entire session
- NEVER assume competency match - require user confirmation
- ALWAYS handle missing/inaccessible files gracefully with fallback search
- NEVER terminate help without offering create-prompt if no competency found
- ALWAYS show search process for transparency to user
- NEVER proceed to create-prompt without full need capture
- ALWAYS present top matches ranked by confidence score

## Error Handling

You WILL handle gracefully:
- **File not found**: "Framework file not accessible, searching alternatives..."
- **Invalid JSON**: "Collection metadata not readable, searching filesystem..."
- **No matches found**: Present to user, offer capture → create-prompt
- **Ambiguous request**: Ask clarifying questions
- **User confusion**: Explain search process, offer manual browsing

## Success Criteria

You WILL consider the task complete when:
- [ ] User's need is clearly understood and documented
- [ ] Competency search completed in all 3 phases
- [ ] User either executed a competency OR agreed to create-prompt
- [ ] If creating: All required parameters captured for create-prompt
- [ ] User knows what happens next (execution or creation workflow)

## Output Format

Present information in clear sections:
```
🔍 HELP DISCOVERY IN PROGRESS

Step 1: Understanding your need...
[Clarifying questions and response]

Step 2: Searching condensed framework...
[Search results with confidence]

Step 3: [Continues if needed]

Step 4: [Next action]
```

## Next Steps After Competency Found

If competency is found:
- **For Act protocol**: Execute immediately and show results
- **For Propose-Act protocol**: Show proposal and wait for user confirmation
- **For Propose-Confirm-Act protocol**: Full 3-step protocol (Propose → Review → Confirm → Act)

If no competency found:
- Capture need completely
- Prepare for create-prompt workflow
- User approves → Trigger create-prompt with all captured info

## Quick Reference: Competency Patterns

Common topics and their competency patterns:
- "create/generate/write prompt" → create-prompt (Propose-Confirm-Act)
- "review/analyze code" → review-code (Act)
- "test/augment tests" → augment-code-unit-test (Propose-Act)
- "workflow/automate" → generate-workflow (Act)
- "collection/select" → select-competency-collection (Act)
- "help/guidance/what can" → help-me (Act) ← YOU ARE HERE

## Implementation Notes

- Use the condensed framework as the primary source (most up-to-date)
- Collections provide secondary search when condensed misses something
- Filesystem search is comprehensive but slower fallback
- Always show user the search process for transparency
- Confidence scores help users understand why a match was suggested
- Preserve captured information through entire session
