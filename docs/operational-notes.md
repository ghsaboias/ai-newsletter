# Operational & Harness Notes

Environment/harness quirks that bite the newsletter pipeline — headless execution, CLI cred resolution, and Claude Code subagent behavior. These are machine/runtime facts, not editorial voice.

> **Pi note:** this file is the "operational/headless knowledge" bucket. Its contents are candidates for a dedicated section in the Pi's `CLAUDE.md` so they're always in context on the machine that runs the daily cron headless.

---

## Bash background tasks die at turn end (headless sessions)

In `claude --print` mode (e.g. the michael-slack harness), the CLI exits as soon as the model's final turn ends — and **exiting kills still-running Bash background tasks**, so their completion notification never arrives.

- **Subagent (Agent) and Workflow launches DO hold the process open** and re-invoke; Bash `run_in_background` does **not**.
- `nohup`'d jobs survive but are invisible to the harness.

This stalled the 2026-07-03 draft one step from the push: `ingest` (~4 min) was killed by the default 2-min Bash timeout, relaunched via `nohup`, and the session died waiting for a monitor loop's notification.

**Why:** the Bash tool's "you will be notified when it completes" promise only holds while the turn is open (or in interactive mode). Ending the turn to "wait" is fatal in headless.

**How to apply:** run long pipeline steps (e.g. `ingest.sh --execute`) as **one foreground Bash call with explicit `timeout: 600000`** — never `run_in_background`/`nohup`. Fixes shipped 2026-07-03: `newsletter-draft` SKILL.md Step 3.5c note, SLACK_CONTEXT rule + `Agent` watchdog match + an auto-resume net in michael-slack `src/claude.ts` (auto-resumes a session once if it exits with pending bg tasks).

---

## `sstats` runs from any directory

The `sstats` CLI (`~/.local/bin/sstats`) reads Substack creds (`SUBSTACK_SID`, `SUBSTACK_PUB_HOST`) from a `.env.local`. Its `find_env` used to only walk up from `$PWD`, so it failed anywhere without `.env.local` on the path (e.g. `~/ai-newsletter`). The creds actually live in `~/daily-journal-platform/.env.local`.

On 2026-07-02 `find_env` was extended to a 3-tier lookup so `sstats` runs from anywhere:
1. `$SSTATS_ENV` env var (explicit override) if set and the file exists
2. walk up from `$PWD` (a project-local `.env.local` still wins)
3. fallback to `$HOME/daily-journal-platform/.env.local`

So no more need to `cd ~/daily-journal-platform` first. The same `find_env` pattern exists in `pipeline/substack-preview.sh` / `sbq` if they ever need the same fix.

---

## Claude Code supports nested subagents (max 5 levels)

Claude Code supports **nested subagents** as of **v2.1.172 (2026-06-10)** — a subagent spawned via the Agent/Task tool can itself dispatch further subagents. This **postdates the Opus 4.8 training cutoff (Jan 2026)**; the older instinct that "nesting is capped at one level, flatten into the main loop or use a Workflow" is **wrong** for current Claude Code.

Specifics (per `https://code.claude.com/docs/en/sub-agents.md`, updated 2026-07-06):
- **Max depth: 5 levels**, fixed and not configurable. A subagent at depth 5 doesn't receive the Agent tool and can't spawn further.
- Subagents **inherit the Agent tool by default** from the parent, so they can nest unless restricted.
- Restrict with `disallowedTools: Agent` in frontmatter, or a `tools:` allowlist that omits `Agent`. Listing `Agent` in `tools` explicitly grants nesting (any agent-type list in parens is ignored).
- Only the top-level subagent's summary returns to the main conversation; the intermediate fan-out is hidden. Intended for e.g. a reviewer subagent that dispatches a verifier per finding.

Relevant to the subagent-heavy pipeline (`newsletter-draft` / `newsletter-research` spawn `researcher-{ai,hw,world}` etc.) — a cluster researcher could itself fan out within the depth cap instead of flattening everything to the orchestrator.
