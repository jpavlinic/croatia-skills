# Compliance audit playbook: auditing a codebase/product against Croatian + EU law

Use this file when asked to audit a concrete project (backend + frontend + marketing site). It turns the
law in references 01–05 into things that can be found (or not found) in code, config and pages.

Rule of thumb: **every finding must cite the file:line (or "NOT FOUND" + what was searched) AND the legal
source** (article + act). Never "fix" anything during an audit unless the user explicitly asks.

---

## Phase 0 — establish the facts that change the answer

First read the project memory file `.claude/croatia/legal-compliance.md` if it exists (pinned facts, accepted
risks, prior findings). Then answer these; most later conclusions depend on them.

| Question | Why it matters | Where to look |
|---|---|---|
| Legal form: obrt (paušal / na dohodak) or d.o.o./j.d.o.o.? VAT payer? | Impressum content (ZTD Art 21 vs Zakon o obrtu), VAT on invoices, eRačun dates, retention under ZoR vs OPZ | Footer, legal pages, invoice config, JSON-LD, docs |
| B2B only, or are consumers (potrošači) able to buy? | ZZP (withdrawal right, pre-contract info, price incl. VAT, ADR), ZEK Art 50 consent for marketing, Rome I / Brussels Ia | Pricing page wording, target-audience sections ("studenti", "privatne osobe"), signup form (is company mandatory?), is the tax-ID field at checkout optional? |
| Who are the data subjects? Users only, or also third parties inside user content (their clients, patients, tenants, end customers)? | Controller vs processor → need for a DPA (Art 28) | Entities / DB schema, free-text fields, report templates |
| Which countries are customers in? | OSS (€10k EU B2C), reverse charge, foreign VAT/GST, language | Payment-provider config, tax resolver, country lists |
| Any AI/LLM features? Any user-generated public content? | AI Act Art 50, DSA hosting duties | Dependencies (anthropic, openai, langchain), share-link endpoints |
| Headcount / turnover | Microenterprise exemptions (EAA services, DSA Art 15), NIS2 size cap | Ask the user if unknown |

---

## Phase 1 — inventory (read-only)

Produce an inventory with file:line citations. Suggested searches (adapt to stack):

```bash
# Personal data in schema
grep -rniE "email|phone|telefon|oib|vat|tax_id|address|adresa|ip_?address|user_?agent|birth|iban" <migrations/ entities/>
# Consent / marketing flags
grep -rniE "consent|privola|marketing|newsletter|opt.?in|opt.?out|unsubscribe|odjav|terms_?accept|tos_version" .
# Cookies / storage / trackers
grep -rniE "document\.cookie|setCookie|localStorage|sessionStorage|indexedDB|gtag|googletagmanager|G-[A-Z0-9]{6,}|fbq|hotjar|clarity|posthog|plausible|umami|mixpanel|segment|sentry|logrocket|fullstory" --include=*.{js,ts,tsx,jsx,html,vue,svelte} .
grep -rniE "fonts\.googleapis|fonts\.gstatic|youtube\.com/embed|maps\.google|recaptcha|hcaptcha|turnstile" .
# Emails
grep -rniE "List-Unsubscribe|unsubscribe|odjav|MimeMessage|JavaMailSender|sendgrid|mailgun|ses|postmark|brevo" .
# Deletion / export / retention
grep -rniE "delete.*(user|account|me)|export.*(data|account)|anonymi|retention|purge|cleanup|@Scheduled|cron" .
# Payments / invoices
grep -rniE "stripe|checkout|invoice|racun|fiskal|jir|zki|eracun|vies|reverse.?charge|oss|tax" .
# Secrets committed
git -C <repo> ls-files | grep -iE "\.env|application.*(yml|yaml|properties)|secrets|credentials|\.pem|\.p12|\.key$"
# Legal pages
find . -iname "*privat*" -o -iname "*privacy*" -o -iname "*terms*" -o -iname "*uvjet*" -o -iname "*kolacic*" -o -iname "*cookie*" -o -iname "*impressum*" -o -iname "*pristupacn*"
```

For a large codebase dispatch an Explore subagent with the inventory list from Phase 2 headings.

---

## Phase 2 — check against the law (checklist)

Mark each item ✅ compliant / ⚠️ partial / ❌ missing / ➖ not applicable, with evidence.

### A. Identity & mandatory website information
- [ ] Full legal name, seat **street address**, OIB, (VAT ID), email, phone visible on site (ZET Art 6; ZZP pre-contract info). → 03
- [ ] d.o.o.: registry court + MBS, share capital & amount paid, board members, bank/IBAN on website ("poslovno pismo" incl. web, ZTD Art 21). Obrt: name, seat, name of the obrtnik (vlasnik obrta), register. → 03
- [ ] Same identity in the **app** (not only marketing site) and in **email footers**.

