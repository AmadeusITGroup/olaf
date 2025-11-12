---
name: augment-code-unit-test
description: Iteratively improve unit test coverage by analyzing code complexity and enhancing tests for the most complex modules
category: developer
tags: [iterative, unit-testing, code-analysis, complexity, coverage]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.


## Template Variables
- `[id:core_dir]`: Directory containing the codebase to analyze
- `[id:findings_dir]`: Directory for output files and reports
- `[id:tools_dir]`: Directory containing analysis tools
- `[id:competencies_dir][competency]/prompts/`: Directory containing workflow prompts

## Workflow Type
Iterative - Processes modules by complexity ranking until coverage target is achieved

## Workflow Overview
This workflow systematically improves unit test coverage by:
1. **FIRST STEP - Check State File**: Always read `[id:findings_dir]unit-test-augmentation-state.json` to understand current iteration status
2. Analyzing existing unit tests to understand testing patterns
3. Ranking modules by cyclomatic complexity 
4. Iteratively processing the most complex modules first
5. Checking test coverage and quality for each module
6. Running existing tests and fixing failures
7. Adding meaningful new unit tests (excluding trivial getters/setters)
8. Generating a comprehensive final report

## **CRITICAL FIRST STEP - State File Analysis**
**🚨 MANDATORY - NO EXCEPTIONS 🚨**: Before any other action, you MUST:
1. Read the state file: `[id:findings_dir]unit-test-augmentation-state.json`
2. If state file exists:
   - Determine current iteration number
   - Identify next unprocessed module from complexity rankings
   - Check for any failing tests that need fixing
   - Continue from where the previous iteration left off
3. If state file doesn't exist:
   - This is iteration 1, proceed with initial analysis
   - Run complexity analysis to create initial state file

**⚠️ DO NOT SKIP THIS STEP - IT'S THE FOUNDATION OF THE ITERATIVE PROCESS ⚠️**

## Prerequisites
- Existing codebase with some unit tests in `[id:core_dir]`
- Cyclomatic complexity analysis tool available
- Testing framework installed and configured
- Write access to test directories

## Input Requirements
- **Primary Input:** Codebase directory path (`[id:core_dir]`)
- **Iteration State File:** `unit-test-augmentation-state.json`
- **Input Format:** JSON file containing iteration state and progress data

## Output Specifications
- **Iteration Output:** `ads\findings\unit-test-iteration-results.json` (updated each iteration)
- **Final Output:** `ads\findings\unit-test-augmentation-final-report.json`
- **Progress Tracking:** `ads\findings\unit-test-coverage-progress.json`
- **Output Location:** `ads\findings\` (resolved from `[id:findings_dir]`)

## Iteration Logic

### Iteration Step: Process Next Complex Module
- **Complexity Tool:** `python [id:tools_dir]hotspot_analyzer.py --repo-path "[id:core_dir]" --output "ads\findings\hotspot-analysis\complexity-hotspots.md"`
- **Coverage Analysis:** Built-in testing framework coverage tools
- **Input:** 
  - First iteration: Codebase analysis results + complexity rankings
  - Subsequent iterations: Previous iteration results + updated coverage metrics
- **Output:** `ads\findings\unit-test-iteration-results.json`
- **Description:** 
  1. Select next most complex unprocessed module
  2. Analyze existing test coverage using framework tools
  3. Run existing tests and identify failures
  4. Fix failing tests using developer expertise
  5. Identify coverage gaps through code analysis
  6. Add meaningful new unit tests (excluding trivial getters/setters)
  7. Update coverage metrics and save to `ads\findings\`
- **Validation:** Test coverage improvement and all tests passing

## Completion Criteria
```json
{
  "completion_criteria": {
    "primary_condition": "Overall test coverage >= 55%",
    "secondary_conditions": [
      "All existing tests are passing",
      "Top 10 most complex modules have adequate coverage",
      "No critical testing gaps remain"
    ],
    "max_iterations": 10,
    "success_threshold": "55% code coverage"
  }
}
```

## Template Validation
- All `[id:...]` references must exist in memory map
- Iteration logic must be clearly defined
- State management files must be properly structured
- Completion criteria must be measurable
- User authorization points must be clearly identified
- No infinite iteration loops allowed

## User Authorization Process

### After Each Iteration:
1. **Present Results:** Display module processed, tests added/fixed, current coverage
2. **Provide Recommendation:** 
   - **Continue:** "Coverage is at X%, need Y% more. Next most complex module is Z."
   - **Stop:** "Coverage target of 55% achieved. All critical modules covered."
   - **Modify:** "Approaching iteration limit. Consider adjusting strategy or target."
3. **Request Authorization:** "Based on the analysis, I recommend [RECOMMENDATION]. Shall I proceed?"

### Recommendation Logic:
- **Continue if:** Coverage < 55% AND iterations < 10 AND complex modules remain
- **Stop if:** Coverage >= 55% OR no more significant modules to process
- **Modify if:** Iterations >= 8 AND coverage progress is slow

## Data Flow Diagram
```
[Codebase Analysis] → [Complexity Ranking] → [Select Module] → [Test Analysis] → [Fix/Add Tests] → [Update Coverage] → [User Auth] → [Next Module]
                                                      ↑                                                    ↑
                                               [State File]                                        [Updated State]
