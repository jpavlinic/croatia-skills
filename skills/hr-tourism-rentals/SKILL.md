---
name: hr-tourism-rentals
description: >-
  Croatian private accommodation and small tourism businesses: rješenje o
  odobrenju / kategorizacija, eVisitor guest check-in, tourist tax, tourist
  board fee, flat-rate tax per bed (2025 index ranges), VAT and PDV-ID for
  Booking/Airbnb commissions, DAC7, fiscalization and receipts, house rules,
  guest messages in Croatian and English, co-owner consent, the new
  Hospitality Act and EU STR Regulation 2024/1028 registration numbers. Use
  for "iznajmljivač", "privatni smještaj", "apartman", "obiteljski smještaj",
  "kategorizacija", "eVisitor", "boravišna pristojba", "turistička pristojba",
  "turistička članarina", "TZ-2", "paušal po krevetu", "PDV-ID iznajmljivač",
  "provizija Booking PDV", "DAC7", "registracijski broj", "suglasnost
  suvlasnika", "kućni red", "short-term rental Croatia", "holiday rental
  Croatia", "Airbnb Croatia tax", or a vacation-rental site/app for Croatia.
---

# Croatian private accommodation and tourism rentals

Practical, source-cited knowledge for people who rent rooms, apartments, holiday houses or camp
pitches to tourists in Croatia (iznajmljivači), and for developers building tools for them. It
covers registration, categorisation, eVisitor, the tourist tax, the tourist board membership fee,
the flat-rate tax per bed, VAT on platform commissions, DAC7, receipts and fiscalization, guest
communication, and the 2025–2027 regulatory changes.

Status: researched 2026-10-25.

> **Not legal, tax or financial advice.** This skill provides general,
> research-based information that may be incomplete or out of date. Always
> verify with the official sources cited and consult a qualified professional
> (lawyer / odvjetnik, tax adviser / porezni savjetnik, accountant /
> računovođa) before acting.

**Disclaimer rules for Claude**
- End every answer that touches law, tax, fees or registration with one line in the user's language:
  - EN: *This is general information, not legal or tax advice. Check the cited sources and consult a professional.*
  - HR: *Ovo su opće informacije, a ne pravni ni porezni savjet. Provjerite navedene izvore i posavjetujte se sa stručnjakom.*
- Start every generated document, template, house-rules text or calculation with:
  - HR: `PREDLOŽAK – nije pravni savjet. Prilagodite ga svom slučaju i dajte ga na provjeru stručnjaku.`
  - EN: `TEMPLATE – not legal advice. Adapt it to your case and have it reviewed by a professional.`

## How to use

1. **Pin the facts that change the answer.** Ask, or infer and say what you assumed:
   - **Legal form**: a physical person in domaćinstvo (obiteljski smještaj), an OPG (seljačko
     domaćinstvo / agroturizam), an obrt, or a d.o.o.
   - **Location**: the municipality or city (JLS). It sets the flat-rate tax per bed, and the
     county sets the tourist tax.
   - **Capacity**: the number of units and beds (main and extra beds), or camp pitches.
   - **VAT status**: not in VAT, PDV-ID only, or a full VAT payer (obveznik PDV-a).
   - **Channels**: Booking.com, Airbnb, Vrbo, agencies, direct bookings; and how guests pay
     (via the platform, by card or cash on site, or by bank transfer).
   - **Building**: a house, or a flat in a multi-apartment building (co-owner consent).
   - **Residence**: whether the owner lives in Croatia (EEA/Swiss nationality is required for
     domaćinstvo; non-residents have different eRačun rules).
2. **Load only the reference you need** (grep first):

