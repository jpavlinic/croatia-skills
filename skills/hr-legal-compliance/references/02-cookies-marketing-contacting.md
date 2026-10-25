# Cookies, tracking, e-marketing and contacting people: Croatian software business (obrt or d.o.o.)

**Status:** researched 2026-10-05; Digital Omnibus status re-checked 2026-10-25.

General information, not legal advice. Items marked **VERIFY** are uncertain or need a lawyer's check before you rely on them.

Croatian sources were read in full from zakon.hr's consolidated texts:
- **ZEK**: Zakon o elektroničkim komunikacijama, NN 76/22, 14/24, 45/26 (the last one dated 29.04.2026)
- **ZZP**: Zakon o zaštiti potrošača, NN 19/22, 59/23, 59/26 (the last one dated 09.06.2026)
- **ZET**: Zakon o elektroničkoj trgovini, NN 173/03 … 67/25

AZOP, HAKOM and EU sources are cited inline. The full list is in §9.

---

## 0. Key findings

1. **Cookie rule in Croatia = ZEK čl. 43. st. 4.** This is unchanged by the 2024 and 2026 amendments. It requires prior consent (privola) for any storing of, or access to, information on the user's device. There are only two exemptions: transmission of a communication, or storage that is *nužno* (necessary) to provide a service the user explicitly requested. Croatia has **no statutory analytics exemption**.
2. **Unsolicited e-marketing rule = ZEK čl. 50.** ("Neželjene elektroničke komunikacije")
   - Consent is required for email, SMS, MMS, fax and automated calls (st. 1).
   - Soft opt-in for your own customers (st. 2).
   - Every message must show the sender's identity and a valid free opt-out address (st. 3).
   - **St. 4: paragraphs 1 and 2 do not apply to communications to legal persons (pravne osobe).** B2B email to a d.o.o. needs no ZEK consent. It is still subject to GDPR when the address identifies a person, and to st. 3.
   - Obrtnici, freelancers and members of liberal professions in independent practice are natural persons. They are **not** covered by the st. 4 exemption.
3. **Penalties under ZEK čl. 170. st. 1.** Breaches of 43(4), 50(1), 50(2) and 50(3) are points 12–15.
   - Legal person: €13,270–132,720
   - Odgovorna osoba (responsible person in the company): €2,650–13,270
   - Fizička osoba (natural person): €1,320–6,630, with higher amounts if the breach was for gain
   - Misdemeanour courts (općinski sud) decide. HAKOM inspectors supervise. HAKOM **or** AZOP can order a breach to stop (čl. 51). Limitation period is 4 years (čl. 174).
   - Separately, AZOP fines cookie and marketing breaches under the **GDPR**. In Sept 2023 it issued cookie fines of €20k and €30k, based on GDPR Arts 6, 7 and 13.
4. **ePrivacy Regulation is dead.** The Commission withdrew it on 16 July 2025 and published the withdrawal in the OJ on 6 Oct 2025 (C/2025/5423). Directive 2002/58/EC plus ZEK remain the law.
5. **Digital Omnibus (data/GDPR part) is NOT adopted.** It would add new GDPR Arts 88a and 88b. The Council agreed its negotiating mandate on **21 Oct 2026** (it proposes further exemptions from cookie consent); the Parliament position is pending and trilogues have not started. Adoption is expected **2027 at the earliest**. The separate AI Omnibus *was* adopted (Reg. (EU) 2026/1744, in force 27 July 2026), but it does not touch cookies. **Build for the current rules.**
6. **CJEU C-654/23 Inteligo Media (13 Nov 2025)** matters for your trial funnel:
   - A free tier or free account can count as obtaining contact details "in the context of the sale" for soft opt-in, because the paid tier supplies the remuneration.
   - Informational newsletters are still direct marketing if their aim is to promote the paid service.
   - ePrivacy Art 13 is the **exclusive** basis for such emails and displaces GDPR Art 6.
7. **ZZP after NN 59/26.** "Proizvod" (product) includes services and digital services (čl. 4).
   - Any "posebni oblik prodaje" (sale, discount) must be priced **below the lowest price in the prior 30 days** (čl. 19. st. 1). Breach is misdemeanour point 35 of čl. 149: €1,500–50,000 for a legal person.
   - The obligation to *display* the 30-day reference price applies to goods (st. 4) and to services sold in business premises (st. 7). It expressly does **not** apply to advertising of services or to distance contracts (second "st. 7", in effect st. 8).
   - Fake countdowns are on the blacklist (čl. 37. t. 11). So are fake reviews (t. 31–32).
   - A "withdrawal button" (funkcija za jednostrani raskid, čl. 81.a) now applies to online consumer contracts.
8. **Ne zovi register:** ZZP čl. 12 plus Pravilnik NN 117/22. HAKOM keeps the register. Calling or messaging (including WhatsApp and Viber) consumers whose numbers are on it is a ZZP offence (čl. 149. st. 1. t. 21). The Državni inspektorat (State Inspectorate) enforces it.

---

## 1. EU framework and its status in 2026

### 1.1 ePrivacy Directive 2002/58/EC (as amended by 2009/136/EC)

**Art 5(3).** Storing information, or gaining access to information already stored, in a user's terminal equipment is allowed only with consent given after clear and comprehensive information, per Directive 95/46, now the GDPR (Art 94(2) GDPR).

There are two exemptions:
- (a) storage or access "for the sole purpose of carrying out the transmission of a communication"; or
- (b) storage or access "strictly necessary" for an information society service "explicitly requested" by the user.

Art 5(3) covers *any* information, personal or not. It applies to cookies, localStorage, sessionStorage, IndexedDB, cache, pixels and fingerprinting scripts alike.

**Art 13** covers unsolicited communications:
- (1) Automated calling systems, fax and email (which includes SMS) for direct marketing require **prior consent**.
- (2) **Soft opt-in.** Contact details obtained from customers "in the context of the sale of a product or a service" may be used for direct marketing of the controller's **own similar products or services**. The customer must have been given a clear, free, easy chance to object at collection and in every message.
- (3) Other unsolicited communications (e.g., live calls) are opt-in or opt-out per national law.
- (4) Disguising or concealing sender identity, or omitting a valid opt-out address, is banned.
- (5) Paras 1 and 3 apply to natural persons. Member States must "sufficiently protect" the legitimate interests of legal persons.

### 1.2 Key EU interpretive sources

**CJEU C-673/17 Planet49 (1 Oct 2019).** Pre-ticked boxes are not valid consent. Art 5(3) applies whether or not the data is personal. Users must be told cookie duration and third-party access. AZOP explicitly relies on this case.

