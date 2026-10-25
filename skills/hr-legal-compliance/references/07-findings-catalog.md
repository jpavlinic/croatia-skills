# Findings catalog: recurring compliance problems in software products

A library of **anonymous, generic patterns** that show up again and again when Croatian / EU software products,
SaaS apps and websites are audited. Before an audit, skim it and search the new project for each pattern that fits
its type. Not every pattern applies to every product, and finding none is a valid result.

Entry shape: **Pattern** — *Why it's a problem* (act + article) · *Where to look* · *Fix*.

Severity is not fixed here: rate each finding in context (see `00-audit-playbook.md`, Phase 3).

---

## A. Data protection (GDPR / ZPDZ)

- **Privacy policy omits processors that the infrastructure reveals.** Why: GDPR Art 13(1)(e)–(f), 28. Look: DNS
  MX/SPF (hosted mail providers, e-mail routing), proxy/CDN response headers, error-tracking DSN hosts, CI services,
  AI assistants or agents with access to production logs. Fix: build the processor table from code + DNS + headers,
  not from memory; name the region and transfer mechanism for each.
- **"Anonymous" or "irreversible" claims that are not true.** Why: Art 5(1)(a), 13. Look: policy wording about
  analytics ("anonimna analitika") or hashing. Fix: describe cookie-based analytics as pseudonymous tracking; an
  unsalted hash of an e-mail address is reversible by dictionary attack, so do not call it anonymous.
- **"Forever" anti-abuse data.** Why: Art 5(1)(e). Look: hash tables with no purge (trial-abuse lists),
  unbounded suppression or block lists. Fix: a finite period with an LIA, keyed HMAC instead of a plain hash.
- **Account deletion blocked by an invoice foreign key.** Why: Art 17 vs the duty to keep invoices (ZoR čl. 10).
  Look: `invoices.customer_id REFERENCES …` without `ON DELETE`; every other path that deletes an account or company.
  Fix: snapshot the buyer data on the invoice row, then
  `SET NULL` / anonymise the link.
- **Deletion does not touch the payment provider or other processors.** Why: Art 17, 19; charging a deleted user is
  also unjust enrichment. Look: delete-account code with no subscription cancel / customer clean-up at the payment
  provider, no removal from the e-mail service. Fix: cancel and anonymise in the same flow; notify processors.
- **Billing contact frozen at the first account holder.** Why: Art 5(1)(d), 17. Look: payment-provider customer
  created once and never updated. Fix: sync on ownership transfer or member removal.
- **Ownership transfer leaves the previous holder's card and billing data.** Why: Art 5(1)(f), 6; ZZP čl. 51 (no
  payment without express consent). Look: transfer implemented as a role swap only. Fix: detach the payment method,
  update the customer, ask the new holder for payment details.
- **Unverified sign-up + silent OAuth auto-linking = account takeover.** Why: Art 32. Look: accounts marked verified
  at registration, plus "link the social identity if the e-mail already exists". Fix: link only verified accounts, or
  reset password and sessions when linking.
- **Anonymous submissions auto-linked to an account by e-mail.** Why: Art 5(1)(f), 25, 32. Look: registration that
  attaches earlier form submissions with the same contact e-mail before the address is verified. Fix: link only after
  a real verification click, or via a token in the submission's own confirmation e-mail.
- **Account enumeration.** Why: Art 32. Look: "user not found / already exists" on reset, magic link, resend,
  register, invite. Fix: generic responses plus throttling.
- **Rate limiter keyed on the proxy IP or on a client-supplied header.** Why: Art 32. Look: remote-address lookups
  behind a reverse proxy without trusted forwarded-header config. Fix: trusted real-IP resolution and per-route
  limits.
- **Staging shares production database, users or admin secrets.** Why: Art 25, 32. Look: identical credentials
  across profiles (compare hashes, never print values), same host, admin tokens without an environment claim. Fix:
  separate roles and secrets; gate staging.
- **Third parties' personal data in the repository.** Why: Art 5(1)(b),(c),(f); possibly copyright. Look: real
  customer documents used as test fixtures, committed log files, API-client collections with real payloads. Fix:
  remove (history too), anonymise fixtures, get permission.
