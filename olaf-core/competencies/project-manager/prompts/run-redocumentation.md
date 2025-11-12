

## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.




## Intent


Execute systematic redocumentation of any multi-repository or complex application by following an orchestrator plan, tracking progress, and generating carry-over files at each step. This competency uses **FRESH ASSESSMENT methodology** - focusing on direct source code analysis rather than reading previous analysis documents to ensure maximum value generation.





**🚨 METHODOLOGY UPDATE (20251103):** Competency updated to prioritize direct source analysis over previous document synthesis, ensuring each step brings NEW insights through fresh code examination.





## Execution Protocol


**Protocol:** Act (automated execution with progress tracking)





## Process Flow





### Step 1: Review Current Progress


- **Locate Progress Tracker:** Find the progress tracking file in `olaf-data/findings/{project-name}/artifacts/` directory


  - Naming pattern: `redocument-{project-name}-progress.md` or similar systematic naming


- **Load Orchestrator Plan:** Identify and load the corresponding orchestrator plan file


  - Naming pattern: `redocument-{project-name}-orchestrator.md` or similar systematic naming


- **Identify Next Step:** Determine the next pending step in the orchestration plan


- **Validate Prerequisites:** Ensure all dependencies for the identified step are met





### Step 1.5: Fresh Assessment Protocol - Direct Source Analysis





**🚨 CRITICAL METHODOLOGY REQUIREMENT:** Execute FRESH ASSESSMENT focusing on **direct source code and file analysis** rather than reading previous analysis documents.





**Fresh Assessment Protocol:**





1. **Progress Tracking Only:** Review progress tracker ONLY for structural information:


   - Which step to execute next


   - File naming conventions and artifact locations


   - Completion status tracking


2. **Direct Source Focus:** Target analysis directly at actual source code, configuration files, and implementation


3. **Avoid Prior Analysis:** DO NOT read previous step analysis documents as primary input


4. **New Insights Mandate:** Each step MUST generate NEW insights through direct examination





**Rationale for Fresh Assessment:**





- **Prevents Synthesis Loops:** Reading previous analysis leads to rewriting existing content without new value


- **Maximizes Discovery:** Direct code analysis uncovers implementation gaps and technical debt


- **Ensures Competency Effectiveness:** OLAF competencies work best analyzing actual implementations


- **Avoids Echo Chambers:** Document-to-document synthesis reduces analytical value and insight generation





**Implementation Details:**





1. **Step Execution:** Load the target competency and apply it directly to source repositories


2. **Input Sources:** Code files, configuration files, build scripts, API contracts - NOT previous analysis documents


3. **Context Limitation:** Use progress tracker for structure only - file locations, naming patterns, completion status


4. **Value Generation:** Each step must contribute NEW findings through direct implementation examination





**Exception Handling - DFD Analysis:**





- **DFD Competency Exception:** The `dfd/prompts/dfd_main_coordinator.md` competency is **EXEMPT** from fresh assessment protocol


- **DFD Internal Progression:** DFD uses its own multi-phase system (Phase A→B→C→D) that MUST read its own previous phases


- **DFD Execution:** Execute DFD as complete self-contained process, then use DFD results for subsequent steps


- **Step 4.2 Integration:** Use completed DFD artifacts combined with fresh code analysis for enhanced functional specifications





**Validation Requirements:**





- Competency execution focuses on fresh code analysis (except DFD which uses internal progression)


- Generated artifacts contain NEW insights not present in previous documents


- Analysis reveals previously undiscovered implementation patterns, gaps, or technical debt


- Documentation provides actionable information for developers and stakeholders


- DFD analysis completed as integrated multi-phase process when Step 4.1 is reached





### Step 2: Execute Next Step with Fresh Assessment





- **Load Competency:** Load the specific OLAF competency for the identified step


- **Direct Source Analysis:** Apply competency directly to source code, configurations, and actual implementation files


- **Execute with Protocol:** Follow the competency's defined protocol (Act/Propose-Act/Propose-Confirm-Act)


- **Target Focus:** Apply the competency to the target repositories/application (typically in `your-repos/{project-name}/`)


- **Generate New Insights:** Create artifacts containing fresh findings from direct code examination, not synthesis from previous analysis