**CJEU C-654/23 Inteligo Media (13 Nov 2025).** See §0 point 6. Bird & Bird reads time-limited free trials as covered, because whoever continues past the trial pays. Free white papers with no paid version are not covered.

**EDPB Guidelines 2/2023 on Technical Scope of Art 5(3)** (final v2, adopted 7 Oct 2024, published 16 Oct 2024). Art 5(3) covers:
- pixel tracking and tracking links (URL-based tracking);
- local processing that sends results back;
- IP-based tracking where the entity instructs the device to send information;
- JavaScript that collects device or browser properties (fingerprinting);
- IoT reporting.

"Cookieless" is therefore **not** automatically outside Art 5(3). The test is whether you cause information to be stored on, or read from, the device.

**EDPB Cookie Banner Taskforce Report** (adopted 17 Jan 2023). Its positions:
- A first layer with no reject option is a breach.
- Pre-ticked boxes are invalid.
- Deceptive link design (a reject link hidden in text) and deceptive colours or contrast are problematic case by case.
- Claiming "legitimate interest" for cookies is invalid.
- Mislabelling non-essential cookies as "essential" is a breach.
- Withdrawal must be easy; a persistent icon or link is expected.

**EDPB Guidelines 05/2020 on consent** (paras 39–41). Cookie walls do not yield freely given consent. **EDPB Opinion 08/2024** (17 Apr 2024) covers "consent or pay" for *large online platforms*. It is not directly aimed at a small SaaS, but the principle is that an equivalent free alternative without behavioural tracking should be offered. A small SaaS should simply not use a cookie wall.

### 1.3 ePrivacy Regulation: withdrawn

The 2017/0003(COD) proposal was announced as withdrawn in the Commission Work Programme 2025 (11 Feb 2025). The withdrawal was approved 16 July 2025 and published in the OJ on 6 Oct 2025 (C/2025/5423). Source: EP Legislative Train, updated 20 Sept 2026.

### 1.4 Digital Omnibus (COM, 19 Nov 2025): status

**Proposal content (cookies):**
- Cookie rules would move into the GDPR via new **Art 88a** whenever personal data is processed. The ePrivacy Directive would remain for non-personal data.
- Consent-free cases would be a closed list: transmission; a service explicitly requested; **first-party aggregated audience measurement for the provider's own service and internal use**; and security of a service requested by the user.
- After a refusal, the site may not re-ask for the same purpose for **6 months**. After consent, it may not re-ask while that consent remains valid.
- **Art 88b** would require honouring machine-readable browser or OS consent signals. Browser makers other than SMEs would have to support them. Art 88b would apply after 24 months; Art 88a after 6 months.

**Status (Oct 2026):**
- The AI part was adopted: Reg. (EU) 2026/1744, signed 8 July 2026, OJ 24 July, in force 27 July 2026.
- The **data/GDPR/cookie part is still at first reading.** The Council agreed its mandate on 21 Oct 2026, with further cookie-consent exemptions than the Commission proposal (exact list: **VERIFY** in the Council text). The Parliament position and trilogue are still to come, and conclusion is not expected before 2027.
- **EDPB-EDPS Joint Opinion 2/2026** (Feb 2026) broadly supports moving cookie rules under the GDPR and the audience-measurement exemption, with caveats.
- **VERIFY** before any 2027 redesign.

**Practical consequence.** Today, Croatian law (ZEK 43(4)) has *no* analytics exemption. The Omnibus would create one for strictly first-party, aggregated, own-use measurement. Self-hosted, cookieless, first-party analytics is a "future-proof" choice either way.

---

## 2. Croatian law

### 2.1 ZEK (NN 76/22, 14/24, 45/26)

**Čl. 43. st. 4 (cookies; storage on terminal equipment).** Unchanged by 45/26. It reads:

> "Uporaba elektroničkih komunikacijskih mreža za pohranu podataka ili za pristup već pohranjenim podacima u terminalnoj opremi krajnjeg korisnika ili korisnika dopušteno je samo u slučaju kada je taj krajnji korisnik ili korisnik dao svoju privolu, nakon što je dobio jasnu i potpunu obavijest u skladu s propisima o zaštiti osobnih podataka, i to osobito o svrhama obrade podataka. Time se ne može spriječiti tehnička pohrana podataka ili pristup podacima isključivo u svrhu obavljanja prijenosa komunikacija … ili, ako je to nužno, radi pružanja usluga informacijskog društva na izričit zahtjev krajnjeg korisnika ili korisnika."

The Croatian text says "nužno" where the Directive says "strictly necessary". AZOP applies the strict Directive / WP29 standard regardless.

**Čl. 50 (Neželjene elektroničke komunikacije):**
- **st. 1:** Automated calling systems without human intervention, fax, or email including SMS and MMS, used for "izravna promidžba i prodaja" (direct marketing and sales), are allowed only with the end user's **prior consent**.
- **st. 2 (soft opt-in):** A trader (fizička ili pravna osoba trgovca) may use email addresses obtained *from its consumers* in connection with the sale of products or services. They may be used for direct marketing of **exclusively its own similar products or services**. The consumer must have had a clear, free and easy way to object at collection *and* in every message, and must not have refused in advance.
- **st. 3:** The following are prohibited for marketing email, SMS and MMS:
  - misrepresenting or concealing the sender;
  - sending without a valid address or number to which the recipient can send a free stop request;
  - messages contrary to e-commerce rules (ZET), or messages urging visits to sites that breach them.
- **st. 4:** "Odredbe stavaka 1. i 2. … ne primjenjuju se na komunikaciju … prema pravnim osobama u svrhu izravne promidžbe i prodaje." St. 3 still applies to B2B.
- st. 5–10 are duties of email service operators. They are not relevant to you.

"Elektronička pošta" is defined in čl. 4. t. 15 as *any* text, voice, sound or image message sent over a public communications network that can be stored until the recipient collects it. This arguably covers OTT messages (WhatsApp, Viber, Messenger). **VERIFY** for LinkedIn InMail; treat it as covered to be safe.

**Supervision and enforcement:**
- **Čl. 51 (amended NN 45/26):** "Agencija [HAKOM] ili tijelo nadležno za zaštitu osobnih podataka [AZOP]" may, ex officio or on request, order breaches of čl. 42–50 to stop, and may demand information.
- **Čl. 161–162:** HAKOM's inspectors (inspektori elektroničkih komunikacija) carry out inspection of the whole Act.
- **Čl. 173:** The općinski sud (municipal court) handles misdemeanour proceedings at first instance. Inspectors may issue a prekršajni nalog (misdemeanour order).
- **Čl. 174:** 4-year limitation.
- In practice, complaints about spam SMS and email have historically gone to HAKOM (e.g., nezeljeni.sms@hakom.hr). AZOP handles cookies and marketing as a GDPR matter (Arts 6, 7, 13, 21) and fines under GDPR Art 83. **The 2023 AZOP cookie fines were GDPR fines, not ZEK fines.** Some commentary conflates the two.

