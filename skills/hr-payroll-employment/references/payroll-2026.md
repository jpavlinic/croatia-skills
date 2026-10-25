# Payroll calculation 2026 (obračun plaće) – Croatia, researched 2026-10-25

Applies to salary (plaća, dohodak od nesamostalnog rada) paid in 2026 to a Croatian tax
resident by one employer. Use `scripts/hr_salary.py` for numbers; this file explains the rules.

## 1. Key figures 2026

| Item | 2026 value | Source |
|---|---|---|
| Minimum wage (minimalna plaća), full time | **EUR 1,050.00 gross/month** | Uredba o visini minimalne plaće za 2026., NN 132/2025 (mrosp.gov.hr, 24 Oct 2025) |
| Average wage used for contribution bases | EUR 1,993.00 | Naredba NN 150/2025 čl. 2 |
| Minimum monthly contribution base | EUR 757.34 (0.38 × 1,993) | Naredba NN 150/2025 čl. 3 |
| Maximum monthly contribution base (MIO) | **EUR 11,958.00** (6 × 1,993) | Naredba NN 150/2025 čl. 4 |
| Maximum annual contribution base | EUR 143,496.00 | Naredba NN 150/2025 čl. 5 |
| Minimum base for employed management-board member | EUR 1,295.45 | Naredba NN 150/2025 (coefficient 0.65) |
| MIO I (pillar I) from salary | **15 %** (20 % if only in pillar I) | Zakon o doprinosima |
| MIO II (pillar II) from salary | **5 %** | Zakon o doprinosima |
| Health insurance on salary (employer) | **16.5 %** of gross, no cap | Zakon o doprinosima |
| MIO I base reduction | EUR 300 for gross ≤ 700; 0.5 × (1,300 − gross) for 700.01–1,300; 0 above | ZoD (NN 114/23, from Dec 2023 pay); Porezna uprava brochure |
| Basic personal deduction (osnovni osobni odbitak) | **EUR 600.00/month** | ZPD čl. 14 st. 1 (NN 152/24) |
| Tax brackets | lower rate up to **EUR 5,000/month** (EUR 60,000/year), higher above | ZPD čl. 19 |
| Rate ranges set by local units | municipality 15–20 / 25–30 %; town 15–21 / 25–31 %; large town or county seat 15–22 / 25–32 %; **Zagreb 15–23 / 25–33 %**; default 20/30 % | ZPD čl. 19.a |
| Prirez (surtax) | abolished since 1 Jan 2024 | ZPD NN 114/23 |
| Sick-pay cap (HZZO-funded) | EUR 995.45/month | hzzo.hr (2026) |
| Protected net pay for enforcement (ovrha) | average net EUR 1,434 reference; other claims: 3/4 of net exempt, max EUR 956 | Smart Group summary of 2026 changes – **VERIFY** in Ovršni zakon notice |

The minimum wage excludes increases for overtime, night, Sunday and holiday work and other
allowances (Zakon o minimalnoj plaći) – **VERIFY** the current list in the Act. Sector minimums
can be higher under extended collective agreements.

## 2. 2026 income-tax rates of major cities (from 1 Jan 2026)

Source: Porezna uprava table of decisions published by 15 Dec 2025, as reproduced by RRiF
("Stope poreza na dohodak za isplate od 1. siječnja 2026.") and EDUS/Hina (19 Dec 2025).

| City | Lower / higher | City | Lower / higher |
|---|---|---|---|
| Zagreb | 23 / 33 | Dubrovnik | 20 / 30 |
| Split | 21.5 / 32 | Karlovac | 19 / 29 |
| Rijeka | 20 / 25 (cut from 22/32 for 2026) | Sisak | 21.6 / 31.6 |
| Osijek | 20 / 30 | Bjelovar | 18 / 25 |
| Zadar | 20 / 30 | Samobor | 18 / 27 |
| Pula | 22 / 32 (raised for 2026) | Čakovec | 20 / 30 |
| Varaždin | 21 / 32 | Koprivnica | 20 / 30 |
| Slavonski Brod | 20 / 30 | Gospić | 22 / 32 |
| Velika Gorica | 20 / 30 | Pazin | 22 / 30 |
| Šibenik | 20 / 30 | Vukovar | 20 / 30 |

