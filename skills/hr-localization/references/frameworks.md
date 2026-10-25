# i18n frameworks and hr message files: setup, patterns, review checklist

Read this when adding Croatian to an app, reviewing `hr.json` / `messages/hr.*` / `hr.po` /
`hr.yml` / `strings.xml (values-hr)`, or when a PR touches Croatian translations. Wording of the
strings themselves (UI glossary, tone, Vi/ti) → `croatia:croatian-language`.

## 1. Setup per stack

| Stack | Locale id | Notes |
|---|---|---|
| next-intl / Next.js App Router | `hr` | ICU messages; `formatter.dateTime`, `formatter.number` use Intl; set `timeZone: 'Europe/Zagreb'` to avoid server/client mismatch |
| react-intl / FormatJS | `hr` | ICU; older targets need `@formatjs/intl-pluralrules` + `/locale-data/hr` |
| i18next / react-i18next | `hr` | JSON v4 keys `_one/_few/_other`; `fallbackLng: 'en'` (never `sr`/`bs`) |
| vue-i18n | `hr` | add custom `pluralRules.hr` (default rule is not Slavic); `datetimeFormats`/`numberFormats` per locale |
| Angular | `hr` | `registerLocaleData(localeHr)` from `@angular/common/locales/hr`; `LOCALE_ID` `'hr'`; ICU plural/select in templates |
| Django | `hr` | `LANGUAGE_CODE = 'hr'`, `USE_I18N = True`, `.po` with the Plural-Forms header (plurals.md); `USE_THOUSAND_SEPARATOR` uses Django's hr formats (check output) |
| Rails | `:hr` | `rails-i18n` gem (plural keys one/few/other); `I18n.l(date, format: :long)` |
| Laravel | `hr` | `lang/hr/*.php` or `lang/hr.json`; `trans_choice` uses its own Slavic rule set — test 21/22/25 |
| Android | `values-hr/` | `<plurals>` one/few/other |
| iOS | `hr.lproj`, String Catalog | one/few/other |
| Java | `Locale.forLanguageTag("hr-HR")` | use ICU4J for MessageFormat plurals; `java.text.Collator.getInstance(hr)` |
| .NET | `CultureInfo("hr-HR")` | ICU-based on .NET 5+ (Linux/macOS); check `NumberFormatInfo` group separator in tests |

Server rendering: format dates/numbers on one side, or both sides with the same locale, time zone and
ICU version. Node and browsers ship different ICU versions; avoid snapshot tests that depend on exact
whitespace (U+00A0 vs U+202F) unless you normalise.

## 2. Message patterns that work in Croatian

```json
{
  "cart.items": "{count, plural, one {# proizvod} few {# proizvoda} other {# proizvoda}}",
  "cart.summary": "{count, plural, one {U košarici je # proizvod.} few {U košarici su # proizvoda.} other {U košarici je # proizvoda.}}",
  "order.shipped": "Narudžba {orderId} je poslana.",
  "comment.new": "{gender, select, male {{name} je komentirao.} female {{name} je komentirala.} other {Novi komentar: {name}}}",
  "delivery.city": "Dostava: {city}",
  "greeting.formal.unknown": "Poštovani,",
  "date.deadline": "Rok: {deadline, date, long}"
}
```

- `{deadline, date, long}` → *25. listopada 2026.*; never `"Rok: " + day + ". " + monthName`.
- Keep punctuation inside the message; Croatian ends the date with a dot, so a following sentence dot
  merges ("Rok je 25. listopada 2026."). Watch for double dots when a template adds its own:
  `"Rok je {deadline}."` with a formatted `25. 10. 2026.` → `2026..`.

## 3. Review checklist for hr message files

Language quality is covered by `croatia:croatian-language`; this list is about i18n mechanics.

1. **Plural branches**: every count message has `one`, `few`, `other` (i18next: `_one/_few/_other`).
   Grep for keys that exist with `_one` and `_other` but not `_few`.
2. **No concatenation** in code around translated fragments (`t('you_have') + n + t('items')`).
3. **Case of inserted values**: variables appear as labels or subjects in nominative; places use stored
   inflected forms (places.md); names not declined unless via a tested helper (names-vocative.md).
4. **Gender**: strings that mention the user/sender in the past tense have a `select` or a neutral
   rewrite.
5. **Sentence case**, not English Title Case: *Postavke računa*, not *Postavke Računa*. Machine-
   translated files and copy-pasted English keys often keep title case.
6. **Capitalisation of months, weekdays, languages, nationalities-as-adjectives**: lowercase
   (*listopad, ponedjeljak, hrvatski*).
7. **Number/date/currency formatting via Intl/ICU**, not hard-coded strings: grep for `'€'`, `€{`,
   `.toFixed(2)` next to a currency symbol, `/ 100 + ' kn'`, `HRK`, `kn`.
8. **No kuna** in live UI (euro since 2023-01-01) except historical records.
9. **Percent and units with a space**: `25 %`, `5 km` — prefer Intl output; check hard-coded `25%`.
10. **Quotes**: Croatian quotes „…” (or »…«) in UI text; JSON escaping unaffected.
11. **Length**: Croatian strings are typically longer than English (rule of thumb +20–30 %); check
    buttons, tabs and table headers. Use CSS `hyphens: auto` with `lang="hr"` for long words.
12. **Encoding**: files are UTF-8 (no BOM for JSON), no mojibake (`Ä`, `Å¡`), NFC.
13. **Fallback**: missing hr keys fall back to `en`, never to `sr`/`bs`; log missing keys in dev.
14. **Placeholders untouched**: `{count}`, `%s`, `%{name}`, `{{name}}` survive translation; ICU keywords
    (`plural`, `one`, `few`, `other`, `select`) are not translated.
15. **Formal vs informal** address is consistent across the whole file (all *Vi* or all *ti*).

Quick greps:

```bash
# i18next: keys with _one but no _few
jq -r 'paths(scalars)|join(".")' messages/hr.json | grep -E '_one$' | sed 's/_one$//' | while read k; do
  jq -e --arg k "${k}_few" 'paths(scalars)|join(".")|select(.==$k)' messages/hr.json >/dev/null || echo "missing few: $k"; done
# English-style currency and percent
grep -nE "€ ?[0-9]|[0-9]%|\bkn\b|HRK" messages/hr.json
# mojibake
grep -nE "Ã|Ä|Å" messages/hr.json
```

## 4. Typical bugs seen in Croatian localisation

| Bug | Fix |
|---|---|
| `toLocaleDateString()` without locale → US format on servers | always pass `'hr'` (and `timeZone`) |
| `"25. listopad 2026."` | month in nominative: use formatter with day+month |
| `€12.50` / `12.50 €` | `Intl.NumberFormat('hr',{style:'currency',currency:'EUR'})` |
| `prije 21 dana`, `2 dan` | `Intl.RelativeTimeFormat('hr')` or ICU plural |
| `Dobrodošli, Ivan` | no name, or vocative via helper / *Dobar dan, Ivan Horvat* |
| `Apartmani u Hvar` | stored locative *na Hvaru* / *u Hvaru* |
| list sorted č/ć/š/ž last | `Intl.Collator('hr')`, hr DB collation |
| search for "cevapi" finds nothing | folded column / `und` level-1 collation |
| `Đ` lost in slug ("-akovo") | fold `đ` explicitly (NFD does not decompose it) |
| weeks start on Sunday in date pickers | set `firstDay: 1` / locale week info |
| 12-hour time picker | 24-hour for hr |
| html `lang="en"` on Croatian pages | `lang="hr"` |
