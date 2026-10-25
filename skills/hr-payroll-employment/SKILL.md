---
name: hr-payroll-employment
description: >-
  Croatian labour law and payroll for 2026: employment contracts (ugovor o radu, fixed-term,
  probation, part-time, dodatni rad, rad od kuće / rad na daljinu), working time, overtime,
  annual leave, sick leave, maternity/paternity leave, termination (otkaz, otkazni rok,
  otpremnina), salary calculation bruto→neto and neto→bruto with city tax rates, employer cost,
  minimum wage, non-taxable payments, student contracts, foreign workers' permits, HR records.
  Use for "plaća", "bruto", "neto", "obračun plaće", "kalkulator plaće", "minimalna plaća",
  "porez na dohodak", "osobni odbitak", "doprinosi", "JOPPD", "ugovor o radu", "probni rad",
  "otkaz", "otkazni rok", "otpremnina", "godišnji odmor", "bolovanje", "rodiljni", "očinski",
  "neoporezivi primici", "regres", "božićnica", "dnevnica", "studentski ugovor", "studentska
  satnica", "radna dozvola", "dozvola za boravak i rad", "payroll Croatia", "salary calculator
  Croatia", "net salary Zagreb", "employment law Croatia", "hire in Croatia".
---

# Croatian payroll and employment law (hr-payroll-employment)

Answers questions about employing people in Croatia and calculates 2026 salaries: contracts,
working time, leave, termination, pay rules, gross/net and employer cost, tax-free benefits,
student work and foreign workers. Built for employers, HR and payroll staff, founders,
developers of HR/payroll software, and employees checking their pay.

Status: researched 2026-10-25.

> **Not legal, tax or financial advice.** This skill provides general,
> research-based information that may be incomplete or out of date. Always
> verify with the official sources cited and consult a qualified professional
> (lawyer / odvjetnik, tax adviser / porezni savjetnik, accountant /
> računovođa) before acting.

## Mandatory output rules

- End **every** answer that touches labour law, tax or payroll with one line in the user's
  language:
  - EN: *This is general information, not legal or tax advice. Check the cited sources and consult a professional.*
  - HR: *Ovo su opće informacije, a ne pravni ni porezni savjet. Provjerite navedene izvore i posavjetujte se sa stručnjakom.*
- Start every generated document, template or calculation (contract draft, dismissal letter,
  payslip estimate, policy) with:
  - HR: `PREDLOŽAK – nije pravni savjet. Prilagodite ga svom slučaju i dajte ga na provjeru stručnjaku.`
  - EN: `TEMPLATE – not legal advice. Adapt it to your case and have it reviewed by a professional.`
- Cite act + article (e.g. "ZOR čl. 122", "ZPD čl. 14") or the official URL for each rule and
  number; give amounts **with the year** ("2026: …"). Surface relevant **VERIFY** items as open
  questions instead of stating them as settled.
- Croatian text must follow `croatia:croatian-language` (ijekavica, polite **Vi/Vaš** to one
  person). Croatian legal terms get an English gloss the first time.

## How to use

1. Identify the situation: employer or employee; worker type (employee, director, student,
   foreigner, freelancer); residence city (for tax); dates (2026 rules only for 2026 payments).
2. For any salary number, **run the script** rather than calculating by hand:

   ```bash
   python3 scripts/hr_salary.py --gross 1500 --city zagreb
   python3 scripts/hr_salary.py --net 1200 --city split --children 2
   python3 scripts/hr_salary.py --gross 1100 --lower 20 --higher 30 --pillar1-only
   python3 scripts/hr_salary.py --gross 1500 --city zagreb --youth under25   # refund estimate
   python3 scripts/hr_salary.py --list-cities      # built-in 2026 city table
   python3 scripts/hr_salary.py --self-test        # 33 hand-checked cases
   ```

   Options: `--children N`, `--dependants N`, `--disabled N`, `--disabled100 N`,
   `--pillar1-only`, `--no-mio-relief`, `--youth under25|26-30`, `--assisted-area`,
   `--apply-reliefs-monthly`, `--health-exempt`, `--json`. For towns not in the table pass
   `--lower/--higher` from the Porezna uprava table (default without a decision: 20/30 %).
   The script prints the rule year, sources and "ESTIMATE ONLY"; it does not handle several
   employers in one month, non-residents, directors' minimum base or non-taxable payments.
3. Load only the reference you need:

