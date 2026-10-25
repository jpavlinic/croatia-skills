# Taxes, VAT, receipts, fiscalization, DAC7 and platforms

Status: researched 2026-10-25. Main sources:
- Porezna uprava pages "Iznajmljivač turistima" and "Oporezivanje djelatnosti iznajmljivanja
  smještaja turistima"
- Zakon o porezu na dohodak (amended NN 152/24, in force 1 Jan 2025)
- Pravilnik o paušalnom oporezivanju djelatnosti iznajmljivanja i organiziranja smještaja u turizmu
- Zakon o PDV-u
- Zakon o lokalnim porezima (ZLP)
- Zakon o fiskalizaciji (Fiskalizacija 2.0)
- Zakon o administrativnoj suradnji u području poreza (DAC7)

## 1. Income tax: flat rate per bed (paušalni porez)

**Eligibility** (all must apply, per Porezna uprava):
1. a rješenje for domaćinstvo services;
2. **not** a VAT payer for this activity (the threshold has been €60,000 since 1 Jan 2025);
3. income not determined from business books;
4. **≤ 20 beds** in houses, apartments or rooms the renter owns; camp or robinson ≤ 10 units / 30 guests.

Otherwise the income is taxed as **self-employment income** (dohodak od samostalne djelatnosti),
based on real income and expenses.

**How the amount is set (since 1 Jan 2025)**: each city or municipality (JLS) sets an amount per bed
(per camp unit, per robinson unit) **within a range fixed by its category under the tourism
development index** (indeks turističke razvijenosti). The decision must be adopted by **15 December**
to apply from 1 January of the next year, and it stays in force until changed.

| JLS category (index) | Range per bed / unit per year | Default if the JLS adopts no decision |
|---|---|---|
| I | **€100–300** | €200 |
| II | **€70–200** | €135 |
| III | **€30–150** | €90 |
| IV and 0 | **€20–100** | €60 |

Source: porezna-uprava.gov.hr (both pages above). Porezna uprava publishes spreadsheets of every
JLS's adopted amount for 2024, 2025 and 2026. Look up the property's municipality there.

**Formula**: annual tax = number of beds (or units) × the JLS amount per bed. Extra beds: check the
JLS decision and the Pravilnik. Porezna's guide counts beds as stated in the rješenje. **VERIFY**
whether extra beds count for the income-tax paušal, as they do for the tourist tax.

**Payment**: quarterly, **¼ of the annual amount by the last day of each quarter**: **31 Mar, 30 Jun,
30 Sep, 31 Dec**. It is prorated by quarter if capacity changes mid-year. The tax is **final**: no
annual income-tax return, and costs cannot be deducted. Since 2020 it has been paid to the
municipality where the property is. Surtax (prirez) was abolished from 2024.

**Registration**: within **8 days** of the rješenje, file **RPO** and a copy of the rješenje with the
tax office. Report changes (beds, closure) within 8 days. Porezna issues a new decision from
1 January of the following year.

**Proposed change for 2027** (Government proposal, 10 Sep 2026; Hina via index.hr and poslovni.hr):
- Category I: minimum **€100 → €150**; default **€200 → €225**.
- Category II: minimum **€70 → €100**; default **€135 → €150**.
- **VERIFY** whether Parliament adopted it, and the JLS decisions for 2027 (deadline 15 Dec 2026).

**Paušal vs real income**: the flat rate is usually cheaper for small renters with high occupancy.
Real-income taxation (keeping books, deducting costs, contributions) makes sense mainly for large
investments or a business set-up. Get an accountant's comparison → `croatia:hr-business-admin`.

## 2. VAT (PDV)

### Not a VAT payer, but a PDV-ID for platform commissions
- Booking.com (Booking.com B.V., Netherlands) and Airbnb (Airbnb Ireland UC) invoice their
  commission or service fee to the host as a **B2B service**. The place of supply is Croatia
  (Zakon o PDV-u, general B2B rule), so **the host self-assesses Croatian VAT at 25%** (reverse charge,
  prijenos porezne obveze), even when the host is not in the VAT system.
- **PDV-ID**: request it with form **P-PDV** at least **15 days before** receiving the service from an
  EU supplier. A PDV-ID is **not** VAT registration: the renter stays outside VAT for the
  accommodation itself (Zakon o PDV-u čl. 90 exemption) and keeps the flat-rate tax.
- Non-EU suppliers (e.g. a US-based platform entity): no PDV-ID is needed, but VAT on the service
  is still due.
