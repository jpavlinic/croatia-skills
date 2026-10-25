---
name: hr-eu-funding
description: >-
  Finding, checking eligibility for, applying to and staying compliant with grants,
  subsidies and subsidised loans in Croatia: EU funds (PKK, ITP, ULJP/ESF+, SP ZPP,
  Interreg, Horizon Europe, EIC Accelerator, LIFE, Erasmus+, Creative Europe) and national
  schemes (HZZ, FZOEU, HAMAG-BICRO, HBOR, ministries, cities, counties). For entrepreneurs,
  SMEs, startups, NGOs, farmers and households. Covers de minimis, SME definition,
  eligible costs, writing the application, budget, procurement (NOJN), reporting,
  visibility and repayment risk. Triggers: "EU fondovi", "EU funding Croatia", "grant",
  "subsidy", "bespovratna sredstva", "natječaj", "javni poziv", "poziv na dostavu
  projektnih prijedloga", "prijava projekta", "upute za prijavitelje", "potpora za
  samozapošljavanje", "HZZ potpora", "HAMAG-BICRO", "HBOR kredit", "FZOEU", "solarni
  paneli poticaj", "dizalica topline poticaj", "NPOO", "de minimis", "potpora male
  vrijednosti", "eKohezija", "APPRRR", "OPG natječaj", "LAG natječaj", "NOJN".
---

# Croatian grants, subsidies and EU funds (hr-eu-funding)

Helps Claude find **current** calls for Croatian applicants, test eligibility, draft a
strong application (in Croatian or English) and keep a beneficiary compliant after the
award. Funding calls open and close every month, so this skill teaches a **method** plus a
**dated snapshot**. The snapshot is never proof that a call is open today.

Status: researched 2026-10-25. Landscape snapshot valid as of that date only.

> **Not legal, tax or financial advice.** This skill provides general,
> research-based information that may be incomplete or out of date. Always
> verify with the official sources cited and consult a qualified professional
> (lawyer / odvjetnik, tax adviser / porezni savjetnik, accountant /
> računovođa) before acting.

**End every answer on these topics** with one line in the user's language:
- EN: *This is general information, not legal or tax advice. Check the cited sources and consult a professional.*
- HR: *Ovo su opće informacije, a ne pravni ni porezni savjet. Provjerite navedene izvore i posavjetujte se sa stručnjakom.*

**Start every generated document** (application draft, budget, business plan, checklist
handed to the user) with:
- HR: `PREDLOŽAK – nije pravni savjet. Prilagodite ga svom slučaju i dajte ga na provjeru stručnjaku.`
- EN: `TEMPLATE – not legal advice. Adapt it to your case and have it reviewed by a professional.`

## How to use

### 1. Pin the facts that change the answer
Ask (or infer and state the assumption):

| Fact | Why it matters |
|---|---|
| Applicant type: natural person / unemployed person / obrt / d.o.o. / j.d.o.o. / OPG / udruga / zadruga / public body | Every call lists eligible applicant types |
| Size: headcount (GJR), turnover, balance sheet, **linked and partner enterprises** | SME status per Recommendation 2003/361 decides eligibility and aid intensity |
| Sector and **NKD 2025** code (main and planned activity) | Many calls exclude NKD areas (e.g. trade, accommodation, agriculture, real estate) |
| Location: county and town/municipality, **development index group** (skupina razvijenosti I.–VIII.), island, assisted area | Regional calls (ITP, LAG), higher intensity, extra points |
| Project type: investment, equipment, R&D, digitalisation, energy, hiring, training, export | Determines programme and state-aid rule (de minimis vs GBER) |
| Timeline: when must spending start; has anything been bought or ordered already? | Costs before the eligibility date, or works started before applying, are usually ineligible |
| Co-financing capacity and cash flow (pre-financing until reimbursement) | Grants usually reimburse later; own share often 15–60 % |
| **De minimis already received in the last 3 years** (all linked enterprises) | €300,000 ceiling, Reg. (EU) 2023/2831 |
| Tax debts, blocked accounts, "poduzetnik u teškoćama" status | Most common hard exclusion |

### 2. Load only the reference you need

