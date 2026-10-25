# Local SEO in Croatia: GBP, NAP, citations, reviews, city pages

Researched 2026-10-25. Directory URLs were opened on that date; sites close,
change owner or get repurposed, so open each one again before recommending
it.

## 1. Google Business Profile (GBP)

Google Maps and the local pack are the main local discovery surface in
Croatia (Google has about 94% of search, see `market-data.md`).

**Setup**

- Business name exactly as customers see it on the sign and in the
  register; no keywords or towns added to the name (against GBP guidelines).
- **Categories:** GBP shows categories in the user's interface language, so
  in Croatian you see Croatian names (for example `Računovođa`,
  `Frizerski salon`, `Apartman za odmor`). Pick the most specific primary
  category; add a few secondary ones that are true.
- Service-area businesses (plumbers, cleaners, mobile hairdressers) hide the
  address and list towns or regions served.
- Description in correct Croatian (`croatia:croatian-language`); for
  tourism, add an English description on the website, since GBP has one
  description field.
- Hours plus **special hours for every Croatian public holiday** and seasonal
  closures (`croatia:hr-calendar`).
- Photos taken on site; products and services lists in Croatian.

**Verification** (Google Business Profile Help, checked 2026-10-25): Google
decides which methods are offered, depending on business type, public info,
region and hours. Possible methods: phone or SMS, e-mail, live video call,
video recording, postcard (not available for all businesses; codes usually
arrive within 14 days and expire after 30 days). Review takes up to 5
business days. Instant verification can happen when the website is verified
in Search Console. Tips for Croatia:

- For video, show the street sign or exterior, the business inside, and
  proof of management (keys, till, branded equipment).
- Croatian postal delivery to apartments and rural addresses can be slow; if
  the postcard is the only option, keep name, address and category unchanged
  while waiting, or the code stops working.
- Apartments in a private house: the address must be where guests actually
  stay; one profile per real rental property, not per unit, unless units are
  separately bookable with their own entrance and signage. **VERIFY** current
  GBP guidelines for vacation rentals before advising.

**Reviews culture.** Croatian customers read Google reviews and, in tourism,
Booking.com and TripAdvisor scores. Ask every satisfied customer, by link or
QR code, in Croatian and in the guest's language. Reply to every review in
the reviewer's language, politely, with the reviewer addressed as `Vi`.

- No incentives for reviews, no review gating (asking only happy customers),
  no fake reviews: against Google policy, and fake or bought reviews are
  unfair commercial practice under EU consumer law (Omnibus Directive) as
  implemented in Croatia. Legal detail: `croatia:hr-legal-compliance`.

## 2. NAP consistency with official registers

NAP = name, address, phone. Keep one canonical version and copy it
everywhere.

| Legal form | Official register | What to copy |
|---|---|---|
| d.o.o., j.d.o.o., d.d., ustanova, zadruga | Sudski registar, sudreg.pravosudje.hr (search by name, OIB or MBS) | legal name (tvrtka), seat address |
| Obrt | Obrtni registar (Ministry of Economy); public search at pretrazivac-obrta.gov.hr (**VERIFY** URL, page needs JavaScript) | name of the obrt, address of the seat |
| Udruga | Registar udruga (Ministry of Justice) | name, seat |

- Show the legal name in the impressum/footer and the trading name as the
  brand; GBP uses the trading name used on signage.
- Use one phone number format and the same number everywhere.
- Address spelling: same street name form everywhere (`Ulica grada Vukovara`
  vs `Vukovarska` are different streets). Use the form from the register or
  the official street register; check in Google Maps that the pin is correct.
- When the business moves or changes name, update the register first, then
  site, GBP, Apple, Bing and every directory.

## 3. Citations: Croatian directories and platforms

Verified as live and on-topic on 2026-10-25 unless marked.

