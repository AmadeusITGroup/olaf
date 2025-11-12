# Step-by-Step Tutorial

## Bootstrap Functional Spec from Code: Step-by-Step Tutorial

**How to Execute the "Bootstrap Functional Spec from Code" Workflow**

This tutorial shows exactly how to analyze source code and extract functionalities to create a draft functional specification using the OLAF business-analyst competency.

## Prerequisites

- OLAF framework properly installed and configured
- Access to a source code directory or codebase to analyze
- Understanding of functional specification structure
- Access to the business-analyst competency pack

## Step-by-Step Instructions

### Step 1: Prepare the Source Code

[Ensure you have the codebase ready for analysis]

**User Action:**

1. Locate the application's source code or codebase directory
2. Ensure the directory is accessible and contains the main application code
3. Note the full path to the source code directory

**System Response:**
Directory should be readable and contain analyzable source code files.

### Step 2: Invoke the Bootstrap Command

**User Action:** Execute the OLAF command to start functional spec generation

```bash
olaf bootstrap functional spec from code
```

**Provide Parameters:**

- **source_path**: [path/to/your/source-code] - Full path to the codebase directory
- **output_format**: [markdown/html/pdf] - Output format (default: markdown)
- **detail_level**: [overview/standard/detailed] - Level of detail (default: standard)

### Step 3: Code Analysis Process

**What OLAF Does:**

- Scans the directory structure and identifies entry points
- Analyzes main components and their relationships
- Extracts business logic and workflows from the source code
- Documents data models and system relationships

**You Should See:** Progress messages indicating directory scanning and code analysis phases

### Step 4: Business Logic Extraction

**What OLAF Does:**

- Identifies core business rules embedded in the code
- Maps out user flows and system interactions
- Documents system boundaries and external dependencies
- Identifies integration points and external services

**You Should See:** Summary of identified business processes and system components

### Step 5: Specification Generation

**What OLAF Does:**

- Loads the functional specification template
- Structures extracted content for business audience
- Translates technical code into business-focused language
- Includes relevant code examples and visual diagrams where helpful

**You Should See:** Formatted functional specification following the standard template structure

### Step 6: Output Generation and Saving

**What OLAF Does:**

- Generates filename in format: `FunctionalSpec-YYYYMMDD-NNN.md`
- Saves the specification to `olaf-data/specs/` directory
- Creates business-focused documentation without technical jargon
- Includes technical details in appendices for reference

**You Should See:**

- Complete functional specification in chosen format
- File save confirmation with location
- Executive summary of identified functionalities
- Clear separation between business and technical views

## Verification Checklist

✅ **Source code successfully analyzed and components identified**
✅ **Business logic extracted and documented in business terms**
✅ **Functional specification generated following template structure**
✅ **Specification saved to olaf-data/specs/ with proper naming convention**
✅ **Business-focused language used (no technical jargon in main sections)**
✅ **Traceability to source code maintained for validation**

## Troubleshooting

**If source code cannot be analyzed:**

- Verify the source path is correct and accessible
- Ensure the directory contains recognizable source code files
- Check if the codebase uses supported programming languages

**If business logic extraction is incomplete:**

- Try using 'detailed' level for more comprehensive analysis
- Ensure the source code contains meaningful business logic
- Check if code comments and documentation help with context

**If specification template errors occur:**

- Verify the functional specification template exists in the competency pack
- Check if the template is properly formatted and accessible

## Key Learning Points

1. **Code-to-Business Translation:** The workflow translates technical implementation into business-understandable functional requirements
2. **Template-Driven Consistency:** Uses standardized templates to ensure consistent specification structure
3. **Traceability Maintenance:** Maintains clear links between generated specification and source code for validation

## Next Steps to Try

- Review the generated functional specification with business stakeholders
- Validate the extracted functionalities against actual system behavior
- Use the specification as a starting point for requirements refinement
- Update and maintain the specification as the codebase evolves

## Expected Timeline

- **Total analysis time:** 5-15 minutes depending on codebase size
- **User input required:** Providing source path and configuration parameters
- **OLAF execution time:** Automated code analysis, business logic extraction, and specification generation