#!/usr/bin/env python3
"""Extract a structured pipeline trace from a Claude Code daily-run session.

Reads the parent session JSONL + its subagents/ transcripts and emits one
trace.json describing the run: skills invoked, agents launched (type, wall
time, tokens by bucket, tool calls, model), main-loop usage, and the human
prompts that drove the run.

Usage:
  extract_trace.py <session.jsonl> [--out DIR]      # one session
  extract_trace.py --all [--out DIR]                # every daily-run session
"""
import json, sys, re, argparse
from pathlib import Path
from datetime import datetime, timezone

PROJ = Path.home() / ".claude/projects/-home-guilhermesaboia-ai-newsletter"
DAILY_MARKER = "rode o /newsletter-draft"


def ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")) if s else None


def iter_jsonl(path):
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def usage_bucket():
    return {"input": 0, "output": 0, "cache_read": 0, "cache_creation": 0, "api_calls": 0}


def add_usage(bucket, u):
    if not u:
        return
    bucket["input"] += u.get("input_tokens", 0)
    bucket["output"] += u.get("output_tokens", 0)
    bucket["cache_read"] += u.get("cache_read_input_tokens", 0)
    bucket["cache_creation"] += u.get("cache_creation_input_tokens", 0)
    bucket["api_calls"] += 1


def parse_subagent(path):
    """Aggregate one subagent transcript."""
    agg = {
        "usage": usage_bucket(),
        "models": {},
        "tools": {},
        "turns": 0,
        "first_ts": None,
        "last_ts": None,
    }
    for d in iter_jsonl(path):
        t = d.get("timestamp")
        if t:
            agg["first_ts"] = agg["first_ts"] or t
            agg["last_ts"] = t
        if d.get("type") != "assistant":
            continue
        m = d.get("message") or {}
        agg["turns"] += 1
        add_usage(agg["usage"], m.get("usage"))
        mdl = m.get("model")
        if mdl:
            agg["models"][mdl] = agg["models"].get(mdl, 0) + 1
        for c in m.get("content") or []:
            if isinstance(c, dict) and c.get("type") == "tool_use":
                agg["tools"][c["name"]] = agg["tools"].get(c["name"], 0) + 1
    return agg


def parse_session(sess_path):
    sess_path = Path(sess_path)
    session_id = sess_path.stem
    subdir = sess_path.parent / session_id / "subagents"

    agents = {}          # tool_use_id -> agent record
    receipts = {}        # agentId -> tool_use_id
    skills = []
    bash_calls = []
    prompts = []
    main_usage = usage_bucket()
    main_models = {}
    main_tools = {}
    first_ts = last_ts = None

    for d in iter_jsonl(sess_path):
        t = d.get("timestamp")
        if t:
            first_ts = first_ts or t
            last_ts = t
        typ = d.get("type")
        m = d.get("message") or {}

        if typ == "assistant":
            add_usage(main_usage, m.get("usage"))
            mdl = m.get("model")
            if mdl:
                main_models[mdl] = main_models.get(mdl, 0) + 1
            for c in m.get("content") or []:
                if not (isinstance(c, dict) and c.get("type") == "tool_use"):
                    continue
                main_tools[c["name"]] = main_tools.get(c["name"], 0) + 1
                inp = c.get("input") or {}
                if c["name"] == "Agent":
                    agents[c["id"]] = {
                        "tool_use_id": c["id"],
                        "subagent_type": inp.get("subagent_type"),
                        "description": inp.get("description"),
                        "launched_at": t,
                        "completed_at": None,
                        "status": None,
                    }
                elif c["name"] == "Skill":
                    skills.append({"skill": inp.get("skill"), "args": inp.get("args"), "ts": t})
                elif c["name"] == "Bash":
                    bash_calls.append({"ts": t, "cmd": (inp.get("command") or "")[:160]})

        elif typ == "user":
            tur = d.get("toolUseResult")
            content = m.get("content")
            # agent launch receipt -> agentId mapping
            if isinstance(tur, dict) and tur.get("agentId"):
                for c in content or []:
                    if isinstance(c, dict) and c.get("type") == "tool_result" and c.get("tool_use_id") in agents:
                        receipts[tur["agentId"]] = c["tool_use_id"]
                        # sync agents complete in the receipt itself
                        if "totalDurationMs" in tur:
                            agents[c["tool_use_id"]]["completed_at"] = t
                            agents[c["tool_use_id"]]["status"] = tur.get("status") or "completed"
            # async completion notifications
            if isinstance(content, str) and "<task-notification>" in content:
                for tid, status in zip(
                    re.findall(r"<tool-use-id>(.*?)</tool-use-id>", content),
                    re.findall(r"<status>(.*?)</status>", content) or ["?"],
                ):
                    if tid in agents and agents[tid]["completed_at"] is None:
                        agents[tid]["completed_at"] = t
                        agents[tid]["status"] = status
            # human prompts (Slack messages, not tool results/notifications)
            elif isinstance(content, str) and not content.startswith("<") and tur is None and not d.get("isMeta"):
                prompts.append({"ts": t, "text": content[:400]})

    # attach subagent transcript aggregates via agentId -> file
    for agent_id, tuid in receipts.items():
        f = subdir / f"agent-{agent_id}.jsonl"
        rec = agents.get(tuid)
        if rec is None:
            continue
        rec["agent_id"] = agent_id
        if f.exists():
            rec.update(parse_subagent(f))
    for rec in agents.values():
        a, b = ts(rec.get("launched_at")), ts(rec.get("completed_at"))
        rec["wall_s"] = round((b - a).total_seconds()) if a and b else None

    return {
        "session_id": session_id,
        "date": (first_ts or "")[:10],
        "first_ts": first_ts,
        "last_ts": last_ts,
        "prompts": prompts,
        "skills": skills,
        "bash": bash_calls,
        "main_loop": {"usage": main_usage, "models": main_models, "tools": main_tools},
        "agents": sorted(agents.values(), key=lambda r: r["launched_at"] or ""),
    }


def daily_sessions():
    import subprocess
    r = subprocess.run(
        ["grep", "-l", DAILY_MARKER, *[f.name for f in PROJ.glob("*.jsonl")]],
        cwd=PROJ, capture_output=True, text=True,
    )
    return sorted(PROJ / n for n in r.stdout.split())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("session", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent.parent / "traces"))
    args = ap.parse_args()

    targets = daily_sessions() if args.all else [Path(args.session)]
    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    for p in targets:
        trace = parse_session(p)
        name = f"{trace['date']}_{trace['session_id'][:8]}.json"
        (outdir / name).write_text(json.dumps(trace, indent=1, ensure_ascii=False))
        n_agents = len(trace["agents"])
        toks = sum(a.get("usage", {}).get("output", 0) for a in trace["agents"] if isinstance(a.get("usage"), dict))
        print(f"{trace['date']}  {trace['session_id'][:8]}  agents={n_agents:3d}  subagent_out_tok={toks:8,d}  -> {name}")


if __name__ == "__main__":
    main()
