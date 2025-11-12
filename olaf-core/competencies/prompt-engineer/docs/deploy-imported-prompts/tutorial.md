# Tutorial: Deploy Imported Prompts (Phase 2)

## Overview
Execute the approved migration plan to convert and deploy external prompts to OLAF competencies.

## Prerequisites
- Approved mapping plan from Phase 1
- OLAF framework installed
- Write access to target competencies

## Estimated Time
45-90 minutes (depending on number of prompts)

## Steps

### Step 1: Invoke Deploy Prompts
```
olaf deploy prompts
```

### Step 2: Provide Mapping Plan Path
Specify path to the approved mapping plan from Phase 1.

### Step 3: Select Execution Mode
Choose "sequential", "batch", or "selective".

### Step 4: Configure Validation Level
Select "basic", "standard", or "comprehensive".

### Step 5: Confirm Backup Settings
Approve backing up original prompts (recommended).

### Step 6: Monitor Deployment Progress
Watch as prompts are converted and deployed.

### Step 7: Review Deployment Report
Examine success/failure status for each prompt.

### Step 8: Address Any Failures
Manually handle prompts that failed automated deployment.

## Verification Checklist
- [ ] All prompts deployed
- [ ] Manifests updated
- [ ] Validation passed
- [ ] Originals backed up
- [ ] Deployment report generated

## Troubleshooting
- **Conversion failed**: Review prompt for complex dependencies
- **Validation failed**: Check prompt against OLAF standards

## Next Steps
- Test deployed prompts with real use cases
- Generate tutorials for deployed prompts
- Update team documentation
- Communicate new capabilities to users
