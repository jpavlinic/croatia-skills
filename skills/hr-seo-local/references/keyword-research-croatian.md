# Keyword research in Croatian

Researched 2026-10-25. Claims about how Google treats specific Croatian forms
are observations to test, not documented rules: Google does not publish how
it handles Croatian morphology or diacritics. Always confirm in the live SERP
(Croatian location, Croatian interface) and in Search Console.

## 1. How Croatian queries behave

### Padeži (cases) and number

Croatian nouns, adjectives and place names change with case (7 cases:
nominativ, genitiv, dativ, akuzativ, vokativ, lokativ, instrumental) and
number. One topic therefore appears as many strings:

| Intent | Typical queries |
|---|---|
| Rent a flat in Zagreb | `stan zagreb`, `stanovi zagreb`, `najam stana zagreb`, `stan za najam zagreb`, `stanovi u zagrebu`, `iznajmljivanje stanova zagreb` |
| Accountant in Split | `računovođa split`, `racunovodja split`, `knjigovodstvo split`, `knjigovodstveni servis split`, `računovodstvo u splitu` |
| Apartments on Hvar | `apartmani hvar`, `apartman hvar`, `smještaj hvar`, `apartmani na hvaru`, `privatni smještaj hvar` |

Patterns seen in practice:

- **Telegraphic queries dominate:** noun in the nominative + place in the
  nominative (`frizer zagreb`). The grammatical form `frizer u zagrebu` is
  less common in typed queries but common in voice and AI prompts.
- **Genitive after action nouns:** `najam stana`, `prodaja auta`, `izrada
  web stranica`, `popravak perilice`.
- **Plural for browsing intent** (`apartmani`, `stanovi`, `restorani`),
  singular for a specific need (`apartman za 4 osobe`).
- **Questions** use full grammar: `koliko košta najam stana u zagrebu`,
  `kako otvoriti obrt`. These are the queries AI answers target.

Google generally understands that inflected forms belong together, but the
ranking pages for `stan zagreb` and `stanovi u zagrebu` can differ. Decide by
SERP overlap (section 3), not by assumption.

### Diacritics (č, ć, đ, š, ž, dž)

Many users, especially on mobile and in the diaspora, type without
diacritics: `cevapi`, `kuca za odmor`, `zubar`, `racunovodja`, `vrtic`.

- `č` and `ć` both become `c`; `š` → `s`; `ž` → `z`; `dž` → `dz`.
- `đ` is typed as `d` **or** `dj` (`računovođa` → `racunovoda` /
  `racunovodja`; `Đakovo` → `dakovo` / `djakovo`). Both appear in queries.
- Folding can create a different word: `kuća` (house) vs `kuca` (knocks),
  `šuma` (forest) vs `suma` (sum). Google usually resolves this from
  context, but short or ambiguous queries may get mixed SERPs.

**Test strategy**

1. For each important cluster, search both spellings with Croatian location
   and interface (`google.hr`, settings or a Croatian VPN/location, private
   window).
2. Compare the top 10. Mostly the same → treat as one keyword. Clearly
   different → note it; the unaccented SERP may favour forums, classifieds or
   regional (BA/RS) sites.
3. In Search Console, filter queries with and without diacritics (regex such
   as `[čćđšž]`) to see which spelling actually brings impressions to the page.
4. **Never write content without diacritics** to "match" queries. It reads as
   careless and does not help. Correct Croatian on the page; the unaccented
   form can appear naturally only where it is a real string (a URL slug, a
   username).

### Regional vocabulary and register

The same thing has different everyday words in different regions. Standard
Croatian is right for the content, but queries may use regional or colloquial
words. Examples (check volumes before acting):

| Standard | Also typed | Note |
|---|---|---|
| rajčica | paradajz, pomidor | `paradajz` colloquial in continental Croatia, `pomidor` in Dalmatia/Istria |
| pekarnica | pekara | both are in everyday use; check which one the SERP and Search Console show |
| kuća | bajta (colloquial "place, house") | slang; not for page copy |
| prijenosno računalo | laptop | `laptop` dominates queries |
| internetska trgovina | web shop, webshop, online trgovina | anglicisms dominate queries |
| mobitel | mobilni, smartphone | `mobitel` is the normal Croatian word |
| najam automobila | rent a car | `rent a car` is very common in tourism queries |
| smještaj | apartmani, booking | users often type the platform name |

Rule: write standard Croatian, then mention the common anglicism or regional
word once where it helps users ("prijenosna računala (laptopi)"). Do not
stuff variants. Language quality: `croatia:croatian-language`.

