---
name: hr-market-brands
description: >-
  Who's who in the Croatian consumer and business market: correct, current
  names, spelling, owners and status of Croatian retailers, banks, telecoms,
  media, delivery, payments, energy, FMCG, insurance and SME software, plus the
  defunct or foreign brands to avoid. Use when writing or localizing content,
  examples, mock data, comparisons or product copy for Croatia, or when
  fact-checking a brand. Triggers: "Croatian brands", "Croatian companies",
  "shops in Croatia", "banks in Croatia", "localize examples", "mock data
  Croatia", "fact-check brand", "is X still in Croatia", hrvatski brendovi,
  trgovine, trgovački lanci, banke u Hrvatskoj, dostava, paketomat, pouzeće,
  Njuškalo, Konzum, KEKS Pay, operateri, lokalizacija primjera, testni podaci;
  or a Croatian text naming OLX, Walmart, Amazon.hr, Tele2, Vipnet, Optima,
  Splitska banka, Sberbank, Agrokor, kuna, Cammeo, Sancta Domenica, Bolt Food.
---

# Croatian market: brands and who's who

Use this skill so that Croatian content, examples, mock data, comparisons and
product decisions name real, current, correctly spelled Croatian brands: Njuškalo
rather than OLX, Konzum rather than Walmart, **dm** in lower case, **KEKS Pay**,
**A1 Hrvatska** rather than Vipnet, **Telemach** rather than Tele2. It lists who
owns what, what merged, rebranded or left, and when.

Status: researched 2026-10-25. Every entry carries a source URL and "checked 2026-10".

> **Notice.** Brand names and trademarks belong to their owners. Listing a brand
> here is a statement of fact, not an endorsement, partnership or recommendation.
> Ownership, store counts, prices and market shares change; facts here may be
> out of date. Re-check anything that matters before publishing.

## How to use

1. Identify the sector(s) the text touches and read only the matching reference.
2. Check every brand in the text against it: spelling and capitalisation, still
   active, current owner. Fix defunct or wrong-country brands with the quick
   table below and `references/common-mistakes.md`.
3. If a brand is not in the references, do not guess. Check its official site or
   the relevant register (HNB for banks, HANFA for insurers, HAKOM for telecoms
   and post, HERA for energy suppliers) and say what you checked.
4. Carry **VERIFY** flags through to the user when the fact matters to them.

| Need | File | Grep hints |
|---|---|---|
| Supermarkets, discounters, convenience, cash & carry | `references/retail-grocery.md` | `Konzum`, `Lidl`, `Studenac`, `Tommy`, `Eurospin` |
| Drugstores, pharmacies, DIY, furniture, electronics, sport | `references/retail-nonfood.md` | `dm`, `Prima Pharme`, `Lesnina`, `Big Bang`, `Pevex` |
| Classifieds, job and property portals, web shops, cross-border | `references/online-marketplaces.md` | `Njuškalo`, `Index Oglasi`, `MojPosao`, `eKupi`, `Temu`, `Amazon` |
| Banks, payments, fintech, card acceptance, insurance | `references/finance-payments.md` | `HNB`, `OTP`, `Addiko`, `KEKS Pay`, `Aircash`, `pouzeće`, `HANFA` |
| Telecom operators, TV, press, portals | `references/telecom-media.md` | `HT`, `A1`, `Telemach`, `Iskon`, `RTL`, `Nova TV`, `N1` |
| Parcels, paketomati, food delivery, taxi, buses, rail, ferries, airlines | `references/transport-delivery.md` | `BOX NOW`, `Paket24`, `GLS`, `Wolt`, `Wizi`, `HŽPP` |
| Electricity, gas, fuel stations | `references/energy-fuel-utilities.md` | `HEP Elektra`, `E.ON`, `INA`, `Tifon`, `Crodux`, `Lukoil` |
| Food and drink producers, Fortenova divestments | `references/fmcg-food.md` | `Podravka`, `Kraš`, `Ledo`, `Jamnica`, `Zvijezda`, `Fortenova` |
| SME accounting, invoicing, eRačun intermediaries | `references/services-software.md` | `Minimax`, `Pantheon`, `Moj-eRačun`, `Fina` |
| e-Građani, ePorezna, mPorezna, e-Pristojbe, MikroeRačun | `references/public-digital-services.md` | `NIAS`, `ePorezna`, `FiskAplikacija` |
| Defunct, renamed and wrong-country brands, with dates | `references/common-mistakes.md` | brand name |

## Rules

1. **Use real, current brands** when a real brand is needed, spelled exactly as
   the owner writes it (see "Spelling" below). Never invent a brand, a product
   name, a store count or a market share.
2. **Never imply endorsement or partnership.** "You can pay with KEKS Pay" is a
   fact; "KEKS Pay recommends …" or a logo wall implying a partnership is not.
   Do not use logos unless the user has the right to.
3. **Comparisons** of named competitors (price, quality, "better than") are
   comparative advertising: follow `croatia:hr-legal-compliance` (objective,
   verifiable, like-for-like, not denigrating, no trademark free-riding).
4. **Trademarks belong to their owners.** Do not use a brand as a generic word in
   marketing copy unless the owner does ("naruči Woltom" is colloquial; in copy
   write "naruči putem Wolta").
