# Plurals for Croatian (hr) in code

Read this when writing or reviewing any string that contains a count, when configuring an i18n
library for `hr`, or when debugging "21 dana" / "2 dan" style bugs. Prose rules for numbers and nouns
are in `croatia:croatian-language`; this file is about getting the code right.

## 1. The CLDR rule (CLDR 47, same as bs and sr-Latn)

Operands: `i` = integer part, `v` = number of visible fraction digits, `f` = visible fraction digits
as an integer (`1.50` → v=2, f=50).

| Category | Rule | Examples | Noun form |
|---|---|---|---|
| `one` | v = 0 and i % 10 = 1 and i % 100 ≠ 11 — **or** f % 10 = 1 and f % 100 ≠ 11 | 1, 21, 31, 101, 121, 1001; 0.1, 1.1, 2.1, 21.1 | nominative singular: *1 dan, 21 korisnik, 31 poruka* |
| `few` | v = 0 and i % 10 = 2..4 and i % 100 ≠ 12..14 — **or** f % 10 = 2..4 and f % 100 ≠ 12..14 | 2–4, 22–24, 102; 0.2, 1.2, 3.22 | genitive singular: *2 dana, 3 korisnika, 4 poruke* |
| `other` | everything else | 0, 5–20, 25–30, 11–14, 111–114, 1.5, 2.5, "1.0" | genitive plural: *5 dana, 11 korisnika, 25 poruka* |

There is **no `many`, `zero` or `two`** for hr. 0 is `other` ("0 poruka"). Ordinals have only `other`
(`new Intl.PluralRules('hr',{type:'ordinal'})`), because ordinals are written `1.`, `2.`.

Observed (Node 22, ICU 77): `Intl.PluralRules('hr').resolvedOptions().pluralCategories` →
`["few","one","other"]`; `select` for 0–10 000 and the decimals above matched `hr_text.py plural`
exactly (compared programmatically on 2026-10-25).

### Trailing zeros matter

`new Intl.PluralRules('hr').select(1)` → `one`, but with `minimumFractionDigits: 1` the number is
`1.0` (v=1, f=0) → `other`. If you display `1,0 km`, select the category with the same options you
format with (`new Intl.PluralRules('hr', { minimumFractionDigits: 1 })`), or pass the formatted string
to `hr_text.py plural "1.0"`.

### Decimals in prose (note)

CLDR output for decimals is mechanical: `Intl.NumberFormat('hr',{style:'unit',unit:'liter',unitDisplay:'long'})`
gives `1,5 litara`, `2,5 litara`, `1,1 litra`, `1,2 litre` (observed). Many Croatian writers and
grammars use the genitive singular after a decimal number (*1,5 litre*, *2,5 kilometra*). **VERIFY**
the current IHJJ position before relying on either in high-visibility copy; the safe pattern for UI
is the unit symbol (`1,5 l`, `2,5 km`), which needs no agreement.

## 2. Reference implementations

### JavaScript

```js
const pr = new Intl.PluralRules('hr');
const forms = { one: 'dan', few: 'dana', other: 'dana' };
const label = n => `${n} ${forms[pr.select(n)]}`;   // 21 dan, 22 dana, 25 dana, 11 dana, 111 dana
```

### Python (stdlib) — see `scripts/hr_text.py`

```python
def plural(n):  # n as int, float or str ("1.0" keeps its trailing zero)
    i, v, f = operands(n)
    if (v == 0 and i % 10 == 1 and i % 100 != 11) or (f % 10 == 1 and f % 100 != 11):
        return "one"
    if (v == 0 and 2 <= i % 10 <= 4 and not 12 <= i % 100 <= 14) or \
       (2 <= f % 10 <= 4 and not 12 <= f % 100 <= 14):
        return "few"
    return "other"
```

`python3 scripts/hr_text.py plural 22 dan dana dana` → `22 dana`.

## 3. Framework configuration

