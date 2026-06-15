# Phase 00, Lesson 10 — Terminal & Shell

## Key concepts

### Processes
- Every terminal tab is a separate zsh process with a unique PID
- `echo $$` shows your current process ID
- Processes have isolated memory — variables set in one tab don't exist in another

### Redirection
- `>` saves output to a file (overwrites)
- `>>` appends to a file
- `2>` saves errors to a file
- `2>&1` sends errors to the same place as normal output

### Pipes
- `|` sends output of one command as input to the next
- Example: `cat train.log | grep "loss" | wc -l`

### Background processes
- `command &` runs in background, dies if terminal closes
- `nohup command &` runs in background, survives terminal close
- Check with `jobs`, kill with `kill %1`

### tmux
- `tmux new -s training` creates a persistent session
- `Ctrl+B %` splits vertically, `Ctrl+B "` splits horizontally
- `Ctrl+B d` detaches (session keeps running)
- `tmux attach -t training` reattaches
- `tmux ls` lists all sessions

### htop
- Shows all running processes, CPU and memory usage live
- Press `q` to exit

## Completed: 2026-06-15