| Topic | File | Grep hints |
|---|---|---|
| Contract content, form, HZMO registration, fixed-term, probation, part-time, dodatni rad, on-call, remote work, platform work, ugovor o djelu, directors, work rules, whistleblowing, pay transparency | `references/employment-contracts.md` | `čl. 15`, `čl. 12`, `probni`, `18.a`, `izdvojenom`, `daljinu`, `platform`, `direktor`, `prijavitelj`, `2023/970` |
| Working time, overtime, night work, breaks, rest, records, increased pay (Sunday +50 %), annual leave, paid leave, sick leave (42 days, caps), maternity/paternity/parental leave | `references/working-time-leave.md` | `čl. 65`, `čl. 94`, `čl. 77`, `čl. 86`, `42`, `995,45`, `očinski` |
| Termination types, protected persons, works council, notice table, severance, collective redundancy, deadlines | `references/termination.md` | `čl. 115`, `čl. 116`, `čl. 34`, `čl. 122`, `čl. 126`, `čl. 127`, `čl. 133` |
| 2026 payroll figures, city tax rates, step-by-step calculation, personal deduction table, reliefs, worked examples, JOPPD/payslip | `references/payroll-2026.md` | `11.958`, `umanjenje`, `koeficijent`, `Zagreb`, `čl. 45`, `JOPPD` |
| Tax-free benefits 2026 with limits (božićnica/regres, dar djetetu, prehrana, dnevnice, km, rad od kuće, jubilarna, otpremnina, potpore) | `references/non-taxable-payments-2026.md` | `700`, `140`, `1.200`, `dnevnica`, `0,50`, `izdvojenom`, `jubilar` |
| Student contracts: who, hourly minimum, 12,000 € limit, 3,600 € dependant limit, client cost | `references/student-work.md` | `6,56`, `12.000`, `3.600`, `12 %` |
| EU vs third-country workers, single permit, HZZ test, NN 55/2026 changes, digital nomads | `references/foreign-workers.md` | `čl. 99`, `90 dana`, `103.d`, `nomad` |
| All URLs and the open VERIFY list | `references/sources.md` | `VERIFY` |

4. Hand off related questions: employee personal data, privacy notices, monitoring, GDPR →
   `croatia:hr-legal-compliance`; public holidays and working-day counts → `croatia:hr-calendar`;
   OIB/IBAN validation → `croatia:hr-identifiers`; obrt/d.o.o. owner contributions, paušalni
   obrt, drugi dohodak, ugovor o djelu taxation → `croatia:hr-business-admin`; seasonal tourism
   staffing context → `croatia:hr-tourism-rentals`; EU-funded hiring subsidies →
   `croatia:hr-eu-funding`; date/number formatting in HR UIs → `croatia:hr-localization`.
