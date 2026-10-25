---
name: hr-calendar
description: >-
  Croatian calendar facts and date arithmetic: public holidays (blagdani i
  neradni dani, praznici, Uskrs, Tijelovo, Dan državnosti, Svi sveti), working
  days (radni dani, fond sati), procedural deadlines that roll past Sundays and
  holidays (rok, računanje rokova, ZUP, ZPP), Sunday shop opening (radne
  nedjelje, rad trgovina nedjeljom, Zakon o trgovini), school holidays
  (praznici škola, zimski/proljetni odmor), time zone Europe/Zagreb and DST, and
  recurring tax/filing deadlines (JOPPD, PDV, PO-SD, DOH, PD, GFI, doprinosi,
  turistička pristojba). Includes a Python script for holidays (.ics/JSON),
  working-day counts, Easter and deadline dates. Use for "holidays Croatia",
  "is X a working day", "working days in 2026", "Croatian bank holidays",
  "when is Corpus Christi", "shops open Sunday Croatia", "school holidays
  Croatia", "deadline JOPPD", "rok za PO-SD", "kad je Tijelovo", "neradni dani
  2027", "koliko radnih dana", or any scheduling, calendar app or reminder
  feature for Croatia.
---

# Croatian calendar: holidays, working days, deadlines

Facts and a calculator for Croatian dates: the 14 public holidays and how they
fall, working-day counts, procedural deadline arithmetic, Sunday trading rules,
school holidays, time zone, and a calendar of recurring statutory deadlines for
businesses and individuals.

Status: researched 2026-10-25.

> **Not legal, tax or financial advice.** This skill provides general,
> research-based information that may be incomplete or out of date. Always
> verify with the official sources cited and consult a qualified professional
> (lawyer / odvjetnik, tax adviser / porezni savjetnik, accountant /
> računovođa) before acting.

When an answer touches deadlines, tax or legal obligations, Sunday trading
rules or holiday pay, **end it with one line** in the user's language:
- EN: *This is general information, not legal or tax advice. Check the cited sources and consult a professional.*
- HR: *Ovo su opće informacije, a ne pravni ni porezni savjet. Provjerite navedene izvore i posavjetujte se sa stručnjakom.*

Any generated deadline calendar, reminder list or compliance document starts with:
- HR: `PREDLOŽAK – nije pravni savjet. Prilagodite ga svom slučaju i dajte ga na provjeru stručnjaku.`
- EN: `TEMPLATE – not legal advice. Adapt it to your case and have it reviewed by a professional.`

## How to use

1. **Compute, don't recall.** For any date question run the script
   (`python3 scripts/hr_calendar.py …`, see below) instead of computing Easter,
   weekdays or roll-overs mentally.
2. **Load the reference you need** (grep first, they are long):

| Topic | File | Grep hints |
|---|---|---|
| Holiday law, exact names, 2025–2030 table, religious days, spomendani, working-day definition, ZUP/ZPP/ZOO deadline rules, EuroNKS/TARGET payment days, time zone/DST, month and weekday names, name days | `references/holidays-law.md` | `čl. 1`, `čl. 3`, `Spomendani`, `## 7`, `EuroNKS`, `DST`, `siječnja` |
| Sunday/holiday shop opening, 16 working Sundays, 90 h/week, exemptions, penalties, pending changes | `references/sunday-trading.md` | `st. 4`, `st. 5`, `st. 6`, `kiosk`, `Penalties`, `obrt` |
| School year 2025/26 and 2026/27 dates, structure, universities | `references/school-calendar.md` | `2026/2027`, `Winter break`, `academic year` |
| Recurring tax and filing deadlines (JOPPD, PDV, PO-SD, DOH, PD, GFI, contributions, tourist tax, fiscalization reporting) | `references/statutory-deadlines.md` | `JOPPD`, `PDV`, `PO-SD`, `GFI`, `pristojba`, `Monthly`, `Annual` |

3. **Cite the source** (act + article, NN number) for every legal claim and
   pass on **VERIFY** markers as open questions, not as facts.
4. **Hand off** detailed questions: tax obligations →
   `croatia:hr-business-admin`; holiday pay, leave, Sunday work of employees →
   `croatia:hr-payroll-employment`; tourist season, eVisitor →
   `croatia:hr-tourism-rentals`; date formatting in UI → `croatia:hr-localization`;
   eRačun / fiscalization → `croatia:hr-fiscalization-dev`; Croatian copy →
   `croatia:croatian-language`.
