# Step-by-Step Tutorial

**Generate Test Plan: Step-by-Step Tutorial**

**How to Execute the "Generate Test Plan" Workflow**

This tutorial shows exactly how to create comprehensive test plans based on functional specifications using the OLAF tester competency.

## Prerequisites

- OLAF framework properly installed and configured
- Access to functional specification document
- Understanding of testing methodologies and QA processes
- Access to the tester competency pack

## Step-by-Step Instructions

### Step 1: Prepare the Functional Specification
[Ensure you have the specification ready for analysis]

**User Action:**
1. Locate the functional specification document for the application/feature
2. Ensure the specification includes clear requirements and acceptance criteria
3. Note the full path to the specification file
4. Determine the application name for test plan identification

**System Response:**
Specification document should be accessible and readable.

### Step 2: Invoke the Test Plan Generation Command
**User Action:** Execute the OLAF command to start test plan generation
```
olaf generate test plan
```

**Provide Parameters:**
- **specification**: [/path/to/spec.md] - Path to the functional specification
- **application**: [ApplicationName] - Name of the application under test
- **test_levels**: (Optional) [["unit", "integration", "system", "acceptance"]] - Test levels to include
- **test_types**: (Optional) [["functional", "performance", "security"]] - Test types to include
- **coverage_target**: (Optional) [85] - Target test coverage percentage

### Step 3: Requirement Analysis Process
**What OLAF Does:**
- Reads and parses the functional specification document
- Identifies testable requirements from the specification
- Extracts acceptance criteria and success metrics
- Defines test objectives aligned with requirements
- Documents assumptions and constraints

**You Should See:** 
- Progress messages for specification analysis
- List of identified testable requirements
- Test objectives summary

### Step 4: Test Strategy Definition
**What OLAF Does:**
- Defines test levels based on parameters (unit, integration, system, acceptance)
- Identifies test types to execute (functional, performance, security, usability)
- Determines test environment requirements (hardware, software, network, data)
- Establishes entry criteria (prerequisites for starting testing)
- Defines exit criteria (conditions for completing testing)
- Plans test data requirements and setup

**You Should See:**
- Test strategy summary with levels and types
- Environment requirements specification
- Entry/exit criteria definitions

### Step 5: Test Case Development
**What OLAF Does:**
- Creates test cases in Gherkin format (Given-When-Then)
- Organizes test cases by feature or module
- Defines test data sets for each test case
- Specifies preconditions and postconditions
- Documents expected results with clear pass/fail criteria
- Includes both positive and negative test scenarios
- Ensures traceability to requirements

**You Should See:**
- Test cases organized by feature/module
- Gherkin-formatted scenarios
- Clear acceptance criteria for each test
- Traceability matrix linking tests to requirements

### Step 6: Test Execution Planning
**What OLAF Does:**
- Schedules test cycles and phases
- Allocates resources (testers, environments, tools)
- Defines risk management approach
- Plans defect management process
- Establishes reporting and communication strategy
- Documents test deliverables

**You Should See:**
- Test execution schedule
- Resource allocation plan
- Risk assessment matrix
- Defect management workflow

### Step 7: Test Plan Document Generation
**What OLAF Does:**
- Loads the test plan template from `templates/test-plan-template.md`
- Structures all planning information according to the template
- Includes all required sections:
  - Introduction and scope
  - Test items and features
  - Test approach and strategy
  - Test environment requirements
  - Entry/exit criteria
  - Test deliverables
  - Schedule and responsibilities
  - Risks and contingencies
- Formats the document in markdown

**You Should See:**
- Complete test plan document following the standard template
- All sections populated with relevant information
- Clear structure and formatting

### Step 8: Report Saving and Output
**What OLAF Does:**
- Generates filename in format: `test-plan-<application>-YYYYMMDD-NNN.md`
- Saves the test plan to `olaf-data/findings/` directory
- Displays the complete test plan document
- Provides summary of test plan contents

**You Should See:**
- Complete test plan in markdown format
- File save confirmation with location
- Summary statistics:
  - Number of test cases generated
  - Test coverage target
  - Number of features covered
  - Resource requirements summary

## Verification Checklist

✅ **Functional specification successfully analyzed**
✅ **All testable requirements identified**
✅ **Test strategy defined with levels and types**
✅ **Test cases created in Gherkin format**
✅ **Entry/exit criteria clearly defined**
✅ **Test environment requirements documented**
✅ **Risk assessment completed**
✅ **Test plan saved with proper naming convention**
✅ **Test plan follows official template structure**
✅ **Traceability to requirements established**

## Troubleshooting

**If specification cannot be read:**
- Verify the file path is correct and accessible
- Ensure the document format is supported (markdown, text)
- Check file permissions

**If no testable requirements found:**
- Review the specification for clarity and completeness
- Ensure requirements include acceptance criteria
- Consider using analyze-business-requirements first to validate the spec

**If test cases are incomplete:**
- Verify the specification includes sufficient detail
- Check that acceptance criteria are clearly defined
- Consider specifying test_types to focus the test case generation

**If template errors occur:**
- Verify the test plan template exists in the competency pack
- Check template format and structure
- Ensure all required template sections are present

## Key Learning Points

1. **Requirements-Driven Testing:** Test plans are directly derived from functional specifications
2. **Structured Approach:** Following the template ensures comprehensive coverage of all testing aspects
3. **Gherkin Format:** Test cases use Given-When-Then format for clarity and automation readiness
4. **Risk-Based Planning:** Test prioritization considers risk and business impact
5. **Traceability:** Clear links between requirements and test cases ensure coverage

## Next Steps to Try

- Review the generated test plan with the development team
- Validate test environment requirements with infrastructure team
- Prioritize test cases based on risk assessment
- Use the test plan to guide test case implementation
- Track test execution progress against the plan
- Update the test plan as requirements evolve

## Expected Timeline

- **Requirement analysis:** 2-3 minutes
- **Test strategy definition:** 2-3 minutes
- **Test case development:** 5-10 minutes depending on specification size
- **Test execution planning:** 2-3 minutes
- **Document generation:** 1-2 minutes
- **Total time:** 12-21 minutes
- **User input required:** Specification path, application name, and optional configuration parameters
