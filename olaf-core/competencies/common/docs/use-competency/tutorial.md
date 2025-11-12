# Use Competency: Step-by-Step Tutorial

**How to Execute the "Use Competency" Workflow**

This tutorial shows how to use intelligent competency routing to find and execute the right competency for your goal.

## Prerequisites

- Clear understanding of what you want to accomplish
- Basic description of your goal or problem
- Willingness to provide clarifying details if needed

## Step-by-Step Instructions

### Step 1: Invoke the Router
Start the competency discovery process

**User Action:**
1. Type one of these commands:
   - `use competency`
   - `find competency`
   - `execute competency`
2. Describe what you want to accomplish

**OLAF Response:**
OLAF will begin analyzing your goal and searching for matching competencies

### Step 2: Describe Your Goal
**User Action:** Clearly describe what you want to accomplish
```
I want to review my code for security vulnerabilities and get recommendations
for improvements
```

**Provide Context:**
- **Technology**: Python web application
- **Framework**: Django
- **Focus**: Security best practices

### Step 3: Competency Discovery
**What OLAF Does:**
- Analyzes your goal description
- Searches competency index for matches
- Ranks competencies by relevance
- Identifies the best match
- May ask clarifying questions if ambiguous

**You Should See:** Identification of matching competency

### Step 4: Confirmation (if needed)
**What OLAF May Do:**
- Present the identified competency
- Explain why it matches your goal
- Ask for confirmation to proceed
- Request additional details if needed

**You Should See:** Competency identified with brief explanation

### Step 5: Automatic Execution
**What OLAF Does:**
- Automatically executes the identified competency
- Passes your context and requirements
- Runs the competency workflow
- Delivers results

**You Should See:** The competency executing and producing results

## Verification Checklist

✅ **Correct competency was identified**
✅ **Competency matches your goal**
✅ **Execution began automatically**
✅ **Results are relevant to your need**

## Troubleshooting

**If wrong competency is selected:**
- Provide more specific description of your goal
- Mention the domain or technology explicitly
- Clarify what you don't want: "not testing, but code review"

**If multiple competencies seem relevant:**
- OLAF will ask you to choose
- Provide more context to narrow down
- Try the suggested competency and adjust if needed

**If no competency matches:**
- Try broader description
- Use `olaf help` to browse available competencies
- Consider if your goal requires human expertise: `find expert contact`

**If you want to see options before executing:**
- Ask: "what competencies are available for [goal]?"
- Use `olaf help` to browse first
- Then use `use competency` with specific choice

## Key Learning Points

1. **Natural Language**: Describe goals naturally, no need to memorize commands
2. **Intelligent Routing**: Automatically finds the best match
3. **Seamless Execution**: Routes and executes in one step
4. **Context-Aware**: Uses your context to improve matching

## Next Steps to Try

- Use for different types of goals (development, architecture, documentation)
- Experiment with different description styles
- Combine with other competencies for complex workflows
- Bookmark frequently used competencies for direct access

## Expected Timeline

- **Total routing time:** 1-2 minutes
- **User input required:** Goal description (30 seconds)
- **OLAF execution time:** Discovery and routing (30 seconds)
- **Competency execution:** Varies by competency