| Topic | File | Grep hints |
|---|---|---|
| Types (domaćinstvo, OPG, obrt, d.o.o., camp), capacity limits, rješenje and categorisation procedure, documents, stars, plaque, minimum conditions, safety, insurance | `references/registration-categorisation.md` | `Capacity`, `Documents`, `Stars`, `Plaque`, `Safety`, `obrt` |
| eVisitor check-in/out, guest list, MUP, tourist tax (per night and flat rate), exemptions, deadlines, holiday-home owners, tourist board fee and TZ-2, fines | `references/evisitor-tourist-tax.md` | `24 h`, `Exempt`, `31 July`, `TZ-2`, `Fines`, `vikendaš` |
| Flat-rate income tax per bed, 2025 index ranges, 2027 proposal, quarterly payment, real income, VAT threshold, PDV-ID and reverse charge on commissions, 13% VAT, receipts, EP book, fiscalization and eRačun, property tax, DAC7, platform practicalities | `references/taxes-vat-platforms.md` | `Category I`, `PDV-ID`, `reverse`, `EP`, `fiscal`, `nekretnine`, `DAC7`, `Airbnb` |
| NN 152/24 amendments, co-owner consent (ZUOZ čl. 34), local capacity decisions, the new Hospitality Act (Final Proposal, Oct 2026), registration numbers, Reg. (EU) 2024/1028, rekategorizacija, ViDA | `references/regulation-2025-2026.md` | `152/24`, `čl. 34`, `35a`, `Final Proposal`, `2024/1028`, `1 May 2027` |
| Guest messages HR + EN: booking confirmation, check-in instructions, house rules, tourist-tax explanation, ID request, review request | `references/guest-communication-templates.md` | `Booking confirmation`, `Check-in`, `Kućni red`, `tourist tax` |
| All URLs and acts, with what each was used for | `references/sources.md` | act name, `porezna`, `mint` |

3. **Answer with sources.** Cite the act and article (e.g. "Zakon o turističkoj pristojbi čl. 17(2)")
   or the official URL. Give every amount with its year. Surface the relevant **VERIFY** items as
   questions for the local tourist board, the tax office or an accountant.
4. **Local amounts are local.** The flat-rate tax per bed (JLS decision) and the tourist tax (county
   decision) differ by place. Give the national range, then tell the user where the exact local
   figure is published (the Porezna uprava spreadsheet of JLS decisions; the county's official
   gazette; the local turistička zajednica; the eVisitor "Financije" view).
5. **Croatian text** (guest messages, house rules, letters to authorities): correct standard
   Croatian with the polite capital **Vi/Vaš/Vam** for one guest and lower-case **vi/vaš** for a group.
   Apply `croatia:croatian-language`.
6. **Hand-offs to other skills in this plugin:**
   - GDPR for guest data, website/booking terms, consumer law → `croatia:hr-legal-compliance`
   - obrt or d.o.o. for tourism, VAT registration in depth → `croatia:hr-business-admin`
   - fiscal receipts and eRačun implementation → `croatia:hr-fiscalization-dev`
   - seasonal workers (cleaners, receptionists) → `croatia:hr-payroll-employment`
   - buying property to rent, property tax detail → `croatia:hr-real-estate`
   - listing copy, local SEO for a rental website → `croatia:hr-seo-local`
   - season dates and public holidays → `croatia:hr-calendar`
   - OIB and IBAN validation in a booking form → `croatia:hr-identifiers`
   - number/date/currency formatting → `croatia:hr-localization`
   - grants for tourism investments → `croatia:hr-eu-funding`
7. **Do not invent local figures, article numbers or deadlines.** If research could not confirm
   something, say so and point to the office that can.
8. **Per-project memory.** If the user runs a rental business across sessions, store their pinned
   facts (municipality, beds, VAT status, platforms) in the project, e.g.
   `.claude/croatia/hr-tourism-rentals.md`. Never edit this skill's files.

## The rules that cover most cases (2026)

1. **Domaćinstvo** = a physical person (Croatian, EEA or Swiss national) renting property they own:
   max **10 rooms or 20 beds** (extra beds not counted), or a camp with max **10 units / 30 guests**
   (Zakon o ugostiteljskoj djelatnosti, ZUD čl. 30). Beyond that, or with services beyond breakfast,
   you need an obrt or a company (`references/registration-categorisation.md`).
2. **Nothing starts without a rješenje** (approval decision with the category) from the county
   administrative office, or the City of Zagreb (ZUD čl. 34). It is entered in the Središnji registar.
3. **eVisitor: register every guest within 24 h of arrival and deregister within 24 h of departure**
   (Zakon o turističkoj pristojbi, ZoTP čl. 22(1)).
