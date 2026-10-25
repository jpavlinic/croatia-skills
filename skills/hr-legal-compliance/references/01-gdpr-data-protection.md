# Data protection law for a small Croatian software business (obrt or d.o.o.)

**Status:** researched 2026-10-05; Digital Omnibus, DPF, EDPB fining guidelines and the GDPR procedural regulation re-checked 2026-10-25. General information, not legal advice. Items marked **VERIFY** were not confirmed against a primary source, or are still changing.

**Checked directly against primary text (Oct 2026)**
- **Croatian statutes** (consolidated texts on zakon.hr, database updated 26 Sep 2026 up to NN 105/26):
  - ZPDZ (NN 42/2018), full text
  - ZEK (NN 76/22, 14/24, 45/26), Art 43(4), Art 50 and the penalty articles
  - ZOO, Arts 225–230
  - Zakon o računovodstvu (NN 85/24, 145/24, 151/25), Arts 10–11
  - OPZ, Arts 66 and 108
  - Zakon o fiskalizaciji (NN 89/25), Art 35
  - ZZP (NN 19/22, 59/23, 59/26), Art 10(7)
  - Zakon o PDV-u, Art 79
- **AZOP pages:** the fines register, the breach-reporting page, the complaint procedure, the US-transfers page, and the 2025 statistics.
- **Status of the Digital Omnibus and the EU-US DPF:** law-firm and trade sources (Sep–Oct 2026), the DataGuidance report of the CJEU order of 4 June 2026, and reports of the Council mandate of 21 Oct 2026.

**Main conclusions**
- **The GDPR has not been amended.** The data part of the Digital Omnibus (procedure 2025/0360(COD)) is still being negotiated: the Council agreed its negotiating mandate on 21 Oct 2026; the European Parliament has not adopted its position, so trilogues have not started. Only the AI-Act part was adopted, in July 2026.
- **The EU-US Data Privacy Framework is still valid** (re-checked 2026-10-25). The General Court upheld it on 3 Sep 2025 (T-553/23). Latombe's appeal (C-703/25 P) is still pending. After the US Supreme Court decided Trump v. Slaughter (29 Jun 2026), noyb announced a new challenge; whether it has been filed could not be confirmed (**VERIFY**). Keep the 2021 SCCs as a fallback for every US vendor.
- **Retention periods are not the round numbers often quoted:**
  - Accounting documents: at least **11 years** (ZoR Art 10).
  - Fiscalised eRačuni: **6 years** from the end of the year they were issued (Zakon o fiskalizaciji Art 35, NN 89/25).
  - Tax records: **10 years from the start of the limitation period** (OPZ Art 66(18)).
  - Consumer written-complaint register: **1 year** (ZZP Art 10(7)).
  - General limitation period: **5 years** (ZOO Art 225). Claims between businesses from trade contracts for goods and services: **3 years** (ZOO Art 228).
- **Marketing email under ZEK Art 50:**
  - Consumers: prior consent, except a "soft opt-in" for your own similar products or services offered to your existing customers.
  - Legal persons: the consent rule does not apply at all (Art 50(4)). Emails to a named employee are still that person's personal data under the GDPR, so you rely on legitimate interest with an opt-out.
- **Cookie and spam fines are separate from GDPR fines.** Breaching ZEK Art 43(4) or Art 50 is a misdemeanour (prekršaj) under ZEK Art 170: €13,270–132,720 for a legal person and €1,320–6,630 for a natural person such as a sole trader.

---

## 0. Legal framework and current status

| Instrument | Status as of Oct 2026 | Source |
|---|---|---|
| GDPR, Regulation (EU) 2016/679 (Opća uredba o zaštiti podataka) | In force and unamended | https://eur-lex.europa.eu/eli/reg/2016/679/oj |
| Zakon o provedbi Opće uredbe o zaštiti podataka (ZPDZ), NN 42/2018 | In force; no amendments listed | https://narodne-novine.nn.hr/clanci/sluzbeni/2018_05_42_805.html ; https://www.zakon.hr/z/1023 |
| Zakon o elektroničkim komunikacijama (ZEK), NN 76/22, 14/24, 45/26 (implements the ePrivacy Directive) | In force. Art 43(4) covers cookies, Art 50 covers unsolicited communications | https://www.zakon.hr/z/182 |
| Digital Omnibus (COM(2025) 837, proposed 19 Nov 2025) | **Not adopted.** The AI-Act part was agreed 7 May 2026 and adopted in July 2026. The data/GDPR part: about 1,840 amendments were tabled in the Parliament in August 2026; the **Council agreed its mandate on 21 Oct 2026** (incl. a legitimate-interest rule for AI processing, Art 88c / "88bis" in the Council text, and further cookie-consent exemptions). Reports differ on how far the Council text narrows the definition of personal data (**VERIFY** against the Council document). Parliament position pending; trilogues not started. EDPB-EDPS Joint Opinion 2/2026 strongly opposes a narrower definition of personal data | gdprlocal.com (22 Sep 2026); dig.watch (22 Oct 2026); noyb (23 Oct 2026); EDPB Joint Opinion 2/2026 |
| GDPR procedural regulation, Regulation (EU) 2025/2518 | In force 1 Jan 2026; **applies from 2 Apr 2027** to cross-border complaints and investigations (procedure between supervisory authorities; no new duties for a small controller beyond cooperating) | https://eur-lex.europa.eu/eli/reg/2025/2518/oj |
| Main GDPR changes proposed in the Omnibus (do not apply yet) | Art 4(1): personal data defined relative to who holds it. Art 12: refusal of abusive access requests. Art 13: information exemption for "obvious" low-risk relationships. Art 33: breach notice only for *high* risk, 96 hours, single EU portal. Art 35: one EU-wide DPIA list. New Art 88a: cookie rules moved into the GDPR, with a 6-month ban on re-asking and audience-measurement exemptions. Art 88b: browser-level privacy signals. Art 88c: legitimate interest as a basis for AI training | as above |

**In practice:** build to the current GDPR. Watch Art 33 (96 hours, high-risk threshold) and Art 88a (cookies). These would be the most useful relief for a small SaaS if they are adopted, but with trilogues only starting after the Parliament's position, the earliest they could apply is probably late 2027 or 2028 (**VERIFY**).

---

## 1. Core GDPR rules

### 1.1 Principles (Art 5) (načela)
**Rule.** Personal data must be:
- (a) processed lawfully, fairly and transparently;
- (b) collected for specified purposes only (purpose limitation);
- (c) minimised;
- (d) accurate;
- (e) kept no longer than needed (storage limitation);
- (f) kept secure (integrity and confidentiality).

Art 5(2) adds **accountability**: you must be able to *prove* compliance.

**AZOP's enforcement pattern.** AZOP combines Art 5 with other articles in almost every decision:
- **Real-estate agency, Feb 2026, €100,000.** It kept 11,887 client contracts from 2010–2019 after their purpose had ended (Art 5(1)(e)). It also held 914 copies of ID cards and bank cards without a legal basis (Art 6), and had no staff instructions (Art 32(4)).
- **Casino (Admiral), 2 Oct 2026, €2.59M.** Four fingerprints were collected where fewer would do (Art 5(1)(c)). The bundled consents were invalid. Its notices contradicted each other (Arts 12/13).

**For a SaaS.** Every table and column needs a purpose, a legal basis and a deletion rule. "We might need it later" is not a purpose.

### 1.2 Lawful bases (Art 6(1)) (pravne osnove)

