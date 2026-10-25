# AI search and answer engines in Croatian

Researched 2026-10-25.

## 1. Availability

| Surface | Croatia / Croatian | Source (read 2026-10-25) |
|---|---|---|
| Google AI Overviews | Croatia is a supported country; Croatian is a supported language (also Bosnian, Serbian, Serbian (Latin), Slovenian) | support.google.com/websearch/answer/14901683 |
| Google AI Mode | Croatia supported; Croatian supported. AI Mode expanded to 35+ new languages and 40+ countries on 7 Oct 2025 | support.google.com/websearch/answer/16011537; blog.google, 7 Oct 2025 |
| Gemini model choice inside AI Mode (premium model) | Not listed for Croatia or other EU countries on the help page | same page |
| ChatGPT search, Gemini app, Microsoft Copilot, Perplexity | Usable in Croatia and in Croatian | product availability; no Croatia-specific restrictions found |

Usage: 32% of Croatian internet users aged 16–74 used a generative AI tool in
the three months before the 2025 survey, mostly for private purposes (90% of
those users), education (49%) and work (33%) (DZS, ZTI-2025-1-2, published
8 Dec 2025). Search is still the larger channel, but AI answers are now a
real entry point, especially for younger users.

Search Console counts AI Overview and AI Mode appearances inside the normal
Performance report ("Web" search type); there is no separate filter. Google
reports clicks from pages with AI Overviews as higher quality on average
(Google's statement, not independent data).

## 2. What Google says about optimisation

From "AI features and your website" (Google Search Central):

- No additional requirements and no special optimisation are needed to
  appear in AI Overviews or AI Mode. The page must be indexed and eligible
  for a snippet.
- "You don't need to create new machine readable files, AI text files, or
  markup to appear in these features." No special schema.org markup either.
- Normal SEO applies: crawlable (robots.txt, CDN, firewall not blocking
  Googlebot), internal links, textual content, structured data that matches
  visible text, up-to-date Merchant Center and Business Profile data.
- Controls: `nosnippet`, `data-nosnippet`, `max-snippet`, `noindex` limit
  what is shown; `Google-Extended` controls use in some other Google AI
  systems but not Search.
- Google's spam policies now explicitly include attempts to manipulate
  generative AI responses in Search.

## 3. Writing passages that get quoted in Croatian

AI systems lift short, self-contained passages. In Croatian:

- **Answer first, in one or two sentences, in full grammar.** Put the
  question as a heading in natural Croatian (`Koliko košta najam stana u
  Zagrebu?`) and answer directly below: `Prosječna mjesečna najamnina za
  jednosobni stan u Zagrebu u listopadu 2026. iznosi ... € (izvor: ...).`
- **Name the subject in each passage.** Croatian drops pronouns and relies on
  case endings; a passage that starts `Ona se plaća ...` means
  nothing out of context. Write `Turistička pristojba plaća se ...`.
- **Numbers with dates and sources:** `2026.: ... €`, with a link to the
  primary source (Narodne novine, gov.hr, Porezna uprava, DZS, HNB).
- **Croatian terminology with the official term**, and the common variant
  once: `paušalni obrt (paušalist)`, `PDV (porez na dodanu vrijednost)`.
- **Lists and tables** for steps, prices and comparisons, with Croatian
  headers.
- **No Serbian forms or calques.** A model may answer Croatian users from a
  Serbian or Bosnian source if the Croatian page is weaker or unclear. Clear,
  standard Croatian helps the right page win. Apply
  `croatia:croatian-language`.
- **Keep facts current.** Out-of-date thresholds (HRK amounts, old tax rates)
  get repeated by AI and damage trust.

## 4. Entity consistency

- One name for the business everywhere (site, GBP, Apple Business, social
  profiles, directories, Wikipedia/Wikidata if applicable). Legal name as in
  sudreg or the obrtni registar, trading name as on signage.
- `Organization` / `LocalBusiness` JSON-LD with `sameAs` links to official
  profiles.
- An "O nama" (About) page that states who you are, where, since when, and
  what you do, in plain Croatian, plus an English version for foreign
  audiences.
- Mentions on trusted Croatian sites (local news portals, chambers, branch
  associations, municipalities, universities) help both search and AI
  systems associate the brand with the topic. Earn them; paid links must be
  `rel="sponsored"`.

## 5. llms.txt and similar files

- `llms.txt` is an informal proposal for a Markdown site summary for LLMs.
  Google says no AI text files are needed for its AI features; it has no
  effect on Google rankings or AI Overviews.
- Other assistants may or may not read it. Adding one is optional and cheap;
  if you do, write it in the site's main language (Croatian for a Croatian
  site, with English if the audience is international) and keep it in sync
  with the site.
- Do not block AI crawlers by accident (some CDNs and firewalls block them by
  default). Decide deliberately per crawler in robots.txt; blocking
  Googlebot also removes the site from AI Overviews.

## 6. Testing AI visibility in Croatian

- Ask the questions customers ask, in Croatian, with and without diacritics,
  in AI Mode, ChatGPT, Gemini, Copilot and Perplexity; note which sources
  are cited.
- Repeat in the main foreign languages for tourism businesses.
- Answers vary run to run: test several times and record the date. Track
  trends, not single answers.
