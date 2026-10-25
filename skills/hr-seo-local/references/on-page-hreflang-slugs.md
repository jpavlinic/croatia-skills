# On-page for Croatian pages: titles, slugs, lang, hreflang, schema

Researched 2026-10-25. Google guidance quoted from Google Search Central pages
listed in `sources.md`. Examples use the fictitious business "Primjer d.o.o."
and the domain `primjer.hr`.

## 1. Titles, meta descriptions, headings

- **Sentence case.** Croatian orthography capitalises only the first word and
  proper names: `Najam stanova u Zagrebu – cijene i ponuda`. Title Case
  ("Najam Stanova U Zagrebu") marks a page as translated or careless.
- Months, weekdays and nationality adjectives are lower case: `listopad`,
  `ponedjeljak`, `hrvatski`. Place names and institutions are capitalised:
  `Zagreb`, `Hvar`, `Porezna uprava`.
- Croatian words are long; front-load the main term. Aim for roughly 50–60
  characters in titles and 140–160 in meta descriptions as a display guide,
  not a rule.
- Use the form users search as the primary term, then let grammar carry the
  other forms: title `Apartmani na Hvaru uz more`, H1 `Apartmani na Hvaru`,
  body `apartman za četiri osobe u gradu Hvaru`.
- Polite address: `Vi/Vaš` (capital) when the text addresses one reader
  directly, `vi/vaš` for a group. Most web copy addresses the reader as one
  person. Follow the site's existing convention if it is consistent;
  otherwise apply `croatia:croatian-language`.
- Write the meta description as a natural sentence with a clear benefit; no
  keyword lists.
- Run every Croatian title, meta and heading through `croatia:croatian-language`.

## 2. Slugs

- Lower case, diacritics folded, words joined by hyphens:
  `/najam-stanova-zagreb/`, `/cevapi-recept/`.
- **đ:** choose `d` or `dj` once per site, record it in the project notes
  (`.claude/croatia/hr-seo-local.md`), and never mix. Both are seen on
  Croatian sites. Transliteration rules: `croatia:hr-localization`.
- `dž` → `dz`; `č`, `ć` → `c`; `š` → `s`; `ž` → `z`.
- Do not use percent-encoded diacritics (`/ku%C4%87a/`) for new sites: they
  work, but are ugly when shared and error-prone. Google accepts UTF-8 URLs,
  so an existing site that already uses them should not be migrated only for
  this.
- Short slugs: drop filler words where meaning survives
  (`/najam-stanova-zagreb/` rather than `/najam-stanova-u-gradu-zagrebu/`).
- Localised slugs per language are fine: `/apartmani/`, `/en/apartments/`,
  `/de/ferienwohnungen/`.
- **Never change live slugs** without 301 redirects and a reason.

## 3. Language markup and hreflang

Google's documented behaviour:

- Google detects page language from the visible content. It does not use the
  HTML `lang` attribute or hreflang for language detection. Still set
  `<html lang="hr">` (accessibility, browsers, other engines).
- One language per page for main content and navigation. Avoid side-by-side
  translations.
- Hreflang values: language in ISO 639-1 (`hr`), optional region in
  ISO 3166-1 alpha-2 (`hr-HR`, `hr-BA`, `hr-DE`), optional script in
  ISO 15924 (`sr-Latn`). Codes outside these standards are ignored. Montenegrin
  has no ISO 639-1 code, so `cnr` cannot be used in hreflang.
- Every version lists itself and all others (reciprocal); absolute URLs;
  one method (HTML tags, HTTP headers or sitemap), not all three.
- `x-default` for the fallback (language selector, or the version for
  unmatched languages).
- Do not auto-redirect by IP or browser language; Google crawls mostly from
  the US without `Accept-Language` and may not see other versions. Offer
  visible language links instead.

**Which Croatian code?**

| Situation | Use |
|---|---|
| One Croatian version for everyone (most sites) | `hr` |
| Separate versions for Croatia and BiH (different prices, delivery, legal text) | `hr-HR` and `hr-BA`, plus `hr` pointing to the main one |
| Diaspora page with different shipping or currency for Germany | `hr-DE` only if the content really differs; otherwise `hr` covers Croatian speakers everywhere |

**Tourism site example** (Croatian home market, English and German guests):

```html
<link rel="alternate" hreflang="hr" href="https://www.primjer.hr/apartmani/" />
<link rel="alternate" hreflang="en" href="https://www.primjer.hr/en/apartments/" />
<link rel="alternate" hreflang="de" href="https://www.primjer.hr/de/ferienwohnungen/" />
<link rel="alternate" hreflang="x-default" href="https://www.primjer.hr/en/apartments/" />
```

The same block appears on all three pages. For a tourism site, English is
usually the sensible `x-default`; for a Croatian-market business, the
Croatian page is.

