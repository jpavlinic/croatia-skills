# Dates, times, numbers, currency and units for hr / hr-HR

Read this when formatting or parsing dates, times, numbers, money, percentages or units in
Croatian, or when a test compares Intl/ICU output with expected strings.

All "observed" outputs below were produced on 2026-10-25 with **Node 22.22 (ICU 77.1, CLDR 47)**
and **Python Babel 2.18**; both agree unless noted. `⍽` marks U+00A0 NO-BREAK SPACE.
Other runtimes (older browsers, Java, .NET, Android) may use older CLDR data; re-check there.

## 1. Locale codes

| Code | Use |
|---|---|
| `hr` | Croatian language. Enough for most apps; Intl/ICU resolve it to Croatia data. |
| `hr-HR` | Croatian as used in Croatia. Use for `<html lang>` only if you also ship other `hr-*`; otherwise `lang="hr"` is fine. |
| `hr-BA` | Croatian in Bosnia and Herzegovina. Differs in CLDR: short date `25. 10. 26.`, currency KM (BAM). |
| `sr`, `bs`, `sh` | Not Croatian. Never fall back from `hr` to `sr`; fall back to `en` (or your default). `sh` is deprecated. |

- `<html lang="hr">` on Croatian pages; `lang="en"` on English ones (screen readers switch voice).
- hreflang values: `hr` or `hr-HR` (+ `x-default`). Full rules and URL strategy: `croatia:hr-seo-local`.
- `Accept-Language: hr-HR,hr;q=0.9,en;q=0.8` is typical; match on the primary subtag `hr`.

## 2. Dates

### What the norm says (IHJJ, *Hrvatski pravopis*, pravopis.hr, rules 8.1 Bjelina and 8.2 Točka)

- Ordinal numbers take a dot, so day and month numbers in a date take dots, **and so does the
  year**: `25. 10. 2026.` — with spaces between the parts (8.1 c: "između sastavnica nadnevka: 24. 12. 1998.").
- Written-out month: `25. listopada 2026.` (month name in the **genitive**, lowercase).
- Months and weekdays are written lowercase (siječanj, ponedjeljak). Capitalise only at the start of a
  sentence or heading.
- In running text the final dot of the year merges with the sentence-final dot:
  "Rok je 25. listopada 2026." (one dot). Before a comma it stays: "25. listopada 2026., a ...".
- Ambiguity: "do 15?" = 15 o'clock, "do 15.?" = the 15th (pravopis 8.2 f).

### Month names (observed Intl/Babel output)

| Nominative (standalone, `month:'long'` alone) | Genitive (in a date, `day` + `month:'long'`) | Abbrev. (`month:'short'`) |
|---|---|---|
| siječanj | siječnja | sij |
| veljača | veljače | velj |
| ožujak | ožujka | ožu |
| travanj | travnja | tra |
| svibanj | svibnja | svi |
| lipanj | lipnja | lip |
| srpanj | srpnja | srp |
| kolovoz | kolovoza | kol |
| rujan | rujna | ruj |
| listopad | listopada | lis |
| studeni | studenoga | stu |
| prosinac | prosinca | pro |

- `studenoga` is CLDR's choice; `studenog` is also standard. Do not "fix" one to the other in tests.
- CLDR abbreviations have **no dot** (`25. lis 2026.`). There is no official IHJJ month-abbreviation
  list; in prose prefer the full name or the numeric date.
- Weekdays: ponedjeljak, utorak, srijeda, četvrtak, petak, subota, nedjelja; short: pon, uto, sri,
  čet, pet, sub, ned; narrow: p, u, s, č, p, s, n.

### Getting genitive vs nominative right

ICU picks the grammatical form from the pattern, so **let the formatter build the whole string**:

```js
const d = new Date(2026, 9, 25);
new Intl.DateTimeFormat('hr', { day: 'numeric', month: 'long', year: 'numeric' }).format(d) // "25. listopada 2026."
new Intl.DateTimeFormat('hr', { month: 'long', year: 'numeric' }).format(d)                 // "listopad 2026."  (calendar header)
new Intl.DateTimeFormat('hr', { month: 'long' }).format(d)                                  // "listopad"
new Intl.DateTimeFormat('hr', { dateStyle: 'full' }).format(d)                              // "nedjelja, 25. listopada 2026."
```

Bug pattern: `day + '. ' + monthNames[m] + ' ' + year` with a nominative array gives
"25. listopad 2026" (wrong case, missing year dot). If you must assemble, keep two arrays
(nominative and genitive) or use `formatToParts`.

Python: `babel.dates.format_date(d, "d. MMMM y.", locale="hr")` → genitive;
`"LLLL y."` (stand-alone `L`) → `listopad 2026.`. `strftime("%B")` depends on the OS locale and is not
portable; do not use it for user-facing text.

### Styles (observed, date 2026-10-25 14:30 Europe/Zagreb, and 2026-03-03 09:05)

| Intl option | Output |
|---|---|
| `dateStyle:'full'` | `nedjelja, 25. listopada 2026.` |
| `dateStyle:'long'` | `25. listopada 2026.` / `3. ožujka 2026.` |
| `dateStyle:'medium'` | `25. lis 2026.` / `3. ožu 2026.` |
| `dateStyle:'short'` | `25. 10. 2026.` / **`03. 03. 2026.`** (zero-padded) |
| `{day:'numeric',month:'numeric',year:'numeric'}` | also `03. 03. 2026.` (CLDR pattern is `dd. MM. y.`) |
| `timeStyle:'short'` | `14:30` / `09:05` |
| `{hour:'numeric',minute:'2-digit'}` | `9:05` |
| `timeStyle:'full'` | `14:30:00 (srednjoeuropsko standardno vrijeme)` |
| `toLocaleString('hr-HR')` | `25. 10. 2026. 14:30:00` |
| `hr-BA` short | `25. 10. 26.` |

- IHJJ examples use no leading zeros (`3. 3. 2026.`). Zero-padded `03. 03. 2026.` is common on forms
  and in official documents and is not wrong, but if you want the pravopis look, build it yourself:
  `` `${d.getDate()}. ${d.getMonth() + 1}. ${d.getFullYear()}.` ``.
- **Parsing user input**: accept `25.10.2026`, `25. 10. 2026.`, `25.10.2026.`, `25/10/2026` and ISO
  `2026-10-25`; always day-month-year. Never parse `10/25/2026` as US for Croatian users.
- Store ISO 8601 (`2026-10-25`, UTC timestamps); format only at the edge. Time zone: `Europe/Zagreb`
  (CET/CEST).

### Time

- 24-hour clock only. Pravopis allows colon or dot between hours and minutes (`19:30`, `19.30`),
  no space around it (8.1 "Bjelina se ne nalazi" i). Intl uses the colon.
- With a unit: `u 14 h`, `u 14 sati`, `14.30 h` — with a space; never `14h`.
- `hour12:true` gives `02:30 PM`; never use it for hr.

### Date ranges

Observed `formatRange` with `{day:'numeric',month:'long',year:'numeric'}`:

| Range | Output |
|---|---|
| 25–28 Oct 2026 | `25. – 28. listopada 2026.` |
| 25 Oct – 3 Nov 2026 | `25. listopada – 03. studenoga 2026.` ← CLDR quirk: zero-padded `03.` |
| 28 Dec 2026 – 3 Jan 2027 | `28. prosinca 2026. – 03. siječnja 2027.` |

The zero-padding inside long-format ranges looks wrong to Croatian readers; format the two ends
separately (`fmt(a) + ' – ' + fmt(b)`, en dash with spaces) or post-process `formatRangeToParts`.
Pravopis: en dash with spaces between dates (8.1 f, "Posjeti: 15 – 17"); see `croatia:croatian-language`
for the house style on spaced vs unspaced dashes.

