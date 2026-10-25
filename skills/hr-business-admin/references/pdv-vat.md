# VAT (PDV) for small businesses – 2026

Status: researched 2026-10-25. ZPDV = Zakon o porezu na dodanu vrijednost (consolidated on zakon.hr, last
amendments NN 151/25, 52/25, 32/26). **VERIFY** marks unconfirmed points.

This file covers the business-admin side (registration, rates, PDV-ID, returns). For OSS, invoice elements,
fiscalization, Stripe fees and SaaS specifics, read `croatia:hr-legal-compliance` →
`references/04-tax-fiscalization-payments.md` §2–3 and §7–9 instead of repeating them here.

Contents: 1 Threshold and registration · 2 Rates · 3 Selling services abroad · 4 PDV-ID for non-VAT
businesses · 5 Buying services from abroad (reverse charge) · 6 Returns and deadlines · 7 Decision guide

---

## 1. Registration threshold (2026)

- **€60,000.00 annual domestic turnover** (value of supplies with a Croatian place of supply, excl. VAT) –
  below it a Croatian business is exempt (mali porezni obveznik, small taxpayer) (ZPDV čl. 90 st. 1, NN 152/24,
  from 1.1.2025; it was €40,000 in 2024).
- What counts: taxable domestic supplies and certain exempt supplies (čl. 90 st. 3). **B2B services taxed in
  another country (reverse charge abroad) and OSS sales do not count** toward the threshold (RRiF; see legal
  skill 04 §3.1). Sales of fixed assets are excluded (st. 4).
- **Crossing the threshold:** you become a VAT payer and must file the registration (P-PDV) – practitioners
  and PU guidance say within **8 days**, VAT applies from the day after the threshold is crossed (**VERIFY**
  exact article and start date in ZPDV čl. 79–90 / Pravilnik o PDV-u). A paušalist then also loses paušal
  (`pausalni-obrt.md` §8).
- **Voluntary registration:** possible below the threshold (to deduct input VAT, e.g. for B2B businesses with big
  purchases). Binding for the current and the next calendar year (practitioner sources; **VERIFY** in ZPDV
  čl. 90). Ends paušal.
- **EU cross-border SME scheme** (from 2025): a Croatian small taxpayer may apply the exemption in other member
  states if EU turnover ≤ €100,000, after prior notification; identification number = OIB + "EX" (ZPDV čl. 90
  st. 5–9). Rarely relevant for services; detail in legal skill 04 §3.1.

## 2. Rates (ZPDV čl. 38, as of 2026)

| Rate | Main items (abridged – check the Act for exact wording) |
|---|---|
| **25%** standard | Everything not listed below: most services, IT/SaaS, consulting, design, marketing, goods in general |
| **13%** | Accommodation in hotels and similar, campsites, nautical-tourism accommodation; preparing and serving food and desserts (catering); newspapers/periodicals not at 5%; children's car seats and nappies; menstrual products; public water supply and drainage; electricity; natural gas and district heating; firewood, pellets, briquettes, wood chips (see temporary 5% below); municipal waste collection; urns and coffins; authors'/composers'/performers' services via collective-rights organisations |
| **5%** | All bread; milk (not yoghurt etc.), infant formula; professional/scientific/educational books and textbooks; approved medicines; disability aids per HZZO list; cinema, concert, sports and cultural event tickets; daily newspapers of a media publisher; scientific journals; baby food; edible oils and fats, butter, margarine; live animals, fresh/chilled meat, sausages, fish, seafood, crustaceans; fresh vegetables, fruit, nuts; fresh eggs; seeds and seedlings; fertilisers and pesticides; animal feed (not pet food) |
| **5% temporary** | Natural gas until 31.3.2027 (čl. 38 st. 4). District heating and firewood/pellets were at 5% until 31.3.2026 (st. 5) – now 13% unless extended (**VERIFY**) |
| **0%** | Supply and installation of solar panels on homes and public-interest buildings (čl. 38 st. 6) |

Private accommodation (iznajmljivači) VAT rules: `croatia:hr-tourism-rentals`.

## 3. Selling services abroad – place of supply

- **B2B (customer is a business):** place of supply = customer's seat (ZPDV čl. 17 st. 1, = VAT Directive art.
  44). To an EU business: **no Croatian VAT; the customer self-assesses (reverse charge)**. Check the customer's
  VAT number in **VIES** and keep proof.
- **B2C (customer is a consumer):** general rule = supplier's seat (čl. 17 st. 2), so Croatian VAT (or the
  small-taxpayer exemption). Exceptions: electronically supplied services, telecoms and broadcasting to EU
  consumers are taxed where the consumer lives once EU-wide sales exceed €10,000 (OSS) – legal skill 04 §3.4.
- **Non-EU B2B:** outside Croatian VAT under čl. 17 st. 1; report the value in the PDV return if you are
  registered or have a PDV-ID (legal skill 04 §3.5).
