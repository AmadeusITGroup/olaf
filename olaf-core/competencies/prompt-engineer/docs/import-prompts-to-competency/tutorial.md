# Tutorial: Import Prompts To Competency (Phase 1)

## Overview
Analyze external prompt collections and generate mapping recommendations for OLAF integration.

## Prerequisites
- External prompts to import
- OLAF framework installed
- Understanding of source prompt structure

## Estimated Time
30-45 minutes

## Steps

### Step 1: Invoke Import Prompts
```
olaf import prompts
```

### Step 2: Specify Source Directory
Provide path to directory containing prompts to import.

### Step 3: Select Analysis Scope
Choose "structure", "content", or "both".

### Step 4: Configure Duplicate Handling (Optional)
Specify how to handle duplicates: "skip", "merge", or "rename".

### Step 5: Review Analysis Report
Examine mapping recommendations, duplicate detection, and complexity assessment.

### Step 6: Refine Mapping Plan
Adjust recommendations based on your understanding of prompts.

### Step 7: Approve Migration Plan
Confirm the plan is ready for Phase 2 execution.

## Verification Checklist
- [ ] All prompts analyzed
- [ ] Competency mappings recommended
- [ ] Duplicates identified
- [ ] Complexity assessed
- [ ] Effort estimated
- [ ] Plan approved

## Troubleshooting
- **Source directory not found**: Verify path
- **Unclear mappings**: Manually specify target competencies

## Next Steps
- Review mapping plan with stakeholders
- Proceed to Deploy Imported Prompts (Phase 2)
- Create new competency packages if needed