- **Returns**: file **PDV** and, for EU services, **PDV-S**, electronically (ePorezna, credentials of
  security level 2 or 3), **by the last day of the month after the month** in which the service was
  received. Pay the VAT to the state budget: IBAN per Porezna, **model HR68, reference 1201-OIB**.
  **Do not file zero returns** for months with no commission.
- ZUD čl. 32(2): when advertising to EU taxable persons (the platforms), show the OIB or PDV-ID.
  Platforms ask for it in the host account.
- **Commission base**: VAT is due on the full commission or fee on the platform invoice, including
  "payments" and other fees billed to the host. Download monthly invoices from the extranet or
  host dashboard.

**Airbnb 2026 fee change**: from **13 October 2026**, EEA hosts moved to Airbnb's host-only
("simplified") fee, generally **15.5%** of the booking subtotal (14–16% for some), replacing the
split ~3% host fee + guest fee (Airbnb notices; Croatian press July–October 2026). For Croatian
hosts this multiplies the reverse-charge VAT base about five-fold: 25% of 15.5% ≈ **3.9% of each
booking**. Adjust prices and budget for the monthly PDV. **VERIFY** the exact percentage in your
Airbnb account.

### Becoming a VAT payer
- Mandatory when supplies in the current or previous year exceed **€60,000** (Zakon o PDV-u čl. 90;
  from 1 Jan 2025). Voluntary registration is possible.
- A VAT payer charges **13% VAT on accommodation** (smještaj, smještaj s doručkom, polupansion,
  puni pansion) (Zakon o PDV-u čl. 38(3)(a)). Other services (e.g. transfers, minibar, extra
  services) are generally at **25%**. **VERIFY** item by item.
- It loses the flat-rate income tax and is taxed on real income. It must issue and receive
  **eRačun** for B2B and fiscalize B2C receipts (Fiskalizacija 2.0) → `croatia:hr-fiscalization-dev`.
- Input VAT on the platform commission becomes deductible.

### ViDA (EU "VAT in the Digital Age")
Directive (EU) 2025/516 introduces a **deemed-supplier rule**: from **1 July 2030** platforms will
be liable for VAT on short-term accommodation when the host does not charge VAT. Member states may
take an option not to apply it in some cases. **VERIFY** Croatia's choice nearer the date.

## 3. Receipts, EP book, fiscalization, eRačun

**Invoice (račun)** for every service, unless an agency issues it (ZUD čl. 32(1)(4)). Per Porezna:
- at least **2 copies**;
- content: number and date; the renter's name, address and **OIB**; place of service; the guest's
  name; description and quantity (e.g. nights × unit); total amount; the note on the VAT exemption
  (e.g. "PDV nije obračunan temeljem čl. 90. st. 1. Zakona o PDV-u");
- "Tourist tax included" may be stated. It is not shown separately for flat-rate payers.

**EP book (evidencija prometa, obrazac EP)**: record the daily total of all invoices issued,
**including unpaid ones**. The yearly total goes on TZ-2.

**Fiscalization**: Porezna uprava states that invoices of flat-rate renters in domaćinstvo **do not
have to be fiscalized**, whether the guest pays cash, by card or by bank transfer. Renting is
taxed as income from property, not self-employment.
- Obrti, companies and renters taxed on real income as self-employment **do** fiscalize B2C
  receipts. From 1 Jan 2026 this also covers payments to a bank account (Fiskalizacija 2.0).