### Relative time (observed `Intl.RelativeTimeFormat('hr', {numeric:'auto'})`)

| Value | Output |
|---|---|
| -1 / -2 / 0 / 1 / 2 day | `jučer` / `prekjučer` / `danas` / `sutra` / `prekosutra` |
| -3, -5, -21, -22 day | `prije 3 dana`, `prije 5 dana`, `prije 21 dan`, `prije 22 dana` |
| 5 day | `za 5 dana` |
| -1, -3, -5 hour | `prije 1 sat`, `prije 3 sata`, `prije 5 sati` |
| 2, 21, 22 hour | `za 2 sata`, `za 21 sat`, `za 22 sata` |
| -1, -3, -5 minute | `prije 1 minutu`, `prije 3 minute`, `prije 5 minuta` |
| ±1 week / month / year | `prošli tjedan` / `sljedeći tjedan`, `prošli mjesec`, `prošle godine` / `sljedeće godine` |
| `numeric:'always'` -1 day | `prije 1 dan` (prefer `numeric:'auto'` → `jučer`) |
| `style:'short'` -3 hour | `prije 3 h` |

Plural agreement is already correct; do not hand-roll "prije X dana". Hand-rolled strings are the
classic source of "prije 21 dana" / "prije 2 dan" bugs.

### Weeks

- Week starts on **Monday** (observed `new Intl.Locale('hr-HR').getWeekInfo()` →
  `{firstDay:1, weekend:[6,7], minimalDays:1}`).
- CLDR gives `minimalDays: 1` for HR, so "locale week numbers" differ from ISO 8601 (which needs 4).
  Croatian business practice uses ISO weeks: compute with an ISO function (`date-fns/getISOWeek`,
  Python `date.isocalendar()`), not with locale week data.
- Holidays and working days: `croatia:hr-calendar`.

## 3. Numbers

### Norm vs CLDR

| Aspect | IHJJ pravopis (8.1 h, 8.2 c–d) | CLDR / Intl `hr` (observed) |
|---|---|---|
| Decimal separator | comma `1,41` | comma `1.234,56` |
| Thousands, numbers ≥ 10 000 | **space** `10 000`, `859 343 286`; dot allowed in financial texts `10.000` | dot `12.345` |
| Thousands, 4-digit numbers | no separator `5331` (space allowed in mathematics) | dot `1.234` |
| Negative | hyphen/en dash in print | **U+2212 MINUS SIGN** `−5` |

- Both the dot (CLDR default, accepted in finance) and a no-break space (pravopis basic rule) are
  correct for ≥ 10 000. Follow the project's existing convention; otherwise CLDR output is acceptable.
- Pravopis-style output in JS: `new Intl.NumberFormat('hr', { useGrouping: 'min2' })` gives
  `1234` and `12.345` (observed); then replace `.` with U+00A0 if you want spaces.
- **Never** use a plain space as group separator in HTML: the number can wrap. Use U+00A0 (or U+202F).
- **Parsing**: users type `1.234,56`, `1234,56`, `1 234,56`, sometimes `1234.56`. Strip spaces/NBSP/dots
  used as grouping, then treat the comma as decimal. If a string has only a dot and exactly three
  digits after it (`1.234`) it is ambiguous; prefer locale-aware parsing and validate ranges.
- Tests that compare formatted strings must include U+00A0 and U+2212 exactly, or normalise first.

### Currency (euro since 1 January 2023)

- Croatia's currency is the **euro** since 2023-01-01; fixed conversion rate **1 € = 7,53450 kn**
  (Council Regulation (EU) 2022/1208; *Zakon o uvođenju eura kao službene valute u Republici Hrvatskoj*,
  NN 57/2022; euro.hr). Mandatory dual display (€ + kn) ran from 5 September 2022 00:00 to
  31 December 2023 24:00 (*Odluka o objavi uvođenja eura kao službene valute u Republici Hrvatskoj*,
  NN 85/2022, point II) and has **ended** — do not add new dual-display UI.
