---
name: hr-business-admin
description: >-
  Starting and running a small business in Croatia: choosing obrt / paušalni obrt / slobodno zanimanje /
  j.d.o.o. / d.o.o., registration (e-Obrt, START), owner taxes and contributions (doprinosi), paušal classes,
  PO-SD, KPR, KPI, porez na dohodak, porez na dobit, dividends, director contributions, PDV threshold and
  PDV-ID, reverse charge, ZP/PDV-S, freelancing for foreign clients, drugi dohodak (ugovor o djelu, autorski
  honorar), bookkeeping, GFI, accountant costs, mirovanje, odjava obrta, likvidacija. Triggers: "obrt",
  "paušalni obrt", "paušal", "paušalist", "j.d.o.o.", "d.o.o.", "otvoriti firmu", "otvaranje obrta",
  "start a business in Croatia", "freelancer Croatia", "sole trader Croatia", "PDV prag", "PDV ID",
  "porez na dobit", "doprinosi", "PO-SD", "KPR", "računovođa", "drugi dohodak", "ugovor o djelu",
  "autorski honorar", "zatvaranje obrta", "likvidacija d.o.o.", "how much tax do I pay in Croatia".
---

# Croatian small-business admin (obrt, paušal, j.d.o.o., d.o.o.)

Research-based knowledge for choosing a legal form, registering, paying owner taxes and contributions,
handling VAT, invoicing foreign clients, keeping books and closing a small business in Croatia.

Status: researched 2026-10-25. Figures are for **tax year 2026**. Items marked **VERIFY** in the references are
not confirmed against a primary source or are still changing (notably the announced **2027 paušal reform**).

> **Not legal, tax or financial advice.** This skill provides general, research-based information that may be
> incomplete or out of date. Always verify with the official sources cited and consult a qualified professional
> (lawyer / odvjetnik, tax adviser / porezni savjetnik, accountant / računovođa) before acting.

## Disclaimer rules (always apply)

1. **End every answer that touches tax, accounting or law** with one line in the user's language:
   - EN: *This is general information, not legal or tax advice. Check the cited sources and consult a professional.*
   - HR: *Ovo su opće informacije, a ne pravni ni porezni savjet. Provjerite navedene izvore i posavjetujte se sa stručnjakom.*
2. **Start every generated document, template or calculation** (cost comparison, tax estimate, invoice text,
   checklist meant to be followed) with:
   - HR: `PREDLOŽAK – nije pravni savjet. Prilagodite ga svom slučaju i dajte ga na provjeru stručnjaku.`
   - EN: `TEMPLATE – not legal advice. Adapt it to your case and have it reviewed by a professional.`
   Calculations also say "estimate only" and the year whose rules they use.
3. Present **VERIFY** items as questions for an accountant or Porezna uprava, never as settled.
4. Never apply 2026 figures to another year without saying so. For 2027, check whether the announced paušal
   changes have been published (references/pausalni-obrt.md §10).

## How to use

1. **Read project memory** if it exists: `.claude/croatia/business-admin.md` in the user's project (legal form,
   VAT status, city, decisions). Offer to save pinned facts there; never edit this skill's files.
2. **Pin the facts that change the answer** (ask, or state your assumptions):
   - legal form now or planned (none / paušal obrt / obrt na dohodak / slobodno zanimanje / j.d.o.o. / d.o.o.);
   - VAT status (outside VAT, PDV-ID only, VAT payer);
   - **employed elsewhere full time? pensioner?** (changes contributions completely);
   - clients: B2B or B2C; domestic, EU or non-EU; buys foreign services (ads, SaaS)?
   - expected annual receipts and real expenses; city of residence (income-tax rate);
   - first-ever obrt (HOK exemption), registered unemployed (HZZ grant – before registering!).
3. **Load only the reference you need** (grep first; they are long):

| Question | Reference | Grep hints |
|---|---|---|
| Which form? Comparison, liability, costs | `references/legal-forms.md` | `Comparison`, `How to choose`, `NKD`, `vezani` |
| Paušal: classes, tax, contributions, PO-SD, KPR, leaving paušal, side job, pensioner, 2027 | `references/pausalni-obrt.md` | `Class`, `290.98`, `druga djelatnost`, `PO-SD`, `2027` |
| Obrt na dohodak / dobit, slobodno zanimanje, city rates, KPI, advances | `references/obrt-dohodak.md` | `19.a`, `472.84`, `KPI`, `predujam` |
| d.o.o./j.d.o.o.: capital, reserves, profit tax, director contributions, dividends, GFI | `references/doo-jdoo.md` | `390.a`, `727.45`, `dividend`, `GFI`, `30 April` |
| VAT: threshold, rates, PDV-ID, reverse charge, ZP/PDV-S, foreign SaaS | `references/pdv-vat.md` | `60,000`, `13%`, `PDV-ID`, `PDV-S`, `Google` |
| Foreign clients, ugovor o djelu, autorski honorar, Wise/PayPal, digital nomads | `references/freelancing-foreign-clients.md` | `drugi dohodak`, `30%`, `Reverse charge`, `Wise` |
| Registering, e-services, accountant, retention, mirovanje, odjava, likvidacija | `references/registration-and-closing.md` | `START`, `e-Obrt`, `ePorezna`, `mirovanje`, `472.a` |
| Sources and open VERIFY list | `references/sources.md` | `VERIFY` |