**Penalties: čl. 170 (NN 45/26), "Teške povrede".** St. 1 covers legal persons at €13,270–132,720, for these points:
- t. 12: storage or access without consent or information (43/4);
- t. 13: marketing by email, SMS or automated systems without prior consent (50/1);
- t. 14: using consumer emails without a free, easy objection (50/2);
- t. 15: hidden sender, no opt-out address, or contrary to e-commerce rules (50/3).

Other paragraphs:
- st. 2: odgovorna osoba €2,650–13,270
- st. 3: natural person €1,320–6,630
- st. 4: if committed for gain, odgovorna osoba €5,300–26,540 and natural person €2,650–13,270
- Equipment confiscation is possible for some points.

Whether an **obrtnik** is punished as a "fizička osoba" under st. 3 or otherwise: **VERIFY**. The article has no separate "fizička osoba obrtnik" category.

*Numbering note:* older commentary cites "čl. 166/170 t. 18–21". Those were the kuna-era and original numbers. Current euro čl. 170. st. 1 uses points 12–15.

### 2.2 Does Croatia protect legal persons?

- Under ZEK, no for consent and soft opt-in (čl. 50. st. 4). Yes for sender identity and opt-out (st. 3).
- Under GDPR, legal persons' own data is not protected (Recital 14). But AZOP (2019 opinion on marketing) says a business email that identifies a natural person (ana.horvat@primjer.hr) **is personal data**. AZOP also says data of obrtnici, slobodna zanimanja and natural-person entrepreneurs is personal data.
- So B2B email to a d.o.o.:
  - ZEK consent: not required.
  - GDPR lawful basis: required for a named person. Legitimate interest (Art 6(1)(f), Recital 47) is normally used.
  - Art 21(2)–(3) right to object must be honoured absolutely.
  - Art 21(4) requires the objection right to be flagged clearly and separately at first communication.
  - Art 14 notice is required.
- AZOP also states that business contact data may be used only "u svrhu službenog (poslovnog) kontaktiranja vezanog uz djelatnost pravne osobe". Keep cold outreach strictly relevant to the recipient's business role.
- **Obrt or sole proprietor recipients** are not "pravne osobe". ZEK čl. 50. st. 1 consent applies. The soft opt-in applies only if they are your customers *and* "potrošači"; čl. 50. st. 2 says "potrošača", which is narrower than the Directive's "customers". **VERIFY.** Conservative rule: **no cold email to obrtnici or freelancers without consent.**

### 2.3 ZZP, Ne zovi register (čl. 12; Pravilnik o Registru »NE ZOVI«, NN 117/22)

- Calls and/or messages by phone for promotion or sale to consumers on the register are prohibited (čl. 12. st. 1).
- HAKOM keeps the register. Operators enter numbers within 7 days.
- Traders can check numbers free one at a time ("da/ne" check on hakom.hr), or register to download the full list (Pravilnik čl. 11).
- "Poruka" includes SMS, MMS **and messages via interpersonal communication services**, i.e. WhatsApp and Viber (Pravilnik čl. 4. t. 3).
- Consent given before registration and not revoked, or given after registration, still allows contact (Pravilnik čl. 7).
- The register covers **consumers (fizičke osobe)** only.
- Penalty: čl. 149. st. 1. t. 21, €1,500–50,000 for a legal person. Enforced by the tržišna inspekcija (market inspection) of the Državni inspektorat.
- Also relevant:
  - **ZZP čl. 40. st. 1. t. 3:** "ustrajno i neželjeno komuniciranje s potrošačem putem telefona, telefaksa, elektroničke pošte…" (persistent, unwanted contact) is an aggressive practice in itself.
  - **čl. 11:** passing consumer data to third parties contrary to data protection rules is prohibited.
  - **čl. 18:** no ads in mailboxes marked as refusing them, and no postal ads after an explicit refusal.

### 2.4 ZET (NN 173/03 … 67/25)

- **čl. 6:** general information duties. These apply to your website imprint and are relevant to every commercial email footer:
  - name or firm, seat, contact including email;
  - register number and registry (sudski / obrtni registar);
  - supervising body if regulated;
  - VAT number if a VAT payer;
  - prices must state whether taxes and costs are included.
- **čl. 7, "Sadržaj komercijalnog priopćenja"** (content of a commercial communication). Each commercial communication must be:
  - (i) clearly identifiable as such on receipt;
  - (ii) clearly identify the person on whose behalf it is sent;
  - (iii) make promotional offers (discounts, gifts) clearly identifiable as such;
  - (iv) make the conditions to qualify easily accessible and clear.
- **čl. 8:** unsolicited commercial email only with prior consent, "u skladu sa zakonom kojim se uređuje područje … elektroničkih komunikacija". This defers to ZEK čl. 50, including the B2B exception.
- **čl. 22:** supervision by tržišni inspektori of the Državni inspektorat.
- **čl. 23 penalties** are still written in HRK in the consolidated text. At the fixed conversion rate of 7.53450:
  - legal person 5,000–100,000 HRK ≈ €663.61–13,272.28;
  - odgovorna osoba / natural person 1,000–10,000 HRK ≈ €132.72–1,327.23;
  - a 3–6-month activity ban is possible for grave or repeat breaches.
  - **VERIFY** the euro amounts applied in practice.

---

## 3. Cookie and tracking consent in practice

### 3.1 What is exempt vs. what needs consent

Test: is the storage or access strictly needed for something the user explicitly asked for, judged from the **user's** perspective? AZOP's recommendation (azop.hr/obrada-osobnih-podataka-kolacici, updated 6 Aug 2024) adopts WP29 Opinion 04/2012.

