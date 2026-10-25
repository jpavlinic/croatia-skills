---
name: hr-legal-compliance
description: >-
  Croatian + EU legal compliance for SaaS, apps, websites and online businesses in or selling into
  Croatia/the EU. Use when building, auditing or advising: GDPR + ZPDZ/AZOP,
  privacy policy, cookies (ZEK čl. 43), e-mail marketing and contacting people (ZEK čl. 50, soft opt-in, cold B2B,
  "Ne zovi"), consumer law (ZZP: withdrawal button, order button, 14-day withdrawal for SaaS), terms under ZOO,
  retention, fiscalization/eRačun/VAT/OSS for payment-provider sales, impresum (ZTD čl. 21, ZET čl. 6),
  DSA, AI Act, EAA, Data Act, NIS2, CRA, product liability, language law, OSS licences, comparative advertising.
  Triggers: "is this legal", "GDPR", "privacy policy", "politika privatnosti", "uvjeti korištenja", "opći uvjeti",
  "terms of service", "cookie banner", "kolačići", "privola", "newsletter consent", "can I email", "unsubscribe",
  "data retention", "delete account", "fiskalizacija", "eRačun", "AZOP", "impresum", "legal audit",
  "zaštita potrošača", or making a Croatian project "fully legal". Not legal advice.
---

# Croatian + EU legal compliance for software products

Research-based compliance knowledge for a small business (obrt or d.o.o.) running a SaaS, web/mobile app, content
site or online shop from Croatia or selling into Croatia/the EU. Use it to (1) answer legality questions, (2) audit
a codebase and its public pages, (3) draft legal texts and compliant implementations.

Status: researched 2026-10-05; time-sensitive points (Digital Omnibus, DPF, AI Act Art 50, ZZP price display,
Fiskalizacija pravilnik, GDPR procedural regulation, Data Act switching) re-checked 2026-10-25. Items marked
**VERIFY** in the references were not confirmed against a primary source or are still moving.

> **Not legal, tax or financial advice.** This skill provides general, research-based information that may be
> incomplete or out of date. Always verify with the official sources cited and consult a qualified professional
> (lawyer / odvjetnik, tax adviser / porezni savjetnik, accountant / računovođa) before acting.

## Disclaimer rules (always apply)

1. **End every answer that touches law, tax or compliance** with one line in the user's language:
   - EN: *This is general information, not legal or tax advice. Check the cited sources and consult a professional.*
   - HR: *Ovo su opće informacije, a ne pravni ni porezni savjet. Provjerite navedene izvore i posavjetujte se sa stručnjakom.*
2. **Start every generated document** (policy, terms, DPA, notice, e-mail template, checkout copy, audit report,
   invoice logic) with:
   - HR: `PREDLOŽAK – nije pravni savjet. Prilagodite ga svom slučaju i dajte ga na provjeru stručnjaku.`
   - EN: `TEMPLATE – not legal advice. Adapt it to your case and have it reviewed by a professional.`
   Every file in `assets/` already starts with this line; keep it when you copy from them. For a document that will
   be published, tell the user to remove the line only after professional review.
3. Surface relevant **VERIFY** items as questions for a lawyer or accountant, never as settled law.

## Be realistic. Never oversell.

- An audit does not have to find something. If an area is genuinely compliant, say so plainly, with the evidence,
  and move on. Do not invent or pad findings, inflate severities, or turn best practice into "legal requirements".
- Say how real a risk is: what the law actually requires, who enforces it, and how likely enforcement is in
  practice. Separate "illegal now" from "only matters if a breach or complaint happens" from "nice to have".
- If something is bad, say it is bad, without hedging. If something is good, say it is good.
- When the user accepts a risk, record it in the project memory file (below) and stop raising it.

## How to use

1. **Read project memory first.** If `.claude/croatia/legal-compliance.md` exists in the user's project, read it:
   accepted risks, decisions, prior findings, facts already pinned. Do not re-raise accepted risks.
2. **Pin the facts that change the answer** (ask or infer; say what was assumed): legal form and VAT status · B2B
   only or consumers too · customer countries · whose personal data is stored (users only, or third parties inside
   user content) · AI features / public user content · headcount and turnover.
