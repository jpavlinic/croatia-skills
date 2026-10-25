---
name: hr-localization
description: >-
  Implementing Croatian (hr, hr-HR) correctly in software: i18n/l10n setup, hr.json /
  messages/hr.* / hr.po / values-hr review, Intl and ICU date, time, number, euro and percent
  formatting, CLDR plural forms (one/few/other, Plural-Forms header), ICU MessageFormat, grammatical
  case and gender in UI strings, name declension and vocative in greetings, place names with u/na,
  Croatian collation (č ć dž đ lj nj š ž; Intl.Collator, PostgreSQL hr-HR-x-icu, MySQL
  utf8mb4_croatian_ci), diacritics folding for search, slugs (đ → d or dj), NFC, mojibake
  (Windows-1250, ISO-8859-2), address and phone display. Triggers: "Croatian locale", "hr-HR",
  "i18n", "translation file", "plural", "Intl", "date format", "euro format", "sorting č ć",
  "slugify", "diacritics", "lokalizacija", "prijevod sučelja", "množina", "padeži", "vokativ",
  "deklinacija imena", "u ili na", "abecedni redoslijed", "kvačice", "dijakritici", "format datuma".
---

# Croatian in code and data (hr / hr-HR)

How to make software handle Croatian correctly: formatting, plurals, inflected names and places,
sorting, search, slugs, encodings, addresses. This skill is about **code and data**; the wording,
spelling and tone of Croatian text are covered by `croatia:croatian-language` — apply both whenever
Croatian UI strings are written.

Status: researched 2026-10-25. Runtime behaviour verified on Node 22.22 (ICU 77.1, CLDR 47),
Python 3.14 + Babel 2.18, PostgreSQL 18.6 (ICU) and a local MySQL server; norms from IHJJ
(*Hrvatski pravopis*, pravopis.hr; *Etnici i ktetici*, hrvatski.hr) and Hrvatska pošta.

## How to use

1. Identify the stack (Intl/ICU, i18next, next-intl, Django, Rails, SQL engine…) and the task.
2. Load only the reference you need:

| Task | Reference | Grep hints |
|---|---|---|
| Dates, months (genitive vs nominative), time, ranges, relative time, weeks, numbers, euro, %, units | `references/dates-numbers.md` | `Month names`, `Getting genitive`, `formatRange`, `RelativeTime`, `Currency`, `min2` |
| Plural rules, framework config, Plural-Forms header, common bugs, tests | `references/plurals.md` | `CLDR rule`, `Framework configuration`, `Common bugs`, `Trailing zeros` |
| Case and gender in templates, name declension, vocative in greetings | `references/names-vocative.md` | `concatenation`, `Gender agreement`, `Vocative`, `Safe patterns` |
| Place names: u/na, genitive, from-forms, ethnics, counties | `references/places.md` + `assets/toponyms.csv` | `u or na`, `Direction`, `Counties` |
| Sorting, DB collations, search folding, slugs, NFC, digraph code points, mojibake, keyboards | `references/collation-search.md` | `Observed results`, `PostgreSQL`, `MySQL`, `folding`, `Slugs`, `mojibake` |
| Framework setup, hr message-file review checklist, typical bugs | `references/frameworks.md` | `Setup per stack`, `checklist`, `Typical bugs` |
| Address format, form fields, phone display | `references/addresses-forms.md` | `Hrvatska pošta`, `form fields`, `Phone` |

3. Use the script for deterministic work instead of reasoning it out:

```bash
python3 scripts/hr_text.py plural 22 dan dana dana        # 22 dana
python3 scripts/hr_text.py slugify "Šibenik – Đakovo" [--dj] # sibenik-dakovo / sibenik-djakovo
python3 scripts/hr_text.py fold "Ćevapčići"                  # cevapcici
python3 scripts/hr_text.py sort names.txt                    # Croatian alphabetical order
python3 scripts/hr_text.py fix-mojibake "Å¡kola" [--legacy]  # škola
python3 scripts/hr_text.py vocative Petar --gender m         # Petre (falls back when unsure)
python3 scripts/hr_text.py greeting --first Ana --last Kovač --gender f   # Poštovana gospođo Kovač,
python3 scripts/hr_text.py place Hvar                        # u Hvaru (town) / na Hvaru (island)
python3 scripts/hr_text.py --self-test
```

The functions are importable (`from hr_text import plural, fold, slugify, sort_key, fix_mojibake,
vocative, greeting, place`) — port them to the project's language if needed, together with the tests.

4. When reviewing a project, report concrete `file:line` findings and the fix; follow the project's
   existing conventions (e.g. dot vs space thousands separator, đ → d vs dj in slugs) where the norm
   allows both.

## Quick reference

### Locale and markup

