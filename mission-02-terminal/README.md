# Mission 2 - Become Comfortable with the Terminal

## 1. Task / objective
Use CLI to inspect folders, create and manage practice files, understand options and pipes, adn explain package managers.

## 2. Work completed
I checked my current location and directory contents, created practice files, added a second line without replacing the first, copied and renamed a backup and displayed the file. I compared normal and detailed listings, included hidden files, and sent a listing through a pipe. I also checked Homebrew and viewed its package lists without installing or removing anything.

## 3. Commands / tools used 

### Task 2.1

| Operation	| Command | What it does|
|---|---|---|
|Current directory display | pwd | Shows the full path of the folder I am currently in |
| Directory listing	| ls | Lists files and folders in the current location |
| Detailed listing | ls -l | Shows detailed information about files and folders | 
| Change directory | cd .. | Moves to the parent folder |
| Create directory | mkdir 	| Creates a new folder |
| Create empty file | touch | Creates an empty text file |
| Copy file | cp | Creates a copy of file |
| Move/rename file | mv | Renames the file |
| Display file contents | cat | Displays the contents of file |

### Task 2.2 

- **What is the difference between replacing a file's contents and adding text to the end?**
    - Replacing a file's contents syntax: echo "text" > file.txt
    - Adding text at end syntax: echo "text" >> file.txt

- **What is the difference between copying and moving a file?** 
    - Copying a file: cp filename1.txt filename2.txt (it copies content in filename1 to filename2)
    - Moving a file: mv filename1.txt filename2.txt (it moves filename1 to filename2)

- **What information does the current-directory display provide?** 
    - PWD provide us the information about the path of the folder we are currently in.

- **Why is a directory listing useful?** 
    - Directory-listing is useful operation to list all the files and folders in the current directory.

### Task 2.3

- ls : Display a normal directory listing
- ls -l : display with detailed information
- ls -a : display hidden files
- ls -h : file sizes are displayed in a human-readable format (KB or MB)
- ls -lah : include hidden files and readable file sizes

- ls -lah | head : output of a detailed listing to a command that displays only the first few lines.
- **Pipe symbol (|) :** It sends the left command's output as input to the command on the right. 

### Task 2.4

- Homebrew 7.0.13 
- ca-certificates, fortune, lolcat, ruby, telnet, cowsay, libyaml, openssl@3, sl, tree
- A package manager is a tool that helps users manage software. It makes it easier to install, update, and remove programs through Terminal. In macOS, Homebrew is a commonly used package manager. 

## 4. My understanding
I understood about different CLI commands, what a package manager is and importance of pipe symbol.

## 5. Difficulties faced
At first, I was unsure about ls -h, ls -lah | head and ls -lah, these commands and also don't know that Homebrew is also called as brew. 

## 6. How I resolved them
I took the help of my chatgpt to learn about the unknown commands.

## 7. Evidence / files
- `terminal-practice/file.txt` and `terminal-practice/backup.txt`: the two-line file and it's backup
- [`mission-02-terminal/README.md`](mission-02-terminal/README.md): notes about the command results

## 8. Commit details
Commit message: `Complete Terminal and file management mission`
Status: Committed and pushed