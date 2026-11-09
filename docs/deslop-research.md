# Making GovernedAI look less AI-made

Research and a ranked change list. Written 2026-11-09. Nothing in either repo was changed.

**Before you commit this file:** the Pages workflow (`.github/workflows/pages.yml`) publishes every file in the repo except `.git`, `.github`, `.claude` and `.hallmark`. If you commit `docs/`, this report and its screenshots go live at governedai.ca/docs/. Add `--exclude 'docs'` to the rsync line first, or keep the report somewhere else.

## Summary

The site's words are mostly clean. It has no em dashes, no "seamless" or "robust", and short sentences. The AI look comes from three other things:

1. **The visual defaults.** Warm cream paper, an orange accent close to Claude's own terracotta, huge tightly tracked headlines, a floating pill nav with a drop shadow, and 144 px gaps between sections. Each one is a known default of AI site generators. The site was built with the Hallmark skill, theme "Furrow", axes "light / grotesk-sans / warm" (`site.css:1-4`).
2. **The page shape.** Almost every section is a big heading plus a one-line lead beside it. Several leads are aphorisms: "The model reads. Code applies the rules." Headlines end with a full stop.
3. **A generator signature in public.** The live `site.css` starts with Hallmark's build notes, including "pre-emit critique: P4 H4 E4 S5 R4 V4". Anyone who opens the stylesheet sees that a design agent made the page.

The product UI has the opposite problem. It looks like a plain tool, which is good. Its tell is over-explanation: almost every page opens with a paragraph that tells the user what the feature does and what CVCite "never" does, then adds small grey notes under each control. The templates have 88 `lede` or `small muted` paragraphs.

## 1. What marks a page as AI-made

### Visual

