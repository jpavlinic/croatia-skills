# Integration architecture for Croatian fiscalization and eRačun

Status: researched 2026-10-25. Design guidance derived from the Act and specs cited in the other
references; it is engineering practice, not a legal requirement unless a source is cited.

## 1. Build vs buy

| Option | What you build | When it fits |
|---|---|---|
| **Fiscalization API / SaaS provider** (F1) | REST call with receipt data; provider signs with your certificate (uploaded) or its own model, returns JIR/ZKI/QR | small teams, web shops, SaaS billing; check where your certificate and data live |
| **Own F1 client** | XML build, ZKI, XMLDSig, SOAP client, offline queue, numbering | POS vendors, high volume, offline-first devices; budget for the XML-signature edge cases and the offline queue, not just the happy path |
| **ERP / invoicing software with built-in fiscalization** | configuration only | businesses that do not write software |
| **Information intermediary** (F2) | map invoices to HR CIUS UBL (or the provider's JSON), call its API, process status webhooks | almost everyone issuing/receiving eRačuni |
| **Own access point** (F2) | AS4, AMS/MPS, validation, PU fiscalization and eIzvještavanje | software vendors and very large issuers; certification and operations burden |

Questions to ask any provider (neutral checklist): Is it on PU's intermediary list for the
services you need? Does it fiscalize incoming and outgoing eRačuni and do eIzvještavanje under
your FiskAplikacija authorisation? API style, sandbox, webhooks, idempotency keys? Validation
against the current PU schematron? Archive duration and export (XML + PDF)? EU data residency and
ISO 27001 (Zakon čl. 59–62)? Exit plan (data export, AMS re-registration)? Pricing per document?
Name no vendor as "recommended"; compare on these criteria.

## 2. Reference architecture (F1, B2C receipts)

```
checkout/payment webhook ──► Invoice service ──► Fiscal outbox (DB table, same transaction)
                                   │                    │
                                   │                    ▼
                            number allocator      Fiscal worker ──► CIS SOAP (cis.porezna-uprava.hr:8449)
                            (lock per sequence)        │  sign XML (KMS/HSM or .p12 from secret store)
                                                       ▼
                                          receipts (JIR | pending), audit log, PDF/e-mail renderer
```

Core rules:
1. **Allocate the receipt number and compute the ZKI before the network call**, in the same DB
   transaction that creates the receipt row. The receipt exists legally even if the CIS call fails.
2. **Sequence lock per key** – `(OIB, OznPosPr)` for `OznSlijed=P`, `(OIB, OznPosPr, OznNapUr)`
   for `N`. Use `SELECT … FOR UPDATE` on a counter row or a DB sequence per key; never `MAX()+1`
   without a lock. Gaps are a breach of Zakon čl. 9(2); rolled-back transactions must not consume
   numbers (allocate inside the committing transaction).
3. **Idempotency** – one receipt per business event. Key the outbox on the payment/charge/order ID
   (e.g. Stripe `invoice.id`/`payment_intent.id`); webhook retries must find the existing receipt.
4. **Retry queue** – status `pending → fiscalized | failed_permanent`. Transient errors (timeout,
   TLS, `s006`) retry with backoff; schema/signature/cert errors (`s001`–`s005`, `s013`) need a fix
   and alert immediately. Every attempt gets a new `IdPoruke`; `NakDost=true` once the receipt was
   handed to the buyer without JIR. Hard deadline: 2 working days (Zakon čl. 21(2)) – page someone
   well before that.
5. **Never block the sale** – after a short timeout, print/send the receipt with ZKI and the
   `zki=` QR URL; deliver later (Pravilnik čl. 9(3)). Current receipts first, backlog later.
6. **Clock sync** – NTP on every server/device (Europe/Zagreb for printed time; store UTC too).
   Issue time in the future is rejected (restrictive error 177); test validation flags 6-hour
   skews (v101, v103) and issue time later than send time (v104).
7. **Audit log** – store the exact signed request XML, response XML, JIR, ZKI input fields, timestamps,
   certificate serial, app version. Immutable storage; retention per accounting rules (legal skill).
8. **Certificates** – load from a secret manager/KMS at startup, never from the repo; one
   certificate per OIB (multi-tenant SaaS: per tenant, encrypted at rest, access-logged). Monitor
   expiry 60/30/7 days. Separate demo and production certificates by environment config so a
   demo cert can never reach production.
9. **Response verification** – verify the CIS signature (fiskalcis/fiskalcistest) against the CA
   chain, not a pinned leaf; PU rotated the production cert on 8.9.2026.
10. **Rounding** – compute VAT per rate on the receipt total the way you print it; CIS tolerances
    are ±0.01 € for the total and ±0.10 € for VAT in the test validation (v166, v160/v161).

## 3. Payment providers (Stripe, PayPal, card acquirers)

- A Stripe/PayPal/acquirer receipt is **not** a fiscal receipt. Stripe states it provides no
  Croatian fiscalization (see `croatia:hr-legal-compliance` reference 04 §1.8).
- Pattern: webhook (`invoice.paid`, `checkout.session.completed`, `charge.succeeded`) → idempotent
  receipt creation → fiscalize → send your own receipt e-mail/PDF with JIR, ZKI, QR. Disable or
  re-word provider receipts that show payment details before your fiscal receipt exists, or mark
  them "OVO NIJE FISKALIZIRANI RAČUN" (Zakon čl. 29) – **VERIFY** wording with an adviser.
- Payment method: online card → `K`; bank transfer → `T` (cannot be combined with
  `OibPrimateljaRacuna`); vouchers, wallets, mixed → `O` (**VERIFY** edge cases).
- Refunds/chargebacks (`charge.refunded`, `charge.dispute.closed` lost) → new negative receipt
  (storno) referencing the original (Zakon čl. 24). For B2B eRačuni → credit note (381) via the
  intermediary.
- Subscriptions: fiscalize each paid period when it is invoiced/paid, not at signup.
- Currency: fiscal amounts are **EUR only** (Spec §2 note; HR CIUS `EUR`). If you charge in another
  currency for a Croatian-taxed sale, convert to EUR for the fiscal data per your accountant's rule
  (VAT law conversion rate) and keep the original amount for reconciliation – **VERIFY** the rate
  source (HNB/ECB) with your accountant.

## 4. Reference architecture (F2, eRačun)

```
Billing ──► UBL generator (HR CIUS) ──► validator (XSD + CEN + HR schematron)
                                            │
                                            ▼
                           Intermediary API  ──► AS4 delivery ──► buyer
                                            │        (status webhook: delivered / rejected / error)
                                            ├──► fiscalization (EvidentirajERacun, I)
                                            └──► eIzvještavanje (EvidentirajNaplatu by the 20th)
Inbound: intermediary webhook ──► store XML ──► fiscalize (U) within 5 working days ──► AP workflow
                                          └──► reject? ──► EvidentirajOdbijanje by the 20th
```

- Decide per customer at checkout: **Croatian business (OIB, in AMS)** → eRačun; consumer → F1
  receipt; EU/non-EU business → ordinary invoice (reverse charge text) with no eRačun duty. Store
  the decision and the evidence (OIB, VIES result).
- Lookup the buyer in AMS (via the intermediary) **before** issuing; if not found, follow čl. 40
  (paper/PDF + eIzvještavanje) and log the lookup result as evidence.
- Payment reporting job: match bank statements/PSP payouts to outgoing eRačuni and send
  `EvidentirajNaplatu` monthly (or continuously) – deadline the 20th for the previous month
  (Zakon čl. 53). Partial payments: one record per payment; corrections with negative amounts.
- Inbound: fiscalize every received eRačun within 5 working days even if you will dispute it;
  report rejections monthly (čl. 52) – rejection means no input VAT on that invoice.
- Keep the XML as the source of truth; render PDFs from it for humans.

## 5. Choosing F1 vs F2 for a B2B sale paid by card

Zakon čl. 39 lets a B2B sale paid in cash/card be fiscalized as an F1 receipt with
`OibPrimateljaRacuna` instead of an eRačun – then no eRačun for the same sale. Bank transfer
(`T`) cannot use this route (restrictive error 181). Product decision with legal input: see
`croatia:hr-legal-compliance` reference 04 §1.6.

## 6. Multi-tenant SaaS checklist

- Per tenant: OIB, VAT status (`USustPdv`), premises labels, device numbers, sequence mode P/N,
  certificate + password (encrypted), operator OIB mapping (internal act), intermediary
  credentials, FiskAplikacija authorisation status.
- Tenant onboarding wizard: validate OIB checksum, check premises are registered in ePorezna,
  run an echo + test receipt on cistest with the tenant's demo cert, then switch to production.
- Isolation: a bug must not be able to sign tenant A's receipt with tenant B's certificate
  (`s005` would catch OIB mismatch, but log and alert on it).
