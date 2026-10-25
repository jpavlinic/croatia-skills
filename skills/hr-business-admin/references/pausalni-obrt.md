# Paušalni obrt (flat-rate sole trader) – 2026

Status: researched 2026-10-25. Applies to tax year **2026**. Items marked **VERIFY** are not confirmed in a
primary source or are changing.

Contents: 1 Who can use paušal · 2 Classes and tax 2026 · 3 Contributions 2026 · 4 Paušal next to employment,
pensioners · 5 Deadlines · 6 Records (KPR, PO-SD) · 7 Fiscalization and eRačun · 8 When paušal ends ·
9 Other costs · 10 2027 reform (pending) · 11 Worked example

---

## 1. Who can use paušal (paušalno oporezivanje)

- **Legal basis:** Zakon o porezu na dohodak (ZPD) čl. 82 st. 1: an obrtnik (sole trader) carrying on an
  activity under ZPD čl. 29 st. 1 t. 1 (obrt and other business activities) or st. 3 (agriculture/forestry),
  who is **not a VAT payer** and whose **annual receipts (primici)** do not exceed the VAT registration
  threshold, may have income and tax set as a flat amount.
- **Limit 2026: €60,000.00 receipts** per calendar year: ZPD čl. 82 st. 1 refers to the VAT threshold, which is
  €60,000.00 under Zakon o PDV-u čl. 90 st. 1 (NN 152/24, from 1.1.2025).
  - Receipts = money actually received (cash basis), not invoiced amounts.
  - **VERIFY** with an accountant how receipts from EU/non-EU B2B services (place of supply abroad) are treated
    for the paušal limit as opposed to the VAT threshold: the VAT threshold counts only supplies with a Croatian
    place of supply, while ZPD čl. 82 speaks of "ukupni godišnji primitak" from the activity. Practitioners
    disagree; PU's position should be checked (pisitenam.porezna-uprava.hr) before relying on the narrower
    reading.
- **Slobodna zanimanja (liberal professions, ZPD čl. 29 st. 2)** such as lawyers, doctors, architects,
  engineers, translators, consultants registered as slobodno zanimanje **cannot** use paušal: čl. 82 st. 1 covers
  only čl. 29 st. 1 t. 1 and st. 3. Many IT and consulting activities can be done as an obrt instead (see
  `legal-forms.md`).
- A paušalist does **not** keep business books, only the turnover record (evidencija o prometu) (ZPD čl. 82
  st. 4). Expenses are not deductible: the tax is a fixed amount by class.
- A paušalist may have employees; then payroll rules apply (`croatia:hr-payroll-employment`). **VERIFY** any
  limits in the Pravilnik for the current year.

## 2. Classes and annual tax 2026

Tax = **12% of the annual paušal income** of the class (ZPD čl. 82 st. 6, NN 114/23 and 152/24). Since the
2024 reform the paušal tax **does not depend on the city**: the city surtax (prirez) was abolished from
1.1.2024 and the 12% rate is fixed in the Act. (Before 2024: 10% plus local prirez.)

Paušal income = upper class limit minus 85% normed expenses. Classes: Pravilnik o paušalnom oporezivanju
samostalnih djelatnosti čl. 3 (NN 1/20 … 1/24; classes 6 and 7 added by NN 16/25, in force 1.2.2025). The same
seven amounts are listed as contribution bases in the Naredba for 2026 (NN 150/2025 čl. 14), which confirms them.

| Class | Annual receipts (EUR) | Annual paušal income | **Annual tax 2026** | Quarterly | Monthly equivalent |
|---|---|---|---|---|---|
| 1 | 0.00 – 11,300.00 | 1,695.00 | **203.40** | 50.85 | 16.95 |
| 2 | 11,300.01 – 15,300.00 | 2,295.00 | **275.40** | 68.85 | 22.95 |
| 3 | 15,300.01 – 19,900.00 | 2,985.00 | **358.20** | 89.55 | 29.85 |
| 4 | 19,900.01 – 30,600.00 | 4,590.00 | **550.80** | 137.70 | 45.90 |
| 5 | 30,600.01 – 40,000.00 | 6,000.00 | **720.00** | 180.00 | 60.00 |
| 6 | 40,000.01 – 50,000.00 | 7,500.00 | **900.00** | 225.00 | 75.00 |
| 7 | 50,000.01 – 60,000.00 | 9,000.00 | **1,080.00** | 270.00 | 90.00 |

Note: some commercial sites list class 2 as €274.32; 2,295.00 × 12% = €275.40 is the arithmetic result from the
official base. If PU's rješenje or ePorezna shows a different figure, follow PU.

**Relief:** ZPD čl. 43 gives 50% / 100% relief for self-employed people in Vukovar and assisted areas of group I
(potpomognuta područja I. skupine) **only if** they employ more than two workers on permanent contracts with
residence conditions. **VERIFY** whether and how this applies to a paušalist.

