# Git Setup — Migration Branching

## Goal
Create migration branch and tags for tracking progress and enabling rollback points.

## Preferred Approach (Automated)
1. **Create Migration Branch**:
   ```bash
   # Create branch if specified
   if [ -n "<branch-name>" ]; then
     git checkout -b <branch-name>
   fi
   ```

2. **Create Migration Tag**:
   ```bash
   # Create tag if specified  
   if [ -n "<tag-name>" ]; then
     git tag -a <tag-name> -m "<intention from action>"
   fi
   ```

3. **Validation**:
   ```bash
   # Verify clean working directory
   git status --porcelain
   
   # Confirm branch/tag creation
   git log --oneline --decorate --graph -n 5
   ```

## Fallback Approach (Manual)
If branch/tag already exists:
1. Check if they point to intended commit: `git show <branch-name>` / `git show <tag-name>`
2. If correct, proceed with existing branch/tag
3. If incorrect, delete and recreate: `git branch -D <branch-name>` / `git tag -d <tag-name>`

## Verification Commands
```bash
# Verify clean working directory
git status --porcelain | wc -l  # Should be 0

# Confirm branch exists and is active
git branch --show-current

# Confirm tag exists  
git tag -l "<tag-name>"

# Show recent commits with decorations
git log --oneline --decorate --graph -n 5
```

## Issue Collection
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `git-branch-tag-<YYYYMMDD-HHmm>.json`
- **Categories**: branch-creation, tag-creation, working-directory-dirty
- **Common Remediation Keys**:
  - `git-branch-exists`
  - `git-tag-exists` 
  - `git-working-directory-dirty`

## Success Criteria
- ✅ Migration branch created (if specified) and active
- ✅ Migration tag created (if specified) at current commit
- ✅ Working directory clean: `git status --porcelain` returns empty
- ✅ Branch/tag visible in git log output

## Commit Message Convention
All migration commits follow Conventional Commits:
```
<type>(<scope>): <description> (<phase.task>)
```

**Types**: feat, fix, docs, chore, test, refactor, build  
**Scopes**: java, spring-boot, jakarta, junit, deps, ci, toolkit  
**Examples**:
- `feat(java): upgrade to JDK 17 (1.4)`
- `refactor(jakarta): migrate javax to jakarta packages (2.3)`