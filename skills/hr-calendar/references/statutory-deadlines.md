# Recurring statutory deadlines (general calendar)

Status: researched 2026-10-25. **General information only.** Deadlines depend
on legal form, VAT status, tax period and special regimes, and several changed
in 2025–2026 (NN 151/25, Fiskalizacija 2.0 from 1 Jan 2026, new Zakon o
računovodstvu NN 85/24). Rows marked **VERIFY** were not confirmed against the
current consolidated text; check porezna-uprava.gov.hr, fina.hr and zakon.hr
before relying on them. Detailed obligations: `croatia:hr-business-admin`;
payroll: `croatia:hr-payroll-employment`; tourism: `croatia:hr-tourism-rentals`;
fiscalization: `croatia:hr-fiscalization-dev`.

Start every calendar or reminder list generated from this file with:
`PREDLOŽAK – nije pravni savjet. Prilagodite ga svom slučaju i dajte ga na provjeru stručnjaku.`

Abbreviations: ZPDV = Zakon o porezu na dodanu vrijednost; ZPD = Zakon o
porezu na dohodak; ZPDobit = Zakon o porezu na dobit; ZOD = Zakon o
doprinosima; ZOR = Zakon o računovodstvu (NN 85/24, 145/24, 59/26); ZTP =
Zakon o turističkoj pristojbi; ZČTZ = Zakon o članarinama u turističkim
zajednicama; ZF = Zakon o fiskalizaciji (NN 89/25); ZLP = Zakon o lokalnim
porezima; ZR = Zakon o radu; "Pravilnik" = Pravilnik o porezu na dohodak
(last amended NN 157/25).

## Weekend / holiday rule

- Tax procedure applies ZUP where the Opći porezni zakon is silent (OPZ čl. 4);
  OPZ has no general non-working-day rule of its own.
- **ZUP čl. 81 st. 2:** if the last day of a deadline is a Sunday, a holiday or
  another day the authority does not work, the deadline ends on the next
  working day. Porezna applied this to the 2025 DOH return: Saturday
  28 Feb 2026 → Monday 2 Mar 2026.
- **Payments:** no explicit Porezna statement was found that a payment due on
  a weekend moves forward; interest runs from the due date (OPZ čl. 130 st. 3).
  Pay by the last working day before the due date, and remember interbank
  transfers do not settle on EuroNKS/TARGET closing days
  (`scripts/hr_calendar.py is-payment-day`). **VERIFY** for a specific case.
- **Own rules:** JOPPD has its own "at the latest the next working day" rule.
  **Intrastat does not shift**: the 15th applies even on a non-working day.
- Example: 31 Oct 2026 is a Saturday and 1 Nov a Sunday and holiday, so under
  ZUP čl. 81 the September / Q3 2026 VAT return falls on Monday 2 Nov 2026
  (not separately confirmed by Porezna).

## Monthly