- Kuna (HRK) is only for historical data: keep stored HRK amounts as HRK with their date, convert
  with the fixed rate and round to cents only for display/reporting (conversion rules: same act).
- Observed Intl output:

| Call | Output |
|---|---|
| `NumberFormat('hr-HR',{style:'currency',currency:'EUR'}).format(1234.56)` | `1.234,56⍽€` |
| same, `5` | `5,00⍽€` |
| same, `-1234.5` | `−1.234,50⍽€` (U+2212) |
| `currencyDisplay:'code'` | `1.234,56⍽EUR` |
| `currencyDisplay:'name'`, 1234.56 / 2 / 5 | `1.234,56 eura` / `2,00 eura` / `5,00 eura` |
| `currency:'HRK'` | `1.234,56⍽kn`, name: `1.234,56 hrvatskih kuna` |
| `en-US` EUR (for contrast) | `€1,234.56` |

- Croatian order is **amount, space, symbol**: `1.234,56 €` / `99,90 €` (pravopis 8.1 m). The English
  `€1,234.56` pattern in a Croatian UI is a localisation bug (usually a hard-coded `'€' + amount`).
- Whole euro amounts: `5 €` or `5,00 €` are both fine; be consistent per screen (prices on shelf
  labels/checkout usually show cents). Invoices and fiscal receipts: `croatia:hr-fiscalization-dev`.
- Word forms: 1 euro, 2–4 eura, 5+ eura; "euro" does not change in the genitive plural
  (`5 eura`, `21 euro`, `22 eura`). Cents: `1 cent, 2 centa, 5 centi`. Use plural rules (plurals.md).

### Percent, units, compact

| Call | Output |
|---|---|
| `{style:'percent'}` 0.25 | `25⍽%` (pravopis 8.1 l: `50 %`, with a space) |
| `{style:'unit',unit:'kilometer'}` 5 | `5 km` (**regular U+0020 space** — can wrap; swap for NBSP in HTML) |
| `unitDisplay:'long'` 5 / 2 / 21 km | `5 kilometara` / `2 kilometra` / `21 kilometar` |
| `unit:'celsius'` 25 | `25 °C` |
| `notation:'compact'` 1500 / 1 500 000 | `1,5⍽tis.` / `1,5⍽mil.` |
| `compactDisplay:'long'` 1.5M / 2M / 5M | `1,5 milijuna` / `2 milijuna` / `5 milijuna` |

- Units and currency are separated by a space (pravopis 8.1 k, m): `5 km`, `3 kg`, `220 V`, `99,90 €`;
  no space for `°` angles, `+5`, `–5`, and none in `50 m/s`.
- Multiplication sign and other typography: `croatia:croatian-language`.

### Lists and display names (observed)

- `new Intl.ListFormat('hr').format(['Zagreb','Split','Rijeka'])` → `Zagreb, Split i Rijeka`
  (no serial comma before `i`); disjunction → `Zagreb ili Split`.
- `Intl.DisplayNames('hr',{type:'language'}).of('hr')` → `hrvatski`; region `HR` → `Hrvatska`;
  currency `EUR` → `euro`. Language/region names are lowercase/uppercase as in prose
  (language names lowercase: "hrvatski", "engleski").

## 4. Python specifics

- Babel (`pip install babel`) gives the same CLDR data as Intl (observed identical date/number output).
- `locale.setlocale(LC_ALL, 'hr_HR.UTF-8')` + `strftime`/`locale.currency` worked on macOS
  (`nedjelja 25. listopada 2026.`, `1.234,56 €`), but **`locale.strxfrm` sorting was wrong on macOS**
  (č/š/ž ordered at the start). Locale availability differs per server/container; do not depend on
  OS locales in production code.
