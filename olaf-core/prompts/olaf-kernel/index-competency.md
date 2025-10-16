---
name: index-competency
description: Ensure competency is available in competency index by finding prompt file, checking index presence, and adding with protocol selection
tags: [competency, index, olaf, framework]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
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
- **competency_prompt_filename**: string - Name of the competency prompt file to index (REQUIRED)
- **protocol_preference**: string - Preferred interaction protocol: Act/Propose-Act/Propose-Confirm-Act (OPTIONAL - defaults to Act)
- **create_documentation**: boolean - Whether to create documentation in /docs (OPTIONAL - defaults to ask user)
- **doc_title**: string - 3-4 word title for documentation if creating (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Act protocol for competency index modifications due to framework impact

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Request competency prompt filename from user if not provided
- Validate competency prompt file exists in olaf-core/prompts/ structure
- Check access to competency index reference file
- Verify write permissions for index modifications

### 2. Execution Phase

**File Location Operations:**
<!-- <competency_search> -->
You WILL locate the competency prompt file:
- Search olaf-core/prompts/ directory structure recursively
- Identify the full path of the specified competency prompt file
- Validate file contains proper competency structure and metadata
- Extract competency name and description from file header
<!-- </competency_search> -->

**Index Verification Operations:**
<!-- <index_check> -->
You WILL check competency index reference:
- Read olaf-core/reference/query-competency-index.md
- Search for existing entries matching the competency name
- Identify if competency is already present in index
- Note current competency patterns and formatting structure
<!-- </index_check> -->

**Protocol Selection Operations:**
<!-- <protocol_selection> -->
You WILL present protocol options if competency not found:
- Offer numbered list of available protocols:
  1. Act (default) - Direct execution
  2. Propose-Act - Propose then execute with approval
  3. Propose-Confirm-Act - Propose, review, confirm, then execute
- Allow user to select preferred protocol for this competency
- Apply selected protocol for index addition process
<!-- </protocol_selection> -->

**Index Addition Operations:**
<!-- <index_addition> -->
You WILL add competency to index following user approval:
- Follow existing competency pattern format in index
- Add competency mapping with triggers and workflow path
- Include selected interaction protocol in the entry
- Maintain alphabetical or logical ordering in index
- DO NOT modify condensed OLAF framework directly
<!-- </index_addition> -->

**Documentation Creation Operations:**
<!-- <documentation_creation> -->
You WILL offer to create documentation:
- Propose creating documentation in /docs with 3-4 word title
- If user approves, create comprehensive documentation including:
  - Competency purpose and functionality explanation
  - Mermaid diagrams showing workflow and decision points
  - Usage examples and integration patterns
  - Protocol selection rationale
<!-- </documentation_creation> -->

**Core Logic**: Execute following protocol requirements
- Apply Propose-Act protocol for index modifications
- Respect user's protocol selection for competency execution
- Maintain framework integrity by avoiding direct condensed framework changes

### 3. Validation Phase
You WILL validate results:
- Confirm competency properly added to index reference
- Verify index formatting and structure maintained
- Validate documentation created if requested
- Ensure condensed framework remains unmodified

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Updated competency index reference file
- Documentation file: /docs/[doc-title].md (if requested)
- Index entry format: competency_triggers→workflow_path|protocol
- Mermaid diagrams: Workflow visualization in documentation

## User Communication

### Progress Updates
- Confirmation when competency prompt file is located
- Status of index verification (found/not found)
- Protocol selection confirmation
- Index addition completion status
- Documentation creation progress (if applicable)

### Completion Summary
- Competency indexing results (added/already present)
- Protocol assigned to competency
- Index reference file location and changes made
- Documentation file created (if applicable) with location
- Framework integrity confirmation (condensed framework unchanged)

### Next Steps
You WILL clearly define:
- Competency ready for use with assigned protocol
- Index reference updated and available for framework loading
- Documentation available for team reference (if created)
- Reminder about create feature for PR to merge into another branch
- Suggestion to test competency execution with new index entry

### Final Summary & PR Reminder
You MUST provide a concise summary and remind about PR workflow:
- **Concise Summary**: Brief overview of competency indexing completed
- **PR Reminder**: Strongly remind user they can use create feature for PR to merge changes into another branch
- **Integration Status**: Confirm competency is now available in framework
- **Next Actions**: Suggest testing the newly indexed competency

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER modify condensed OLAF framework directly - only update competency index reference
- Rule 2: ALWAYS maintain existing competency pattern format in index
- Rule 3: MUST offer protocol selection with numbered list for user choice
- Rule 4: ALWAYS preserve alphabetical or logical ordering in competency index
- Rule 5: MUST validate competency prompt file exists before attempting to index
- Rule 6: ALWAYS use Propose-Act protocol for index modifications
- Rule 7: MUST offer documentation creation with mermaid diagrams
- Rule 8: ALWAYS remind user about PR creation capability at completion

## Success Criteria
You WILL consider the task complete when:
- [ ] Competency prompt filename obtained and file located
- [ ] Competency index reference checked for existing entries
- [ ] Protocol selection offered and user choice recorded (if not present)
- [ ] Competency added to index reference with proper formatting (if not present)
- [ ] Documentation created with mermaid diagrams (if user approved)
- [ ] Condensed OLAF framework confirmed unchanged
- [ ] User approval obtained via Propose-Act protocol
- [ ] Concise summary provided with PR reminder
- [ ] Framework integrity maintained throughout process

## Required Actions
1. Request competency prompt filename and locate file
2. Check competency index reference for existing entries
3. Offer protocol selection if competency not found
4. Execute index addition following Propose-Act protocol
5. Offer documentation creation with mermaid diagrams
6. Provide comprehensive summary with PR workflow reminder

## Error Handling
You WILL handle these scenarios:
- **Competency File Not Found**: Search all subdirectories and provide clear error with suggestions
- **Index Reference Access Failed**: Provide alternative paths and manual update instructions
- **Invalid Competency Format**: Analyze file structure and provide format guidance
- **Index Formatting Issues**: Preserve existing format and request manual review if needed
- **Documentation Creation Failed**: Offer alternative documentation approaches
- **Protocol Selection Invalid**: Re-present options and request valid selection
- **User Rejection During Propose-Act**: Request specific feedback and modification preferences

⚠️ **Critical Requirements**
- MANDATORY: Follow Propose-Act protocol for all index modifications
- MANDATORY: Never modify condensed OLAF framework directly
- MANDATORY: Offer protocol selection with numbered list for user choice
- MANDATORY: Remind user about PR creation capability at completion
- NEVER bypass competency index reference - always update through proper channels
- NEVER add competencies without validating prompt file exists and is properly formatted
- ALWAYS maintain framework integrity by preserving existing patterns and structure
- ALWAYS offer documentation creation with mermaid diagrams for comprehensive coverage