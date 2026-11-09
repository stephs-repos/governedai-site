# Handoff: CVCite by GovernedAI — brand system, direction 1a "Ink"

## Overview
Brand system for CVCite (product) by GovernedAI (company, Ottawa). Chosen direction: **1a Ink** — no accent colour; buttons and links are ink so nothing can be read as a verdict. Apply to two repos:
- `governedai-site` — static HTML marketing site (home, security, privacy, sample grid, FR).
- `bidgrid` — Jinja templates + grid stylesheet in `cvcite/render/style.py`.

## About the design files
`CVCite Brand Directions.dc.html` is a **design reference built in HTML**, not production code. Open it in a browser; set the Tweak "only" to "a" (or read the 1a column). Recreate the designs in each repo's existing structure (plain HTML/CSS for the site, Jinja + the style.py stylesheet for bidgrid). `tokens.css` IS meant to be used directly.

## Fidelity
High-fidelity. Colours, type, sizes, radii and copy are final.

## Hard rules (from the brief — enforce in review)
- Verdict colours (`--sup --par --uns --gap --cfm` and their `-bg`/`-ink`) appear **only** on verdicts. Never on links, buttons, notices, charts-as-decoration.
- No accent. Buttons/links = ink.
- Background is `--canvas` #F3F4F1 or `--paper` white. No cream/beige/warm off-white.
- No shadows, no gradients (striped image placeholders excepted in mocks only), radius ≤ 4px (2px default, 3px pills).
- No floating/pill nav, no three-card feature rows, no icon/emoji bullets, no illustrations, no stock photos.
- No eyebrow labels, no decorative badges ("New", "AI-powered", "Beta").
- Headings: no full stop, no negative tracking, h1 ≤ 2.75rem (we use 2.5rem). **Note:** the live home h1 "Every criterion, cited from the CV." — drop the full stop.
- Nothing resembling Government of Canada identity (maple leaf, FIP red+white+black together, Canada wordmark style).
- Wordmark only, no symbol.
- Copy: use existing governedai.ca copy. New lines ≤ 20 words, active voice, no "not X but Y", no triplets, no slogans.

## Design tokens
See `tokens.css` (complete). Summary:

Neutrals: ink #17202E · muted #566171 · rule #DFE3E8 · canvas #F3F4F1 · band #F7F8F6 · paper #FFFFFF · field border #737D8C
Action: accent = ink #17202E, hover #2C3747, text on accent #FFFFFF; link = ink, underline #8A93A0, offset 3px, hover underline = currentColor
Error: #A61B29 on #FBEAEB
Verdicts (unchanged): Supported #1A6B43/#E3F2EA · Partial #8A5600/#FBEFD2 · Unsupported #434C59 text, #6B7482 bar/border, #ECEEF1 bg · Gap #234F97 text, #2B5FB4 bar/border, #E2EBFA bg · Needs confirmation #5F2C8C text, #7A3FB0 bar/border, #F1E8FA bg

### Contrast (WCAG 2.2; AA = 4.5:1 text, 3:1 UI)
| Pair | fg / bg | Ratio |
|---|---|---|
| Ink on paper | `#17202E` / `#FFFFFF` | 16.37:1 |
| Ink on canvas | `#17202E` / `#F3F4F1` | 14.83:1 |
| Muted on paper | `#566171` / `#FFFFFF` | 6.28:1 |
| Muted on canvas | `#566171` / `#F3F4F1` | 5.69:1 |
| Paper on ink (button, reversed) | `#FFFFFF` / `#17202E` | 16.37:1 |
| Error on paper | `#A61B29` / `#FFFFFF` | 7.47:1 |
| Ink on error-bg | `#17202E` / `#FBEAEB` | 14.09:1 |
| Field border on paper (UI, needs 3:1) | `#737D8C` / `#FFFFFF` | 4.17:1 |
| Supported pill | `#1A6B43` / `#E3F2EA` | 5.62:1 |
| Partial pill | `#8A5600` / `#FBEFD2` | 5.39:1 |
| Unsupported pill | `#434C59` / `#ECEEF1` | 7.48:1 |
| Gap pill | `#234F97` / `#E2EBFA` | 6.64:1 |
| Needs confirmation pill | `#5F2C8C` / `#F1E8FA` | 7.94:1 |

All text pairs pass AA.

### Type
- Sans (UI + headings): **IBM Plex Sans** 400/500/600/700, Google Fonts, OFL, full French accents.
- Serif (quoted CV and solicitation text ONLY): **Charter** stack — `Charter, "Bitstream Charter", "Sitka Text", Cambria, Georgia, serif`. Not on Google Fonts; system fallback is acceptable. Self-host Bitstream Charter (free licence) if consistent rendering matters.
- Mono (IDs, notice numbers, criterion IDs, timings, dates in tables): **IBM Plex Mono** 400/500.
- Scale: h1 2.5rem/1.15/600 · h2 1.625rem/1.25/600 · h3 1.1875rem/1.35/600 · lead 1.125rem/1.55 · body 1rem/1.55 · small 0.875rem/1.5 · caption 0.8125rem · pill 0.75rem/1.55/600. Letter-spacing 0 everywhere.
- Use `font-variant-numeric: tabular-nums` for counts, ratios, percentages.

