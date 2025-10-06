# Run Persona-Based Benchmark Evaluation

**Competency**: Prompt Engineer  
**Protocol**: Propose-Confirm-Act  
**Target**: Otter Codebase

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

## Input Parameters

You MUST request these parameters if not provided by the user:

- **agent_name**: string - Name of the AI agent being tested (MANDATORY, no default)
- **model_name**: string - Specific model version (MANDATORY, no default)
- **persona**: string|coder|business_analyst|architect_designer|technical_writer|tester|project_manager - Role-based benchmark type (MANDATORY, default: "coder")

## User Interaction Protocol

You MUST follow the established interaction protocol strictly:

- Use **Propose-Confirm-Act** protocol for benchmark initialization and persona confirmation
- Use **Act** protocol during task execution (you are the agent being tested)
- Use **Propose-Act** protocol for final reporting

## Process

### 1. Validation Phase

You WILL verify all requirements:

- Confirm agent_name and model_name with user
- Confirm persona selection from valid options: coder, business_analyst, architect_designer, technical_writer, tester, project_manager
- Verify Otter codebase exists at expected location
- Verify persona-based benchmark protocol exists at `docs/benchmark/run/persona-based-benchmark-protocol.md`
- Check that `[id:ads_dir]` directory exists
- Retrieve current timestamp in YYYYMMDD-HHmm format

### 2. Execution Phase

<!-- <persona_benchmark_initialization> -->
**Step 1: Initialize Persona Benchmark Environment**

You WILL set up the persona benchmark environment using **Git branching strategy** (no expensive copying):

**CRITICAL**: The `otter/` directory is NOT a Git repository - it's a folder within the main workspace repository. You must create branches in the main workspace repository, not in the otter folder.

1. Switch to the `research-benchmark` branch in the main workspace repository
2. Create Git branch: `benchmark-otter-[agent]-[model]-[persona]-[timestamp]` from research-benchmark
3. Create results directory: `olaf-data/benchmarks/otter-[timestamp]-[persona]-[agent]-[model]/`
4. Create session info file with persona-specific configuration and branch reference
5. Initialize persona-specific task structure

**Git Commands to Execute**:
```bash
# IMPORTANT: Work in main repository root, NOT in otter/ subdirectory
git checkout research-benchmark
git checkout -b benchmark-otter-[agent]-[model]-[persona]-[timestamp]
mkdir -p olaf-data/benchmarks/otter-[timestamp]-[persona]-[agent]-[model]/
```

You MUST verify the setup creates:

- Git branch: `benchmark-otter-[agent]-[model]-[persona]-[timestamp]`
- Current working branch switched to benchmark branch
- `olaf-data/benchmarks/otter-[timestamp]-[persona]-[agent]-[model]/` directory structure
- `session-info.json` with persona configuration and branch reference
- `persona-tasks.json` with persona-specific task definitions
- `interventions.json` for logging
- `git-branch-info.json` with branch metadata

You WILL present the setup summary to the user for confirmation before proceeding.
<!-- </persona_benchmark_initialization> -->

<!-- <persona_benchmark_execution> -->
**Step 2: Execute Persona-Specific Tasks**

You MUST execute ONLY the tasks for the selected persona. Do NOT execute tasks from other personas.

**IMPORTANT**: 
- The sections below show all possible persona tasks for reference, but you ONLY execute the tasks for your selected persona
- All work MUST be done in the `otter/` directory while on the benchmark branch
- Commit your work regularly with descriptive commit messages
- All deliverables should be created in the `otter/` directory and committed to the benchmark branch

## Coder Persona Tasks

**Task C1: Build, Test & Release Documentation**
- Create comprehensive build documentation linking to code/docs
- Document unit testing procedures with examples
- Document release process with step-by-step instructions
- **Deliverable**: `BUILD-TEST-RELEASE.md`

**Task C2: Bug Fixes**
- Read and analyze `REALISTIC-BUG-INSTRUCTIONS.md`
- Implement fixes for all documented issues
- Test fixes and document resolution status
- **Deliverable**: `BUG-FIXES-REPORT.md` + code changes

**Task C3: Feature Implementation**
- Read and analyze `REALISTIC-FEATURE-INSTRUCTIONS.md`
- Implement requested features
- Document implementation approach and status
- **Deliverable**: `FEATURES-IMPLEMENTATION-REPORT.md` + code changes

**Task C4: Unit Test Implementation**
- Read and analyze `REALISTIC-TESTING-INSTRUCTIONS.md`
- Implement comprehensive unit tests
- Document test coverage and approach
- **Deliverable**: `UNIT-TESTS-REPORT.md` + test files

**Task C5: Completion Summary**
- Provide detailed status of all completed/incomplete tasks
- Document blockers and recommendations
- **Deliverable**: `CODER-COMPLETION-SUMMARY.md`

## Architect/Designer Persona Tasks

**Task A1: Logical Architecture**
- Create multiple Mermaid diagrams showing logical architecture
- Document system components and their relationships
- Show data flow and interaction patterns
- **Deliverable**: `LOGICAL-ARCHITECTURE.md` with embedded Mermaid diagrams

