# Merge Competency Pack to Main - Tutorial

## Quick Start

**Goal**: Merge the `researcher` competency pack from feature branch to main.

**Command**: 
```
/olaf-merge-competency-pack-to-main
```

**Expected interaction**:
```
Agent: Which competency pack would you like to merge to main?
You: researcher

Agent: Which collection(s) should I add it to? (e.g., "all", "developer", etc.)
You: all

Agent: I'll create branch feat/add-researcher-pack. Proceed?
You: yes

[Agent executes workflow...]

Agent: ✅ Complete! Open PR: https://github.com/Amadeus-xDLC/genai.olaf/compare/main...feat/add-researcher-pack?expand=1
```

## Step-by-Step Tutorial

### Step 1: Identify the Competency Pack

First, determine which pack you want to merge. List available packs on feature branch:

```bash
git ls-tree -d --name-only feature/olaf-feature-system:olaf-core/competencies/
```

Common packs include:
- `pdf-analysis`
- `onboard`
- `researcher`
- `straf`
- `process-documentation`
- `product-owner`
- `security-officer`

### Step 2: Invoke the Competency

Use the OLAF command:
```
/olaf-merge-competency-pack-to-main
```

Or use natural language:
```
Can you help me merge the onboard competency pack to main?
```

### Step 3: Provide Required Information

The agent will ask for:

**1. Competency Pack Name**
```
Which competency pack? 
→ onboard
```

**2. Target Collection(s)**
```
Add to which collection(s)?
→ all
```

Optionally specify multiple:
```
→ all, developer, business-analyst
```

**3. Branch Name** (agent will suggest, you can confirm/modify)
```
Branch name: feat/add-onboard-pack
→ [confirm or provide alternative]
```

### Step 4: Review Execution Plan

The agent will show:
```markdown
## Execution Plan:
1. Checkout main and pull latest
2. Create branch: feat/add-onboard-pack
3. Cherry-pick: olaf-core/competencies/onboard/
4. Update collections.json (add to: all)
5. Regenerate index
6. Commit and push
7. Generate PR URL

Proceed? [yes/no]
```

### Step 5: Monitor Execution

Watch the agent execute each step:

```
✅ Switched to main branch
✅ Created branch feat/add-onboard-pack
✅ Cherry-picked olaf-core/competencies/onboard/
✅ Updated competency-collections.json
✅ Regenerated index (78 entry points → 105 entry points)
✅ Synced 250 command files
✅ Committed changes
✅ Pushed to origin
```

### Step 6: Review the Summary

```markdown
## Merge Summary

**Pack**: onboard
**Branch**: feat/add-onboard-pack
**Collections**: all

### Changes:
- ✅ olaf-core/competencies/onboard/ (27 prompts, 6 tools, 10 workflows)
- ✅ competency-collections.json (+1 entry)
- ✅ query-competency-index.md (+27 entry points)
- ✅ .github/prompts/ (+27 files)
- ✅ .windsurf/workflows/ (+27 files)

### Statistics:
- Total Entry Points: 105 (was 78)
- Total Competencies: 13 (was 12)
- Files Changed: 82

### Next Steps:
1. Open PR: https://github.com/Amadeus-xDLC/genai.olaf/compare/main...feat/add-onboard-pack?expand=1
2. Review changes in GitHub
3. Request reviews from team
4. Merge after approval
5. Delete branch after merge
```

### Step 7: Create and Review PR

Click the provided URL. You'll see:
- All files changed
- Diff viewer
- Commit message
- Option to create PR

Review the PR to ensure:
- ✅ Only the intended competency pack is included
- ✅ Collections.json is correctly updated
- ✅ Index regeneration looks correct
- ✅ No unexpected files are modified

### Step 8: Merge the PR

Once approved:
1. Click "Merge pull request"
2. Confirm merge
3. Delete the integration branch
4. Pull latest main locally

## Common Scenarios

