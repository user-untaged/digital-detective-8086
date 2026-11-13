# Mission 6 - Git and GitHub

## 1. Task / objective
Understand version control, stage and commit changes, create a branch, open a pull request and explain the collaboration workflow

## 2. Work completed

### Task 6.1 - Understand the basic git workflow

| Git operation | What it does |
|---|---|
| Check repository status | `git status` shows which files have been changed and whether they are staged or not |
| Stage selected changes | `git add README.md` selects the changes to include in the next commit |
| Create a commit | `git commit -m "meaningful msg"` saves the staged changes in the local Git history |
| View commit history | `git log --oneline` shows recent commits (modifications) |

### Task 6.2 - Create and use a branch

I used the `update-about` branch to add a “My Learning” section to the root README.md folder. Pulled Request #1 and asked to add that change to `main`. It was reviewed and merged.

### Task 6.3 - Create a pull request

### Task 6.4 - Build your git command glossary

| Operation | Command | What it means |
|---|---|---|
| Initialize a repository | `git init` | Start tracking a project with Git |
| Check status | `git status` | See changed, staged, and untracked files |
| Stage changes | `git add .` | Choose a file's changes for the next commit |
| Commit changes | `git commit -m "text"` | Save staged changes in the local Git history |
| View history | `git log --oneline` | See earlier changes (history) |
| Create or list branches | `git branch name` / `git branch` | Create a branch or list the branches |
| Switch branches | `git switch name` | Switch to another branch |
| Publish changes | `git push -u origin name` | Send a branch and its commits to GitHub |
| Retrieve remote changes | `git pull origin main` | Get changes from the remote main branch and bring them into the current branch |

## 3. Commands / tools used
- git status
- git add . 
- git commit -m "text"
- git log --oneline
- git push

## 4. My understanding
How Git keeps a history of my project (process). I came to know about the pull request. GitHub stores the remote copy so that I can share changes with others.

## 5. Difficulties faced
Creating a pull request.

## 6. How I resolved them
I followed the steps in order with the help of my friend. 

## 7. Evidence / files
- Root [`README.md`](digital-detective-8086/README.md): contains the “My Learning” section

## 8. Commit details
Commit message: `Complete Git and GitHub collaboration mission`
Status: Committed and pushed