| Stack | What to write for hr |
|---|---|
| ICU MessageFormat (FormatJS / react-intl, next-intl, Angular `$localize`/i18n, Lingui, messageformat) | `{count, plural, one {# dan} few {# dana} other {# dana}}` |
| i18next ≥ v21 (JSON v4) | keys `days_one`, `days_few`, `days_other` (uses `Intl.PluralRules`; polyfill on very old runtimes) |
| i18next JSON v3 (legacy) | `days_0`, `days_1`, `days_2` (index order one/few/other) |
| vue-i18n | pipe syntax `'dan | dana | dana'` needs a custom `pluralRules: { hr: (choice) => ... }` returning 0/1/2; the default rule is English-like |
| gettext (`.po`), Django, WordPress, PHP | `"Plural-Forms: nplurals=3; plural=(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2);\n"` |
| Rails (rails-i18n) | `hr` uses `OneFewOther` → keys `one`, `few`, `other` (fractional part handled like CLDR). The bundled `hr.yml` also carries `many:` keys; they are ignored. |
| Android `strings.xml` | `<plurals name="days"><item quantity="one">%d dan</item><item quantity="few">%d dana</item><item quantity="other">%d dana</item></plurals>` |
| iOS `.stringsdict` / String Catalog | `one`, `few`, `other` |
| Java ICU4J / .NET (ICU-based) | ICU MessageFormat as above |

gettext limitation: the `n` in `Plural-Forms` is an integer, so `1,5 dana` is evaluated as `1`
(`one` → "1,5 dan"). For decimals use ICU MessageFormat or `Intl.PluralRules`.

### ICU examples

```text
{count, plural,
  =0 {Nemate novih poruka.}
  one {Imate # novu poruku.}
  few {Imate # nove poruke.}
  other {Imate # novih poruka.}
}
```

Note the adjective agrees too (*novu / nove / novih*) — another reason to keep the whole sentence in
each branch. `=0` is an exact match and is optional; without it 0 falls into `other`
("Imate 0 novih poruka.").

```text
{count, plural, one {Odabran je # proizvod.} few {Odabrana su # proizvoda.} other {Odabrano je # proizvoda.}}
```

The verb agrees as well: *odabran je* (one), *odabrana su* (few), *odabrano je* (other).

## 4. Common bugs (and how they look)

| Bug | Wrong output | Cause |
|---|---|---|
| English two-form logic `n === 1 ? 'poruka' : 'poruka/poruke'` | `21 poruka` OK by luck, but `2 poruka` or `5 poruke`; with *dan*: `21 dana` (should be *21 dan*) | only one/other |
| few as `n >= 2 && n <= 4` | `22 poruka`, `23 poruka`, `102 poruka` (should be *22 poruke*) | ignores `n % 10` |
| one as `n % 10 === 1` without the 11 exception | `11 dan`, `111 korisnik` (should be *11 dana*, *111 korisnika*) | missing `n % 100 != 11` |
| few as `n % 10` in 2..4 without 12–14 | `12 poruke`, `13 poruke` (should be *12 poruka*) | missing `n % 100` check |
| Only `one`/`other` keys in `hr.json` copied from `en.json` | i18next falls back to `other` for 2–4: `3 poruka` | missing `_few` key |
| Pluralising with the formatted string | `"1.234"` parsed as 1.234 → `one` | pass the number, not the localized string |
| Counting with `minimumFractionDigits` but selecting on the raw number | `1,0 kilometar` | select with the same format options |
| Sentence built around the count | `"Imate " + n + " " + noun` | adjectives/verbs don't agree; translate whole sentences |

Test set to put in every hr plural unit test: **0, 1, 2, 4, 5, 11, 12, 14, 21, 22, 25, 101, 111, 112,
121, 1.5, "1.0"**.

## 5. Translator-facing notes for hr.json

- Every plural message needs three branches; review tools often only show `one`/`other` from the
  English source — add `few` explicitly.
- Nouns differ per branch, and so do adjectives, pronouns and past participles.
- Feminine *2 poruke*, masculine *2 korisnika*, neuter *2 pisma*; 5+: *poruka, korisnika, pisama*.
- `euro`: *1 euro, 2 eura, 5 eura, 21 euro*; prices are usually written with the symbol (`5 €`), which
  avoids agreement entirely.
