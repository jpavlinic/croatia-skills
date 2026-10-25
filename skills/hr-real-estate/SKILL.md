---
name: hr-real-estate
description: >-
  Buying, selling, owning and renting property in Croatia: purchase process, land
  registry (ZK izvadak, A/B/C list, uknjižba, katastar), kapara and predugovor,
  notary, taxes and costs 2026 (porez na promet nekretnina 3 %, PDV on new builds,
  24 % tax on resale within 2 years, porez na nekretnine 0.60–8 €/m², rental tax
  12 %), long-term rental (Zakon o najmu stanova, ugovor o najmu, priuštivi najam),
  HNB DSTI/LTV mortgage limits, first-home tax refund, foreigners buying (EU vs
  third-country, reciprocity), energy certificates, legalizacija, apartment
  buildings (upravitelj, pričuva, suvlasnici). Triggers: "buy property Croatia",
  "real estate Croatia", "foreigner buy apartment Croatia", "nekretnine", "kupnja
  stana", "kupoprodajni ugovor", "kapara", "zemljišna knjiga", "ZK izvadak",
  "uknjižba", "porez na promet nekretnina", "porez na nekretnine", "najam stana",
  "ugovor o najmu", "energetski certifikat", "legalizacija", "pričuva",
  "upravitelj zgrade".
---

# Croatian real estate: buy, sell, own, rent

Practical, source-cited knowledge for property transactions and ownership in Croatia:
due diligence, land registry, contract and payment mechanics, taxes and costs, long-term
renting, mortgages, foreign buyers, apartment-building rules, legalisation and energy
certificates. Use it to answer questions, run a buyer's or seller's checklist, estimate
costs, and outline (never finalise) contracts.

Status: researched 2026-10-25.

> **Not legal, tax or financial advice.** This skill provides general,
> research-based information that may be incomplete or out of date. Always
> verify with the official sources cited and consult a qualified professional
> (lawyer / odvjetnik, tax adviser / porezni savjetnik, accountant /
> računovođa) before acting.

**Disclaimer rules (mandatory).**
- End every answer that touches law, tax, money or contracts with one line in the user's language:
  - EN: *This is general information, not legal or tax advice. Check the cited sources and consult a professional.*
  - HR: *Ovo su opće informacije, a ne pravni ni porezni savjet. Provjerite navedene izvore i posavjetujte se sa stručnjakom.*
- Start every generated document, contract outline, checklist or cost calculation with:
  - HR: `PREDLOŽAK – nije pravni savjet. Prilagodite ga svom slučaju i dajte ga na provjeru stručnjaku.`
  - EN: `TEMPLATE – not legal advice. Adapt it to your case and have it reviewed by a professional.`

## How to use

1. **Pin the facts that change the answer.** Ask, or state what you assumed:
   - buyer's/seller's nationality and residence (Croatian, EU/EEA/Swiss, third country) and whether buying as a person or a company;
   - whether this is the buyer's first home, the buyer's age (under 45?) and citizenship (first-home refund);
   - property type (flat, house, land, agricultural land, commercial);
   - new build from an investor (VAT) or resale (RETT);
   - location (city/municipality sets property tax; coast vs inland matters for agricultural land);
   - financing (cash or mortgage) and, for sellers, the acquisition date and whether they lived there.
2. **Load only the reference you need** (grep first, they are long):

| Topic | File | Grep hints |
|---|---|---|
| Step-by-step purchase, predugovor, kapara, notary, payment, escrow-like options, handover | `references/buying-process.md` | `Step`, `kapara`, `predugovor`, `polog`, `tabularna` |
| ZK izvadak, A/B/C list, uknjižba, predbilježba, zabilježba, plomba, katastar mismatch, OSS portal, court fees | `references/land-registry.md` | `vlastovnica`, `teretovnica`, `plomba`, `katastar`, `pristojb` |
| RETT 3 % vs PDV, first-home refund, 24 % resale tax, porez na nekretnine, komunalna naknada, rental tax, full cost table | `references/taxes-costs-2026.md` | `RETT`, `PDV`, `24 %`, `0,60`, `komunalna`, `Cost table` |
| Long-term rental: contract, mandatory elements, rent changes, notice, registration with Porezna, priuštivi najam, HNB mortgage rules | `references/renting-long-term.md` | `čl. 5`, `čl. 25`, `8 dana`, `priuštivi`, `DSTI` |
| Foreign buyers: EU/EEA, OECD amendment, third-country reciprocity and ministry consent, agricultural land, buying via a company | `references/foreigners.md` | `358.a`, `uzajamnost`, `OECD`, `poljoprivredno` |
| Apartment buildings: zajednica suvlasnika, upravitelj, predstavnik, pričuva minimum, short-term rental consent, decisions and majorities | `references/apartment-buildings.md` | `čl. 29`, `čl. 34`, `čl. 47`, `dvotrećinsk`, `prinudni` |
| Legalisation (rješenje o izvedenom stanju, 2026 reopening), uporabna dozvola, pre-1968 buildings, energy certificate rules and fines | `references/legalisation-energy.md` | `izvedenom`, `21. lipnja 2011`, `1968`, `čl. 14`, `čl. 70` |
| Buyer due diligence, seller checklist, landlord checklist, red flags | `references/checklists.md` | `Buyer`, `Seller`, `Red flags` |
| All primary sources with URLs, and the VERIFY list | `references/sources.md` | `VERIFY` |

