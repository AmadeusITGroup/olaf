# Step-by-Step Tutorial

**Check TODOs in Code: Step-by-Step Tutorial**

**How to Execute the "TODO Analysis and Resolution Planning" Workflow**

This tutorial shows exactly how to search, analyze, and provide solutions for TODO comments with user decision tracking using the OLAF developer competency's check-todos-in-code functionality. This workflow systematically identifies and provides actionable solutions for technical debt items.

## Prerequisites

- OLAF framework properly installed and configured
- Codebase with TODO comments to analyze
- Repository or project folder to scan
- Basic understanding of code maintenance and technical debt concepts
- Write access to workspace for document generation

## Step-by-Step Instructions

### Step 1: Initiate TODO Analysis

[Brief description: Start the comprehensive TODO analysis process by invoking the OLAF check-todos-in-code competency]

**User Action:**

1. Open your terminal or OLAF interface
2. Navigate to or identify the repository/project directory to analyze
3. Execute the OLAF check-todos-in-code competency using one of these methods:
   - Direct invocation: `olaf check-todos-in-code`
   - Via aliases: `olaf check todos`, `olaf todo analysis`, `olaf scan todos`

**OLAF Response:**
The system will prompt you to provide the required parameters for TODO analysis.

### Step 2: Provide Repository and Scan Parameters

**User Action:** Specify the repository details and scanning preferences

```text
Required Parameters:
- target_path: Path to folder or repository to scan (REQUIRED)
- repository_name: Name of the repository being analyzed (REQUIRED)
- file_extensions: File extensions to include (optional, defaults to common code files)
- todo_patterns: TODO patterns to search for (optional, defaults to TODO, FIXME, HACK, XXX, BUG)
- save_document: Save resolution document (optional, default: true)
- max_todos_threshold: Maximum TODOs to analyze in one session (optional, default: 50)
```

**Provide Requirements/Parameters:**

- **target_path**: [Example - we used "/src/main/java/com/company/project"]
- **repository_name**: [Example - we used "e-commerce-backend"]
- **file_extensions**: [Example - we used [".java", ".js", ".py"]] (optional)
- **todo_patterns**: [Example - we used ["TODO", "FIXME", "BUG", "HACK"]] (optional)
- **save_document**: [Example - we used "true"] (optional)

### Step 3: Initial Count and Subset Selection

**What OLAF Does:**

- Executes quick TODO count across all specified file types
- Presents total count to user immediately
- Gets current timestamp for document generation
- Assesses if TODO count exceeds threshold (default: 50)

**User Action (if TODOs > threshold):** Choose subset approach:

```text
Subset Options:
1. By Priority: Focus on FIXME/BUG patterns only (critical items)
2. By Folder: Choose specific folder or subfolder
3. By File Type: Limit to specific extensions
4. By Author: Focus on specific author's TODOs
5. By Date: Most recent TODOs only
6. Proceed Anyway: Analyze all (may be slow/incomplete)
```

**You Should See:** Clear breakdown of TODO count with recommended subset options for manageability

### Step 4: Targeted Search and Context Extraction

**What OLAF Does:**

- Executes targeted TODO search based on your subset choice
- Parses results by repository structure: Repo → Folder Path → File → Line
- Extracts TODO context including surrounding code (±5 lines)
- Identifies author information if available in comments
- Organizes findings hierarchically for systematic analysis

**You Should See:** Progress updates during search and context extraction phases

### Step 5: Comprehensive TODO Analysis

**What OLAF Does for Each TODO:**

- **Current validity assessment**: Determines if TODO is still relevant
- **Priority classification**: 🔥 Critical, ⚠️ High, 📝 Medium, 💡 Low
- **Actual replacement code solution**: Complete, syntactically correct code (not just recommendations)
- **Specific line ranges to replace**: Exact locations for implementation
- **Implementation and testing instructions**: Step-by-step guidance
- **Effort estimation**: Time and complexity assessment
- **Dependencies identification**: Required changes or prerequisites

**You Should See:** Detailed analysis with actionable solutions for each TODO item

### Step 6: Document Generation and User Decision Tracking

**User Action:** Approve saving the TODO resolution document

**What OLAF Does:**

- Loads the TODO resolution template
- Populates template with structured findings in repository hierarchy
- Includes user decision tracking sections for each TODO (defaults to "NO" for safety)
- Generates unique document: `todo-resolution-{repo_name}-{timestamp}.md`
- Saves document to workspace with complete analysis and solutions

**You Should See:** Complete TODO resolution document with user decision tracking and implementation guidance

## Verification Checklist

✅ **Repository successfully scanned for TODO patterns**
✅ **TODO count assessed and subset approach selected (if needed)**
✅ **Each TODO analyzed with validity, priority, and solution**
✅ **Actual replacement code provided (not just recommendations)**
✅ **User decision tracking sections included for each TODO**
✅ **TODO resolution document saved with unique identifier**

## Troubleshooting

**If no TODOs are found:**

```bash
# Manual search to verify TODOs exist
grep -r "TODO\|FIXME\|HACK\|XXX\|BUG" . --include="*.java" --include="*.js" --include="*.py"
find . -name "*.java" -exec grep -l "TODO" {} \;
```

**If TODO count is overwhelming:**

- Use subset selection by priority (focus on FIXME and BUG first)
- Limit analysis to specific critical folders (e.g., /src/main)
- Filter by file types that are most actively maintained

**If generated solutions seem incorrect:**

- Review the surrounding code context provided
- Check that file extensions match the programming language
- Verify that TODO patterns were correctly identified

## Key Learning Points

1. **Hierarchical Organization:** TODOs are organized by Repository → Folder → File structure for systematic resolution
2. **Actionable Solutions:** Each TODO receives actual replacement code with specific line ranges, not just recommendations
3. **User Decision Control:** All resolution decisions default to "NO" for safety, requiring explicit user approval for implementation

## Next Steps to Try

- Use the generated document to systematically address TODOs by priority
- Implement the provided solutions following the detailed instructions
- Track progress by updating user decisions from "NO" to "YES" as TODOs are resolved
- Set up regular TODO analysis to prevent technical debt accumulation

## Expected Timeline

- **Total analysis time:** 10-30 minutes (depending on TODO count and complexity)
- **User input required:** Repository details and subset selection (2-5 minutes)
- **OLAF scanning time:** TODO search and context extraction (3-10 minutes)
- **Analysis and documentation:** Solution generation and document creation (5-15 minutes)