| Need | File | Grep hints |
|---|---|---|
| Who funds what in 2026, dated snapshot, URLs | `references/landscape-2026.md` | `PKK`, `ITP`, `ESF`, `NPOO`, `APPRRR`, `HAMAG`, `HBOR`, `grad`, `LAG` |
| SME definition, linked/partner, de minimis, GBER, undertaking in difficulty, tax certificate, double funding, NKD exclusions | `references/eligibility-state-aid.md` | `2003/361`, `partner`, `2023/2831`, `GBER`, `teškoćama`, `Porezn`, `dvostruk` |
| Structure, Croatian terminology, indicators, budget rules, VAT, SCOs, rejection reasons | `references/application-writing.md` | `Pojmovnik`, `pokazatelj`, `DNSH`, `PDV`, `SCO`, `odbij` |
| Procurement (NOJN), reporting, visibility, retention, durability, irregularities, changes | `references/after-award-compliance.md` | `NOJN`, `vidljivost`, `65`, `82`, `nepravilnost`, `izmjen` |
| HZZ self-employment subsidy 2026 (amounts by NKD group, scoring, obligations, repayment) + hiring subsidy summary | `references/hzz-self-employment.md` | `skupina`, `bodov`, `24 mjeseca`, `povrat`, `zapošljavanje` |
| FZOEU household calls 2026 (solar, heat pump, battery, energy renovation, EVs) | `references/fzoeu-households.md` | `EnU-6/26`, `M1`, `M2`, `M3`, `siromaštv`, `vozila` |
| Horizon Europe, EIC Accelerator, Digital Europe, LIFE, Erasmus+, Creative Europe, Interreg | `references/eu-direct-programmes.md` | `EIC`, `Funding & Tenders`, `LIFE`, `Interreg`, `Erasmus` |
| Consultants: fees, what they do, red flags | `references/application-writing.md` | `Konzultant` |
| All sources with dates | `references/sources.md` | |

### 3. Find and check current calls (always, before advising)
1. **Search the live portals**, newest first (details in `landscape-2026.md`):
   - EU cohesion calls (PKK, ITP, ULJP): `eufondovi.gov.hr` → Pozivi, and the
     **Indikativni godišnji plan objave poziva** (planned calls by quarter). Applications go
     through **eKohezija** (`ekohezija.gov.hr`). The old `strukturnifondovi.hr` is now an
     archive (`arhiva.strukturnifondovi.hr`) for 2014–2020.
   - Agriculture/rural: `apprrr.hr` → Natječaji, `ruralnirazvoj.hr` (SP ZPP), local **LAG** sites.
   - Ministries' own pages (e.g. `mingo.gov.hr` → Otvoreni pozivi, `mzozt.gov.hr`), `esf.hr`.
   - National agencies: `mjere.hzz.hr`, `fzoeu.hr` (applications via eFZOEU at `fondovi.gov.hr`),
     `hamagbicro.hr`, `hbor.hr`.
   - City/county/development agency pages (e.g. `zagreb.hr` → Javni pozivi; county
     development agencies, often called RRA).
   - EU direct programmes: the EU Funding & Tenders Portal.
   Use a web search tool if available. If none is available, say the live check could not
   be done and present the snapshot as dated.
2. **Open the call documents** (not news summaries): Poziv / Upute za prijavitelje (UzP),
   Prilozi (obrasci, Opći uvjeti, Pravila o financijskim korekcijama, Program potpora),
   Pitanja i odgovori, and every **Izmjena** (amendments override the original).
3. **Run the eligibility checklist** (`eligibility-state-aid.md` §8): applicant, size,
   NKD, location, project, costs, timing, de minimis headroom, exclusions. Quote the UzP
   section for each item.
4. **Classify the call**: fixed deadline vs **trajni (otvoreni) poziv** (open until funds
   run out, often first come, first served, may be suspended, "privremena obustava"),
   and the assessment method: administrative check only vs scoring with a threshold.
5. **Report** to the user: call name + reference code, funder, status checked on [date],
   deadline, amounts/intensity, the 3–5 eligibility risks, documents to start now, and
   what still needs a professional.

