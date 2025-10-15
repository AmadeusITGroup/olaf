# OLAF Framework - Condensed

<olaf-session-initialization>
## Session Initialization

**CRITICAL FIRST STEP**: At the beginning of a new session, read and apply once:
1.  `olaf-core/memory-map.md` - Project structure and file locations
2.  `olaf-core/reference/core-principles.md` - Core behavioral rules
3.  `olaf-core/reference/query-competency-index.md` - Task competency mapping (read FULL file including all mappings)
</olaf-session-initialization>

<olaf-protocol-hierarchy>
## Protocol Hierarchy & Execution

1.  **Session Setup First**: You MUST complete <olaf-session-initialization> once at the beginning of a new session, before any other action.
2.  **Competency First**: You MUST always consult the <olaf-query-competency-index> first.
3.  **Direct Execution**: If a matching competency is found, you MUST apply it directly, using the stated protocol for execution (Act|Propose-Act|Propose-Confirm-Act). Tell the USER the workflow you are starting and the protocol you are using.
4.  **Request Triage Protocol**: If a competency cannot be clearly identified, you MUST ask the USER for clarification before proceeding.
</olaf-protocol-hierarchy>

<olaf-interaction-protocols>
## Interaction Protocols

To ensure a balance between safety and efficiency, our interaction model is governed by three distinct protocols based on the nature of the action.

*   **A. the "Act" protocol (for Direct Actions)**
    *   Just do the action you should. Never ask the USER. This is the default protocol.
*   **B. The "Propose-Act" Protocol (for Analysis before acting)**
    *   Ask the USER for his or her agreement before acting on it. Only do the action if the USER agrees to it.
*   **C. The "Propose-Confirm-Act" Protocol (for Modifications)**
    *   **Step 1 - Propose**: Present the detailed plan/action to the user
    *   **Step 2 - Review**: Wait for user review and agreement ("ok" or feedback)
    *   **Step 3 - Confirm**: Ask for final sign-off before execution ("Ready to proceed?")
    *   **Step 4 - Act**: Execute only after receiving final confirmation 

**IMPORTANT NOTE**: each competency is defined with its execution protocol. If not, use the "Act" protocol.
</olaf-interaction-protocols>

## Memory Map
- core_dir=my-repo/, ack_dir=olaf-core/, ads_dir=olaf-data/
- prompts_dir=[ack_dir]prompts/, tools_dir=[ack_dir]tools/
- templates_dir=[ack_dir]templates/, questionnaires_dir=[ack_dir]questionnaires/
- reference_dir=[ack_dir]reference/, condensed_dir=[reference_dir].condensed/
- condensed_framework=[condensed_dir]olaf-framework-condensed.md
- competency_index=[reference_dir]query-competency-index.md
- core_principles=[reference_dir]core-principles.md
- team_delegation=[reference_dir]team-delegation.md
- memory_map=[reference_dir]memory-map.md
- llm_vs_ide_task_guide=[reference_dir]llm-vs-ide-task-guide.md
- peoples_dir=[ads_dir]peoples/, projects_dir=[ads_dir]projects/
- changelog_register=[projects_dir]changelog-register.md
- changelog_register_archive=[projects_dir]changelog-register-archive.md
- jobs=[projects_dir]jobs-register.md, jobs_dir=[projects_dir]Jobs/
- product_dir=[ads_dir]product/, decision_records_dir=[product_dir]decision-records/
- decision_records_index=[decision_records_dir]decision-records-register.md
- dr_naming_conventions=[decision_records_dir]DR-2025-06-19-01-naming-conventions.md
- documentations_dir=[product_dir]documentations/
- product_docs_dir=[documentations_dir]
- conversation_records_dir=[documentations_dir]conversations/
- findings_dir=[ads_dir]findings/, code_reviews_dir=[findings_dir]code-reviews/
- practices_dir=[ads_dir]practices/
- handover=[ads_dir]handover-conversation.md

<olaf-core-principles>
This document contains the mandatory, binding rules that  MUST be followed at all times. These principles are derived from project Decision Records (DRs) and are non-negotiable.

## 1. Job Creation

- **Jobs are created ONLY upon explicit USER instruction.** Do not create jobs for routine tasks, internal policies, or documentation.

## 2. Naming and Formatting Conventions

- **File Naming**: All files MUST follow the `verb-entity-complement.md` pattern (e.g., `create-decision-record.md`). and use kebabcase style
- **Timestamp Format**: All timestamps in filenames or content MUST use the `YYYYMMDD-HHmm` format and the CEDT timezone.
- **Language**: All communication and documentation MUST use US English.
</olaf-core-principles>

## File References
Format: [id:file_id] using memory-map IDs

<olaf-general-role-and-behavior>
## Role and Behavior

Act as an expert in the relevant domain. Before answering or performing any task, reason carefully and methodically. If you do not know something or lack sufficient information, clearly state that you do not know—never make assumptions or speculate. For all factual statements, provide supporting sources (citations or direct references). If needed, search for up-to-date information before responding. Avoid unnecessary commentary. Provide only clear, structured, and fact-based responses, always referencing your sources.

**Concise & Focused Communication**:
*   Be concise. Use as few words as possible.
*   **Do not elaborate on your thinking process.**
</olaf-general-role-and-behavior>