- **Invoice wording for reverse charge:** ZPDV čl. 79 st. 7 requires **"prijenos porezne obveze"** or the English
  **"reverse charge"** when the customer pays the VAT. Common, compliant formulation for EU B2B services:
  *"Prijenos porezne obveze / Reverse charge – čl. 17. st. 1. Zakona o PDV-u (čl. 196. Direktive 2006/112/EZ)"*,
  with both parties' VAT ID numbers. For a paušalist do not combine this with the čl. 90 exemption note (legal
  skill 04 §2.1). For non-EU B2B, a common wording is *"PDV nije obračunat – mjesto obavljanja usluge izvan RH,
  čl. 17. st. 1. Zakona o PDV-u"* (**VERIFY** preferred wording with your accountant).

## 4. PDV-ID for businesses outside the VAT system

- A **non-VAT small taxpayer (paušalist, small obrt, non-VAT j.d.o.o./d.o.o.) needs a PDV identifikacijski broj
  (HR + OIB) before** it (a) supplies services to a business in another EU member state, or (b) receives services
  from an EU (or other foreign) supplier that are taxable in Croatia under reverse charge (ZPDV čl. 77; Pravilnik
  o PDV-u; legal skill 04 §3.2–3.3).
- Getting a PDV-ID is **not** entering the VAT system: the business stays exempt on domestic sales and paušal is
  not lost.
- Apply at the local PU office / via ePorezna (form P-PDV); practitioners say allow about 15 days.
- Consequence: file **PDV**, **ZP** (for EU B2B supplies) and/or **PDV-S** (for EU services received) for each
  period in which such transactions happened (§6).

## 5. Buying services from abroad (Google Ads, Meta, SaaS, Stripe…)

- When a Croatian business buys a service from a foreign supplier, the place of supply is Croatia (čl. 17 st. 1)
  and **the Croatian buyer self-assesses 25% VAT** (reverse charge).
- **VAT payer:** reports output VAT and deducts the same amount as input VAT → net zero, but must report it.
- **Non-VAT business (paušalist etc.): pays the 25% with no deduction** – a real 25% surcharge on Google Ads,
  Meta ads, foreign SaaS, AWS, OpenAI and similar, plus PDV-ID and monthly PDV + PDV-S returns.
- Give the foreign supplier your **PDV-ID (HR…)** so it invoices without its own VAT; if you gave only the OIB or
  no number, the supplier may charge its own country's VAT (e.g. Irish VAT) – then Croatian reverse charge does
  not apply but you cannot recover the foreign VAT either (**VERIFY** the correction route with an accountant).
- **Stripe:** card-processing fees are usually exempt financial services; Stripe Billing/Tax/Radar fees are likely
  taxable → reverse charge (legal skill 04 §3.3; **VERIFY** on Stripe's tax invoices).
- **PayPal, Wise, Payoneer** fees: generally exempt payment services – **VERIFY** each invoice.

## 6. Returns and deadlines (from 1.1.2026)

| Form | Who / when | Deadline |
|---|---|---|
| **PDV** (VAT return) | VAT payers each period; PDV-ID holders for periods with EU B2B supplies or reverse-charged purchases | **Last day of the following month** (ZPDV čl. 85 st. 6, NN 151/25 – was the 20th until 2025) |
| **ZP** (Zbirna prijava, EC sales list) | Supplies of goods/services to EU VAT-registered customers | Last day of the following month (čl. 88 st. 2, NN 151/25) |
| **PDV-S** (services received from EU) | EU services received under reverse charge | Last day of the following month (čl. 86 st. 2, NN 151/25) |
| VAT payment | VAT payers | Last day of the month after the period (čl. 76 st. 1) |
| OSS return | OSS-registered | Last day of the month after the quarter (legal skill 04 §3.4) |
| URA, PPO forms | — | **Abolished from 2026** (NN 151/25) |

- **Tax period:** monthly by default. **Quarterly** if supplies incl. VAT in the previous year were under
  €110,000, **unless the business makes intra-EU transactions** (ZPDV čl. 84 st. 1–3) – so a freelancer with EU
  clients files monthly.
- Filing is electronic through **ePorezna**.

## 7. Decision guide – what VAT setup does this business need?

1. Domestic turnover expected above €60,000 within 12 months → VAT registration (and no paušal).
2. Mostly B2B clients who are VAT payers and large purchases with VAT → consider voluntary registration (VAT is
   neutral for the client, input VAT is recoverable). Lose paušal.
3. Mostly consumers (B2C) in Croatia → staying exempt keeps prices 25% lower; watch the €60,000 limit.
4. Any EU B2B client or any foreign service bought → **PDV-ID now**, monthly PDV/ZP/PDV-S in active months.
5. EU consumers buying e-services → €10,000 OSS threshold (legal skill 04 §3.4).

Start any calculation output with the calculation-output header from SKILL.md.
