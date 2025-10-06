---
name: run-benchmark-evaluation
description: Execute AI agent benchmark by running setup, performing tasks, and collecting scored results
tags: [benchmark, evaluation, testing, performance]
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

- **language**: string|java|csharp|cpp|python - Programming language for benchmark (REQUIRED)
- **size**: string|small|medium|large - Repository size/complexity level (REQUIRED)
- **agent_name**: string - Name of the AI agent being tested (OPTIONAL, default: "windsurf-cascade")
- **model_name**: string - Model name/version being used (OPTIONAL, default: "cascade")
- **task_subset**: string|all|1-5 - Which tasks to execute (OPTIONAL, default: "all")

## User Interaction Protocol

You MUST follow the established interaction protocol strictly:

- Use **Propose-Confirm-Act** protocol for benchmark initialization
- Use **Act** protocol during task execution (you are the agent being tested)
- Use **Propose-Act** protocol for intervention logging and final scoring

## Process

### 1. Validation Phase

You WILL verify all requirements:

- Confirm language parameter is one of: java, csharp, cpp, python
- Confirm size parameter is one of: small, medium, large
- Verify benchmark documentation exists at `docs/benchmark/benchmark-protocol.md`
- Verify benchmark setup script exists at `docs/benchmark/benchmark-setup-script.py`
- **CRITICAL**: Read `docs/benchmark/benchmark-repositories-urls.md` to find repository URL for [language]/[size]
- If test repository doesn't exist at `docs/test-repositories/[language]/[size]/`, you MUST:
  1. Create the directory structure: `docs/test-repositories/[language]/[size]/`
  2. Clone the repository from the URL found in `benchmark-repositories-urls.md`
  3. Proceed with benchmark setup
- Check that `[id:ads_dir]` directory exists
- Retrieve current timestamp in YYYYMMDD-HHmm format

### 2. Execution Phase

<!-- <benchmark_initialization> -->
**Step 1: Initialize Benchmark Environment**

You WILL set up the benchmark environment. If the setup script fails or is incompatible, you MUST manually create the required structure:

**Option 1: Try setup script first**

```bash
python docs/benchmark/benchmark-setup-script.py \
  -l [language] \
  -s [size] \
  -a [agent_name] \
  -m [model_name]
```

**Option 2: Manual setup (if script fails)**

1. Create directory: `olaf-data/benchmarks/[language]-[size]-[timestamp]/`
2. Copy repository to: `olaf-data/benchmarks/[language]-[size]-[timestamp]/workspace/`
3. Create required JSON files: `session-info.json`, `tasks.json`, `interventions.json`
4. Proceed with task execution

You MUST verify the setup script creates:

- `olaf-data/benchmarks/[language]-[size]-[timestamp]/` directory structure
- `session-info.json` with configuration
- `tasks.json` with task definitions
- `interventions.json` for logging
- `workspace/` with test repository copy
- `baseline-metrics.json` with pre-benchmark metrics
- `README.md` with instructions

You WILL present the setup summary to the user for confirmation before proceeding.
<!-- </benchmark_initialization> -->

<!-- <benchmark_execution> -->
**Step 2: Execute Benchmark Tasks**

You MUST read and understand task requirements from:

- `docs/benchmark/benchmark-protocol.md` - Complete protocol and success criteria
- `olaf-data/benchmarks/[language]-[size]-[timestamp]/tasks.json` - Task definitions

For each task in the benchmark:

**Task Execution Loop:**

1. **Read Task Definition**: Load task details from `tasks.json`
2. **Announce Task Start**: Inform user which task you are beginning
3. **Execute Task Autonomously**:
   - Work in `olaf-data/benchmarks/[language]-[size]-[timestamp]/workspace/`
   - Follow task requirements from benchmark protocol
   - Create all required deliverables
   - Track your own start time
4. **Monitor Timeout**: Track duration, task has specific time budget
5. **Handle User Interventions**:
   - If user provides help/guidance, you MUST log it immediately
   - Add entry to `interventions.json` with format:

     ```json
     {
       "timestamp": "[ISO format]",
       "task_id": "task1",
       "type": "clarification|correction|guidance|technical_help",
       "description": "What user helped with",
       "time_spent_minutes": [estimate]
     }
     ```

