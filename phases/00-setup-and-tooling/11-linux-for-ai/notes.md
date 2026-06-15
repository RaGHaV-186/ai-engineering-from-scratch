# Phase 00, Lesson 11 — Linux for AI

## Filesystem
- Everything lives under `/` (root) — no drive letters
- Your home is `~` = `/home/raghav` (Linux) or `/Users/raghav` (macOS)

## Permissions
- `ls -la` shows `-rwxr-xr-x` — type, owner, group, others
- `r=4, w=2, x=1` — add them up for numeric chmod
- `chmod +x script.sh` — make executable
- `chmod 644 file` — standard file (rw-r--r--)
- `chmod 755 script.sh` — executable (rwxr-xr-x)

## Essential commands
- `pwd` — where am I
- `ls -la` — list with details and hidden files
- `cat / head / tail` — read files
- `tail -f log.txt` — follow a log in real time
- `grep -r "term" . --exclude-dir=venv` — search inside files
- `find . -name "*.pt" -size +1G` — find files by name/size

## Disk space
- `df -h` — free space per drive
- `du -sh folder/` — size of a folder
- `du -sh ~/* | sort -hr | head -10` — biggest items in home

## Processes
- `ps aux | grep python` — find running Python processes
- `kill PID` — stop a process
- `kill -9 PID` — force kill

## Users and sudo
- `whoami` — current user
- `sudo command` — run as root for one command only

## apt vs brew (macOS→Linux)
- `brew install x` → `sudo apt install -y x`
- Always run `sudo apt update` first

## Completed: 2026-06-15