### Step 3: Update Progress Tracking


- Update the progress file with:


  - Step status (Started → Completed)


  - Start and completion timestamps (YYYYMMDD-HHmm CEDT format)


  - Generated artifacts locations


  - Any issues or notes encountered


- Update overall progress metrics


- Validate quality gate criteria if applicable





### Step 4: Generate Carry-Over File


- Use OLAF competency: `common/prompts/carry-over-session.md`


- Generate carry-over file in `carry-overs/` directory


- Include:


  - Current step completion summary


  - Next step preparation


  - Context for continuation


  - Key artifacts and findings


- Follow OLAF timestamp naming convention: `carry-over-YYYYMMDD-HHmm.txt`





### Step 5: Prepare Next Iteration


- Identify the next step in the orchestration plan


- Validate readiness to proceed or identify blockers


- Provide clear status for user continuation





## Input Requirements


- **Orchestrator Plan:** `olaf-data/findings/{project-name}/artifacts/redocument-{project-name}-orchestrator.md`


- **Progress Tracker:** `olaf-data/findings/{project-name}/artifacts/redocument-{project-name}-progress.md` 


- **Target Application:** `your-repos/{project-name}/` (all repositories/source code)


- **Project Context:** Any existing analysis artifacts in `olaf-data/findings/{project-name}/`





## Output Artifacts


- Updated progress tracking file


- Step-specific documentation artifacts


- Carry-over session file


- Quality gate validation results





## Quality Assurance


- Verify all step prerequisites are met before execution


- Validate artifact generation completeness


- Ensure progress tracking accuracy


- Confirm carry-over file contains sufficient context for session continuation





## Error Handling


- Document any execution issues in progress tracker


- Create detailed error reports for failed steps


- Provide recovery recommendations


- Ensure carry-over file includes error context for troubleshooting





## Success Criteria


- Next step identified and executed successfully


- Progress tracker updated accurately


- Required artifacts generated and stored properly


- Carry-over file created with complete context


- System ready for next iteration or completion





## Usage Notes





### General Usage


- Execute this prompt when ready to advance any systematic redocumentation process


- Ensure OLAF framework is loaded before execution


- Follow the project-specific orchestrator plan sequence strictly


- Maintain traceability through progress tracking


- Use consistent OLAF naming and timestamp conventions





### Project-Specific Setup Required


Before using this competency for a new project, ensure:


1. **Orchestrator Plan Exists:** Create `redocument-{project-name}-orchestrator.md` with systematic steps


2. **Progress Tracker Exists:** Create `redocument-{project-name}-progress.md` with step tracking


3. **Source Code Available:** Target repositories accessible in `your-repos/{project-name}/`


4. **Findings Directory:** Create `olaf-data/findings/{project-name}/` for artifacts





### Example Project Configurations





#### Example 1: Web Application Redocumentation


- **Project Name:** `ecommerce-platform`


- **Orchestrator:** `olaf-data/findings/ecommerce-platform/artifacts/redocument-ecommerce-platform-orchestrator.md`


- **Progress:** `olaf-data/findings/ecommerce-platform/artifacts/redocument-ecommerce-platform-progress.md`


- **Source:** `your-repos/ecommerce-platform/`





#### Example 2: Microservices Architecture Documentation


- **Project Name:** `payment-gateway`


- **Orchestrator:** `olaf-data/findings/payment-gateway/artifacts/redocument-payment-gateway-orchestrator.md`


- **Progress:** `olaf-data/findings/payment-gateway/artifacts/redocument-payment-gateway-progress.md`


- **Source:** `your-repos/payment-gateway/`





### Reusability Features


- **Dynamic Project Detection:** Automatically detects project name from directory structure


- **Flexible Step Categories:** Adapts to different documentation phases based on orchestrator plan


- **Generic Artifact Naming:** Follows consistent patterns for any project type


- **Universal Context Integration:** Reads any step artifacts regardless of specific content





---


**Competency Type:** Execution Orchestrator  


**Framework:** OLAF Multi-Step Process Management  


**Integration:** Progress Tracking + Artifact Generation + Session Management  


**Reusability:** Generic for any systematic documentation project