| Item | Value |
|---|---|
| Locale id | `hr` (or `hr-HR`); `hr-BA` = Croatian in Bosnia and Herzegovina |
| Fallback | `en` (or your default) — **never** `sr`/`bs` |
| HTML | `<html lang="hr">`; hreflang `hr`/`hr-HR` → details in `croatia:hr-seo-local` |
| Time zone | `Europe/Zagreb` |
| Week | Monday first; use ISO 8601 week numbers (CLDR `minimalDays` for HR is 1) |
| Clock | 24-hour |
| Currency | EUR since 2023-01-01; 1 € = 7,53450 kn (fixed); kuna only for historical data |

### Formatting (observed Intl output; ⍽ = U+00A0 no-break space)

| What | Code | Output |
|---|---|---|
| Long date | `{day:'numeric', month:'long', year:'numeric'}` | `25. listopada 2026.` (genitive) |
| Calendar header | `{month:'long', year:'numeric'}` | `listopad 2026.` (nominative) |
| Full date | `{dateStyle:'full'}` | `nedjelja, 25. listopada 2026.` |
| Short date | `{dateStyle:'short'}` | `25. 10. 2026.` — but `03. 03. 2026.` (zero-padded; pravopis style is `3. 3. 2026.`) |
| Time | `{timeStyle:'short'}` | `14:30` (pravopis also allows `14.30`; with unit `14 h`) |
| Range | `formatRange` | `25. – 28. listopada 2026.`; cross-month gives `03. studenoga` (zero-pad quirk) |
| Relative | `RelativeTimeFormat('hr',{numeric:'auto'})` | `jučer`, `prije 3 dana`, `prije 21 dan`, `za 2 sata`, `prije 5 minuta` |
| Number | `NumberFormat('hr')` | `1.234.567,891`; negative uses U+2212 `−5` |
| Pravopis grouping | `{useGrouping:'min2'}` | `1234`, `12.345` (IHJJ: space for ≥ 10 000, dot allowed in finance) |
| Euro | `{style:'currency', currency:'EUR'}` | `1.234,56⍽€` (not `€1,234.56`) |
| Percent | `{style:'percent'}` | `25⍽%` (space, per IHJJ) |
| Unit | `{style:'unit', unit:'kilometer'}` | `5 km` (plain space — use NBSP in HTML) |
| List | `ListFormat('hr')` | `Zagreb, Split i Rijeka` |

Months: siječanj, veljača, ožujak, travanj, svibanj, lipanj, srpanj, kolovoz, rujan, listopad,
studeni, prosinac (genitive: siječnja … listopada, studenoga, prosinca). Lowercase, like weekdays
(ponedjeljak … nedjelja). The year in a date takes a dot: `25. 10. 2026.`

### Plurals (CLDR hr: one / few / other)

| n | Category | Noun | Example |
|---|---|---|---|
| 1, 21, 31, 101, 121 (not 11, 111) | one | nominative sg. | *21 dan, 21 poruka* |
| 2–4, 22–24, 102 (not 12–14) | few | genitive sg. | *22 dana, 3 poruke* |
| 0, 5–20, 25–30, 11–14, 111–114, 1.5 | other | genitive pl. | *25 dana, 11 poruka* |
| decimals: f ends in 1 (not 11) → one; 2–4 (not 12–14) → few | | | `1.1` one, `0.2` few, `"1.0"` other |

```text
{count, plural, one {# nova poruka} few {# nove poruke} other {# novih poruka}}
```

gettext: `nplurals=3; plural=(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2);`
i18next: `key_one`, `key_few`, `key_other`. Test with 0, 1, 2, 5, 11, 12, 21, 22, 25, 101, 111, 1.5.

### Grammar in templates

- Never concatenate translated fragments; translate whole sentences with ICU `plural`/`select`.
- Insert variables as labels in the nominative (`Grad: Split`, `Pošiljatelj: Ana Horvat`), or use
  stored inflected forms.
- Gender: past tense and adjectives agree (*prijavio / prijavila*). Use ICU `select`, the polite
  plural *Vi* form (*Jeste li sigurni?*), or neutral rewrites (*Prijava je uspjela.*).
- Greetings: *Poštovani gospodine Horvat,* · *Poštovana gospođo Kovač,* · unknown gender *Poštovani,*
  · informal *Dragi Ivane,* / *Draga Ana,*. Female names and all female surnames stay in the
  nominative; male surnames after *gospodine* may stay in the nominative (current usage; textbook
  *Babiću* also correct). Only decline first names you are sure of (`vocative` helper).

### Places

