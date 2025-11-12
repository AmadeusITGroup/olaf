---

name: check-todos-in-code

description: Search, analyze, and provide solutions for TODO comments with user decision tracking

tags: [todo, code-analysis, technical-debt, cleanup]

## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.If you need to generate a filename or identifier that includes a timestamp (e.g., YYYYMMDD-HHmm or YYYYMMDD), obtain the current time from the terminal, not from model/context data.

- Windows (date+time): `Get-Date -Format "yyyyMMdd-HHmm"`
- Windows (date only): `Get-Date -Format "yyyyMMdd"`
- Unix/Linux/macOS (date+time): `date +"%Y%m%d-%H%M"`
- Unix/Linux/macOS (date only): `date +"%Y%m%d"`




## Input Parameters

You MUST request these parameters if not provided by the user:

- **target_path**: string - Path to folder or repository to scan (REQUIRED)

- **repository_name**: string - Name of the repository being analyzed (REQUIRED)

- **file_extensions**: array - File extensions to include (OPTIONAL, defaults to common code files)

- **todo_patterns**: array - TODO patterns to search for (OPTIONAL, defaults to TODO, FIXME, HACK, XXX, BUG)

- **save_document**: boolean - Save resolution document (OPTIONAL, default: true)

- **max_todos_threshold**: number - Maximum TODOs to analyze in one session (OPTIONAL, default: 50)



## User Interaction Protocol

You MUST follow the established interaction protocol strictly:

- Act / Propose-Act / Propose-Confirm-Act (defined externally)

- Use **Propose-Act** protocol for TODO analysis and document generation



## Process



### 1. Validation Phase

You WILL verify all requirements:

- Confirm target_path exists and is accessible

- Validate repository_name is provided

- Check file_extensions format if provided

- Ensure search patterns are valid

- Verify template access: `[id:competencies_dir]developer/templates/todo-resolution-template.md`



### 2. Execution Phase



**Initial Count Operations**:

- Execute quick TODO count across all specified file types  

- Present total count to user immediately

- **If TODOs > 50**: Propose subset selection options:

  - Focus on specific folder/subfolder

  - Filter by priority patterns (FIXME, BUG > TODO > others)  

  - Limit to specific file types

  - Choose top N by creation date or author

- **If TODOs ≤ 50**: Proceed with full analysis

- Wait for user selection before continuing with detailed analysis



**Search Operations** (after subset selection):

- Execute targeted TODO search based on user's subset choice

- Parse results by repository structure: Repo → Folder Path → File → Line  

- Extract TODO context including surrounding code (±5 lines)

- Identify author information if available in comments



**Analysis Operations**:

For each TODO found, analyze in hierarchical order:

1. **Repository Level**: Group by repository name

2. **Folder Level**: Organize by relative folder paths  

3. **File Level**: List files containing TODOs

4. **TODO Level**: Individual TODO analysis including:

   - Current validity assessment

   - Priority classification (🔥 Critical, ⚠️ High, 📝 Medium, 💡 Low)

   - **Actual replacement code solution** (not recommendations)

   - **Specific line ranges to replace**

   - **Implementation and testing instructions**

   - Effort estimation

   - Dependencies identification



**Document Generation**:

- Load template: `[id:competencies_dir]developer/templates/todo-resolution-template.md`

- Populate template with structured findings

- Include user decision tracking sections for each TODO

- Default all user answers to "NO" for safety

- Generate unique document ID: `todo-resolution-{repo_name}-{timestamp}`



### 3. Validation Phase

You WILL validate results:

- Confirm all TODOs are analyzed and structured correctly

- Verify proposed solutions are syntactically correct

- Ensure document follows repository hierarchy structure

- Validate user decision sections are properly formatted



## Output Format

You WILL generate outputs using template structure:

- **Primary deliverable**: Populated TODO Resolution Report following `todo-resolution-template.md`

- **Document location**: `{workspace}/todo-resolution-{repo_name}-{timestamp}.md`

- **Structure**: Repository → Folder Path → File → TODO (with user decision tracking)



## User Communication



### Initial Count Proposal (if TODOs > threshold)

You WILL propose subset options to user:

```

🔍 TODO Analysis - Initial Count Complete



Found {total_count} TODOs in {repository_name} (threshold: {max_todos_threshold})



⚠️ Large codebase detected! Analyzing all {total_count} TODOs may exceed session limits.

Recommended: Focus on a manageable subset for better results.



📊 Subset Options:

1. **By Priority**: Focus on FIXME/BUG patterns only ({critical_count} items)

2. **By Folder**: Choose specific folder (e.g., /src/main - {main_folder_count} items)

3. **By File Type**: Limit to specific extensions ({java_count} .java, {js_count} .js files)

4. **By Author**: Focus on specific author's TODOs (@{author_name} - {author_count} items)

5. **By Date**: Most recent {max_todos_threshold} TODOs only

6. **Proceed Anyway**: Analyze all {total_count} (may be slow/incomplete)



Which subset approach would you prefer? (Recommended: Option 1 or 2)

```



