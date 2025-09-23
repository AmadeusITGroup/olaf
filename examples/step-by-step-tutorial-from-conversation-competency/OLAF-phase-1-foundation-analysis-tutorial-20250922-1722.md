# Master Your Project Onboarding: Step-by-Step Tutorial

**From Zero to Complete Foundation Analysis in Under 30 Minutes**

**How to Execute the "OLAF Phase 1 Foundation Analysis"**

This tutorial shows exactly how to reproduce the comprehensive project onboarding execution demonstrated in conversation-record-20250922-1651.md. Follow these steps to perform a complete foundation analysis of any enterprise Java project.

## Prerequisites

- VS Code workspace with the target project repository
- OLAF framework installed (`olaf-core/` directory structure)
- Python environment with required dependencies
- Git repository access and basic terminal knowledge
- Windows PowerShell (or equivalent terminal for your OS)

## Step-by-Step Instructions

### Step 1: Initiate Project Onboarding Request
**What this accomplishes:** Triggers the OLAF framework to begin comprehensive project analysis

**User Action:**
1. Open VS Code in your project workspace
2. Ensure you have the target project directory (e.g., `CRM-System/`)
3. Type: `"onboard project [project-name]"`

**GitHub Copilot Response:**
The system will:
- Read required initialization files (`memory-map.md`, `core-principles.md`, `query-competency-index.md`)
- Identify the matching competency: "onboard project" → `orchestrate-project-onboarding.md`
- Present a comprehensive 10-phase analysis plan
- Propose analysis of your repository with output location

**Expected Output:** Detailed analysis proposal with 10 structured phases

### Step 2: Confirm Analysis Execution
**User Action:** Respond with `"yes"` to approve the comprehensive analysis

**GitHub Copilot Response:**
The system automatically:
1. Creates todo list with 11 items (initialization + 10 phases)
2. Checks for existing output directory (e.g., `olaf-data/product/documentations/CRM-System/`)
3. Creates fresh directory structure if needed
4. Sets up foundation subdirectory for Phase 1 outputs

**Expected Output:** 
- Todo list created and displayed
- Directory structure: `olaf-data/product/documentations/[project-name]/foundation/`

### Step 3: Execute Workspace Content Structure Analysis
**What GitHub Copilot Does Automatically:**
1. Reads Phase 1 workflow: `olaf-core/prompts/onboard/workflows/phase-1-foundation.md`
2. Loads analysis prompt: `analyze-workspace-content-structure.md`
3. Retrieves current timestamp using: `Get-Date -Format "yyyyMMdd-HHmm"`
4. Runs Python script: `olaf-core/tools/commons/project-onboarding/workspace_content_analyzer.py`
5. Performs manual directory analysis using PowerShell commands
6. Analyses Maven POM configuration
7. Creates comprehensive workspace analysis document

**Expected Output:** 
- `script-workspace-structure.md` (automated analysis)
- `analyze-workspace-content-structure.md` (comprehensive manual analysis)

**File Contains:**
- Complete directory tree structure
- Maven project layout verification
- Build artifact analysis
- Configuration file identification

### Step 4: Repository Application Classification
**What GitHub Copilot Does Automatically:**
1. Loads classification prompt: `classify-repo-application-types.md`
2. Performs semantic search for Spring patterns (controller, service, DAO, entity)
3. Examines key source files:
   - Controller: `src/main/java/com/spring/controller/CustomerController.java`
   - Service: `src/main/java/com/spring/service/CustomerServiceImpl.java`
   - Aspect: `src/main/java/com/spring/aspect/LoggingAspect.java`
4. Reviews web application structure: `src/main/webapp/WEB-INF/view/`
5. Analyses SQL database scripts: `sql-scripts/customers.sql`

**Expected Output:** `classify-repo-application-types.md`

**File Contains:**
- Application type determination (e.g., "Full-Stack Enterprise Web Application")
- Architecture pattern identification (e.g., "Multi-tier MVC")
- Technology stack classification
- Framework analysis results

### Step 5: Programming Language Distribution Analysis
**What GitHub Copilot Does Automatically:**
1. Reads language analysis prompt: `analyze-repo-language-distribution.md`
2. Executes Python script: `language_distribution_analyzer.py`
3. Generates automated output: `script-language-distribution.md`
4. Performs additional PowerShell file extension analysis
5. Conducts polyglot architecture assessment excluding build artifacts

**Expected Output:**
- `script-language-distribution.md` (automated metrics)
- `analyze-repo-language-distribution.md` (comprehensive analysis)

**File Contains:**
- Language percentages (e.g., Java 62.7%, JSP 16.8%)
- Lines of code per language
- File count distribution
- Polyglot architecture assessment