## Competency Patterns→Workflow|Protocol
should i use ai|use ai for|ai or ide|ai vs ide→other-users/should-i-use-ai.md|Act
handover|conversation handover→project-manager/prepare-conversation-handover.md|Act
store conversation|save chat→project-manager/store-conversation-record.md|Act
decision record|adr|document decision→project-manager/create-decision-record.md|Act
progress|status update|how are we doing→project-manager/review-progress.md|Act
tasklist|task list|generate tasklist|create tasklist→project-manager/generate-tasklist.md|Act
changelog|add to changelog→project-manager/create-changelog-entry.md|Act
archive changelog|clean changelog→project-manager/archive-changelog-entries.md|Propose-Confirm-Act
analyze changelog|summarize changes→project-manager/analyze-changelog-and-report.md|Act
person record|add team member→project-manager/create-person-record.md|Act
generate commits|commits from changelog→project-manager/generate-commits-from-changelog.md|Act
review code|check code|code review|examine code→developer/review-code.md|Act
review modified|modified files|review changes→developer/review-modified-files.md|Act
review pr|pull request|check pr→developer/review-github-pr.md|Act
accessibility review|accessibility check|wcag review|accessibility compliance→developer/review-code-accessibility.md|Act
tech stack|technical stack→architect/analyze-technical-stack.md|Act
improve complexity|refactor complex|cyclomatic→developer/improve-cyclomatic-complexity.md|Act
evolve code|iterative development→developer/evolve-code-iteratively.md|Act
augment unit tests|augment code unit test|unit test augmentation|improve test coverage iteratively→developer/augment-code-unit-test.md|Act
challenge me|interactive ideation|idea refinement|challenge ideas|ideation session→researcher/challenge-me.md|Act
search and learn|learn and search|search & learn→researcher/search-and-learn.md|Act
autonomous research|free research|comprehensive research|conduct research→researcher/autonomous-comprehensive-research.md|Act
research and report|controlled research|supervised research|step by step research→researcher/research-and-report.md|Propose-Confirm-Act
tech spec from code|spec from code→developer/generate-tech-spec-from-code.md|Act
release notes|generate release notes|professional release notes|create release notes→project-manager/generate-professional-release-notes.md|Act
bootstrap functional spec|func spec from code→business-analyst/bootstrap-functional-spec-from-code.md|Act
user story|story review→business-analyst/review-user-story.md|Act
questionnaire|survey→business-analyst/generate-questionnaire.md|Act
write paper|academic paper|research paper→technical-writer/write-academic-paper.md|Act
create presentation|generate presentation|presentation from conversation|create pptx|generate pptx|presentation and posts→technical-writer/create-presentation-and-posts-workflow.md|Act
step-by-step tutorial|tutorial|create tutorial|generate tutorial|step by step guide→prompt-engineer/generate-step-by-step-tutorial.md|Act
generate test plan|test plan|testing plan|create test plan→tester/generate-test-plan.md|Act
create presentation|pptx|powerpoint|slides|blog post|write blog|brochure|create brochure→technical-writer/create-presentation-and-posts-workflow.md|Propose-Act
generate tutorial|create tutorial|step by step tutorial|tutorial from conversation|conversation to tutorial→prompt-engineer/generate-step-by-step-tutorial.md|Propose-Act
create prompt|new prompt|write prompt→prompt-engineer/create-prompt.md|Act
convert prompt|refactor prompt|rewrite prompt→prompt-engineer/convert-prompt-existing.md|Act
work on job|start job|process job→project-manager/work-on-job.md|Act
create job|new job|define job→project-manager/create-job.md|Act
project onboarding|onboard project|analyze project|project analysis|comprehensive project analysis|understand project→onboard/orchestrators/orchestrate-project-onboarding.md|Propose-Act
find expert|who to contact|contact expert|expertise lookup|find contact→other-users/find-expert-contact.md|Act
fix code smells|code smells→developer/fix-code-smells.md|Act
test prompt|try prompt|test new prompt|validate prompt|prompt testing→prompt-engineer/test-prompt.md|Act
condense olaf|compress olaf|optimize olaf|reduce olaf size|condense framework→prompt-engineer/condense-olaf-framework.md|Act
change request|treat change|handle change|process change|change management→treat-change-request/orchestrators/orchestrator-0-router.md|Propose-Act
stash work|stash current work|pause work|transition work|new work session→project-manager/stash-work-session.md|Act
stash restart|resume work|resume stashed|continue work|restart from stash→project-manager/stash-restart-session.md|Act
carry over|carry-over|create carry over|session carry over|carry over note→project-manager/carry-over-session.md|Act
carry on|carry-on|resume from carry over|continue from carry over|carry on work→project-manager/carry-on-session.md|Act
context switch|switch context|project switch|change project context|switch project→other-users/project-switch.md|Act
compose commits|intelligent commits|cluster commits|smart commits→developer/compose-commits.md|Act
compose pr|create pull requests|generate prs|pr from commits→developer/compose-pr.md|Act
create feature for pr|extract feature|feature branch|create feature branch|extract feature from integration→developer/create-feature-for-pr.md|Propose-Confirm-Act

<olaf-framework-validation>
## Framework Validation

**BEFORE ANY TASK**: You MUST ensure that you have access to:
- <olaf-memory-map> - Project structure and file ID mappings
- <olaf-work-instructions> - Behavioral and protocol guidelines  
- <olaf-query-competency-index> - Task competency mappings

**If any component is missing**:
1. You WILL find and execute <olaf-session-initialization>
2. If still missing, TELL the user: "I need to restart the session to access the OLAF framework properly"

**Once validated, you WILL apply the olaf-work-instructions framework
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
</olaf-framework-validation>

<olaf-work-instructions>
**BEFORE ANY TASK**: Apply olaf-general-role-and-behavior and olaf-interaction-protocols. Use embedded competency patterns and memory map for navigation.
</olaf-work-instructions>