3. **Load only the reference(s) needed** (they are long; grep first):

| Topic | File | Grep hints |
|---|---|---|
| Audit procedure, checklist, report format | `references/00-audit-playbook.md` | `Phase`, `### A.` … `### K.` |
| GDPR, ZPDZ, AZOP fines, lawful bases, privacy-policy contents, rights, DPA, ROPA, transfers/DPF, retention, logs, minimisation | `references/01-gdpr-data-protection.md` | `Art 13 checklist`, `Lawful bases`, `Retention`, `DPF`, `AZOP`, `Annex` |
| Cookies/trackers, banners, fonts, e-mail marketing, soft opt-in, trial e-mails, cold B2B, Ne zovi, unfair practices, templates, "can I send this e-mail" | `references/02-cookies-marketing-contacting.md` | `43`, `čl. 50`, `Inteligo`, `4.4`, `7.1`–`7.7`, `Decision tree` |
| ZZP (pre-contract info, order button, withdrawal for SaaS, "Raskid ugovora", complaints, ADR, unfair terms, fines, price display), digital-content act, ZET, impresum, ZOO terms, liability caps, jurisdiction, professional-tool disclaimers, subscriptions, geo-blocking | `references/03-consumer-contracts-terms.md` | `Art 74`, `81.a`, `Art 10`, `345`, `Rome I`, `bazna`, `(c) Sample`, `(d) Impressum` |
| Fiskalizacija 2.0, eRačun, invoice content, VAT/PDV-ID/reverse charge/OSS, retention, payment providers/PCI/SCA, penalties (legal "what") | `references/04-tax-fiscalization-payments.md` | `1.7`, `Art 39`, `Art 29`, `OSS`, `PDV-ID`, `penalt` |
| EAA, DSA (+ HAKOM notice), Data Act, AI Act, NIS2, CRA, product liability, language law, copyright/OSS licences, trademarks, sector rules, comparative advertising, testimonials, security baseline | `references/05-other-regulations.md` | `Summary table`, `Prioritised`, `DSA`, `AI Act`, `PLD`, `Sector`, `nedopuštenom` |
| Full audit process: coverage ledger, 5 parallel scopes + prompt templates, cross-consistency matrix, adversarial master list | `references/06-exhaustive-audit-procedure.md` | `Step`, `Master list`, `templates` |
| Findings catalog: anonymous recurring problems, where to look, fixes | `references/07-findings-catalog.md` | `## A.` … `## F.` |
| English ↔ Croatian legal glossary (official terms + defining act) | `references/08-glossary-en-hr.md` | the English or Croatian term |

4. **Cite sources.** Every claim cites act + article (e.g. "ZZP čl. 81.a", "GDPR Art 13(2)(d)"). For code audits,
   every finding also cites `file:line` or "NOT FOUND (searched: …)".
5. **Drafting legal texts** → start from `assets/` and fill from the project's real behaviour. A legal text that
   contradicts the code is itself a finding (GDPR Art 5(1)(a), 12, 13; ZZP čl. 35 misleading practice). Use the
   official Croatian terms from `08-glossary-en-hr.md`.
6. **Croatian output** (policies, e-mails, UI copy) → also apply `croatia:croatian-language`. Address one reader with
   the polite capital *Vi/Vaš/Vam*; follow the project's existing house style where the standard allows it.
7. **Do not modify a project during an audit** unless explicitly asked; report only.
8. **Any audit request = exhaustive by default.** Follow `06-exhaustive-audit-procedure.md` end to end: read project
   memory → enumerate every surface into a coverage ledger → dispatch 5 parallel read-only scopes (A backend data,
   B app UI/flows, C website/content, D billing/tax, E cross-cutting) → cross-consistency matrix (policy vs terms vs
   site vs app vs e-mails vs code vs invoices vs payment provider) → adversarial master-list pass until nothing new
   appears → report. Skim `07-findings-catalog.md` first and search the project for each pattern that fits.
   A small, scoped question ("is this e-mail OK?") does not need the full procedure.
