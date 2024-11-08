# Git tutorial

Git is a version control system that helps you track and manage your project.

## local git commands

1. `git init`

Initialises a new git repository on your local directory. You do this only once at the beginning of the project.

2. `git add **file_name**`

Starts tracking the specified file name. Use `git add .` to track all the untracked files present.

3. `git restore **file_name**`

Undo the changes made to a tracked file

4. `git rm --cached **file_name**`

Undo tracking of a file

5. `git commit -m "commit message"`

Saves/commits the files being tracked. You should always add a meaningful and short commit message.

6. `git log` or `git log --oneline`

View the commit logs. `git log` will show a detailed output with the full commit hash. `git log --oneline` will show only a one line summary

7. `git commit -am "commit message"`

Combine both `git add` and `git commit` into one command for a modified file.

8. `git status`

Check the current status of the git repository. You should do this after every change or command to be sure.