Each language version also needs its own self-referencing canonical. Never
canonicalise `/en/` to the Croatian page.

## 4. Prices, numbers, dates, addresses

- **Currency:** euro since 1 January 2023. Write `49,00 €` or `49,00 EUR`
  (decimal comma, symbol after the number with a space). Remove leftover
  `kn`/HRK prices. In schema use `"priceCurrency": "EUR"` and a dot decimal
  (`"price": "49.00"`).
- **Numbers:** decimal comma; thousands with a dot or a space (`12.500` or
  `12 500`; IHJJ writes four-digit numbers without a separator, `1250`).
  Follow `croatia:croatian-language`.
- **Dates:** `25. listopada 2026.` (genitive month, ordinal dots) or
  `25. 10. 2026.`; ISO `2026-10-25` in `datetime` attributes and schema.
- **Times:** `9.00 – 17.00` or `9:00 – 17:00`; be consistent.
- **Phone:** `+385 1 234 5678` in international form for schema and
  `tel:` links; `01 234 5678` is fine in visible local text.
- **Address order:** street and number, then postal code and town:
  `Primjerna ulica 12, 10000 Zagreb`. Postal codes have five digits and come
  before the town.

## 5. Structured data

Mark up only what is visible on the page, and keep it identical to the GBP
and register data.

### LocalBusiness (or a more specific type)

```json
{
  "@context": "https://schema.org",
  "@type": "AccountingService",
  "name": "Primjer d.o.o.",
  "url": "https://www.primjer.hr/",
  "telephone": "+38512345678",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Primjerna ulica 12",
    "postalCode": "10000",
    "addressLocality": "Zagreb",
    "addressCountry": "HR"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 45.8150, "longitude": 15.9819 },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "08:00",
      "closes": "16:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "opens": "00:00",
      "closes": "00:00",
      "validFrom": "2026-12-25",
      "validThrough": "2026-12-26"
    }
  ],
  "priceRange": "€€"
}
```

- `addressRegion` (županija) is optional; Croatian addresses work without it.
- **Holidays.** Google's documented pattern for closures and seasonal hours
  is an `OpeningHoursSpecification` with `validFrom`/`validThrough`;
  `opens` and `closes` both `00:00` means closed all day. schema.org also
  defines `specialOpeningHoursSpecification`, but Google's local business
  documentation shows the `validFrom`/`validThrough` pattern. For Maps, set
  **special hours in Google Business Profile** too; that is what users see.
- Croatia has 14 public holidays (neradni dani) by law; get the dates for the
  year (including Easter Monday and Corpus Christi, which move) from
  `croatia:hr-calendar`.
- `priceRange` must be under 100 characters; `€€` or `od 50 €` both work.
- Seasonal tourism businesses: mark the season with `validFrom` /
  `validThrough` instead of leaving year-round hours.

### Organization and identifiers

On the home or contact page, `Organization` with `legalName` (as in the
register), `name` (trading name), `vatID` only if the business has a PDV ID
(`HR` + OIB) and shows it, `address`, `contactPoint`, `sameAs` (GBP, social
profiles). Whether and how to show the OIB, MBS and registration court is a
legal question (impressum): `croatia:hr-legal-compliance`; validate the
numbers with `croatia:hr-identifiers`.

### FAQ in Croatian

FAQPage rich results are limited by Google to well-known authoritative
government and health sites (since 2023), so most sites no longer get FAQ
snippets. A visible Croatian FAQ is still useful for users and for AI answers
(see `ai-search-croatian.md`). Marking it up does no harm if it matches the
visible text. **VERIFY** current FAQ rich result eligibility at
developers.google.com/search/docs/appearance/structured-data/faqpage.

## 6. Content trust signals for Croatian sites

- Visible company data (impressum: name, address, OIB, register court and
  MBS for companies, contact). Croatian users look for it; it is also a legal
  duty for most sites. Details: `croatia:hr-legal-compliance`.
- Named authors with real credentials for advice content (legal, tax,
  health, finance): bylines such as `Ana Horvat, ovlaštena računovođa` (fictitious example) with
  an author page.
- Cite primary Croatian sources by name and link: Narodne novine
  (narodne-novine.nn.hr), gov.hr, Porezna uprava, DZS (dzs.gov.hr /
  podaci.dzs.hr), HZZO, HZMO, HNB, FINA, ministries.
- Dates: show the published and updated date in Croatian format and keep
  rates, thresholds and laws current with the year they apply to.
- Comparison pages that name competitors are comparative advertising:
  facts must be accurate and verifiable (`croatia:hr-legal-compliance`).
- No machine-translated text without a native edit. It shows quickly in
  Croatian (calques, wrong cases, Serbian forms).