### Serbian and Bosnian spillover

Croatia, Bosnia and Herzegovina, Serbia and Montenegro share a lot of
vocabulary and Latin script, so Google may show regional pages for Croatian
queries, and Croatian users sometimes type ekavian or Serbian words
(`hleb`, `voz`, `fudbal`, `porodica`, `opština`, `hiljadu`).

- Keep the content in standard Croatian (ijekavian, Croatian vocabulary:
  `kruh`, `vlak`, `nogomet`, `obitelj`, `općina`, `tisuću`). See
  `croatia:croatian-language`, `hrvatski-vs-srpski`.
- Do not add Serbian words to a Croatian page to catch spillover queries;
  it undermines trust with Croatian readers.
- If the regional market matters commercially, build separate localised
  versions (see `international-regional.md`).

## 2. Method

1. **Seeds.** From the business: services, products, problems, places served.
   Add how customers actually speak (sales calls, reviews, Njuškalo ads,
   forum threads, the site's Search Console queries).
2. **Expand forms.** For each seed noun: singular/plural, the cases that
   occur in queries (nominative, genitive after action nouns, locative after
   `u`/`na`), with and without diacritics. Use `scripts/kw_variants.py`:

   ```
   python3 scripts/kw_variants.py forms stan:m2 kuća:f
   python3 scripts/kw_variants.py phrase "najam stana zagreb" --noun stan:m2 --place zagreb:u:zagrebu
   ```

   The script only declines nouns you name, with the class you give, and
   skips forms it cannot predict safely. Place locatives and `u`/`na` must be
   supplied (irregular: `u Splitu`, `na Hvaru`, `u Rijeci`, `na Krku`); check
   them with `croatia:hr-localization`.
3. **Expand intent.** Add modifiers Croatians use: `cijena`, `cjenik`,
   `iskustva`, `recenzije`, `najbolji`, `povoljno`, `jeftino`, `akcija`,
   `blizu mene` (less used than in English; locals type the neighbourhood or
   town), `radno vrijeme`, `kontakt`, `iznajmljivanje`, `prodaja`, `servis`,
   `popravak`, `kako`, `koliko košta`, `što je`.
4. **Collect demand data.**
   - Search Console (first-party, the best source for an existing site).
   - Google Keyword Planner: location **Croatia**, language **Croatian**.
     Without active ad spend it shows ranges; many terms show `0–10`.
     Treat it as relative, not absolute.
   - Google Trends with region Croatia for seasonality and spelling
     comparison (`ćevapi` vs `cevapi`).
   - Autocomplete and "People also ask" on google.hr.
   - Third-party tools have thin Croatian databases; treat their volumes as
     rough.
5. **SERP check.** For each candidate, look at the top 10 for intent (shop,
   service page, article, map pack, classifieds, AI Overview).
6. **Group.** Variants with largely the same top results go on one page
   (section 3).
7. **Plan pages** with one primary keyword (the form users type most, often
   nominative or plural) and the other forms as secondary terms.

## 3. Grouping variants onto one page

- **SERP overlap rule of thumb:** if two variants share most of the top 10
  URLs, one page serves both. If they share almost none, the intents differ
  (e.g. `stan zagreb` → classifieds; `kupnja stana savjeti` → guides).
- Put the main form in the title and H1, and let the others appear where
  grammar needs them: "Najam stanova u Zagrebu", body "stan za najam",
  "najam stana na Trešnjevci". Natural Croatian uses several cases on its own.
- Do not create one URL per case or per diacritic spelling.
- Plural vs singular for a product category: use what the SERP rewards
  (usually the plural for categories: `perilice rublja`).

## 4. Low volumes, realistically

- Croatia has about 3.9 million inhabitants (DZS, census 2021: 3,871,833).
  The Croatian-speaking audience adds diaspora and Croats in Bosnia and
  Herzegovina, but volumes stay small.
- A term showing `10–100` can still bring customers. Score by intent and
  business value, not by volume alone.
- Combine small variants: ten forms at `0–10` each are one real topic.
- Local services: the map pack and GBP often matter more than organic rank.

## 5. Output format for a keyword plan

| Cluster | Primary keyword | Variants on the same page | Intent | SERP type | Page (URL) | Notes |
|---|---|---|---|---|---|---|
| najam stanova Zagreb | najam stanova zagreb | stan zagreb, stanovi u zagrebu, najam stana zagreb, stanovi zagreb najam | commercial | classifieds + map | `/najam-stanova-zagreb/` | unaccented SERP same |

State the date of the data and the source (Search Console, Keyword Planner,
Trends) next to every number.