### Progress Updates  

- Initial TODO count with subset recommendation (if applicable)

- Confirmation when targeted search completes  

- Progress indicator during analysis phase

- Template loading confirmation

- Document generation status



### Completion Summary

- Total TODOs found organized by priority levels

- Document saved location with unique identifier

- Instructions for completing user decision sections

- Next steps for implementation planning



### Document Save Proposal

You WILL propose to user:

```

📄 TODO Resolution Document Ready



Found {total_count} TODOs across {file_count} files in {repository_name}

- 🔥 {critical_count} Critical (immediate action required)

- ⚠️ {high_count} High (current sprint)  

- 📝 {medium_count} Medium (technical debt)

- 💡 {low_count} Low (enhancements)



Save detailed resolution document? This includes:

✅ Structured analysis by Repository → Folder → File

✅ Validity assessment and proposed solutions for each TODO

✅ User decision tracking (YES/NO) with default NO for safety

✅ Implementation checklist and effort estimates



Document will be saved as: olaf-data/findings/remaining-todos/todo-resolution-{repo_name}-{timestamp}.md



Proceed with saving? (Recommended: YES)

```



## Domain-Specific Rules

You MUST follow these constraints:

- Rule 1: **ALWAYS start with TODO count** - if count > max_todos_threshold, MUST propose subset options before proceeding

- Rule 2: Structure output strictly by Repository → Folder Path → File → TODO hierarchy  

- Rule 3: Default ALL user decision fields to "NO" for safety

- Rule 4: Generate complete, ready-to-implement code solutions (not recommendations)

- Rule 5: Include specific line ranges and implementation instructions for every solution

- Rule 6: Never modify source files during analysis - read-only operation only



## Success Criteria

You WILL consider the task complete when:

- [ ] All TODOs discovered and catalogued in hierarchical structure

- [ ] Each TODO analyzed with validity assessment and complete code solution

- [ ] Priority classification applied consistently

- [ ] User decision tracking sections included for every TODO

- [ ] Document generated using official template structure

- [ ] Document saved with unique timestamp identifier (if user approved)

- [ ] Implementation checklist created with priority grouping



## Required Actions

1. Validate all input parameters and template access

2. Execute comprehensive TODO search with hierarchical organization

3. Analyze each TODO for validity and generate specific solutions

4. Populate template with structured findings and user decision tracking

5. Create directory structure `olaf-data/findings/remaining-todos/` if it doesn't exist

6. Propose document saving and execute if approved by user in the correct findings directory



## Output File Management



You MUST save all TODO resolution documents in the correct location:

- **Base Directory**: `olaf-data/findings/remaining-todos/`

- **File Name Pattern**: `todo-resolution-{repository_name}-{YYYYMMDD-HHmm}.md`

- **Full Path Example**: `olaf-data/findings/remaining-todos/todo-resolution-cytric-signpdf-20251022-1049.md`



**Directory Creation Instructions**:

1. Check if `olaf-data/findings/remaining-todos/` exists

2. If not, create the directory structure using appropriate commands:

   - Windows: `New-Item -ItemType Directory -Path "olaf-data\findings\remaining-todos" -Force`

   - Unix/Linux/macOS: `mkdir -p olaf-data/findings/remaining-todos`

3. Save the document in this directory only



**CRITICAL**: Never save TODO resolution documents in the workspace root or any other location.



## Error Handling



You WILL handle these scenarios:

- **Template Access Failed**: Provide manual template structure and continue

- **Invalid Repository Path**: Request valid path with directory listing

- **No TODOs Found**: Confirm search patterns and suggest expanding scope

- **Large Result Set (>50 TODOs)**: MANDATORY subset selection - do not proceed with full analysis without user choice

- **User Refuses Subset Selection**: Warn about session limits but proceed if explicitly confirmed

- **Document Save Failure**: Offer alternative save locations and formats



⚠️ **Critical Requirements**

- MANDATORY: Structure all output by Repository → Folder Path → File → TODO hierarchy

- MANDATORY: Default all user decision fields to "NO" for safety

- MANDATORY: Use Propose-Act protocol for document generation and saving

- NEVER modify source code files during analysis

- ALWAYS provide complete, ready-to-implement code solutions with specific line ranges

- ALWAYS validate generated code solutions are syntactically correct and compilable