| Pattern | What critics say | Sources |
|---|---|---|
| Cream or beige page with a serif or big grotesk display | The current "tasteful AI" default, after the purple gradient. Asking an agent to look "less AI" often produces warm cream with a terracotta accent. Cream plus terracotta is the Claude interface palette, so on another brand it signals the tool. | [925 Studios: AI slop tells](https://www.925studios.co/blog/ai-slop-design-tells), [925 Studios guide](https://www.925studios.co/blog/ai-slop-web-design-guide), [Impeccable: visible tells](https://924b8765.impeccable-2rv.pages.dev/slop), [capitalandcompute: fix AI slop tell by tell](https://capitalandcompute.net/blog/fix-ai-slop-design/) |
| Purple-to-blue gradient, glow, gradient text | The first-wave default. The model picks the statistical middle of its training data. | [prg.sh: the same purple gradient website](https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website), [superdesign: why AI design looks generic](https://www.superdesign.dev/blog/why-ai-design-looks-generic) |
| Three rounded cards in a row, each with an icon | Listed in almost every checklist, next to a centred hero with one button. | [Fountain Institute: 7 tells](https://pages.thefountaininstitute.com/posts/7-tells-that-a-ui-is-ai-generated), [saasui: SaaS UI looks AI-generated](https://www.saasui.design/blog/saas-ui-looks-ai-generated), [noqta: overused UI patterns](https://noqta.tn/en/blog/ai-design-slop-overused-ui-patterns-fix-2026) |
| Emoji or icon bullets | Decoration that repeats the text beside it. | [Anti AI slop ban list](https://github.com/Laith0003/ux-skill/wiki/Anti-AI-slop-ban-list), [Kosta Canatselis: spot the slop](https://world.hey.com/kostac/spot-the-slop-a-ui-designer-s-guide-to-fixing-ai-defaults-4c448c9c) |
| Eyebrow labels (small uppercase, wide tracking) over each heading; a subtitle under each heading | Once a choice, now applied by default. The stack "eyebrow, heading, description" repeats on every section. | [noqta](https://noqta.tn/en/blog/ai-design-slop-overused-ui-patterns-fix-2026), [Towards AI: 10 signs](https://pub.towardsai.net/10-signs-of-ai-generated-design-and-how-to-make-yours-not-look-like-it-482ff7da81fc) |
| Pills and badges that carry no information ("New", "Beta", "AI-powered") | A badge is only useful when it states a value the reader needs. | [Anti AI slop ban list](https://github.com/Laith0003/ux-skill/wiki/Anti-AI-slop-ban-list), [saasui](https://www.saasui.design/blog/saas-ui-looks-ai-generated) |
| Big soft shadows, floating pill nav, large radius | Part of the same default kit. | [Impeccable gallery](https://impeccable.style/gallery), [925 Studios](https://www.925studios.co/blog/ai-slop-web-design-guide) |

All of these sources make the same point: no single choice is slop. An unexamined default is. Cream is fine if it is a real brand decision. Swapping one default for another (cream for "near-black with one acid green") does not fix anything.

### Prose

| Pattern | Notes | Sources |
|---|---|---|
| "Not X but Y", "It's not just X, it's Y" | About 3 times more common in AI text than in human text. | [Wikipedia: Signs of AI writing (summary)](https://flowingdata.com/2025/10/20/signs-of-ai-writing-on-wikipedia/), [Pangram: 9 signs, with data](https://www.pangram.com/signs-of-ai-writing) |
| Triplets ("fast, simple and secure") | About 4 times more common. Wikipedia says the rule of three suits persuasion, not information. | [Pangram](https://www.pangram.com/signs-of-ai-writing), [Beutler Ink on the Wikipedia guide](https://www.beutlerink.com/blog/how-to-spot-ai-writing) |
| Em dashes | Was a strong tell for a while. Generators now avoid them, so their absence proves little. | [Boing Boing](https://boingboing.net/2025/08/20/wikipedia-publishes-list-of-ai-writing-tells.html), [Pillitteri: the new em dash](https://pasqualepillitteri.it/en/news/11195/new-em-dash-9-ai-writing-tells) |
| Stock words: seamless, robust, leverage, empower, unlock | Formal synonyms that add no meaning. | [Apollo UX writing guide](https://apollographql.com/docs/ux-writing-style-guide), [Pangram](https://www.pangram.com/signs-of-ai-writing) |
| Hero copy: short aphorism with a full stop, then a balanced one-line subtitle | "Every X, Y." headlines and two-beat leads ("The model reads. Code applies the rules.") read as written for rhythm, not for the buyer. | Pattern of the parallel-construction finding above; also [Fountain Institute](https://pages.thefountaininstitute.com/posts/7-tells-that-a-ui-is-ai-generated) |
| Text that describes itself ("Stated plainly, so…", "Here's what you need to know") | Meta-commentary. The Wikipedia guide lists it. | [dataconomy on the Wikipedia guide](https://dataconomy.com/2025/09/04/wikipedia-releases-guide-to-spot-ai-written-articles) |

The Wikipedia page warns that these signs are evidence, not proof, and that fixing only the surface signs makes detection harder without making the text better. The useful aim is text a buyer can act on, not text that passes a detector.

## 2. ASD-STE100 (Simplified Technical English)

**What it is.** A controlled language from the aerospace industry, first published as AECMA Simplified English in the 1980s for maintenance manuals read by non-native speakers. The current issue is 9 (January 2025). It has two parts: writing rules (53 in issue 9, in 9 sections) and a dictionary of about 875 approved words. The standard is free on request from [asd-ste100.org](https://www.asd-ste100.org/). ([SKYbrary](https://skybrary.aero/articles/simplified-technical-english-ste), [TechScribe](https://mail.techscribe.co.uk/techw/asd-simplified-technical-english.htm))

**Main rules:**

- Use only approved words, and only in their approved meaning. Each word has one meaning per part of speech. You may add "technical names" (product names, CV, RFP) and "technical verbs" from your field.
- Procedures (instructions): at most 20 words a sentence. Descriptions: at most 25.
- One instruction per sentence. Write instructions as commands.
- Use the active voice.
- Use simple tenses. Do not use "-ing" forms as verbs or nouns.
- Do not make noun clusters of more than three words.
- Keep articles ("the", "a"). Do not drop them to save space.
- At most six sentences in a paragraph, one topic per paragraph.
- Start a warning with a clear command.

**Tooling.** TechScribe's [term checker](https://simplified-english.co.uk/) (dictionary checks only, issue 9), [Boeing's Simplified English Checker](https://www.boeing.com/company/simplified-english-checker), and commercial tools listed on the [ASD software page](https://www.asd-ste100.org/STEsoftware.html) (Acrolinx, HyperSTE and others). There are also community Claude skills for STE, for example on [claudecodehq](https://www.claudecodehq.com/playbooks/simplified-technical-english). ASD itself says software cannot check every rule; sentence length and vocabulary are easy, paragraph structure is not.

**How practical it is here.**

- For **product UI** (instructions, errors, the Assess form, the security and privacy pages) it fits well. These are procedures and descriptions. The 20-word limit and one-instruction-per-sentence rule alone would fix most of the product's long notes.
- For **marketing copy** it is a filter, not a rulebook. Strict STE removes voice and some useful words. But its rules remove every slop pattern above as a side effect: no "-ing" openers, no stock words (none of them are in the dictionary), no aphorisms, short literal sentences.
- For **French**, STE does not apply. Write the French page from the plain English, then have a French reader check it.
- Translation gets easier, which matters for a bilingual Canadian government audience.

**Before and after.** These are STE-style rewrites. They follow the rules above but were not checked word by word against the dictionary.

| Before (source) | After |
|---|---|
| "CVCite finds the consultant's name in the CV on its own server, removes it, then reads the CV again to check; if the two readings disagree, it stops and sends nothing." (`assess_web/templates/new.html:13`, 31 words, four actions) | "CVCite finds the consultant's name in the CV and removes it. Then CVCite reads the CV again. If the two results are different, CVCite stops and sends nothing to the model." |
| "Every consultant the firm holds, by reference. A bid manager can show names beside the references (Show names, at the top); every page that shows them is recorded." (`web/templates/bench.html:9`) | "This page shows each consultant by reference number. To show names, a bid manager clicks Show names. CVCite records each page that shows names." |
| "Where a tool would guess, the grid names the gap." (`index.html:131`) | "If the CV does not show a criterion, the grid shows a gap and the reason." |

## 3. What "Claude design" means

It almost certainly means **Claude Design**, a product from Anthropic Labs launched on 17 April 2026 as a research preview. ([Anthropic announcement](https://www.anthropic.com/news/claude-design-anthropic-labs), [The New Stack](https://thenewstack.io/anthropic-claude-design-launch/), [VentureBeat](https://venturebeat.com/ai/anthropic-just-launched-claude-design-an-ai-tool-that-turns-prompts-into-prototypes-and-challenges-figma))

What it does:

- You first set up a design system: colours, type and components. Claude Design builds it from a GitHub repo, a local folder, Figma files, logos, fonts or a brand deck. Every later project uses it. ([Claude support guide](https://support.claude.com/en/articles/14604397), [DesignerUp](https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/))
- You then make prototypes, pages or slides on a visual canvas, and compare versions.
- Export goes to HTML, PDF, PPTX, Canva, or "Handoff to Claude Code". ([Design Systems Collective workflow](https://www.designsystemscollective.com/from-prompt-to-production-a-designers-step-by-step-workflow-with-claude-design-claude-code-a7705daad026))
- Available on Pro, Max, Team and Enterprise. Off by default on Enterprise.

What the observer most likely meant: decide the look visually first, in Claude Design, and only then bring the design system into code. The current site went the other way. A coding agent with the Hallmark skill picked a theme and wrote tokens straight into `tokens.css`. Nobody compared alternatives on a canvas.

Suggested use:

1. Set up a design system in Claude Design from the bidgrid repo (the grid's tokens in `render/style.py` are the strongest existing identity) plus the rules in section 5 below.
2. Tell it what is banned (cream, terracotta, floating pill nav, display type over 48 px). One source notes cream plus terracotta is Claude's own palette, so do not trust its defaults either.
3. Mock the home page and one product page in two or three directions. Pick one.
4. Hand off to Claude Code. Make later visual changes in Claude Design first, so code and design do not drift. ([claudefa.st on handoff](https://claudefa.st/blog/guide/mechanics/claude-design-handoff))

## 4. Audit

Screenshots of the live site, taken 2026-11-09 in an 800 px wide pane:

- [Home, first screen](deslop-screens/home-hero.jpg): beige paper, orange button, headline over four lines.
- [Home, gaps section](deslop-screens/home-gaps.jpg): big heading at left, one short line far right, wide empty space.
- [Security, first screen](deslop-screens/security-top.jpg): a one-word marketing hero for a policy page, then a large gap.
- [Vision tour, first screen](deslop-screens/vision-top.jpg): hero with nothing beside it, then a large gap.

### Public site

| Where | What reads as AI | Fix |
|---|---|---|
| `site.css:1-4` (live) | Hallmark build notes and "pre-emit critique" scores ship in the public stylesheet. | Delete the comment. Keep build notes in `.hallmark/`, which is not published. |
| `tokens.css:11` `--color-paper: oklch(96% 0.011 85)` and `paper-2`, `paper-3`, `rule`, `grid`, `sheet` (hue 85) | Warm cream page. The observer's "cream is banned". | White or a cool neutral grey. See house style. |
| `tokens.css:13` `--color-accent: oklch(70% 0.19 40)` | Orange close to Claude's terracotta (#D97757). With cream it is the exact Claude look. | Ink (`#17202E`) buttons and links until the brand work picks an accent. Not the grid's blue: that colour means "gap". |
| `tokens.css:12` ink and muted at hue 60 | Warm-tinted greys, part of the same palette. | Neutral or cool greys. |
| `tokens.css:4,20,22` display sizes up to 5.25 rem, tracking −0.035em, weight 600 | Giant tightly tracked grotesk headline. Home h1 wraps to four lines at 800 px (`home-hero.jpg`). | Max about 2.75 rem for h1, 1.75 rem for h2, tracking −0.01em or 0. |
| `site.css:11-12` floating pill nav with `--shadow-card` | Floating pill nav is a named Hallmark default ("nav: floating pill"). | Plain header with a bottom rule. No shadow. |
| `site.css:36,61,91` and `tokens.css:21-22` soft long shadows on sheet, screenshots and video | Soft drop-shadow cards. | 1 px border. No shadow. |
| `tokens.css:9` section gaps 120 to 176 px | Long empty bands between short sections (`home-gaps.jpg`, `security-top.jpg`). | 48 to 72 px. |
| `site.css:57` `.head`: heading left, lead right, on every section | The "subtitle under every heading" pattern, as a layout. Home has 5 leads, vision 3. | Heading, then content. Keep a sentence only when it states a fact. |
| `index.html:32`, `fr/index.html:32`, `vision/index.html:31` | Headlines end with a full stop ("Every criterion, cited from the CV."). A current AI-hero tic. | No full stop. Say what it does: "Check a CV against every RFP criterion". |
| `index.html:116` "The model reads. Code applies the rules." | Two-beat aphorism. | "A language model finds the CV text. Fixed rules decide each verdict." |
| `index.html:131` "Where a tool would guess, the grid names the gap." | Antithesis built for rhythm. | Delete; the table under it says this. |
| `index.html:80` "Answers use only the CV's own passages, each one numbered and quoted." | Fine as a fact, but it repeats the h2. | Keep one of the two. |
| `vision/index.html:55` "Stated plainly, so nobody mistakes a plan for a product." | Text that describes itself. | Delete. |
| `vision/index.html:32` "A concept tour of the product as planned, not as built." | "X, not Y" pattern. | "This film shows planned features. Most are not built yet." |
| `index.html:145-158` band with `dl` | Fine. Real facts (what you send, what you get, processing, deletion). | Keep. Fill in the retention days; the dashed placeholder looks unfinished. |
| `index.html:48-53` verdict chips | Not slop: each chip states a verdict. | Keep. |
| `security/index.html:29-34`, `privacy/index.html:29-34` | A marketing hero for a policy page, then a big gap. | Plain document layout: normal h1, text at 65 ch, no hero spacing. |
| `security/index.html:32` "Where client data is kept, who processes it, how it is protected, and how to tell us about a problem." | Lead that lists the headings below it. | Delete; the headings do this. |
| `fr/index.html` | Same structure and same aphorisms ("Le modèle lit. Le code applique les règles."). | Same fixes; write the French from the new English. |

### Product UI (bidgrid, read only)

| Where | What reads as AI | Fix |
|---|---|---|
| `web/templates/in_mind.html:9` "Most bids start from a few people someone already has in mind. Put up to … side by side: …; then shortlist th…" | Opening paragraph that sells the feature to someone already using it. | One line: "Compare up to N consultants." |
| `web/templates/bench.html:9`, `lists.html:7`, `opportunities.html:5`, `costs.html:5` | Same pattern: every page opens with a lede that narrates the feature. | Cut to one line or nothing. Put the explanation in a help page. |
| `web/templates/lists.html:7` "You decide who is on each list: CVCite never adds or removes anyone." and `bench.html:30` "CVCite never merges two people" | Repeated reassurance about what the tool never does. | Say it once, in the help page or on the action itself. |
| `web/templates/bench.html:22`, `bench.html:30`, `_add_to_bid.html:17`, `opportunity.html:106`, `list.html:60` | Long small grey notes under controls. 88 `lede` or `small muted` paragraphs across both apps. | Max one sentence under a control, 20 words. Move the rest to help. |
| `_add_to_bid.html:17` "Costs nothing and grids nobody." | Cute parallel phrasing. | "This does not run a grid." |
| `assess_web/templates/new.html:13,22,28` | 30 to 45 word hints with semicolons and several actions each. | STE rewrite (see section 2). |
| `assess_web/templates/sign_in.html:5` | Sign-in page with a product pitch. | "Enter your invite code." Link to the site for the pitch. |
| `assess_web/templates/base.html:29` "invite-only beta" beside the brand; `web/templates/base.html:16` "local · development data only" | Status label that adds little on every page. The dev one is useful in dev only. | Show the dev label only when not in production. Drop "invite-only beta"; the sign-in already says it. |
| `web/templates/bench.html:56` `<span class="pill none">not assessed</span>` | Pill for an empty value. | A plain dash. Keep pills for real states. |
| `web/static/app.css:106` `.send-list li::before` filled black number circles | Decorative numbered badges. | Plain numbers. |
| `web/static/app.css:24-25`, `:116-117` rounded filter and pick chips (12 to 14 px radius) | Pill chips. Mild. | Same 3 to 4 px radius as buttons. |
| `render/style.py:19-28` grid palette and Charter for quotes | Not slop. Cool neutrals, verdict colours with meaning, serif only for quoted CV text. | Keep. Use it as the base for the site's house style. |

## 5. Recommendations

### House style

**Palette** (taken from the grid, so site and product match):

- Page `#FFFFFF`. Bands and table stripes `#F5F6F7`.
- Ink `#17202E`. Secondary text `#566171`. Rules `#DFE3E8`.
- Buttons and links in ink `#17202E`. Any accent the brand work adds must not be close to a verdict colour, or a link will look like a verdict.
- Verdict colours only on verdicts: supported `#1A6B43` on `#E3F2EA`, partial `#8A5600` on `#FBEFD2`, gap `#234F97` on `#E2EBFA`, unsupported `#434C59` on `#ECEEF1`, needs confirmation `#5F2C8C` on `#F1E8FA`.
- No cream, beige, terracotta, orange, gradients or glow.

**Type:**

- One sans for everything: Red Hat Text is fine, or the system UI stack the grid uses.
- Charter (serif) only for quoted CV and RFP text, as the grid does. A serif then means "this is a quote".
- Mono only for IDs (M01, notice numbers).
- h1 at most 2.75 rem, h2 1.75 rem, h3 1.25 rem. Weight 600. Tracking 0 to −0.01em.
- Headings in sentence case, no full stop.

**Layout:**

- Plain top bar with a bottom rule. No floating nav, no shadows.
- Radius 4 px or less. Borders, not shadows.
- Section gaps 48 to 72 px.
- Text pages (privacy, security) as a single column, 65 ch wide.
- The product is the visual: real grid rows and screenshots, at real size. No icons, no illustrations.

**Prose:**

- Write to the bid manager. Say what the product does to their CV and RFP.
- Sentences at most 20 words for instructions, 25 for descriptions.
- One idea per sentence. Active voice.
- No headline full stops, no aphorisms, no "not X but Y", no triplets for rhythm.
- No sentence that describes the page itself.
- A sentence under a heading must give a fact the heading does not.
- Numbers and names over adjectives: "18.1 s", "notice 1000190326", "35 days".

### Deslop checklist for CLAUDE.md

Paste this into the CLAUDE.md of both `governedai-site` and `bidgrid`:

```markdown
## Deslop rules (UI and copy)

Visual
- No cream, beige or warm off-white backgrounds. Page is #FFFFFF; bands #F5F6F7.
- No terracotta or orange accent. Buttons and links in ink #17202E. No accent close to a verdict colour (green, amber, blue, purple). Verdict colours only on verdicts.
- No gradients, glow, gradient text, or soft drop shadows. Use 1px borders.
- No floating or pill-shaped nav. Radius 4px or less everywhere.
- No icon or emoji bullets. No three-card feature rows. No decorative illustrations.
- No eyebrow labels above headings.
- h1 at most 2.75rem; tracking no tighter than -0.01em. Serif only for quoted CV/RFP text.
- Section spacing 48-72px. Do not pad a short section to fill a screen.

Content
- Do not put a subtitle under a heading unless it states a fact the heading does not.
- Remove every sub-text, hint, status or badge that does not change what the user does next.
- A pill or badge must show a value (a verdict, a state). Never "New", "Beta", "AI".
- Empty values are a dash, not a pill.

Prose (based on ASD-STE100)
- At most 20 words in an instruction, 25 in a description. One instruction per sentence.
- Active voice. Simple tenses. No "-ing" openers.
- No: seamless, robust, leverage, empower, unlock, effortless, streamline, cutting-edge.
- No "not X but Y" / "not just X", no rhythmic triplets, no two-beat aphorisms.
- No em dashes. No full stops on headings.
- No text that describes itself ("Simply put", "Stated plainly", "Here's how").
- Say what CVCite "never" does once, in one place, not on every page.

Process
- Do visual direction in Claude Design first; code follows the approved design.
- Never ship generator notes (Hallmark comments, critique scores) in public files.
- Before merging UI: read every visible string aloud and delete each one you would not say to a bid manager.
```

### Top 10 changes, ranked by effect per hour

| # | Change | Where | Effort | Why this rank |
|---|---|---|---|---|
| 1 | Delete the Hallmark comment from the public stylesheet | `site.css:1-4` | 5 min | Direct proof the page is machine-made, for anyone who views source. |
| 2 | Replace cream and orange with white, cool greys and ink buttons | `tokens.css:11-16` | 30 min | The single biggest visual tell, and the observer named it. A token change recolours every page. |
| 3 | Cut leads under headings that add no fact, and the aphorisms | `index.html:80,116,131`; `fr/index.html:80,117,132`; `vision/index.html:32,55`; `security/index.html:32` | 45 min | Removes the "subtitle under every heading" pattern and the most mannered lines. |
| 4 | Plain header instead of the floating pill nav; borders instead of shadows | `site.css:11-12,36,61,91`; `tokens.css:21-22` | 1 h | Second most recognisable visual default. |
| 5 | Smaller headings, normal tracking, no headline full stops | `tokens.css:4,20`; `index.html:32`; `fr/index.html:32`; `vision/index.html:31` | 45 min | Ends the four-line giant headline. |
| 6 | Section gaps down to 48-72 px | `tokens.css:9`, `base.css:23-24` | 15 min | Removes the empty bands that make short pages look padded. |
| 7 | Security and privacy as plain documents | `security/index.html`, `privacy/index.html`, one new CSS class | 1 h | These are the pages a government buyer's security team reads. A marketing hero there looks wrong. |
| 8 | Product: cut each page's opening lede to one line; move explanations to a help page | `web/templates/*.html`, `assess_web/templates/*.html` | 3-4 h | The product's main tell. Larger job, so ranked lower per hour. |
| 9 | Product: STE pass on the Assess form and its errors; drop the "invite-only beta" label and empty-value pills | `assess_web/templates/new.html`, `base.html:29`, `web/templates/bench.html:56`, `app.css:106` | 2 h | Assess is what beta users see first. |
| 10 | Set the house style in Claude Design from the grid's palette, then hand off to code | Claude Design, then both repos | 4-6 h | Stops the next generated page from bringing the defaults back. |

Items 1 to 6 together are about three hours of work on the public site and change how it looks on every page. Do them, and the French page, in one pass, then take new screenshots for comparison.