- **Checksum-valid OIB with a realistic name/address in mock-ups or fixtures.** Why: Art 5(1)(c),(f) if it is real
  (about 1 in 11 random 11-digit numbers passes the OIB checksum). Look: design files, tests, seeds. Fix: use an
  obviously fictitious example marked as such (validate with `croatia:hr-identifiers`).
- **Production logs or databases available to an AI assistant.** Why: Art 28, 44–46. Look: project instructions or
  tool configs giving an assistant log or DB access. Fix: commercial terms with a DPA, list it as a processor,
  minimise and mask.
- **"Nothing leaves your browser / nothing is stored" contradicted by edge or request logs.** Why: Art 5(1)(a),(c),
  13, 25(2). Look: client-side tools whose API calls carry user input in the query string; serverless/edge platforms
  with request or invocation logging enabled (URL + IP retained for days). Fix: move user data out of URLs, switch
  off or shorten request logs, and word claims precisely ("form data is not stored").
- **"We collect nothing / no cookies" claims contradicted by a tracker added later.** Why: Art 5(1)(a), 13; ZEK
  čl. 43(4); ZZP čl. 35 / Zakon o nedopuštenom oglašavanju čl. 5. Look: `git log -S` for analytics snippets, then grep
  the copy (pages, FAQ, llms.txt, docs) for "ne prikupljamo", "bez kolačića". Fix: remove the tracker, or add consent
  and correct every claim.
- **Brand-only "controller" with no identity or contact.** Why: Art 12(2), 13(1)(a)–(b); ZET čl. 6. Look: "Voditelj
  obrade je <brand>" without OIB/address/e-mail; contact domain without MX. Fix: impresum/contact page and a working
  mailbox.
- **Invitation e-mails to third parties without an Art 14 notice, or with unescaped tenant text.** Why: Art 14, 32.
  Look: invite templates; workspace names inserted raw into HTML. Fix: short notice footer; HTML-escape.
- **Expired invitations, tokens or unconfirmed sign-ups never purged.** Why: Art 5(1)(e). Look: clean-up jobs that
  skip some token types. Fix: include them in the retention job.
- **Unsubscribing a never-confirmed double-opt-in sign-up moves it into long retention.** Why: Art 5(1)(c),(e),
  13(2)(a). Look: unsubscribe/complaint handlers that set a status regardless of confirmation; purge jobs keyed on
  status. Fix: if never confirmed, delete the record and keep only a suppression entry.
- **Production retention config differs from the documented retention; purge job off by default.** Why: Art 5(1)(e),
  13(2)(a). Look: `*_RETENTION_DAYS` in the production profile vs policy text; job toggles that default to off;
  tables storing rendered e-mail bodies forever. Fix: align code and policy; ask the user for the live state.
- **Permanent login credential in URLs.** Why: Art 5(1)(f), 25, 32. Look: `?key=` / `?token=` in e-mail templates,
  keys stored unhashed, keys visible in edge logs. Fix: one-time login tokens or URL fragments, HMAC at rest,
  rotation.
- **Ops alerts with users' personal data sent to a personal mailbox.** Why: Art 13(1)(e), 28, 32. Look: alert
  recipients on consumer mail domains; alert bodies containing addresses or payloads. Fix: a company mailbox under a
  DPA, minimised alert content.
- **Precise location logged "for statistics".** Why: Art 5(1)(c), 25. Look: INFO logs with latitude/longitude,
  high-accuracy geolocation requests. Fix: log only the derived area; round on the client.
- **Search terms or identifiers in page URLs on pages that run analytics.** Why: Art 5(1)(c), 25; ZEK čl. 43(4).
  Look: `?q=`, `?address=` on routes where the analytics tag records the full page URL. Fix: remove analytics or
  redact the query before it is sent.
- **Stale supervisory-authority address in policies.** Why: Art 13(2)(d) accuracy. Look: grep the AZOP address in
  every policy; compare with azop.hr/kontakt. Fix: update all copies.

## B. Cookies, trackers and contacting people (ZEK)

- **Analytics and font CDNs on every page with no consent banner.** Why: ZEK čl. 43(4); GDPR Art 6 (LG München I,
  3 O 17493/20, for fonts). Look: analytics tags and font CDN links in HTML **and in build templates** (blog
  generators, static-site layouts). Fix: remove analytics (then no banner is needed) or gate it behind consent;
  self-host fonts.