| Technology | Consent? | Notes |
|---|---|---|
| Session / auth cookie, JWT in localStorage for logged-in app | **No** | WP29 "authentication cookies". Keep to session or a reasonable lifetime; for "remember me", tie to the user ticking it. |
| CSRF token, security cookies (login abuse detection) | **No** | "User-centric security" cookies with limited duration. |
| Load balancer stickiness | **No** | Session duration. |
| Consent-state cookie or localStorage (stores the user's choice) | **No** | Needed to honour the choice. CNIL practice: keep the choice up to 6 months (refusal) and a consent cookie up to 13 months. **VERIFY**; not Croatian law. |
| UI preference (language, theme) set by user action | **No** (session) / grey if persistent | WP29: "UI customisation" for session or a few hours. A persistent language choice the user explicitly made is widely accepted. |
| Shopping cart / multi-step form state | **No** | "User-input" cookies. |
| Stripe.js `__stripe_mid` / `__stripe_sid` (fraud prevention) | **Likely no if limited to payment flow** | Fraud prevention for a payment the user requested is defensible as necessary or security. Stripe's advice to load Stripe.js on *every* page goes beyond that. Load it only on checkout and billing pages. **VERIFY.** |
| Google Analytics 4 | **Yes** | Third-party analytics. Also involves a US transfer, now covered by the EU-US Data Privacy Framework (adequacy 10 July 2023; General Court dismissed *Latombe* T-553/23 in Sept 2025; appeal status **VERIFY**). AZOP lists GA among tools that must not fire before consent (AZOP answer 14 Aug 2026). |
| Google Consent Mode v2, **Advanced** (cookieless pings before consent) | **Treat as yes** | Pings carry device-read data. Under EDPB 2/2023 that is likely Art 5(3) access. Use **Basic** mode (no Google tags until consent). **VERIFY.** |
| Meta Pixel, LinkedIn Insight, Google Ads conversion tags | **Yes** | AZOP 2026: must not activate before consent. Operational ad purposes (frequency capping, fraud) are also not exempt (AZOP/WP29). |
| Plausible / Umami / self-hosted cookieless analytics | **Grey; lower risk** | Nothing stored, but JS reads screen size, URL and referrer and sends them. EDPB 2/2023 suggests Art 5(3) can apply. Croatia has no analytics exemption (France's CNIL has one). Options: (a) put it behind consent anyway; (b) run first-party server-log analytics with no client JS; (c) accept residual risk with full disclosure. The Omnibus 88a(3)(c) would legalise (c)-type use later. **VERIFY.** |
| Session replay (Hotjar, Clarity, PostHog/Sentry Replay) | **Yes, high risk** | Captures keystrokes and screen content, possibly personal or sensitive data. Consent plus masking of all inputs plus DPA (data processing agreement). Avoid on authenticated app screens with client data. |
| Error tracking (Sentry, other JS error / RUM tools) | **Grey** | If the SDK sets cookies or session storage, or fingerprints the device, Art 5(3) is engaged. Error monitoring is not on the WP29 list. Lower risk if: no replay, no persistent IDs, no cookie or storage, PII scrubbed, purpose limited to fixing faults in the service the user is using. Many DPAs would still expect consent for third-party RUM. Server-side error logging carries no Art 5(3) issue. **VERIFY.** |
| YouTube embed | **Yes** | Use a click-to-load placeholder ("two-click"). youtube-nocookie.com still uses storage after play. |
| Google Maps embed | **Yes** (or click-to-load) | Loads Google cookies and sends the IP to Google. |
| Google Fonts loaded from Google CDN | Not Art 5(3), but **GDPR problem** | *LG München I, 20.01.2022, 3 O 17493/20*: transmitting the visitor IP to Google without a legal basis → €100 damages and injunction. **Self-host fonts.** |
| Chat widgets (Intercom, Crisp) | Usually **yes** for pre-chat tracking | Load them on click. |
| Social share buttons that load third-party scripts | **Yes** | Plain links are fine. WP29 exempts social plugin cookies only for logged-in members using the requested function, not for tracking. |
| localStorage, sessionStorage, IndexedDB, Cache API, service workers | **Same rules as cookies** | Art 5(3) is technology-neutral (EDPB 2/2023; ZEK 43(4) "pohrana podataka"). |
| Tracking pixels in marketing emails (open tracking) / tracked links | **Yes** under EDPB 2/2023 | Pixels and URL tracking fall within Art 5(3) (see §1.2). Put open tracking behind newsletter consent, or switch it off. **VERIFY**; enforcement is still unsettled. |

### 3.2 Banner requirements: AZOP plus EDPB checklist

**AZOP's model (Recommendation 2024 and answer of 14 Aug 2026):**
1. **No non-essential cookie or script before consent.** This covers page load and further navigation.
2. **First layer:** "Prihvaćam sve" and "Odbijam sve", each a single click and **designed identically** (same size, colour and contrast; no pre-highlighting). Also a "Postavke kolačića" (settings) option and a link to the cookie notice. An **X that closes the banner = no consent**, and browsing continues.
3. **Second layer:** granular categories, **all off by default**, with "accept all / reject all / confirm choices".
4. **Legitimate interest cannot be used** for cookies, and especially not for marketing (AZOP, explicit).
5. **Withdrawal as easy as giving consent.** A link to cookie settings in the **footer of every page**.
6. Refusing must not block basic content or functions. **No cookie wall.**
7. **Minimum information** (GDPR Art 13, per AZOP):
   - controller identity and contacts;
   - purpose per processing;
   - data types;
   - right to withdraw;
   - recipients and third parties;
   - storage period or cookie duration;
   - automated decisions if any;
   - third-country transfer risks.
8. The cookie policy must match reality. Remove claims about cookies you don't use. The site operator (controller) is responsible even if an agency built the site. AZOP recommends the **EDPB Website Auditing Tool**.
9. If you use **only necessary cookies, no banner is needed**, but you still need an accurate notice (AZOP 2026).

**From the EDPB Taskforce Report and general practice:**
- record of consent: timestamp, banner version, choices, pseudonymous ID (GDPR Art 7(1));
- re-ask when purposes or vendors change;
- re-prompt after refusal no sooner than about 6 months. That is CNIL practice and Omnibus-aligned, not Croatian law. **VERIFY.**

### 3.3 Croatian enforcement

- **AZOP, September 2023:** first cookie fines, €20,000 and €30,000, against companies. GDPR Art 6(1) (no legal basis), Art 7 (consent not properly obtained or withdrawable), Art 13(1)–(2) (inadequate information).
- AZOP's highest overall fine is €5.47M (a debt collector). A bank was fined €1.5M in Dec 2025 (see `01` §2.3).
- No public ZEK misdemeanour judgments on cookies were found. **VERIFY.**

---

## 4. Email marketing and contacting people

### 4.1 Legal bases matrix

| Recipient / situation | Email or SMS marketing allowed? | Basis |
|---|---|---|
| Consumer / individual, no relationship | **Only with prior consent** | ZEK 50(1); ZET 8. GDPR Art 6 is displaced (Inteligo). |
| Your customer (paid) or free-trial user who is a consumer | **Yes, soft opt-in**, for **your own similar** products, if opt-out was offered at signup and is in every message | ZEK 50(2); Dir. Art 13(2); Inteligo for free tiers and trials. |
| Obrtnik / freelancer / liberal professional as natural person, no relationship | **Consent** (conservative) | Not a "pravna osoba", so 50(4) does not apply. |
| d.o.o., j.d.o.o. or other legal person, generic address (info@, ured@) | **Allowed** without ZEK consent. GDPR is usually not engaged. | ZEK 50(4); still 50(3) and ZET 6–7. |
| d.o.o. employee named address (ana.horvat@primjer.hr) | **Allowed** under ZEK 50(4). GDPR legitimate interest with LIA (legitimate interests assessment), Art 14 notice, Art 21 opt-out. | GDPR 6(1)(f), Recital 47; AZOP 2019 (business use only). |
| Purchased or rented lists of consumers | **Effectively prohibited.** Consent to third-party marketing is almost never specific or informed for *you*; ZZP čl. 11 also applies. | ZEK 50(1); GDPR 6, 7, 14. |
| "Refer a friend" emails sent by you to the friend | **No** (you lack the friend's consent). Let the user send from their own client, or a share link. | ZEK 50(1). |
| Re-permission campaign to people without valid consent | **No.** Asking for consent by email is itself marketing. | UK *Honda/Flybe* line (ICO 2017); same logic under ePrivacy. **VERIFY** for HR. |

### 4.2 Consent standard

- GDPR Art 4(11) and Art 7: freely given, specific, informed, unambiguous, by active opt-in.
- **Unticked** checkbox; separate from ToS acceptance; not a condition of the service (Art 7(4)).
- Proof of consent is required (Art 7(1)).
- **Double opt-in** is not a statutory requirement in Croatia, but it is best evidence of who consented (German BGH practice) and prevents typos and abuse. Recommended.
- Store: timestamp, IP, form version and text, source URL, confirmation click time.

### 4.3 Soft opt-in conditions (ZEK 50(2) + Inteligo)

1. The address was obtained **from the person themselves** in the context of a sale. Free trial or free tier counts, per Inteligo, when a paid tier exists.
2. Marketing is for **your own similar** products or services. A plan upgrade, add-on or related feature of the same SaaS qualifies. A partner's product does not.
3. A **clear, free, easy opt-out at collection.** An **unticked** "I don't want marketing" checkbox, or a clear notice plus a one-click opt-out at signup.
4. An **opt-out in every message**.
5. The person hasn't refused.

The ZEK wording is "od svojih potrošača". For **business** trial users, use 50(4) where the customer is a legal person, plus GDPR LI.

Duration: no statutory limit. Stop after a reasonable period of inactivity, e.g. 12–24 months after trial expiry. **VERIFY**; this is common DPA practice.

### 4.4 Transactional vs marketing: your trial funnel

Inteligo's test: commercial purpose plus addressed individually equals direct marketing, even if the content is useful.

| Email | Classification | Basis / handling |
|---|---|---|
| Account confirmation, password reset, invoices, security alerts, ToS changes | Transactional / service | Contract (GDPR 6(1)(b)) or legal obligation. No unsubscribe required. Keep promotional content out. |
| "Your trial ends in 3 days; what happens next (charged / downgraded / data retention)" | Service, if neutral | Arguably needed to perform the trial contract and avoid surprise charges. It supports ZZP transparency duties. Adding a discount makes it mixed, so treat as marketing. |
| Onboarding "how to use feature X" during the trial | Grey | Helping use the contracted service is service-like. If it pushes conversion to paid, it is marketing. Safe path: send under the soft-opt-in regime with an unsubscribe link. |
| "Upgrade now and get 20% off" / expired-trial win-back offer | **Marketing** | Soft opt-in (Inteligo) for consumers; 50(4) for legal persons. Must satisfy ZET čl. 7 (identifiable as an offer; conditions clear) and ZZP čl. 19 and 37 (see §5). |
| Product newsletter / blog digest | Marketing | Consent, or soft opt-in for customers and trial users. |
| Feedback / NPS survey | Often treated as marketing by DPAs when it has a commercial aim. **VERIFY** | Include an unsubscribe link. |

**Design rule:** keep two streams.
- "Service" emails: no promotional content, no unsubscribe link needed (you may add a preferences link).
- "Marketing / lifecycle" emails: unsubscribe in every email, honoured immediately across all marketing streams.

### 4.5 Every marketing message must contain

- Sender identity (the firm/name as in the register). ZEK 50(3); ZET 7.
- A working, **free** opt-out: a link and/or a reply address. ZEK 50(3).
- Recognisable as a commercial communication; promotions labelled; conditions accessible (ZET 7).
- ZET 6 data. Best practice: address, OIB / register number, contact.
- For GDPR Art 21(4): the right to object must be shown clearly and separately at first communication at the latest.

### 4.6 Unsubscribe processing and suppression

- GDPR Art 21(3): after an objection, data must no longer be processed for direct marketing, i.e. immediately. There is no Croatian statutory day count. Process automatically and instantly. Allow at most a few days for manual channels.
- Gmail/Yahoo bulk-sender rules (since 2024) require **one-click unsubscribe** (RFC 8058 List-Unsubscribe-Post) honoured within 2 days. This is an industry rule, not law.
- **Suppression list:** keep the minimum (email or a hash of it, date, source) indefinitely to ensure you never email the person again. Basis: legitimate interest / compliance (GDPR 6(1)(c)/(f)). Delete the rest of the marketing profile (Art 17(1)(c)).

### 4.7 Cold B2B outreach

**Defensible:**
- Email to legal persons (d.o.o.) at generic or role addresses about products relevant to their business (ZEK 50(4)).
- Emails to named employees on LI with:
  - documented LIA;
  - relevance to their role;
  - low volume;
  - Art 14 notice;
  - instant opt-out;
  - no tracking pixels.

**Not defensible:**
- Obrtnici and freelancers without consent (natural persons; ZEK 50(1)).
- Personal Gmail addresses.
- Automated high-volume sequences ignoring replies.
- Persistent follow-ups after "no". ZZP 40 concerns consumers, but GDPR Art 21 applies anyway.

**Art 14 GDPR** (data not obtained from the data subject). Provide all Art 14(1)–(2) information. Where data is used to communicate, it must be given **at the first communication** at the latest (Art 14(3)(b)). That includes the **source** of the data, e.g. "sudski registar / your public website".
- The Art 14(5)(b) "disproportionate effort" exemption is not available when you are emailing the person anyway.

**LinkedIn outreach:**
- A manual, personalised message to a business contact is lower risk.
- Automated sequences via tools are higher risk. They also breach LinkedIn's User Agreement.
- Whether InMail is "elektronička pošta" under ZEK čl. 4(15) is untested. Treat as covered when the recipient is a natural person outside 50(4). **VERIFY.**

**Cold calling:**
- Live human calls are not in ZEK 50(1), which covers only automated systems.
- For **consumers**: check the Ne zovi register before each campaign (ZZP 12), and respect ZZP 40(1)(3) (no persistent calls).
- For businesses: GDPR LI plus Art 21.
- Automated or robo calls always need consent.

**SMS / WhatsApp / Viber marketing:**
- Consent (ZEK 50(1)), or soft opt-in for consumer customers. 50(2) speaks of "adrese elektroničke pošte", but SMS is within "elektronička pošta". **VERIFY.**
- The Ne zovi register also covers interpersonal-messaging "poruke".
- WhatsApp Business policy separately requires opt-in.

### 4.8 Contact forms

- Use data only to answer the enquiry: GDPR 6(1)(b) pre-contractual, or 6(1)(f).
- **No newsletter addition** without a separate, unticked opt-in.
- Short retention, e.g. 12 months after the enquiry is closed, unless a contract follows.
- Give Art 13 information at the form (link to the privacy notice).

---

## 5. Consumer law angles of marketing (ZZP, NN 19/22 … 59/26)

- **Unfair practices** (nepoštena poslovna praksa) are prohibited: čl. 33. Definition in čl. 34. Misleading actions in čl. 35, misleading omissions in čl. 36, the blacklist in čl. 37, aggressive practices in čl. 39–40. Damages are available (čl. 41) and the burden of proof is on the trader (čl. 42).
- **Fake urgency / countdowns:** čl. 37. t. 11 is per se banned. It covers falsely claiming a product is available only for a very limited time, or on special terms only for a limited time, to force an immediate decision.
  - A **real** deadline is fine, e.g. an offer valid until the trial expiry date + N days that genuinely ends.
  - **Do not reset timers or re-offer the "last chance" price repeatedly.**
  - An offer "valid until [date]" sent near the end of a trial is fine if that date is stated and enforced.
- **"Free" trial:**
  - čl. 37. t. 26: "besplatno / gratis" is banned if the consumer must pay anything beyond unavoidable response or delivery costs.
  - A truly free trial is OK. If a card is required and the trial **auto-converts to paid**, disclose this prominently before signup and in the trial-ending email. Disclose price, renewal period and how to cancel (čl. 36. st. 4: price, payment terms, right to terminate).
  - Silent auto-conversion risks čl. 36 omission and the Art 6/8 CRD pre-contract duties transposed in ZZP čl. 60 ff.
- **Price reductions (Omnibus Art 6a):**
  - **ZZP čl. 19. st. 1:** any posebni oblik prodaje (special sale) means selling **below the lowest price applied in the prior 30 days**. "Proizvod" includes services and digital services (čl. 4).
  - **Penalty čl. 149. st. 1. t. 35:** selling during a special sale at a price **not lower** than that 30-day minimum.
  - **The display duty** (show the 30-day lowest price):
    - goods (st. 4, also in advertising per st. 6);
    - services **in business premises** (st. 7);
    - it does **not** apply to advertising of services or to distance contracts (the second "st. 7").
  - The Directive's Art 6a covers goods only. Croatia extended the definition to services; that is gold-plating.
  - **Consequence for SaaS:** you need not *display* the 30-day lowest price online, but any advertised "akcija / sniženje / -20%" must truly be below your lowest price of the prior 30 days. Otherwise it breaches čl. 19/149 and is misleading under čl. 35.
  - **Personalised coupons** sent to one trial user: the Commission's Art 6a guidance (2021) excludes personalised reductions and loyalty schemes. Whether čl. 19 does so too is **VERIFY**. Avoid the "akcija" framing for personal coupons; present them as an individual offer with clear conditions (ZET 7).
- **Editorial / advertorial content without disclosure:** čl. 37. t. 16 (paid content presented as editorial). Commercial intent must be apparent: čl. 36. st. 2. t. 2.
- **Withdrawal button:** čl. 81.a (NN 59/26, in force from 19 June 2026). For distance consumer contracts concluded via an online interface, you must provide a "raskid ugovora" function during the 14-day withdrawal period, with a "potvrditi raskid ugovora" confirmation step and immediate acknowledgement on a durable medium. **VERIFY** how it interacts with SaaS where the consumer agreed to immediate performance (čl. 86 exclusions).
- **Penalties:**
  - čl. 149: legal person €1,500–50,000; odgovorna osoba €1,500–2,500; trader–natural person €750–2,500.
  - čl. 150: widespread / EU-wide infringements (incl. t. 56 nepoštena praksa) up to 4% of turnover, or 2–5% for EU-wide.
  - Enforcement by the Državni inspektorat.

---

## 6. Reviews, testimonials, influencers

- **Fake reviews:** čl. 37. t. 32 bans posting fake consumer reviews or endorsements, commissioning them, or misrepresenting reviews (e.g. showing only positive ones as if complete).
- **t. 31:** claiming reviews come from real users without reasonable, proportionate verification steps is banned.
- **čl. 36. st. 5. t. 3:** if you show reviews, you must state **whether and how** you verify they come from actual users.
- **Testimonials** from business customers: get written permission to use name, logo and quote. That covers GDPR for named persons and trademark use. Keep evidence they are genuine customers. Disclose any incentive (discount for a review).
- **Influencer / affiliate posts:** paid promotion must be clearly identifiable (čl. 36. st. 2. t. 2; čl. 37. t. 16). Industry standard: **IAB Croatia "Smjernice za bolje influencanje"** (Nov 2025, campaign "Važno je znati kad se plati"). These are self-regulatory, not law. Use a clear label at the start ("#reklama", "plaćena suradnja s …") and the platform's paid-partnership tool. The brand shares responsibility for the content. Contracts should require disclosure.

---

## 7. Practical templates

The Croatian texts below are drafts for legal and proofreading review. Replace [placeholders]. When you hand any of them to a user as a document, start it with the line `PREDLOŽAK – nije pravni savjet. Prilagodite ga svom slučaju i dajte ga na provjeru stručnjaku.`

### 7.1 Cookie banner, first layer

> **Kolačići na [Naziv]**
> Koristimo nužne kolačiće kako bi stranica i aplikacija radile (prijava, sigurnost). Uz Vašu privolu koristili bismo i analitičke kolačiće za mjerenje posjećenosti [te marketinške kolačiće za mjerenje uspješnosti oglasa]. Privolu možete u svakom trenutku povući putem poveznice „Postavke kolačića” u podnožju stranice. Više u [Obavijesti o kolačićima].
> [ Odbijam sve ] [ Prihvaćam sve ] [ Postavke kolačića ] ✕

Implementation notes:
- Both main buttons get identical styling.
- ✕ means reject.
- No non-essential script before a click.

**Second layer:** toggles, all OFF by default, for "Analitički" and "Marketinški". "Nužni" is shown as always active, with explanation. Buttons: [Odbijam sve] [Prihvaćam sve] [Spremi odabir].

### 7.2 Cookie policy table (example)

| Naziv | Pružatelj | Svrha | Vrsta / kategorija | Trajanje | Privola |
|---|---|---|---|---|---|
| `SESSION` | [Naziv] (prva strana) | Održavanje prijave u aplikaciju | Nužni | Sesija | Ne |
| `XSRF-TOKEN` | [Naziv] | Zaštita od CSRF napada | Nužni | Sesija | Ne |
| `cookie_consent` (localStorage) | [Naziv] | Pamćenje Vašeg izbora o kolačićima | Nužni | 6–12 mjeseci | Ne |
| `__stripe_mid`, `__stripe_sid` | Stripe Payments Europe Ltd. (IE) | Sprječavanje prijevara pri plaćanju (samo stranica plaćanja) | Nužni (sigurnost) | 1 godina / 30 min | Ne (VERIFY) |
| [plausible / umami]: nema kolačića | [self-hosted] | Zbirna statistika posjećenosti | Analitički | – | Da / prema odluci (VERIFY) |
| `_ga`, `_ga_<ID>` | Google Ireland Ltd. | Analitika posjećenosti | Analitički | 2 godine | Da |
| YouTube (nakon klika) | Google Ireland Ltd. | Prikaz videozapisa | Sadržaj treće strane | do 6 mj. | Da (klikom na „Učitaj video”) |

Below the table, include: controller identity and contact; recipients; transfers (EU-SAD DPF); how to withdraw consent; link to the privacy policy (politika privatnosti); AZOP complaint right.

### 7.3 Newsletter consent checkbox (unticked)

> ☐ Želim primati [Naziv] newsletter s novostima, savjetima i ponudama za [proizvod] e-poštom (najviše [2] puta mjesečno). Privolu mogu povući u svakom trenutku poveznicom za odjavu u svakoj poruci. Više u [Politici privatnosti].

Then send a double opt-in email:

> „Potvrdite prijavu na newsletter: [Potvrđujem prijavu]. Ako se niste prijavili, zanemarite ovu poruku.”

### 7.4 Unsubscribe footer (marketing emails)

> Ovu poruku šalje [Tvrtka d.o.o. / Obrt Naziv, vl. Ime Prezime], [adresa], OIB [ ], upisan u [sudski registar Trgovačkog suda u … / Obrtni registar], MBS [ ]. Primate je jer ste [se prijavili na naš newsletter / koristili probno razdoblje usluge [Naziv]].
> **[Odjava jednim klikom]** · [Postavke obavijesti] · Odjavu možete zatražiti i odgovorom na ovu poruku ili na [privatnost@domena.hr]. Odjava je besplatna i provodi se odmah.

### 7.5 Soft opt-in notice at signup (trial registration form)

> Nakon registracije povremeno ćemo Vam slati e-poštom savjete i ponude za [Naziv] i naše srodne usluge. Ako to ne želite, označite kućicu u nastavku. Od tih se poruka možete odjaviti i u svakoj poruci, besplatno i jednim klikom.
> ☐ Ne želim primati savjete i ponude e-poštom.

The notice must be adjacent to the email field, not buried in the ToS. Store the state of the box and the notice version.

### 7.6 Defensible B2B cold email (to a d.o.o. contact)

> **Predmet:** [Konkretna korist] za [Naziv tvrtke]
>
> Poštovani gospodine [Prezime],
>
> javljam se jer se [Naziv tvrtke] bavi [djelatnost primatelja], a razvili smo [Naziv], alat koji [jedna rečenica koristi]. Ako Vas zanima, rado ću Vam pokazati demo od 15 minuta ili otvoriti besplatno probno razdoblje.
>
> Lijep pozdrav,
> [Ime Prezime], [Tvrtka d.o.o.], [adresa], OIB [ ], [telefon]
>
> ---
> *Zašto ste primili ovu poruku i kako se odjaviti:* Vaše poslovne kontaktne podatke (ime, prezime, poslovna e-adresa, funkcija) preuzeli smo s [mrežne stranice Vaše tvrtke / iz sudskog registra] i obrađujemo ih na temelju legitimnog interesa (čl. 6. st. 1. t. (f) GDPR-a) kako bismo Vam ponudili uslugu relevantnu za Vaše poslovanje. Voditelj obrade je [Tvrtka d.o.o.], [kontakt]. Podatke ne dijelimo s trećima osim s pružateljem usluge e-pošte [naziv, EU]. Čuvamo ih najviše [6] mjeseci ako ne odgovorite. **Imate pravo prigovora na ovu obradu u svakom trenutku. Odgovorite „ODJAVA” i više Vas nećemo kontaktirati** (Vaš ćemo kontakt zadržati samo na popisu za blokiranje slanja). Imate i pravo na pristup, ispravak, brisanje i ograničenje obrade te pravo na pritužbu Agenciji za zaštitu osobnih podataka (azop.hr). Više: [poveznica na obavijest].

Rules for using it:
- Only for legal persons, never obrtnici.
- One follow-up maximum.
- No tracking pixel.
- Keep an LIA on file.
- Never send to personal (non-business) addresses.

### 7.7 Decision tree: "Can I send this email?"

```
1. Is it purely transactional/service (account, billing, security, legally required notice,
   neutral trial-status info) with NO promotional content?
   → YES: send (contract/legal basis). No unsubscribe needed. STOP.
   → NO (it promotes anything, incl. upgrades/discounts/newsletter): it's MARKETING → go to 2.

2. Has the recipient given valid, recorded, unticked-box consent for this kind of marketing
   (ideally double opt-in) and not withdrawn it?
   → YES: send with sender ID + one-click opt-out + ZET čl. 7 offer clarity. STOP.
   → NO → 3.

3. Is the recipient a LEGAL PERSON (d.o.o., j.d.o.o., d.d., udruga…) contacted at a business address
   about something relevant to its business?
   → YES: ZEK čl. 50(4) — no ZEK consent needed.
        • Generic address (info@)? → send with sender ID + opt-out.
        • Named person address? → also need GDPR LIA + Art 14 notice in the email + honour objection
          immediately. Check suppression list. STOP.
   → NO (consumer, obrtnik, freelancer, private address) → 4.

4. Did you get their email from them in the context of a sale — incl. paid plan OR free
   trial/free tier of a service that has a paid version (Inteligo)?
   AND was a clear free opt-out offered at signup, which they did not use?
   AND is the email about YOUR OWN SIMILAR product/service?
   AND will it contain a free opt-out?
   AND is the relationship still reasonably recent (e.g., ≤ 12–24 months)?
   → ALL YES: send under soft opt-in (ZEK čl. 50(2)). STOP.
   → ANY NO → 5.

5. DO NOT SEND. Get consent through a non-email channel you lawfully control (website form,
   in-app opt-in). Never "email to ask for consent", never buy lists.

Before any send, also check:
 - Suppression list (unsubscribed/objected) → never send.
 - Discount claims: price really below lowest price of prior 30 days (ZZP čl. 19)? Real deadline (čl. 37 t. 11)?
 - "Free" claims accurate (čl. 37 t. 26)? Auto-renewal disclosed (čl. 36)?
 - Tracking pixels/links only if covered by consent (EDPB 2/2023) — VERIFY.
 - Phone/SMS/WhatsApp to a consumer? → consent, and check Ne zovi register (ZZP čl. 12).
```

---

## 8. Open points marked VERIFY

1. Omnibus timing and final Art 88a/88b text. Council mandate agreed 21 Oct 2026; Parliament position pending.
2. Whether self-hosted cookieless analytics (Plausible/Umami) needs consent under ZEK 43(4). No Croatian exemption exists; EDPB 2/2023 leans "yes".
3. Stripe.js fraud cookies and Sentry / RUM tools as "necessary". There is no Croatian guidance.
4. ZEK 50(2) says "potrošača": does soft opt-in extend to obrtnik or business customers who are natural persons?
5. Whether čl. 19 ZZP's 30-day rule covers personalised coupons.
6. Whether an obrtnik is penalised as "fizička osoba" under ZEK čl. 170. st. 3.
7. ZET čl. 23 euro amounts.
8. Status of the *Latombe* appeal on the EU-US DPF (C-703/25 P, still pending 2026-10-25).
9. Email open-tracking pixels under Art 5(3): enforcement is unsettled.
10. Re-permission emails in Croatia. There is no local precedent; the ICO line suggests they are prohibited.

---

## 9. Sources (primary first)

**Croatian legislation and HAKOM:**
- ZEK consolidated text, NN 76/22, 14/24, 45/26: https://www.zakon.hr/z/182/zakon-o-elektronickim-komunikacijama (čl. 4(15), 43, 50, 51, 161–162, 170, 173–174); original NN 76/22: https://narodne-novine.nn.hr/clanci/sluzbeni/2022_07_76_1116.html
- ZZP consolidated text, NN 19/22, 59/23, 59/26: https://www.zakon.hr/z/193/zakon-o-zastiti-potrosaca (čl. 4, 7, 11, 12, 18, 19, 20, 33–42, 81.a, 149, 150)
- Pravilnik o Registru »NE ZOVI«, NN 117/22: https://narodne-novine.nn.hr/clanci/sluzbeni/full/2022_10_117_1791.html
- HAKOM e-Registar NE ZOVI: https://www.hakom.hr/hr/e-registar-ne-zovi/224; gov.hr: https://gov.hr/hr/e-registar-ne-zovi/562
- ZET consolidated text, NN 173/03 … 67/25: https://www.zakon.hr/z/199/zakon-o-elektronickoj-trgovini (čl. 6, 7, 8, 22, 23)

**AZOP:**
- AZOP, Recommendation on cookies (updated 6 Aug 2024): https://azop.hr/obrada-osobnih-podataka-kolacici/
- AZOP, answer on cookies (14 Aug 2026): https://azop.hr/kolacici-gdpr/
- AZOP, marketing / newsletter opinion (2019): https://azop.hr/obrada-osobnih-podataka-u-svrhe-marketinga/
- AZOP cookie fines 2023 (summary): https://www.notarius.hr/aktualno/u-sredistu/57374; AZOP fines list: https://azop.hr/upravne-novcane-kazne/

**EU:**
- Directive 2002/58/EC (EUR-Lex CELEX 32002L0058), Arts 5(3) and 13
- CJEU C-673/17 Planet49; CJEU C-654/23 Inteligo Media: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:62023CJ0654 (commentary: https://www.twobirds.com/en/insights/2025/understanding-soft-opt-in-when-free-deals-count-as-a-sale-under-eprivacy-rules)
- EDPB Guidelines 2/2023 (final, Oct 2024): https://www.edpb.europa.eu/documents/guideline/guidelines-22023-on-technical-scope-of-art-53-of-eprivacy-directive_en
- EDPB Cookie Banner Taskforce Report (17 Jan 2023): https://www.edpb.europa.eu/system/files/2023-01/edpb_20230118_report_cookie_banner_taskforce_en.pdf
- EDPB-EDPS Joint Opinion 2/2026 on the Digital Omnibus: https://www.edpb.europa.eu/system/files/documents/2026-02/edpb_edps_jointopinion_202602_digitalomnibus_en.pdf
- ePrivacy Regulation withdrawal: https://www.europarl.europa.eu/legislative-train/theme-connected-digital-single-market/file-jd-e-privacy-reform (C/2025/5423, 6 Oct 2025)
- Digital Omnibus status: Heuking, 24 Sept 2026: https://www.heuking.de/en/news-events/newsletter-articles/detail/gdpr-ai-and-cookies-what-the-eus-data-omnibus-could-change-for-companies.html; Renaissance Numérique, 15 Sept 2026: https://www.renaissancenumerique.org/en/publications/synthesis-digital-omnibus-what-implications-for-privacy/; Art 88a/88b content: https://www.taylorwessing.com/zh-hant/global-data-hub/2026/the-digital-omnibus-proposal/gdh---the-digital-omnibus---cookies

**Other:**
- LG München I, 20.01.2022, 3 O 17493/20 (Google Fonts). Cited from known case law; not re-fetched.
- IAB Croatia, Smjernice za bolje influencanje (Nov 2025): https://iab-croatia.com/novo-poglavlje-odgovornog-oglasavanja-objavljene-smjernice-za-bolje-influencanje/