6. **Mark Task Complete**: Update task status in `tasks.json` when finished
7. **Calculate Duration**: Record actual time spent

**MANDATORY EXECUTION**: You MUST execute ALL 5 tasks in sequence: task1 → task2 → task3 → task4 → task5 (unless task_subset specified)

**NO STOPPING EARLY**: You are NOT allowed to stop after completing only some tasks. The benchmark requires completion of ALL tasks to be valid.

**CRITICAL**: You are the AI agent being tested. You MUST work autonomously and only log interventions when the user explicitly provides help.
<!-- </benchmark_execution> -->

<!-- <benchmark_scoring> -->
**Step 3: Calculate Benchmark Score**

After completing all tasks, you WILL:

1. Execute scoring script:

   ```bash
   python docs/benchmark/benchmark-scoring.py olaf-data/benchmarks/[language]-[size]-[timestamp]/
   ```

2. Read generated `scores.json` file
3. Analyze results against baseline metrics
4. Generate performance summary
<!-- </benchmark_scoring> -->

<!-- <benchmark_reporting> -->
**Step 4: Generate Benchmark Report**

You WILL create a comprehensive report at:
`olaf-data/benchmarks/[language]-[size]-[timestamp]/BENCHMARK-REPORT.md`

The report MUST include:

- Benchmark configuration (language, size, agent, model, timestamp)
- Overall score and breakdown by task
- Autonomy score (interventions count and impact)
- Duration for each task vs. budget
- Deliverables checklist (what was created)
- Key observations and challenges
- Comparison to baseline metrics (improvements made)
- Efficiency metrics (if available)
- Recommendations for agent improvement
<!-- </benchmark_reporting> -->

### 3. Validation Phase

You WILL validate results:

- Confirm all task deliverables exist in workspace
- Verify `scores.json` was generated successfully
- Confirm benchmark report is complete
- Check all files are in correct directory structure
- Validate intervention log is accurate

## Output Format

You WILL generate outputs following this structure:

**Primary Deliverable**: Benchmark results directory

```
olaf-data/benchmarks/[language]-[size]-[YYYYMMDD-HHmm]/
├── workspace/              # Test repository with your work
│   ├── FUNCTIONALITY.md    # Task 1 deliverables
│   ├── ARCHITECTURE.md
│   ├── BUILD.md
│   ├── TESTING.md
│   ├── DEVELOPMENT.md
│   ├── build-all.sh        # Task 2 deliverables
│   ├── test-all.sh
│   ├── metrics-collect.sh
│   ├── quality-check.sh
│   └── [other task outputs]
├── session-info.json       # Configuration
├── tasks.json              # Task definitions and status
├── interventions.json      # User help log
├── baseline-metrics.json   # Pre-benchmark state
├── scores.json             # Calculated scores
├── BENCHMARK-REPORT.md     # Final summary report
└── README.md               # Setup instructions
```

**Supporting Documentation**:

- Clear summary of score breakdown
- List of all deliverables created
- Intervention log with timestamps
- Performance comparison to baseline

## User Communication

You WILL provide these updates to the user:

### Progress Updates

- Confirmation when setup script completes successfully
- Announcement at start of each task with time budget
- Real-time progress during task execution (major milestones only)
- Immediate logging when user provides intervention
- Completion confirmation for each task with duration
- Scoring script execution results

### Completion Summary

- Overall benchmark score with breakdown
- Total duration vs. total budget
- Autonomy score (intervention count)
- Number of deliverables created successfully
- Location of benchmark results directory
- Key insights from the benchmark run

### Next Steps

You WILL clearly define:

- Benchmark results are ready for review at `olaf-data/benchmarks/[language]-[size]-[timestamp]/`
- Suggested improvements based on performance
- Comparison opportunities (run other languages/sizes for full evaluation)
- How to analyze results in detail (review scores.json and BENCHMARK-REPORT.md)

## Domain-Specific Rules

