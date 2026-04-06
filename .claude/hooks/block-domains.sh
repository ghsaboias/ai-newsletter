#!/bin/bash
# Block WebFetch calls to domains that always return 403

INPUT=$(cat)
URL=$(echo "$INPUT" | jq -r '.tool_input.url')
DOMAIN=$(echo "$URL" | sed -E 's|https?://(www\.)?([^/]+).*|\2|')

BLOCKED="reuters.com bloomberg.com axios.com cnbc.com politico.eu seekingalpha.com businessinsider.com wired.com business-standard.com datacenterdynamics.com etnownews.com archynewsy.com wccftech.com openai.com cybernews.com coindesk.com appleinsider.com aninews.in"

for b in $BLOCKED; do
  if [[ "$DOMAIN" == "$b" ]]; then
    jq -n --arg d "$DOMAIN" '{
      hookSpecificOutput: {
        hookEventName: "PreToolUse",
        permissionDecision: "deny",
        permissionDecisionReason: ("Blocked domain: " + $d + ". Use search snippets instead — do not retry.")
      }
    }'
    exit 0
  fi
done

exit 0
