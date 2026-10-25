---
name: hr-seo-local
description: >-
  SEO and discoverability for the Croatian market and Croatian-language sites:
  keyword research in an inflected language (padeži, singular/plural), queries
  typed without diacritics (cevapi/ćevapi, đ as d or dj), on-page in Croatian,
  slugs, lang="hr", hreflang hr / hr-HR / x-default, .hr vs .com, /en/ /de/
  tourism versions, diaspora and regional markets (SI, BA, RS, ME), local SEO,
  Google Business Profile in Croatia, NAP and citations from Croatian
  directories, city pages with the right locative (u Splitu / na Hvaru), and AI
  Overviews / AI Mode / ChatGPT answers in Croatian. Triggers: "SEO Hrvatska",
  "Croatian SEO", "ključne riječi", "istraživanje ključnih riječi",
  "pretraživanje", "Google Hrvatska", "hreflang hr", ".hr domena", "lokalni
  SEO", "Google Business Profile Hrvatska", "Google moja tvrtka", "dijakritici",
  "citati", "imenici tvrtki", "NAP", "SEO za apartmane", "SEO za obrt", or any
  SEO, content or analytics task on a .hr site or hr locale.
---

# Croatian SEO and local discoverability

Helps plan, audit and write for search in the Croatian market: Croatian query
behaviour, keyword research, on-page and international setup, local SEO, and
AI answer engines. Generic SEO knowledge is assumed. This skill adds what is
specific to Croatia and to the Croatian language.

Status: researched 2026-10-25.

SEO itself is not a regulated topic. The parts that touch law (cookie consent
for analytics, impressum and OIB on the site, comparative claims, reviews) are
covered by `croatia:hr-legal-compliance`. Hand those questions to that skill,
and its disclaimer rules apply there.

## How to use

Work through these steps. Load a reference only when you reach its step.

1. **Audience and locale.** Who searches (people in Croatia, diaspora,
   foreign tourists, the regional ex-Yugoslav market)? Which languages and
   countries? Which domain and URL structure? → `references/international-regional.md`
2. **Keyword variants.** Start from seeds, then expand: inflected forms,
   singular/plural, with and without diacritics, u/na + locative for places,
   anglicisms and regional words. Check each in the SERP and group variants
   that share a SERP onto one page. → `references/keyword-research-croatian.md`,
   `scripts/kw_variants.py`
3. **Page plan.** One page per search intent, not one per inflected form or per
   town without unique substance (doorway risk).
4. **On-page.** Croatian titles and meta in sentence case, slugs, `lang`,
   hreflang, EUR prices, Croatian dates and addresses, LocalBusiness JSON-LD
   with Croatian holidays. → `references/on-page-hreflang-slugs.md`
5. **Local.** Google Business Profile, NAP that matches the official register,
   citations, reviews, city and island pages. → `references/local-seo-citations.md`
6. **AI answers.** Quotable Croatian passages, entity consistency, crawler
   access. → `references/ai-search-croatian.md`
7. **Measure.** Search Console first (first-party data), analytics only with
   consent. Market context and dated numbers. → `references/market-data.md`

If a Search Console, analytics or other SEO tool is available in the session,
use the project's own property for real queries, impressions and positions,
and treat that data as more reliable than third-party estimates. Never query
another site's property.

| Need | File | Grep hints |
|---|---|---|
| Inflection, diacritics, dialect, anglicisms, method, volumes | `references/keyword-research-croatian.md` | `Padeži`, `Diacritics`, `Method`, `Grouping`, `Regional` |
| Titles, meta, slugs, lang, hreflang, schema, dates, prices | `references/on-page-hreflang-slugs.md` | `Titles`, `Slugs`, `hreflang`, `LocalBusiness`, `holidays` |
| GBP, NAP, registers, citations list, reviews, city pages | `references/local-seo-citations.md` | `GBP`, `NAP`, `Citations`, `Reviews`, `City pages`, `Tourism` |
| .hr rules, ccTLD vs gTLD, /en/ /de/, SI/BA/RS/ME, diaspora | `references/international-regional.md` | `.hr`, `Structure`, `Regional`, `Diaspora` |
| AI Overviews / AI Mode availability, ChatGPT, passages, llms.txt | `references/ai-search-croatian.md` | `Availability`, `Passages`, `Entity`, `llms.txt` |
| Search engine, device, browser shares, internet use, AI use | `references/market-data.md` | `Search engines`, `Devices`, `Browsers`, `DZS` |
| All sources with access dates | `references/sources.md` | |