### Step 6: Repository Size Metrics Analysis
**What GitHub Copilot Does Automatically:**
1. Reads size metrics prompt: `measure-repo-size-metrics.md`
2. Executes Python script: `repo_size_metrics_calculator.py`
3. Generates automated output: `script-size-metrics.md`
4. Performs Git repository analysis: `git count-objects -vH`
5. Retrieves Git commit history and branch information
6. Calculates comprehensive size and efficiency metrics

**Expected Output:**
- `script-size-metrics.md` (automated calculations)
- `measure-repo-size-metrics.md` (detailed analysis)

**File Contains:**
- Repository size breakdown (total vs source code)
- Development efficiency metrics (98.6% build artifacts vs 1.4% source)
- Git repository statistics
- Lines of code totals

### Step 7: Phase 1 Completion and Status Update
**What GitHub Copilot Does Automatically:**
1. Updates todo list marking Phase 1 as completed
2. Provides comprehensive phase completion summary
3. Documents key findings across all 4 foundation tasks
4. Lists all generated documentation files
5. Confirms readiness for Phase 2 (Technology Understanding)

**Expected Results You Should Have:**
1. **Workspace Analysis** (.md file) - Complete directory structure and Maven layout
2. **Application Classification** (.md file) - Technology stack and architecture type
3. **Language Distribution** (.md file) - Polyglot analysis with percentages
4. **Size Metrics** (.md file) - Repository efficiency and Git statistics
5. **Automated Scripts Output** (.md files) - Python tool results for verification

**All files located in:** `olaf-data/product/documentations/[project-name]/foundation/`

### Step 8: Optional - Store Conversation Record
**User Action:** Type `"store conversation"` if you want to document the session

**Provide Model Information:** Specify AI model when prompted (e.g., "sonnet 4")

**GitHub Copilot Response:**
Creates comprehensive conversation record documenting the entire session

**Expected Output:** `conversation-record-YYYYMMDD-HHmm.md` in `olaf-data/product/documentations/conversations/`

## Verification Checklist

✅ **Phase 1 Foundation Analysis Complete:**
- [ ] 4 analysis tasks completed successfully
- [ ] 7 documentation files generated (4 analysis + 3 script outputs)
- [ ] All files saved in correct foundation directory
- [ ] Todo list shows Phase 1 as completed
- [ ] Key metrics identified: application type, language distribution, size efficiency

✅ **Quality Indicators:**
- [ ] Application classified correctly (e.g., Full-Stack Enterprise Web Application)
- [ ] Primary language identified with percentage (e.g., Java 62.7%)
- [ ] Repository efficiency calculated (source vs build artifacts ratio)
- [ ] Git repository health confirmed (commit count, branch structure)

✅ **Documentation Standards:**
- [ ] All files follow naming convention with timestamps
- [ ] Both automated and manual analysis completed
- [ ] Prerequisites for Phase 2 established

## Troubleshooting

**Issue:** Python scripts fail to execute
**Solution:** Ensure Python environment is configured correctly using `configure_python_environment` tool

**Issue:** Directory structure not created
**Solution:** Check write permissions to workspace and verify `olaf-data/` directory exists

**Issue:** Git commands fail
**Solution:** Ensure you're in a valid Git repository with proper access permissions

**Issue:** Maven analysis incomplete
**Solution:** Verify `pom.xml` exists in project root and is accessible

**Issue:** Missing analysis files
**Solution:** Check that all 4 Phase 1 tasks completed - rerun any missing analyses

## Key Learning Points

1. **OLAF Framework Structure:** Foundation analysis provides baseline understanding before detailed technical analysis
2. **Automated vs Manual Analysis:** Python scripts provide metrics whilst manual analysis adds context and insights
3. **Comprehensive Documentation:** Each phase generates multiple documents for different perspectives
4. **Systematic Approach:** 10-phase methodology ensures nothing is overlooked in project understanding
5. **Quality Metrics:** Efficiency ratios and language distribution provide immediate project health indicators
6. **Scalable Process:** Same methodology works for any enterprise Java project regardless of size

## Next Steps to Try

- Proceed to Phase 2: Technology Understanding for detailed technical stack analysis
- Review generated documentation to identify potential improvement areas
- Use metrics to compare with other projects in your organisation
- Share foundation analysis with team members for collaborative review

## Expected Timeline

- **Total analysis time:** 15-25 minutes
- **User input required:** Initial project name, confirmation responses, optional conversation storage
- **GitHub Copilot execution time:** Fully automated analysis with Python scripts and file examination
- **Final deliverables:** 7 comprehensive analysis files ready for Phase 2 progression

---

*This tutorial is based on the successful execution demonstrated in conversation-record-20250922-1651.md using the OLAF framework methodology.*