4. **Delegate** what other skills own:
   - fiscalization, eRačun, invoice elements, OSS, Stripe, impressum, GDPR → `croatia:hr-legal-compliance`
     (`references/04-tax-fiscalization-payments.md`); code for receipts/eRačun → `croatia:hr-fiscalization-dev`;
   - employees, director salary, student work → `croatia:hr-payroll-employment`;
   - private accommodation → `croatia:hr-tourism-rentals`; HZZ and EU grants → `croatia:hr-eu-funding`;
   - deadlines calendar → `croatia:hr-calendar`; OIB/IBAN/HUB-3 → `croatia:hr-identifiers`;
   - any Croatian text you write → `croatia:croatian-language`.
5. **Paušal estimate:** `python3 scripts/pausal_estimate.py <receipts> [--status main|employed|pensioner]
   [--hok-exempt] [--months N]` (2026 rules, estimate only; `--self-test` passes). Show the result with the
   calculation header and the sources it prints.
6. **Answer** with the user's numbers, ranges where uncertain, the rule's source (act + article or NN), the
   relevant VERIFY items, and the closing disclaimer line.

## Quick comparison (2026)

| | Paušalni obrt | Obrt na dohodak | j.d.o.o. / d.o.o. |
|---|---|---|---|
| Limit / capital | Receipts ≤ €60,000, outside VAT | None | €1 (j.d.o.o.) / €2,500 (d.o.o.) |
| Liability | Unlimited | Unlimited | Limited |
| Income/profit tax | 12% of class income: €203.40–€1,080/yr | City rates 15–23% / 25–33%, €60,000 band | 10% (< €1M revenue) / 18% |
| Owner contributions | €290.98/month; side job: ≈17.5% of class base/yr; pensioner 0 | €472.84/month | Director not employed elsewhere: €727.45/month |
| Books | KPR + PO-SD (15.1.) | KPI, DI + DOH (end Feb) | Double entry, GFI + PD (30.4.) |
| Money out | Free | Free | Salary or dividend 12% (≈20.8% with profit tax) |
| Closing | Odjava | Odjava | Liquidation or ZTD čl. 472.a shortened procedure |

## Key facts 2026 (cover most questions)

- **Average wage for contribution bases 2026: €1,993.00** (NN 150/2025). Bases: paušal €797.20; obrt na dohodak
  €1,295.45; slobodno zanimanje / obrt na dobit €2,192.30; non-employed director €1,993.00; minimum €757.34.
- **Rates:** MIO 15% + 5% (or 20%), HZZO 16.5% (ZOD čl. 13, 14, 17); drugi dohodak and druga djelatnost: MIO 10%,
  HZZO 7.5%. Contributions due by the **15th** for the previous month.
- **Paušal:** 7 classes, tax 12% of paušal income (ZPD čl. 82; Pravilnik NN 1/24, 16/25), paid **by the last day
  of each quarter**; **PO-SD by 15 January** via ePorezna; KPR is the only book; every B2C invoice fiscalized
  since 1.1.2026; eRačun issuing for non-VAT businesses from 1.1.2027.
- **Income tax:** cities set rates within bands since 2024 (no prirez); lower rate up to €60,000 annual base;
  allowance €600/month (ZPD čl. 14, 19, 19.a).
- **Profit tax:** 10% / 18% at €1M revenue (ZPDob čl. 28); **dividends 12%** (ZPD čl. 70 st. 19).
- **VAT:** threshold **€60,000** (ZPDV čl. 90); rates 25 / 13 / 5% (čl. 38); EU B2B services → reverse charge,
  invoice note "prijenos porezne obveze" / "reverse charge" (čl. 79 st. 7); **PDV-ID needed even outside VAT** for
  EU B2B sales or foreign services bought; PDV, ZP, PDV-S due the **last day of the following month** from 2026.
- **Companies:** j.d.o.o. max 5 members and 1 director, 1/4 of profit to reserves until €2,500 (ZTD čl. 390.a);
  GFI to FINA by 30 April (ZOR čl. 50); records ≥ 11 years (ZOR čl. 10).
- **Cash:** no business cash payments of €10,000 or more (AML law); €700 per invoice between fiscalization obligors.

## Be realistic

- There is no universally "best" form. Show the trade-off with the user's numbers and say what would change it.
- Separate hard law (cited) from practice and market estimates (labelled as such).
- If the facts are missing, ask or state the assumption; do not guess a city rate or a VAT status.
- Point to an accountant for anything with real money at stake: switching regimes, crossing €60,000, closing a
  company, foreign social security.

## Keeping current

| Fact | Changes | Check |
|---|---|---|
| Average wage and contribution bases | Every year (Naredba in NN, December) | narodne-novine.nn.hr, porezna-uprava.gov.hr |
| Paušal classes, 12% rate, limit | 2027 reform announced (classes > €40,000) | esavjetovanja.gov.hr, NN, zakon.hr (ZPD, Pravilnik) |
| City income-tax rates | Any 1 January | PU "Pregled stopa poreza na dohodak" |
| VAT threshold, rates, deadlines | Annual tax packages | zakon.hr ZPDV, PU news |
| Fiscalization / eRačun dates | 2026–2027 phase-in | `croatia:hr-legal-compliance` ref 04, fiskalizacija.gov.hr / PU |
| Court fees, START, HITRO.HR, e-Obrt | Irregular | gov.hr, sudreg.pravosudje.hr |
| HOK / HGK fees | Chamber decisions | hok.hr, hgk.hr |