Related skills in this plugin:

- `croatia:croatian-language`: every Croatian sentence you write (titles, meta,
  FAQ, GBP descriptions). No machine-translated text goes live without it.
- `croatia:hr-localization`: slug transliteration, diacritic folding rules,
  place-name forms (u/na, locative), plural forms in UI.
- `croatia:hr-legal-compliance`: cookie consent for GA4 and ad tags,
  impressum and OIB on the site, comparative advertising, fake reviews.
- `croatia:hr-calendar`: holidays for opening hours, seasonality.
- `croatia:hr-market-brands`: Croatian marketplaces, directories and portals.
- `croatia:hr-tourism-rentals`: rental-specific rules (categorisation,
  tourist tax) that tourism pages must state correctly.
- `croatia:hr-identifiers`: OIB, MBS, IBAN validation when they appear on pages.

## Core rules (cover most cases)

1. **Google is the market.** 94.11% of searches in Croatia (StatCounter,
   September 2026), Bing 3.77%. Optimise for Google; keep Bing Webmaster Tools
   as a cheap extra.
2. **Users type without diacritics.** Plan for `cevapi`, `racunovodja`,
   `zlicarna`. Google usually connects the forms, but the SERPs can differ.
   Check both spellings in the SERP and in Search Console. Always write the
   content with correct diacritics; never misspell on purpose.
3. **Inflection splits volume.** `stan zagreb`, `stanovi zagreb`, `najam
   stana zagreb` and `stan u zagrebu` are one topic. One strong page with
   natural use of several forms beats one page per form.
4. **Volumes are small.** Croatia has about 3.9 million people. Most long-tail
   terms show "0–10" in Keyword Planner. Use Search Console, Google Trends
   (region Croatia), autocomplete and the SERP itself rather than discarding
   low-volume terms.
5. **Sentence case** for Croatian titles and headings: `Najam stanova u
   Zagrebu`, not `Najam Stanova U Zagrebu`. Months and weekdays lower case.
6. **Slugs:** lower case, diacritics folded, hyphens. Pick one rule for đ
   (`d` or `dj`) per site and never change it on live URLs. Rules in
   `croatia:hr-localization`.
7. **Language signals:** `<html lang="hr">`. Google detects language from the
   visible text and does not use `lang` or hreflang for that. Hreflang only
   links language/region versions. Use `hr` (or `hr-HR` when a separate
   `hr-BA` exists), `x-default` for the selector or fallback, and keep
   annotations reciprocal.
8. **Never relabel Croatian as `sr`, `bs` or `sl`.** Each market needs its own
   real localisation, or nothing.
9. **Local NAP = official register.** The business name, address and phone
   on the site, GBP and directories must match each other, and the legal name
   must match sudreg or the obrtni registar. The trading name can be shown
   alongside it.
10. **City and island pages need unique substance** (service area facts,
    prices, staff, photos, local FAQs). Templates that only swap the town name
    are doorway abuse in Google's spam policies. Use the correct locative:
    `u Splitu`, `na Hvaru`, `na Krku`, `u Rijeci`.
11. **Analytics needs consent in Croatia.** There is no statutory analytics
    exemption (ZEK čl. 43. st. 4.), so GA4 fires only after consent. Expect
    gaps in analytics; Search Console is unaffected. → `croatia:hr-legal-compliance`
12. **AI Overviews and AI Mode work in Croatia and in Croatian** (Google help
    pages, checked 2026-10-25). They need no special markup or files; normal
    SEO plus clear, quotable Croatian passages is the method.

## Quick table: Croatian SEO pitfalls