Most municipalities (489 of 556 per netoplaca.hr's reading of the table) apply 20/30 %. The
rate is that of the worker's **residence** (prebivalište/uobičajeno boravište), not of the
workplace (ZPD čl. 1 st. 2). Decisions are adopted by end of November and apply from 1 January;
always re-check the Porezna uprava table for the year.

## 3. Calculation steps (bruto → neto)

1. **Gross (bruto 1)** = basic pay + allowances (dodaci: overtime, night, Sunday, holiday,
   seniority, stimulation) + taxable benefits in kind.
2. **MIO base** = gross, capped at EUR 11,958.00.
3. **MIO I base reduction** (umanjenje mjesečne osnovice, generational solidarity):
   - gross ≤ EUR 700: EUR 300 (never more than the gross);
   - EUR 700.01–1,300: 0.5 × (1,300 − gross);
   - above EUR 1,300: none.
   It reduces **only the MIO I base**; MIO II is calculated on the full base. It applies
   regardless of hours (full or part time) and days insured. With several employers, each
   employer applies a proportional share based on Porezna uprava data (available from the 2nd
   working day of the month) or the worker's statement (mandatory when a new insurance starts
   during the month). Pension rights are unaffected.
4. **MIO I** = 15 % × (base − reduction) (20 % if the worker is only in pillar I);
   **MIO II** = 5 % × base.
5. **Income (dohodak)** = gross − MIO I − MIO II.
6. **Personal deduction (osobni odbitak)** = EUR 600 × coefficient, used up to the income:

   | Basis (ZPD čl. 14 st. 3) | Coefficient | EUR/month |
   |---|---|---|
   | Taxpayer (basic) | 1.0 | 600 |
   | Each dependent family member | 0.5 | 300 |
   | 1st / 2nd / 3rd / 4th child | 0.5 / 0.7 / 1.0 / 1.4 | 300 / 420 / 600 / 840 |
   | 5th / 6th / 7th / 8th / 9th child | 1.9 / 2.5 / 3.2 / 4.0 / 4.9 | 1,140 / 1,500 / 1,920 / 2,400 / 2,940 |
   | Disability (taxpayer or each dependant) | 0.3 | 180 |
   | 100 % disability / care allowance / personal disability benefit / inclusive allowance (instead of 0.3) | 1.0 | 600 |

   Coefficients add up (e.g. two children = 1 + 0.5 + 0.7 = 2.2 → EUR 1,320). Child deductions
   can be split between parents. Dependants are reported on the tax card (porezna kartica) via
   the employer or ePorezna; changes within 30 days (ZPD čl. 26 st. 4).
   A dependant's own annual receipts must not exceed EUR 3,600 (ZPD čl. 17 st. 1 as cited by
   SC Zagreb for 2025/2026).
7. **Tax base (porezna osnovica)** = income − personal deduction (min. 0).
8. **Income tax** = lower rate × min(base, 5,000) + higher rate × excess.
9. **Net (neto)** = income − tax.
10. **Employer cost (bruto 2 / ukupni trošak)** = gross + 16.5 % health insurance.

Payment and admin: salary for a month is paid **by the 15th of the following month** at the
latest (ZOR čl. 92 st. 4) to the worker's bank account; a written payroll statement (obračun)
within 15 days of payment (ZOR čl. 93; content: Pravilnik o sadržaju obračuna plaće, naknade
plaće, otpremnine i naknade za neiskorišteni godišnji odmor, NN 68/2023). An unpaid salary
statement is an enforceable document (ZOR čl. 93 st. 5). Contributions and tax are reported on
the **JOPPD** form via ePorezna, as a rule on the day of payment (Pravilnik o porezu na dohodak –
**VERIFY** exact deadlines per payment type). The employer runs an annual tax calculation for
workers employed all year in December (ZPD, article after čl. 45 – **VERIFY** numbering).

## 4. Reliefs (olakšice)