### Scenario 1: Merge Single Pack to "all" Collection

**Goal**: Add `pdf-analysis` to main in the "all" collection

```
You: /olaf-merge-competency-pack-to-main

Agent: Which pack?
You: pdf-analysis

Agent: Add to which collections?
You: all

[Agent executes...]

Agent: ✅ PR ready: https://github.com/...
```

### Scenario 2: Merge Pack to Multiple Collections

**Goal**: Add `researcher` to both "all" and "business-analyst"

```
You: merge researcher competency to main, add it to all and business-analyst collections

[Agent confirms and executes...]
```

### Scenario 3: Handle Pack Already Exists

If the pack already exists on main:

```
Agent: ⚠️ Warning: olaf-core/competencies/straf/ already exists on main
Agent: Options:
  1. Skip (pack already merged)
  2. Update (overwrite with feature branch version)
  3. Cancel

You: 1

Agent: Skipping. No changes needed.
```

### Scenario 4: Validate Before Merge

**Goal**: Check pack compliance before merging

```
You: validate the onboard competency pack before merging

Agent: [Runs validation on feature branch]
Agent: ✅ Validation passed. Ready to merge.

You: proceed with merge

[Agent executes merge workflow...]
```

## Troubleshooting

### Issue: Pack Not Found

```
Error: competency pack 'xyz' not found on feature/olaf-feature-system
```

**Solution**: List available packs:
```bash
git ls-tree -d --name-only feature/olaf-feature-system:olaf-core/competencies/
```

### Issue: Reindex Fails

```
Error: Failed to regenerate index
```

**Solution**: 
1. Check Python environment is activated
2. Verify `select_collection.py` exists
3. Check collections.json for syntax errors
4. Manually run: `python .\olaf-core\competencies\prompt-engineer\scripts\select_collection.py --collection all`

### Issue: Merge Conflicts

```
Error: Cherry-pick resulted in conflicts
```

**Solution**:
1. Resolve conflicts manually
2. Use `git add <resolved-files>`
3. Continue with `git commit`
4. Agent will resume from next step

### Issue: Branch Already Exists

```
Error: Branch feat/add-pack-name already exists
```

**Solution**:
1. Delete old branch: `git branch -D feat/add-pack-name`
2. Or use different branch name

## Best Practices

1. ✅ **One Pack Per PR**: Merge one competency at a time for clean reviews
2. ✅ **Validate First**: Run validation on feature branch before merging
3. ✅ **Review Collections**: Ensure pack is added to appropriate collections
4. ✅ **Test Locally**: If possible, test commands after merge
5. ✅ **Clean Up**: Delete integration branches after merge
6. ✅ **Document**: Update README.md if adding major capabilities

## Advanced Usage

### Custom Branch Names

```
You: merge pdf-analysis but use branch name fix/integrate-pdf-tools
```

### Selective Collection Updates

```
You: add researcher to main but only in the business-analyst collection, not all
```

### Dry Run Mode

```
You: show me what would happen if I merged straf to main, but don't actually do it
```

## Related Resources

- Competency Pack Validation: `/olaf-validate-olaf-artifacts`
- Git Workflows: Git-assistant competencies
- Index Regeneration: `select_collection.py` documentation
- PR Review: GitHub PR review process

## Expected Duration

- Simple pack (5-10 prompts): ~2 minutes
- Medium pack (20-30 prompts): ~3-5 minutes
- Large pack (50+ prompts): ~5-10 minutes

Most time is spent regenerating the index and syncing command files.

## Success Criteria

✅ Integration branch created from main
✅ Competency pack cherry-picked successfully
✅ Collections.json updated correctly
✅ Index regenerated without errors
✅ Command files synced
✅ Clean commit with descriptive message
✅ Branch pushed to remote
✅ PR URL provided and functional
✅ PR shows only intended changes
✅ No merge conflicts or errors

---

**Next**: After creating the PR, proceed with code review and merge approval process.
