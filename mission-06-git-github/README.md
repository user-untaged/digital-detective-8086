# Mission 6 - Git and GitHub

## 1. Task / objective
Understand version contro, stage and commit changes, create a branch, open a pull request and explain the collaboration workflow.

## 2. Work completed

### Task 6.1 - Understand the basic Git workflow

| Git operation | What it does |
|---|---|
| Check repository status | `git status` shows which files have been changed and whether they are staged or not |
| Stage selected changes | `git add name` selects the changes to include in the next commit |
| Create a commit | `git commit -m "msg"` saves the staged changes in the local Git |
| View commit history | `git log --oneline` shows recent changes (history) |

- Staging: Chooses the changes for the next saved version 
- Committing: Records those chosen changes in the repository history

### Task 6.2 - Create and use a branch
I used the `update-about` branch to add a “My Learning” section to the root README.md folder. Pull Request #1 asked to add that change to `main`; it was reviewed and merged.

- Pull Request: [#1 - Add project overview and mission links](https://github.com/user-untaged/digital-detective-8086/pull/1)
- Status: Merged

### Task 6.3 - Create a pull request

- Branch: Gives me a separate place to work on the changes
- Pull Request: Show me those changes and ask for review before they are merged into the main branch

### Task 6.4 - Build your git command glossay

| Operation | Command | What it means |
|---|---|---|
| Initialize a repository | `git init` | Initializing a project with Git |
| Check status | `git status` | See changed, staged, and untracked files |
| Stage changes | `git add README.md` | Choose a file's changes for the next commit |
| Commit changes | `git commit -m "message"` | Save staged changes in the local Git with a short description |
| View history | `git log --oneline` | See earlier changes (history) |
| Create or list branches | `git branch name` / `git branch` | Create a branch or list the branches |
| Switch branches | `git switch name` | Move to another branch |
| Publish changes | `git push -u origin name` | Send a branch and its commits to GitHub |
| Retrieve remote changes | `git pull origin main` | Get changes from the remote `main` branch and bring them into the current branch |

### Commands / tools used

- `git status` - checked which files had changes
- `git add` - staged selected changes
- `git commit` - recorded changes in history
- `git log --oneline` - viewed the commit history
- `git branch -a` - viewed local and remote branches
- `git push` - published commits to GitHub

## 4. My understanding
- Git: Keeps a history of my project. I stage the changes I want, then commit them to save the version.
- Branch: Keeps work separate and a pull request lets people review it before it is merged. GitHub stores the remote copy so I can share changes with others.

## 5. Difficulties faced
I faced difficulty in Pull Requests.

## 6. How I resolved them
I followed the steps in order notes down in my notes and with the help of my friend, I did it.

## 7. Evidence / files
- Root [`README.md`](digital-detective-8086/README.md): contains the “My Learning” section
- [Pull Request #1](https://github.com/user-untaged/digital-detective-8086/pull/1): merged branch and reviewed record

## 8. Commit details
Commit message: `Complete Git and GitHub collaboration mission`
Status: Committed and pushed