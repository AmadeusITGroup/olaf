---

name: review-code

description: Comprehensive code review with multiple input modes - manual selection, git-modified files, or batch processing. Focuses on quality, security, and maintainability.

tags: [code-review, quality-assurance, security, best-practices, git, batch-processing, modified-files]

## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.If you need to generate a filename or identifier that includes a timestamp (e.g., YYYYMMDD-HHmm or YYYYMMDD), obtain the current time from the terminal, not from model/context data.

- Windows (date+time): `Get-Date -Format "yyyyMMdd-HHmm"`
- Windows (date only): `Get-Date -Format "yyyyMMdd"`
- Unix/Linux/macOS (date+time): `date +"%Y%m%d-%H%M"`
- Unix/Linux/macOS (date only): `date +"%Y%m%d"`




## Input Parameters

**MANDATORY**: You MUST determine the review mode and gather appropriate parameters:



### Review Mode Selection

**source_mode**: [manual|git-modified|file-path|copy-paste] - How to identify code for review



### For Manual Mode (Ask User)

- **code_source**: string - REQUIRED - What to review (can be: copy-pasted code, specific file path, folder path, or repository)

- **language**: string - REQUIRED - Programming language of the code

- **context**: string - (Optional) Additional context about the changes



### For Git-Modified Mode (Automatic Discovery)

- **branch_name**: string - Optional specific branch to review (defaults to current branch)

- **file_filter**: string - Optional file types to include (e.g., "*.cs,*.js,*.py")

- **batch_size**: number - Optional number of files to process per batch (default: 10)



### Universal Parameters (All Modes)

- **focus_areas**: array[enum] - (Optional) Specific areas to focus on (security, performance, style, etc.)

- **review_standards**: string/file - (Optional) Custom coding standards, style guides, or review principles to apply

- **team_conventions**: string/file - (Optional) Team-specific conventions, patterns, or architectural guidelines

- **compliance_requirements**: array[string] - (Optional) Specific compliance standards (OWASP, NIST, company policies)



**DEFAULT STANDARDS**: You MUST apply these universal coding standards:

- **Universal Standards**: `[id:practices_dir]standards/universal-coding-standards.md` - Universal coding principles

- **Team Standards Search**: Automatically search `[id:practices_dir]standards/` for team-specific standards files

- **Integration Standards**: `[id:practices_dir]standards/integration-testing-standards.md` - If applicable

- **OLAF Framework**: Only apply `[id:core_dir]docs/best-practices.md` for OLAF-specific development



**CRITICAL**: Never assume what code to review. Always explicitly ask the user to specify:

1. What code they want reviewed (copy-paste, file, folder, or repo)

2. What programming language it is

3. Any specific focus areas or concerns

4. Any custom review standards, team conventions, or compliance requirements to apply



## Process



**MANDATORY STEPS - Execute in this exact order:**



### Phase 1: Mode Detection & Requirements Gathering



#### A. Determine Review Mode

1. **Check user request context** for git-related keywords ("modified files", "git changes", "current branch")

2. **Auto-select git-modified mode** if context suggests reviewing repository changes

3. **Ask user for mode selection** if ambiguous:

   - "Manual selection" (user specifies what to review)

   - "Git modified files" (review current branch changes)



#### B. Git-Modified Mode Process

1. **Execute git discovery**:

   - Run `git status --porcelain` to identify changed files

   - Categorize as Modified (M), New (A/?), Deleted (D)

   - Filter out binary/non-reviewable files

   - Present file list to user for confirmation

2. **Batch processing setup**:

   - Process files in manageable batches (default: 10)

   - Prioritize by importance and change complexity

   - Create progress tracking



#### C. Manual Mode Process

1. **Always ask the user first** for:

   - What code to review (copy-paste, file path, folder, or repository)

   - Programming language

   - Specific focus areas or concerns

2. **Never assume** what needs to be reviewed



### Phase 2: Standards Loading & Strategic Planning



#### A. MANDATORY Standards Loading (Execute FIRST)

1. **Load Universal Standards**: ALWAYS read `olaf-data/practices/standards/universal-coding-standards.md` first

2. **Search for team-specific standards**: Use `file_search` tool to find team-specific standards in `olaf-data/practices/standards/`

3. **Load all applicable standards**: Read any team-specific standards found (e.g., `*-coding-standards.md`)

4. **Load integration standards**: Read `olaf-data/practices/standards/integration-testing-standards.md` if applicable

5. **Confirm standards loaded**: Verify you have the actual content from these files before proceeding



#### B. Strategic Planning (After Standards Loading)

1. **Analyze the scope** of the code to be reviewed

2. **Determine the review approach**:

   - Single file vs. multiple files

   - Specific functions vs. entire codebase

   - Focus areas (security, performance, maintainability)

   - Standards to apply (loaded universal + team-specific + custom)

3. **Plan the review strategy** based on loaded standards, not general knowledge



### Phase 3: In-Depth Analysis (Apply Loaded Standards)



1. **Initial Analysis**:

   - Review code structure and organization

   - **Apply loaded universal coding standards**: Use the specific standards from `universal-coding-standards.md`

   - **Apply loaded team-specific standards**: Use any team standards found in practices/standards/

   - **Check against loaded quality principles**: Readability, maintainability, function length, complexity

   - **Apply custom review standards** (if provided by user)

   - **Verify adherence to team conventions** (if specified)

   - Assess error handling and logging using loaded standards



