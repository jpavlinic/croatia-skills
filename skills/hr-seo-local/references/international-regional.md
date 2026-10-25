# International and regional setup

Researched 2026-10-25. Domain rules from domene.hr (CARNET) and the
Pravilnik o ustrojstvu i upravljanju vršnom nacionalnom internetskom domenom
(NN 83/2023). URL-structure guidance from Google Search Central
("Managing multi-regional and multilingual sites").

## 1. The .hr domain space (CARNET)

CARNET (Hrvatska akademska i istraživačka mreža) manages `.hr`. Rules
(domene.hr FAQ, read 2026-10-25):

| Domain | Who can register | How | Cost |
|---|---|---|---|
| Free `.hr` (one per entity) | Legal persons registered in Croatia and natural persons with a registered self-employed activity in Croatia (e.g. obrt) | directly at CARNET (domene.hr) | free; renew yearly |
| Paid `.hr` | Legal persons established in an EU member state; natural persons who are EU citizens **and** have a Croatian OIB | only through authorised registrars | registrar price; no limit on number |
| `.com.hr` | Any legal or natural person | only through authorised registrars | registrar price; no limit |
| `.from.hr` | Natural persons with residence or citizenship in Croatia, identified by OIB; form `ime-prezime(-dodatak).from.hr` | at CARNET | free, one per person |

- The free `.hr` name must contain the registered name, a registered short
  name, or an abbreviation of it (Pravilnik čl. 15 for legal persons, čl. 16
  for self-employed natural persons, as cited by the CARNET FAQ). Paid `.hr`
  names have no such restriction (only technical conditions).
- A domain cannot be transferred to another user except for a change of the
  user's name or legal succession; otherwise the current user deletes it and
  the new one registers it.
- Domain disputes go to CARNET arbitration (fee 345.08 EUR per the FAQ,
  read 2026-10-25).
- The list of authorised registrars is at domene.hr/portal/registrars (30
  registrars listed on 2026-10-25, including large Croatian hosts and
  telecoms and some foreign registrars).

**VERIFY** before advising on a specific case: the Pravilnik text (NN 83/2023
and any later amendment) at narodne-novine.nn.hr, and whether non-EU
businesses have any route to a `.hr` (by the FAQ, they can use `.com.hr`).

## 2. Choosing a domain and URL structure

| Option | Use when | Notes |
|---|---|---|
| `.hr` only | Business serves Croatia (and maybe Croatian speakers abroad) | Strongest local signal; ccTLD geotargets Croatia. Fine to host English pages on it too |
| `.hr` with `/en/`, `/de/`, `/it/` subfolders | Croatian business with foreign guests (tourism, export) | Easiest to run; all versions share authority. Common for apartments, marinas, restaurants, tour operators |
| `.com` (gTLD) with `/hr/`, `/en/`, `/de/` | International business or product with Croatia as one market | No country lock; use hreflang |
| Separate ccTLDs (`.hr`, `.si`, `.ba`, `.rs`) | Large regional businesses with local entities and teams | Costly; each must have real localised content |
| Subdomains (`en.primjer.hr`) | Technical constraints | Works, but users read the TLD less clearly as a geotarget |

Google's guidance in short: ccTLDs strongly signal a country; gTLD
subfolders with hreflang are flexible; other local signals are local
addresses and phone numbers, local language and currency, links from local
sites and Business Profile data. Search Console no longer has the old
"International targeting" country setting (retired in 2022), so structure
and hreflang carry the signal.

Common Croatian mistakes:

- Owning `primjer.hr` and `primjer.com` with the same content on both.
  Pick one canonical domain and 301 the other.
- Translating only the menu while the body stays Croatian (mixed-language
  pages).
- Auto-redirecting foreign IPs to `/en/`. Google advises against it; use a
  visible language switcher.
- Machine translation published unedited for German or Italian guests:
  thin and often wrong. Have each language edited by a native speaker.

## 3. Tourism: foreign-language versions

- Main guest markets for Croatian tourism include Germany, Slovenia, Austria,
  Poland, Czechia, Italy, Hungary, the UK and the US (eVisitor / Croatian
  National Tourist Board statistics; check the current year's ranking for a
  specific region at htz.hr). Prioritise languages by your own booking data.
- Each language version needs its own keyword research in that language and
  country (`ferienwohnung kroatien meerblick`, `apartmány chorvatsko`,
  `noclegi chorwacja`), not a translation of Croatian keywords.
- Place names: use the forms guests search. German guests search `Insel
  Krk`, `Rovinj`, `Split`; Italian guests sometimes use Italian names
  (`Rovigno`, `Spalato`, `Pola`, `Zara`, `Fiume`). Mention the local name and
  the common foreign name once where it helps (`Rovinj (Rovigno)`).
- Prices in EUR on every version.

## 4. Regional markets: Slovenia, Bosnia and Herzegovina, Serbia, Montenegro

The languages are related but are separate standards with different
vocabulary, spelling and (for Serbian) script.

| Market | hreflang | Notes |
|---|---|---|
| Slovenia | `sl` / `sl-SI` | Slovenian is a different language; needs full translation |
| Bosnia and Herzegovina | `bs-BA`, `hr-BA`, `sr-BA` | Three official languages. Croats in BiH read Croatian: `hr-BA` can serve them, with BiH prices (BAM), delivery and contacts if they differ |
| Serbia | `sr` (Cyrillic is the official script; Latin widely used), `sr-Latn`, `sr-Cyrl` | Ekavian, different vocabulary. Croatian text is not Serbian |
| Montenegro | `sr-ME` (Montenegrin has no ISO 639-1 code; `cnr` cannot be used in hreflang) | Ijekavian; vocabulary closer to Serbian |

Rules:

- **Never label Croatian text as `sr`, `bs` or `cnr`/`sr-ME`.** It is a wrong
  language signal and a duplicate. Either localise properly (native
  translator, local vocabulary, local currency and contacts) or keep only
  `hr` and let Google show the Croatian page to regional users who search in
  similar words.
- Croatian pages often rank in BiH, Serbia and Montenegro anyway. That is
  fine; do not add Serbian vocabulary to Croatian pages to chase it.
- Content for the region in Croatian (e.g. a B2B software company selling
  across ex-Yugoslavia) can stay `hr` with an English version as
  `x-default`.

## 5. Croatian diaspora

Large Croatian communities live in Germany, Austria, Switzerland, Ireland,
the USA, Canada, Australia, Argentina and Chile, and Croats in Bosnia and
Herzegovina form a Croatian-speaking population next door.

- One `hr` version usually serves all Croatian speakers; Google shows it to
  users searching in Croatian anywhere.
- Add regional versions (`hr-DE`, `hr-AT`, `hr-IE`, `hr-US`, `hr-CA`,
  `hr-AU`) only when content really differs: shipping, prices, local
  contacts, legal terms. Otherwise they are duplicates.
- Diaspora queries more often lack diacritics (foreign keyboards) and mix in
  the host country's words (`Steuer`, `Anmeldung`, `PPS number`). Check those
  in Search Console by country filter.
- Topics with diaspora demand: property in Croatia, inheritance, tax
  residency, OIB, documents, pensions, holidays at home. Link to the
  relevant plugin skills (`croatia:hr-real-estate`, `croatia:hr-identifiers`,
  `croatia:hr-business-admin`) for the substance.
