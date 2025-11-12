# Tutorial: Create Prompt

## Overview
This tutorial guides you through creating a new structured prompt for OLAF using the Create Prompt competency. You'll learn how to generate prompts that follow OLAF standards, include proper error handling, and integrate seamlessly with the framework.

## Prerequisites
- OLAF framework installed and configured
- Access to OLAF competencies directory
- Understanding of the task your prompt will address
- Terminal access for timestamp generation

## Estimated Time
30-45 minutes

## Steps

### Step 1: Invoke the Create Prompt Competency
Open your IDE and invoke the competency:
```
olaf create prompt
```

**Expected Result**: The competency activates and begins the prompt creation workflow.

### Step 2: Provide User Request
When prompted, describe what your new prompt should do:
```
Example: "Create a prompt that analyzes code complexity and suggests refactoring opportunities"
```

**Expected Result**: The competency acknowledges your request and proceeds to next parameter.

### Step 3: Specify Prompt Name
Provide a descriptive name in kebab-case (max 4 words):
```
Example: "analyze-code-complexity"
```

**Expected Result**: Name is validated and accepted.

### Step 4: Select Target Competency
The competency lists available competency packs. Select the appropriate one:
```
Example: "developer"
```

**Expected Result**: Competency selection confirmed, duplicate check performed.

### Step 5: Review Generated Prompt
The competency generates a complete prompt following OLAF template. Review it carefully:
- Check all sections are present (Time Retrieval, Input Parameters, Process, etc.)
- Verify imperative language is used consistently
- Confirm error handling is comprehensive
- Validate success criteria are measurable

**Expected Result**: Generated prompt presented for your review.

### Step 6: Approve or Request Changes
Using Propose-Confirm-Act protocol:
- Approve if prompt meets requirements
- Request specific changes if needed

**Expected Result**: Prompt is saved to target competency's prompts folder.

### Step 7: Review Manifest Update
The competency updates the target competency's manifest with the new entry point.

**Expected Result**: Manifest updated with new prompt entry, aliases generated.

### Step 8: Approve Reindexing (Optional)
When offered, approve reindexing to make your prompt immediately discoverable:
```
Response: "yes"
```

**Expected Result**: Competency index regenerated, new prompt available for use.

## Verification Checklist
- [ ] Prompt file created in correct location
- [ ] All template sections present in generated prompt
- [ ] Imperative language used consistently
- [ ] Error handling scenarios included
- [ ] Success criteria defined
- [ ] Manifest updated with new entry point
- [ ] Aliases generated for prompt invocation
- [ ] Competency index updated (if approved)

## Troubleshooting

### Issue: Competency directory not found
**Solution**: Verify OLAF is properly installed and competencies directory exists at expected location.

### Issue: Duplicate prompt detected
**Solution**: Review existing prompt, decide whether to modify it or create with different name.

### Issue: Manifest update failed
**Solution**: Check write permissions on manifest file, verify JSON syntax is valid.

### Issue: Reindexing script not found
**Solution**: Verify Python environment is configured, check script path in prompt-engineer competency.

## Next Steps
- Test your new prompt with real use cases
- Run Check Prompt Compliance to validate quality
- Generate tutorial for your prompt using Generate Tutorial
- Share prompt with team members

## Additional Resources
- [Prompt Template](../../templates/prompt-template.md)
- [Prompting Principles](../../templates/prompting-principles.md)
- [Check Prompt Compliance](../check-prompt-compliance/description.md)
