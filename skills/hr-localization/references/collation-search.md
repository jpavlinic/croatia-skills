# Sorting, search, slugs, normalisation and legacy encodings

Read this when sorting Croatian strings (JS, Python, SQL), implementing search that must find
"ćevapi" when the user types "cevapi", generating slugs, or cleaning imported data with broken
characters. SEO aspects of slugs and diacritics in search queries → `croatia:hr-seo-local`.

## 1. Croatian alphabetical order

30 letters: **a b c č ć d dž đ e f g h i j k l lj m n nj o p r s š t u v z ž**
(q, w, x, y in foreign words sort in their Latin positions).

- *č* and *ć* are separate letters after *c* (not accent variants); same for *đ* after *dž*, *š* after
  *s*, *ž* after *z*.
- *dž, lj, nj* are single letters: *luk < ljubav* (lj after l), *nož < njiva*, *dub < džem < đak*.
- Known limitation shared by ICU and every common implementation: a d+ž, l+j or n+j sequence that is
  not a digraph (*nadživjeti, podžupan, injekcija, konjunkcija*) is still sorted as a digraph. Fixing
  that needs a word list; nobody does it in practice.

### Observed results (2026-10-25)

Input: *čaša cesta ćup dno džem đak dub ljubav lopta luk njiva noga nož šuma sat žaba zec*

| Engine | Order | Correct? |
|---|---|---|
| `Intl.Collator('hr')` (Node 22, ICU 77) | cesta, čaša, ćup, dno, dub, džem, đak, lopta, luk, ljubav, noga, nož, njiva, sat, šuma, zec, žaba | yes |
| `Intl.Collator('en')` | čaša, cesta, ćup, đak, dno, dub, džem, ljubav, lopta, luk, njiva, … | no (accents as variants) |
| JS `Array.prototype.sort()` (code points) | all uppercase first, then č/ć/đ/š/ž at the very end | no |
| PostgreSQL 18.6 `COLLATE "hr-HR-x-icu"` | same as Intl hr | yes |
| MySQL `utf8mb4_croatian_ci`, `utf8mb4_hr_0900_ai_ci`, `utf8mb4_hr_0900_as_cs` | same as Intl hr | yes |
| MySQL `utf8mb4_0900_ai_ci` (default) | čaša, cesta, ćup, đak, dno, … | no |
| Python `sorted(key=locale.strxfrm)` with `hr_HR.UTF-8` on macOS | čaša, žaba, đak, cesta, … | **broken** |
| `scripts/hr_text.py sort` | identical to Intl hr on a 685-word test list (all toponyms, genitives and ethnics in the CSV) | yes |

### JavaScript

```js
const collator = new Intl.Collator('hr');            // reuse it; creating one per compare is slow
items.sort((a, b) => collator.compare(a.name, b.name));
// numeric: true → "2" before "10"; default sorts "10" before "2"
new Intl.Collator('hr', { numeric: true });
```

`String.prototype.localeCompare(b, 'hr')` works but creates a collator per call.
`Intl.Collator('hr', {sensitivity:'base'})` still treats c ≠ č (they are different letters in hr), so it
**cannot** be used for accent-insensitive search — see §3.

### Python

- Best: PyICU `icu.Collator.createInstance(icu.Locale('hr_HR'))` → `sorted(xs, key=coll.getSortKey)`.
- Stdlib only: `from hr_text import sort_key; sorted(xs, key=sort_key)` (primary Croatian order, then
  accents, then lowercase-before-uppercase, like ICU tertiary strength).
- Don't use `locale.strxfrm` (OS-dependent; wrong on macOS, missing locales in slim containers).

### SQL

PostgreSQL (ICU builds; PostgreSQL 10+):

```sql
SELECT name FROM city ORDER BY name COLLATE "hr-HR-x-icu";
-- or per column
ALTER TABLE city ALTER COLUMN name TYPE text COLLATE "hr-HR-x-icu";
-- case-insensitive equality (nondeterministic collation, PostgreSQL 12+)
CREATE COLLATION hr_ci (provider = icu, locale = 'hr-HR-u-ks-level2', deterministic = false);
```

Observed on PostgreSQL 18.6: with `hr_ci`, `'ZAGREB' = 'zagreb'` is true; `'cevapi' = 'ćevapi'` is
false even at `ks-level1` with an hr locale (č is a primary letter in hr). For accent-insensitive
equality use a root-locale collation:

```sql
CREATE COLLATION und_ai (provider = icu, locale = 'und-u-ks-level1', deterministic = false);
SELECT 'cevapi' = 'Ćevapi' COLLATE und_ai;   -- true
SELECT 'dakovo' = 'Đakovo' COLLATE und_ai;   -- true
SELECT 'cevapi' LIKE 'ćev%' COLLATE und_ai;  -- true on 18.6; LIKE with nondeterministic collations is new in PostgreSQL 18 (errors on older versions)
```

Nondeterministic collations cost performance and don't support every operator; a folded,
indexed column (§3) is usually simpler. `'Dj' = 'Đ'` is false in every collation tested — handle the
*dj* spelling in your folding step.

MySQL 8.0+:

```sql
ALTER TABLE city MODIFY name VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_hr_0900_ai_ci;
```

`utf8mb4_croatian_ci` (older UCA) and `utf8mb4_hr_0900_ai_ci` gave the correct order; both are case-
insensitive, but **`'cevapi' = 'ćevapi'` is 0** (č is a distinct letter), so `WHERE name LIKE '%cevap%'`
does not find *ćevapi*. The default `utf8mb4_0900_ai_ci` does match (1) but sorts wrongly. Use the hr
collation for ordering and a folded column for search, or `ORDER BY name COLLATE utf8mb4_hr_0900_ai_ci`
on a column stored in `utf8mb4_0900_ai_ci`.

Elasticsearch/OpenSearch: `icu_collation_keyword` with `language: hr` for sorting; for search an
analyzer with `lowercase` + `asciifolding` (or `icu_folding`), plus a `dj→đ` char filter if needed.

## 2. Unicode normalisation

- Store and compare in **NFC**. macOS file names, some PDFs and copy-paste from design tools produce
  NFD (`c` + U+030C). `"č" === "č"` is false (observed); after `.normalize('NFC')` it is true.
- Legacy single code points for digraphs exist: **U+01C4–U+01CC** `Ǆ ǅ ǆ Ǉ ǈ ǉ Ǌ ǋ ǌ`. They come from
  old Yugoslav-era encodings and some OCR. Replace them with two letters (`ǆ` → `dž`, `ǉ` → `lj`,
  `ǌ` → `nj`, title-case `ǅ ǈ ǋ` → `Dž Lj Nj`). NFKC also splits them (observed `'ǆ'.normalize('NFKC')`
  → `dž`), but NFKC changes other characters too (ligatures, superscripts, full-width forms), so use an
  explicit map (`hr_text.normalize`).
- Case mapping: `'LJUBAV'.toLocaleLowerCase('hr')` → `ljubav` (observed). No special casing rules exist
  for hr (unlike Turkish i).
- Title case of digraphs at the start of a word is *Lj, Nj, Dž* (*Ljubljana*, *Njemačka*,
  *Džamija*), all-caps is *LJ, NJ, DŽ* (*LJUBLJANA*). A naive `s[0].upper() + s[1:]` is correct for the
  two-letter spelling.

## 3. Search: diacritic folding

Users often type without diacritics (*cevapi, sibenik, zupanija*) — older habit from phones/
keyboards without Croatian layout, and English keyboards abroad. Search must match both ways.

Folding map: **č, ć → c; š → s; ž → z; đ → d** (or **dj**), plus case-folding and NFC.

Recommended implementation:

1. Normalise input (NFC + digraph code points).
2. Store a folded copy of searchable fields (`name_folded`), index it.
3. Fold the query the same way and search the folded column.
4. For *đ*, index **both** variants (`đ → d` and `đ → dj`): users type *Djakovo*, *Dakovo* and *Đakovo*.
   `hr_text.search_variants('Đurđevac')` → `{'durdevac', 'djurdjevac'}`.
5. Display the original string and highlight on the original (map offsets or highlight by regex built
   from the folded query with character classes like `[cčć]`).

JS one-liner (NFD + strip marks) handles č ć š ž but **not đ** (đ has no decomposition):

```js
const fold = s => s.normalize('NFD').replace(/\p{M}/gu, '').replace(/đ/g, 'd').replace(/Đ/g, 'D').toLowerCase();
```

`Intl.Collator('und', {sensitivity:'base', usage:'search'})` treats *cevapi = Ćevapi* and
*dakovo = Đakovo* as equal (observed), but not *djakovo = Đakovo*.