5. **Mock data prefers fictional businesses**: "Primjer d.o.o.", "Trgovina
   Primjer", "Pekara Primjer", `ana.horvat@primjer.hr`. Use real brands only
   where realism needs them (e.g. a dropdown of real banks or couriers, a payment
   method list), and then only current ones from these references.
6. **Date anything that goes stale**: prices (in euro, with the year; Croatia has
   used the euro since 1 January 2023, see `common-mistakes.md`), store counts,
   market shares, ownership. Write "2025 (HAKOM)" or "listopad 2026.".
7. **Pending deals are pending.** Do not write that a takeover happened until it
   closed (e.g. RBI and Addiko, Badel 1862 and Jamnica, Bosqar and PIK Vrbovec
   were not closed when this skill was researched).
8. Croatian copy also follows `croatia:croatian-language` (brand names inflect:
   *u Konzumu*, *s Njuškala*, *preko BOX NOW-a* or *putem BOX NOW paketomata*).

### Spelling that is often wrong

**dm** (always lower case) · **KEKS Pay** · **Njuškalo** (š) · **Index Oglasi** ·
**Plavi oglasnik** (site oglasnik.hr) · **MojPosao** · **eKupi** · **BOX NOW**
(own styling; press writes Box Now) · **A1 Hrvatska** · **HT / Hrvatski Telekom** ·
**bonbon** · **Telemach** · **HEP Elektra** · **E.ON** · **INA** · **Lesnina XXXL** ·
**Big Bang** · **Wolt**, **Glovo** · **Wizi** (ex-Cammeo) · **HPB** ·
**Erste&Steiermärkische Bank** (trades as Erste banka) · **Zagrebačka banka**
(Zaba, UniCredit Group) · **PBZ** (Intesa Sanpaolo Group) · **Raiffeisenbank
Austria** (RBA) · **e-Građani** · **ePorezna** / **mPorezna** · **e-Pristojbe**.

## Quick table: if the text says X, use Y

| Text says (wrong, foreign or defunct) | Use instead (Croatia, checked 2026-10) |
|---|---|
| OLX, Craigslist, Kleinanzeigen, Halo oglasi (Serbian) | Njuškalo, Index Oglasi, Plavi oglasnik |
| Walmart, Tesco, Aldi/Hofer, Billa, Mercator, Getro, Diona | Konzum, Lidl, Kaufland, Spar/Interspar, Plodine, Tommy, Studenac, Eurospin |
| Amazon.hr / "order on Amazon Croatia" | No Croatian Amazon store exists. Local: eKupi, Links, Big Bang, Mall.hr, Chipoteka |
| Tele2 | Telemach (renamed November 2020) |
| Vipnet, Vip | A1 Hrvatska (renamed 1 October 2018); low-cost brand Tomato |
| Optima Telekom | Telemach (taken over 2022, brand merged October 2022) |
| T-Com, T-Mobile | Hrvatski Telekom (HT); Iskon and bonbon are HT brands |
| Splitska banka | OTP banka (merged 1 December 2018) |
| Sberbank, Nova hrvatska banka, Volksbank | HPB (bought Sberbank 2022, merged 2023) |
| Hypo Alpe-Adria-Bank | Addiko Bank (VERIFY rename year, 2016) |
| Agrokor | Fortenova grupa (since 1 April 2019) |
| kuna, kn, HRK prices | euro (EUR, €), since 1 January 2023 |
| Cammeo taxi | Wizi (renamed May 2024); or Uber, Bolt |
| Sancta Domenica | Big Bang (renamed February 2025) |
| Bolt Food, Pauza.hr, Uber Eats | Wolt, Glovo (Bolt Food left 6 October 2025) |
| PayPal as the only option | Cards, plaćanje pouzećem (cash on delivery), KEKS Pay, Aircash, bank transfer, Apple Pay/Google Pay |
| "Lesnina is now XXXLutz" | Wrong: the Croatian chain still trades as Lesnina XXXL (owned by XXXLutz since 2010) |

## Keeping current

What goes stale fastest: pending M&A (Addiko, Jamnica, PIK Vrbovec, a reported
review of the Telemach ownership), Lukoil's Croatian network (owner under
sanctions; ownership may change), store and
paketomat counts, market shares, food-delivery and taxi platforms, eRačun
intermediaries. Official checks:

- Banks: HNB list of credit institutions, hnb.hr › Supervizija › Popis kreditnih institucija.
- Insurers: HANFA register, hanfa.hr › Registri › Tržište osiguranja.
- Telecom and postal market shares: HAKOM quarterly and annual reports, hakom.hr.
- Electricity and gas suppliers: HERA register, hera.hr; HROTE comparison tool.
- Companies, owners and mergers: sudreg.pravosudje.hr; ZSE announcements eho.zse.hr.
- Mergers under review: AZTN, aztn.hr.
- eRačun intermediaries: Porezna uprava list, porezna.gov.hr › Fiskalizacija.
- Business press with dates: Poslovni dnevnik, Lider, Bloomberg Adria, tportal, financije.hr.

Related skills: `croatia:croatian-language` (writing; it sends brand checks here),
`croatia:hr-legal-compliance` (comparative advertising, trademarks),
`croatia:hr-localization` (formats, currency), `croatia:hr-seo-local`.