5. **Project memory**: if a project needs its own calendar (e.g. its chosen 16
   working Sundays, its school's local days off), store it in the user's
   project, e.g. `.claude/croatia/hr-calendar.md`, never in this skill.

## Script: `scripts/hr_calendar.py`

Python 3 standard library, no network. `--self-test` must print `self-test OK`.

| Command | Does |
|---|---|
| `holidays 2026 [--to 2028] [--religious] [--memorial] [--json \| --ics]` | Public holidays; `--religious` adds 7 Jan and Orthodox Easter Monday (believers only), `--memorial` adds spomendani (not days off); `--ics` writes RFC 5545 all-day events for calendar apps |
| `is-working-day 2026-06-04 [--saturday-working]` | Exit 0 if working day, 1 if not, with reason |
| `working-days 2026-01-01 2026-12-31` | Inclusive count, hours, fond sati |
| `add-working-days 2026-12-23 3` | N working days after (negative: before); start not counted |
| `easter 2027 [--julian]` | Easter, Good Friday, Easter Monday, Corpus Christi; Orthodox Easter |
| `deadline 2026-12-10 15 [--rule zup\|zpp\|zoo] [--unit days\|months\|years] [--saturday-open]` | Procedural deadline: trigger day not counted, last day rolls past Sunday/holiday (and Saturday for zup/zpp) |
| `is-payment-day 2026-04-03` | EuroNKS/TARGET interbank settlement day? |

Dates accept `YYYY-MM-DD` or `D.M.YYYY.`. Years before 2020 are refused (the
holiday list was different). Save `.ics` with
`python3 scripts/hr_calendar.py holidays 2026 --to 2030 --ics > blagdani.ics`.

## Key facts

**Public holidays** (Zakon o blagdanima, spomendanima i neradnim danima u RH,
NN 110/19, 72/25, čl. 1): 1.1. Nova godina · 6.1. Bogojavljenje ili Sveta tri
kralja · Uskrs · Uskrsni ponedjeljak · 1.5. Praznik rada · 30.5. Dan
državnosti · Tijelovo (Easter + 60) · 22.6. Dan antifašističke borbe · 5.8. Dan
pobjede i domovinske zahvalnosti i Dan hrvatskih branitelja · 15.8. Velika
Gospa · 1.11. Svi sveti · 18.11. Dan sjećanja na žrtve Domovinskog rata i Dan
sjećanja na žrtvu Vukovara i Škabrnje · 25.12. Božić · 26.12. Sveti Stjepan.

| Year | Uskrs | Uskrsni pon. | Tijelovo | Holidays Mon–Fri | Working days |
|---|---|---|---|---|---|
| 2025 | 20.4. | 21.4. | 19.6. | 11 | 250 |
| 2026 | 5.4. | 6.4. | 4.6. | 9 | 252 |
| 2027 | 28.3. | 29.3. | 27.5. | 8 | 253 |
| 2028 | 16.4. | 17.4. | 15.6. | 10 | 250 |
| 2029 | 1.4. | 2.4. | 31.5. | 10 | 251 |
| 2030 | 21.4. | 22.4. | 20.6. | 11 | 250 |

- A holiday on a **Sunday (or Saturday) is not moved** (čl. 4). No bridge days
  by law.
- **Not days off**: Veliki petak, Badnjak (24.12.), Stara godina (31.12.),
  25.6. Dan neovisnosti, 8.10. Dan Hrvatskoga sabora (memorial days since 2020).
- **Believers only** (čl. 3): Orthodox Christmas 7.1., Orthodox Easter Monday,
  one day each for Ramazanski and Kurban-bajram, Roš hašana and Jom kipur.
- **Working day** = Monday–Friday that is not a holiday. Saturday is not a
  holiday, but offices and courts do not work, so a deadline ending on Saturday
  rolls to Monday under ZUP čl. 81 / ZPP čl. 112 st. 4.
- **Deadlines**: day of service not counted; Sundays and holidays inside the
  period count; only the last day rolls to the next working day (ZUP čl. 80–81,
  ZPP čl. 112, ZOO čl. 300). Tax procedure applies ZUP (Opći porezni zakon čl. 4).
- **Interbank payments**: EuroNKS/TARGET closed on weekends, 1.1., Good Friday,
  Easter Monday, 1.5., 25.12., 26.12.; open on other Croatian holidays. Instant
  payments run every day.
- **Shops**: closed on Sundays and holidays; 16 self-chosen working Sundays per
  year; Monday–Saturday max 90 h/week (+15 h in a working-Sunday week);
  exemptions for stations, airports, ports, petrol stations, hospitals, hotels,
  museums, marinas, campsites, protected nature areas, markets, fairs, vending
  machines, online sales; kiosks 07–13 h (Zakon o trgovini čl. 57).
- **Time zone** Europe/Zagreb, CET (UTC+1) / CEST (UTC+2); switch on the last
  Sunday of March and October (2026: 29.3. and 25.10.; Uredba NN 13/22 covers
  2022–2026, **VERIFY** the decree for 2027+).
- **School 2026/27** (Odluka NN 58/2026): 7.9.2026 – 15.6.2027; winter
  24.12.2026 – 5.1.2027 and 22.–26.2.2027; spring 25.3. – 2.4.2027; summer from
  16.6.2027. Local school days off vary.
- **Months** (lower case): siječanj, veljača, ožujak, travanj, svibanj, lipanj,
  srpanj, kolovoz, rujan, listopad, studeni, prosinac; dates in genitive:
  "4. lipnja 2026.".

**Recurring deadlines** (summary; details, sources and VERIFY flags in
`references/statutory-deadlines.md`):

| Obligation | Who | Deadline (nominal) | Source |
|---|---|---|---|
| Wages paid | Employers | at the latest the 15th for the previous month | ZR čl. 92 st. 4 |
| Contributions on wages | Employers | when the wage is paid | ZOD čl. 24 |
| JOPPD | Payers | on payment day, at the latest the next working day; in-kind by the 15th of next month | Pravilnik o porezu na dohodak čl. 79 |
| Own contributions | Obrtnici, paušalisti | 15th for the previous month | ZOD čl. 67, 71 |
| PDV, PDV-S, ZP | VAT payers | last day of the month after the period (was the 20th until 2025) | ZPDV čl. 85, 86, 88 (NN 151/25) |
| eIzvještavanje (eRačun payments) | eRačun issuers | 20th for the previous month | ZF čl. 53 |
| Paušalni porez | Paušalisti | 31.3., 30.6., 30.9., 31.12. | ZPD čl. 82 |
| PO-SD | Paušalisti | 15.1. | ZPD čl. 82 st. 6 |
| DOH | Obrtnici with books | end of February | ZPD čl. 50 |
| PD (porez na dobit) | Companies | 30.4. | ZPDobit čl. 35 |
| GFI to FINA | Companies | 30.4. statistics / 30.6. public disclosure | ZOR čl. 50, 47 |
| Tourist tax and membership (flat rate) | Private renters | 31.7. (or 31.7./31.8./30.9.) | ZTP čl. 17; ZČTZ čl. 11 |

Deadlines ending on a Sunday, holiday or non-working day move to the next
working day (ZUP čl. 81 via OPZ čl. 4); Intrastat (15th) does not move.

## Keeping current

| Fact | Changes | Check |
|---|---|---|
| Holiday list | Rarely (last: NN 110/19 from 2020; NN 72/25 memorial days) | zakon.hr consolidated text, narodne-novine.nn.hr |
| School year dates | Every year (decision in May/June) | narodne-novine.nn.hr, mzom.gov.hr |
| DST dates | Decree every ~5 years; EU abolition proposal | narodne-novine.nn.hr ("Uredba o ljetnom računanju vremena") |
| Sunday trading | Political topic, amended 2023; Zakon o obrtu changes announced 2026 | zakon.hr Zakon o trgovini, narodne-novine.nn.hr |
| Tax/filing deadlines | Frequently (2025/2026 reforms, Fiskalizacija 2.0) | porezna-uprava.gov.hr, fina.hr, zakon.hr |
| Payment system days | TARGET calendar | fina.hr (EuroNKS), hnb.hr, Porezna uprava notices |

After updating facts, run `python3 scripts/hr_calendar.py --self-test`.
