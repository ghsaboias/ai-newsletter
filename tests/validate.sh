#!/bin/bash
#
# Validate test pipeline output + verify specific changes took effect.
#
# Usage: ./tests/validate.sh 2026-03-30
#        ./tests/validate.sh 2026-03-30 --verbose
#

set -euo pipefail

TESTS_DIR="$(cd "$(dirname "$0")" && pwd)"
DATE="${1:?Usage: validate.sh YYYY-MM-DD}"
VERBOSE="${2:-}"
TEST_OUTPUT="$TESTS_DIR/output/$DATE"
LOG_DIR="$TESTS_DIR/../pipeline/logs"

PASS=0
FAIL=0
WARN=0

pass() { echo "  ✅ $1"; PASS=$((PASS + 1)); }
fail() { echo "  ❌ $1"; FAIL=$((FAIL + 1)); }
warn() { echo "  ⚠️  $1"; WARN=$((WARN + 1)); }

echo ""
echo "=== Validate: $DATE ==="
echo "  Output: $TEST_OUTPUT"
echo ""

# ============================================================
# 1. Output file validity
# ============================================================
echo "--- Output Files ---"

# Research
if [[ -f "$TEST_OUTPUT/research.json" ]]; then
  if jq empty "$TEST_OUTPUT/research.json" 2>/dev/null; then
    STORIES=$(jq '.story_count // (.stories | length)' "$TEST_OUTPUT/research.json")
    SOURCES=$(jq '.source_count // 0' "$TEST_OUTPUT/research.json")
    pass "research.json: valid JSON ($STORIES stories, $SOURCES sources)"
  else
    fail "research.json: invalid JSON"
  fi
else
  fail "research.json: missing"
fi

# Article
if [[ -f "$TEST_OUTPUT/pt.md" ]]; then
  WORDS=$(wc -w < "$TEST_OUTPUT/pt.md" | tr -d ' ')
  LINKS=$(grep -oE 'https?://[^)]+' "$TEST_OUTPUT/pt.md" | sort -u | wc -l | tr -d ' ')
  if head -1 "$TEST_OUTPUT/pt.md" | grep -q "^---"; then
    pass "pt.md: valid ($WORDS words, $LINKS unique links)"
  else
    warn "pt.md: missing frontmatter ($WORDS words)"
  fi
else
  fail "pt.md: missing"
fi

# Repetition check
if [[ -f "$TEST_OUTPUT/repetition.json" ]]; then
  if jq empty "$TEST_OUTPUT/repetition.json" 2>/dev/null; then
    ISSUES=$(jq '.issues | length' "$TEST_OUTPUT/repetition.json" 2>/dev/null || echo "?")
    pass "repetition.json: valid JSON ($ISSUES issues)"
  else
    fail "repetition.json: invalid JSON"
  fi
else
  warn "repetition.json: missing (ok if no previous editions)"
fi

# Audit
if [[ -f "$TEST_OUTPUT/audit.json" ]]; then
  if jq empty "$TEST_OUTPUT/audit.json" 2>/dev/null; then
    ISSUES=$(jq '.issues | length' "$TEST_OUTPUT/audit.json" 2>/dev/null || echo "?")
    pass "audit.json: valid JSON ($ISSUES issues)"
  else
    fail "audit.json: invalid JSON"
  fi
else
  fail "audit.json: missing"
fi

echo ""

# ============================================================
# 2. Change verification (log analysis)
# ============================================================
echo "--- Change Verification ---"

# Find research log(s) for this date
RESEARCH_LOGS=$(find "$LOG_DIR" -name "$DATE-research-*.log" -newer "$TEST_OUTPUT" 2>/dev/null || true)
if [[ -z "$RESEARCH_LOGS" ]]; then
  RESEARCH_LOGS=$(find "$LOG_DIR" -name "$DATE-research-*.log" 2>/dev/null | tail -3)
fi

if [[ -z "$RESEARCH_LOGS" ]]; then
  warn "No research logs found — can't verify changes"
