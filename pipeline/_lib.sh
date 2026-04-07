#!/bin/bash
#
# Shared utilities for newsletter pipeline scripts
#

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$DIR/.." && pwd)"
DJ_DIR="$HOME/daily-journal-platform"

# --- Pi config ---
PI_CMD="pi"
PI_MODEL="${PIPELINE_MODEL:-anthropic/claude-opus-4-6}"
PI_EXTENSIONS_DIR="$DIR/extensions"
PI_BLOCK_DOMAINS="-e $PI_EXTENSIONS_DIR/block-domains.ts"

# --- Topic loading ---
# Defaults to "ai". Override with --topic <name> in script args.
TOPIC="${PIPELINE_TOPIC:-ai}"
LOOP_DIR="${PIPELINE_OUTPUT:-$DIR/output/$TOPIC}"
TOPIC_DIR="$ROOT_DIR/newsletters/$TOPIC"
TOPIC_PROMPTS_DIR="$TOPIC_DIR/prompts"

# Load topic config if it exists (adds TOPIC_* variables)
if [[ -f "$TOPIC_DIR/config.sh" ]]; then
  source "$TOPIC_DIR/config.sh"
fi

# Set DAY_DIR for per-date output. Call after DATE is set.
init_day_dir() {
  DAY_DIR="$LOOP_DIR/$DATE"
  mkdir -p "$DAY_DIR"
}

# --- Logging ---
LOG_DIR="$DIR/logs/$TOPIC"
mkdir -p "$LOG_DIR"

# Initialize log file for a given date
# Usage: init_log "2026-02-24"
init_log() {
  local date="$1"
  LOG_FILE="$LOG_DIR/$date-$(date +%H%M%S).log"
  echo "  Log: $LOG_FILE"
}

# --- Pi runner ---
# Run pi in print mode with common flags.
# Usage: run_pi [--tools tool1,tool2] [--web] [--no-ext] "prompt"
#   --web       include exa tools + domain blocker (default: no extensions)
#   --no-ext    explicitly disable all extensions
#   --tools     override built-in tools (default: read,write,edit)
run_pi() {
  local tools="read,write,edit"
  local ext_flags="--no-extensions"
  local prompt=""

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --tools)  tools="$2"; shift 2 ;;
      --web)    ext_flags="$PI_BLOCK_DOMAINS"; shift ;;
      --no-ext) ext_flags="--no-extensions"; shift ;;
      *)        prompt="$1"; shift ;;
    esac
  done

  $PI_CMD -p \
    --model "$PI_MODEL" \
    --tools "$tools" \
    $ext_flags \
    "$prompt"
}

# --- Tmux helpers for parallel research ---
# Launch a pi agent in a tmux pane and signal when done.
# Usage: launch_pane "window" "name" "prompt" [extra pi flags...]
# The pane signals "done-$name" when finished.
launch_pane() {
  local window="$1"
  local name="$2"
  local prompt="$3"
  shift 3

  local log="$LOG_DIR/$DATE-research-${name}.log"
  local cmd="$PI_CMD -p --no-session --model $PI_MODEL --tools read,write,bash $PI_BLOCK_DOMAINS $* \"$prompt\" 2>&1 | tee $log; tmux wait-for -S done-$name"

  # First pane reuses the window, subsequent panes split
  if tmux list-panes -t "$window" 2>/dev/null | grep -q .; then
    tmux split-window -t "$window" -v -d "$cmd"
  else
    tmux new-window -n "$window" -d "$cmd"
  fi

  # Even out the layout
  tmux select-layout -t "$window" tiled 2>/dev/null || true
}

# Wait for all named panes to finish.
# Usage: wait_panes name1 name2 name3
wait_panes() {
  for name in "$@"; do
    tmux wait-for "done-$name"
  done
}

# --- Common arg parsing helper ---
# Parse DATE from args (YYYY-MM-DD or "test")
parse_date_arg() {
  for arg in "$@"; do
    case "$arg" in
      20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) echo "$arg"; return ;;
      test) echo "test"; return ;;
    esac
  done
  # Default to today
  date +%Y-%m-%d
}

# Parse --topic from args. Call before parse_date_arg if needed.
parse_topic_arg() {
  local next_is_topic=false
  for arg in "$@"; do
    if [[ "$next_is_topic" == true ]]; then
      echo "$arg"; return
    fi
    [[ "$arg" == "--topic" ]] && next_is_topic=true
  done
  echo "${PIPELINE_TOPIC:-ai}"
}