### 4. Write or review the application
Use `application-writing.md` and the templates in `assets/`. For Croatian text also apply
`croatia:croatian-language` (formal style, polite capital **Vi** when addressing one
person). Mirror the call's own wording for objectives and indicators.

| Asset | Use |
|---|---|
| `assets/projektni-prijedlog-predlozak.md` | Bilingual (HR/EN) proposal outline: call summary, problem → objectives → activities → indicators → budget → capacity → risks → sustainability → horizontal principles/DNSH, pre-submission checklist |
| `assets/proracun-predlozak.md` | Bilingual budget outline: parameters, cost lines with eligibility/VAT/procurement columns, financing plan, cash-flow and pre-financing, checks |

Both start with the PREDLOŽAK/TEMPLATE line; keep it in anything generated from them.

### 5. After the award
Use `after-award-compliance.md`: procurement before buying anything, visibility within
the deadline, separate accounting, reporting dates, durability, keeping documents.

## Core rules (cover most cases)

1. **Never present a call as open from memory.** Check the live page, state the check date.
   If a call is from the snapshot, say "as of 2026-10-25, VERIFY".
2. **Do not buy, order or start works before the call allows it.** Most calls make costs
   eligible only from a set date (submission, publication or contract), and many require
   that works have not started (incentive effect, GBER Art. 6).
3. **The call documents win** over this skill, news articles and consultants. Amendments
   (izmjene) win over the original text.
4. **De minimis: €300,000 per "single undertaking" over any rolling 3 years**
   (Reg. (EU) 2023/2831, in force 1 Jan 2024 to 31 Dec 2030); primary agriculture has its
   own ceiling (Reg. 1408/2013 as amended by Reg. 2024/3118; €50,000, VERIFY). Count every
   linked company and every grantor (state, county, city, HZZ, FZOEU, HAMAG-BICRO interest
   subsidies, guarantees).
5. **SME status is computed with linked and partner enterprises** (Recommendation
   2003/361): micro < 10 staff and ≤ €2 m turnover or balance; small < 50 and ≤ €10 m;
   medium < 250 and turnover ≤ €50 m or balance ≤ €43 m.
6. **Clean tax record**: no unpaid tax/contribution debts (potvrda Porezne uprave, usually
   not older than 30 days, VERIFY per call); no blocked account. Debts settled by an
   upravni ugovor with the Tax Administration are accepted by some calls (e.g. HZZ).
7. **No double financing** of the same cost from two public sources (CPR 2021/1060
   Art. 63(9)); declarations are signed under material and criminal liability.
8. **Own funds must be real**: plan pre-financing; most grants pay after expenditure
   is verified (advance payments exist in some calls, often against a guarantee).
9. **Beneficiaries that are not public contracting authorities still follow procurement
   rules** (NOJN annex of the call) for EU-funded purchases; splitting purchases to stay
   under thresholds leads to financial corrections.
10. **Keep everything**: generally 5 years from 31 Dec of the year of the final payment
    for cohesion funds (CPR Art. 82), longer if the call or state-aid rules say so
    (10 years for state aid records, GBER Art. 12). Durability usually 5 years (3 for SMEs
    if the call allows) after final payment (CPR Art. 65).
11. **2026 transitions**: the Recovery and Resilience Plan (NPOO) measures had to be
    completed by **31 Aug 2026**; final payment requests in autumn 2026. Do not suggest new
    NPOO calls. The GBER (Reg. 651/2014) expires **31 Dec 2026**; a new GBER is expected
    from 1 Jan 2027 (VERIFY). The 2021–2027 cohesion period runs to end-2029 for spending.
    The next EU budget (2028–2034) is still being negotiated (VERIFY).
12. **Consultants are optional.** Never endorse a specific firm. See red flags in
    `application-writing.md`.

## Quick landscape (snapshot 2026-10-25, VERIFY all on the live portal)

