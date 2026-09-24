#!/bin/bash
#
# Shared utilities for newsletter pipeline scripts
#

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$DIR/.." && pwd)"
DJ_DIR="$HOME/daily-journal-platform"

# --- Claude config ---
CLAUDE_CMD="claude"
CLAUDE_MODEL="${PIPELINE_MODEL:-claude-opus-4-8}"
CLAUDE_HOOKS_DIR="$DIR/hooks"
CLAUDE_BLOCK_DOMAINS_SETTINGS="$CLAUDE_HOOKS_DIR/block-domains.json"

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

# --- Claude runner ---
# Run claude in print mode with common flags.
# Usage: run_claude [--tools Tool1,Tool2] [--web] "prompt"
#   --tools  allowed tools, PascalCase (default: Read,Write,Edit)
#   --web    enable exa MCP tools + block-domains hook
run_claude() {
  local tools="Read,Write,Edit"
  local extra=()
  local prompt=""

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --tools) tools="$2"; shift 2 ;;
      --web)
        tools="Read,Write,Bash,mcp__exa__web_search_exa,mcp__exa__web_fetch_exa"
        [[ -f "$CLAUDE_BLOCK_DOMAINS_SETTINGS" ]] && extra+=(--settings "$CLAUDE_BLOCK_DOMAINS_SETTINGS")
        shift ;;
      *) prompt="$1"; shift ;;
    esac
  done

  $CLAUDE_CMD -p \
    --model "$CLAUDE_MODEL" \
    --allowedTools "$tools" \
    ${extra[@]+"${extra[@]}"} \
    <<< "$prompt"
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
