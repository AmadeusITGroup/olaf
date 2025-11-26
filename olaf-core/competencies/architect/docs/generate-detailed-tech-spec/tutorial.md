# Step-by-Step Tutorial

**Generate Detailed Tech Spec: Step-by-Step Tutorial**

**How to Execute the "Generate Detailed Tech Spec" Workflow**

This tutorial shows exactly how to create comprehensive technical specification documents with code examples and source references using the OLAF architect competency.

## Prerequisites

- OLAF framework properly installed and configured
- Access to the source codebase for analysis
- General technical specification document available
- Understanding of the application architecture
- Access to the architect competency pack

## Step-by-Step Instructions

### Step 1: Prepare the General Specification
[Ensure you have the parent specification ready]

**User Action:**
1. Locate or create a general technical specification document
2. Identify which sections need detailed documentation
3. Note the full path to the specification file
4. Determine the application name for output organization

**System Response:**
Specification document should be accessible and readable.

### Step 2: Invoke the Documentation Command
**User Action:** Execute the OLAF command to start detailed spec generation
```
olaf generate detailed tech spec
```

**Provide Parameters:**
- **spec_path**: [/path/to/general-spec.md] - Path to the parent specification
- **application_name**: [AppName] - Name for output organization
- **sections**: [["Error Handling", "Configuration", "Authentication"]] - Sections to detail
- **focus_areas**: (Optional) [["Security", "Performance"]] - Specific emphasis areas
- **output_dir**: (Optional) [/custom/output/path] - Custom output location

### Step 3: Initial Setup and Job Creation
**What OLAF Does:**
- Creates a tracking job for the documentation work
- Sets up directory structure at `olaf-data/findings/detailed-specs/<application_name>-spec/`
- Initializes documentation templates for each section
- Validates access to source code and specification

**You Should See:** 
- Job creation confirmation
- Directory structure setup messages
- Template initialization progress

### Step 4: Source Code Analysis
**What OLAF Does:**
- Scans codebase for components relevant to each section
- Identifies key classes, functions, and modules
- Maps relationships and dependencies between components
- Extracts code examples and implementation patterns
- Analyzes configuration files and setup code

**You Should See:**
- Progress messages for each section being analyzed
- List of identified components per section
- Dependency mapping information

### Step 5: Documentation Generation for Each Section
**What OLAF Does:**
For each specified section:
- Creates section overview and purpose statement
- Documents component breakdowns with responsibilities
- Includes comprehensive code examples with context
- Generates architecture diagrams (if applicable)
- Documents design decisions and rationale
- Links to specific source files with line numbers
- Describes implementation patterns and best practices

**You Should See:**
- Section-by-section documentation progress
- Code example extraction confirmations
- Diagram generation (if applicable)
- Source file reference mapping

### Step 6: Quality Assurance and Validation
**What OLAF Does:**
- Validates all code examples for syntax correctness
- Verifies accuracy of source file references
- Ensures consistency with the general specification
- Checks for completeness of each section
- Cross-references between related sections

**You Should See:**
- Validation progress messages
- Any warnings about missing or inconsistent information
- Confirmation of quality checks passed

### Step 7: Documentation Package Assembly
**What OLAF Does:**
- Organizes all section specifications into a coherent package
- Creates a main index document linking all sections
- Generates cross-reference tables
- Includes supporting diagrams and assets
- Creates a generation report with metadata

**You Should See:**
- Final documentation structure
- Index file creation
- Asset organization confirmation
- Generation report summary

### Step 8: Output and Delivery
**What OLAF Does:**
- Saves all documentation to the specified output directory
- Displays summary of generated documentation
- Lists all created files and their purposes
- Provides recommendations for next steps

**You Should See:**
- Complete file listing with paths
- Documentation package summary
- Sections documented count
- Files analyzed count
- Any issues or recommendations

## Verification Checklist

✅ **All requested sections have detailed documentation**
✅ **Code examples are complete and syntactically correct**
✅ **Source file references include accurate paths and line numbers**
✅ **Architecture diagrams are included where applicable**
✅ **Design decisions are documented with rationale**
✅ **Cross-references between sections are accurate**
✅ **Documentation follows consistent formatting**
✅ **Output saved to correct directory structure**

## Troubleshooting

**If source code cannot be analyzed:**
- Verify the codebase is accessible from the working directory
- Check file permissions for reading source files
- Ensure the code structure is recognizable (standard project layout)

**If code examples are incomplete:**
- Verify the section names match actual code organization
- Check that relevant source files are not excluded by .gitignore
- Consider specifying focus_areas to guide extraction

**If specification inconsistencies are found:**
- Review the general specification for clarity
- Ensure section names in the spec match requested sections
- Validate that the spec accurately describes the implementation

## Key Learning Points

1. **Code-Driven Documentation:** Specifications are generated from actual implementation, ensuring accuracy
2. **Section-Based Organization:** Documentation is organized by architectural concerns for easy navigation
3. **Comprehensive Context:** Each component includes purpose, implementation, and usage examples
4. **Traceability:** Direct links to source files maintain connection between docs and code

## Next Steps to Try

- Review generated documentation with the development team
- Use the detailed specs for developer onboarding
- Keep documentation in sync with code through periodic regeneration
- Create additional sections for other architectural concerns
- Use the specs as basis for code review and refactoring decisions

## Expected Timeline

- **Initial setup:** 1-2 minutes
- **Source code analysis:** 2-5 minutes per section
- **Documentation generation:** 3-5 minutes per section
- **Quality assurance:** 2-3 minutes
- **Total time:** 10-30 minutes depending on number of sections
- **User input required:** Specification path, section selection, and configuration parameters
