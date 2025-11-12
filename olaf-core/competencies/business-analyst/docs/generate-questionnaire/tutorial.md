# Step-by-Step Tutorial

## Generate Questionnaire: Step-by-Step Tutorial

**How to Execute the "Generate Questionnaire" Workflow**

This tutorial shows exactly how to create a well-structured questionnaire for gathering specific information from a target audience using the OLAF business-analyst competency.

## Prerequisites

- OLAF framework properly installed and configured
- Clear understanding of the questionnaire purpose and target audience
- Access to the business-analyst competency pack
- Knowledge of desired question types and structure

## Step-by-Step Instructions

### Step 1: Define Questionnaire Requirements

[Prepare the questionnaire parameters and objectives]

**User Action:**

1. Clearly define the primary goal/purpose of the questionnaire
2. Identify the target audience and their characteristics
3. Determine preferred question types and desired length
4. Consider logical sections for question grouping

**System Response:**
Requirements should be clear and specific to guide questionnaire creation.

### Step 2: Invoke the Generation Command

**User Action:** Execute the OLAF command to start questionnaire generation

```bash
olaf generate questionnaire
```

**Provide Parameters:**

- **purpose**: [Primary goal of the questionnaire] - Clear description of what you want to achieve
- **audience**: [Target audience description] - Who will be responding to the questionnaire
- **question_types**: [open-ended, multiple-choice, Likert, etc.] - Preferred question types (optional)
- **sections**: [section names] - Logical groupings for questions (optional)
- **length**: [short/medium/long] - Desired questionnaire length (default: medium)

### Step 3: Questionnaire Design Process

**What OLAF Does:**

- Defines clear objectives based on the specified purpose
- Determines appropriate question types for the target audience
- Structures logical flow and question progression
- Ensures question clarity, neutrality, and bias-free language

**You Should See:** Progress messages indicating design phase completion and objective clarification

### Step 4: Content Creation Process

**What OLAF Does:**

- Drafts introduction and clear instructions for respondents
- Creates relevant questions aligned with the stated purpose
- Adds appropriate response options for structured questions
- Includes demographic section if applicable to the audience

**You Should See:** Generated questions organized by sections with appropriate response formats

### Step 5: Review and Refinement Process

**What OLAF Does:**

- Checks for bias and leading questions in the content
- Ensures logical progression and flow between sections
- Validates question clarity and respondent understanding
- Estimates completion time for the questionnaire

**You Should See:** Refined questionnaire with clear, neutral questions and logical structure

### Step 6: Output Generation and Saving

**What OLAF Does:**

- Applies the questionnaire template structure
- Formats the questionnaire as a complete markdown document
- Saves to `olaf-data/questionnaires/` with descriptive filename
- Creates copy-paste friendly format for distribution

**You Should See:**

- Complete questionnaire preview with structure overview
- Estimated completion time for respondents
- File save confirmation with location
- Ready-to-distribute format

## Verification Checklist

✅ **Questionnaire objectives clearly defined and aligned with purpose**
✅ **Questions are clear, concise, and bias-free**
✅ **Related questions grouped together in logical sections**
✅ **Appropriate question types used for target audience**
✅ **Questionnaire saved to olaf-data/questionnaires/ with proper naming**
✅ **Introduction, instructions, and thank you note included**

## Troubleshooting

**If questions seem biased or leading:**

- Review the purpose statement for neutrality
- Ensure the target audience description is objective
- Consider using more neutral question types (open-ended vs. leading multiple choice)

**If questionnaire structure is unclear:**

- Specify sections explicitly to guide logical grouping
- Review the target audience needs for appropriate structure
- Consider breaking complex topics into multiple sections

**If questionnaire is too long or short:**

- Adjust the length parameter (short/medium/long)
- Refine the purpose to be more or less specific
- Consider splitting into multiple shorter questionnaires

## Key Learning Points

1. **Purpose-Driven Design:** The workflow creates questions specifically aligned with stated objectives and target audience needs
2. **Bias Prevention:** Automatically checks for and prevents leading questions and biased language
3. **Template Consistency:** Uses standardized templates to ensure professional questionnaire structure

## Next Steps to Try

- Review the generated questionnaire with stakeholders before distribution
- Test the questionnaire with a small sample of the target audience
- Use the questionnaire for data collection and analysis
- Refine based on initial feedback and response patterns

## Expected Timeline

- **Total generation time:** 3-7 minutes depending on complexity and length
- **User input required:** Providing purpose, audience, and configuration parameters
- **OLAF execution time:** Automated design, content creation, review, and formatting