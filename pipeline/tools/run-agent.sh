#!/bin/bash
#
# Run an agent in the foreground and signal tmux when the output file appears.
#
# Usage: run-agent.sh <output-file> <signal-name> <command> [args...]
#
# Polls for the output file in the background; signals tmux wait-for when it
# appears. Stdin is inherited, so callers can redirect a prompt file via
# `< prompt.md` on the outer invocation. The pane stays open so you can
# inspect the results.
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

# Run the agent in foreground (inherits TTY/stdin)
"$@" || true

# If the agent exits before the file appeared (error/manual exit), clean up and signal
kill $POLL_PID 2>/dev/null || true
tmux wait-for -S "$SIGNAL" 2>/dev/null || true
