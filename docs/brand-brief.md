# Brand brief: GovernedAI and CVCite

For Claude Design. Paste everything under "Brief" into a new design-system setup. Fill in the three decisions marked **[Steph]** first.

Attach with it:
- the bidgrid repo, or just `cvcite/render/style.py` (the grid's colours and type);
- a screenshot of the sample grid: https://governedai.ca/cvcite/sample-grid/
- your reference sites (decision 2).

---

## Brief

### Who we are

GovernedAI is a one-person company in Ottawa. Its product is CVCite.

CVCite checks a consultant's CV against the mandatory and rated criteria in a Canadian government solicitation. For each criterion it says whether the CV supports it, and it quotes the CV lines that show it. If the CV does not show it, CVCite names the gap. It does not guess. Every sentence it writes is checked against the quoted text, and a sentence that fails is rewritten once or removed.

CVCite works in English and French. French is in beta.

### Who buys

Bid managers and owners at IT and professional-services staffing firms that bid on federal and provincial contracts. They read dense solicitations every week. They care about:
- not losing a bid on a mandatory criterion;
- the time it takes to match CVs to criteria;
- where client and consultant data is kept (Canada, by default).

Their security and procurement staff will also read the site. They expect plain facts.

### What the brand should feel like

- A well-made working document, not a startup landing page.
- Exact and calm. Numbers, references and quotes do the persuading.
- Serious enough for a government bid team, without looking like the government.

### Decisions **[Steph]**

1. **Which name leads:** GovernedAI (the company) with CVCite as its product, or CVCite first with "by GovernedAI". Today the site leads with CVCite. → CVCite first with "by GovernedAI"
2. **References:** 3 to 5 sites whose look I like: ______. 1 or 2 I do not like: https://proposalforge.io.
3. **One word for the colour of the brand**, if any (for example "ink", "slate", "forest"), or "let Claude Design propose three". → let Claude Design propose three

### What already exists, and must stay

The compliance grid is the product. Its colours carry meaning and must not change or be reused for decoration:

| Verdict | Text | Background |
|---|---|---|
| Supported | `#1A6B43` | `#E3F2EA` |
| Partial | `#8A5600` | `#FBEFD2` |
| Unsupported | `#434C59` | `#ECEEF1` |
| Gap (working view) | `#234F97` / `#2B5FB4` | `#E2EBFA` |
| Needs confirmation | `#5F2C8C` / `#7A3FB0` | `#F1E8FA` |

Grid neutrals: ink `#17202E`, muted `#566171`, rules `#DFE3E8`, canvas `#F3F4F1`, paper `#FFFFFF`.

Grid type: a sans (system UI stack) for the tool's own words; Charter (serif) only for quoted CV and solicitation text.

**The brand accent must not be green, amber, blue or purple close to the verdict colours.** A link or button must never look like a verdict. If no accent fits, use ink for buttons and links.

### Banned

- Cream, beige or warm off-white backgrounds.
- Terracotta, clay or orange accents.
- Purple or blue gradients, glow, gradient text.
- Soft drop shadows; floating or pill-shaped navigation; corner radius over 4 px.
- Three-card feature rows, icon or emoji bullets, decorative illustrations, stock photos.
- Eyebrow labels above headings; a subtitle under every heading.
- Badges with no value ("New", "AI-powered", "Beta" as decoration).
- Display headlines over 2.75 rem, tight negative tracking, full stops on headings.
- Anything that suggests the Government of Canada: red-and-white maple leaf, the Canada wordmark style, the federal identity colours used together.
- A pictorial or abstract logo symbol. We want a wordmark only.

### What to make

1. **Wordmark.** "GovernedAI" (and "CVCite") set in the brand typeface, with any small type adjustment it needs. One colour on white, one reversed on ink. No symbol.
2. **Palette.** Neutrals, one accent (or none), plus the verdict colours above, unchanged. Give contrast ratios for text pairs. Must pass WCAG AA.
3. **Type.** One sans family for UI and headings (Google Fonts or system, free for web use, with full French accents). Charter or an equal serif for quotes only. A mono for IDs. A size scale with h1 at most 2.75 rem.
4. **Components.** Header, footer, button (primary and secondary), link, table, verdict pill, definition list, form field, notice (info, warning, error).
5. **Mock pages, in two or three directions:**
   - The home page, using its current content: hero with the six-verdict table, demo video, a grid screenshot, the gaps list, "how a verdict is reached", "what it will not do", the free-match offer.
   - The security page as a plain document.
   - One product page: the Bench (a table of consultants with filters).
   Same content in each direction; only the system changes.

### Writing rules for any copy in the mocks

- Use the real copy from governedai.ca. Do not write new marketing lines.
- If a line is needed: at most 20 words, active voice, no "not X but Y", no triplets, no slogans.

### Handoff

When a direction is chosen, export tokens as CSS custom properties and hand off to Claude Code for two repos: `governedai-site` (static HTML) and `bidgrid` (Jinja templates plus the grid stylesheet in `cvcite/render/style.py`). Verdict colour names in code stay `--sup`, `--par`, `--uns`, `--gap`, `--cfm`.