### B. Privacy policy (GDPR Arts 12–14) → 01 §3, Annex (a)
- [ ] Controller identity incl. OIB + address; privacy contact.
- [ ] Purpose **+ legal basis per purpose** (table); legitimate interests named.
- [ ] Every processor/recipient category, and each **third-country transfer with its mechanism** (DPF / SCC) — no "may transfer".
- [ ] Concrete retention periods (not "as long as necessary" only).
- [ ] All rights incl. **withdrawal of consent**, **right to object shown separately**, **complaint to AZOP** (address).
- [ ] Automated decisions statement; cookies section/link; marketing section; children (16, ZPDZ Art 19).
- [ ] Version / effective date; Croatian language (EN optional extra).
- [ ] Consistency: policy claims match code (retention, processors, verification, newsletters).

### C. Records & contracts
- [ ] ROPA exists (Art 30; <250 exemption almost never applies).
- [ ] Art 28 DPA signed/accepted with **every** processor (hosting, email, logs, payments role split, analytics, form backends, fiscal intermediary).
- [ ] Own DPA offered to B2B customers if the product stores their third-party data.
- [ ] Sub-processor list published.
- [ ] Breach register + incident plan (72h to AZOP, incidenti@azop.hr).

### D. Collection points (signup, contact, newsletter, checkout)
- [ ] Short Art 13 notice + link at each form.
- [ ] Terms acceptance recorded (user, version, timestamp) — proof for contract & disputes.
- [ ] Marketing consent: separate, **unticked**, recorded (purpose, text version, timestamp, source) — or documented soft opt-in with opt-out offered **at collection** (ZEK Art 50(2)).
- [ ] Age/professional-use confirmation if relevant (ZPDZ Art 19: 16).
- [ ] Minimal fields (e.g. phone optional unless needed).

### E. Cookies & trackers (ZEK Art 43(4)) → 02
- [ ] No non-essential cookie/localStorage/pixel/fingerprinting before consent.
- [ ] Banner: Accept and **Reject equally prominent at first layer**, granular, withdrawable, consent logged.
- [ ] Google Fonts self-hosted (no IP leak to Google), YouTube via nocookie+click-to-load, maps click-to-load.
- [ ] Cookie table in policy (name, provider, purpose, duration, type).
- [ ] Auth tokens in localStorage = strictly necessary (exempt) but note XSS risk (Art 32).

### F. Email & contacting people → 02
- [ ] Transactional vs marketing classified per template; promo content (discounts, upsell offers) = marketing.
- [ ] Marketing only with consent/soft opt-in (B2C & named B2B persons under GDPR LI).
- [ ] Every marketing email: sender identity, **working unsubscribe link**, `List-Unsubscribe` + `List-Unsubscribe-Post` (one-click; also Gmail/Yahoo bulk-sender rules), honoured promptly, suppression list.
- [ ] Per-user preference flag gating sends (not only a global switch).
- [ ] Cold B2B outreach: legal basis (LI + LIA), Art 14 notice in first email, opt-out, no purchased lists.
- [ ] Phone calls: check do-not-call register (Registar "ne zovi") for consumer numbers.

### G. Data-subject rights & lifecycle → 01 §4, §10
- [ ] Self-service export (Art 15/20) — account-level, machine-readable.
- [ ] Rectification incl. email change.
- [ ] Deletion: complete (all tables, processors notified: payment-provider customer, email provider, logs), **cancels active subscription**, keeps only legally required billing data (Art 17(3)(b)).
- [ ] Retention jobs per category (inactive/trial accounts, logs, backups, tokens).
- [ ] Backups: encrypted, off-site, rotation documented.
- [ ] DSAR process: mailbox, 1-month deadline, log.

### H. Security (Art 32) → 01 §7
- [ ] **No secrets in git** (rotate any that were committed; history keeps them).
- [ ] Password hashing (bcrypt/argon2), MFA for admin, rate limiting/brute-force protection on auth.
- [ ] HTTPS + HSTS, CSP, CORS allowlist, CSRF where cookies authenticate.
- [ ] Logs: PII/secret masking **before** every appender/shipper, retention set, IP truncation.
- [ ] Admin console: least privilege, audit trail of admin access to user data.
- [ ] Dependency updates; restore tests.