| Obligation | Who | Deadline | Source |
|---|---|---|---|
| Wage payment | Employers | As agreed, **at the latest the 15th** of the current month for the previous month; payslip within 15 days of payment | ZR čl. 92 st. 4; čl. 93 st. 1 |
| Contributions on wages | Employers | **When the wage is paid**; if wages are not paid, by the last day of the month for the previous month | ZOD čl. 24 st. 1–2 |
| JOPPD, general rule | Payers of wages and other receipts | On the day of payment, **at the latest the next working day**; where tax/contributions fall due within 30 days, within that period | Pravilnik čl. 79 st. 1 (NN 16/25) |
| JOPPD, exceptions | Same | Receipts in kind: by the **15th** of the following month (st. 5); drugi dohodak under ZPD čl. 76.b: by the 15th of the following month (st. 18); seasonal agricultural workers: last day of the month of payment (st. 4) | Pravilnik čl. 79 |
| Contributions of obrtnici (business books) | Self-employed on income tax | By the **15th** for the previous month | ZOD čl. 67 st. 1 |
| Contributions of paušalisti | Flat-rate obrt | By the **15th** for the previous month | ZOD čl. 71 |
| Contributions of company directors / board members (not employed elsewhere) | Insured board members | By the 15th for the previous month | ZOD (section on board members) — article **VERIFY** |
| Income tax advances | Obrtnici with business books | By the **last day of the month** for the previous month | ZPD čl. 37 st. 5 |
| Corporate income tax advances | d.o.o., j.d.o.o., other CIT payers | By the **end of the month** for the previous month | ZPDobit čl. 34 st. 1 |
| VAT return (obrazac PDV) and payment | VAT payers (monthly; quarterly if prior-year supplies < €110,000, ZPDV čl. 84 st. 2) | By the **last day of the month after the period** (was the 20th until 2025; the last 2025 period kept the old deadline) | ZPDV čl. 85 st. 6 (NN 151/25 čl. 4); payment čl. 76 st. 1 (article number **VERIFY**) |
| PDV-S (EU acquisitions / services received) | VAT payers | Last day of the following month | ZPDV čl. 86 st. 2 (NN 151/25) |
| ZP (EC sales list) | VAT payers with EU supplies | Last day of the following month | ZPDV čl. 88 st. 2 (NN 151/25) |
| eIzvještavanje o naplati (report of collected eRačuni) | eRačun issuers | By the **20th** for the previous month (note: not the same day as VAT) | ZF čl. 53 st. 1 |
| Report of rejected eRačuni | eRačun recipients | By the **20th** for the previous month | ZF čl. 52 st. 1 |
| Fiscalising eRačuni | Issuers / recipients | Issued: at issue (self-billing within 5 working days); received: within 5 working days of receipt | ZF čl. 48 st. 3–4 |
| Intrastat | Businesses above thresholds | By the **15th** for the previous month, no shift for non-working days | DZS "Intrastat upute 2026" (EU Reg. 2019/2152, 2020/1197); national article **VERIFY** |
| Tourist membership fee advance | Companies and obrt (incl. paušalisti) | By the last day of the month for the current month (or one annual advance, see below) | ZČTZ čl. 10 st. 2 |
| Local consumption tax (porez na potrošnju) | Hospitality businesses | PP-MI-PO form by the **20th**, payment by the last day of the month, for the previous month | ZLP čl. 23 st. 4 |
| Tourist tax (per night) | Hotels and obrt in accommodation | For nights in each half-month (1st–15th, 16th–end), due within 7 days | ZTP čl. 17 st. 1 |

## Quarterly

| Obligation | Who | Deadline | Source |
|---|---|---|---|
| Flat-rate income tax (paušal) | Flat-rate obrt | By the last day of each quarter: **31 Mar, 30 Jun, 30 Sep, 31 Dec** | ZPD čl. 82 st. 1 and 11; Pravilnik o paušalnom oporezivanju čl. 6 st. 1 |
| Flat-rate income tax for private renters | Iznajmljivači u domaćinstvu | Quarterly by the last day of each quarter, per Porezna decision | ZPD čl. 82 st. 5 |
| VAT return, quarterly filers | Quarterly VAT payers | Last day of the month after the quarter (Q1 2026 → 30 Apr 2026) | ZPDV čl. 85 st. 6 |

## Annual

| Obligation | Who | Deadline | Source |
|---|---|---|---|
| PO-SD (flat-rate income report) | Flat-rate obrt | **15 January** for the previous year; any balance paid on filing | ZPD čl. 82 st. 6; Pravilnik o paušalnom čl. 7 st. 4, čl. 6 st. 2 |
| TZ form, private renters | Iznajmljivači u domaćinstvu | **15 January** for the previous year | ZČTZ čl. 13 st. 4 |
| INO-DOH; seafarers' certificate | Specific payers | 31 January | Pravilnik čl. 90; čl. 32 st. 2 |
| DOH (annual income tax return) | Obrtnici and self-employed with business books, others under ZPD čl. 48 | **End of February** (2025 return: 2 Mar 2026, weekend shift) | ZPD čl. 50 st. 2 |
| Citizens' claims (deductions, child allowance split) | Employees and other taxpayers | End of February | ZPD čl. 53 st. 1 |
| Annual JOPPD for capital gains | Payers | End of February | Pravilnik čl. 79 st. 13 |
| Annual membership-fee advance (optional) | Income-tax payers / CIT payers | End of February / end of April | ZČTZ čl. 10 st. 3 |
| Non-profit annual financial statements to FINA | Udruge and other non-profits | Within 60 days of year end (~1 March; 2025 statements: 2 Mar 2026); half-year by 30 July | Pravilnik o izvještavanju u neprofitnom računovodstvu (article **VERIFY**) |
| Porez na nekretnine: report changes | Property owners | **31 March** (status on 31 March decides who pays); tax paid within 15 days of the decision | ZLP čl. 25 st. 1, čl. 49 st. 4, čl. 49.a |
| CIT return (PD) and balance | CIT payers (calendar year) | Within 4 months: **30 April** | ZPDobit čl. 35 st. 1–2 |
| GFI for statistics and other purposes | Businesses | **30 April** (a public-disclosure GFI filed by 30 April also counts) | ZOR čl. 50 st. 1–2 |
| Izjava o neaktivnosti | Inactive businesses | 30 April | ZOR čl. 47 st. 9 |
| Report of consolidation obligation | Parent companies | 30 April | ZOR čl. 52 st. 10 |
| Closing the books | Businesses | Within 4 months of year end | ZOR čl. 12 st. 9 |
| GFI for public disclosure | Businesses | Within 6 months: **30 June**; consolidated within 9 months (30 Sep) | ZOR čl. 47 st. 5–7 |
| Provisional income tax decision for citizens | Porezna uprava | Delivered by **30 June** | ZPD čl. 54 st. 2 |
| Objection to the provisional decision | Taxpayers | **31 July** (or 30 days from late receipt); balance paid within 15 days after the objection deadline | ZPD čl. 54 st. 3, 4, 9 |
| Flat-rate tourist tax | Renters (domaćinstvo, OPG) | By **31 July**, or in thirds: 31 Jul, 31 Aug, 30 Sep | ZTP čl. 17 st. 2 |
| Flat-rate tourist tax | Holiday-home owners | 15 July | ZTP čl. 17 st. 3–4 |
| Flat-rate tourist membership fee | Renters (domaćinstvo) | By **31 July**, or 31 Jul / 31 Aug / 30 Sep; first-year renters by 31 Dec | ZČTZ čl. 11 st. 3, 7 |