## 3. Contributions (doprinosi) 2026 – paušal as main activity

Basis: Zakon o doprinosima (ZOD) čl. 68–71: the paušalist is the payer; PU sets the obligation by rješenje.
Monthly base = average wage × 0.4 (ZOD čl. 70).

- **Average wage for 2026:** €1,993.00 (Naredba o iznosima osnovica za obračun doprinosa za 2026. godinu,
  NN 150/2025, čl. 2).
- **Base 2026:** €797.20 per month (NN 150/2025 čl. 7).

| Contribution | Rate (ZOD) | Monthly 2026 |
|---|---|---|
| MIO I. stup (pension pillar I) | 15% (čl. 13 st. 1 t. 1.2) | 119.58 |
| MIO II. stup (pension pillar II) | 5% (čl. 17) | 39.86 |
| Zdravstveno osiguranje (HZZO) | 16.5% (čl. 14 st. 1) | 131.54 |
| **Total** | 36.5% | **290.98 / month = 3,491.76 / year** |

- Insured only in pillar I: MIO 20% (159.44) instead of 15% + 5%; the total is the same.
- **Due by the 15th of the month for the previous month** (ZOD čl. 71). Paid to the accounts on PU's rješenje
  (payment details: ePorezna → Porezna kartica; HUB-3 slips → `croatia:hr-identifiers`).
- The amount is the same in every class: contributions do not depend on revenue in 2026.

## 4. Paušal next to employment (druga djelatnost) and pensioners

