# Git workflow cheatsheet

## Daily workflow
git status
git add .
git diff --staged
git commit -m "scope: what you did"
git push

## Branch workflow
git checkout -b lesson/phase-XX-YY
git push -u origin lesson/phase-XX-YY
git checkout main
git merge lesson/phase-XX-YY
git push

## Undo toolkit
git restore <file>           # discard working dir change
git restore --staged <file>  # unstage (keep the edit)
git log --oneline -10        # see last 10 commits
