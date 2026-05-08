#!/bin/bash
#
# PreToolUse hook: block exa_web_fetch calls to paywall/403 domains.
#
# Receives Claude Code hook payload on stdin:
#   { "tool_name": "mcp__exa__web_fetch_exa", "tool_input": { "urls": [...] } }
#
# Emits a deny decision when any URL hits a blocked domain. Otherwise exits 0
# silently (allow).

set -euo pipefail

BLOCKED='reuters.com bloomberg.com axios.com cnbc.com politico.eu seekingalpha.com businessinsider.com wired.com business-standard.com datacenterdynamics.com etnownews.com archynewsy.com wccftech.com openai.com cybernews.com coindesk.com appleinsider.com aninews.in'

payload="$(cat)"
tool="$(jq -r '.tool_name // ""' <<< "$payload")"

if [[ "$tool" != "mcp__exa__web_fetch_exa" ]]; then
  exit 0
fi

urls="$(jq -r '(.tool_input.urls // []) | .[]' <<< "$payload" 2>/dev/null || true)"
[[ -z "$urls" ]] && exit 0

hits=()
while IFS= read -r url; do
  [[ -z "$url" ]] && continue
  host="$(printf '%s' "$url" | sed -E 's|^https?://||; s|/.*$||; s|^www\.||')"
  for d in $BLOCKED; do
    if [[ "$host" == "$d" ]]; then
      hits+=("$d")
      break
    fi
  done
done <<< "$urls"

if [[ ${#hits[@]} -eq 0 ]]; then
  exit 0
fi

reason="Blocked domains: $(printf '%s\n' "${hits[@]}" | sort -u | paste -sd, -). Use exa_search snippets instead — do not retry these URLs."

jq -nc --arg r "$reason" '{
  hookSpecificOutput: {
    hookEventName: "PreToolUse",
    permissionDecision: "deny",
    permissionDecisionReason: $r
  }
}'