9. **After an audit or decision, offer to update project memory** at `.claude/croatia/legal-compliance.md` in the
   user's project (create it if missing): pinned facts, accepted risks (with date and reason), decisions, open
   findings and their status, VERIFY questions sent to a professional. Never edit this skill's own files.
10. **Fixing a live product = no breaking changes.** Existing users notice nothing unless they act: new opt-out flags
    default to current behaviour, no already-sent e-mail is re-sent, terms/consent versioning grandfathers existing
    users; migrations are additive; plan deploy order (backend → app → website) and re-probe in production. State
    this constraint in every implementation plan.

## Related skills in this plugin

`croatia:hr-fiscalization-dev` (how to implement fiscalization/eRačun in code) · `croatia:hr-business-admin` (obrt vs
d.o.o., paušal, registration, VAT registration) · `croatia:hr-payroll-employment` (labour law, salaries) ·
`croatia:hr-identifiers` (OIB/IBAN/VAT ID validation) · `croatia:hr-localization` (formats, currency, dates) ·
`croatia:hr-tourism-rentals` · `croatia:hr-real-estate` · `croatia:hr-eu-funding` · `croatia:croatian-language`.

## Assets

| File | Use |
|---|---|
| `assets/politika-privatnosti-template.md` | Croatian privacy policy (controller) with per-purpose basis/retention table |
| `assets/opci-uvjeti-template.md` | Croatian terms of use and sale: B2B + optional consumer sections, optional professional-tool clause, liability cap |
| `assets/snippets.md` | Sign-up consent block + consent schema, consumer checkout block, "Raskid ugovora" flow, e-mail footers + `List-Unsubscribe`, contact-form notice, report footer, Art 28 DPA skeleton, retention YAML |

## Non-negotiables (the short list that catches most problems)

**Data protection**
- Lawful basis per purpose; the privacy policy names the controller (OIB + street address), every processor and
  each third-country transfer mechanism (DPF Decision 2023/1795 / SCCs 2021/914 — never "may transfer"), concrete
  retention, all rights incl. withdrawal of consent, a separately highlighted right to object, AZOP complaint.
