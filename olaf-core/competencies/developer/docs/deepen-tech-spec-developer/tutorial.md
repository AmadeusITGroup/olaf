# Step-by-Step Tutorial

**Deepen Tech Spec Developer: Step-by-Step Tutorial**

**How to Execute the "Developer-Focused Deep Technical Analysis" Workflow**

This tutorial shows exactly how to execute a comprehensive developer-focused technical analysis using the OLAF developer competency's deepen-tech-spec-developer functionality. This workflow creates chapter-based deep-dive documentation covering code quality, unit testing, architecture patterns, and design principles with evidence-based evaluation.

## Prerequisites

- OLAF framework properly installed and configured
- Existing technical specification file to deepen
- Application codebase to analyze (for evidence-based assessment)
- Basic understanding of software architecture and design patterns
- Access to project repository and documentation

## Step-by-Step Instructions

### Step 1: Initiate Deep Technical Analysis

[Brief description: Start the comprehensive developer-focused analysis by invoking the OLAF deepen-tech-spec-developer competency]

**User Action:**

1. Open your terminal or OLAF interface
2. Ensure you have access to both the technical specification and application codebase
3. Execute the OLAF deepen-tech-spec-developer competency using one of these methods:
   - Direct invocation: `olaf deepen-tech-spec-developer`
   - Via aliases: `olaf deepen tech spec`, `olaf deep dive spec`, `olaf chapter mode`

**OLAF Response:**
The system will prompt you to provide the required parameters for deep technical analysis.

### Step 2: Provide Specification and Application Details

**User Action:** Specify the tech spec file and application information

```text
Required Parameters:
- tech_spec_path: Path to the existing technical specification file (REQUIRED)
- application_name: Name of the application for file naming (REQUIRED)
- chapter_focus: Specific chapter to start with (OPTIONAL, defaults to first chapter)
```

**Provide Requirements/Parameters:**

- **tech_spec_path**: [Example - we used "docs/technical-specification.md"]
- **application_name**: [Example - we used "e-commerce-backend"]
- **chapter_focus**: [Example - we used "Architecture & Design Patterns"] (optional)

### Step 3: Validation and Prerequisites Check

**What OLAF Does:**

- Confirms tech specification file exists and is readable
- Validates application name is properly formatted (kebab-case)
- Checks for existing chapter files to prevent conflicts
- Verifies access to findings directory for file creation
- Gets current timestamp for chapter file naming

**You Should See:** Confirmation that all prerequisites are met and files are accessible

### Step 4: Tech Spec Analysis and Chapter Planning

**What OLAF Does:**

- **Reads and analyzes** existing technical specification
- **Extracts key information**: application architecture, components, technology stack, security features
- **Creates comprehensive chapter outline** covering all 6 developer-focused areas:
  1. Architecture & Design Patterns Assessment
  2. API Implementation Quality Analysis
  3. Data Access & Transaction Management
  4. Error Handling & Exception Strategy
  5. Unit Testing & Code Quality Evaluation
  6. Module Dependencies & Structure Assessment

**User Action:** Review and approve the proposed chapter structure

**You Should See:** Detailed chapter outline with developer-focused analysis areas presented for approval

### Step 5: Chapter Development Cycle (Iterative)

**What OLAF Does for Each Chapter:**

- **Deep Analysis**: Extracts detailed technical information from codebase with evidence
- **Evidence-Based Assessment**: Analyzes actual code patterns, violations, and implementations
- **Documentation Creation**: Creates comprehensive chapter with code examples and best practices
- **User Review**: Presents completed chapter and requests feedback

**User Action:** For each chapter completion:

```text
Session Options:
- Continue to next chapter in current session
- Request carry-over for new session (maintains progress)
- Stop analysis and generate final report
```

**What OLAF Does After Each Chapter:**

- Saves chapter file: `deep-dive-{application_name}-chapter-{N}-{chapter-name}-YYYYMMDD-NNN.md`
- Offers session transition management if needed
- Continues with next chapter or manages session carry-over

**You Should See:** Individual chapter files generated with comprehensive developer-focused analysis

### Step 6: Session Management and Final Documentation

**What OLAF Does:**

- **Session Transition**: Executes carry-over competency when requested for new sessions
- **Progress Tracking**: Maintains current progress state and next chapter information
- **Final Documentation**: Compiles all completed chapters into comprehensive deep-dive analysis
- **File Organization**: Saves all chapters to `olaf-data/findings/specs/` with proper naming

**You Should See:** Complete set of developer-focused technical chapters with evidence-based analysis

## Verification Checklist

✅ **Tech specification file successfully analyzed**
✅ **Chapter structure approved with all 6 developer-focused areas**
✅ **Evidence-based analysis completed for each chapter**
✅ **Code examples and implementation details included**
✅ **Chapter files saved with proper naming convention**
✅ **Session management handled for complex analysis sessions**

## Troubleshooting

**If tech specification file cannot be accessed:**

```bash
# Check file permissions and existence
ls -la docs/technical-specification.md
file docs/technical-specification.md
```

**If chapter conflicts are detected:**

- Review existing chapter files in `olaf-data/findings/specs/`
- Choose different application name or move existing files
- Use chapter_focus parameter to resume from specific chapter

**If codebase analysis fails:**

- Ensure access to complete application source code
- Verify that the codebase matches the technical specification
- Check for missing dependencies or build configuration issues

## Key Learning Points

1. **Evidence-Based Analysis:** All assessments are grounded in actual code implementation rather than theoretical documentation
2. **Chapter-Based Approach:** Complex technical analysis is broken into manageable, focused chapters for comprehensive coverage
3. **Session Management:** Long analysis sessions can be managed with carry-over functionality to maintain progress across multiple sessions

## Next Steps to Try

- Use the generated chapters to identify specific improvement areas in your codebase
- Apply the documented patterns and best practices to enhance code quality
- Use the analysis as input for technical debt prioritization and refactoring planning
- Share the developer-focused chapters with your development team for architectural discussions

## Expected Timeline

- **Total analysis time:** 2-6 hours (depending on application complexity and chapter count)
- **User input required:** Specification details and chapter approvals (15-30 minutes total)
- **OLAF analysis time:** Tech spec analysis and chapter planning (30-60 minutes)
- **Chapter development:** Iterative analysis and documentation (1-4 hours across sessions)