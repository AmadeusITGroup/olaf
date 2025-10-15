# Project Memory Map
<metadata>
version: 1.5.0
last_updated: 2025-10-13
purpose: LLM navigation aid - consolidated OLAF framework
</metadata>

<olaf-memory-map>
## Project Structure and Paths

### Core solution [id:core_dir] = `my-repo/`
# Example usage:
# [id:core_dir]README.md → refers to my-repo/README.md
# [id:core_dir]src/      → refers to my-repo/src/

### Core Framework [id:ack_dir] = `olaf-core/`
# Example usage:
# [id:ack_dir]README.md → refers to olaf-core/README.md
# [id:prompts_dir]phase-0-1-build-setup.md → refers to olaf-core/prompts/phase-0-1-build-setup.md
- **Prompts Directory** [id:prompts_dir] = `[id:ack_dir]prompts/`

- **Tools Directory** [id:tools_dir] = `[id:ack_dir]tools/`
- **Templates Directory** [id:templates_dir] = `[id:ack_dir]templates/`
- **Questionnaires Directory** [id:questionnaires_dir] = `[id:ack_dir]questionnaires/`
- **Reference Directory** [id:reference_dir] = `[id:ack_dir]reference/`
- **Condensed Framework Directory** [id:condensed_dir] = `[id:reference_dir].condensed/`
- **Condensed Framework** [id:condensed_framework] = `[id:condensed_dir]olaf-framework-condensed.md`
- **Competency Index** [id:competency_index] = `[id:reference_dir]query-competency-index.md`
- **Core Principles** [id:core_principles] = `[id:reference_dir]core-principles.md`
- **Team Delegation** [id:team_delegation] = `[id:reference_dir]team-delegation.md`
- **Memory Map** [id:memory_map] = `[id:reference_dir]memory-map.md`
- **LLM vs IDE Task Guide** [id:llm_vs_ide_task_guide] = `[id:reference_dir]llm-vs-ide-task-guide.md`

### Work Environment [id:ads_dir] = `olaf-data/` 
- **Peoples** [id:peoples_dir] = `[id:ads_dir]peoples/`
- **Projects** [id:projects_dir] = `[id:ads_dir]projects/`
  - **Changelog Register** [id:changelog_register] = `[id:projects_dir]changelog-register.md` 
  - **Changelog Archive** [id:changelog_register_archive] = `[id:projects_dir]changelog-register-archive.md` 
  - **Jobs Register** [id:jobs] = `[id:projects_dir]jobs-register.md` 
  - **Jobs Directory** [id:jobs_dir] = `[id:projects_dir]Jobs/` 
- **Product** [id:product_dir] = `[id:ads_dir]product/`
  - **Decision Records** [id:decision_records_dir] = `[id:product_dir]decision-records/` 
    - **Register** [id:decision_records_index] = `[id:decision_records_dir]decision-records-register.md` 
    - **Naming Conventions** [id:dr_naming_conventions] = `[id:decision_records_dir]DR-2025-06-19-01-naming-conventions.md` 
  - **Documentation** [id:documentations_dir] = `[id:product_dir]documentations/` 
    - **Directory** [id:product_docs_dir] = `[id:documentations_dir]` 
    - **Conversations** [id:conversation_records_dir] = `[id:documentations_dir]conversations/` 
- **Directory** [id:findings_dir] = `[id:ads_dir]findings/` 
  - **Code Reviews** [id:code_reviews_dir] = `[id:findings_dir]code-reviews/` 
- **Practices** [id:practices_dir] = `[id:ads_dir]practices/` 

### External References 
- **Handover Document** [id:handover] = `[id:ads_dir]handover-conversation.md`
</olaf-memory-map>