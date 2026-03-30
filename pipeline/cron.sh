#!/bin/bash
# Runs draft.sh then commits+pushes output regardless of exit code
cd ~/ai-newsletter
export PATH="$HOME/.local/bin:$PATH"

DATE=$(date +%Y-%m-%d)
LOG=~/logs/ai-newsletter.log

echo "=== $DATE $(date +%H:%M:%S) ===" >> "$LOG"
pipeline/draft.sh "$DATE" >> "$LOG" 2>&1
EXIT=$?

echo "draft.sh exited: $EXIT" >> "$LOG"

git add pipeline/output/ai/"$DATE"/ >> "$LOG" 2>&1
git diff --cached --quiet || git commit -m "Auto: draft $DATE (exit $EXIT)" --no-gpg-sign >> "$LOG" 2>&1 && git push >> "$LOG" 2>&1

echo "=== done $(date +%H:%M:%S) ===" >> "$LOG"