- Art 28 DPA with every processor (AZOP's €2.265M B2 Kapital fine). Offer your own DPA when storing customers'
  third-party data (SaaS = processor for that content). ROPA always (the <250 exemption rarely fits a SaaS).
- Self-service export + complete deletion (also cancel the subscription at the payment provider, notify processors);
  keep only billing records (11 y ZoR / 6 y fiscalized eRačun / OPZ) and contract-acceptance proof (5 y; B2B 3 y).
- Croatian digital-consent age is **16** (ZPDZ čl. 19).
- No secrets in git; masking before every log shipper; breach → AZOP within 72 h (incidenti@azop.hr).

**Cookies and contact**
- Nothing non-essential (analytics, pixels, font CDNs, embeds) before opt-in; Reject as prominent as Accept. No
  analytics exemption in Croatian law today. Fines: ZEK čl. 170 €13,270–132,720 (legal person).
- Marketing e-mail to natural persons (incl. obrtnici, freelancers) needs consent or soft opt-in (ZEK čl. 50(2);
  CJEU C-654/23 *Inteligo*: a free trial of a paid service counts) with opt-out offered **at collection** and in
  every message. Legal persons are outside čl. 50(1)–(2), but named-employee addresses still need GDPR LI + Art 14
  notice. Discount / "upgrade now" / win-back mails are marketing; neutral trial-status mails are service.
- Every marketing mail: sender identity, one-click unsubscribe + `List-Unsubscribe`, per-user suppression.

**Consumers** (only if consumers can buy — "students", "private persons", optional company field ⇒ yes)
- Prices incl. VAT in EUR; pre-contract info in Croatian; button "Naruči s obvezom plaćanja" (else the order is not
  binding, ZZP čl. 74(4)); confirmation on a durable medium; 14-day withdrawal for SaaS cannot be fully waived — only
  pro-rata after an express request (ZZP čl. 77, 84(8)); **"Raskid ugovora" function since 19 June 2026** (no-grace
  offence); written complaint reply ≤ 15 days; ADR info; **remove ODR links** (platform closed 20 July 2025).
- **From 17 Nov 2026** consumer-facing traders and service providers must show a *bazna cijena* (reference price)
  and publish a machine-readable price list; the rulebooks are still in consultation — **VERIFY** scope for online
  subscriptions (`03` §1.2a).
- No "changes without notice", no blanket "no refunds", no forcing consumers to a Zagreb court, liability cap never
  for intent/gross negligence (ZOO čl. 345) or product liability (ZOO čl. 1079 from 9 Dec 2026).

**Tax and invoicing** (legal "what"; implementation → `croatia:hr-fiscalization-dev`)
- Every B2C invoice fiscalized (JIR/ZKI/QR) whatever the payment method — paušalisti too — since 1 Jan 2026.
  Domestic B2B: eRačun (VAT payers since 2026, non-VAT issuers from 1 Jan 2027) or the Art 39 card route.
- VAT: HR 25 %; EU B2B reverse charge only with a **VIES-validated** VAT ID; EU B2C ≤ €10k/yr EU-wide → Croatian VAT
  and fiscalize; > €10k → OSS; non-EU → outside EU VAT (check local GST). Payment providers do not fiscalize.
- Payment-provider receipts must not pose as invoices before the fiscal invoice (Zakon o fiskalizaciji čl. 29).

**Other**
- Company identity on the website: d.o.o. → name, seat, court + MBS, OIB, share capital paid, director, bank + IBAN
  (ZTD čl. 21(4)–(5)); plus ZET čl. 6 contact info. Same identity in the app and e-mails.
- DSA: a service storing user content is a hosting service → contact points, T&C moderation section, notice and
  action, statement of reasons, HAKOM notification (e-Pružatelj DSA).
- EAA: micro service providers exempt (re-test yearly). NIS2: size cap excludes micro. CRA: only downloadable
  products. AI Act Art 50 applies since 2 Aug 2026; machine-readable marking for generative systems already on the
  market by **2 Dec 2026**.
- Claims: no "certificiran / odobren od Ministarstva / službeni" unless provable; comparative content must be
  verifiable, dated, non-denigrating, no competitor logos (Zakon o nedopuštenom oglašavanju čl. 6, reversed burden).
- Open source: third-party notices page (MPL/LGPL code shipped to browsers needs a source pointer); CI gate against
  AGPL/GPL/SSPL.

## Where the references disagree (resolve explicitly when relevant)
- **Data Act Ch. VI for SaaS**: `03` says likely in scope; `05` says likely out where computing is incidental
  (Commission FAQ). Treat as open; offering full export + termination assistance satisfies both views cheaply.
- **ZZP čl. 19 30-day lowest-price rule for SaaS discounts**: `03` (read from text) says the display duty excludes
  distance services; `02` notes the "below the 30-day minimum" sale rule. Prefer `03` for display; never run a fake
  "sale", and misleading-practice rules always apply.
- **Fiscalization of B2C sales to non-EU consumers**: the Tax Administration's Q&A suggests no; the HOK leaflet
  suggests yes → safest is to fiscalize every sale whose place of supply is Croatia and ask the Porezna uprava.

## Keeping current
These laws change often: ZZP (amended 06/2026; price-display rulebooks in consultation until 13 Nov 2026), ZOO
(06/2026, product liability from 9 Dec 2026), ZEK (04/2026), Fiskalizacija pravilnik (09/2026), GDPR "Digital
Omnibus" (Council mandate 21 Oct 2026, Parliament pending), GDPR procedural regulation 2025/2518 (applies 2 Apr
2027), DPF (appeal C-703/25 P pending), Data Act switching charges (zero from 12 Jan 2027). When advice depends on a
date-sensitive point, check narodne-novine.nn.hr, zakon.hr, azop.hr, porezna-uprava.gov.hr, hakom.hr, eur-lex.europa.eu
for changes after 2026-10-25 and say what you checked. Record project-specific conclusions in the project memory
file, not in this skill.