| Relief | Rule | How applied |
|---|---|---|
| Youth (mladi) | **100 %** of the tax on the lower-rate part of salary for persons **up to 25**; **50 %** for **26–30**; for the whole year in which the age is reached (ZPD čl. 45 st. 2, 8) | Annual assessment (godišnji obračun / refund) per Porezna uprava ("Umanjenje se koristi u godišnjem obračunu"); monthly payroll withholds normally – **VERIFY** if a payroll may apply it monthly |
| Assisted areas group I / Vukovar | **50 %** of the tax on salary or pension for residents (ZPD čl. 45 st. 1); youth relief is applied first (st. 7) | Annual assessment |
| Returning emigrants | **100 %** of salary tax for 5 years for Croatian citizens back after 2+ years abroad, and certain emigrants/descendants (ZPD čl. 45 st. 3–5) | Annual assessment |
| Croatian war invalids | tax reduced by the disability percentage (ZPD čl. 42) | Monthly |
| Employer health exemption for young workers, etc. | Zakon o doprinosima provides exemptions from the 16.5 % (e.g. young persons hired on indefinite contracts; the Porezna uprava 2024 brochure example shows 0 health contribution for a "mlada osoba") | **VERIFY** conditions in ZoD before applying |

## 5. Worked examples (computed by `hr_salary.py`, 2026)

All: resident, one employer, pillar II member, no reliefs.

| Case | Gross | MIO I | MIO II | Tax | Net | Employer cost |
|---|---|---|---|---|---|---|
| Zagreb, single | 1,500.00 | 225.00 | 75.00 | 138.00 | **1,062.00** | 1,747.50 |
| Zagreb, single, minimum wage | 1,050.00 | 138.75 (relief 125) | 52.50 | 59.51 | **799.24** | 1,223.25 |
| Zagreb, 2 children | 1,500.00 | 225.00 | 75.00 | 0.00 | **1,200.00** | 1,747.50 |
| Zagreb, single | 8,000.00 | 1,200.00 | 400.00 | 1,414.00 | **4,986.00** | 9,320.00 |
| Zagreb, single (MIO capped) | 15,000.00 | 1,793.70 | 597.90 | 3,462.77 | **9,145.63** | 17,475.00 |
| Rijeka, single | 6,000.00 | 900.00 | 300.00 | 840.00 | **3,960.00** | 6,990.00 |

Example 1 step by step: 1,500 × 15 % = 225; × 5 % = 75; income 1,200; − 600 = 600; × 23 % =
138; net 1,062; employer 1,500 × 1.165 = 1,747.50.

Cross-checks:
- The script reproduces all four rows of the **official Porezna uprava brochure example**
  (2024 rules: deduction 560, Veliko Trojstvo 17.5 %): nets 445.00, 237.50, 836.37, 840.50
  (self-test cases "PU …").
- 1,500 Zagreb matches the breakdown in bruto-neto.hr ("Kako izračunati neto plaću", 2026:
  contributions 300, income 1,200, deduction 600) and the employer total EUR 1,747.50 on
  kalkulator.com.hr (2026).
- Net 1,200 in Zagreb ↔ gross 1,724.02 (a public 2026 example quotes "bruto 1.724 eura").
- Note: some public calculators quote "about EUR 805" net for a minimum-wage single worker
  in Zagreb; that figure results if the MIO relief is also applied to MIO II. The Porezna
  uprava brochure applies it to MIO I only, giving EUR 799.24.

## 6. Other payroll items

- **Sick pay, maternity**: see `working-time-leave.md`. First 42 days of sick leave are an
  employer cost (salary compensation, taxed like salary).
- **Annual leave pay**: at least the 3-month average (ZOR čl. 81).
- **Non-taxable payments** (božićnica, regres, prehrana, dnevnice, km, dar djetetu…): see
  `non-taxable-payments-2026.md`. Amounts above the limits are taxed as salary (gross-up).
- **Benefits in kind** (company car, etc.) are taxable salary; valuation rules are in the
  Pravilnik o porezu na dohodak – **VERIFY** before computing.
- **Student contracts** are not salary – see `student-work.md`.
- **Ugovor o djelu / author fees / drugi dohodak**, owner contributions and obrt payroll →
  `croatia:hr-business-admin`.
- Draft amendments to the Zakon o porezu na dohodak were in public consultation from
  31 July 2026 (porezna-uprava.gov.hr) – likely to change figures from 2027; **VERIFY**.