- **eRačun**: from 1 Jan 2026, VAT payers issue and receive eRačun B2B. Non-VAT obligated persons
  receive eRačun from 2026 and issue from **1 Jan 2027** (Porezna uprava, "Izdavatelji i primatelji
  eRačuna"). Porezna's example says a **non-resident** VAT-registered renter paying the flat rate
  is not obliged to issue or fiscalize eRačun.
- **VERIFY** for a resident flat-rate renter with only a PDV-ID whether Fiskalizacija 2.0
  obligations (receiving eRačun) apply. The Porezna pages do not address renters explicitly. The
  free **MIKROeRAČUN** app in ePorezna exists for non-VAT persons.
- **Platform payouts** (Booking/Airbnb collect and pay out): the renter still issues an invoice to
  the guest, or to the platform or agency, depending on the contract. Porezna: whether the
  invoice goes to the guest or the agency depends on the contract that sets the sale price and
  commission. Booking.com "Payments by Booking" and Airbnb act as payment collectors for the host.
  **VERIFY** your contract.

## 4. Property tax (porez na nekretnine), from 2025

- Introduced **1 Jan 2025** to replace the holiday-house tax (porez na kuće za odmor). Each JLS
  sets **€0.60–8.00 per m²** of usable floor area per year (Porezna uprava; ZLP).
- Payable by the owner as of **31 March** of the tax year (ZLP čl. 25(1)), on a JLS decision.
- **Paying the flat-rate income tax or other taxes on renting does not affect** property-tax status
  (ZLP čl. 25(4)). So an apartment rented to tourists that nobody lives in permanently is generally
  **taxable**, in addition to the flat rate.
- Exemptions (ZLP čl. 27) include property used for **permanent residence**, property in long-term
  rental, and property that serves a **domaćin** (ZUD čl. 30a) as permanent residence (čl. 27(1)(9)).
- If the JLS's **communal fee decision** classifies the unit with a business-premises coefficient
  (koeficijent namjene za poslovni prostor), it is **not a "nekretnina"** under ZLP čl. 2(1)(12),
  so no property tax is due (RRIF opinion, 2025, quoting ZLP). In that case the higher communal fee
  applies instead.
- Detail → `croatia:hr-real-estate`.

## 5. DAC7: what the platforms report

- Directive (EU) 2021/514 (DAC7), transposed in the **Zakon o administrativnoj suradnji u području
  poreza** and the **Pravilnik o automatskoj razmjeni informacija u području poreza** (Porezna
  uprava, "Obveze za operatere platformi (DAC7)"). Applies from reporting year 2023.
- Platforms report to the tax authority of their EU establishment (e.g. Booking.com → NL, Airbnb →
  IE), which forwards the data to Croatia. Croatian platform operators report to Porezna uprava by
  **31 January** of the following year.
- Data per host: identity (name, address, OIB/TIN, date of birth), financial account (IBAN), and
  for each **property**: its address, land-registry number where available, **total consideration
  per quarter**, **number of days rented**, and **fees/commissions/taxes withheld per quarter**
  (Dir. 2021/514, Annex V, Section III(B)). **VERIFY** the paragraph numbers.
- The platform must give the host a copy of the reported data by 31 January.
- No small-host exclusion for accommodation. The 30-sales / €2,000 exclusion applies only to sales
  of goods. Hosts with more than 2,000 rentals of the same listing per year (hotels) are excluded.
- **Practical point**: Porezna uprava matches DAC7 data with eVisitor nights, rješenja and
  paušal/VAT records. Unregistered listings and nights not in eVisitor are detectable. Under-declared
  commissions (missing PDV returns) are also visible.

## 6. Platform practicalities (Booking.com, Airbnb, Vrbo, agencies)

- **Listing data**: type and category exactly as in the rješenje; capacity no larger than the
  rješenje; OIB or PDV-ID in the account. From 2027, the **registration number**.
- **Invoices from the platform**: monthly commission invoices (Booking: extranet → Finance;
  Airbnb: host dashboard → transaction history and VAT invoices). Keep them for the PDV return and
  for 11 years (general retention under the Opći porezni zakon; **VERIFY**).
- **Guest payments**: "payments by platform" (the platform collects, deducts the commission and pays
  out) or guest pays the property (cash, card terminal, bank transfer). Either way, the host issues
  an invoice to the guest (or the agency per contract) and records it in the EP book.
- **Tourist tax in the listing**: for flat-rate hosts it is included in the price. Do not configure
  a separate per-night "city tax" charge unless your price list and invoices match it.
- **Cancellation policies**: choose a policy and state it identically on every channel and on your own
  website. Consumer law on distance contracts excludes accommodation for a specific date from
  the 14-day withdrawal right (ZZP; Dir. 2011/83/EU Art 16(l)). The contractual cancellation terms
  therefore govern → `croatia:hr-legal-compliance`.
- **Reviews**: respond politely and factually. Do not offer incentives for positive reviews. Fake
  reviews breach the platforms' rules and consumer law.
- **Channel managers / PMS**: they sync calendars and prices across platforms and often connect to
  eVisitor. Choose one that supports eVisitor check-in, invoice numbering and the EP book. This
  skill does not endorse any vendor.
- **Agencies** (domestic tour operators): the contract sets the price and commission. A domestic
  agency's commission invoice carries Croatian VAT (no reverse charge), or none if the agency is not
  in VAT.