- **Policy describes a consent banner that does not exist, or tags fire before the choice.** Why: GDPR Art 5(1)(a),
  13; ZEK čl. 43(4). Look: policy text vs code; consent-mode defaults; ad-platform consent dashboards. Fix: make the
  policy true: a working CMP with defaults set to "denied" before the choice.
- **Mobile SDK analytics auto-collect, advertising ID declared, policy says "no tracking".** Why: ZEK čl. 43(4);
  GDPR Art 5(1)(a). Look: SDK initialisation at import time, default collection flags, ad-ID permission in the
  manifest. Fix: collection off by default, in-app consent, remove the ad-ID permission if unused.
- **Third-party sign-in SDK loaded on page open.** Why: ZEK čl. 43(4) (grey), GDPR Art 13. Look: identity-provider
  scripts injected on mount for every visitor. Fix: load on click.
- **Lifecycle and trial e-mails with discounts or "upgrade now" CTAs and no opt-out.** Why: ZEK čl. 50(2)–(3); CJEU
  C-654/23 *Inteligo Media*. Look: every scheduler-sent mail; only a global on/off switch; no `List-Unsubscribe`.
  Fix: soft opt-in offered at sign-up, a per-user flag checked at send time, one-click unsubscribe.
- **Cross-selling the operator's other paid services to users of a free platform.** Why: ZEK čl. 50(2) fails (no
  sale, product not "similar", no opt-out at collection); ZET čl. 7. Look: schedulers mailing registrants offers
  through the transactional sender. Fix: pause; unticked opt-in or legal persons only; identity footer, unsubscribe,
  suppression check.
- **Form backend outside the EEA described as "EEA only".** Why: GDPR Art 13(1)(f), 44–46, 5(1)(e). Look: form
  endpoints of hosted form services in HTML; read the vendor's privacy page for location, sub-processors and
  retention. Fix: name the vendor and mechanism; purge on schedule or switch to an EU backend.
- **Privacy notice unlinked or hidden while the site collects data.** Why: Art 12–13 (information at collection).
  Fix: footer link on every page and a short notice at each form.
- **Cold B2B e-mail with no legal-form filter.** Why: ZEK čl. 50(4) exempts only legal persons; registers also hold
  natural-person traders (obrtnici, trgovci pojedinci), for whom čl. 50(1) consent applies; fines under čl. 170. Look:
  recipient-selection logic ignores the legal form. Fix: allow-list of legal-person forms (d.o.o.,
  j.d.o.o., d.d., j.t.d., k.d., zadruga, ustanova…); unknown form = excluded.
- **No LIA / ROPA for a cold-mail campaign; personal (freemail) addresses targeted.** Why: GDPR Art 5(2), 6(1)(f),
  14, 30. Fix: documented LIA, Art 14 notice in the first mail, exclude personal addresses.
- **Objection not shared across all senders of the same controller, not checked at send time, or erasable by an
  admin "reset".** Why: GDPR Art 21(3), 5(2); ZEK čl. 50(3). Fix: one suppression list (address-based) checked by
  every sender at send time; never delete unsubscribed/complained records.
- **Mailing frequency higher than the notice describes.** Why: Art 6(1)(f) balancing, 5(1)(a). Fix: cap the number
  of mailings and say so.
- **Unsubscribe proxy reports success when the upstream call failed.** Why: ZEK čl. 50(3); GDPR Art 21(3). Look:
  backend-for-frontend routes that never check the upstream status. Fix: propagate errors; retry.
- **E-mail event pipeline (bounces/complaints) disabled in production while sending is on.** Why: GDPR Art 5(1)(a),
  21(3); ZEK čl. 50(3). Look: provider configuration-set / webhook settings in the production environment vs the
  "sending enabled" flag. Fix: make the event pipeline a go-live gate.
- **Unsubscribe or landing pages of a campaign loading third-party fonts/trackers.** Why: GDPR Art 6; ZEK čl. 43(4).
  Fix: self-host.

## C. Consumer and contract law (ZZP, ZOO, ZET)