```

## State Management
- **State File Format:** `unit-test-augmentation-state.json`
```json
{
  "iteration_number": 1,
  "start_time": "20250813-1611",
  "current_status": "processing_module",
  "complexity_rankings": [
    {
      "module": "module_name",
      "complexity_score": 15,
      "processed": false,
      "coverage_before": 20,
      "coverage_after": 65
    }
  ],
  "overall_coverage": {
    "current_percentage": 45,
    "target_percentage": 55,
    "lines_covered": 1200,
    "total_lines": 2667
  },
  "previous_outputs": [
    {
      "iteration": 1,
      "module_processed": "complex_module_1",
      "output_file": "unit-test-iteration-results.json",
      "timestamp": "20250813-1611"
    }
  ],
  "completion_progress": {
    "criteria_met": ["existing_tests_passing"],
    "criteria_pending": ["coverage_target", "complex_modules_covered"],
    "progress_percentage": 82
  }
}
```

## Error Handling
- **Test Execution Failure:** Log error details, attempt to fix common issues, skip to next module if unfixable
- **Coverage Tool Error:** Fall back to manual test analysis, continue with best effort
- **Module Analysis Failure:** Skip problematic module, continue with next in ranking
- **State Recovery:** Backup state file after each iteration, restore from last known good state

## Common Error Patterns
- **Testing framework not found:** Verify framework installation and configuration
- **Permission errors:** Check write access to test directories and files
- **Complexity tool failure:** Verify `[id:tools_dir]hotspot_analyzer.py` exists and Python 3.7+ is available
- **Coverage calculation errors:** Implement fallback coverage estimation methods
- **Test compilation failures:** Provide clear error messages and suggested fixes
- **Invalid memory map ID:** Check reference exists in memory map file
- **User authorization timeout:** Continue with default recommendation after 5 minutes
- **Infinite loop detection:** Enforce max iterations and progress validation

## Detailed Process Steps

### Step 0: State File Check (🚨 MANDATORY FIRST STEP 🚨)
**ALWAYS START HERE - NO EXCEPTIONS**
1. **Read State File**: Check if `ads\findings\unit-test-augmentation-state.json` exists
2. **If State File Exists**:
   - Parse current iteration number and status
   - Identify next unprocessed module from complexity rankings
   - Check if there are failing tests from previous iteration that need fixing
   - Resume from current state (go to Step 2)
3. **If State File Missing**:
   - This is iteration 1, proceed to Step 1 for initial analysis

### Step 1: Initial Analysis (Only if no state file exists)
1. **Resolve Memory Map References**: Convert `[id:findings_dir]` to `ads\findings\` and `[id:tools_dir]` to `ack\tools\`
2. Run `python [id:tools_dir]hotspot_analyzer.py --repo-path "[id:core_dir]" --output "ads\findings\hotspot-analysis\complexity-hotspots.md"` to get complexity rankings
3. Analyze existing unit test structure and patterns (if any exist)
4. Calculate baseline code coverage using appropriate testing framework
5. Create initial state file in `ads\findings\unit-test-augmentation-state.json`

### Step 2: Module Processing (Iterative)
For each iteration:
1. Select next most complex unprocessed module
2. Analyze existing tests using coverage tools and code inspection
3. Run existing tests and collect results
4. Fix any failing tests using developer expertise
5. Identify coverage gaps through code analysis and testing framework reports
6. Generate meaningful new unit tests (skip trivial setters/getters)
7. Run all tests to ensure they pass
8. Update coverage metrics
9. Update state file

### Step 3: User Authorization Check
1. Present current iteration results
2. Show coverage progress toward 55% target
3. Recommend next action based on progress
4. Wait for user authorization before continuing

### Step 4: Final Report Generation
When completion criteria are met:
1. Generate comprehensive final report
2. Include coverage statistics and improvements
3. List all modules processed and tests added
4. Provide recommendations for future improvements

## Completion Actions
- [ ] Overall coverage >= 55% achieved
- [ ] All existing tests passing
- [ ] Final report generated and validated
- [ ] State file archived with completion timestamp
- [ ] Test suite documentation updated

## Next Steps
- Review final report for additional improvement opportunities
- Consider implementing continuous integration testing
- Plan regular coverage maintenance reviews
- Document testing patterns for team reference

## Example Output Structure

### Iteration Results File
```json
{
  "iteration": 3,
  "timestamp": "20250813-1611",
  "module_processed": "data_processor.py",
  "complexity_score": 12,
  "tests_before": 5,
  "tests_after": 12,
  "coverage_before": 35,
  "coverage_after": 78,
  "tests_added": [
    "test_complex_data_transformation",
    "test_error_handling_edge_cases",
    "test_concurrent_processing"
  ],
  "tests_fixed": [
    "test_basic_processing"
  ],
  "overall_coverage": 48
}
```

### Final Report Structure
```json
{
  "summary": {
    "start_coverage": 25,
    "final_coverage": 58,
    "target_achieved": true,
    "modules_processed": 7,
    "tests_added": 34,
    "tests_fixed": 8,
    "total_iterations": 7
  },
  "module_details": [
    {
      "module": "complex_module",
      "complexity": 15,
      "coverage_improvement": 43,
      "tests_added": 8
    }
  ],
  "recommendations": [
    "Consider adding integration tests for module interactions",
    "Monitor coverage for newly added features"
  ]
}
```