| SaaS processing | Recommended basis | Notes |
|---|---|---|
| Creating an account and logging in; delivering the app; storing the user's projects | **6(1)(b) contract** (izvršenje ugovora) | Includes steps before the contract at the user's request, such as sign-up. EDPB Guidelines 2/2019: only what is *objectively necessary* for the service. |
| Free trial | 6(1)(b) | Trial terms are a contract, even an unpaid one. |
| Billing, invoices, Stripe payment data, keeping invoices | 6(1)(b) for charging; **6(1)(c) legal obligation** (pravna obveza) for issuing, fiscalising and keeping invoices | Legal sources: ZoR Art 10, Zakon o PDV-u Art 79, Zakon o fiskalizaciji, OPZ Art 66. |
| Security logs, rate limiting, fraud and abuse prevention | **6(1)(f) legitimate interest** (legitimni interes); Recital 49 names network security explicitly | Document a short legitimate-interest assessment (LIA). |
| Error monitoring (e.g. Sentry) | 6(1)(f) | Minimise personal data in payloads. |
| Product analytics *without* cookies or device access (server-side, aggregated) | 6(1)(f) | Use an LIA and offer an opt-out. |
| Analytics that use cookies, localStorage or fingerprinting (GA4, PostHog JS, etc.) | **Consent** under ZEK Art 43(4) for storing or reading on the device, then 6(1)(a) | CJEU C-673/17 Planet49: pre-ticked boxes are invalid. EDPB Guidelines 2/2023 extend this to pixels, URL tracking and local storage. |
| Transactional emails (password reset, invoices, trial-expiry and service notices) | 6(1)(b) | Not marketing; no consent needed. Keep upsell content minimal. |
| **Trial "nurture" sequence** (tips, onboarding, "upgrade now" with a discount) | Mixed: onboarding/help → 6(1)(b) or (f). **Promotional content to consumers → ZEK Art 50(1) consent, or the Art 50(2) soft opt-in** for your *own similar* services if the contact was collected "in connection with a sale" and an opt-out was offered at collection and in every message | Whether a *free* trial counts as "in the context of a sale": the CJEU appears to have accepted that a free account linked to a paid offer can qualify (C-654/23 *Inteligo Media*, 2025, **VERIFY** date and holding). Safest: an unticked marketing checkbox at sign-up, or soft opt-in with a clear opt-out shown at sign-up. |
| Marketing to B2B contacts (company addresses) | ZEK Art 50(4): the consent rule does not apply to legal persons. GDPR 6(1)(f) for named individuals' emails (ana.horvat@primjer.hr) | The opt-out and sender-identity duties still apply (Art 50(3)), as does GDPR Art 21(2)–(3): an absolute right to object to direct marketing. |
| Newsletter or blog signup | 6(1)(a) consent with double opt-in (recommended, not legally required) | Keep proof of consent: timestamp, IP, form version. |
| **Admin viewing users' projects** (support/debugging) | 6(1)(b) where the user asked for support; 6(1)(f) for security investigations | Must be disclosed in the privacy notice. Use role-based access, log every admin access, and preferably show "admin viewed your project" or require a per-ticket consent toggle. If the SaaS acts as *processor* for the content (see §5), admin access must stay within the DPA's instructions. |
| Customer support tickets | 6(1)(b)/(f) | — |
| Keeping data after an account is deleted, to defend claims | 6(1)(f) (establishing or defending legal claims), with Art 17(3)(e) | Limited to the limitation period (§10). |
| Backups | Same basis as the original data | Deleted data rolls out when the backup rotates. |

### 1.3 Legitimate-interest assessment (LIA)
**Rule.** Art 6(1)(f) uses a three-step test:
1. **Purpose:** is there a legitimate interest?
2. **Necessity:** is the processing necessary for it?
3. **Balancing:** do the user's interests or rights override yours?

Sources: CJEU C-621/22 *KNLTB* (4 Oct 2024) held that a purely commercial interest *can* be legitimate. CJEU C-252/21 *Meta v Bundeskartellamt* (2023) held that necessity is strict and reasonable expectations matter. EDPB Guidelines 1/2024 on legitimate interest (**VERIFY** whether the final version after consultation has been adopted; it is cited as authoritative in EDPB Guidelines 03/2026).

**Example LIA (security logs).** Purpose: detect and prevent unauthorised access and abuse. Necessity: IP address and user ID are needed to trace attacks, and no less intrusive alternative exists. Balancing: users expect providers to secure services; the data has low sensitivity; it is kept 90 days; access is restricted; IPs are truncated after 30 days. Outcome: the interest prevails, and users are told about their right to object under Art 21(1).

### 1.4 Consent (Art 4(11), Art 7) (privola)
**Requirements:**
- freely given, specific, informed and unambiguous, given by a clear affirmative act;
- provable (Art 7(1));
- separated from other matters (Art 7(2));
- as easy to withdraw as to give (Art 7(3));
- not a condition of the service unless necessary (Art 7(4)).

See also EDPB Guidelines 05/2020.

**AZOP enforcement.** In the casino case (Oct 2026) AZOP held that combining several purposes in one consent breaches Art 7 with Art 4(11). Consent cannot make excessive processing lawful.

**Implementation:**
- separate unticked checkboxes for each purpose;
- a `consents` table storing user_id, purpose, text version, timestamp, IP/UA, source and withdrawn_at;
- a cookie banner with "Odbij sve" (reject all) shown as prominently as "Prihvati sve" (accept all), and no analytics scripts before consent.

### 1.5 Children (Art 8 and ZPDZ Art 19)
**Rule.** Croatia sets the age at **16**. Where consent is the basis for information-society services offered directly to a child resident in Croatia, the child must be at least 16 (ZPDZ Art 19(1)–(2)). Breaching this is treated as a breach of GDPR Art 8 and fined under Art 83 (Art 19(3)).

**For a professional or B2B SaaS:** state in the Terms of Service that the service is intended for users aged 18+ or professionals, and add an age confirmation at sign-up. A final AZOP decision involving minors is published with the offender's name (ZPDZ Art 48).

---

## 2. Croatian implementing law (ZPDZ, NN 42/2018) and AZOP

### 2.1 Key ZPDZ provisions (verified against the full text)

| Article | Content |
|---|---|
| 4 | The supervisory authority is the **Agencija za zaštitu osobnih podataka (AZOP)**, an independent state body accountable to the Croatian Parliament (Sabor), based in Zagreb. |
| 6 | AZOP's powers beyond the GDPR. If AZOP doubts an adequacy decision or the SCCs, it suspends the case and refers it to the High Administrative Court (Visoki upravni sud), which may refer it to the CJEU. |
| 18 | AZOP publishes decisions on high-risk processing, anonymised or pseudonymised. |
| **19** | **A child's consent for information-society services is valid from age 16.** |
| 20 | Genetic data may not be used for life insurance; consent cannot lift this ban. |
| 21–24 | Biometrics. Private sector: only if provided by law or necessary to protect people, property, classified information or trade secrets, or for secure identification of users. For secure identification, the basis is **explicit consent** (Art 22(2)). Employees: biometric time-recording only as an *alternative* option and with explicit consent (Art 23). |
| 25–32 | **Video surveillance (videonadzor):** only to protect people and property (Art 26). Mandatory sign with a picture, the controller's identity and contact details (Art 27). Automated log of access to recordings (Art 28(4)). Recordings kept **at most 6 months** (Art 29). Workplace cameras need prior notice to employees and never cover rest rooms, toilets or changing rooms (Art 30). Residential buildings need consent of 2/3 of co-owners (Art 31). Public areas: only public bodies (Art 32). |
| 33 | Statistical purposes. |
| **34** | Anyone may file a **zahtjev za utvrđivanje povrede prava** (request to establish a breach of rights). AZOP decides by *rješenje* (an administrative act). No appeal is allowed; the remedy is an administrative lawsuit (upravni spor). |
| 35 | Deletion order: the court may postpone deletion, in which case processing is blocked meanwhile. |
| 36–40 | Inspections, announced or unannounced, with police assistance if needed. AZOP may copy storage systems, and may seal or seize equipment for up to 15 days. Records of inspection, with 15 days to object. |
| 41 | Representation by NGOs, including for Art 82 compensation claims. |
| 42–43 | AZOP gives expert opinions within 30 days (extendable by 30). Free for data subjects; **a fee for businesses and consultants asking in the course of their business**. |
| 44–46 | Fines are imposed by separate decision (odluka). Instalments are possible. Payment is due within 15 days of the decision becoming final, and is collected by the Tax Administration (Porezna uprava) if unpaid. No interest accrues. |
| **47** | **No administrative fines on public authorities** (state bodies and local or regional self-government units). Corrective powers still apply. |
| **48** | A final decision is published **with the offender's name** if it concerns minors, special categories, automated decisions or profiling, a repeat offender, or a fine of at least 100,000 HRK (about €13,272). |
| 49 | Limitation period for collecting fines follows the tax procedure rules (OPZ). |
| 51 | Video-surveillance fines up to 50,000 HRK (about €6,636) for missing signs, missing access logs or misuse of recordings. |