- **Consumers can buy, but there are no consumer mechanics.** Why: ZZP čl. 7, 60, 74, 76, 81.a. Look: target groups
  such as "students" or "private persons", optional company field, net "+ PDV" prices, no withdrawal function. Fix:
  either implement consumer mechanics or genuinely exclude consumers (mandatory business ID, matching marketing).
- **Free service run by a company with no impresum and no privacy policy.** Why: ZET čl. 6 (applies to free,
  commercially motivated services too), ZTD čl. 21(4)–(5), GDPR Art 13. Look: footer, about page, JSON-LD
  `legalName`, public registers. Fix: impresum + policy.
- **Terms contradict the product.** Why: ZOO čl. 295–296; ZZP čl. 35. Look: terms promising steps the code does not
  do (manual approval, e-mail confirmation), VAT treatment, pricing unit (per user vs per seat). Fix: one canonical
  statement per fact; align code and texts.
- **Terms ban redistributing the very output the product is sold to produce.** Why: ZOO čl. 296 (defeats the purpose
  of the contract). Fix: narrow the restriction to the software itself.
- **Blanket "the software is not liable for results" in exports or UI.** Why: ZOO čl. 345(1); ZOO čl. 1079 from
  9 Dec 2026 (product liability cannot be excluded); ZZP čl. 54. Fix: a statement of roles plus a version /
  methodology footer (see `03` §6).
- **Plan or seat change charges immediately with no preview or confirmation.** Why: ZZP čl. 51, 60(5)–(6). Look:
  "always invoice" proration behind a single button. Fix: price preview and explicit confirmation.
- **Free-trial promise stated unconditionally while the code limits it.** Why: ZZP čl. 35–36. Look: trial limited to
  one per e-mail, single seat, or switchable off. Fix: state the conditions where the promise is made.
- **Legally required confirmation behind a global send cap with no retry.** Why: ZZP čl. 76, čl. 81.a(6) (no-grace
  offence). Look: order or withdrawal confirmation guarded by "N mails per hour" counters; failures only logged; UI
  says "sent" regardless. Fix: exempt the account holder's own address, add a re-drive job, honest UI status.
- **Phone number missing from consumer pre-contract information.** Why: ZZP čl. 60(1) t. 2 (phone and e-mail are
  both mandatory). Fix: publish a business number.
- **Website legal texts deployed before the backend that implements them.** Why: ZZP čl. 81.a; GDPR Art 5(1)(a), 13.
  Look: probe on PRODUCTION every function the new texts promise (withdrawal page, unsubscribe endpoint, sign-up
  opt-out). Fix: deploy order backend → app → website, re-probe after each step.
- **Paid B2B subscription sold by e-mail with no terms and no record of the accepted offer.** Why: ZOO čl. 247–255,
  295–296. Fix: short B2B terms referenced in every offer, stored acceptance, price-history table, notice before
  switch-off.
- **Content says X is not taxable / not reportable, code treats it the opposite way (or vice versa).** Why: ZZP
  čl. 35; ZOO čl. 1045. Fix: one source of truth; test.

## D. Tax and fiscalization

(Legal "what" here; implementation detail lives in `croatia:hr-fiscalization-dev`.)

- **Short fiscalization outage → paid invoice never issued.** Why: Zakon o fiskalizaciji čl. 21, 72. Look: fixed
  retry count with a short delay, no re-drive job or alert. Fix: durable queue, retry within 2 working days, alert.
- **No storno for refunds, disputes or credits.** Why: Zakon o fiskalizaciji čl. 24. Look: webhook handlers lack
  refund, dispute and credit-note events. Fix: fiscalized storno / credit note for each.
- **Payment-provider portal or e-mails show their own non-fiscal invoices or receipts.** Why: Zakon o fiskalizaciji
  čl. 29, 71. Look: hosted customer portal defaults, dunning e-mails, hosted invoice links. Fix: disable or relabel
  them; send your own fiscalized invoice.
- **Gross price charged to 0 %-VAT customers.** Why: ZET čl. 6(2); ZZP čl. 35. Look: VAT-inclusive price objects
  combined with reverse-charge or export branches in the backend. Fix: net pricing for B2B / non-EU, or adjust the
  amount.
- **EU consumers blocked or "parked" instead of taxed in Croatia under €10,000.** Why: ZPDV čl. 26a; geo-blocking
  Reg. 2018/302 Art 4. Look: tax resolver that throws for EU B2C. Fix: Croatian VAT below the threshold, OSS above.