| Rule | Examples |
|---|---|
| Towns: **u** + locative | u Zagrebu, u Splitu, u Rijeci, u Puli, u Osijeku, u Dubrovniku, u Zadru |
| Islands: **na** + locative | na Hvaru, na Krku, na Rabu, na Braču, na Pagu |
| Same-name town vs island | u Hvaru (town) / na Hvaru (island); also Krk, Rab, Pag, Cres, Vis, Korčula, Lastovo |
| From: **iz** / **s(a)** + genitive | iz Zagreba, iz Rijeke; s Hvara, s Krka, sa Šolte |
| Ethnics | Zagrepčanin/Zagrepčanka, Splićanin, Riječanin, Osječanin, Puljanin, Zadranin |

236 places (all 128 cities incl. county seats, major islands, regions, tourist places) with genitive,
locative, from-form and IHJJ ethnics: `assets/toponyms.csv`.

### Sorting and search

| Need | Use |
|---|---|
| Alphabet | a b c č ć d dž đ e f g h i j k l lj m n nj o p r s š t u v z ž |
| JS | `new Intl.Collator('hr').compare` (reuse the instance) |
| PostgreSQL | `COLLATE "hr-HR-x-icu"`; case-insensitive: ICU `hr-HR-u-ks-level2`, `deterministic=false` |
| MySQL | `utf8mb4_hr_0900_ai_ci` or `utf8mb4_croatian_ci` (correct order; c ≠ č) |
| Python | PyICU, or `hr_text.sort_key` (stdlib); not `locale.strxfrm` |
| Search | fold č ć→c, š→s, ž→z, đ→d **and** dj; store a folded, indexed column |
| Slugs | same folding; pick d or dj and keep it; never change published slugs without 301 |
| Input hygiene | NFC; replace U+01C4–U+01CC (ǆ ǉ ǌ…) with two letters; keep user's diacritics in stored names |
| Mojibake | `Å¡`→š, `Ä\x8d`→č, `Ä‡`→ć, `Ä‘`→đ, `Å¾`→ž (UTF-8 read as cp1252); `è æ ð`→č ć đ (cp1250 read as cp1252, opt-in) |

### Addresses and phones

- `Ilica 1, 10000 Zagreb` — street + house number, postal code + place; `bb` = *bez broja*;
  settlement line only when it differs from the post office (Hrvatska pošta).
- Fields: *Ulica i kućni broj*, *Poštanski broj*, *Mjesto/Grad*, optional *Kat, stan*; county rarely
  needed (21 counties incl. Grad Zagreb in places.md).
- Phones: display `01 234 5678`, `021 123 456`, `091 234 5678` / `+385 91 234 5678`; store E.164.
  Validation → `croatia:hr-identifiers`.

## Rules that cover most cases

1. Let Intl/ICU/Babel format dates, numbers and currency with locale `hr`; never assemble
   `day + month name` or `'€' + amount` by hand.
2. Every counted string has one/few/other; check `hr.json` for missing `few`.
3. No string concatenation around variables; whole sentences, ICU select/plural.
4. Don't auto-decline names or unknown places; use labels, stored forms, or the conservative helper.
5. Sort with a Croatian collation; search on folded keys with both đ spellings.
6. Normalise all text input to NFC; repair or reject mojibake at import.
7. Tests compare formatted strings with exact U+00A0 / U+2212, or normalise them first.

## Related skills

`croatia:croatian-language` (wording, spelling, UI glossary, e-mail etiquette) ·
`croatia:hr-identifiers` (OIB, IBAN, phone, postal code validation) · `croatia:hr-calendar`
(holidays, working days) · `croatia:hr-seo-local` (hreflang, slugs and diacritics for SEO) ·
`croatia:hr-fiscalization-dev` (invoice/receipt amounts and formats) ·
`croatia:hr-legal-compliance` (personal data in forms, language-law aspects).

## Keeping current

| Fact | Changes when | Check |
|---|---|---|
| Intl/ICU outputs (zero-padding, separators, month forms) | CLDR release (twice a year), browser/Node upgrade | re-run the snippets in `references/dates-numbers.md` on the target runtime; cldr.unicode.org |
| Plural rules for hr | rarely | CLDR `plurals.xml`; `Intl.PluralRules('hr').resolvedOptions()` |
| Pravopis rules (spacing, dates, numbers) | new IHJJ edition | pravopis.hr |
| Toponym forms and ethnics | IHJJ updates | hrvatski.hr/etnici-i-ktetici; resolve **VERIFY** rows in `assets/toponyms.csv` |
| List of cities/counties | amendments to *Zakon o područjima županija, gradova i općina* | narodne-novine.nn.hr |
| DB collations | PostgreSQL/MySQL major versions | engine release notes |

Per-project choices (thousands separator, đ convention, formal/informal address, vocative table
overrides, extra toponyms) belong in the user's project, e.g. `.claude/croatia/hr-localization.md`
or a project data file — not in this plugin's files.
