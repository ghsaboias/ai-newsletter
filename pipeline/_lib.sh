#!/bin/bash
#
# Shared utilities for newsletter pipeline scripts
#

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOOP_DIR="$DIR/output"
DJ_DIR="$HOME/daily-journal-platform"

# --- Logging ---
LOG_DIR="$DIR/logs"
mkdir -p "$LOG_DIR"

# Initialize log file for a given date
# Usage: init_log "2026-02-24"
init_log() {
  local date="$1"
  LOG_FILE="$LOG_DIR/$date-$(date +%H%M%S).log"
  echo "  Log: $LOG_FILE"
}

# --- Progress filter: parse stream-json and show tool activity ---
# Tees full output to log file, shows tool summaries to terminal
show_progress() {
  local step_name="$1"
  local tool_count=0
  local last_tool=""

  while IFS= read -r line; do
    # Log every line
    echo "$line" >> "$LOG_FILE"

    # Try to extract tool_use events (Claude starting a tool call)
    tool_name=$(echo "$line" | jq -r '
      if .type == "assistant" then
        (.message.content[]? | select(.type == "tool_use") | .name) // empty
      else
        empty
      end
    ' 2>/dev/null || true)

    # Log errors and result messages
    error_msg=$(echo "$line" | jq -r '
      if .type == "error" then .error.message // .error // "unknown error"
      elif .type == "result" then "EXIT: cost=\(.cost_usd // "?") duration=\(.duration_ms // "?")ms turns=\(.num_turns // "?")"
      else empty
      end
    ' 2>/dev/null || true)

    if [[ -n "$error_msg" ]]; then
      echo "      [$step_name] $error_msg"
    fi

    if [[ -n "$tool_name" && "$tool_name" != "$last_tool" ]]; then
      tool_count=$((tool_count + 1))
      last_tool="$tool_name"

      # Format tool name for display
      case "$tool_name" in
        Write)     display="Writing file" ;;
        Read)      display="Reading file" ;;
        Edit)      display="Editing file" ;;
        WebFetch)  display="Fetching URL" ;;
        WebSearch) display="Searching web" ;;
        mcp__exa__web_search_exa) display="Searching (Exa)" ;;
        *)         display="$tool_name" ;;
      esac

      echo "      [$step_name] #$tool_count $display ($(date '+%H:%M:%S'))"
    fi
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