- **Reverse charge without VIES validation.** Why: ZPDV čl. 17(1), 79. Look: "any tax ID → 0 %". Fix: VIES check,
  store the consultation result.
- **Wrong 0 % wording, invoice lines without period/quantity/unit price, single piece of location evidence.** Why:
  ZPDV čl. 79, 17; Reg. 282/2011 čl. 24a–24f. Fix: correct legal note per case; complete line data; two pieces of
  evidence.
- **Clearing customer details wipes the billing identity, so later renewals fail.** Why: Zakon o fiskalizaciji;
  ZPDV čl. 79. Look: "remove my details" flows that clear the payment-provider customer the invoice reader depends
  on. Fix: read the buyer from the invoice's own snapshot.
- **Stale tax ID on a reused customer turns a consumer into a B2B buyer.** Why: ZPDV čl. 79; ZZP. Fix: clear tax IDs
  on consumer checkout.
- **Confirmation promises "invoice sent by e-mail" with no code doing it.** Why: ZZP čl. 76; Zakon o fiskalizaciji
  čl. 29. Fix: say where the invoice is available and add "Ova poruka nije račun."
- **Surcharge for a payment method.** Why: Zakon o platnom prometu čl. 32(5) (a total ban, also for B2B cards;
  VERIFY numbering against the consolidated text). Fix: offer a discount instead, disclosed before payment.

## E. Website, content and claims

- **Static host publishes the whole repository.** Why: trade secrets; internal notes become evidence (Zakon o
  nedopuštenom oglašavanju čl. 10). Look: publish directory set to the repo root; probe `/README.md`, `/docs/`,
  internal notes. Fix: publish only the build folder, or add deny rules.
- **Marketing claims a feature the code does not implement.** Why: Zakon o nedopuštenom oglašavanju čl. 5–6; ZZP
  čl. 35. Look: map every claim (file formats, methods, standard editions, integrations) to code. Fix: implement or
  remove.
- **Unprovable statistics** ("0 % error", "95 % faster", average-result badges, hard-coded counters). Why: Zakon o
  nedopuštenom oglašavanju čl. 5, 10 (reversed burden of proof); ZZP čl. 35–36. Fix: substantiate with dated evidence,
  use live numbers, or remove.
- **Claimed standard edition differs from the implemented one.** Why: same as above. Fix: state the edition actually
  implemented.
- **Global CTA template over-claims on every page** ("automates everything above"). Fix: page-specific wording.
- **Results labelled as an official document that only an authorised person or body can issue.** Why: ZZP čl. 35;
  Zakon o nedopuštenom oglašavanju čl. 5. Fix: rename ("izračun", not "certifikat") plus a clear "this is not…" line.
- **Trust words that the process does not support** ("provjerene", "ovlaštene", "licencirane", "certificiran",
  "službeni"). Why: ZZP čl. 35–36; Zakon o nedopuštenom oglašavanju čl. 5. Look: grep copy, data, meta, JSON-LD,
  llms.txt, blog templates; compare with the actual vetting code. Fix: describe the real check.
- **Track-record claims by a newly founded business; portfolio metrics the product cannot produce.** Why: Zakon o
  nedopuštenom oglašavanju čl. 5, 10. Fix: remove or substantiate.
- **Outdated legal statements in older posts after a law changed.** Why: ZZP čl. 35 (if commercial); reputational.
  Look: posts about tax, consumer, fiscalization, AI, accessibility. Fix: update with the article and date, or mark the post as historical.
- **Posts that contradict each other or the product's single source of truth.** Why: ZZP čl. 35; Zakon o
  nedopuštenom oglašavanju čl. 5. Fix: one canonical statement per rule, linked from the rest.
- **Misread transition periods** (e.g. EAA "existing services until 2030" applies only to certain products and
  contracts; NIS2 "all cloud providers regardless of size"; eRačun "optional"). Fix: re-check against the act.
- **Systematically backdated publication dates.** Why: ZZP čl. 35 (minor). Look: `datePublished`, RSS. Fix: honest
  dates.
- **Third-party logos or app-store icons used as "supported" badges without a non-affiliation note.** Why: EUTMR
  Art 14(1)(c); ZASP. Fix: text badges or press-kit assets plus "nije povezano s …".
