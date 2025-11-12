# Step-by-Step Tutorial

## Review User Story: Step-by-Step Tutorial

**How to Execute the "Review User Story" Workflow**

This tutorial shows exactly how to review user stories against standard templates to ensure quality, clarity, and completeness using the OLAF business-analyst competency.

## Prerequisites

- OLAF framework properly installed and configured
- A user story document or content to review
- Understanding of user story structure and acceptance criteria
- Access to the business-analyst competency pack

## Step-by-Step Instructions

### Step 1: Prepare the User Story Content

[Ensure you have the user story ready for review]

**User Action:**

1. Locate or prepare the user story text to be reviewed
2. Ensure the story content is accessible (either as text or file)
3. Note any specific template requirements or review depth needed
4. Prepare to provide the user story content to OLAF

**System Response:**
User story content should be readable and contain story elements for analysis.

### Step 2: Invoke the Review Command

**User Action:** Execute the OLAF command to start user story review

```bash
olaf review user story
```

**Provide Parameters:**

- **user_story_content**: [Your user story text] - The complete user story text to be reviewed
- **template_reference**: [specific template name] - Optional template to use for evaluation
- **review_depth**: [basic/thorough/comprehensive] - Depth level for the review (optional)

### Step 3: User Story Loading and Parsing

**What OLAF Does:**

- Receives and processes the user story content provided
- Parses and structures the story components for systematic analysis
- Identifies existing story elements (title, description, acceptance criteria, etc.)
- Prepares the content for template-based evaluation

**You Should See:** Confirmation that the user story has been loaded and parsed successfully

### Step 4: Template-Based Analysis Process

**What OLAF Does:**

- Loads the user story review template for evaluation criteria
- Evaluates the story against each template requirement systematically
- Checks for clarity, understandability, and completeness
- Assesses testability of acceptance criteria and verification methods
- Identifies missing or unclear information that needs clarification

**You Should See:** Progress through different evaluation criteria with findings noted

### Step 5: Structured Review Generation

**What OLAF Does:**

- Creates comprehensive markdown-formatted review based on analysis
- Structures review with standardized sections including:
  - Overall assessment summary and quality rating
  - Identified strengths and positive elements
  - Areas requiring improvement with specific recommendations
  - Clarifying questions to help improve the story
- Frames all feedback constructively and collaboratively

**You Should See:** Detailed review structured according to the standard template format

### Step 6: Review Report Saving and Output

**What OLAF Does:**

- Saves the review to `olaf-data/findings/user-story-reviews/` directory
- Generates filename in format: `user-story-review-YYYYMMDD-NNN.md`
- Provides summary statistics of the review results
- Displays the complete review with actionable recommendations

**You Should See:**

- Complete structured review of the user story
- File save confirmation with location
- Summary of strengths, improvement areas, and questions generated
- Overall quality assessment and rating

## Verification Checklist

✅ **User story successfully loaded and parsed for analysis**
✅ **Story evaluated against standard template requirements**
✅ **Clarity, testability, and completeness assessed systematically**
✅ **Review structured with standardized sections (summary, strengths, improvements, questions)**
✅ **Review saved to olaf-data/findings/user-story-reviews/ with proper naming**
✅ **Feedback framed constructively and collaboratively**

## Troubleshooting

**If user story content cannot be parsed:**

- Ensure the story text is complete and properly formatted
- Check that the content contains recognizable story elements
- Verify there are no encoding or format issues with the text

**If template evaluation seems incomplete:**

- Specify a particular template_reference if available
- Use "comprehensive" review_depth for more thorough analysis
- Ensure the user story has sufficient content for meaningful evaluation

**If clarifying questions are too general:**

- Provide more detailed user story content for specific analysis
- Consider using "thorough" or "comprehensive" review depth
- Review the generated questions to ensure they address specific story elements

## Key Learning Points

1. **Template-Based Quality Assurance:** The workflow uses standardized templates to ensure consistent and comprehensive user story evaluation
2. **Constructive Feedback Approach:** Reviews are structured to be helpful and collaborative rather than critical
3. **Actionable Recommendations:** Generates specific clarifying questions and improvement suggestions for story refinement

## Next Steps to Try

- Address the identified improvement areas in the user story
- Use the clarifying questions to gather additional story details
- Apply the review feedback to enhance story clarity and testability
- Repeat the review process after making improvements to verify enhancements

## Expected Timeline

- **Total review time:** 2-5 minutes depending on story complexity and review depth
- **User input required:** Providing user story content and configuration parameters
- **OLAF execution time:** Automated parsing, template-based analysis, and structured review generation