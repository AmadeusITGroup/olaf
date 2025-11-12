---

name: review-github-pr

description: Perform a comprehensive code review of GitHub Pull Requests with user-guided selection and automated analysis.

tags: [code-review, github, pull-request, automation, propose-act]

## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.If you need to generate a filename or identifier that includes a timestamp (e.g., YYYYMMDD-HHmm or YYYYMMDD), obtain the current time from the terminal, not from model/context data.

- Windows (date+time): `Get-Date -Format "yyyyMMdd-HHmm"`
- Windows (date only): `Get-Date -Format "yyyyMMdd"`
- Unix/Linux/macOS (date+time): `date +"%Y%m%d-%H%M"`
- Unix/Linux/macOS (date only): `date +"%Y%m%d"`




## GitHub Access Priority

**PRIMARY METHOD**: Use GitHub PR Analyzer Script (simplifies complex MCP interactions):



### GitHub PR Analyzer Script

Located: `olaf-core/competencies/developer/tools/gh-pr-analyzer.py`



**Usage Examples**:

- `python olaf-core/competencies/developer/tools/gh-pr-analyzer.py --pr 123` - Analyze specific PR

- `python olaf-core/competencies/developer/tools/gh-pr-analyzer.py --branch feature/my-branch` - Latest PR for branch

- `python olaf-core/competencies/developer/tools/gh-pr-analyzer.py --latest-open` - Latest open PR



**Script Features**:

- Uses GitHub CLI internally for all data collection

- Returns comprehensive PR analysis in structured format

- Includes: PR details, diff, files changed, reviews, status checks

- Ready for immediate analysis by the prompt



### Fallback Method: Direct GitHub CLI

- `gh auth status` - Check authentication

- `gh pr list --state open` - List open PRs

- `gh pr view [number]` - View PR details

- `gh pr diff [number]` - Get PR changes



### Last Resort: Local Git

- Use git commands for branch comparison

- `git diff main..feature-branch` for changes



## Input Parameters



**MANDATORY**: You MUST always ask the USER first to specify what to review.



**CRITICAL**: Never assume what PR to review. Always explicitly ask the user to specify:



### PR Selection (Required - Ask User)

- **What to review**: Ask user to choose from:

  - Specific PR number (e.g., "PR #123")  

  - Branch name (e.g., "feature/new-feature")

  - "Latest open PR" 

  - "Current branch changes"



### Repository Context (Optional)

- **repository**: string - Repository in format 'owner/repo' (default: auto-detect from git)

- **review_scope**: array[enum] - Focus areas (security, performance, style, etc.)



### Review Options (Optional)

- **review_depth**: enum - [quick|standard|comprehensive] (default: standard)

- **auto_approve**: boolean - Auto-approve if no critical issues (default: false)



## Process



**MANDATORY FIRST STEP**: Always ask the user what they want to review before proceeding.



### Phase 1: User Interaction & Selection (REQUIRED FIRST)



1. **Ask User for PR/Branch Selection**:

   - Present available options (list open PRs, current branches)

   - Get user's specific choice

   - Confirm repository context if needed

   - Ask for any specific review focus areas



2. **User Confirmation**:

   - Present review plan to user  

   - Ask "Do you want me to proceed with reviewing [selected PR/branch]?"

   - Wait for user agreement before proceeding



### Phase 2: PR Analysis & Review (Only after user agreement)



1. **GitHub Authentication Check** (MANDATORY FIRST):

   - **ALWAYS** run: `gh auth status` 

   - Verify GitHub CLI is authenticated before proceeding

   - If not authenticated, guide user to run: `gh auth login`

   - Only proceed to script execution after confirming authentication



2. **Data Collection using PR Analyzer Script**:

   - Run: `python olaf-core/competencies/developer/tools/gh-pr-analyzer.py --pr [number]` OR

   - Run: `python olaf-core/competencies/developer/tools/gh-pr-analyzer.py --branch [branch-name]` OR  

   - Run: `python olaf-core/competencies/developer/tools/gh-pr-analyzer.py --latest-open`

   - Script returns comprehensive structured analysis ready for review



2. **Code Analysis** (Based on script output):

   - Analyze changed files from diff

   - Check for security vulnerabilities

   - Verify coding standards compliance

   - Assess test coverage impact

   - Review commit quality and messages



3. **Review Generation**:

   - Create structured feedback based on script analysis

   - Categorize findings by severity (Critical/Major/Minor)

   - Include code suggestions with line references

   - Reference relevant standards



### Phase 3: Output & Documentation



1. **Present Review Results**:

   - Show comprehensive analysis

   - Highlight critical issues

   - Provide actionable recommendations



2. **Save Review & Action Plan**:

   - **ALWAYS propose saving results** - Ask user if they want to save the review

   - **If user agrees**, save to: `olaf-data/findings/code-reviews/github-pr-review-YYYYMMDD-HHmm.md`

   - **AFTER SAVING**: Automatically propose creating a curative action plan

   - **Use template**: `[id:competencies_dir]developer/templates/code-review-action-plan-template.md`

   - **Save action plan** to: `olaf-data/findings/code-reviews/github-pr-action-plan-YYYYMMDD-HHmm.md`



## Output/Result Format

- GitHub PR review with:

  - Summary of findings

  - File-specific comments

  - Suggested improvements

  - Security recommendations

  - Overall assessment



## Output to USER

1. **Review Summary**:

   - PR overview

   - Key findings

   - Required actions



2. **Detailed Feedback**:

   - Per-file analysis

   - Code suggestions

   - Security concerns



3. **Review Status**:

   - Approval status

   - Blocking issues

   - Next steps



## Domain-Specific Rules

- Rule 1: Respect GitHub review guidelines

- Rule 2: Follow team's coding standards

- Rule 3: Prioritize security issues

- Rule 4: Provide actionable feedback

- Rule 5: Maintain professional tone



## Required Actions



### Pre-Review (Mandatory)

1. **ALWAYS ask user first** what PR/branch to review

2. **Present available options** (list open PRs, branches)  

3. **Get explicit user selection** and confirmation

4. **Ask user agreement** before proceeding with analysis



### Review Process (After User Agreement)

1. **Check GitHub Authentication**: ALWAYS run `gh auth status` first to verify authentication

2. **Use PR Analyzer Script**: Run `python olaf-core/competencies/developer/tools/gh-pr-analyzer.py` with appropriate arguments

3. **Analyze Script Output**: Review comprehensive data (PR details, diff, files, reviews, status)

4. **Code Quality Assessment**: Examine changes against standards and best practices

5. **Security Review**: Check for vulnerabilities, secrets, or security concerns

6. **Generate Comprehensive Review**: Create structured feedback with severity levels

7. **Present Findings**: Show analysis results to user



### Post-Review (Mandatory)

1. **ALWAYS propose saving results** - Ask user if they want to save the review as a file

2. **If user agrees**, save to: `olaf-data/findings/code-reviews/github-pr-review-YYYYMMDD-HHmm.md`

3. **AFTER SAVING**: Automatically propose creating a curative action plan with specific steps

4. **Use template**: `[id:competencies_dir]developer/templates/code-review-action-plan-template.md`

5. **Save action plan** to: `olaf-data/findings/code-reviews/github-pr-action-plan-YYYYMMDD-HHmm.md`



⚠️ **Critical Notes**

- Never expose sensitive information

- Follow branch protection rules

- Respect code ownership

- Document review decisions

- Consider CI/CD status