- **Owner employed full-time elsewhere:** the obrt is a "druga djelatnost" (ZOD čl. 7 t. 6). No monthly
  contributions on €797.20. Instead PU sets **annual** contributions by rješenje (ZOD čl. 183 st. 2, čl. 240) on
  an **annual base equal to the class's paušal income** (ZOD čl. 185 st. 3; NN 150/2025 čl. 14):
  MIO 7.5% + 2.5% (or 10% pillar I only) (ZOD čl. 13 st. 3, čl. 17 st. 2) and HZZO 7.5% (ZOD čl. 14 st. 2),
  i.e. about **17.5% of the class base**:

  | Class | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
  |---|---|---|---|---|---|---|---|
  | Annual contributions 2026 (≈) | 296.64 | 401.64 | 522.39 | 803.25 | 1,050.00 | 1,312.50 | 1,575.00 |

  (Rounded per item; PU's rješenje is decisive.) The paušal tax is the same as for a main-activity obrt.
  When the employment ends, the obrt becomes the main activity and monthly contributions of €290.98 start;
  report changes to PU/HZMO (**VERIFY** current procedure, usually handled automatically from the registers).
- **Pensioner (umirovljenik)** who keeps pension status under the Zakon o mirovinskom osiguranju: **no
  contributions** on paušal income (ZOD čl. 212 st. 3). Excludes children receiving a family pension
  (st. 4). Tax still applies. **VERIFY** with HZMO (mirovinsko.hr) whether the specific pension type may be
  combined with an obrt.
- Students, part-time employment, maternity/parental leave: special rules. **VERIFY** case by case.

## 5. Deadlines (2026)

| What | Deadline | Source |
|---|---|---|
| Contributions | 15th of each month for the previous month | ZOD čl. 71 |
| Paušal tax, quarterly | **31.3., 30.6., 30.9., 31.12.** (last day of each quarter) | ZPD čl. 82 st. 1 |
| PO-SD report for the previous year + difference of tax | **15 January** (15 days after year end); difference paid the same day | ZPD čl. 82 st. 6 |
| HOK chamber contribution | quarterly, by 28.2., 31.5., 31.8., 30.11. | Odluka NN 154/2022 čl. 8 |
| Registration change (e.g. leaving paušal) | 8 days | ZPD čl. 83 / 87 (**VERIFY** article) |

Some commercial guides say the quarterly tax is due at the end of the month after the quarter; the Act says
"do posljednjeg dana svakog tromjesečja". Follow the Act and PU's rješenje.

Deadlines calendar for reminders: `croatia:hr-calendar`.

## 6. Records: KPR and PO-SD

- **KPR – Knjiga prometa** (turnover book): the only record a paušalist keeps (ZPD čl. 82 st. 4; form KPR in
  the Pravilnik). Enter every receipt (cash and non-cash) with date, invoice number and amount. Most
  invoicing/fiscalization apps generate it. **VERIFY** the current KPR column layout in the Pravilnik.
- **PO-SD – Izvješće o paušalnom dohotku od samostalnih djelatnosti** (PO-SD-Z for joint activity): filed
  electronically through **ePorezna** by **15 January** for the previous year (ZPD čl. 82 st. 6; TEB, Jan 2026:
  "nikako u papirnatom obliku"). It reports receipts by quarter and the resulting class; PU then sets the
  quarterly tax for the next year. A new PO-SD form applies from tax year 2025 (Pravilnik NN 16/25 čl. 4).
- Paušal income is final: it is not included in the annual income tax return (ZPD čl. 49 st. 1 t. 5).
- Keep invoices and KPR for the general limitation period (Opći porezni zakon): practitioners advise about
  11 years (see `registration-and-closing.md` §6).

## 7. Fiscalization and eRačun (summary – detail elsewhere)

- **Every B2C invoice must be fiscalized from 1.1.2026, whatever the payment method** (cash, card, bank
  transfer, Stripe), including paušalists (Zakon o fiskalizaciji, NN 89/2025). Needs a fiscal certificate,
  business premises registration and fiscalization-capable invoicing software.
- **eRačun:** paušalists must be able to **receive** eRačuni since 1.1.2026 (address in the AMS register) and must
  **issue** eRačuni to Croatian businesses from **1.1.2027**.
- Invoice text for a non-VAT paušalist: "Oslobođeno PDV-a temeljem čl. 90. st. 1. Zakona o PDV-u" (exempt small
  taxpayer).
- Full rules, invoice elements and edge cases: `croatia:hr-legal-compliance` →
  `references/04-tax-fiscalization-payments.md` §1–2. Implementation in code: `croatia:hr-fiscalization-dev`.

## 8. When paušal ends

1. **Receipts exceed €60,000** in the year: the obrtnik becomes a VAT payer (Zakon o PDV-u čl. 90; P-PDV
   registration within 8 days per PU practice – **VERIFY** exact article) and moves to real income (dohodak)
   under ZPD čl. 82 st. 8–10. Paušal applies until the end of the month in which the limit was crossed
   (st. 10), unless it happens in December.
2. **Voluntary VAT registration** (e.g. to deduct input VAT): paušal is no longer possible (ZPD čl. 82 st. 1).
3. **Voluntary switch to dohodak or dobit** (e.g. large real expenses): file the change with PU (form RPO);
   **VERIFY** timing (usually from 1 January of the next year).
4. **Becoming a slobodno zanimanje** activity: not eligible.

After leaving paušal: KPI book, monthly income-tax advances, contributions on €1,295.45 (see `obrt-dohodak.md`).

## 9. Other costs to budget (2026)

- **HOK komorski doprinos:** 1.9% of the basic personal allowance (€600.00 in 2026, ZPD čl. 14 st. 1) =
  **€11.40 per month**, paid quarterly; **exempt for the first two years** of a first-ever obrt (Odluka NN
  154/2022 čl. 6, 15). Also owed by obrtnici who are employed elsewhere.
- **Turistička članarina** (tourist board membership fee): many obrti pay it, often as a fixed annual amount for
  paušalists (Zakon o turističkoj članarini). **VERIFY** your activity's group and amount.
- **Bank account fees, fiscalization/invoicing software, fiscal certificate** (FINA), accountant (optional:
  many paušalists do it themselves; market estimate €25–60/month for a paušal bookkeeping service, not an
  official figure).
- **Reverse-charge VAT on foreign services** (Google Ads, Meta, SaaS, some Stripe products): a non-VAT paušalist
  pays 25% Croatian VAT on taxable services bought from abroad, with no deduction, and needs a PDV-ID number.
  See `pdv-vat.md` §5.

## 10. 2027 reform (announced, not law as of 2026-10-25)

- In July 2026 the Government/Ministry of Finance announced changes from **1.1.2027** to paušal for classes
  **above €40,000**: lower normed expenses and higher contributions. Minister Ćorić said classes up to €40,000
  (about 83% of paušalists) stay unchanged (Ministry of Finance presentation 27.7.2026; Dnevnik.hr, Index.hr,
  tportal, July 2026). Reported example: top class total tax + contributions from about €4,572 to €7,605 a year.
- As of 2026-10-25 the amended ZPD (zakon.hr shows the last amendment as NN 152/24) and Pravilnik were **not** yet
  published. **VERIFY** on narodne-novine.nn.hr / esavjetovanja.gov.hr before giving 2027 figures. Never apply the
  2026 table to 2027 without checking.

## 11. Worked example (2026, estimate)

Obrt as main activity, receipts €24,000 (class 4), first year (HOK exempt):
- Tax: €550.80 a year, €137.70 per quarter.
- Contributions: €290.98 × 12 = €3,491.76.
- Total ≈ €4,042.56 a year (≈ 16.8% of receipts), before software, bank and reverse-charge VAT.

Run `python3 scripts/pausal_estimate.py 24000 --hok-exempt` for the same estimate. Start the answer with the
calculation-output header from SKILL.md.