| Platform | Type | Notes |
|---|---|---|
| Google Business Profile | maps, reviews | essential |
| Apple Business (business.apple.com) | Apple Maps place card | Apple Business Connect became **Apple Business** on 14 April 2026; "Brand and Location Management" is listed for Croatia |
| Bing Places for Business (bing.com/forbusiness) | Bing Maps | live; small share but free. **VERIFY** whether Croatian listings import from GBP |
| Facebook page, Instagram profile | social, reviews | widely used by Croatian small businesses; keep NAP identical |
| sudreg.pravosudje.hr | official court register | not a listing you edit, but the source of truth for the name |
| poslovna.hr | business database (Dun & Bradstreet) | covers companies, obrti, associations; data come from registers |
| companywall.hr | business and credit data | profiles generated from registers; claimable profile **VERIFY** |
| fininfo.hr | business and credit data | profiles from registers |
| mojatvrtka.net | company directory | free listings of companies and obrti |
| njuskalo.hr | largest classifieds | "Usluge", "Nekretnine", "Turistički smještaj" categories; business accounts |
| index.hr/oglasi | classifieds | free listings |
| eistra.info, ekvarner.info | regional business portals (Istria, Kvarner) | relevant if the business operates there |
| Booking.com, Airbnb, TripAdvisor | tourism | essential for accommodation and restaurants; names must match GBP |
| Branch associations and chambers (HOK, HGK, professional chambers) | member directories | strong, relevant links where membership exists |

**Do not recommend:** `pauza.hr` (no longer operates as a business
directory; the domain redirected to an unrelated site when checked on
2026-10-25) and any directory you have not opened recently. Avoid paid "submit to 500 directories" services; low-quality
directory links are listed as link spam in Google's spam policies.

For marketplaces and portals by sector (real estate, jobs, cars, food
delivery) see `croatia:hr-market-brands`.

## 4. City, town and island landing pages

**Done right**

- Create a page only where the business really serves customers and has
  something specific to say: local projects, prices or travel fees, team
  members who work there, photos, local regulations, a map, testimonials
  from that town, FAQs that differ by place.
- Use correct Croatian place-name forms. Locative and preposition are
  irregular and must be checked:

  | Place | Correct | Wrong |
  |---|---|---|
  | Split | u Splitu | na Splitu |
  | Hvar (island and town) | na Hvaru (island), u Hvaru / u gradu Hvaru (town) | |
  | Krk (island) | na Krku | u Krku (only for the town, if meant) |
  | Rijeka | u Rijeci | u Rijeki |
  | Zadar | u Zadru | u Zadaru |
  | Pula | u Puli | |
  | Makarska | u Makarskoj | u Makarski |
  | Brač | na Braču | |

  Full rules: `croatia:hr-localization`.
- Title pattern: `Vodoinstalater u Splitu – hitne intervencije 0–24`, H1
  `Vodoinstalater u Splitu`, slug `/vodoinstalater-split/`.
- Link city pages from a clear "Područja rada" (service areas) hub, not
  from a footer block of 80 town names.

**Doorway risk.** Google's spam policies list "multiple domain names or pages
targeted at specific regions or cities that funnel users to one page" and
"substantially similar pages" as doorway abuse, and "blocks of text that list
cities and regions" as keyword stuffing. A template that swaps only the town
name is exactly that. Prefer one strong service page plus GBP service areas
over dozens of thin town pages.

## 5. Tourism specifics

- **Seasonality:** demand for coastal accommodation, restaurants, boat tours
  and rent-a-car peaks June–September, with searches starting months
  earlier (winter and spring planning, foreign-language queries). Publish
  and refresh seasonal pages before the planning window. Calendar:
  `croatia:hr-calendar`; Google Trends (region Croatia, and the guest
  countries) for timing.
- Most tourism searches come from abroad in German, English, Slovenian,
  Polish, Czech, Italian, Hungarian and other languages: see
  `international-regional.md` for /de/, /en/ etc.
- Keep NAP and names consistent between GBP, Booking.com, Airbnb and the own
  site; mismatches confuse users and maps.
- Legal facts on rental pages (categorisation, tourist tax, house rules):
  `croatia:hr-tourism-rentals`.
- Off-season: update GBP hours (`Privremeno zatvoreno` or seasonal hours)
  rather than leaving summer hours.
