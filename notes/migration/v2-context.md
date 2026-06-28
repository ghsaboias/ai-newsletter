# Newsletter v2 — context

Working on v2 of the newsletter — both its **format** and its **generation pipeline**. The tasks mapped so far (Gui's framing, verbatim):

## Mapped tasks

1. **Ingestion clustering** — verify if the articles/news ingestion/creation goes through the matching logic that clusters articles instead of creating (if within the app's thresholds).

2. **Better formatting/structure** — better formatting/structuring of the newsletter. Today the paragraphs are long, boring to read, have no special formatting to make them visually more pleasant.

3. **Simplify research** — research can be vastly simplified without losses to research quality/comprehensiveness. Today we fire 3 clusters. Given that we have Techmeme ingested by DJ already, we can simply use the DJ database as our pre-made research, and do agentic search just to make sure we didn't lose anything.

4. **DJ database audit** — analyze the DJ database to check if the stories covered by previous newsletters were in the db *before* I ingested them with the newsletter `finalize.sh` flow. The goal: make sure I can rely on the db for the stories, and — if I can't rely on the db for all stories/areas — get clarity on which.

5. **Substack formatting options** — experiment extensively with all formatting options for a post that Substack offers.

6. **Best possible voice (most important)** — make the draft have the best possible voice, with no interventions/corrections made by me (there are memories about many of the corrections I've had to make to the draft). The voice is neutral, dense; the content speaks for itself.

> These items span multiple steps of the pipeline. Starting point chosen: **explore all the formatting options Substack offers first (#5).**

## Execution note for #5

First pass made using the actual Substack browser editor (already open): inventory the different formats by clicking around → `substack_inventory.md`. Then check how to use them from the API by probing it. Deliverables: drafts that use all the different formats available, so we also have a draft that is itself an inventory of all formats available.

---

*Companion docs: `substack_inventory.md` (the #5 output). Roadmap + dependencies tracked in memory (`newsletter-v2-roadmap.md`).*
