# Exhaustive audit procedure ("check absolutely everything")

Use this whenever the user asks for a full / complete / thorough legal audit or "everything that needs to change".
There is **no time budget**: completeness beats speed. An audit is finished only when every row of the coverage
ledger is filled and the adversarial pass returns nothing new.

Use it together with `00-audit-playbook.md`, which has the law checklist and the report format. This file adds the
*process* that guarantees nothing is skipped.

---

## Step 0 — Load prior state
- Read the project memory file `.claude/croatia/legal-compliance.md` if it exists, plus any earlier audit report or
  TODO in the project. Read them first.
- New findings must be **deltas**: new items, or corrections to old ones. Never re-report risks the user explicitly
  accepted (they are listed in the memory file's "accepted risks" section).
- Pin the facts (playbook Phase 0). Record each assumption.

## Step 1 — Enumerate every surface (coverage ledger skeleton)
Before judging anything, **list** every unit that could carry legal risk. Each becomes a ledger row.

| Surface | How to enumerate |
|---|---|
| DB tables/columns | all migrations (`db/migration`, `prisma/schema`, `models/`), all entities |
| Endpoints | every controller/route handler, incl. admin and public, webhooks |
| Scheduled jobs / workers | `@Scheduled`, cron, queues |
| Outgoing emails | every mail-sender call site and template |
| App screens | every route under `app/`/`pages/`, plus every i18n namespace (all locales) |
| Website pages | every HTML/MDX page, layout, footer, JSON-LD, OG tags, llms.txt, sitemap, robots, headers file |
| Content | every blog post / doc / PDF / marketing one-pager |
| Generated documents | PDF/DOCX/XLSX export templates, invoices |
| Third parties | every external host in code, config, CI, IaC, package manifests, DNS (MX/SPF) |
| Client storage | every cookie, localStorage/sessionStorage/IndexedDB key, external script |
| Dependencies | production deps + licences, per repo |
| Infra & ops | hosting, regions, backups, logs, CI/CD, staging, monitoring, admin access, AI assistants with prod access |
| Organisational | DPAs, ROPA, breach register, contracts, IP assignments, trademark, insurance, registrations (HAKOM DSA, PU premises) |

## Step 2 — Parallel deep review (5 fixed scopes)
Dispatch **five read-only subagents in one message**, each given: the skill path, the references to read, the
project memory file / prior report, and the instruction to return (a) a NEW findings table, (b) corrections, (c) a coverage ledger.
Use these scopes; the prompt templates are below.

| Agent | Scope | Main references |
|---|---|---|
| A | Backend data lifecycle: tables, endpoints/IDOR, jobs, emails, admin, logs, backups, processors, Art 32, DSR | 01, 05 §14 |
| B | App UI & flows: all strings (all locales), every route, signup/checkout/cancel/delete, exports/report templates, client storage, a11y, language, OSS, in-app disclaimers, DSA | 03, 02, 01, 05 |
| C | Website & content: every page and EVERY post, claims, comparisons, outdated law statements, JSON-LD, forms, third-party resources, headers | 05 §8–12, 02 §5, 03 |
| D | Billing, tax & invoicing: invoice content, timing, storno, eRačun, VAT logic, gross/net, receipts, retention, dunning/coupons/refunds | 04, 03 §1.2, §7 |
| E | Cross-cutting: sub-processor inventory (incl. DNS/MX discovery), OSS licences (all repos), DSA, AI Act, PLD readiness, sector-rule currency, infra security incl. **live read-only probes** (HTTP/HSTS, subdomains, exposed paths), contracts/org, Data Act, language | 05, 01 §5–9 |

Agents B and C must also build the **product-claim truth table** (every marketing claim mapped to code). Agent D
must trace **every** charge path to a fiscal invoice. After the agents finish, independently re-verify the 2–3 most
severe claims yourself (e.g. curl, read the cited lines) before reporting them.

Every agent prompt must contain:
- `STRICTLY READ-ONLY … do not print secret values`;
- "read the project memory file / prior report FIRST, report only NEW issues or corrections";
- "honest severities; cite file:line + act/article; coverage ledger with ✅ or finding #; mark anything unchecked";
- "take as much time as needed".

## Step 3 — Cross-consistency matrix (do this yourself after agents return)
Most real findings are contradictions. For each fact, compare every place it is stated:

| Fact | Privacy policy | Terms | Website/FAQ | App UI | Emails | Code/config | Invoices | Payment provider |
|---|---|---|---|---|---|---|---|---|
| Trial length / card needed / auto-convert | | | | | | | | |
| Price, VAT incl/excl, per-seat, proration | | | | | | | | |
| Cancellation & refund | | | | | | | | |
| Retention after trial/cancel/deletion | | | | | | | | |
| Email verification / account creation process | | | | | | | | |
| Processors & regions | | | | | | | | |
| Newsletter / marketing | | | | | | | | |
| Company identity & contacts | | | | | | | | |
| Standards, rule versions & methodology claimed | | | | | | | | |

Any mismatch is a finding (GDPR Art 5(1)(a)/13; ZZP misleading practice čl. 35–37; ZOO čl. 295).

## Step 4 — Adversarial "what did we miss" pass
Run through the master list below. For each line, answer "checked / N/A / finding #". Anything unanswered → go
look. If anything new is found, repeat Step 4 once more.

### Master list (beyond playbook §A–K)
**People & data**
- Invitations to third parties: what is sent, Art 14 notice, retention of unaccepted invites
- Admin/ops notification emails containing user PII (sign-up alerts, feedback), and the mailboxes they reach
- Personal emails/phones of staff in config, seeds, fixtures, docs; real customer data in tests/demo generators
- Staging using production data; backups readable by whom; logs readable by whom (incl. bearer tokens)
- AI assistants or agents given production logs/DB access (= disclosure to a processor → DPA, zero-retention, policy mention)
- Removed team members, ex-employees, deleted companies: what remains
- Trial-abuse hashes and other "forever" data; suppression lists
- Cold-mail recipient selection: legal-form allow-list (trgovac pojedinac/obrt = natural person), freemail targeting, LIA on file
- Suppression shared across every sender of the same controller, checked at send time, not erasable by admin tools
- Stale contact data and mailing frequency vs what the Art 14 notice says
- IDOR / cross-tenant access; enumeration in auth endpoints; public endpoints returning PII

**Money**
- Every charge path produces a fiscalized invoice: first charge, renewals, proration/seat changes, trial carry-over, coupons, 100 % discounts (zero invoices), parked/failed issuance
- Refund/chargeback → storno; payment-provider receipts vs Zakon o fiskalizaciji čl. 29; invoice delivery and 11-year retention survives every deletion path
- What the customer is shown (site, app, hosted checkout) vs what is charged vs what is invoiced

**Content & claims**
- Outdated legal statements in blog posts or docs (law changes since publication)
- Competitor comparisons: dated, sourced, accurate prices, no denigration or logos
- Structured data (JSON-LD ratings, reviews, offers), OG text, llms.txt claims
- Health/safety claims, guarantees, savings promises, "certified/official" wording
- AI-generated text/images published to inform the public (AI Act Art 50(4) unless human editorial responsibility documented)
- Testimonials, client logos, case studies: real, consented, disclosed incentives
- Track-record/experience claims vs founding date; portfolio metrics vs the product's real capabilities
- Blog posts offering "legal review" (reserved legal assistance); stale funding programmes; transition-period misreadings
- Hosted form backends: vendor location, retention, sub-processors vs the notice
- Internal notes that record known law changes or corrections: check the published content was actually updated
- Every "we collect nothing / no cookies" claim (pages, llms.txt, manifest, docs) vs `git log -S` for trackers added later
- Content/media sites: "elektronička publikacija" registration and impresum with responsible editor (Zakon o elektroničkim medijima; VERIFY current act)
- llms.txt / llms-full.txt / robots.txt licensing stance consistent (TDM opt-out machine-readable)

**Product**
- In-app and in-export disclaimers, methodology version, known limitations, bug-notification process (PLD from 9 Dec 2026)
- Sector-rule currency (new laws in force, an upcoming regulation replacing the implemented one)
- Exports (portability, Data Act), deletion, rectification incl. email change

**Live / deployed state** (code review alone misses these — do read-only probes)
- `curl -I http://<every host>`: plain-HTTP served without redirect? HSTS, CSP, X-Frame-Options present on every host?
- Static-site publish directory: is the whole repo served (internal docs, strategy notes, `.md`, `package.json`, `/docs`)? Probe a few known internal paths for 200.
- `dig` every subdomain (`blog.`, `stage.`, `admin.`, `www.`) → undocumented apps, shared IPs, staging exposure.
- MX/SPF/DMARC of every domain → hidden processors (hosted mail, e-mail routing) and spoofing risk.
- Public CMS endpoints (`/wp-json/wp/v2/users`, login pages, open comments).
- Public API docs (`/docs`, `/redoc`, `/openapi.json`) on admin/back-office APIs.
- **Re-audit after fixes:** probe on PROD every function the published legal texts promise (withdrawal page/endpoint, unsubscribe, sign-up opt-out, order button). The site often deploys before the app/API.
- Serverless/edge request logs (Cloudflare Workers `observability`, Vercel, Netlify): do URLs/query strings carry user data? Retention? Compare with "nothing is stored" claims.
- `curl -I http://` returns 200 instead of 301 even when HSTS is configured in the app (HSTS over HTTP is ignored); check hstspreload status.
- Public proxy endpoints: input bounds, fan-out to upstream, rate limiting.
- Upstream data APIs: attribution / commercial-use clauses in each provider's API terms.
- Search terms or identifiers placed in page URLs on pages that run analytics (`page_location` leak).
- Served HTML of legal pages: CDN email obfuscation ("[email protected]") hiding the mandatory contact email.

**Product-claim truth table** (marketing vs code)
- For each feature claim on the site, blog, brochure, manifest or llms.txt, find the code that implements it. Unimplemented features are claimed surprisingly often (file formats, calculation methods, integrations, standard editions).
- Check that the standard *edition* claimed matches the formulas actually implemented.
- Check that global CTAs and templates ("automates everything above") don't over-claim on every page.
- Check that trial limits (seats, features) match "bez ograničenja" wording.

**Account & billing edge flows**
- Ownership transfer: who keeps paying, and who sees whose billing data?
- Seat/plan change: immediate charge without preview or consent?
- Export after churn: paywalled while the UI promises the data is "saved"?
- Payment-provider customer e-mail after people leave.
- Fiscalization retry/outage window, unmatched webhooks, refunds/disputes → storno, portal invoice history showing non-fiscal invoices.
- Invoice line content (period, quantity, unit price) and 0 % wording.

**Ads, sponsorship & data sources**
- Map every featured/"special offer"/partner tile to billing or own-company records; each needs an "Oglas"/"Naš projekt" label; check "independent / not affiliated" wording
- Ad-platform consent (CMP) status and analytics consent-mode defaults; mobile analytics SDK defaults and advertising-ID permission
- Cold outreach lists: legal form of each recipient, opt-out footer, suppression and send log

**Organisation**
- DPAs filed, ROPA, TIAs, breach register, incident plan, DSAR process
- HAKOM DSA notification; PU business premises / internal act; AMS eRačun address
- Contractor IP assignments; trademark; domain registrant; insurance (PI/tech E&O, product liability)
- Licence notices for shipped frontend code; fonts/images licences

## Step 5 — Deliver
1. Findings merged and deduplicated; severities re-checked by you (agents tend to inflate or deflate). Areas with no
   findings are reported as compliant, with evidence.
2. Write the report in the playbook format (`00-audit-playbook.md` Phase 3): it starts with the PREDLOŽAK/TEMPLATE
   line and ends with the one-line disclaimer.
3. Give the user a short summary: counts by severity, the top items, and decisions needed from them.
4. Offer to update the project memory file `.claude/croatia/legal-compliance.md` (facts, decisions, accepted risks,
   open findings, new project-specific checks). Never edit this skill's own files.

---

## Subagent prompt templates

Fill `{PROJECT}`, `{SKILL}` (= this skill's directory), `{PRIOR}` (memory file / earlier report paths), `{FACTS}`
(legal form, B2C?), `{WAIVERS}` (accepted risks from the memory file).

**Common header (prepend to each):**
```
STRICTLY READ-ONLY legal-compliance audit. Do NOT modify, create or delete any file anywhere. Do not print secret values.
Project: {PROJECT}. Facts: {FACTS}. Do NOT report these accepted risks: {WAIVERS}.
Legal knowledge base (read the relevant parts before judging): {SKILL}/SKILL.md and the references named below.
Already known (read FIRST; report only NEW issues or corrections): {PRIOR}.
OUTPUT: (a) NEW findings table: # | Severity | Finding with file:line | Law (act + article) | Concrete fix;
(b) corrections to prior items; (c) coverage ledger of everything checked (✅ or finding #; mark unchecked).
Take as much time as needed. Honest severities.
```

**A — backend data lifecycle** (refs 00, 01, 05 §14): enumerate every migration and entity → PII column table with
purpose / basis / deletion path; every endpoint returning or accepting PII → authorization and IDOR checks, public
leaks; every scheduled job; every email sender (recipient, PII, transactional vs marketing); admin console powers and
audit trail; logging and masking paths and log readers; backups and staging; every outbound third-party call and the
data sent; Art 32 items (password policy, token hashing, sessions, CORS/CSRF/headers, actuator/swagger, upload
parsing, rate limiting, enumeration, reset and magic-link flows, OAuth linking, vulnerable dependency versions); DSR
coverage (access, export, rectification incl. email, erasure, restriction, objection, invited and removed members).

**B — app UI & flows** (refs 03, 02, 01, 05): read all i18n files in every locale; walk every route; legal links,
consent capture, pre-payment information, cancellation ease, seat changes and charging disclosure, invitation and
removal flows, deletion UX; export and report templates (disclaimer, version, standards, identity); client storage and
every external request; accessibility blockers; language; OSS licences of production deps; in-app calculation
disclaimers; DSA reporting and contact; metadata and public files.

**C — website & content** (refs 05 §8–12, 02 §5, 03, 01): every page line by line (claims, pricing, FAQ vs reality,
contacts, JSON-LD, OG, llms.txt, footer); **every** blog post and doc (competitor comparisons, outdated law,
professional advice without disclaimer, copyright, personal data, fake testimonials, health and safety claims);
forms; all third-party URLs; hosting headers, robots, sitemap; accessibility and language; marketing PDFs.

**D — billing & tax** (refs 04, 03 §1.2 and §7): invoice payload vs ZPDV čl. 79 and ZoF čl. 7; exemption and
reverse-charge wording; timing, outages and parked invoices; every charge path fiscalized (proration, trial
carry-over, coupons, zero amounts); storno for refunds and chargebacks; numbering, premises, operator; eRačun, AMS
and e-reporting; VAT logic (B2B/B2C detection, VIES, EU threshold, location evidence, non-EU); gross vs net; payment-provider
receipts; invoice delivery and retention across deletion paths; dunning, coupons, price changes, refunds; PCI, SCA,
webhook signatures, idempotency; questions for the accountant.

**E — cross-cutting** (refs 05, 01 §5–9): a complete sub-processor table (vendor, data, region, mechanism, DPA
status); OSS licences across all repos (frontend distribution vs server-side); DSA; AI Act (incl. AI-written public
content); PLD readiness (versioning, validation tests, bug notification); sector-regulation currency; infra security
(TLS/HSTS, CSP, staging, CI, scanning, security.txt, incident doc); contracts and organisation (DPAs, ROPA, IP
assignments, trademark, domains, insurance, AI assistants with prod access); Data Act export; EAA thresholds;
language.