| Pitfall | Why it hurts | Fix |
|---|---|---|
| Separate page per inflected form (`stan-zagreb`, `stanovi-zagreb`) | Cannibalisation, thin pages | One page; use forms naturally in title, H1, body |
| Content written without diacritics to "match queries" | Looks unprofessional, hurts trust; Google folds anyway | Correct Croatian in content; check unaccented queries in the SERP |
| Title Case In Croatian Titles | Wrong by Croatian orthography; reads as translated | Sentence case |
| Machine-translated pages | Low quality, calques, Serbian forms | Human edit with `croatia:croatian-language` |
| Croatian text labelled `sr`/`bs` to "reach the region" | Duplicate, wrong language signal | Separate real localisation, or target the region with Croatian `hr` + `hr-BA` |
| Doorway city pages (`vodoinstalater-[grad]` ×100) | Spam policy: doorway, scaled content | Few pages with unique local substance; service-area in GBP |
| Wrong locative (`u Hvaru`, `na Splitu`) | Natives notice at once | Check u/na with `croatia:hr-localization` |
| NAP differs from sudreg/obrtni registar | Weak local signals, verification trouble | Copy the legal name and address from the register |
| Auto-redirect by IP or browser language | Google may not crawl other versions | Language switcher links; hreflang; no forced redirects |
| `hreflang="hr-HR"` with no `x-default` or no return links | Annotations ignored | Reciprocal sets, self-reference, `x-default` |
| `.hr` and `.com` copies of the same Croatian site | Duplicate content | One canonical domain; redirect the other |
| GA4 loading before consent | Unlawful under ZEK čl. 43 | Consent first; read Search Console for SEO |
| Prices in HRK or "kn" | Euro since 1 Jan 2023; outdated content | EUR only, Croatian number format |
| Opening hours ignore Croatian holidays | Wrong info in Maps on 14 public holidays | GBP special hours + schema with `validFrom`/`validThrough` |
| Listing in dead or repurposed directories | Bad neighbourhood links | Use the verified list in `local-seo-citations.md` |

## Checklists

**New Croatian site or section**
- [ ] Audience, languages, countries decided; domain and URL structure chosen
- [ ] Seed list expanded (forms, plural, no-diacritics, locatives, anglicisms)
- [ ] SERP checked for each cluster; one page per intent
- [ ] Titles and meta in Croatian sentence case, edited by a native or with `croatia:croatian-language`
- [ ] Slugs folded, one đ rule; `lang="hr"`; hreflang sets reciprocal with `x-default`
- [ ] EUR prices, Croatian dates (`25. listopada 2026.`), Croatian address format
- [ ] Organization or LocalBusiness JSON-LD matches visible text and the register
- [ ] Impressum data on the site (`croatia:hr-legal-compliance`)
- [ ] Search Console property verified, sitemap submitted; Bing Webmaster Tools optional
- [ ] Consent banner gates analytics and ad tags

**Local business**
- [ ] GBP claimed and verified; primary category is the closest match
- [ ] NAP identical on site, GBP, Apple Business, Bing Places and directories
- [ ] Legal name matches sudreg / obrtni registar
- [ ] Special hours set for every Croatian public holiday of the year
- [ ] Review request flow in place (no incentives, no gating)
- [ ] City or island pages only where the business really operates, with unique content

## Keeping current

| Fact | Changes | Check |
|---|---|---|
| Search engine, device, browser shares | Monthly | gs.statcounter.com (Croatia) |
| AI Overviews / AI Mode countries and languages | Any time | support.google.com/websearch/answer/14901683 and /16011537 |
| .hr registration rules, registrar list | Rarely | domene.hr (FAQ, registrar list, Pravilnik NN 83/2023) |
| GBP verification options | Often | support.google.com/business/answer/7107242 |
| Apple Business (ex Business Connect) features in Croatia | Any time | support.apple.com/guide/business (feature availability) |
| Directory list | Sites close or change owner | Open each URL before recommending it |
| Internet and AI use in Croatia | Yearly (DZS release in December) | podaci.dzs.hr, Eurostat `isoc_ci_ifp_iu` |
| Analytics consent rules | EU Digital Omnibus pending | `croatia:hr-legal-compliance` |

Per-project notes (chosen đ rule, target locales, citation log) belong in the
user's project, for example `.claude/croatia/hr-seo-local.md`, not in this
skill.