**Task A2: Codebase Structure Analysis**
- Analyze and document codebase structure with Mermaid diagrams
- Show module dependencies and relationships
- Document package/namespace organization
- **Deliverable**: `CODEBASE-STRUCTURE.md` with embedded Mermaid diagrams

**Task A3: Technical Architecture**
- Document technical architecture (different from logical)
- Include all versions, frameworks, dependencies
- Show deployment and infrastructure considerations
- **Deliverable**: `TECHNICAL-ARCHITECTURE.md`

## Business Analyst Persona Tasks

**Task B1: Functional Specification - Overview**
- Create high-level functional specification document
- Provide overview of all functional domains
- Link to detailed sub-documents per domain
- **Deliverable**: `FUNCTIONAL-SPEC-OVERVIEW.md`

**Task B2: Functional Specification - Domain Details**
- Create detailed sub-documents for each functional domain
- Document business rules and processes
- Include use cases and scenarios
- **Deliverable**: Multiple `FUNCTIONAL-SPEC-[DOMAIN].md` files

**Task B3: Acronyms and Terminology**
- Create comprehensive acronym and terminology document
- Tie definitions to actual codebase elements
- Include business and technical terms
- **Deliverable**: `ACRONYMS-TERMINOLOGY.md`

**Task B4: Data Flow Diagrams**
- Create context diagram (Level 0) with Mermaid
- Create Level 1 data flow diagrams
- Create Level 2 diagrams where needed
- **Deliverable**: `DATA-FLOW-DIAGRAMS.md` with embedded Mermaid diagrams

## Tester Persona Tasks

**Task T1: Major Workflow Documentation**
- Identify and document top 5 common workflows
- Cover major use cases of the application
- Include step-by-step user interactions
- **Deliverable**: `MAJOR-WORKFLOWS.md`

**Task T2: Use Case Catalog**
- Create comprehensive list of use cases
- Organize by functional area
- Include actors and preconditions
- **Deliverable**: `USE-CASES-CATALOG.md`

**Task T3: Functional Tests in Gherkin**
- Create extensive functional tests in Gherkin format
- Generate feature files for major scenarios
- Cover happy path and edge cases
- **Deliverable**: Multiple `.feature` files + `GHERKIN-TESTS-SUMMARY.md`

## Technical Writer Persona Tasks

**Task W1: User Manual**
- Create comprehensive user manual
- Include screenshots and examples where applicable
- Cover all user-facing functionality
- **Deliverable**: `USER-MANUAL.md`

**Task W2: Admin Manual**
- Create administrator manual
- Document configuration and maintenance procedures
- Include troubleshooting guides
- **Deliverable**: `ADMIN-MANUAL.md`

**Task W3: Operator Manual**
- Create operator manual for system operations
- Document monitoring and operational procedures
- Include deployment and scaling guidance
- **Deliverable**: `OPERATOR-MANUAL.md`

**Task W4: API Documentation**
- Create comprehensive API documentation
- Document all endpoints, parameters, responses
- Include examples and use cases
- **Deliverable**: `API-DOCUMENTATION.md`

## Project Manager Persona Tasks

**Task P1: Complex Code Areas Analysis**
- Identify top 5 most complex code areas
- Provide improvement recommendations for each
- Specify unit test needs and refactoring degree
- Identify single top priority improvement
- **Deliverable**: `COMPLEX-CODE-ANALYSIS.md`

**Task P2: Performance Critical Areas**
- Identify most important areas for performance
- Analyze potential performance improvements
- Provide implementation recommendations
- **Deliverable**: `PERFORMANCE-ANALYSIS.md`

## Task Execution Instructions

**EXECUTION RULE**: Based on your selected persona, execute ONLY the corresponding tasks:

- **If persona = "coder"** → Execute Tasks C1, C2, C3, C4, C5 (Coder tasks only)
- **If persona = "business_analyst"** → Execute Tasks B1, B2, B3, B4 (Business Analyst tasks only)  
- **If persona = "architect_designer"** → Execute Tasks A1, A2, A3 (Architect tasks only)
- **If persona = "technical_writer"** → Execute Tasks W1, W2, W3, W4 (Technical Writer tasks only)
- **If persona = "tester"** → Execute Tasks T1, T2, T3 (Tester tasks only)
- **If persona = "project_manager"** → Execute Tasks P1, P2 (Project Manager tasks only)

**MANDATORY EXECUTION**: You MUST execute ALL tasks for your selected persona (and ONLY those tasks)

**NO STOPPING EARLY**: You are NOT allowed to stop after completing only some tasks. The benchmark requires completion of ALL tasks for your persona to be valid.

**CRITICAL**: You are the AI agent being tested. You MUST work autonomously and only log interventions when the user explicitly provides help.
<!-- </persona_benchmark_execution> -->

<!-- <persona_benchmark_reporting> -->
**Step 3: Generate Persona Benchmark Report**

You WILL create a comprehensive report at:
`olaf-data/benchmarks/otter-[timestamp]-[persona]-[agent]-[model]/PERSONA-BENCHMARK-REPORT.md`

The report MUST include:

- Benchmark configuration (persona, agent, model, timestamp)
- Overall completion status and quality assessment
- Persona-specific deliverables summary
- Autonomy score (interventions count and impact)
- Time analysis per task
- Quality assessment of deliverables
- Recommendations for persona-specific improvements
- Comparison to baseline expectations for the persona
<!-- </persona_benchmark_reporting> -->

## Output Format

You WILL generate outputs following this structure:

**Primary Deliverable**: Persona benchmark results directory

```text
olaf-data/benchmarks/otter-[YYYYMMDD-HHmm]-[persona]-[agent]-[model]/
├── session-info.json            # Benchmark configuration + Git branch reference
├── persona-tasks.json           # Persona task definitions and status
├── interventions.json           # User intervention log
├── git-branch-info.json         # Branch metadata and commit references
├── PERSONA-BENCHMARK-REPORT.md  # Comprehensive results
└── README.md                    # Setup and results summary

otter/                               # Working directory (Git repository)
├── [original Otter files]           # Base codebase
├── [your modifications/additions]   # Changes made during benchmark
└── [persona-specific deliverables]  # All committed to benchmark branch
```

**Supporting Documentation**:

- Clear summary of persona task completion
- List of all deliverables created per persona
- Intervention log with timestamps
- Quality assessment per deliverable

## User Communication

You WILL provide these updates to the user:

### Progress Updates

- Confirmation when persona benchmark setup completes
- Announcement at start of each persona task
- Real-time progress during task execution (major milestones only)
- Completion notification for each task
- Final completion summary

### Completion Summary

- Overall persona benchmark completion status
- Total duration for all persona tasks
- Autonomy score (intervention count)
- Quality score per deliverable
- Location of all generated artifacts
- Key insights from the persona benchmark run

## Domain-Specific Rules

You MUST follow these constraints:

- Rule 1: You are the agent being tested - work autonomously without asking user for task solutions
- Rule 2: Log interventions ONLY when user explicitly provides help (not for clarifications about benchmark process)
- Rule 3: All benchmark work MUST happen in the `otter/` directory on the benchmark branch
- Rule 4: You MUST complete ALL tasks for the selected persona (and ONLY those tasks - do not execute tasks from other personas)
- Rule 5: Directory naming MUST follow pattern: `otter-[YYYYMMDD-HHmm]-[persona]-[agent]-[model]`
- Rule 6: You MUST update `persona-tasks.json` status after completing each task
- Rule 7: Never modify Otter codebase on `main` branch - only work on benchmark branch
- Rule 8: If a task is impossible, log it as failed and continue to next task
- Rule 9: Results directory location is ALWAYS `olaf-data/benchmarks/otter-[timestamp]-[persona]-[agent]-[model]/` with Git branch reference
- **Rule 10: COMPLETE ALL PERSONA TASKS - Do not stop early or skip tasks**
- **Rule 11: All Mermaid diagrams must be properly formatted and embedded in markdown**

## Success Criteria

You WILL consider the task complete when:

- [ ] Agent name and model confirmed with user
- [ ] Persona type confirmed with user
- [ ] Current timestamp retrieved in YYYYMMDD-HHmm format
- [ ] Persona benchmark setup completed successfully
- [ ] Results directory created at `olaf-data/benchmarks/otter-[timestamp]-[persona]-[agent]-[model]/`
- [ ] All persona-specific tasks executed autonomously
- [ ] All persona deliverables created in workspace directory
- [ ] Interventions logged accurately in `interventions.json`
- [ ] Task statuses updated in `persona-tasks.json`
- [ ] `PERSONA-BENCHMARK-REPORT.md` created with comprehensive analysis
- [ ] User informed of final location and results summary

## Required Actions

1. Validate all required input parameters and prerequisites
2. **CRITICAL**: Confirm agent name, model name, and persona type with user
3. Set up Otter codebase in persona benchmark workspace
4. Execute persona benchmark setup following Propose-Confirm-Act protocol
5. Execute ALL persona-specific tasks autonomously following Act protocol - DO NOT STOP EARLY
6. Log user interventions immediately when they occur
7. Generate comprehensive persona benchmark report
8. Provide final summary with results location

## Error Handling

You WILL handle these scenarios:

- **Missing Parameters**: Request agent name, model name, and persona from user with valid options
- **Invalid Persona**: Provide valid persona options and request correction
- **Otter Codebase Missing**: Provide error message with expected location
- **Task Instruction Files Missing**: Document missing files and continue with available tasks
- **Deliverable Creation Fails**: Log failure, document reason, continue with remaining tasks
- **Invalid Timestamp Retrieval**: Retry with alternative command or request manual timestamp input

⚠️ **Critical Requirements**

- MANDATORY: You are the AI agent being tested - perform persona tasks autonomously
- MANDATORY: Log interventions ONLY when user provides task-specific help
- MANDATORY: All work MUST be in `otter/` directory on benchmark branch `benchmark-otter-[agent]-[model]-[persona]-[timestamp]`
- MANDATORY: Complete ALL tasks for the selected persona
- MANDATORY: Generate high-quality, professional deliverables appropriate for the persona