3. **Templates** (`assets/`): `buyer-due-diligence-checklist.md` (EN+HR checklist) and
   `ugovor-o-najmu-stana-outline.md` (Croatian outline of a long-term lease, per Zakon o najmu
   stanova čl. 5). Fill them from the user's facts; never present them as a finished contract.
4. **Croatian output** (contracts, letters, ads) must be correct standard Croatian: apply
   `croatia:croatian-language`. Use **Vi/Vaš** when addressing one person.
5. **Related skills**: OIB for foreigners → `croatia:hr-identifiers`; short-term/tourist rental
   (rješenje, paušal, co-owner consent detail) → `croatia:hr-tourism-rentals`; renting through an
   obrt or d.o.o. → `croatia:hr-business-admin`; energy-renovation grants → `croatia:hr-eu-funding`;
   consumer contract and GDPR questions (e.g. agency forms) → `croatia:hr-legal-compliance`;
   property portals as brands → `croatia:hr-market-brands`; deadlines and holidays →
   `croatia:hr-calendar`.

## Quick figures 2026

| Item | 2026 value | Source |
|---|---|---|
| Porez na promet nekretnina (RETT) | 3 % of market value, paid by the **buyer**; no general first-home exemption since 2017 | Zakon o porezu na promet nekretnina (ZPPN) čl. 6, 12 |
| New build from a VAT-registered investor (before first occupancy / within 2 years of it) | PDV 25 % in the price, **no** RETT | ZPPN čl. 5(2); Zakon o PDV-u čl. 40(1)(j) |
| First-home refund (Croatian citizens under 45, contract signed after 1 Jan 2025) | RETT refunded (max 3 % of the base) or 50 % of VAT (max 12.5 % of the base), within area/price limits; apply within 24 months | Zakon o priuštivom stanovanju (NN 45/26) čl. 62–66; apn.hr |
| Income tax on resale within 2 years of acquisition (not own home) | 24 % of the gain | porezna-uprava.gov.hr (dohodak od otuđenja) |
| Porez na nekretnine (dwellings not used for permanent living or long-term rent) | 0.60–8.00 €/m² of useful area per year, set by the city/municipality (0.60 if no decision) | Zakon o lokalnim porezima čl. 26, 27 |
| Long-term rent counts as exempt from property tax if let | at least 10 months in the tax year | ZLP čl. 27(5) |
| Rental income tax (individual, long-term) | 12 % on rent minus 30 % flat expenses → about 8.4 % of gross rent | porezna-uprava.gov.hr (dohodak od najma) |
| Register a lease with Porezna | within 8 days (none if a notary certifies it) | porezna-uprava.gov.hr; Zakon o najmu stanova čl. 26 |
| Uknjižba court fees | 6.64 € filing + 26.54 € decision per right (50 % off the filing fee if filed electronically); 5× if filed later than 60 days | sudovi.hr; gov.hr; Uredba o Tarifi sudskih pristojbi (NN 37/23) |
| HNB mortgage limits | DSTI ≤ 45 % (housing), LTV ≤ 90 %, maturity ≤ 30 years; bank exception quota 10 % per quarter from 1 Oct 2026 (was 20 %) | hnb.hr Odluka o kriterijima kreditiranja potrošača |
| Minimum building reserve (pričuva) | 0.54 % of the etalonska cijena per m² per year → about 0.36 €/m² per month (with 796.34 €/m², NN 106/25) | Zakon o upravljanju i održavanju zgrada (ZUOZ) čl. 29 |
| Short-term rental in a block of flats | prior written consent of a 2/3 majority **plus** all adjoining neighbours; existing rentals must collect it by 1 Jan 2030 | ZUOZ čl. 34, 63 |
| Energy certificate | mandatory before sale, rent or lease; class in every ad; valid 10 years; owner (natural person) fine 1,000–2,000 € | Zakon o energetskoj učinkovitosti u zgradarstvu (NN 155/25) čl. 13, 14, 70 |
| Legalisation | filing deadline abolished from 16 May 2026; only buildings built by 21 June 2011 (DOF5/2011 orthophoto), via eDozvola | ZPNIZ amendment NN 48/26; mpgi.gov.hr |
| Agency commission | no legal cap; no advance payment; if both sides pay, the total may not exceed the top of the price list | Zakon o posredovanju u prometu nekretnina (NN 69/26) čl. 28–30 |

