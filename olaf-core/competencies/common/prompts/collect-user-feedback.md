---
name: collect-user-feedback
description: Collect structured user feedback with rating, message, and used prompts, then send to backend endpoint via curl
tags: [feedback, user-experience, rating, curl, api]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## Feedback Endpoint
The feedback endpoint is configured as:
- **ENDPOINT**: `https://uat.digital-logging.saas.amadeus.com/postUILogs`

## Input Parameters
You MUST request these parameters if not provided by the user:
- **User Consent**: Ask if user wants to provide feedback (if they decline, gracefully exit)
- **rating**: number - User satisfaction rating from 1 to 4 (REQUIRED)
  - 1 = Very Dissatisfied
  - 2 = Dissatisfied
  - 3 = Satisfied
  - 4 = Very Satisfied
- **user_message**: string - Optional feedback message or comments (OPTIONAL)
- **prompts_used**: array of strings - Auto-detected from conversation context (AUTOMATIC)

## Prompt Detection
You MUST automatically detect prompts used in the conversation by:
- Analyzing conversation history for OLAF competency invocations
- Identifying workflow patterns and competency names
- Extracting prompt file names from context

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for feedback collection and submission

## Process

### 1. User Consent Phase
You MUST first obtain user consent:
- Ask: "Would you like to provide feedback on this session?"
- If user declines (no/skip/not now), respond with "No problem! Let me know if you need anything else." and EXIT
- If user agrees, proceed to collection phase

### 2. Validation Phase
You WILL verify all requirements:
- Confirm rating is between 1 and 4 (inclusive)
- Auto-detect prompts from conversation context
- Verify curl command availability on system

### 3. Execution Phase

**Parameter Collection:**
<!-- <parameter_collection> -->
You WILL gather all required feedback data:
- Request rating if not provided (1-4 scale)
- Ask for optional user message
- Auto-detect prompts/workflows used from conversation history (EXCLUDE "collect-user-feedback" from this list)
<!-- </parameter_collection> -->

**Feedback Submission:**
<!-- <feedback_submission> -->

```bash
python olaf-core/competencies/common/tools/collect-user-feedback.py
```
You WILL send feedback using curl command:
- macOS/Linux:
  ```bash
  curl -X POST "https://uat.digital-logging.saas.amadeus.com/postUILogs" \
    -H "Content-Type: application/json" \
    -d '<json_payload>'
  ```
- Windows PowerShell:
  ```powershell
  $body = '<json_payload>'
  Invoke-RestMethod -Uri "https://uat.digital-logging.saas.amadeus.com/postUILogs" -Method Post -ContentType "application/json" -Body $body
  ```
- Fire-and-forget approach: If endpoint is unreachable, data loss is acceptable
<!-- </feedback_submission> -->

**Core Logic**: Execute following protocol requirements
- Apply Act protocol for straightforward feedback submission
- Ensure data privacy and security in transmission
- Provide confirmation of submission attempt

### 4. Completion Phase
You WILL complete the process:
- Execute curl command
- Confirm submission was attempted
- Provide submission confirmation
- Note: Response validation not required (fire-and-forget)

## Output Format
You WILL generate outputs following this structure:
- Confirmation message: "Feedback submitted"
- Include submitted data summary (rating, prompts count)
- Note: Response validation not performed (fire-and-forget approach)

## User Communication

### Progress Updates
- Status of payload construction
- Curl command execution status

### Completion Summary
- Feedback submission attempted
- Submitted rating and prompts count

### Next Steps
You WILL clearly define:
- Thank user for providing feedback
- Confirm submission attempt completed

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: ALWAYS obtain user consent before collecting feedback
- Rule 2: ALWAYS validate rating is between 1 and 4
- Rule 3: ALWAYS escape special characters in user_message for JSON
- Rule 4: MUST auto-detect prompts from conversation context
- Rule 5: ALWAYS confirm submission attempt with user
- Rule 6: Accept data loss if endpoint is unreachable (fire-and-forget)

## Success Criteria
You WILL consider the task complete when:
- [ ] User consent obtained (or user declined and exited gracefully)
- [ ] Rating validated (1-4)
- [ ] Prompts auto-detected from conversation
- [ ] JSON payload constructed correctly
- [ ] Curl command executed
- [ ] User confirmation message displayed

## Error Handling

### Common Issues and Solutions:
1. **User declines feedback:**
   - Respond gracefully: "No problem! Let me know if you need anything else."
   - Exit the feedback collection process

2. **Invalid rating:**
   - Request valid rating (1-4)
   - Explain rating scale clearly

3. **Cannot auto-detect prompts:**
   - Analyze conversation history more carefully
   - Include generic placeholder if no prompts detected

4. **Connection failure:**
   - Accept data loss (fire-and-forget approach)
   - Confirm submission was attempted

5. **Invalid JSON:**
   - Re-escape special characters
   - Validate JSON structure before submission
