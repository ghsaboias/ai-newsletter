# M&A Newsletter — Formatting

Reformat the M&A newsletter from `{day_dir}/final.md` into structured, section-based HTML for Substack. **Keep every link intact.** Do not change any wording, facts, or links — only restructure and style.

Read the markdown file first. Save output to `{day_dir}/substack.html`.

## Sections

Group paragraphs into thematic sections based on content. Typical sections (use only what applies to this edition):

- **🤝 Deals** — announced, completed, or failed acquisitions and mergers
- **⚖️ Regulatório** — antitrust reviews, merger challenges, regulatory decisions
- **🌍 Cross-Border** — international deals and foreign investment reviews
- **🏥 Setores** — sector-specific deal clusters (pharma, tech, energy, etc.) — use a more specific label when one sector dominates
- **📊 Mercado** — trends, activist investors, advisory mandates, market dynamics

You don't need all sections every edition. 3-5 is typical. Merge small sections. If a story could go in two sections, pick the most natural one.

## HTML Structure

```html
<h1>[title from frontmatter]</h1>
<p class="subtitle">[opening line / subtitle]</p>
<p class="byline">[byline if present]</p>

<h2>🤝 Deals</h2>
<p>[paragraph with inline links preserved]</p>

<h2>⚖️ Regulatório</h2>
<p>[paragraph]</p>

<!-- etc. -->
```

## Rules

- **Every link in the original must appear in the output.** No links dropped, no links added.
- **No wording changes.** Copy sentences verbatim. You are reformatting, not rewriting.
- **Split long paragraphs** that cover multiple deals into one `<p>` per deal when it improves readability.
- **Bold the deal value or key number** in each deal paragraph: `<strong>US$ 29,1 bilhões</strong>`.
- **Strip the YAML frontmatter** — output is pure HTML, no markdown.
- Convert markdown links `[text](url)` to HTML `<a href="url">text</a>`.
- Preserve `<em>` for italics where the original uses them.