## Core rules that cover most questions

- **Ownership passes only on registration** (uknjižba) in the zemljišna knjiga, not on signing
  (gov.hr; ZZK čl. 8, 34). The buyer is protected by trust in the land register only for what
  is registered (ZZK čl. 8(3)), so check the ZK izvadak on the day of signing and again before paying.
- **The seller signs a tabularna isprava** (explicit consent to registration, ZZK čl. 59(1)(b)),
  either in the contract (clausula intabulandi) or as a separate document handed over against
  payment. The signature must be notarised (ZZK čl. 57).
- **Kapara** is a deposit under ZOO čl. 303–305: the payer who backs out loses it; the recipient
  who backs out returns double. If the contract is fulfilled, it is credited to the price.
  Agree in writing whether a payment is kapara or a plain advance (predujam).
- **RETT is assessed by Porezna** after the notary sends the contract (within 30 days, ZPPN čl. 18);
  pay within 15 days of the rješenje (čl. 26). Porezna may reassess a below-market price (čl. 9).
- **Sellers**: no income tax if sold more than 2 years after acquisition, or if it was their
  own home (registration of address alone is not proof). Otherwise 24 % of the gain.
- **Owners**: check the city's property-tax decision; report changes by 31 March (ZLP čl. 49a).
  Permanent living must be proven by actual use, not just a registered address (čl. 27(3)).
- **Landlords**: written contract with the čl. 5 elements, energy certificate handed over,
  contract filed with Porezna within 8 days, 12 % tax on 70 % of rent.
- **Foreigners**: EU/EEA nationals buy like Croatians (agricultural land: same rules since
  1 July 2023, incl. state pre-emption on larger plots). Third-country nationals need reciprocity
  and consent of the ministry of justice before registration.
- **Blocks of flats**: a manager (upravitelj) is mandatory (ZUOZ čl. 47); every owner pays at
  least the statutory reserve monthly (čl. 29); arrears stay with the flat in practice, so ask
  the manager for a debt certificate before buying.
- **Illegal or unregistered buildings** are a major risk: check uporabna dozvola, rješenje o
  izvedenom stanju or the pre-1968 status, and that the building is drawn in the cadastre and ZK.

## Keeping current

| Fact | Changes | Check |
|---|---|---|
| Porez na nekretnine per m² | each city by 15 Dec for next year (e.g. Zagreb 8 €/m² from 2027) | city's Odluka o lokalnim porezima; porezna-uprava.gov.hr |
| HNB DSTI/LTV and exception quotas | by HNB decision (last change 1 Oct 2026) | hnb.hr |
| Etalonska cijena građenja (drives minimum pričuva) | ministry publishes in Narodne novine | narodne-novine.nn.hr, mpgi.gov.hr |
| First-home refund conditions, average prices per m² | rulebook under Zakon o priuštivom stanovanju čl. 66(9); yearly price table | apn.hr, mpgi.gov.hr |
| Foreigners: OECD amendment of ZV čl. 358.a | enters into force when Croatia joins the OECD | narodne-novine.nn.hr (NN 52/25); mpudt.gov.hr reciprocity list |
| Legalisation fee (naknada za zadržavanje) | Uredba NN 84/26 | mpgi.gov.hr |
| Program priuštivog najma calls | APN public calls | apn.hr, mpgi.gov.hr |
| Rental, capital gains, RETT rates | yearly tax packages (usually in force 1 Jan) | porezna-uprava.gov.hr, zakon.hr |

Items not confirmed against a primary source are marked **VERIFY** in the references and
collected in `references/sources.md`. Surface the relevant ones to the user as questions for
a lawyer, notary or tax adviser rather than presenting them as settled.