- **Comparison pages** are generally fine when dated ("pristupljeno"), sourced, non-denigrating and logo-free; the
  usual problems are misstated *own* features and unsourced inferences about competitors (Zakon o nedopuštenom
  oglašavanju čl. 6).
- **Paid or own-product placements unlabelled while the site claims independence.** Why: ZET čl. 7; ZZP
  čl. 36 and blacklist čl. 37 t. 16. Look: featured/deal tiles vs billing data; unused `is_sponsored` flags. Fix:
  "Oglas" / "Naš projekt" labels.
- **Agency or freelancer copy promising an unconditional transfer of all IP.** Why: ZASP čl. 96(3), 100(6); pre-contract
  statements under ZOO. Fix: payment condition plus carve-outs for pre-existing and open-source components.
- **A non-law business advertising "legal review" of contracts.** Why: reserved legal assistance under the Zakon o
  odvjetništvu (VERIFY scope). Fix: rephrase as technical review.
- **AI-written posts on public-interest topics with no named editor, or inventing first-person credentials.** Why:
  AI Act Art 50(4) (exemption needs human review and editorial responsibility); ZZP čl. 35. Fix: named editor and a
  review log, or a label; never invent credentials.
- **AI disclosure only in page footers, not inside standalone public media.** Why: AI Act Art 50(4) (light
  disclosure for evidently creative works, but it must travel with the content). Fix: end card, caption, metadata.
- **AI-licensing stance contradicts itself** (llms.txt says "no reproduction" while robots allow all AI crawlers and
  a full-text file is published). Why: ZASP čl. 188(5) (TDM opt-out must be machine-readable). Fix: one consistent,
  machine-readable stance.
- **Content site never registered as an "elektronička publikacija".** Why: Zakon o elektroničkim medijima (NN
  111/21, 114/22) — registration and impresum with a responsible editor for editorial portals; regulator now
  "Agencija za medije" (VERIFY applicability to small blogs and the current act after the EMFA implementation). Fix:
  check with the regulator; impresum with editor.

## F. Infrastructure and live state

- **App reachable over plain HTTP; no HSTS.** Why: GDPR Art 32. Look: `curl -I http://…` (HSTS sent over HTTP is
  ignored). Fix: redirect + HSTS, consider preload.
- **Undocumented apps on production hosts or subdomains** (old CMS, staging). Why: Art 32. Look: DNS enumeration,
  public CMS user endpoints. Fix: remove or secure; document.
- **Public API docs of an admin API** (`/docs`, `/redoc`, `/openapi.json`). Why: Art 32. Fix: disable in production.
- **Static log-reader or admin tokens that bypass MFA; public admin paths.** Why: Art 32. Fix: MFA everywhere,
  network restrictions.
- **Committed secrets** (incl. token-signing keys). Why: Art 32. Look: tracked config files
  and history (never print values). Fix: rotate, not just remove or hash; history keeps the plaintext.
- **Admin session leaks over HTTP behind a TLS proxy.** Why: Art 32. Look: missing forwarded-header config,
  redirects to `http://`, cookies without `Secure`/`SameSite`, API keys accepted in query strings. Fix: proxy config,
  cookie flags, header-only keys.
- **Framework or runtime past its support window; no dependency scanning; CI skips tests.** Why: Art 32. Fix:
  upgrade plan, automated alerts.
- **Domain with no SPF / DMARC (or `p=none`).** Why: spoofing and phishing risk (Art 32). Fix: SPF, DKIM, DMARC; a
  null MX for domains that never send mail.
- **Unbounded fan-out from a public proxy endpoint to an upstream API.** Why: Art 32(1)(b). Fix: input bounds, rate
  limits.
- **CDN e-mail obfuscation hides the mandatory contact e-mail.** Why: ZET čl. 6; ZTD čl. 21. Look: obfuscated
  placeholders in the served HTML of impresum/legal pages. Fix: exclude those pages from obfuscation.
- **Third-party API terms not met** (missing attribution, non-commercial keys used commercially, keys or accounts not
  in the company's own name). Why: contract (ToS; CJEU C-30/14 *Ryanair*). Fix:
  read each provider's terms; one paid account in the company's name; required credit line.