4. **Tourist tax for domaćinstvo is an annual flat amount per bed**, including extra beds (ZoTP čl. 12).
   2026 national range: about **€46.45–132.72 per bed** (OPG: about €26.54–66.36). The exact amount
   is set by the county. Pay by **31 July**, or in three equal instalments on **31 July, 31 August
   and 30 September** (ZoTP čl. 17(2)).
5. **Tourist board membership fee (turistička članarina)** for non-bookkeeping renters, 2026:
   **€5.97 per main bed and €2.99 per extra bed**. File **TZ-2 via ePorezna by 15 January** (for 2026,
   by 15 Jan 2026). Pay in one sum by 31 July, or in three instalments: 31 July, 31 August, 30 September.
6. **Flat-rate income tax per bed** (since 1 Jan 2025, set by each JLS within ranges by tourism
   development index): **I: €100–300 · II: €70–200 · III: €30–150 · IV/0: €20–100** per bed per year.
   It is paid quarterly, a quarter of the annual amount **by 31 Mar, 30 Jun, 30 Sep and 31 Dec**.
   It is final, with no annual tax return. Only renters with up to 20 beds who are not VAT payers
   can use it.
7. **Booking.com / Airbnb commissions are B2B services from EU companies. The renter self-assesses
   25% Croatian VAT (reverse charge) even below the €60,000 VAT threshold.** This needs a
   **PDV-ID** (form P-PDV, at least 15 days before receiving the service). File the monthly PDV and
   PDV-S returns by the last day of the following month. A PDV-ID is not VAT registration.
8. **Receipts**: issue a numbered invoice for every stay (2 copies) unless an agency issues it, and
   record daily totals in the **EP (evidencija prometa)** book. Porezna uprava states that paušalist
   renters' invoices **do not need to be fiscalized**. VAT payers, obrti and companies do fiscalize.
9. **VAT payers** (over €60,000 turnover, or by choice) charge **13% VAT on accommodation** (Zakon o
   PDV-u čl. 38(3)(a)). They lose the flat-rate regime and are taxed on real income.
10. **Flat in a building**: since 1 Jan 2025, a new short-term rental needs the prior written consent of
    a **two-thirds majority of co-owners (by share) plus all adjoining co-owners**. Existing renters
    have five years, until the end of 2029 (Zakon o upravljanju i održavanju zgrada, ZUOZ čl. 34, 63;
    ZUD čl. 34(2)).
11. **Registration numbers (Reg. (EU) 2024/1028)**: the Regulation has applied since 20 May 2026, but
    Croatia has **not yet** required numbers. The Ministry says the obligation starts in 2027. The
    new Hospitality Act's Final Proposal (in Parliament since 21–22 Oct 2026) sets **1 May 2027**.
    Until then, no number is needed to advertise.
12. **DAC7**: platforms report each host's payouts, fees and property data to their EU tax authority
    by 31 January each year. Porezna uprava receives the data and matches it against paušal, VAT and
    eVisitor records.

## Annual calendar (domaćinstvo, flat-rate, not in VAT)

| When | What | Source |
|---|---|---|
| By **15 Jan** | TZ-2 (tourist board fee calculation for the previous year) via ePorezna | Zakon o članarinama u TZ čl. 11; Porezna uprava |
| By **31 Mar / 30 Jun / 30 Sep / 31 Dec** | Flat-rate income tax, ¼ of the annual amount each quarter | Pravilnik o paušalnom oporezivanju …; Porezna uprava |
| **Monthly**, by the last day of the next month | PDV + PDV-S for months with Booking/Airbnb/EU commissions (no zero returns) | Zakon o PDV-u; Porezna uprava |
| By **31 Jul** (or 31 Jul / 31 Aug / 30 Sep) | Tourist tax flat amount (eVisitor payment slips) | ZoTP čl. 17(2) |
| By **31 Jul** (or 31 Jul / 31 Aug / 30 Sep) | Tourist board membership fee | Zakon o članarinama u TZ |
| Within **24 h** of each arrival/departure | eVisitor check-in / check-out | ZoTP čl. 22(1) |
| **Daily** | EP book totals; an invoice per stay | Porezna uprava |
| Within **8 days** of a rješenje or any capacity change | Register with or notify the tax office (RPO form + copy of rješenje) | Porezna uprava |
| By **31 Jan** | Platforms send DAC7 data and give you a copy (no action, but check it) | Dir. 2021/514; Porezna uprava |
| After **31 Mar** ownership date | Property tax decision (porez na nekretnine) from the JLS, where applicable | Zakon o lokalnim porezima čl. 25 |
| Before **15 Dec** | JLS adopts next year's flat-rate tax per bed (check your municipality) | Zakon o porezu na dohodak; Porezna uprava |