## GovernedAI corporate mark (chosen: wordmark 2a + icon 3a)
Reference: `GovernedAI Logo.dc.html` (options #2a and #3a).

**Wordmark 2a:** IBM Plex Sans, letter-spacing +0.005em. "Governed" weight 500 + "AI" weight 700, no space: `<span class="wm-corp">Governed<b>AI</b></span>`. Ink #17202E on white; white on ink. Header size 22px. Mirrors the CVCite mark ("CV" 700 + "Cite" 500).

**Icon 3a "Cited G":** an ink #17202E square with a white "G" lower-left and a white outlined citation box, the same box as the grid's numbered citation marker (`sup span`), top-right. No rounding on the square. Specs on a 96px grid:
- Square 96×96, #17202E.
- "G": IBM Plex Sans 500, 58px, line-height 1, white; left 10px, bottom 6px.
- Citation box: 24×24 (border-box), 3px white border, radius 3px, top 10px, right 10px. Contains "1", IBM Plex Sans 700 14px, white, centred.
- 36px (next to wordmark): G 22px at left 4 / bottom 2; box 9×9, 1.5px border, radius 1px, top 4 / right 4. No number.
- 16px favicon: G 600 10px at left 1 / bottom 0; box 5×5, 1px border, top 2 / right 2. No number.
- Leave a clear gap of 4px or more (at 96px) between the G and the box.
- Lockup: icon at 36px + 12px gap + wordmark at 26px, vertically centred.
- Production: convert the text to outlines and export favicon.svg, favicon-32.png, apple-touch-icon (180px), and a 512px PNG. Make a hand-tuned 16px version; don't just scale down.
- The icon is never recoloured. No verdict colours. White-on-ink only (on dark backgrounds, add a 1px #FFFFFF outline around the square or use the wordmark alone).

## CVCite wordmark
Live text, not an image. IBM Plex Sans, letter-spacing +0.005em.
- "CVCite": "CV" weight 700 + "Cite" weight 500, no space: `<span class="wm"><b>CV</b>Cite</span>`.
- Lockup: wordmark + "by GovernedAI" in 400, muted (#566171 on white, #B8C0CA on ink), baseline-aligned, gap 8px. Header size: wordmark 24px, "by GovernedAI" 13px.
- "GovernedAI" alone: weight 700.
- Colourways: ink #17202E on white; white on ink #17202E. No other colours.
- CVCite leads; "by GovernedAI" follows.

## Components
- **Header (site):** white bg, border-bottom 2px solid ink, padding 16px 40px, flex space-between. Left: wordmark lockup (link to /). Right nav, gap 24px, 15px/500: "Sample grid", "Français" (lang="fr"), then primary button "Ask for a free match" (padding 9px 14px). Not sticky, not floating.
- **Header (app, bidgrid):** same bg/border, padding 0 32px. Wordmark 20px, then tabs gap 28px, 15px/500, padding 18px 0 15px, active = 600 + 3px solid currentColor bottom border. Right: "Sign out" muted 14px.
- **Footer:** paper bg, border-top 1px rule, inner max-width 1080px, padding 28px 40px 36px, gap 14px, 14px/1.5 muted. Lines: "An RFP to try? info@governedai.ca" (ink); nav links ink, gap 20px (Sample grid, Français, Privacy, Security); legal line "GovernedAI, Ottawa. The sample grid uses CanadaBuys notice 1000190326 and contains information licensed under the Open Government Licence, Canada." max-width 760px.
- **Button primary:** bg ink, text white, 1px solid ink, padding 10px 16px (9px 14px in header / 8px 14px compact), 15px/1.3/600, radius 2px; hover bg #2C3747; focus 2px ink outline offset 2px.
- **Button secondary:** transparent, 1px solid ink, ink text, same metrics; hover bg paper (on canvas) or canvas (on paper).
- **Disabled:** text #6F7A88, border rule, bg canvas.
- **Link:** ink, underline #8A93A0 offset 3px; hover underline currentColor. Never coloured.
- **Table:** paper bg, 1px rule border. th: left, 600, muted, 13–14px, padding 8px 12px, border-bottom 2px solid ink. td: padding 7–9px 12px, border-top 1px rule. Total row: 700, border-top 1px ink. Numbers right-aligned, tabular. IDs in mono 13px/500.
- **Verdict pill:** inline-block, padding 1px 8px, radius 3px, 12px/1.55/600, nowrap; colours per verdict (text = -ink where defined).
- **Definition list:** grid 140px / 1fr, 15px/1.5. dt 600, padding 10px 16px 10px 0; dd padding 10px 0; each row border-top 1px rule. Security page variant: stacked dt (1.1875rem/600) over dd (16px/1.6), border-top 1px rule, padding 12px 0.
- **Form field:** label 14px/600 above, gap 6px. Input: 15px, padding 8px 10px, 1px solid #737D8C, radius 2px, paper bg; focus 2px ink outline offset 1px. Hint 13px muted below. Error: 2px solid #A61B29 border (padding 7px 9px to keep size), message 13px/600 #A61B29 below. Checkboxes: accent-color ink.
- **Notices** (padding 12px 14px, radius 2px, 14px/1.5, leading bold word + full stop):
  - Info: 1px rule border, paper bg, "Note."
  - Warning: 1px ink border with 3px ink top border, paper bg, "Warning."
  - Error: 1px #A61B29 border, #FBEAEB bg, "Error." in #A61B29, body ink.
  - Never amber/blue/purple — those are verdicts.

## Screens
### Home (governedai.ca/)
Canvas bg; main max-width 1080px, padding 56px 40px 72px, sections gap 72px.
1. Hero — grid 5fr/7fr, gap 48px. Left: h1 "Every criterion, cited from the CV" (no full stop); lead "CVCite checks a consultant’s CV against an RFP and flags every gap." 18px; buttons gap 12px: primary "Ask for a free match", secondary "Open the sample grid". Right: paper table box — title row h2 16px/600 "Six mandatory criteria, one CV" + "18.1 s" mono 13px muted right; columns Criterion (mono) / Asks for / Verdict (pill) / Why (muted). Rows M01–M06 as on live site (M02, M03 = Gap). Caption 13px muted: "A fictional consultant we wrote, against CanadaBuys notice 1000190326. The full grid."
2. "The demo in under two minutes" — h2, p with link "the concept tour", 16:9 video max-width 840px, 1px rule border.
3. "Every sentence points to its line" — h2, p, grid-case.png full width, caption.
4. "Gaps you can fix before bidding" — grid 4fr/6fr: list (each item border-top rule, padding 10px 0, bold term over muted description) + grid-gaps.png with caption "M02: the reason, then each requirement."
5. "How a verdict is reached" — h2, p "The model reads. Code applies the rules.", ordered list as rows: grid 56px / 300px / 1fr, gap 16px, padding 14px 0, border-top rule; number mono "01"–"04" muted, h3, p. (Rows, not cards.)
6. "What it will not do" — h2, p, two-column table (It will not / You see instead), first column 45%.
7. Free match — border-top 2px ink; grid 4fr/6fr: h2 "A free match on your RFP" + primary button "Email info@governedai.ca"; definition list You send / You get / Processing / Afterwards.
Then footer.

### Security (/security/)
Plain document. Main max-width 760px, paper bg with 1px rule left/right, padding 56px 40px 72px, gap 40px. h1 "Security", lead paragraph, then h2 sections (Where data is kept; Sub-processors; How it is protected) each with stacked definition list; final h2 "Reporting a security problem" + paragraph. Copy verbatim from the live page.

### Bench (bidgrid, product)
App header (above). Content padding 28px 32px 40px, gap 20px.
- Title row: h1 "Bench" 1.75rem/600 + count "6 consultants" 15px muted; right buttons secondary "Export CSV", primary "Add a CV" (8px 14px, 14px).
- Grid 240px / 1fr, gap 24px. Left filter panel: paper, 1px rule, radius 2px, padding 16px, gap 18px — "Name or role" text input, "Clearance" select (Any/Reliability/Secret/Top Secret), "Languages" fieldset checkboxes English/French, "Location" select.
- Right: info notice "Note. French is in beta, said on the grid." then table: ID (mono) / Name (ink link, 600) / Role / Clearance / Languages / Location / CV updated (mono, muted, ISO date) / Grids (right). Row hover bg canvas.
Consultant data in the mock is fictional.

## Interactions
- Hover: buttons darken (#2C3747) or fill; links switch underline to currentColor; table rows → canvas. No transitions needed; if any, ≤120ms opacity/colour only.
- Focus: visible 2px ink outline on all interactive elements.
- No animation.
- Responsive (site): below ~860px, two-column grids collapse to one column; header nav wraps; tables scroll horizontally (`overflow-x:auto`). Bench filters stack above table.

## bidgrid / style.py notes
- Keep existing verdict variables and names. Add `--uns-ink`, `--gap-ink`, `--cfm-ink` as above (values already used inline in the grid).
- Swap the grid's UI font stack to `var(--sans)` (IBM Plex Sans) and its h1/group headings from Charter to the sans — Charter stays only on quoted passages (`.ev q`) and criterion/solicitation text.
- Toggle/buttons: radius 5px → 2px. Tooltip radius 6px → 2px. Key panel radius 6px → 2px.
- Focus outline: switch to ink (currently Gap blue — a verdict colour).
- `.clamp` "Show all" link: currently #234F97 (Gap) — change to ink.

## Assets
None. No logo files — wordmark is live text. Screenshots (grid-case.png, grid-gaps.png) and demo video already exist on governedai.ca.

## Files
- `tokens.css` — production tokens for direction 1a.
- `CVCite Brand Directions.dc.html` — visual reference for all three directions; 1a is the chosen one.
- `GovernedAI Logo.dc.html` — corporate wordmark and icon options; 2a + 3a chosen.
- `support.js` — runtime for the two .dc.html references; keep it in the same folder.