else
  # --- Check: --model (should see sonnet for research) ---
  # The model appears in the claude CLI invocation or in stream-json metadata
  # We check for result events that show model info
  if grep -ql "sonnet" $RESEARCH_LOGS 2>/dev/null; then
    pass "--model sonnet: found in research logs"
  else
    warn "--model sonnet: not detected in research logs (may not be implemented yet)"
  fi

  # --- Check: tool discovery waste ---
  TOOL_SEARCH_COUNT=0
  for log in $RESEARCH_LOGS; do
    count=$(grep -c '"ToolSearch"\|"TodoWrite"\|"Agent"\|"TodoRead"' "$log" 2>/dev/null || echo 0)
    TOOL_SEARCH_COUNT=$((TOOL_SEARCH_COUNT + count))
  done
  if [[ $TOOL_SEARCH_COUNT -eq 0 ]]; then
    pass "No tool discovery waste (ToolSearch/TodoWrite/Agent: 0)"
  else
    fail "Tool discovery waste detected: $TOOL_SEARCH_COUNT calls"
  fi

  # --- Check: crawling_exa usage ---
  CRAWL_COUNT=0
  for log in $RESEARCH_LOGS; do
    count=$(grep -c 'crawling_exa' "$log" 2>/dev/null || echo 0)
    CRAWL_COUNT=$((CRAWL_COUNT + count))
  done
  if [[ $CRAWL_COUNT -gt 0 ]]; then
    pass "crawling_exa: used $CRAWL_COUNT time(s)"
  else
    warn "crawling_exa: not used (may not have encountered paywalled URLs)"
  fi

  # --- Check: domain blocklist (WebFetch on blocked domains) ---
  BLOCKED_DOMAINS="reuters.com bloomberg.com axios.com cnbc.com politico.eu seekingalpha.com businessinsider.com wired.com business-standard.com datacenterdynamics.com"
  BLOCKED_FETCHES=0
  for log in $RESEARCH_LOGS; do
    for domain in $BLOCKED_DOMAINS; do
      count=$(grep '"WebFetch"' "$log" 2>/dev/null | grep -c "$domain" 2>/dev/null || true)
      count=${count:-0}
      if [[ "$count" -gt 0 ]]; then
        fail "WebFetch called on blocked domain: $domain ($count times)"
        BLOCKED_FETCHES=$((BLOCKED_FETCHES + count))
      fi
    done
  done
  if [[ $BLOCKED_FETCHES -eq 0 ]]; then
    pass "Domain blocklist: no WebFetch on blocked domains"
  fi

  # --- Check: thinking tokens (effort level) ---
  THINKING_CHARS=0
  for log in $RESEARCH_LOGS; do
    chars=$(grep -o '"thinking"' "$log" 2>/dev/null | wc -l | tr -d ' ')
    THINKING_CHARS=$((THINKING_CHARS + chars))
  done
  if [[ $THINKING_CHARS -lt 5 ]]; then
    pass "--effort low: minimal thinking blocks ($THINKING_CHARS)"
  else
    warn "--effort low: $THINKING_CHARS thinking blocks detected (expected fewer with low effort)"
  fi

  # --- Verbose: show tool usage summary ---
  if [[ "$VERBOSE" == "--verbose" ]]; then
    echo ""
    echo "  --- Tool usage (research logs) ---"
    for log in $RESEARCH_LOGS; do
      name=$(basename "$log" .log | sed "s/$DATE-//")
      echo "  [$name]"
      grep -oE '"(WebFetch|WebSearch|mcp__exa__web_search_exa|mcp__exa__crawling_exa|Read|Write|Bash)"' "$log" 2>/dev/null \
        | sort | uniq -c | sort -rn | sed 's/^/    /' || echo "    (no tool calls found)"
    done
  fi
fi

# --- Check: session persistence ---
# Look for new JSONL files created during the test run
RECENT_JSONL=$(find ~/.claude/projects/ -name "*.jsonl" -newer "$TEST_OUTPUT/research.json" 2>/dev/null | head -5)
if [[ -z "$RECENT_JSONL" ]]; then
  pass "--no-session-persistence: no new JSONL files"
else
  JSONL_COUNT=$(echo "$RECENT_JSONL" | wc -l | tr -d ' ')
  warn "--no-session-persistence: $JSONL_COUNT new JSONL file(s) found (may not be implemented yet)"
  if [[ "$VERBOSE" == "--verbose" ]]; then
    echo "$RECENT_JSONL" | sed 's/^/    /'
  fi
fi

echo ""

# ============================================================
# 3. Mini mode checks
# ============================================================
if [[ -f "$TEST_OUTPUT/research.json" ]]; then
  STORY_COUNT=$(jq '.stories | length' "$TEST_OUTPUT/research.json" 2>/dev/null || echo 0)
  # Check only 1 cluster ran (no research-hw.json or research-world.json)
  CLUSTER_COUNT=0
  for c in ai hw world seeds; do
    [[ -f "$TEST_OUTPUT/research-${c}.json" ]] && ((CLUSTER_COUNT++))
  done

  echo "--- Mini Mode ---"
  if [[ $CLUSTER_COUNT -le 1 ]]; then
    pass "Single cluster: $CLUSTER_COUNT cluster file(s)"
  else
    warn "Multiple clusters ran: $CLUSTER_COUNT (expected 1 in mini mode)"
  fi

  if [[ $STORY_COUNT -le 5 ]]; then
    pass "Story cap: $STORY_COUNT stories (≤5)"
  else
    warn "Story cap: $STORY_COUNT stories (expected ≤5 in mini mode)"
  fi
fi

# ============================================================
# Summary
# ============================================================
echo ""
echo "=== Results: $PASS passed, $FAIL failed, $WARN warnings ==="

if [[ $FAIL -gt 0 ]]; then
  exit 1
fi