## Event-based

| Obligation | Deadline | Source |
|---|---|---|
| eVisitor guest check-in / check-out | Within **24 hours** of arrival / departure | ZTP čl. 22 st. 1 |
| GFI after status change, liquidation, bankruptcy | Within 90 days | ZOR čl. 47 |

## Things that no longer exist

- **PDV-K** (annual VAT statement): abolished (around 2015). **U-RA and PPO**
  forms: abolished from 2026 (secondary sources: fiskai.hr, minimax.hr).
- **Porez na kuće za odmor**: abolished from 1 Jan 2025, replaced by porez na
  nekretnine (ZLP, NN 152/24).
- **VAT deadline on the 20th**: replaced by the last day of the following
  month from 1 Jan 2026 (NN 151/25).
- There is no general employer duty to give employees an annual income
  statement under the current Pravilnik.

## Open points (VERIFY)

- ZPDV payment article (čl. 76 st. 1 inferred from structure).
- Non-profit reporting pravilnik article and NN numbers.
- TZ form date for companies and obrt (set in the form pravilnik; in practice
  with the DOH / PD return).
- National legal basis for Intrastat deadlines.
- Annual contribution top-up for obrtnici on DOH (ZOD article).
- zakon.hr may lag: the Pravilnik o paušalnom oporezivanju is consolidated to
  NN 16/25; check for later amendments.

## Sources

- ZPDV: https://www.zakon.hr/z/1455/zakon-o-porezu-na-dodanu-vrijednost ;
  NN 151/25: https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_151_2262.html
- ZPD: https://www.zakon.hr/z/85/zakon-o-porezu-na-dohodak
- Pravilnik o porezu na dohodak: https://www.zakon.hr/c/podzakonski-propis/60043/
- Pravilnik o paušalnom oporezivanju: https://www.zakon.hr/c/podzakonski-propis/60049/
- ZPDobit: https://www.zakon.hr/z/99/zakon-o-porezu-na-dobit
- ZOD: https://www.zakon.hr/z/365/zakon-o-doprinosima
- ZOR: https://www.zakon.hr/z/118/zakon-o-racunovodstvu
- ZTP: https://www.zakon.hr/z/2071/zakon-o-turistickoj-pristojbi
- ZČTZ: https://www.zakon.hr/z/341/zakon-o-clanarinama-u-turistickim-zajednicama
- ZF: https://narodne-novine.nn.hr/clanci/sluzbeni/2025_06_89_1233.html
- OPZ: https://www.zakon.hr/z/100/opci-porezni-zakon ;
  ZUP: https://www.zakon.hr/z/65/zakon-o-opcem-upravnom-postupku
- ZLP: https://www.zakon.hr/z/875/zakon-o-lokalnim-porezima
- Zakon o radu čl. 92: https://zakoni.lexium.hr/zakon-o-radu/clanak/art92
- DZS Intrastat upute 2026: https://dzs.gov.hr/UserDocsImages/dokumenti/Intrastat%20upute%202026.pdf