You MUST follow these constraints:

- Rule 1: You are the agent being tested - work autonomously without asking user for task solutions
- Rule 2: Log interventions ONLY when user explicitly provides help (not for clarifications about benchmark process)
- Rule 3: All benchmark work MUST happen in the workspace directory
- Rule 4: You MUST respect task timeout budgets (stop if exceeded)
- Rule 5: Directory naming MUST follow pattern: `[language]-[size]-[YYYYMMDD-HHmm]`
- Rule 6: You MUST update `tasks.json` status after completing each task
- Rule 7: Scoring can only run after all tasks complete (or timeout/fail)
- Rule 8: Never modify baseline metrics or test repository outside workspace
- Rule 9: If a task is impossible, log it as failed and continue to next task
- Rule 10: Results directory location is ALWAYS `olaf-data/benchmarks/[language]-[size]-[timestamp]/`
- **Rule 11: COMPLETE ALL 5 TASKS - Do not stop early or skip tasks**
- **Rule 12: If repository setup fails, use `docs/benchmark/benchmark-repositories-urls.md` to find and clone the correct repository**

## Success Criteria

You WILL consider the task complete when:

- [ ] All required parameters validated (language, size)
- [ ] Current timestamp retrieved in YYYYMMDD-HHmm format
- [ ] Benchmark setup script executed successfully
- [ ] Results directory created at `olaf-data/benchmarks/[language]-[size]-[timestamp]/`
- [ ] All specified tasks executed (autonomously as the agent being tested)
- [ ] All deliverables created in workspace directory
- [ ] Interventions logged accurately in `interventions.json`
- [ ] Task statuses updated in `tasks.json`
- [ ] Scoring script executed successfully
- [ ] `scores.json` generated with results
- [ ] `BENCHMARK-REPORT.md` created with comprehensive analysis
- [ ] User informed of final location and results summary

## Required Actions

1. Validate all required input parameters and prerequisites
2. **CRITICAL**: Read `docs/benchmark/benchmark-repositories-urls.md` to find repository URL for your language/size combination
3. Set up test repository (clone if needed) before proceeding
4. Execute benchmark setup (script or manual) following Propose-Confirm-Act protocol
5. Execute ALL 5 benchmark tasks autonomously following Act protocol - DO NOT STOP EARLY
6. Log user interventions immediately when they occur
7. Calculate scores using scoring script
8. Generate comprehensive benchmark report
9. Provide final summary with results location

## Error Handling

You WILL handle these scenarios:

- **Missing Parameters**: Request language and size from user with valid options
- **Invalid Language/Size**: Provide valid options and request correction
- **Benchmark Documentation Missing**: Provide error message with expected file locations
- **Setup Script Fails**: Display error output and request user to verify prerequisites
- **Test Repository Missing**: Inform user and provide instructions to create test-repositories directory
- **Task Timeout Exceeded**: Mark task as incomplete, log timeout in interventions, proceed to next task
- **Deliverable Creation Fails**: Log failure, document reason, continue with remaining tasks
- **Scoring Script Fails**: Provide manual scoring instructions and error details
- **Directory Creation Fails**: Check permissions, provide alternative manual setup steps
- **User Interruption Mid-Task**: Log intervention, mark task status, allow resume or skip
- **Invalid Timestamp Retrieval**: Retry with alternative command or request manual timestamp input

⚠️ **Critical Requirements**

- MANDATORY: You are the AI agent being tested - perform tasks autonomously
- MANDATORY: Log interventions ONLY when user provides task-specific help
- MANDATORY: All work MUST be in `olaf-data/benchmarks/[language]-[size]-[timestamp]/workspace/`
- MANDATORY: Use Propose-Confirm-Act for setup, Act for task execution
- NEVER ask user how to solve benchmark tasks (that defeats the purpose)
- NEVER work outside the designated workspace directory
- NEVER modify baseline metrics or original test repository
- ALWAYS respect task timeout budgets
- ALWAYS update task status in tasks.json after each task
- ALWAYS log user interventions immediately with accurate details
- ALWAYS generate comprehensive benchmark report at the end
