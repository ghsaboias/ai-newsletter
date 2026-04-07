#!/bin/bash
#
# Run a pi agent interactively and signal tmux when the output file appears.
#
# Usage: run-agent.sh <output-file> <signal-name> pi [pi args...]
#
# Runs pi in the foreground (interactive TUI visible). Polls for the output
# file in the background. When it appears, signals tmux wait-for.
# The pane stays open so you can inspect the results.
#

set -euo pipefail

OUTFILE="$1"
SIGNAL="$2"
shift 2

# Poll for output file in background — signal when it appears
(
  while true; do
    if [[ -f "$OUTFILE" ]]; then
      sleep 2
      tmux wait-for -S "$SIGNAL"
      break
    fi
    sleep 2
  done
) &
POLL_PID=$!

# Run pi in foreground (gets the TTY, user sees everything)
"$@" || true

# If pi exits before the file appeared (error/manual exit), clean up and signal
kill $POLL_PID 2>/dev/null || true
tmux wait-for -S "$SIGNAL" 2>/dev/null || true
