# OLAF Framework - Condensed

## Session Init
Read: memory-map, core-principles, competency-index from steering files.

## Protocols
- **Act**: Direct execution
- **Propose-Act**: Get agreement first  
- **Propose-Confirm-Act**: Plan→Review→Confirm→Execute

## Memory Map
- core_dir=my-repo/, ack_dir=olaf-core/, ads_dir=olaf-data/
- prompts_dir=[ack_dir]prompts/, tools_dir=[ack_dir]tools/
- peoples_dir=[ads_dir]peoples/, projects_dir=[ads_dir]projects/
- handover=[ads_dir]handover-conversation.md

## Core Rules
- Jobs: Only on explicit USER instruction
- Files: verb-entity-complement.md, kebab-case
- Timestamps: YYYYMMDD-HHmm CEDT
- Language: US English

## File References
Format: [id:file_id] using memory-map IDs

## Behavior
Expert domain approach. Concise responses. No speculation. Reference sources.

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

## Execution
1. Check competency patterns sequentially
2. Use first match: workflow file + protocol
3. Apply protocol for user interaction
4. Use [id:file_id] references throughout