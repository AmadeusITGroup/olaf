---

name: evolve-code-iteratively

description: Incrementally improve code based on specific goals (performance, maintainability, testability) using a structured, iterative approach.

tags: [refactoring, code-quality, optimization, iterative]

## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.If you need to generate a filename or identifier that includes a timestamp (e.g., YYYYMMDD-HHmm or YYYYMMDD), obtain the current time from the terminal, not from model/context data.

- Windows (date+time): `Get-Date -Format "yyyyMMdd-HHmm"`
- Windows (date only): `Get-Date -Format "yyyyMMdd"`
- Unix/Linux/macOS (date+time): `date +"%Y%m%d-%H%M"`
- Unix/Linux/macOS (date only): `date +"%Y%m%d"`




## Input Parameters

**IMPORTANT**: When you don't have these required parameters, ask the USER to provide them.

- **code**: string - The code to be analyzed and evolved (REQUIRED)

- **goals**: array[enum] - Primary goals from: performance, maintainability, testability (REQUIRED - select one or more)

- **iterations**: number - (Optional) Maximum number of iterations (default: 3, max: 5)

- **test_cases**: string - (Optional) Test cases to validate changes



## Process



1. **Initial Assessment**:

   - Analyze code structure and patterns

   - Establish baseline metrics (count lines, functions, complexity indicators where measurable)

   - Identify optimization opportunities with estimated impact

   - Document current state and technical debt



2. **Iterative Improvement**:

   - For each iteration (up to max iterations):

     1. Critique current code against goals

     2. Propose two distinct solutions with specific implementation details

     3. Compare options with pros/cons table

     4. Make a recommendation to the USER and ask for feedback: "Option 1", "Option 2", or "Stop here"

     5. Based on USER feedback, implement selected changes

     6. Validate with unit tests if they exist or propose to create basic validation

     7. Document changes and measure impact where possible

   - Continue until max iterations reached or user chooses to stop



3. **Finalization**:

   - Generate comprehensive improvement report with available metrics

   - Document all changes made with rationale for each decision

   - Provide before/after code comparison with annotations

   - Include recommendations for future improvements

   - Create rollback instructions if needed



## Output/Result Format



Use template: `[id:competencies_dir]developer/templates/code-evolution-report-template.md`



The report should include:

- Initial assessment with baseline metrics

- Iteration reports documenting each improvement cycle

- Before/after code comparisons with annotations

- Metrics comparison showing improvements

- Decision log with rationale for each change

- Rollback instructions for each iteration

- Final recommendations for future work



Save iteration reports to: `[id:ads_dir]/code-evolution/YYYYMMDD-HHmm/`



## Output to USER

1. **Initial Analysis**:

   - Code quality assessment

   - Identified improvement areas

   - Proposed iteration plan



2. **Iteration Updates**:

   - Changes made in each iteration

   - Impact on goals

   - Validation results



3. **Final Report**:

   - Summary of improvements with measurable impact where possible

   - Qualitative assessment of code quality improvements

   - Performance analysis (theoretical gains, algorithm improvements)

   - Recommendations for future work

   - Rollback instructions for each change made



## Domain-Specific Rules

- Rule 1: Preserve functionality

- Rule 2: One change per iteration

- Rule 3: Validate with tests

- Rule 4: Document decisions

- Rule 5: Maintain readability



## Required Actions

1. Validate all required input parameters are provided

2. Analyze input code and establish baseline measurements

3. Define success criteria for each selected goal

4. Execute iterative improvement process with user feedback

5. Validate changes preserve functionality

6. Document process and generate comprehensive deliverables



⚠️ **Critical Notes**

- Never break existing functionality without explicit user approval

- Keep iterations small and focused on one primary improvement area

- Provide rollback capability and instructions for each change

- Document all assumptions and limitations clearly

- Consider team's skill level when proposing solutions

- Stop iterations if no meaningful improvements can be identified

- Measure impact where possible, document qualitative improvements where quantitative metrics aren't available