## Quick figures 2026

| Item | 2026 amount | Source |
|---|---|---|
| Flat-rate income tax per bed, by JLS index category | I €100–300 (default €200); II €70–200 (€135); III €30–150 (€90); IV/0 €20–100 (€60) | porezna-uprava.gov.hr ("Iznajmljivač turistima", "Oporezivanje djelatnosti iznajmljivanja smještaja turistima") |
| Tourist tax per person per night (national range) | 1 Apr–30 Sep €1.33–2.65; rest of year €0.93–1.86 | Pravilnik NN 71/2019 čl. 2 (in kuna: 10–20 / 7–14 kn) **VERIFY** euro rounding |
| Tourist tax flat amount, domaćinstvo, per bed | €46.45–132.72 (350–1,000 kn) | Pravilnik NN 71/2019 čl. 2(2) |
| Tourist tax flat amount, OPG, per bed | ≈ €26.54–66.36 (200–500 kn) | same |
| Tourist tax flat amount, camp unit in domaćinstvo | €66.36–132.72 (500–1,000 kn) | same |
| Children | under 12 exempt; 12–18 pay 50% | ZoTP čl. 5(1), 6 |
| Tourist board fee, domaćinstvo | €5.97 per main bed, €2.99 per extra bed | local TZ notices for 2026; Pravilnik under Zakon o članarinama **VERIFY** class differences |
| Tourist board fee, OPG / camp unit | €2.65 per bed / €13.94 per unit | same **VERIFY** |
| VAT threshold (small business) | €60,000 (since 1 Jan 2025) | Zakon o PDV-u čl. 90; Porezna uprava |
| VAT on platform commission (reverse charge) | 25% | Zakon o PDV-u; Porezna uprava |
| VAT on accommodation (VAT payers) | 13% | Zakon o PDV-u čl. 38(3)(a) |
| Property tax (porez na nekretnine) | €0.60–8.00 per m² per year, set by the JLS | Zakon o lokalnim porezima; Porezna uprava |
| Domaćinstvo capacity limit | 10 rooms / 20 beds; camp 10 units / 30 guests | ZUD čl. 30(3) |
| Flat-rate tax eligibility | ≤ 20 beds; camp ≤ 10 units / 30 guests; not a VAT payer | Porezna uprava |
| Administrative fee for a rješenje request | €9.29 (example from a county office) | local office notice **VERIFY** |

## Keeping current

These facts go stale. Check them at the source:
- **Flat-rate tax per bed**: each JLS decides by 15 Dec. The Porezna uprava page "Oporezivanje
  djelatnosti iznajmljivanja smještaja turistima" links the JLS spreadsheets. A Sept 2026 government
  proposal would raise the minimums for categories I and II from 2027 (`references/taxes-vat-platforms.md`).
- **Tourist tax**: county decisions (published in the county's official gazette) and Pravilnik NN 71/2019.
  Check whether the ministry has issued a euro-denominated replacement.
- **Hospitality Act**: the new Zakon o ugostiteljskoj djelatnosti was in its second reading in late
  October 2026. Check narodne-novine.nn.hr and mint.gov.hr for the adopted text and dates.
- **Registration numbers**: mint.gov.hr news, and the eTurizam system.
- **Platform fees and invoicing**: Booking.com and Airbnb help centres. Airbnb moved EEA hosts to a
  host-only fee from 13 Oct 2026, so the VAT base grows (`references/taxes-vat-platforms.md`).
- **eRačun / fiscalization**: Porezna uprava's Fiskalizacija 2.0 pages (non-VAT issuers from 1 Jan 2027).