2. **Security Assessment** (Using Loaded Standards):

   - **Apply loaded security standards**: Use security requirements from `universal-coding-standards.md`

   - Identify potential vulnerabilities based on loaded standards

   - Check input validation per loaded requirements

   - Review authentication/authorization against loaded standards

   - **Apply compliance requirements** (OWASP, NIST, etc. if specified)



3. **Quality Evaluation** (Using Loaded Standards):

   - **Apply loaded quality standards**: Use readability & maintainability from loaded standards

   - **Check function length**: Apply loaded limits (typically 20-30 lines)

   - **Check complexity**: Apply loaded complexity limits (typically <10)

   - **Verify naming conventions**: Apply loaded naming standards

   - **Check test coverage**: Apply loaded testing requirements (typically >80%)

   - **Cross-reference with loaded standards**: Never use general knowledge, only loaded standards



4. **Performance Check**:

   - Identify potential bottlenecks

   - Review resource usage

   - Check for memory leaks

   - Assess algorithm efficiency



### Phase 4: Deep Investigation

- **Take time to understand** the code's purpose and context

- **Look for subtle issues** that might not be immediately obvious

- **Consider the broader implications** of the code changes

- **Think about edge cases** and potential failure scenarios



## Output/Result Format

Use `[id:competencies_dir][competency]/templates/developer/code-review-template.md` to structure the review findings:

- Follow the template's sections for consistency

- Include all required fields from the template

- Replace placeholder content with actual findings

- Maintain the structured format for documentation



## Output to USER



### For Single File/Manual Mode

1. **Critical Issues**: Security vulnerabilities, major bugs, performance concerns

2. **Recommendations**: Code improvements, best practices, refactoring suggestions  

3. **Positive Feedback**: Well-implemented features, clean code examples, good practices followed

4. **Save Review Results**: Always propose to save as `code-review-YYYYMMDD-HHmm.md`



### For Git-Modified Mode (Multiple Files)

1. **Files gathered**: [number of modified/new/deleted files]

2. **Reviews completed**: [number of files successfully reviewed]

3. **Individual reviews**: Generated for each analyzed file

4. **Summary report created**: `code-review-summary-YYYYMMDD-NNN.md` containing:

   - Number of files reviewed by type (modified, new, deleted)

   - List of all generated code review files

   - Aggregated findings by severity level

   - Common patterns or issues found across multiple files

   - Recommendations for team-wide improvements

5. **Key findings**: Brief overview of critical issues found across all files

6. **Recommendations**: High-priority actions for code quality improvement



## Domain-Specific Rules

- Rule 1: Be constructive and specific

- Rule 2: Reference relevant standards

- Rule 3: Prioritize findings by severity

- Rule 4: Provide clear examples

- Rule 5: Consider context and constraints



## Required Actions



### For All Review Modes

1. Analyze code changes

2. Identify issues and improvements

3. Document findings

4. Provide actionable feedback

5. Highlight positive aspects



### Single File/Manual Mode Actions

6. **ALWAYS propose saving results** - Ask user if they want to save the review as a file

7. **If user agrees**, save to: `olaf-data/findings/code-reviews/code-review-YYYYMMDD-HHmm.md`

8. **AFTER SAVING**: Automatically propose a curative action plan with specific, actionable steps

9. **Save action plan** to: `olaf-data/findings/code-reviews/action-plan-YYYYMMDD-HHmm.md`



### Git-Modified Mode Actions (Additional)

6. **Filter non-reviewable files** before user confirmation (binary files, large data files)

7. **Process in manageable batches** to avoid overwhelming output

8. **Prioritize high-impact files** (core logic, frequently changed) first

9. **Generate individual review files** before creating summary to ensure completeness

10. **Create comprehensive summary** with serial number: `code-review-summary-YYYYMMDD-NNN.md`

11. **Aggregate findings** across all reviewed files by severity level

12. **Identify common patterns** or issues found across multiple files



## Curative Action Plan Requirements

**MANDATORY**: After saving the code review, you MUST automatically generate and propose a curative action plan.



Use template: `[id:competencies_dir]developer/templates/code-review-action-plan-template.md`



The action plan should include:

- **Priority Matrix**: Issues categorized by severity and difficulty

- **Actionable Steps**: Specific fix instructions for both human developers and LLM agents

- **Implementation Order**: Logical sequence considering dependencies

- **Effort Estimates**: Time/complexity estimates for each fix

- **Code Examples**: Before/after examples for major changes

- **Validation Criteria**: How to verify each fix is successful



⚠️ **Critical Notes**

- **ALWAYS ASK FIRST**: Never assume what code to review - always explicitly ask the user

- **DEPTH REQUIRED**: Take time to understand code before jumping to conclusions

- **STRATEGIC APPROACH**: Plan your review methodology based on the code scope

- Never expose sensitive information

- Consider the change's context

- Balance perfection with practicality

- Respect team conventions

- Keep feedback objective

- **NO SHORTCUTS**: Thorough analysis is mandatory - never rush to conclusions

