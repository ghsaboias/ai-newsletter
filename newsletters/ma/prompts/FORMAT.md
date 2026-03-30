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

<!-- Deal summary table: every deal/event in the edition -->
<table>
  <tr><th>Deal</th><th>Valor</th><th>Status</th></tr>
  <tr><td><strong>Sysco</strong> → Jetro Restaurant Depot</td><td>US$ 29,1 bi</td><td>Anunciado</td></tr>
  <!-- ... one row per deal ... -->
</table>

<hr>

<h2>🤝 Deals</h2>
<p>[paragraph with inline links preserved]</p>

<h2>⚖️ Regulatório</h2>
<ul>
  <li><strong>Nexstar / Tegna</strong> — [description with links]</li>
  <li><strong>DOJ / Paramount-WBD</strong> — [description with links]</li>
</ul>

<!-- etc. Use <hr> between sections -->
```

## Rules

- **Every link in the original must appear in the output.** No links dropped, no links added.
- **No wording changes.** Copy sentences verbatim. You are reformatting, not rewriting.
- **Deal summary table at the top.** One row per deal or major event. Columns: Deal (acquirer → target or description), Valor (deal value or "-" if undisclosed), Status (Anunciado / Concluído / Bloqueado / Em revisão / etc.).
- **Bold key actors.** Company names, regulators, and people get `<strong>` on first mention in each section.
- **Use `<ul>/<li>` lists** when a section has 3+ short items (especially regulatory actions, cross-border updates). Use `<p>` for longer narrative items with context.
- **Split long paragraphs** that cover multiple deals into one `<p>` or `<li>` per deal.
- **Bold the deal value or key number** in each item: `<strong>US$ 29,1 bilhões</strong>`.
- **`<hr>` between sections** for visual breathing room.
- **`<blockquote>` for notable quotes** — pull out direct quotes that add color (e.g. regulator statements, activist critiques).
- **Strip the YAML frontmatter** — output is pure HTML, no markdown.
- Convert markdown links `[text](url)` to HTML `<a href="url">text</a>`.
- Preserve `<em>` for italics where the original uses them.
