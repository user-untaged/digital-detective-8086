# Mission 3 - Understand the Operating System

## 1. Task / objective
To explore the operating system, running processes, storage, paths and file permissions, and describe the OS responsibilities.

## 2. Work completed 

### Task 3.1 - Exploring my OS

| Information | What it tells me | My observation |
|---|---|---|
| Operating system | The system software managing my computer | macOS Tahoe 26.4 |
| Current account | Which account is active | Account name is `[redacted]`|
| Available and used storage | How much space is used and available | About 105.89 GB used out of 994.61 GB, available 888.71 GB|
| System activity snapshot | Which apps and background tasks are running | It showed the running apps and background processes like VScode, Slack, Safari and many more.|

### Task 3.2 - Understand processes

- **Process:** A process is a program that is running. 
- **PID:** The PID column shows each process's identification number. The number helps the OS to keep track of each running program. 
- **Examples:** Finder and Brave Browser

### Task 3.3 - Understand paths and permissions 

- I checked the current location in the repository and then moved into the Mission 3 folder. The displayed location changed when I changed between the folders.

- **Absolute path:** Starts at the root of the computer and gives the full location.
    - Example: '/Users/[redacted]/Desktop/digital-detective-8086/mission-03-operating-system/README.md`
- **Relative path:** Starts from the folder I am already in.
    - Example: (from the repository root) `mission-03-operating-system/README.md`

The README file's permissions were `-rwxr--r--`. The owner's permissions are `rwx`, i.e. owner can read, write and execute. The group and others have permission to only read. 

### Task 3.4 - Explain OS responsibilities

| Responsibility | My explanation | Example |
|---|---|---|
| Process management | Keeps track of programs that are running and shares processor time between them | A browser and a text editor can both run at a time |
| Memory management | Gives programs memory while they work and reuses it when they are closed | A browser uses memory to keep a webssite open |
| Device management | Helps programs communicate with the connected hardware | The OS sends a document to a printer to print |
| File management | Organizes files, folders and controls how they are opened or modified | I opened and saved a README.md file |
| User interface / shell | Allows me to control the computer with windows by CLI | The desktop is a graphical interface and terminal is a shell|
| Security and permissions | Controls which accounts can read, change, or execute | The file's permission letters show what it's owner,group and others can do |


## 3. Commands / tools used
- brew --version
- brew list
- pwd

## 4. My understanding
I learnt about chmod permissions, PID, process, what my OS manages, version of it and it's activity monitor. Also I came to know the difference between absolute path and relative path. 

## 5. Difficulties faced
I faced difficulty in finding the version of my macOS. 

## 6. How I resolved them
I was initially searching for it in the terminal rather than directly seeing it in the settings. 

## 7. Evidence / files
- [`mission-03-system/README.md`](mission-03-system/README.md): notes about the observations and permissions.

## 8. Commit details
Commit message: `Document operating system and file management`
Status: Committed and pushed
