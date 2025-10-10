# Git Setup — Migration Branching

## Preferred approach
1. Create baseline tag and backup branch.
2. Create migration working branch.
3. Push branches/tags if remote is configured.

Commands (Windows PowerShell or bash):
```bash
git tag -a baseline-before-migration -m "Baseline before migration"
git branch backup/pre-migration
git branch migration/java-upgrade
# optional
# git push origin baseline-before-migration
# git push origin backup/pre-migration migration/java-upgrade
```

## Backup option
- If branches exist already, validate they point to the intended commits and proceed.

## Verify
- `git log --oneline --decorate --graph -n 5` shows the tag and branches.
- `git status` is clean before starting tasks.

## Notes
- You may also run the automation in `task-0.1-git-setup/create-branches.ps1|.sh` when available.