### I. Consumer & contract (if B2C possible) → 03
- [ ] Pre-contract info (ZZP Art 60 for distance contracts) before order; confirmation on durable medium (Art 76).
- [ ] Order button "Naruči s obvezom plaćanja" (statutory phrase: "narudžba s obvezom plaćanja") or equivalent unambiguous wording.
- [ ] Withdrawal right info + **express consent & acknowledgement of loss** for immediate start of a digital service; model withdrawal form; **withdrawal button/function** (Directive 2023/2673, from 19 June 2026).
- [ ] Prices for consumers **incl. VAT, in EUR**; trial-to-paid terms clear; cancellation as easy as signup.
- [ ] From 17 Nov 2026: *bazna cijena* shown next to the current price and a machine-readable price list published, unless an exemption applies (rulebooks in consultation, **VERIFY**). → 03 §1.2a
- [ ] Complaint procedure (written reply ≤15 days, ZZP Art 10), ADR body info; **remove ODR links** (platform closed 20 July 2025).
- [ ] No unfair terms: no unilateral changes "without notice", no blanket refund exclusion overriding statutory rights, no consumer-jurisdiction clause forcing Zagreb court, liability limits that respect ZOO Art 345 and consumer law.
- [ ] Digital content/service conformity & updates (ZDS / Directive 2019/770).
- [ ] Professional-tool disclaimer where the product produces calculations, reports or advice-like output (tool, not professional advice; user verifies; standards claims accurate).
- [ ] Terms consistent with real product behaviour.

### J. Tax, invoices, fiscalization → 04
- [ ] Every B2C sale fiscalized (JIR/ZKI/QR) — all payment methods since 1.1.2026.
- [ ] Domestic B2B: eRačun (VAT payers since 1.1.2026; non-VAT issuers from 1.1.2027) or Art 39 card route.
- [ ] Invoice content per ZPDV Art 79 + numbering n/premises/device, no gaps; business premises "internetska trgovina" registered.
- [ ] VAT logic: HR 25%; EU B2B reverse charge with **VIES-validated** VAT ID; EU B2C ≤€10k → HR VAT (fiscalize), >€10k → OSS; non-EU → outside scope (check foreign GST).
- [ ] Price shown vs price charged consistent across site, app, Terms, payment provider (net vs gross!).
- [ ] Payment-provider receipts not presented as invoices before the fiscal invoice (Zakon o fiskalizaciji čl. 29 "OVO NIJE FISKALIZIRANI RAČUN").
- [ ] Refunds/chargebacks → storno invoice.
- [ ] Billing data kept 11 years (ZoR) / eRačun 6 years even after account deletion; invoice FK must not block deletion of the rest.

### K. Other regulations → 05
- [ ] Accessibility (EAA / Croatian transposition) — if not microenterprise and B2C e-commerce service: WCAG 2.1 AA + accessibility statement.
- [ ] DSA Art 11/12 contact points, Art 14 T&C moderation info (if hosting UGC), notice-and-action.
- [ ] Data Act switching/export clauses if a "data processing service".
- [ ] AI Act Art 4 AI literacy & Art 50 transparency if AI features.
- [ ] Croatian language (Zakon o hrvatskome jeziku) for consumer-facing info.
- [ ] Open-source licence notices; image/font licences; trademark of brand; comparative advertising rules for competitor content.
- [ ] Marketing claims about standards/regulation compliance are accurate and verifiable.

---

## Phase 3 — report format

The report is a generated document, so it **starts** with the template line in the user's language:
`PREDLOŽAK – nije pravni savjet. Prilagodite ga svom slučaju i dajte ga na provjeru stručnjaku.` /
`TEMPLATE – not legal advice. Adapt it to your case and have it reviewed by a professional.`

1. **Facts assumed** (legal form, B2B/B2C, countries) — and what changes if wrong. Accepted risks from project
   memory listed once as "accepted, not re-assessed".
2. **Severity-ranked findings** table: `# | Severity (Critical/High/Medium/Low) | Area | Finding (evidence file:line) | Law | Risk/penalty | Realistic likelihood | Fix`.
   - Critical: active unlawful processing at scale or security exposure (committed secrets, trackers without consent, marketing without opt-out, unfiscalized sales).
   - High: missing mandatory documents/rights mechanisms (no DPA, no export, deletion broken, missing withdrawal info for consumers).
   - Medium: incomplete/inaccurate documents, retention gaps.
   - Low: best practice.
3. **What is already good** (be fair — masking, hashing, EU e-mail region, etc.). An area with no findings is
   reported as compliant, with the evidence.
4. **Prioritised remediation plan** (week 1 / month 1 / quarter), non-breaking for live products.
5. **Documents to produce** (with template pointers in `assets/`).
6. **Open questions for a lawyer / accountant** (every VERIFY item that matters).
7. **Offer to update project memory** (`.claude/croatia/legal-compliance.md`): facts, decisions, accepted risks,
   open findings.

The report **ends** with the one-line disclaimer in the user's language:
- EN: *This is general information, not legal or tax advice. Check the cited sources and consult a professional.*
- HR: *Ovo su opće informacije, a ne pravni ni porezni savjet. Provjerite navedene izvore i posavjetujte se sa stručnjakom.*

Also remind the user to confirm VERIFY items with a Croatian lawyer/accountant and to check Narodne novine for
amendments after the skill's status date.