### 2.2 AZOP: role and complaint process
- **Contact:** Ulica Metela Ožegovića 16, 10000 Zagreb; azop@azop.hr; online form at https://azop.hr/zahtjev-za-utvrdivanje-povrede-prava/.
- **Process.** AZOP tells data subjects to write to the controller first; if there is no reply within a month, they can complain to AZOP. The complaint needs name, OIB, address, a description and supporting evidence (including correspondence with the controller). AZOP decides by *rješenje*, which can be challenged in the administrative court. The one-stop-shop applies to cross-border processing.
- **Expect** a written request from AZOP to explain your position (očitovanje). In B2 Kapital, slow replies and missing system logs counted as **aggravating factors**. Reply fully and on time.

### 2.3 AZOP fines: statistics and notable cases
Totals from the AZOP register (https://azop.hr/upravne-novcane-kazne-3/):

| Year | Number of fines | Total |
|---|---|---|
| 2020 | 1 | €145,995 |
| 2021 | 4 | €103,192 |
| 2022 | 14 | €528,369 |
| 2023 | 28 | €8,266,350 |
| 2024 | 38 | €538,200 |
| 2025 | 13 | €6,725,500 |

- In 2025 AZOP ranked 6th of 30 EEA authorities by total fines (AZOP news, 9 Apr 2026). The 2024 average was about €14k per fine, which shows that **small companies are fined routinely**.
- AZOP does not anonymise when Art 48 applies; otherwise decisions are published anonymised.

**Notable cases relevant to a SaaS:**
- **B2 Kapital d.o.o. (debt collection), May 2023, €2,265,000.**
  - The privacy policy gave the wrong legal basis (Art 13(1)).
  - **No Art 28 DPA with a processor**; 83,896 OIBs were affected.
  - Inadequate Art 32 security led to exfiltration of 77,317 records (name, date of birth, OIB).
  - Aggravating: poor cooperation, and logs not provided.
  - https://azop.hr/agenciji-za-naplatu-potrazivanja-izrecena-upravna-novcana-kazna-u-iznosu-od-226-milijuna-eura/
- **Debt collection agency, Oct 2023, €5.47M**, the highest so far: a data leak (Jutarnji, 5 Oct 2023).
- **Telecom operator, Nov 2025, €4.5M.**
  - Personal data went to a group company in Serbia with **no valid SCCs after 27 Dec 2022 and no transfer risk assessment** (Arts 44 and 46).
  - Its privacy policy said data "may" go outside the EEA; vague wording breached Arts 12(1) and 13(1)(f).
  - Employee ID copies and criminal-record certificates were collected without a basis.
  - A processor's security was **not checked in advance** (Art 28(1)).
- **Bank, Dec 2025, €1.5M** (tportal, 18 Dec 2025).
- **Real-estate agency, Feb 2026, €100,000:** storage limitation, ID and card copies, staff instructions (Arts 5(1)(e), 6 and 32(4)).
- **Casino (Admiral), Oct 2026, €2.59M:**
  - biometrics beyond what was necessary;
  - bundled consents (Art 7);
  - inconsistent notices (Arts 12 and 13).
- **Cookies, 2023:** two betting companies fined **€20,000 and €30,000** for cookies without consent (regula.consent.hr; AZOP cookie-fines page).
- **Hotel, 2024, €15,000:** breaches of Arts 6, 13, 32 and 38.
- **A processor fined directly under Art 32** (2024): processors are liable too.
- 2025 also included fines on a betting shop and a school (PDFs in the AZOP register).
- **Email marketing:** no AZOP *GDPR* fine specifically for spam was found in this research. Spam is mainly enforced as a ZEK misdemeanour (Art 170: €13,270–132,720 for a legal person, €1,320–6,630 for a natural person). The competent bodies are HAKOM and AZOP (ZEK Art 51), with proceedings in the municipal court (općinski sud) (Art 173). Prosecution is time-barred after 4 years (Art 174).

---

## 3. Transparency (Arts 12–14)

**Art 12.** Information must be concise, transparent, intelligible, easily accessible, in clear and plain language, and free of charge. See WP29/EDPB Transparency Guidelines WP260 rev.01, which support layered notices.

**Language.** The GDPR does not name a language, but "intelligible" for a Croatian audience means **Croatian**. Consumer law (ZZP) and the Zakon o hrvatskom jeziku (NN 14/2024) also push toward Croatian for consumer-facing information (**VERIFY** how far the language law reaches private websites). Offer English as a second version.

**AZOP enforcement:** vague phrases ("may transfer", "exceptionally outside the EU") and notices that contradict each other are penalised (telecom 2025, casino 2026, B2 Kapital 2023).

### Art 13 checklist (data collected from the user)

| # | Item | Article |
|---|---|---|
| 1 | Controller's identity and contact details: full legal name, OIB, registered address, email | 13(1)(a) |
| 2 | DPO contact details, if one is appointed | 13(1)(b) |
| 3 | Purposes **and** legal basis for *each* purpose | 13(1)(c) |
| 4 | The legitimate interests relied on, named specifically | 13(1)(d) |
| 5 | Recipients or categories of recipients (processors by category or by name) | 13(1)(e) |
| 6 | Transfers to third countries: whether there is an adequacy decision, or which safeguard is used and how to get a copy | 13(1)(f) |
| 7 | Retention period, or the criteria for it | 13(2)(a) |
| 8 | Rights: access, rectification, erasure, restriction, objection, portability | 13(2)(b) |
| 9 | Right to withdraw consent at any time | 13(2)(c) |
| 10 | Right to complain to AZOP | 13(2)(d) |
| 11 | Whether providing data is a statutory or contractual requirement, and the consequences of not providing it | 13(2)(e) |
| 12 | Automated decision-making or profiling: the logic involved and the consequences | 13(2)(f) |
| 13 | Further processing for a new purpose: tell users first | 13(3) |

**Art 14** (data obtained from others, e.g. a B2B customer enters their client's details into your app): the same items plus the **categories of data** and the **source**. Deadline: within a reasonable time, at most one month. Where your SaaS is a processor, this is your customer's duty, not yours.

**Art 21(4).** The right to object must be shown clearly and **separately** from other information.

**Layered approach:**
- **Layer 1:** a short notice on sign-up and newsletter forms (controller, purpose, basis, a link to the full policy, rights).
- **Layer 2:** the full privacy policy (Politika privatnosti).
- **Layer 3:** a cookie policy and a sub-processor list.

**Example short notice at sign-up (Croatian):**
> *Voditelj obrade je [Naziv d.o.o.], OIB [..]. Vaše podatke obrađujemo radi izvršenja ugovora o korištenju usluge (čl. 6. st. 1. t. b) GDPR-a). Više o obradi, rokovima čuvanja i Vašim pravima pročitajte u [Politici privatnosti].*

(In English: "The controller is [Name d.o.o.], OIB [..]. We process your data to perform the contract for use of the service (Art 6(1)(b) GDPR). Read more about processing, retention periods and your rights in our [Privacy Policy].")

---

## 4. Data subject rights (Arts 12 and 15–22)

**Deadlines and fees.** Respond without undue delay and **within 1 month** of receipt. This can be extended **by 2 more months** for complex or numerous requests, but you must tell the person about the extension, with reasons, within the first month (Art 12(3)). If you will not act, say so within one month, with the reasons and the person's right to complain and seek a court remedy (Art 12(4)). The service is **free**. A reasonable fee or refusal is possible only for manifestly unfounded or excessive requests, and you carry the burden of proof (Art 12(5)).

CJEU C-307/22 (26 Oct 2023): the first copy is free *whatever the reason* for the request. The proposed Omnibus "abuse" ground is not law.

**Identity (Art 12(6)).** Ask for extra information only where you have reasonable doubt. EDPB Guidelines 01/2022: an authenticated session or a confirmation link to the account email is usually enough. **Do not ask for ID copies by default.** AZOP repeatedly treats ID copies as excessive (real-estate 2026, telecom 2025).

| Right | Article | SaaS implementation |
|---|---|---|
| Access | 15 | Self-service "Download my data" (JSON plus a human-readable PDF/HTML). The answer must cover purposes, categories, recipients *including the actual identity of recipients if asked* (CJEU C-154/21), retention, source, and safeguards for transfers. The copy must be a faithful reproduction (C-487/21). Include exports of logs relating to the user where feasible. |
| Rectification | 16 | Editable profile, and correction of billing data on future invoices. Issued invoices cannot be changed except by credit note. |
| Erasure | 17 | "Delete account" leads to: an immediate soft-lock → a hard delete after a grace period (e.g. 30 days) → keeping invoices and the payment ledger (Art 17(3)(b) legal obligation) and a minimal claims record (Art 17(3)(e)) → backups expire on rotation, with a note that restored backups are re-purged. Notify recipients (Art 19), e.g. delete from the email service provider and analytics, and deactivate the Stripe customer. |
| Restriction | 18 | A "restricted" flag that blocks processing except storage. |
| Portability | 20 | Applies only to data based on consent or contract and processed automatically. Use a structured, machine-readable format (JSON/CSV) of the user's projects. |
| Objection | 21 | Absolute for direct marketing (unsubscribe link, plus a suppression list kept *only* to honour the opt-out). For processing based on legitimate interest you must stop unless you have compelling legitimate grounds. |
| Automated decisions | 22 | Usually not applicable. Note fraud-scoring by Stripe Radar. Art 22 applies only to decisions with legal or similarly significant effect. Mention it in the policy. See C-203/22 *Dun & Bradstreet Austria* (27 Feb 2025) on explaining the logic. |

**Process.** Use a privacy@ mailbox and a DSAR log with: date received, identity check, deadline, actions, date answered. Keep the log 3–5 years as accountability evidence (**VERIFY** that this period is proportionate for you).

---

## 5. Controller vs processor; Art 28 DPA

**Roles.** See EDPB Guidelines 07/2020.
- For account, billing, marketing and logs about *your users*, you are the **controller** (voditelj obrade).
- For **content your B2B customers upload about third parties**, you are typically a **processor** (izvršitelj obrade). Examples: names and contact details of the customer's own clients, patients, tenants or employees stored in the product. The customer decides why that data is processed; you process it only to provide the service.
- Consequence: you must **offer an Art 28 DPA** (Ugovor o obradi podataka) to your B2B customers, for example as an annex to the Terms that is accepted on sign-up.
- You stay a controller for your own uses, such as aggregated statistics, security and billing.

**Your own processors:** hosting, email, monitoring, Stripe for some functions. Stripe acts as an independent controller for fraud/AML/KYC and as a processor for some services; see the Stripe DPA (**VERIFY** the current split). AZOP fined B2 Kapital for having **no DPA**, and the telecom operator for **not checking a processor's security in advance** (Art 28(1)).

**Sub-processors (Art 28(2) and (4)).** Use a general written authorisation, a published sub-processor list, advance notice of changes (e.g. 30 days) and a right to object. Impose the same obligations on each sub-processor ("flow-down").

**Example clause (in a SaaS DPA):**
> "The Processor shall engage sub-processors listed at [URL]. The Processor shall notify the Controller of any intended addition or replacement at least 30 days in advance by email, during which the Controller may object on reasonable data-protection grounds; if no resolution is reached the Controller may terminate the affected Service and receive a pro-rata refund."

The full DPA checklist is in Annex (d).

---

## 6. Records of processing activities (ROPA) (Art 30) (evidencija aktivnosti obrade)

**Rule.** Controllers and processors must keep written (electronic is fine) records. The **exemption for fewer than 250 employees (Art 30(5)) does not apply** if the processing:
- is likely to pose a risk to rights and freedoms;
- is **not occasional**; or
- includes special categories or criminal-offence data.

A SaaS processes user data continuously, so the processing is not occasional and **the exemption does not apply**. AZOP can request the ROPA during any inspection (Art 30(4)).

**Controller fields (Art 30(1)):**
- name and contact details of the controller (and DPO);
- purposes;
- categories of data subjects and of data;
- categories of recipients;
- third-country transfers and safeguards;
- retention periods;
- general description of security measures (Art 32).

**Processor fields (Art 30(2)):**
- processor and each controller (customer);
- categories of processing performed for each controller;
- transfers;
- security measures.

See Annex (b).

---

## 7. Security (Art 32); breaches (Arts 33 and 34)

**Art 32.** Measures appropriate to the risk, for example:
- pseudonymisation and encryption;
- confidentiality, integrity, availability and resilience;
- the ability to restore data;
- regular testing;
- staff acting only on instructions (Art 32(4), cited in the real-estate fine).

**Minimum baseline for a small SaaS:**
- TLS everywhere and HSTS;
- encrypted disks and backups;
- password hashing with bcrypt, scrypt or argon2;
- MFA for admin and provider consoles;
- least-privilege roles and an admin access audit log;
- secrets in a vault, never in logs;
- dependency patching;
- restore tests of backups (e.g. quarterly);
- a written incident response plan;
- offboarding procedures;
- signed DPAs;
- confidentiality undertakings with contractors.

**Art 33 (notifying AZOP).**
- Notify **without undue delay and where feasible within 72 hours of becoming aware**, unless the breach is unlikely to result in risk. A late notification must state the reasons for the delay.
- You can notify in phases if facts are incomplete.
- **How:** use the AZOP form *Izvješće o povredi osobnih podataka* (RTF: https://azop.hr/wp-content/uploads/2025/05/izvjesce_o_povredi_osobnih_podataka.rtf). Fill in all mandatory (*) fields, sign it (and stamp if applicable), and send the scan to **incidenti@azop.hr**, with the original by post to Ulica Metela Ožegovića 16, Zagreb. Source: https://azop.hr/izvjescivanje-o-povredi-osobnih-podataka/
- **Contents (Art 33(3)):** nature of the breach, categories and approximate numbers of data subjects and records, DPO or contact point, likely consequences, measures taken or proposed.
- **Processor duty (Art 33(2)):** notify the controller without undue delay. In your DPA, commit to a fixed time such as 24–48 hours.

**Art 34 (notifying individuals)** where the risk is **high**, in clear language. Exceptions: the data was encrypted or unintelligible, the risk was mitigated, or individual notice would take disproportionate effort (use a public notice instead).

**Breach register (Art 33(5)).** Document **every** breach, even ones not notified: facts, effects, remedial action, and the reasoning for whether to notify. AZOP stresses this. See also EDPB Guidelines 9/2022.

**NIS2 note.** The Croatian cybersecurity law (Zakon o kibernetičkoj sigurnosti, NN 14/2024) applies mainly to medium and large entities in listed sectors. A micro SaaS is usually out of scope (**VERIFY** your size and sector).

---

## 8. DPIA (Art 35) and DPO (Art 37)

**DPIA (procjena učinka).** Required where processing is likely to be high-risk: systematic and extensive profiling with significant effects, large-scale special categories, or systematic monitoring of public areas (Art 35(3)). Also when two or more WP248 criteria are met, or the activity is on the AZOP list (AZOP decision on the list of processing requiring a DPIA, NN 88/2019, **VERIFY** the reference).
- A typical B2B productivity SaaS **does not need a DPIA**.
- Do one if you add: AI features processing user content at scale, biometrics, location tracking, employee monitoring features, or large-scale health data.
- Record a short "DPIA screening" note in the ROPA anyway.

**DPO (službenik za zaštitu podataka).** Mandatory only for public authorities, for core activities involving large-scale regular and systematic monitoring, or for large-scale special categories (Art 37(1)). **A small SaaS usually does not need one.** Instead, name a privacy contact (e.g. privacy@domain). If you voluntarily call someone a "DPO", all of Arts 37–39 apply, and you must notify AZOP using its appointment form (https://azop.hr/obrazac-za-imenovanje-sluzbenika-za-zastitu-podataka/).

---

## 9. International transfers (Chapter V)

### 9.1 Legal mechanisms
- **Adequacy decisions (Art 45):** includes the UK, Switzerland, Japan, Korea, Canada (commercial), Israel and others, and the **US for organisations certified under the DPF** (Commission Implementing Decision (EU) 2023/1795).
- **SCCs (Art 46(2)(c)):** Commission Implementing Decision (EU) **2021/914**. Use Module 2 (controller to processor) or Module 3 (processor to processor), plus a **transfer impact assessment (TIA)** following EDPB Recommendations 01/2020.
- **Derogations (Art 49):** narrow and not for routine SaaS use.

### 9.2 DPF status (Oct 2026)
- **General Court, 3 Sep 2025, T-553/23 *Latombe v Commission*:** action dismissed and the DPF upheld.
- **Appeal C-703/25 P,** lodged 31 Oct 2025 (OJ C/2025/6610). Microsoft was admitted as an intervener on 4 Jun 2026. **No hearing date** as of the last reports (Jul–Aug 2026). A request to suspend the DPF in the meantime was reportedly rejected (**VERIFY**).
- **US Supreme Court, *Trump v. Slaughter* (29 Jun 2026):** FTC commissioners can be removed at will. The adequacy decision relies heavily on FTC independence. noyb asked the Commission on 30 Jun 2026 to withdraw the decision and announced a CJEU action. gdpr.news (31 Aug 2026) reports that the action has been filed (**VERIFY**). The PCLOB reportedly cannot function (**VERIFY**).
- **The Commission's position:** it continues to apply the DPF and is monitoring.
- **AZOP's US-transfers page** (updated Jun 2026) still treats DPF transfers as needing no supplementary measures.
- **Practical posture:** the DPF can be used **today**, but have SCCs plus a short TIA ready for every US processor as a fallback, prefer EU data regions, and keep the vendor list mapped to transfer mechanisms.

**Lesson from the telecom case (2025):** AZOP fined €4.5M for missing SCCs and a missing *transfer risk assessment*, even for a group company. Keep TIAs on file.

### 9.3 Common processors

| Vendor | Entity / region | Transfer basis (verify current DPA) |
|---|---|---|
| Stripe | Stripe Technology Europe Ltd (IE) for EEA customers, with onward transfers to Stripe Inc (US) | DPF + SCCs in Stripe DPA (**VERIFY**) |
| Google (Analytics, Workspace, Cloud) | Google Ireland, Google LLC | DPF + SCCs. GA4: consent required under ZEK 43(4). Several EU DPAs (AT, FR, IT, 2022) found the old Universal Analytics unlawful before the DPF; disable advertising signals and set data retention to 2 months |
| AWS | AWS EMEA SARL; EU regions (e.g. eu-central-1) | DPF + SCCs (AWS GDPR DPA) |
| Mailgun (Sinch) | EU region (DE) available | DPF/SCCs (**VERIFY**) |
| SendGrid (Twilio) | US | DPF + Twilio BCRs/SCCs (**VERIFY**) |
| Brevo | Sendinblue SAS (FR) | EU-based; check its US sub-processors |
| Cloudflare | Cloudflare, Inc. | DPF + SCCs. Data Localization Suite available |
| Sentry | Functional Software, Inc.; EU data region (DE) available | DPF + SCCs (**VERIFY**) |
| PostHog | PostHog Inc.; EU Cloud (Frankfurt) | DPA with SCCs. Use EU cloud and cookieless mode where possible (**VERIFY** DPF status) |

**Example policy wording:**
> "Some of our processors are established in the USA. Transfers rely on the European Commission's adequacy decision for the EU-U.S. Data Privacy Framework (Decision (EU) 2023/1795) where the recipient is certified, and in addition on the Standard Contractual Clauses (Decision (EU) 2021/914). A copy of the safeguards is available at privacy@…"

Use exact wording. "May transfer" was penalised by AZOP.

---

## 10. Data retention: Croatian statutory periods (verified)

| Record | Period | Source |
|---|---|---|
| Accounting documents (knjigovodstvene isprave) behind entries in the journal, general ledger and subsidiary ledgers, which includes **invoices** | **At least 11 years**, unless the fiscalisation law says otherwise. Counted from the last day of the business year to which the books relate | Zakon o računovodstvu, Art 10(2) items 3–4 and Art 10(8) (NN 85/24, 145/24, 151/25) |
| Journal and general ledger; subsidiary ledgers | At least 11 years | ZoR Art 11(2) |
| Payslips | At least 6 years | ZoR Art 10(2) item 1 |
| Payroll analytical records | Permanently | ZoR Art 10(2) item 2 |
| Annual financial statements | Permanently, in original | ZoR |
| **Fiscalised eRačuni** (issued and received) | **6 years** from the end of the year of issue, in original form, if the fiscalisation procedure was carried out. Afterwards the Tax Administration keeps the data | **Zakon o fiskalizaciji, NN 89/25, Art 35** (in force 1 Sep 2025; eRačun articles from 1 Jan 2026; MIKROeRAČUN issuing from 1 Jan 2027) |
| Tax records: books, documents, daily cash records | **10 years from the start of the limitation period**, unless a longer period applies. The limitation period starts at the end of the year in which the liability arose, so in practice about 11 years | **OPZ Art 66(18)**; tax limitation period 6 years (OPZ Art 108(1)–(2)) |
| VAT invoices | As under OPZ (real-estate documents: 10 years) | Zakon o PDV-u |
| Consumer written-complaint register (evidencija pisanih prigovora) | **1 year** from receipt, on a durable medium | **ZZP Art 10(7)** (NN 19/22, 59/23, 59/26). Reply within 15 days (Art 10(6)) |
| Contract and account data kept to defend claims | Up to the limitation period: **general 5 years** (ZOO Art 225); **claims between businesses from trade contracts for goods and services 3 years** (ZOO Art 228); periodic claims 3 years (Art 226); damages 3 years from knowledge, at most 5 years from the event (Art 230) | Zakon o obveznim odnosima (amended NN 69/26, in force 7 Jul 2026; Arts 225–230 unchanged per the consolidated text) |
| Video recordings | At most 6 months | ZPDZ Art 29 |
| Server, security and access logs | No statute. Typical **30–90 days for raw logs**; **6–12 months** for security or audit logs; longer only for an incident | Art 5(1)(e) with an LIA |
| Backups | Rolling 14–35 days; document that deleted data disappears on rotation | Art 5(1)(e) |
| Marketing consent proof | For as long as the consent is used, plus the limitation period for proof (e.g. +3 years, **VERIFY** proportionality; the ZEK prosecution limitation period is 4 years, Art 174) | Art 7(1) |
| Unsubscribe/suppression list (email or its hash) | For as long as you send marketing | Art 21(3) |
| Trial accounts that never converted | Delete about 6–12 months after the trial expires with no activity (tie to the nurture end date) | Art 5(1)(e) |
| Inactive paid accounts after cancellation | Delete account content 30–90 days after the contract ends (export window). Keep billing for 11 years (or 6 for eRačuni) | Art 5(1)(e); ZoR |

**Note for sole traders (obrt) taxed as paušalisti:** they are not bound by ZoR, but by income-tax and paušal rules (KPR) and OPZ Art 66 (10 years from the start of the limitation period) (**VERIFY** with your accountant).

**What to keep after a user deletes their account.** Keep the Stripe customer ID, invoices (name or company, address, OIB if B2B, amounts) and the contract acceptance record (Terms version and timestamp). Delete the projects, profile, analytics identifiers and support history older than the limitation period.

---

## 11. IP pseudonymisation and personal data in logs

- **IP addresses are personal data,** including dynamic IPs, where the controller has legal means to identify the person (CJEU C-582/14 *Breyer*).
- **Pseudonymised data is still personal data** for the controller (Recital 26; EDPB Guidelines 01/2025 on pseudonymisation, consultation version). CJEU C-413/23 P *EDPS v SRB* (4 Sep 2025) held that pseudonymised data *may* not be personal data **for a recipient** with no reasonable means of re-identification. The controller's information duty is still assessed at the time of collection. This does **not** take your own logs outside the GDPR.

**In practice:**
- Truncate IPs: IPv4 /24 (drop the last octet), IPv6 /48. Or hash with a key that rotates daily (HMAC-SHA256 with a daily salt) for analytics. Keep full IPs only in short-lived security logs (e.g. 30 days).
- Never log passwords, tokens, API keys, session cookies, full card numbers, OIBs, or the full contents of user projects.
- Mask email addresses, e.g. `j***@domain.hr` or a user ID instead.
- Scrub at the source: use a logging encoder or masking converter. Third-party log shippers may **bypass** your framework's masking layer, so mask before the appender, or use the shipper's own scrubbing rules. Test this.
- Error trackers: turn on server-side scrubbing, and turn off "send default PII" or request bodies.
- Access to logs: restricted, with MFA and audit.
- Retention is set in the log platform (e.g. 30 days hot, then deletion).

**Example log policy line:**
> "Application logs reference users by internal UUID; IP addresses are truncated after 30 days; secrets and PII fields (password, token, authorization, email, oib, iban) are masked before emission; logs are retained 30 days (security audit logs 12 months)."

---

## 12. Data minimisation in practice

**What you CAN store** (with a basis):
- email, name, password hash;
- company name, address, **VAT ID/OIB of business customers** (required on invoices: the buyer's OIB when the buyer is a taxable person, Zakon o PDV-u Art 79(1) item 3 and Art 79(2));
- Stripe customer and subscription IDs, last 4 card digits, card brand and expiry (from Stripe);
- plan and usage metrics;
- consent records;
- support tickets.

**What you should NOT store:**
- **Full card numbers (PAN) or CVV.** Use Stripe Elements or Checkout so that card data never touches your servers (PCI DSS SAQ A scope).
- **A consumer's OIB.** A B2C invoice does not need the buyer's OIB, and OIB is a unique national identifier. Collect it only when a law requires it (B2B R1 invoices, eRačun under fiscalisation 2.0). Do not ask for it "just in case". AZOP treats unnecessary OIB processing as high risk (B2 Kapital).
- **Copies of ID cards or passports** (AZOP fines in 2025 and 2026).
- **Special categories (Art 9)** (health, religion, biometrics, etc.). Avoid them. Warn in the Terms that users must not upload such data into free-text fields unless they are the controller and have a basis.
- **Plain-text passwords** or reversibly encrypted passwords. Use argon2id/bcrypt.
- Unnecessary date of birth, gender or phone number.
- Precise geolocation.
- Full user-agent fingerprints for tracking.

**Deleted accounts:** follow §4 (Art 17) and §10. **Inactive accounts:** send a warning (e.g. after 12 months inactive, or 6 months after trial expiry), then delete or anonymise. Anonymise usage statistics irreversibly, by aggregating or dropping identifiers, if you want to keep them.

---

## 13. Privacy by design and by default (Art 25)

**Rule.** Build data protection into design (e.g. pseudonymisation, minimisation). **By default**, process only the data necessary for each purpose: the amount, the extent of processing, the retention period and accessibility. Personal data must not be made public by default (Art 25(2)). See EDPB Guidelines 4/2019.

**Implementation checklist:**
- marketing checkbox unticked;
- analytics off until consent;
- project sharing private by default;
- public share links expire and are revocable;
- minimal sign-up form (email and password only; collect billing details only at upgrade);
- automatic retention jobs (cron) per data category;
- admin "break-glass" access logged;
- deletion and export built from day one;
- test environments use synthetic or masked data, never a production copy;
- for each new feature, a privacy review question: "What new personal data? Basis? Retention? Processor?"

---

## 14. Fines (Art 83) and compensation (Art 82)

**Art 83 maximums:**
- **€10M or 2%** of worldwide annual turnover, whichever is higher: Arts 8, 11, 25–39 (security, DPA, ROPA, breach notice, DPIA).
- **€20M or 4%:** principles, lawful basis and consent (Arts 5, 6, 7, 9), rights (Arts 12–22), transfers (Arts 44–49), and non-compliance with orders.

**Factors (Art 83(2)):**
- nature, gravity and duration;
- intent or negligence;
- mitigation;
- previous infringements;
- **cooperation**;
- categories of data;
- how the authority learned of it.

**Case law:**
- CJEU C-807/21 *Deutsche Wohnen* (5 Dec 2023): fines require intent or negligence, but no identified individual in management needs to be at fault.
- C-383/23 *ILVA* (13 Feb 2025): for the maximum, "undertaking" turnover means the whole group.
- The EDPB adopted guidelines on the use of fining powers in relation to other corrective powers on 21 Sep 2026 (AZOP news, confirmed 2026-10-25).

**Croatian specifics:**
- no fines on public bodies (ZPDZ Art 47);
- instalments are possible (Art 45);
- publication with name (Art 48);
- ZEK misdemeanour fines run separately for cookies and spam (Art 170).

**Art 82 (compensation).** Any person who suffered material or non-material damage may claim from the controller or processor.
- CJEU C-300/21 *Österreichische Post* (4 May 2023): no seriousness threshold, but the damage must be proven.
- C-340/21 (14 Dec 2023): fear of misuse after a breach can be damage; a breach does not automatically mean the security measures were inadequate.
- Claims go to Croatian civil courts under ZOO (damages limitation period 3/5 years, Art 230). NGO representation is possible (ZPDZ Art 41).
- **Croatian court practice:** no published leading Croatian Art 82 judgment was found in this research (**VERIFY**; search sudskapraksa.csp.vsrh.hr for "članak 82. Opće uredbe").

---

## 15. Employees and contractors (brief)

- **Basis:** contract or legal obligation for HR data. Consent is generally not valid for employees because of the power imbalance.
- **Zakon o radu Art 29:** employee data may be processed only where provided by law or necessary for employment rights and obligations. Employers with 20 or more employees must appoint a person to oversee this (**VERIFY** the exact current wording).
- **Monitoring:**
  - video only under ZPDZ Arts 26–30 (prior notice; no rest rooms or toilets; 6 months maximum);
  - biometrics for time recording only as an optional alternative with explicit consent (ZPDZ Art 23);
  - email or endpoint monitoring only with a documented LIA, a written policy, proportionality and no covert monitoring.
- **AZOP enforcement:** the 2025 telecom fine covered employee ID copies and criminal-record certificates collected without a basis.
- **Contractors with production access:** a confidentiality clause, instruction under Art 29/32(4), MFA, removal of access at offboarding, and a DPA if they are a separate company acting as a processor.
- **Transparency:** a separate employee privacy notice. EDPB coordinated enforcement in 2026 focuses on transparency, including toward employees (**VERIFY** the topic; AZOP joined CEF 2026 on 12 Jun 2026).

---

# ANNEXES

## (a) Privacy policy skeleton (Politika privatnosti), Croatian headings with English

1. **Uvod i voditelj obrade** (Introduction and controller): full name (e.g. "Obrt X, vl. Ime Prezime" or "X d.o.o."), OIB, registered address, email, phone. Art 13(1)(a).
2. **Kontakt za zaštitu podataka / Službenik za zaštitu podataka** (Privacy contact / DPO): privacy@… (DPO only if appointed). 13(1)(b).
3. **Koje podatke prikupljamo** (What data we collect), by source: from you (account, billing, support), automatically (logs, cookies), from third parties (Stripe, Google sign-in). 14(1)(d), 14(2)(f).
4. **Svrhe i pravne osnove obrade** (Purposes and legal bases): a table of purpose → data → basis (6(1)(a)/(b)/(c)/(f)) → retention. Covers account and service; billing and accounting; security and logs; error monitoring; analytics; transactional emails; marketing (trial nurture, newsletter); support; admin access to projects for support; defending claims. 13(1)(c).
5. **Legitimni interesi** (Legitimate interests): a specific list for each purpose. 13(1)(d).
6. **Primatelji i izvršitelji obrade** (Recipients and processors): categories (hosting, email, payments, monitoring, analytics, accountant, authorities on legal request), plus a link to the sub-processor list. 13(1)(e).
7. **Prijenos u treće zemlje** (Transfers to third countries): which vendors, countries, mechanism (DPF Decision 2023/1795 / SCCs 2021/914), how to get a copy. Clear, not "may". 13(1)(f).
8. **Rokovi čuvanja** (Retention): concrete periods (from Annex (c)). 13(2)(a).
9. **Vaša prava** (Your rights): access, rectification, erasure, restriction, portability, objection (**the right to object shown separately and prominently**, Art 21(4)), withdrawal of consent. How to exercise them, the 1-month deadline, free of charge, identity check. 13(2)(b)–(c).
10. **Pravo na pritužbu AZOP-u** (Right to complain to AZOP): Agencija za zaštitu osobnih podataka, Ulica Metela Ožegovića 16, 10000 Zagreb, azop@azop.hr, www.azop.hr. 13(2)(d).
11. **Obveznost davanja podataka** (Whether providing data is required): which fields are required for the contract or by law (OIB for B2B invoices) and the consequences of not providing them. 13(2)(e).
12. **Automatizirano odlučivanje i profiliranje** (Automated decisions and profiling): none, or a description (e.g. Stripe fraud screening). 13(2)(f).
13. **Kolačići i slične tehnologije** (Cookies and similar technologies): a link to the cookie policy; legal basis ZEK Art 43(4); how to change consent.
14. **Izravni marketing** (Direct marketing): basis (consent / ZEK Art 50(2) soft opt-in), unsubscribe in every email.
15. **Djeca** (Children): the service is not intended for under-16s (or 18+ for B2B). ZPDZ Art 19.
16. **Sigurnost** (Security): a summary of measures.
17. **Uloga izvršitelja obrade za korisnički sadržaj** (Processor role for customer content): for B2B customers' content, we act as processor under the DPA [link]; data subjects should contact the customer.
18. **Izmjene politike** (Changes to this policy): the version date, and how users will be notified.
19. **Datum stupanja na snagu / verzija** (Effective date and version).

## (b) ROPA example for a SaaS

| # | Activity | Purpose | Data subjects | Data categories | Basis | Recipients / processors | Third country / safeguard | Retention | Security (summary) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | User accounts | Provide the service | Users | Email, name, password hash, settings | 6(1)(b) | Hosting provider (EU data centre) | None | Contract + 30–90 days | Encryption, hashing, RBAC |
| 2 | Customer content (processor role) | Store customer data | Customers' own clients | Names, contact details, content entered by the customer | Processor under Art 28 DPA | Hosting | None | Per customer; deleted 30–90 days after termination | As above, plus admin access log |
| 3 | Billing | Charge subscriptions, issue invoices | Paying customers | Name or company, address, OIB (B2B), Stripe IDs, last 4 digits | 6(1)(b), (c) | Stripe; accountant; Tax Administration (fiscalisation) | US: DPF + SCCs | Invoices 11 years (eRačun 6 years) | Stripe-hosted card entry |
| 4 | Transactional email | Service notices | Users | Email, name | 6(1)(b) | Transactional email provider | DPF/SCCs or EU region | Sending logs 30 days | TLS, DKIM |
| 5 | Trial nurture & newsletter | Marketing | Trial users, subscribers | Email, name, engagement | Consent / ZEK 50(2) / 6(1)(f) B2B | Email provider | as above | Until opt-out; suppression list ongoing | Double opt-in |
| 6 | Security logs | Security, abuse prevention | Users, visitors | IP, user ID, UA, timestamps | 6(1)(f) | Log management provider (EU region) | Per DPA | 30 days raw; 12 months audit | Masking, IP truncation |
| 7 | Error monitoring | Fix bugs | Users | User ID, stack traces (scrubbed) | 6(1)(f) | Error-monitoring provider | DPF/SCCs | 30–90 days | Scrubbing |
| 8 | Web analytics | Usage statistics | Visitors | Pseudonymous IDs, pages | Consent (cookies) / 6(1)(f) cookieless | GA4 / PostHog EU | DPF/SCCs | 2–14 months | IP anonymisation |
| 9 | Support | Answer requests | Users | Email, ticket content | 6(1)(b)/(f) | Helpdesk / email | — | 3 years after ticket closure | Access control |
| 10 | Admin console access | Support and security | Users | All account and project data viewed | 6(1)(b)/(f) | Internal only | — | Admin audit log 12–24 months | MFA, logging |
| 11 | DSAR & breach registers | Accountability | Requesters | Request details | 6(1)(c) | — | — | 3–5 years (**VERIFY** proportionality) | Restricted |
| 12 | Consumer complaints | ZZP compliance | Consumers | Complaint, response | 6(1)(c) | — | — | 1 year (ZZP Art 10(7)) | — |

## (c) Retention schedule for Croatia (summary)

| Data | Period | Trigger | Basis |
|---|---|---|---|
| Invoices / accounting documents (non-eRačun) | 11 years | End of business year | ZoR Art 10 |
| Fiscalised eRačuni | 6 years | End of year of issue | Zakon o fiskalizaciji Art 35 |
| Ledgers | 11 years | End of business year | ZoR Art 11 |
| Tax records (incl. obrt) | 10 years from start of tax limitation period | Start of limitation period | OPZ Art 66(18) |
| Contract acceptance, Terms version | 5 years (B2C general) / 3 years (B2B trade contracts) after end of contract | End of contract or due date | ZOO Arts 225, 228 |
| Consumer complaints | 1 year | Receipt | ZZP Art 10(7) |
| Account and project content | Contract + 30–90 days | Termination | Art 5(1)(e) |
| Unconverted trial | 6–12 months | Trial expiry / last login | Art 5(1)(e) |
| Raw app/access logs | 30–90 days | Creation | Art 5(1)(e) + LIA |
| Security/audit logs | 6–12 months (longer if an incident) | Creation | LIA |
| Backups | 14–35 days rolling | Creation | Art 5(1)(e) |
| Marketing consent proof | Consent lifetime + up to 4 years (ZEK limitation) | Withdrawal | Art 7(1) / ZEK Art 174 |
| Suppression list | While marketing continues | — | Art 21(3) |
| Video surveillance | At most 6 months | Recording | ZPDZ Art 29 |
| Payslips / payroll records | 6 years / permanently | — | ZoR Art 10 |

## (d) Art 28(3) DPA checklist (Ugovor o obradi)
- [ ] Subject matter, duration, nature and purpose, types of personal data, categories of data subjects (Art 28(3), first paragraph) — put these in an Annex.
- [ ] Processing only on **documented instructions** from the controller, including on transfers. The processor tells the controller if an instruction infringes the law (28(3)(a), last paragraph).
- [ ] **Confidentiality** of persons authorised to process (28(3)(b)).
- [ ] **Art 32 security measures** (28(3)(c)), with a technical and organisational measures (TOMs) annex.
- [ ] **Sub-processor conditions:** prior specific or general written authorisation, notice of changes, right to object, flow-down of obligations, processor fully liable for its sub-processors (28(2), 28(4), 28(3)(d)).
- [ ] **Help with data subject rights** (28(3)(e)).
- [ ] **Help with Arts 32–36:** security, breach notification (fixed time limit, e.g. ≤48h), DPIA, prior consultation (28(3)(f)).
- [ ] **Deletion or return** at the end of services, at the controller's choice, unless EU or Member State law requires storage (28(3)(g)).
- [ ] **Audits and information:** make available everything needed to show compliance; allow audits and inspections (28(3)(h)).
- [ ] International transfers: mechanism (DPF/SCCs Module 2/3), TIA, list of locations.
- [ ] Records under Art 30(2) kept by the processor.
- [ ] Liability, cooperation with AZOP, governing law (Croatian), order of precedence over the Terms of Service.
- [ ] Optional: incorporate the EU Commission standard Art 28 clauses (Decision (EU) 2021/915).
- [ ] **Before signing (Art 28(1)):** document due diligence on the processor's guarantees, e.g. ISO 27001/SOC 2 and a security questionnaire. AZOP fined the telecom operator for skipping this.

## (e) Common mistakes AZOP and the EDPB penalise
1. **No Art 28 DPA** with a processor (B2 Kapital, €2.265M).
2. **No prior check of a processor's security** (telecom 2025).
3. **Third-country transfers without SCCs or a TIA**, including to group companies (telecom, €4.5M; TikTok €530M confirmed by the Irish High Court in Jun 2026).
4. **Vague or contradictory privacy notices.** Wrong legal basis; "may transfer" wording (B2 Kapital, telecom, casino).
5. **Bundled consent** across several purposes; consent used to justify excessive processing (casino, €2.59M).
6. **Cookies placed without prior consent**, or no reject option (Croatian betting companies, €20k and €30k; ZEK Art 170 misdemeanour).
7. **Keeping data after the purpose has ended**; no deletion routine (real-estate agency, €100k).
8. **Collecting ID-card, passport or bank-card copies** without a legal basis (real-estate 2026; telecom 2025).
9. **Weak security leading to exfiltration**, no logging, and failure to detect the breach (B2 Kapital; collection agency €5.47M).
10. **Staff not instructed or trained** (Art 32(4)) (real-estate 2026).
11. **Poor cooperation with AZOP:** late answers, missing logs (an aggravating factor in B2 Kapital).
12. **Ignoring or missing DSAR deadlines;** charging for or obstructing access; demanding ID unnecessarily (EDPB CEF 2024 on the right of access; CEF 2025 on erasure).
13. **Marketing emails without consent or opt-out;** hiding the sender's identity (ZEK Art 50; ICO's £300k KRA case as a comparator).
14. **Not documenting breaches** in the internal register, or late notification without reasons (Art 33(1) and (5)).
15. **Video surveillance without proper signs or access logs**, or kept longer than 6 months (ZPDZ Arts 27–29, 51).
16. **Biometrics beyond what is necessary,** or without explicit consent (ZPDZ Art 22; casino 2026).
17. **Ignoring your own DPO's advice** (an aggravating factor in the telecom case).

---

## Sources

**Primary law**
- GDPR (EUR-Lex): https://eur-lex.europa.eu/eli/reg/2016/679/oj
- ZPDZ (NN 42/2018): https://narodne-novine.nn.hr/clanci/sluzbeni/2018_05_42_805.html ; https://www.zakon.hr/z/1023
- ZEK: https://www.zakon.hr/z/182 (Arts 43, 50, 51, 170, 173, 174)
- ZOO: https://www.zakon.hr/z/75 (Arts 225–230)
- ZoR (NN 85/24): https://narodne-novine.nn.hr/clanci/sluzbeni/2024_07_85_1474.html ; https://www.zakon.hr/z/118
- OPZ: https://www.zakon.hr/z/100 (Arts 66, 108)
- Zakon o fiskalizaciji (NN 89/25): https://www.zakon.hr/z/3960 (Art 35)
- ZZP: https://www.zakon.hr/z/193 (Art 10)
- Zakon o PDV-u: https://www.zakon.hr/z/1455 (Art 79)

**AZOP**
- Fines register: https://azop.hr/upravne-novcane-kazne-3/
- Breach reporting: https://azop.hr/izvjescivanje-o-povredi-osobnih-podataka/
- Complaints: https://azop.hr/zahtjev-za-utvrdivanje-povrede-prava/
- US transfers: https://azop.hr/prijenos-osobnih-podataka-u-sad/
- B2 Kapital decision: https://azop.hr/agenciji-za-naplatu-potrazivanja-izrecena-upravna-novcana-kazna-u-iznosu-od-226-milijuna-eura/
- EDPB 2025 ranking: https://azop.hr/godisnje-izvjesce-edpb-a-azop-u-europskom-vrhu-po-izrecenim-kaznama/
- Cookie fines: https://azop.hr/obrada-osobnih-podataka-putem-kolacica-upravne-novcane-kazne/

**Reporting on cases**
- Telecom: Jutarnji list report, Nov 2025 (search jutarnji.hr for the AZOP €4.5M telecom fine)
- Real-estate agency: https://forbes.dnevnik.hr/aktualno/azop-izrekao-kaznu-agenciji-za-nekretnine-od-100-tisuca-eura/
- Casino: https://www.hina.hr/vijest/12522480 and the GDPR Croatia summary
- Cookie fines: https://regula.consent.hr/hrvatskim-tvrtkama-50-000-eura-gdpr-kazne-za-kolacice/
- Retention practice: https://www.teb.hr/novosti/2026/cuvanje-racuna-i-knjigovodstvene-dokumentacije/

**Digital Omnibus**
- https://gdprlocal.com/digital-omnibus-what-leaked-documents-say-about-ai-and-personal-data/
- https://www.iubenda.com/en/blog/eu-digital-omnibus-gdpr-changes-proposed-amendments-explained/
- EDPB-EDPS Joint Opinion 2/2026: https://www.edpb.europa.eu/system/files/documents/2026-02/edpb_edps_jointopinion_202602_digitalomnibus_en.pdf

**DPF**
- Latombe appeal notice: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:C_202506610
- Microsoft intervention: https://www.dataguidance.com/news/eu-cjeu-admits-microsoft-intervener-appeal-concerning
- Trump v. Slaughter analysis: https://secureprivacy.ai/blog/is-the-eu-us-data-privacy-framework-at-risk-the-ftc-ruling-explained-2026
- iubenda DPO Newsletter #157

**Vendors**

**Still to verify**
- Inteligo Media C-654/23 (date and holding)
- AZOP DPIA list (NN 88/2019)
- final status of EDPB Guidelines 1/2024 (legitimate interest)
- whether noyb's DPF action has been filed (still unconfirmed 2026-10-25)
- final text of the Council mandate on the Digital Omnibus (21 Oct 2026)
- Zakon o radu Art 29 (exact wording)
- Zakon o hrvatskom jeziku (scope for private websites)
- current DPF and EU-region status of Stripe, Sentry, PostHog and Mailgun
- Croatian Art 82 court practice