| Funder | Instrument | For | Typical amount / intensity | Call rhythm | URL |
|---|---|---|---|---|---|
| Ministries via PKK 2021–2027 (ERDF/CF) | Grants for SMEs: innovation, S3, digital, internationalisation | SMEs, business support organisations | e.g. "Inovacije procesa u S3 područjima" PK.1.3.11: €150,000–450,000, open to 31 Dec 2026 | Several calls/yr; many are trajni | eufondovi.gov.hr |
| ITP 2021–2027 | Territorial calls (urban areas, Just Transition) | SMEs, cities, NGOs in target areas | Call-specific | Per indicative plan | eufondovi.gov.hr |
| ULJP 2021–2027 (ESF+) | Employment, social inclusion, education | NGOs, employers, public bodies | Call-specific | Several/yr | esf.hr, eufondovi.gov.hr |
| SP ZPP 2023–2027 / APPRRR | Investment interventions (73.xx), young farmers (75.01), LAG calls | Farmers, OPG, food processors, rural actors | e.g. investment aid from 45 % (+ increments) | Several/yr; LAG calls locally | apprrr.hr, ruralnirazvoj.hr |
| HZZ | Self-employment subsidy | Unemployed persons registered with HZZ | 2026: up to €7,000 / 10,000 / 15,000 (fixed €5,000 + variable) | Annual; 2026 window closed 30 Sep 2026 | mjere.hzz.hr |
| HZZ | Hiring subsidies, on-the-job training | Employers | 2026: monthly flat €420–1,130 by group/education | Annual | mjere.hzz.hr |
| FZOEU | Households: heat pump, PV, battery (EnU-6/26) | House owners resident ≥ 30 days | 50 % (70 % energy-poor), max €6,250/6,000/5,600 (€8,750/8,400/7,840) | Opened 2 Sep 2026, temporarily closed 3 Sep 2026 | fzoeu.hr |
| FZOEU / MZOZT | Business calls (EVs, Modernisation Fund, waste) | Companies, crafts, LGUs | Call-specific | Indicative annual plan | fzoeu.hr, mzozt.gov.hr |
| HAMAG-BICRO | Micro loans, guarantees, innovation grants | Micro/small, startups, innovators | "Mikro zajmovi za rast i uključenost": max raised to €50,000 (Sep 2026) | Rolling, often suspended | hamagbicro.hr |
| HBOR | Subsidised loans (young, women, start-ups) | MSMEs, OPG | 2026: up to €400,000, fixed 3.00–3.90 % (direct) | Rolling | hbor.hr |
| Cities / counties | Small de minimis grants, interest subsidies | Local crafts, SMEs | Typically €1,500–20,000 | Annual, often Q1 | city/county sites |
| EU direct (EIC, Horizon, LIFE, Erasmus+, Creative Europe, Interreg) | Competitive grants, often in consortia | SMEs, startups, NGOs, research | EIC Accelerator grant < €2.5 m + equity €1–10 m | Fixed cut-offs | Funding & Tenders Portal |

Details, sources and the dates of each figure are in `references/landscape-2026.md`.

## Keeping current

| Fact | Goes stale | Check at |
|---|---|---|
| Which calls are open, deadlines, suspensions | Weekly | eufondovi.gov.hr, apprrr.hr, fzoeu.hr, mjere.hzz.hr, hamagbicro.hr, ministry pages |
| HZZ measures and amounts | Each January (new "Uvjeti i načini korištenja sredstava") | mjere.hzz.hr |
| FZOEU household calls | Each year (indicative plan published ~January) | fzoeu.hr, mzozt.gov.hr |
| De minimis ceilings | Rare (Reg. 2023/2831 to 2030) | eur-lex.europa.eu, mfin.gov.hr |
| GBER | 1 Jan 2027 (new regulation expected) | competition-policy.ec.europa.eu |
| NOJN thresholds | When ZJN thresholds change (ZJN amendment NN 48/2026, simple-procurement thresholds €50,000 / €100,000 from 1 Sep 2026; NOJN annexes may lag) | the call's NOJN annex, narodne-novine.nn.hr |
| SME definition | Commission review ongoing (VERIFY) | single-market-economy.ec.europa.eu |
| EU 2028–2034 programmes | Negotiation ongoing | commission.europa.eu |

Anything a project needs to remember between sessions (e.g. de minimis received, deadlines,
chosen calls) goes in the user's project, e.g. `.claude/croatia/hr-eu-funding.md`, never in
this skill's files.