Don't fold for display or for sorting: folded strings sort wrongly (*č* would sort with *c*).

## 4. Slugs

- Same map as folding, lowercase, non-alphanumerics → `-`, collapse/trim hyphens.
- *đ* has two conventions: **d** (*dakovo* — what generic transliteration produces; observed: Python
  `unidecode('Đakovo')` → `Dakovo`, `python-slugify` → `dakovo`) and **dj** (*djakovo* — the
  traditional Croatian ASCII spelling, common in Croatian URLs and e-mail addresses). Check the library
  your project uses; JS libraries differ. Both are understood. Recommendation:
  follow the project's existing slugs; for a new project pick one, document it, and keep it — **never
  change published slugs** without 301 redirects. *dj* reads more naturally to Croatian users; *d* is
  what generic tooling produces. SEO implications → `croatia:hr-seo-local`.
- `python3 scripts/hr_text.py slugify "Šibenik – Đakovo: 25 % popusta!"` → `sibenik-dakovo-25-popusta`;
  `--dj` → `sibenik-djakovo-25-popusta`.
- Don't put diacritics in URLs unless the whole stack (CMS, CDN, analytics, sharing) handles
  percent-encoded UTF-8 well; they appear as `%C4%8D` when copied.

## 5. Legacy encodings and mojibake

Croatian text appears in four encodings: UTF-8 (use it), **Windows-1250** (old Windows/Office/CSV
exports, banking files), **ISO-8859-2** (old Unix/web), and the 7-bit YUSCII (`^ ~ } { |` used for
č ć đ š ž, e.g. `~a{a` = *čaša*; very old documents only).

| Symptom | Example | Cause | Fix |
|---|---|---|---|
| `Ä` + odd char, `Å¡`, `Å¾` | `Å¡kola Ä‡evapi Å¾aba Ä‘ak`, `Ä\x8dokolada` | UTF-8 bytes decoded as Windows-1252 / Latin-1 | re-encode as cp1252 (Latin-1 for undefined bytes), decode UTF-8 |
| `ÄŒ`, `Ä\x90` | `ÄŒakovec`, `Ä\x90akovo` | same, capitals (Č, Đ) | same |
| `Ã` + char repeated | `ÃƒÂ©` | double-encoded | repeat the fix |
| `è æ ð È Æ Ð` instead of č ć đ Č Ć Đ | `Kuæa u Ðakovu, èaj` | Windows-1250 bytes read as Windows-1252/Latin-1 (š ž look right!) | map single characters, or re-read the file as cp1250 |
| `¹ ¾ © ®` instead of š ž Š Ž | `¹kola, mo¾da` | ISO-8859-2 read as Latin-1 | map, or re-read as iso-8859-2 |
| `�` | `Ä�okolada` | lossy decode already replaced bytes | can't be repaired from the text; go back to the source file |

Best fix: re-read the original bytes with the right codec
(`open(f, encoding='cp1250')`, `iconv -f WINDOWS-1250 -t UTF-8`). For text already in a database:
`python3 scripts/hr_text.py fix-mojibake "Å¡kola"` → `škola`; `--legacy` adds the cp1250/ISO-8859-2
single-character map (opt-in, because è/æ/ð are legitimate in French/Danish/Icelandic text).
For large jobs the `ftfy` library is the general tool.

CSV exports for Croatian Excel users: write UTF-8 **with BOM** (`utf-8-sig`) and `;` as separator
(Croatian Excel uses the comma as decimal separator, so list separator is `;`), or Excel will show
mojibake / one column.

## 6. Keyboard and input

- Croatian keyboard layout (Windows "Croatian", macOS "Croatian"): č ć đ š ž on the keys right of P/L
  (`[ ; ' ]` and `\` positions on US layout); `@` is AltGr+V, `{` `}` are AltGr+B/N.
- Mobile keyboards offer č/ć/š on long-press; many users skip diacritics in search and chat, but
  expect correct Croatian in the UI.
- Never strip diacritics from user input you store (names!). *Đurđica Šimić* must stay as typed.
- Input validation for names: allow letters incl. č ć đ š ž, apostrophes, hyphens, spaces
  (`/^[\p{L}\p{M}' -]+$/u`); do not use `[A-Za-z]`.
- Autocomplete on folded keys (`sib` → *Šibenik*, *Sibinj*).