5. Per-project memory (e.g. the company's collective agreement, city, payroll conventions) goes
   in the user's project, e.g. `.claude/croatia/hr-payroll-employment.md` – never edit this
   skill's files.

## Quick reference – 2026 key figures

| Item | 2026 | Source |
|---|---|---|
| Minimum wage (full time) | **EUR 1,050.00 gross/month** | Uredba, NN 132/2025 |
| Contributions from salary | MIO I **15 %** + MIO II **5 %** (MIO I 20 % if pillar I only) | Zakon o doprinosima |
| MIO I base reduction | EUR 300 (gross ≤ 700); 0.5 × (1,300 − gross) up to 1,300; MIO I only | Porezna uprava brochure; ZoD |
| Employer health insurance | **16.5 %** on gross | Zakon o doprinosima |
| Max monthly contribution base | EUR 11,958.00 (min. EUR 757.34; employed directors min. EUR 1,295.45; directors not insured elsewhere EUR 1,993.00, paid by the director) | Naredba NN 150/2025 |
| Basic personal deduction | **EUR 600/month**; children 0.5/0.7/1.0/1.4…; dependant 0.5 | ZPD čl. 14 |
| Tax brackets | lower rate to **EUR 5,000/month** (60,000/yr), higher above; no prirez | ZPD čl. 19 |
| City rates (lower/higher) | Zagreb 23/33, Split 21.5/32, Rijeka 20/25, Osijek 20/30, Zadar 20/30, Pula 22/32; default 20/30 | Porezna uprava table via RRiF |
| Youth relief | ≤25: 100 %, 26–30: 50 % of lower-rate tax, via annual assessment | ZPD čl. 45 st. 2 |
| Example: gross 1,500, Zagreb, single | net **1,062.00**, employer cost **1,747.50** | `hr_salary.py` |
| Payday | by the **15th** of the following month; payslip within 15 days of payment | ZOR čl. 92, 93 |
| Working time | 40 h/week; overtime max 50 h/week, **180 h/yr (250 by CA)** | ZOR čl. 61, 65 |
| Sunday work | at least **+50 %** | ZOR čl. 94 |
| Annual leave | min **4 weeks** (20 days on a 5-day week); minors 5 weeks | ZOR čl. 77 |
| Paid leave | **7 working days/yr** + 1 day per blood donation | ZOR čl. 86 |
| Sick leave | employer pays days **1–42**; HZZO from day 43, 70 % (80 % after 6 months), cap **EUR 995.45/month** | ZOZO; hzzo.hr |
| Paternity / parental leave | očinski **20 working days** (30 twins), 100 %; roditeljski cap **EUR 3,001.79/month** | ZRRP NN 34/25; hzzo.hr |
| Fixed-term | max **3 years**, max **3 successive contracts**, 6-month gap to restart | ZOR čl. 12 |
| Probation | max **6 months**; notice at least 1 week | ZOR čl. 53 |
| Notice periods | 2 weeks (< 1 yr) → 3 months (20 yrs); +2 weeks at 50+, +1 month at 55+ (with 20 yrs) | ZOR čl. 122 |
| Severance | after 2 years: ≥ 1/3 of avg monthly pay per year, cap 6 months' pay; tax-free **EUR 960/yr** | ZOR čl. 126; Pravilnik čl. 7 |
| Tax-free bonuses | božićnica + regres + other occasional **EUR 700/yr**; dar djetetu **EUR 140**; performance **EUR 1,200** | Pravilnik o porezu na dohodak čl. 7 |
| Tax-free meals / travel | prehrana **EUR 100/month** (1,200/yr) or 150 with invoices; dnevnica **EUR 30** (8–12 h: 15); **EUR 0.50/km**; work from home **EUR 4/day, max 70/month** | Pravilnik čl. 7; Porezna uprava; RRiF |
| Students | min **EUR 6.56 net/hour**; tax-free **EUR 12,000/yr**; dependant limit **EUR 3,600** | MZOM Odluka; SC Zagreb |
| Foreign workers (non-EU) | HZZ test + single permit; MUP decides within **90 days** (from 4 Jun 2026); job change after 6 months | ZoS NN 55/2026 |

## Rules that cover most questions

- **Pay is always agreed in gross**; net depends on residence city, deductions and pillar.
  Quote net only from the script, stating the assumptions.
- **Register with HZMO before work starts** and give the worker the written contract (or
  written confirmation) before day one; otherwise the contract is deemed indefinite
  (ZOR čl. 14).
- Overtime needs a written order; Sunday +50 % is the only statutory minimum premium – other
  premiums come from the collective agreement, work rules or contract.
- Sick leave is never a valid reason for dismissal; pregnancy and parental leave give strong
  protection (ZOR čl. 34, 117).
- Dismissal must be written, reasoned and delivered; misconduct dismissal needs a prior warning
  and a chance to defend; extraordinary dismissal within 15 days of learning the facts.
- Tax-free payments are limited per year and per type; excess is taxed as salary.
- Student contracts and ugovor o djelu do not replace employment for a regular job
  (ZOR čl. 10 st. 2).
- When a question needs a judgment (is this dismissal lawful? is this contract disguised
  employment?), give the rules and risks, then recommend a labour lawyer.

## Keeping current

| Fact | Changes | Check |
|---|---|---|
| Minimum wage | yearly Uredba (October–November) | mrosp.gov.hr, narodne-novine.nn.hr |
| Contribution bases | yearly Naredba (December) | narodne-novine.nn.hr |
| City tax rates | local decisions by end of November, apply 1 Jan | porezna-uprava.gov.hr rate table |
| Personal deduction, brackets, youth relief | ZPD amendments (draft in consultation from 31 Jul 2026) | porezna-uprava.gov.hr, esavjetovanja.gov.hr |
| Non-taxable amounts, student limit | Pravilnik o porezu na dohodak amendments | porezna-uprava.gov.hr, NN |
| Sick/parental caps | budget base changes | hzzo.hr |
| Student hourly minimum | yearly ministry decision | student centres (e.g. sczg.unizg.hr) |
| Labour law | ZOR amendment for pay transparency and platform work expected end of 2026 | zakon.hr, mrosp.gov.hr, NN |
| Foreign workers | ZoS NN 55/2026; implementing rules due by Dec 2026; language exam from 4 Jun 2027 | mup.gov.hr, hzz.hr |

When the current year is later than 2026, say that the built-in figures are 2026 values, mark
them **VERIFY**, and look up the new values before calculating.
