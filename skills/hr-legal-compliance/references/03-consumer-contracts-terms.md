# Croatian consumer protection, e-commerce information duties and T&C/contract law for a software seller (obrt or d.o.o.)

**Status:** researched 2026-10-05 against the consolidated texts on zakon.hr (database updated to NN 105/26 on 26 Sep 2026) and the official texts in Narodne novine; ZZP price-display developments re-checked 2026-10-25. Anything not confirmed against a primary source is marked **VERIFY**. General information, not legal advice. Before going live, have a Croatian lawyer review the final T&C.

---

## 0. Changes since 2025 that matter most

1. **ZZP amended by NN 59/2026** (published 9 Jun 2026, Act of 29 May 2026). It transposes Directive 2023/2673 (distance financial services and the withdrawal function), the Green Transition Directive 2024/825 and the Right-to-Repair Directive 2024/1799. Commencement is staggered (Art 66 of the amending Act):
   - Most provisions: 17 Jun 2026.
   - **Art 81.a "funkcija za jednostrani raskid"** (the withdrawal button) and new Art 60(1)(10): **19 Jun 2026**.
   - New Art 74(1) (order-page information) and Art 60(1)(8),(14),(16)-(19),(27): **27 Sep 2026**.
   - Art 7 price display changes: 17 Nov 2026 (see §1.2a).
   - **All of these are already in force except the Art 7 changes.**
2. **ZOO amended by NN 69/2026** (published 29 Jun 2026). It transposes the new Product Liability Directive 2024/2853. **Software is expressly a "proizvod"** (product). Arts 1073–1080 are rewritten and apply from **9 Dec 2026** to products placed on the market or put into service from that date (transitional Art 21(2)).
3. **The EU ODR platform closed on 20 Jul 2025** (Reg. (EU) 2024/3228 repealed Reg. 524/2013). **Remove every ODR link and ODR clause.**
4. **Zakon o elektroničkoj trgovini amended by NN 67/25** (in force 17 Apr 2025). The hosting/caching/mere-conduit safe harbours (Arts 16–18) and Art 21 are repealed. Those rules now come directly from the **DSA (Reg. 2022/2065), Arts 4–6**.
5. **Dual HRK/EUR price display** was mandatory only until **31 Dec 2023** (Zakon o uvođenju eura; MINGO, HGK). Show EUR only.

---

## 1. Zakon o zaštiti potrošača (ZZP), NN 19/22, 59/23, 59/26

### 1.1 Scope and key definitions (Art 5)
- **"Potrošač"** (consumer): a natural person acting outside their trade, business, craft or profession.
  - A professional buying for their own business is **not** a consumer.
  - A homeowner or student buying privately **is** a consumer.
  - Your checkout should ask "Kupujem kao: fizička osoba (potrošač) / poslovni subjekt" and collect the OIB/VAT number for businesses.
- **"Digitalna usluga"** (digital service): explicitly includes "aplikacije u oblaku" (cloud applications). **Your SaaS is a digital service.**
- **"Maloprodajna cijena"** (retail price): the final price in the official currency (EUR), **including taxes**. B2C prices must be VAT-inclusive.
- **"Trajni medij"** (durable medium): includes email and PDF.

### 1.2 Price display and terms of sale (Arts 7, 8, 19)
- Art 7(1),(7),(9): show the retail price clearly; honour displayed prices; **publish valid price lists on the website**.
- Art 8(1)-(2): display terms of sale (uvjeti prodaje) clearly and comply with them.
- **The Art 19 "lowest price in the last 30 days" rule applies to goods.** For services it applies only "unutar poslovnih prostorija" (on business premises). Art 19(7) [second para. 7, misnumbered in the text] expressly **excludes distance contracts and the advertising of services**.
  - So SaaS coupons and discounts are not subject to the 30-day reference-price rule.
  - They remain subject to the misleading-practice rules (Arts 35–37). Never show a fake "was" price.
- Art 37 item 26: calling something "besplatno/gratis" (free) when the consumer must pay is **always misleading**. A "free trial" that auto-charges must say so prominently.

### 1.2a Reference price ("bazna cijena") and published price lists (from 17 Nov 2026; re-checked 2026-10-25)
- The NN 59/26 changes to Art 7 (price display) apply from **17 Nov 2026**. On that basis the Ministry of Economy
  published two draft rulebooks on 14 Oct 2026 (e-Savjetovanje open until 13 Nov 2026): *Pravilnik o isticanju
  bazne cijene proizvoda* and *Pravilnik o sadržaju i načinu objave cjenika proizvoda* (vlada.gov.hr, 15 Oct 2026).
- Draft content: B2C traders and service providers show, next to the current price, a **bazna cijena** = the price
  on a reference date (**10 Sep 2026** for most goods and **services**; 2 May 2025 for food, drinks, hygiene and
  household products), and publish a **machine-readable price list** (CSV/XML) on their website. The interim
  government decisions ("dodatna" / "sidrena cijena", originally due 1 Oct 2026) were postponed to 17 Nov 2026.
- Draft exemptions include prices personalised to an individual consumer and dynamically set service prices; B2B-only
  sellers are not covered.
- **For SaaS / online subscriptions sold to consumers: VERIFY** whether the final rulebooks cover them (the drafts
  cover "usluge" generally). Low-cost precaution: keep a dated record of public plan prices on 10 Sep 2026 and be
  ready to publish a CSV price list. Check the final texts in Narodne novine before 17 Nov 2026.

### 1.3 Pre-contractual information for distance contracts (Art 60(1), as replaced by NN 59/26)
Give this information "na jasan i razumljiv način" (clearly and comprehensibly), **in Croatian and Latin script** (Art 60(9)). Other languages may be added alongside. The full list relevant to SaaS is in deliverable (a). The 27 points include:
- 1 main characteristics
- 2 name, seat, phone, email, other online means
- 4 complaint address
- 5 price incl. taxes (for subscriptions, see Art 60(3)-(4))
- 6 personalised-pricing notice
- 8 payment, performance and complaint handling
- 9–10 withdrawal conditions, **the model form and the existence and location of the withdrawal function**
- 12 the proportional payment owed if the service started before the withdrawal period ended
- 13 when there is no right of withdrawal or when it is lost
- 15 legal conformity of digital content/services
- 18 minimum period of software updates
- 19 after-sales support
- 20 codes of conduct
- **21 contract duration and termination/auto-renewal conditions**
- **22 minimum term**
- 24 functionality incl. technical protection measures
- 25 compatibility and interoperability
- **26 ADR mechanisms**

Further rules:
- Art 60(3)-(4): for open-ended or subscription contracts, the "total price" means the total per billing period. For fixed fees, it also means the total monthly cost.
- Art 60(6): hidden charges you did not disclose cannot be charged.
- Art 60(2): the information forms part of the contract.
- Art 64: **the trader bears the burden of proof** that the information was given.
- Art 51: **any extra payment needs express consent**. Pre-ticked boxes for add-ons are not allowed, and the consumer can reclaim the money.

### 1.4 Order page and the order button (Art 74, in force from 27 Sep 2026)
- Art 74(1): **immediately before the order**, show clearly and prominently:
  - main characteristics (pt 1)
  - total price (pt 5, plus paras 3–5)
  - durability guarantee (pt 17, N/A for SaaS)
  - **duration and auto-renewal/termination terms (pt 21)**
  - **minimum term (pt 22)**
- Art 74(2)-(3): the button must be labelled **"narudžba s obvezom plaćanja"** (order with obligation to pay) "ili sličnim nedvojbenim izrazom" (or a similar unambiguous phrase).
  - Acceptable: "Naruči i plati", "Pretplati se uz obvezu plaćanja", "Kupi sada".
  - Avoid: "Nastavi", "Registriraj se", "Pokreni probno razdoblje" on a step that commits to payment.
- **Art 74(4): if you breach this, the contract is null and the consumer's order is not binding.**
- Art 75: at the latest when ordering starts, state accepted payment methods and any delivery restrictions, e.g. "usluga dostupna samo u RH/EU".

### 1.5 Confirmation on a durable medium (Art 76)
- Send it within a reasonable time after conclusion, **at the latest when performance starts**.
- It must contain all Art 60(1) information, unless already given on a durable medium.
- It must include **confirmation of the consumer's prior express consent and acknowledgement** for early performance (Art 86(1)(13) / Arts 77, 84).
- Practice: a payment provider's receipt alone is not enough. Send your own email with the T&C PDF, the pre-contract information sheet, the model withdrawal form and a record of the consent given.

### 1.6 Right of withdrawal (jednostrani raskid) for SaaS
- **Period: 14 days** from **contract conclusion** for services and digital content (Art 79(1),(5)).
- **Missing information**: if you fail to inform the consumer per Art 60(1)(9)-(10), the period extends by up to **12 months** (Art 80).

**SaaS is a service, not "digital content".** Two different exceptions exist:

| Exception | ZZP | Applies to | Effect |
|---|---|---|---|
| Services | **Art 86(1)(1)** | **Digital services (SaaS)** | Right lost only when the service is **fully performed** after express prior consent and acknowledgement |
| Digital content not on a tangible medium | **Art 86(1)(13)** | Downloads, e-books, one-off licence keys | Right lost when performance starts, given consent + acknowledgement + Art 76 confirmation |

Consequences for a subscription:
- A monthly or annual subscription is **not "fully performed" within 14 days**. A consumer can therefore **always withdraw within 14 days**.
- If they **expressly asked** you to start during the withdrawal period (Art 77), and you informed them per Art 60(1)(12), they owe a **proportional part of the price** (Art 84(8)). The rest must be refunded.
- If they did not expressly request early start, or you did not inform them, they owe **nothing** (Art 84(9)).
- **So for SaaS you cannot make the consumer "waive" withdrawal outright.** You can only obtain:
  - the express request to start immediately (Art 77(1)), and
  - the acknowledgement that the right is lost once the service is fully performed (Art 77(2)).
  - Combined, these give you the right to keep the pro-rata amount. Sample wording is in deliverable (c).
- **Exact statutory concepts to mirror in the checkbox:**
  - "izričito zahtijevao da pružanje usluge … započne prije isteka roka za jednostrani raskid" (Art 77(1), 84(8))
  - "potvrdu potrošača da je upoznat s činjenicom da će izgubiti pravo na jednostrani raskid ugovora … ako usluga bude ispunjena u potpunosti" (Art 77(2))
  - For digital content (Art 86(1)(13), Art 84(10) as amended): "izričit prethodni pristanak … te … potvrdu da je upoznat s činjenicom da će time izgubiti pravo na jednostrani raskid ugovora".

**How to exercise withdrawal and the refund:**
- Art 81: by the model form or any unambiguous statement. If you accept it online, acknowledge receipt on a durable medium without delay.
- Art 83(1),(4): **refund within 14 days**, using the **same payment method**, at no cost to the consumer.
- Art 83(6)-(9): after withdrawal you may block access, but you must let the consumer **export non-personal content they created, free, in a machine-readable format**.
- Art 84(3): the consumer must stop using the service.

**Free trial converting to paid.** The contract is usually concluded at trial signup if the terms provide automatic conversion. In that case the 14 days can run out during the trial.
- **VERIFY** against the Commission's 2021 CRD Guidance (C/2021/9987) on free trials.
- Best practice, and what inspectors are likely to expect:
  - send a reminder before the first charge
  - make cancellation during the trial one-click
  - voluntarily grant a 14-day refund window from the first paid charge (pro-rata or full)

### 1.7 The withdrawal button (Art 81.a, in force 19 Jun 2026; transposes Dir. 2023/2673 / new CRD Art 11a)
**Status: transposed and in force.** The wording comes from the Croatian text. For a contract concluded "putem mrežnog sučelja" (via an online interface):
1. Provide a withdrawal function **throughout the withdrawal period**, prominently displayed and easily accessible. Label it **"raskid ugovora"** (or an equivalent unambiguous, legible term). (Art 81.a(1)-(2))
2. The function lets the consumer submit or confirm **(1) name, (2) contract details, (3) the email/electronic means for the confirmation**. (Art 81.a(3))
3. Then a confirmation function labelled **"potvrditi raskid ugovora"**. (Art 81.a(4)-(5))
4. Send an **automatic confirmation on a durable medium without delay**, with the content, **date and time** of submission. (Art 81.a(6))
5. Withdrawal is timely if submitted before the period ends. (Art 81.a(7))

Further points:
- Pre-contract information must state the function's **existence and location** (Art 60(1)(10)).
- Not providing it is offence Art 149(1) item 82. It is on the **"no grace" list** in Art 148(4): the inspector must file charges immediately, with no chance to fix first.
- Implementation: a "Raskid ugovora" link in the footer and the account/billing page, accessible without login or with login but trivially reachable. A two-step form, then a timestamped email.

### 1.8 Written complaints (pisani prigovor), Art 10
1. Accept complaints **at business premises, by post and by email**. Other durable channels such as a web form are optional. (para 1-2)
2. **Acknowledge receipt without delay**, in writing. (para 3)
3. **Display how to file a complaint** clearly on the website. (para 4)
4. **Answer in writing within 15 days of receipt**, stating clearly whether the complaint is accepted. (para 6)
5. **Keep a complaint log on a durable medium for 1 year.** (para 7)

Fines and enforcement:
- Breaches are Art 149(1) items 16, 17, 19, 20.
- **Item 19 (no reply in 15 days) is on the no-grace list.**
- The **30-day "reklamacija" regime (Arts 26–27) concerns public services only.** Do not confuse the two.

### 1.9 Alternative dispute resolution (ADR)
- ZZP Art 60(1)(26) requires pre-contract information on "mehanizmima izvansudskog rješavanja sporova" (out-of-court dispute mechanisms).
- **Zakon o alternativnom rješavanju potrošačkih sporova (ZARPS, NN 121/16, 32/19), Art 22:**
  - If you **commit to, or are obliged to use**, an ADR body, you must say so on the website with the body's **postal and web address**.
  - **Art 22(4) (all traders):** if a written complaint cannot be resolved, your reply **must name the competent ADR body(ies)** and state **whether you will participate**.
  - Fines (Art 30): legal person 2,000–5,000 HRK, about **€265–664**. **VERIFY** euro conversion at 7.53450.
- **Croatian notified ADR bodies** (source: szp.hr):
  - **Centar za mirenje pri Hrvatskoj gospodarskoj komori**, Rooseveltov trg 2, 10000 Zagreb, hgk.hr/centar-za-mirenje (HGK also has a "Sud časti")
  - Centar za mirenje pri Hrvatskom uredu za osiguranje (insurance only)
  - Profi Test d.o.o. Centar za mirenje "Medijator", Bjelovar, medijator.com.hr
  - Centar za mirenje pri Hrvatskoj udruzi za medijaciju, Kneza Mislava 12, Zagreb, medijacija.hr
  - **Centar za mirenje Hrvatske obrtničke komore**, Ilica 49/II, Zagreb; plus the **Sud časti HOK** (natural fit for an obrt)
- **ODR:** the platform was discontinued on 20 Jul 2025 (Reg. 2024/3228; ec.europa.eu "consumer-redress" relocation notice). **Delete the ODR link and the ODR sentence.** Leaving a dead mandatory-looking link is harmless legally but looks unmaintained.
- **VERIFY:** a revision of the ADR Directive 2013/11 (2025 package) may bring new duties, e.g. replying within 20 working days whether you will take part. Monitor its Croatian transposition.

### 1.10 Unfair contract terms (Arts 53–59)
- **Definition (Art 53):** a non-negotiated term causing significant imbalance against the consumer contrary to good faith.
- **Indicative grey list (Art 54), items relevant to SaaS:**
  - (1) limiting liability for death or injury
  - (2) limiting consumer rights on non-performance, incl. excluding set-off
  - (6) trader's discretionary termination without the same right for the consumer
  - (7) keeping prepayments for services not provided
  - (8) terminating an indefinite contract without reasonable notice, except for valid reasons
  - **(9) auto-renewal with an unreasonably short opt-out deadline**
  - (10) terms the consumer could not see before contracting
  - **(11) unilateral changes without a valid reason stated in the contract**
  - (12) unilateral change of product characteristics without valid reason
  - **(13) price increases without a right to terminate**
  - (14) trader decides conformity
  - (15) exclusive interpretation right
  - (19) excluding court access, forced arbitration, shifting the burden of proof
- **Other rules:**
  - Art 55: unfairness is determined by a court judgment.
  - Art 56: the price and the main subject matter are not assessed if they are clear and visible.
  - Art 58: ambiguity is construed in the consumer's favour.
  - Art 59: unfair terms are void; the rest of the contract survives.
  - Art 149(1) item 66: using a term already declared unfair by a final judgment is an offence.

### 1.11 Auto-renewal and subscriptions in ZZP
- Disclose duration, auto-renewal and termination conditions (Art 60(1)(21)), the minimum term (pt 22) and the per-period total (Art 60(3)).
- Show them **immediately before the button** (Art 74(1)).
- Art 54(9) on renewal opt-out deadlines; Art 54(13) on price increases.
- **Art 99(2) ("cancelling must not be harder than signing up") and the dark-pattern ban in Art 99(1) sit in the financial-services chapter** (Poglavlje II). For SaaS they are persuasive, not directly applicable (**VERIFY** scope).
  - Equivalent non-financial bases: the unfair-practice rules (Arts 32–40), the **DSA Art 25** dark-pattern ban (online platforms only), and Art 81.a.
- Art 16(1): **charging consumers for payment reminders ("opomena") is prohibited.**

### 1.12 Fines and enforcement (NN 59/26 versions of Arts 148–150)
**Art 149 (general):**
- Trader that is a legal person (d.o.o.): **€1,500–50,000**
- Responsible person (director): **€1,500–2,500**
- **Trader that is a natural person (obrtnik): €750–2,500**

**Art 150 (Omnibus, widespread or EU-dimension infringements)** covers items 56–57, 62–72 and 74–100, which include the pre-contract information, button, confirmation, withdrawal-function and refund items:
- **0.5–4 % of annual turnover**, or €150,000–2,000,000 if turnover data is unavailable.
- Applies where consumers in ≥2 other Member States are harmed. A higher tier applies for EU-wide harm.
- For a natural-person trader: 0.1–4 % of turnover.

**Art 148 opportunity principle:** normally you can avoid a fine by fixing the problem during the inspection. **Except** for items listed in Art 148(4), which include:
- **19** (no complaint answer in 15 days)
- **71** (no contract copy/confirmation for off-premises contracts)
- **80** (no confirmation on durable medium)
- **82** (no withdrawal function)
- **83** (refund not made)
- Art 150 cases
- **any repeat within 12 months**

For these, a misdemeanour charge must be filed within 15 days.

**Arts 145–146:** for persistent online breaches, the inspector can order **takedown or domain deletion**.

**Supervisor:** tržišna inspekcija (market inspection), **Državni inspektorat**, Sektor za nadzor trgovine, usluga i zaštite potrošača, Šubićeva 29, Zagreb.

---

## 2. Digital content and services: Zakon o određenim aspektima ugovora o isporuci digitalnog sadržaja i digitalnih usluga (NN 110/21; in force 1 Jan 2022; transposes Dir. 2019/770)

**Article numbering differs from the Directive.** Mapping: Directive Art 19 = HR Art 20; Directive Art 16 = HR Art 17.

| Topic | HR article | Rule |
|---|---|---|
| Scope | 5 | Consumer pays a price **or provides personal data**. Excluded if data is used only to supply the service or meet legal duties. So a **free plan funded by marketing use of data is covered**. |
| Supply | 6 | Without undue delay; supplied when made available. |
| Subjective conformity | 8 | Description, functionality, compatibility, interoperability, instructions, support and **updates as agreed**. |
| Objective conformity | 9 | Fit for normal purposes, **taking account of technical standards** (e.g. the industry standards or regulations the product claims to follow); qualities reasonably expected incl. **public statements and advertising**; matches the **trial/preview version** (9(1)(d)); **trader must supply necessary updates incl. security updates** (9(2)). |
| Incorrect integration | 10 | Your responsibility if caused by your instructions. |
| Liability period | 12(5) | For continuous supply: any non-conformity appearing **during the subscription**. |
| Burden of proof | 13(3) | **On the trader** for the whole continuous-supply period. Shifts to the consumer only if their environment is incompatible with requirements you disclosed in advance, or they refuse reasonable cooperation (13(4)-(7)). **Publish minimum browser and system requirements before contracting.** |
| Failure to supply | 14 | Demand supply, then terminate; immediate termination in certain cases. |
| Remedies | 15–16 | Bring into conformity free and in reasonable time; otherwise price reduction (pro-rata per affected period) or termination (not for minor defects; trader proves minority). |
| After termination | 17 | Refund the pro-rata unused prepaid part. GDPR applies to personal data. **Do not use the consumer's non-personal content** (except in 4 cases). **Provide it free, in a machine-readable format, within a reasonable time.** You may block access afterwards. |
| Refund timing | 19 | **14 days**, same payment method, no fee. |
| **Modifications** | **20** | For continuous supply you may change the service beyond what conformity needs only if: (a) **the contract allows it and states a valid reason**; (b) no extra cost; (c) clear information. If the change **negatively affects** access or use (more than minor), you must notify on a **durable medium in reasonable time beforehand**, and the consumer may **terminate free within 30 days**, unless you let them keep the unmodified version. |
| Mandatory nature | 22 | Derogations to the consumer's detriment are not binding. |
| Enforcement | 23, 25 | Market inspection. Fines: legal person 10,000–100,000 HRK (about **€1,327–13,272**); responsible person 10,000–15,000 HRK; obrtnik 5,000–15,000 HRK (about €664–1,991). **VERIFY** euro conversion. |

**T&C implication:** include a "Promjene usluge" (changes to the service) clause listing valid reasons, such as:
- security
- legal or regulatory change, e.g. a new regulation or standard the product implements
- technical evolution of the platform
- removal of rarely used features with equivalent replacement
- third-party dependency changes

Also include the notice and termination mechanics. B2B customers fall outside this Act; ZOO and the contract govern them.

---

## 3. Zakon o elektroničkoj trgovini (ZET), NN 173/03, 67/08, 36/09, 130/11, 30/14, 32/19, 67/25

| Art | Duty |
|---|---|
| **6(1)** | Info "neposredno i stalno dostupne" (directly and permanently available) to users and authorities: **name/business name; seat of the obrt or legal entity; contact details for fast direct contact incl. email; court or other public register number and register details; competent supervisory authority if the activity is licensed; for regulated professions: professional body, title, rules; VAT number if a VAT payer**. |
| **6(2)** | Prices clear; state whether **taxes**, delivery and other costs are included. Applies **also to B2B**, so ex-VAT prices must be labelled "+ PDV". |
| 7 | Commercial communications identifiable. **Promo offers and discounts clearly identified, with easily accessible conditions** (relevant to coupons). |
| 8 | Unsolicited email needs prior consent. The Zakon o elektroničkim komunikacijama has a soft opt-in for existing customers (**VERIFY** current article in ZEK NN 76/22). |
| **12(1)-(2)** | Before contracting, give: **the technical steps to conclude the contract; contract terms; general terms if part of the contract; languages offered; codes of conduct**. Provide **means to identify and correct input errors** (a review page before submit). Derogation possible only B2B. |
| **13** | Contract terms and T&C must be available so the user can **store and reproduce them** (downloadable PDF). |
| **14** | **Acknowledge receipt of the order electronically without delay**, by separate message. B2B may derogate. |
| 15 | Contract concluded when the offeror receives the acceptance. Messages count as received when accessible. Cannot be excluded for consumers. |
| 16–18, 21 | **Repealed (NN 67/25).** Intermediary liability is now under **DSA Arts 4–6**. |
| 19 | Liability for hyperlinks: none unless you know of illegality and fail to remove. |
| 23 | Fines (still in HRK): legal person 5,000–100,000 HRK (about **€664–13,272**); responsible person or natural-person provider 1,000–10,000 HRK (about €133–1,327). Ban of 3–6 months for serious or repeat breaches. Supervisor: market inspection (Art 22). |

**DSA overlay.** Storing users' projects at their request makes you a **hosting service** under DSA Art 3(g). Hosting duties apply regardless of size:
- single points of contact (Arts 11–12)
- **T&C must describe content restrictions and moderation** (Art 14)
- **notice-and-action mechanism** (Art 16)
- **statement of reasons** when you suspend or remove (Art 17)

The SME exemption (Art 19) covers only the online-platform section. Croatia's Digital Services Coordinator is HAKOM (**VERIFY**).

---

## 4. Company-law website disclosures

### 4.1 d.o.o.: Zakon o trgovačkim društvima Art 21 (NN 111/93 … 2024 consolidated)
- **Art 21(4):** business papers **"Isto vrijedi i za sadržaj internetske stranice društva"** ("the same applies to the company's website"). They must show:
  - **tvrtka** (full registered name, exactly as registered, Art 21(1))
  - **sjedište** (seat)
  - **the register court and registration number (MBS)**
  - **the name and seat of the bank(s) holding its accounts and the account numbers (IBAN)**
- **Art 21(5), companies with share capital (d.o.o.), additionally:**
  1. **share capital amount and whether fully paid in** (if not, how much is unpaid)
  2. **surname and at least one first name of each management board member (član uprave / direktor)**
- A foreign-language name may be used only together with the Croatian name (Art 21(2)).
- **OIB** comes from ZET Art 6 (register data) and tax practice. **VAT ID (HR + OIB)** is required by ZET Art 6 if VAT-registered.

### 4.2 Obrt: Zakon o obrtu (NN 143/13, 127/19, 41/20)
- **Art 19(2):** the obrt's "tvrtka" contains **the obrt's name, the designation "obrt", the owner's first and last name, and the seat**.
- **Art 19(6):** ZTD rules on business names apply mutatis mutandis. So the **ZTD Art 21(4) website content applies by analogy**: name, seat, register (Obrtni registar, competent administrative office) and registration number (MBO), bank and IBAN. **VERIFY** whether inspectors enforce the bank detail for an obrt. Including it is low-cost.
- From ZET Art 6:
  - **OIB**, plus VAT ID if in the VAT system
  - if under the flat-rate (paušal) regime and outside VAT, state "obveznik nije u sustavu PDV-a" (not in the VAT system)
  - invoices must carry the VAT-exemption note, **VERIFY** wording under Zakon o PDV-u Art 90
  - membership of HOK is compulsory but is not a "regulated profession" disclosure
- **Regulated profession:** a software business itself is usually not regulated. Do **not** present the company as a regulated professional (e.g. "ovlašteni inženjer", "porezni savjetnik", "odvjetnik") unless it is registered as one with the competent chamber.

---

## 5. T&C under the Zakon o obveznim odnosima (ZOO, NN 35/05 … 155/23, 69/26)

### 5.1 General terms (opći uvjeti ugovora)
- **Art 295:** general terms supplement the contract; **specific terms prevail** over them; they **must be published in the usual way**; they bind the other party **only if known or required to be known at conclusion**.
  - Practice: a link plus a mandatory, non-pre-ticked "Pročitao/la sam i prihvaćam Opće uvjete" checkbox; store version number and timestamp; send the PDF in the confirmation (ZET Art 13, ZZP Art 76).
- **Art 296:** general-term provisions are **void** if, contrary to good faith, they cause **"očiglednu neravnopravnost"** (obvious imbalance) or endanger the contract's purpose.
  - **This applies to B2B too.**
  - Exceptions: terms taken from legislation, individually negotiated terms, and clear core price/subject terms.

### 5.2 Limitation and exclusion of liability
- **Art 345(1):** liability for **intent or gross negligence (namjera, krajnja nepažnja)** cannot be excluded or limited in advance, **B2B or B2C**.
- **Art 345(2):** a court may annul exclusions for **ordinary negligence** if they stem from a monopoly or **unequal bargaining position**. This is a risk against consumers and small firms.
- **Art 345(3):** a **maximum compensation cap is valid** if **not obviously disproportionate to the damage**.
- **Art 345(4):** the cap falls away for intent or gross negligence.
- Art 346: compensation covers foreseeable damage and lost profit; full damage for fraud, intent or gross negligence. Art 347: contributory fault reduces compensation. Art 346(4): duty to mitigate.
- **Consumers:** ZZP Art 54(1)-(2). Death or injury exclusions and limits on the consumer's remedies are presumptively unfair. The DSD Act remedies (Arts 14–17) are mandatory (Art 22).
- **Product liability (from 9 Dec 2026):** **ZOO Art 1079** makes any advance exclusion or limitation **void**.

### 5.3 Contractual penalty (ugovorna kazna)
**Art 350(3): cannot be agreed for monetary obligations.** You cannot impose a "late payment penalty" on fees. Use statutory default interest (zatezne kamate) instead.

### 5.4 Limitation periods (zastara)
| Claim | Period | Art |
|---|---|---|
| General | 5 years | 225 |
| **B2B mutual claims from commercial contracts for goods and services** (e.g. SaaS fees between firms) | **3 years**, running separately per supply | 228 |
| Periodic payments (arguably monthly consumer fees) | 3 years from each due date | 226 (**VERIFY** characterisation; otherwise 5 years under 225) |
| Damages (non-contractual) | 3 years subjective / 5 years objective | 230(1)-(2) |
| Damages for breach of contract | Same as the breached obligation | 230(3) |
| One-year period | Household utilities, telecoms, periodicals only. **Not SaaS.** | 232 |
| Product liability (new) | 3 years from knowledge; extinguished after 10 years (25 for latent injury) | 1080 |

### 5.5 Unilateral changes to T&C
- ZOO has no general right to change terms unilaterally.
- **B2C:** ZZP Art 54(11),(13) and DSD Act Art 20. Changes need a valid reason stated in the contract, advance notice on a durable medium, and a right to terminate without cost before the change takes effect.
- **B2B:** prior notice (e.g. 30 days) plus a right to terminate is customary and survives Art 296.
- **Price increases:** apply at the next renewal, with ≥30 days' notice and free cancellation. For annual plans, honour the price for the paid period.

### 5.6 Termination of indefinite relationships
**Art 212:** either party may terminate by notice, not at an inappropriate time; notice period as agreed or reasonable. Monthly plans: terminate effective at the end of the current billing period.

### 5.7 Governing law and jurisdiction
- **B2C, Rome I Art 6:** you may choose Croatian law, but a consumer in another EU state where you "direct" activities keeps the **mandatory protections of their habitual residence**.
  - The clause must say so. CJEU C-191/15 (Amazon) holds that a bare choice-of-law clause without this caveat is misleading and unfair.
- **B2C, Brussels Ia Arts 17–19:** the consumer may sue at home. **You must sue the consumer at their domicile.** A jurisdiction clause binds the consumer only if agreed after the dispute arose or if it adds options for the consumer. **You cannot force consumers to a Zagreb court.** ZZP Art 54(19) adds that compulsory arbitration is unfair.
- **B2B:** choice of court (Brussels Ia Art 25; for domestic cases ZPP Art 70, **VERIFY**) and choice of law (Rome I Art 3) are allowed. E.g. "Trgovački sud u Zagrebu" or the court of your seat.

### 5.8 Language
- **ZZP Art 60(9)** (as amended): distance-contract pre-contract information must be **in Croatian and Latin script**; other languages may be added. This also covers the confirmation (Art 76(2)).
- **Zakon o hrvatskom jeziku (NN 14/2024), Art 11(3)-(5):** Croatian is "sredstvo obavješćivanja javnosti i potrošača o proizvodima i uslugama na tržištu u Hrvatskoj" (the means of informing the public and consumers about products and services on the Croatian market). Public notices and **promotional messages must be in Croatian**. Multilingual ones go **Croatian first**.
  - No specific misdemeanour provision was found in that Act. Enforcement goes through ZZP.
- **B2B contracts** may be in English. For domestic customers, a Croatian version is prudent.

---

## 6. Professional-reliance disclaimers for calculation, reporting and advice-like software

Applies to any product whose output users rely on professionally or personally: technical calculators, tax or
accounting helpers, legal-document generators, health tools, financial tools, AI assistants.

### 6.1 How far a disclaimer works
- A disclaimer **cannot exclude** liability for intent or gross negligence (ZOO 345(1)), product-liability damage
  (ZOO 1079, from 9 Dec 2026), or the consumer's statutory conformity remedies (DSD Act Art 22; ZZP 54).
- It **can**:
  1. **Define the service** (subjective conformity, DSD Act Art 8 / ZOO). Say what the tool does (which rules,
     standards, versions and assumptions it applies) and that it does not replace the judgement of a qualified
     professional. Courts assess conformity against what was promised, so precise scope statements are the
     strongest tool.
  2. **Allocate responsibility.** Where a regulated professional signs the final document (e.g. a licensed engineer
     or authorised person under construction law, a certified accountant, a lawyer, a doctor), a clause that the user
     remains responsible for verifying inputs and outputs and for what they sign reflects the legal reality. It
     supports contributory-fault arguments (ZOO 347).
  3. **Cap damages for ordinary negligence (B2B)** at a level **not obviously disproportionate** (ZOO 345(3)). A
     common market cap is fees paid in the last 12 months.
     - Add an exclusion of indirect or consequential loss (lost profit, rework costs, third-party claims) for
       ordinary negligence only.
     - **Risk:** with very low fees (e.g. €20/month) and potential damage in the thousands, a court may find the cap
       "u očitom nerazmjeru" (obviously disproportionate). Consider a floor such as "the greater of fees paid in 12
       months or €X". **VERIFY with counsel.**
  4. **For consumers:** keep the "tool, not advice" scope statement. **Do not** cap consumer remedies under the DSD
     Act. A cap on consequential damages for ordinary negligence is grey-list territory (ZZP 54(2)) and may be
     struck. Draft it "u mjeri dopuštenoj prisilnim propisima" (to the extent permitted by mandatory law).
- **Show it where the result is shown** (in the tool, at each result and in exported reports), not only in the
  terms. A disclaimer never cures a misleading headline claim (`05` §11).

### 6.2 Product liability
- **Until 8 Dec 2026:** old ZOO 1073–1080 (strict liability for "dangerous products"). Whether software is covered
  is unclear.
- **From 9 Dec 2026 (NN 69/2026):**
  - "Proizvod" (product) includes **software** (Art 1072-definitions).
  - The manufacturer (developer) is **strictly liable** for defective products (1073).
  - Recoverable damage: **death or injury, medically recognised psychological harm, damage to non-business
    property, and destruction or corruption of data not used for professional purposes**. Business-use property
    and data are excluded (1073(2)).
  - Defectiveness considers **updates, self-learning, cybersecurity** (1075). **No exemption for defects caused by
    software updates or missing security updates** while under the manufacturer's control (1078(2)).
  - Disclosure of evidence and presumptions (1074–1074.a). **No contractual exclusion** (1079). Limitation periods in
    1080.
  - Free open-source software outside commercial activity is excluded (1073(5)).
- **Practical exposure for a B2B calculation or reporting tool:**
  - **Pure economic loss is NOT covered**, e.g. a professional's rework cost or a client's claim over a wrong
    result. That stays in contract and tort under ZOO.
  - Exposure arises mainly where an error contributes to **physical or health harm** (e.g. a design error causing
    damage to a private home, an unsafe health recommendation, a wrong dosage) or **corrupts consumers' private
    data**.
  - Keep **version control, a changelog and documentation of validation**. Under the new evidence-disclosure rules
    you may be ordered to produce them.
  - Check **insurance**: professional indemnity / tech E&O plus product liability.

### 6.3 Recommended structure (B2B-focused, consumer-safe)
1. Nature of the service: a tool, not professional, legal, tax, medical or engineering advice.
2. Methodology: the rules, standards and versions applied, published per release.
3. User obligations: correct inputs; independent verification; professional sign-off where required; keep exports.
4. Known limitations, and the duty to report suspected errors.
5. Our obligations: reasonable care; corrections and updates; notice of material errors found in earlier versions
   (good practice; reduces product-liability "presentation" risk).
6. Liability cap for ordinary negligence: the greater of 12 months' fees or €X. No limit for intent, gross
   negligence, death/injury, product liability or mandatory consumer rights.
7. Exclusion of indirect loss: B2B only, ordinary negligence only.
8. Consumer carve-out: "Ništa u ovim Uvjetima ne ograničava prava potrošača prema prisilnim propisima." (Nothing in
   these Terms limits consumers' rights under mandatory law.)

Sample Croatian wording is in deliverable (c).

---

## 7. Subscription mechanics

| Topic | Rule / recommendation | Basis |
|---|---|---|
| **Free trial to paid** | Before signup: state "besplatno X dana, zatim €Y/mj. (s PDV-om) dok ne otkažete" (free for X days, then €Y/month incl. VAT until you cancel), the conversion date, how to cancel, minimum term. Not "besplatno" without a qualifier. **Send a reminder ~3–7 days before the first charge** (best practice; national regulators expect it, **VERIFY**). The button at conversion signup must make the payment obligation clear. | ZZP 37 item 26, 60(1)(5),(21),(22), 74 |
| **Easy cancellation** | Withdrawal function during the 14 days (81.a). Self-service cancel in the account at any time, at least as easy as signup. Effective at end of period. Confirmation email. | ZZP 81.a; 99 by analogy; 54(8),(9) |
| **Price increases** | ≥30 days' notice on a durable medium, effective from next renewal, free cancellation before. Never mid-period on prepaid annual plans. | ZZP 54(13); DSD Act 20; ZOO 296 |
| **Refunds** | Withdrawal: pro-rata if early start was requested and acknowledged, otherwise full; within 14 days; same method. Non-conformity: pro-rata reduction or termination with refund of the unused prepaid part. Voluntary policy beyond that is yours, but state it. | ZZP 83, 84(8)-(10); DSD Act 15, 17, 19 |
| **Prepaid and non-performance** | If you fail to perform, refund prepayment plus default interest within **7 days** of termination. | ZZP 14(2) |
| **VAT display** | B2C: VAT-inclusive EUR price as the headline. B2B: ex-VAT allowed but labelled "+ PDV (25 %)". If an obrt is outside VAT, say "PDV nije obračunat" (**VERIFY** invoice wording). Cross-border B2C e-services: VAT of the customer's Member State above the €10,000 EU threshold, via **OSS**; reverse charge for EU B2B with a valid VAT ID (**VERIFY with an accountant**). Stripe Tax can compute. | ZZP 5(14), 7; ZET 6(2); Zakon o PDV-u |
| **Prorations (up/downgrade)** | Disclose the method, e.g. payment-provider proration on upgrade with immediate charge of the difference, and downgrade at period end. Undisclosed charges are not owed. | ZZP 60(5)-(6) |
| **Coupons** | State conditions clearly and accessibly: validity, eligible plans, first-period-only vs recurring, non-combinable, the price after the discount ends. Show the price after expiry before the button. The 30-day reference-price rule does not apply to distance services (Art 19(7)), but false "was" prices are misleading. | ZET 7; ZZP 35–37, 19(7) |
| **Dunning and suspension** | Retry schedule and grace period, e.g. 3 retries over 14 days, then read-only, then suspension. **No fee for reminders to consumers.** Suspension must be proportionate and notified. Data must not be deleted immediately. B2B: statutory default interest; the €40 recovery lump sum under Zakon o financijskom poslovanju i predstečajnoj nagodbi (**VERIFY** article). | ZZP 16(1); ZOO 29; ZZP 54(8) |
| **Data after termination** | Consumers: export of non-personal content **free, machine-readable, in a reasonable time** (DSD Act 17(5)-(6); ZZP 83(7)-(8)). Recommended: a 30–90-day read-only or export window, then deletion per the privacy policy (GDPR Art 17/20; outside this brief's scope). B2B: contractual, e.g. 30 days. Also the EU Data Act 2023/2854 switching rules for data-processing services (in force since 12 Sep 2025): switching notice of at most 2 months, ≥30-day transition, ≥30-day data retrieval, and from **12 Jan 2027 no switching charges**. **VERIFY** whether your SaaS is a "data processing service" (likely yes: SaaS is expressly included). | DSD Act 17; Data Act Arts 23–31 |

---

## 8. Geo-blocking Regulation (EU) 2018/302 (HR enforcement: Zakon o provedbi Uredbe 2018/302, NN 25/2019)
- **Art 4(1)(b):** you must not apply different general conditions of access based on nationality or residence to customers seeking **electronically supplied services** other than copyright-content access services. **SaaS is squarely in scope.** A consumer from Slovenia must be able to buy on the same terms as a Croatian one.
- **Art 4(2): exemption for traders under the VAT small-business scheme** (Title XII Ch. 1 of the VAT Directive). An **obrt outside the VAT system** (small-business exemption, currently a €60,000 threshold in HR, **VERIFY**) may restrict its sales to Croatia.
- **Art 3:** no blocking or automatic redirection of the website without consent.
- **Art 5:** no payment-method discrimination by issuer country within the accepted methods.
- **Selling only to Croatia:** you may target only Croatia (Croatian language, features built on Croatian regulations) and need not translate or advertise elsewhere.
  - If an EU customer actively wants to buy, you must not refuse on residence grounds unless exempt under Art 4(2).
  - **Objective differences are allowed.** A product legitimately designed for the Croatian regulatory framework may say so in the description, e.g. "Izračuni prema hrvatskim propisima".
  - Art 1(6) and recital 13: you need not comply with the destination country's non-contractual product rules.
- B2B buyers purchasing for **resale** are out of scope. Business end-users are protected.
- Fines under the HR implementing law: **VERIFY** amounts.

---

## 9. Accounts and acceptable use
- **Your IP:** software, algorithms, UI and documentation are protected under Zakon o autorskom pravu i srodnim pravima (NN 111/21) as a computer program. Grant a **non-exclusive, non-transferable licence for the subscription term**, limited to the purchased seats.
- **User content and projects:**
  - The user keeps all rights to input data and outputs: projects, reports, files, imports.
  - You take a **limited licence to host, process, back up and display them solely to provide the service**.
  - Separately and opt-in, anonymised or aggregated statistics for service improvement. For consumers, using their content beyond the service triggers DSD Act Art 5(2) and GDPR.
- **Account sharing:** licences per named user; credential sharing prohibited; you may detect it and, after warning, suspend or require extra seats.
  - Proportionality applies. For consumers, discretionary termination is grey-list (ZZP 54(6)-(8)). Spell out concrete grounds and give notice except for serious breach.
- **Suspension and termination for breach:** list specific grounds such as non-payment, security threat, illegal content, reverse engineering beyond Art 40 ZAPSP exceptions (**VERIFY** article), resale, or abusive load.
  - Under the DSA, give a **statement of reasons** (Art 17) and provide a notice mechanism (Art 16).
  - On termination, allow data export (§7).
- **Acceptable use:** no illegal content, no malware, no scraping or automated access beyond the API, no benchmarking for competitive purposes (B2B only; questionable vs consumers), no circumvention of licence limits.

---

## 10. Platform-to-Business Regulation (EU) 2019/1150
- It applies only to **online intermediation services and search engines** that let business users offer goods or services **to consumers**.
- A SaaS tool that professionals use for their own work is **not an intermediation service**. **P2B does not apply.**
- It would apply only if you added a marketplace, e.g. a "find a provider" directory through which consumers contract the listed businesses. In that case, re-assess both P2B and ZZP Art 61 (online marketplace information duties).

---

# DELIVERABLES

## (a) Pre-contractual information checklist for B2C SaaS (ZZP Art 60(1); ZET Arts 6, 12)
All items in Croatian; on the site before the order and repeated on a durable medium after it.

**Identity and contact**
- [ ] Business name, seat, address for complaints (if different), phone, email and other durable online channels (60(1)(2),(4); ZET 6)
- [ ] Register and number (MBS / Obrtni registar), OIB, VAT ID or "nije u sustavu PDV-a" (ZET 6)

**Product**
- [ ] Main characteristics: plans, features, limits (seats, projects), any standards or regulations the product claims to follow, supported browsers and system requirements (60(1)(1),(24),(25); DSD Act 13(4))
- [ ] Functionality, compatibility and interoperability (import/export formats) and any technical protection (60(1)(24),(25))
- [ ] Minimum period of software updates, or "for the duration of the subscription" (60(1)(18))
- [ ] Support and after-sales service, and its terms (60(1)(19))
- [ ] Statement of legal conformity liability for digital services (60(1)(15))
- [ ] Codes of conduct, if any, or "none" (60(1)(20); ZET 12)

**Price and payment**
- [ ] Price incl. VAT, in EUR, **per billing period**, plus monthly total for fixed fees (60(1)(5), (3)-(4))
- [ ] Price after any trial or coupon ends
- [ ] Notice if the price is personalised by automated decision-making (60(1)(6))
- [ ] Payment terms and accepted methods (e.g. cards via a payment provider) (60(1)(8); 75)
- [ ] When the service starts (immediately after payment / at trial start) (60(1)(8))

**Contract term**
- [ ] Duration, **auto-renewal**, how and when to cancel (60(1)(21))
- [ ] Minimum term (60(1)(22))
- [ ] Any deposit (N/A) (60(1)(23))

**Withdrawal**
- [ ] 14-day withdrawal right: conditions, deadline, procedure (60(1)(9))
- [ ] **Model withdrawal form, and the existence and location of the "Raskid ugovora" function** (60(1)(10))
- [ ] Proportional payment if immediate start is requested (60(1)(12))
- [ ] When the right is lost: service fully performed (60(1)(13))

**Complaints and disputes**
- [ ] Complaint handling: channels, 15-day answer (60(1)(8); 10(4))
- [ ] ADR body (name, postal and web address) and whether you will participate (60(1)(26); ZARPS 22). No ODR link.

**Contracting process (ZET 12)**
- [ ] Technical steps to conclude the contract
- [ ] T&C downloadable and storable (ZET 13)
- [ ] Contract languages
- [ ] Input error correction (a review page)

**Immediately next to the order button (74(1))**
- [ ] Characteristics, total price, duration and auto-renewal, minimum term
- [ ] Button text "Naruči s obvezom plaćanja" (74(3))

**After the order**
- [ ] Immediate order acknowledgement (ZET 14)
- [ ] Confirmation on a durable medium with all of the above plus the consent record (ZZP 76)

---

## (b) Terms of Service skeleton ("Opći uvjeti korištenja i prodaje")

0. **Uvod i podaci o pružatelju** / Introduction and provider identity (impressum data; ZET 6)
1. **Definicije** / Definitions (Korisnik, Potrošač, Poslovni korisnik, Usluga, Pretplata, Sadržaj korisnika)
2. **Prihvaćanje Uvjeta i sklapanje ugovora** / Acceptance and formation (steps, error correction, moment of conclusion, acknowledgement; ZET 12–15; ZOO 295)
3. **Opis Usluge i tehnički zahtjevi** / Service description and system requirements (DSD Act 8, 9, 13)
4. **Korisnički račun** / Account (registration, accuracy, security, named users, no sharing)
5. **Pretplatni planovi, cijene i plaćanje** / Plans, prices, payment (VAT, payment provider, invoices, currency EUR)
6. **Probno razdoblje** / Free trial (duration, conversion, reminder, cancellation)
7. **Kuponi i popusti** / Coupons and discounts
8. **Trajanje, automatsko produljenje i otkaz** / Term, auto-renewal, cancellation (ZOO 212)
9. **Promjena cijena** / Price changes
10. **Pravo potrošača na jednostrani raskid ugovora** / Consumer withdrawal right (+ "Raskid ugovora" function + model form annex)
11. **Neplaćanje, opomene i suspenzija** / Non-payment, dunning, suspension
12. **Usklađenost Usluge, ažuriranja i pravna sredstva** / Conformity, updates, remedies (DSD Act)
13. **Promjene Usluge** / Changes to the Service (DSD Act 20)
14. **Narav rezultata – odgovornost korisnika** / Nature of results: professional-tool disclaimer (only if the product produces calculations, reports or advice-like output)
15. **Odgovornost i ograničenje odgovornosti** / Liability and limitation (ZOO 345; ZOO 1079 carve-out)
16. **Intelektualno vlasništvo i licenca** / IP and licence
17. **Sadržaj korisnika** / User content and licence to process
18. **Prihvatljivo korištenje** / Acceptable use; notice-and-action; statements of reasons (DSA 14, 16, 17)
19. **Raskid zbog povrede i posljedice prestanka ugovora; izvoz podataka** / Termination for breach; data export and deletion (DSD Act 17; Data Act)
20. **Zaštita osobnih podataka** / Privacy (reference to Politika privatnosti)
21. **Pisani prigovori potrošača** / Consumer complaints (ZZP 10)
22. **Izvansudsko rješavanje sporova** / ADR (ZARPS 22)
23. **Mjerodavno pravo i nadležnost** / Governing law and jurisdiction (B2C caveat / B2B choice)
24. **Izmjene Uvjeta** / Amendments to the Terms
25. **Viša sila** / Force majeure
26. **Završne odredbe** / Final provisions (severability, entire agreement, language: the Croatian version prevails; version and date)
- **Prilog 1:** Obrazac za jednostrani raskid ugovora / Model withdrawal form
- **Prilog 2:** Predugovorne obavijesti (sažetak) / Pre-contract information summary

---

## (c) Sample Croatian wording

**c1. Checkbox for immediate start of the service.** Separate, unticked, required for consumers. SaaS = service, so this follows ZZP Arts 77, 84(8), 86(1)(1).
> ☐ Izričito zahtijevam da pružanje Usluge započne odmah, prije isteka roka od 14 dana za jednostrani raskid ugovora. Upoznat/a sam s time da ću, ako jednostrano raskinem ugovor u tom roku, biti dužan/dužna platiti razmjerni dio cijene za razdoblje do raskida te da ću izgubiti pravo na jednostrani raskid ugovora kada Usluga bude u potpunosti ispunjena.

*Variant for one-off digital content* (e.g. a downloadable report pack; ZZP 86(1)(13)):
> ☐ Izričito pristajem da isporuka digitalnog sadržaja započne odmah, prije isteka roka za jednostrani raskid ugovora, i potvrđujem da sam upoznat/a s time da davanjem ovog pristanka gubim pravo na jednostrani raskid ugovora.

**c2. Order button** (ZZP 74(3)):
> **[ Naruči s obvezom plaćanja ]**

(Alternative: **"Pretplati se – obveza plaćanja"**. For a trial converting to paid: **"Započni probno razdoblje – nakon 14 dana naplata €X/mj."** is safer than a plain "Započni besplatno".) Directly above the button:
> Plan PRO – 29,00 EUR mjesečno (uključen PDV 25 %). Pretplata se automatski produljuje svaki mjesec dok je ne otkažete; otkazati možete u bilo kojem trenutku u postavkama računa, s učinkom na kraju tekućeg obračunskog razdoblja. Nema minimalnog trajanja.

**c3. Withdrawal function labels** (ZZP 81.a):
- Link or button: **"Raskid ugovora"**
- Form fields: "Ime i prezime", "Broj narudžbe / e-adresa računa", "E-adresa za potvrdu"
- Confirm button: **"Potvrditi raskid ugovora"**
- Automatic email: "Zaprimili smo Vašu izjavu o raskidu ugovora [sadržaj] dana [DD.MM.GGGG.] u [hh:mm]. …"

**c4. Model withdrawal form** (Prilog 1; matches the CRD Annex I(B) Croatian text; **VERIFY** against the current Pravilnik under ZZP Art 81(6)):
> **OBRAZAC ZA JEDNOSTRANI RASKID UGOVORA**
> (ispunite i pošaljite ovaj obrazac samo ako želite jednostrano raskinuti ugovor)
>
> – Prima: [tvrtka], [adresa], [e-adresa]
> – Ja/Mi (*) ovim izjavljujem/izjavljujemo (*) da jednostrano raskidam/raskidamo (*) ugovor o pružanju sljedeće usluge (*) / isporuci sljedećeg digitalnog sadržaja (*): ____________
> – Naručeno dana (*) / primljeno dana (*): ____________
> – Ime i prezime potrošača: ____________
> – Adresa potrošača: ____________
> – Potpis potrošača (samo ako se obrazac šalje u papirnatom obliku): ____________
> – Datum: ____________
>
> (*) Precrtati nepotrebno.

**c5. Complaint clause** (ZZP 10):
> **Pisani prigovor.** Potrošač može podnijeti pisani prigovor osobno u našem sjedištu ([adresa]), poštom na adresu [adresa] ili elektroničkom poštom na [prigovori@domena.hr]. Primitak prigovora potvrdit ćemo bez odgađanja, a na prigovor ćemo pisano odgovoriti najkasnije u roku od 15 dana od dana zaprimanja, jasno se izjašnjavajući prihvaćamo li njegovu osnovanost. Evidenciju prigovora čuvamo godinu dana.

**c6. ADR clause** (ZARPS 22; no ODR):
> **Izvansudsko rješavanje sporova.** Ako spor ne riješimo putem pisanog prigovora, potrošač može pokrenuti postupak mirenja pred tijelom za alternativno rješavanje potrošačkih sporova: Centar za mirenje Hrvatske obrtničke komore, Ilica 49/II, 10000 Zagreb, www.hok.hr *[ili:* Centar za mirenje pri Hrvatskoj gospodarskoj komori, Rooseveltov trg 2, 10000 Zagreb, www.hgk.hr*]*. Spremni smo sudjelovati u postupku pred navedenim tijelom. Popis svih tijela dostupan je na mrežnim stranicama ministarstva nadležnog za zaštitu potrošača. Pravo potrošača na sudsku zaštitu time nije ograničeno.

(If you will not participate, you must say so instead: "…ne obvezujemo se sudjelovati…". This is legally allowed, but the information duty remains.)

**c7. Liability limitation clause:**
> **Ograničenje odgovornosti.** (1) Za štetu prouzročenu namjerno ili krajnjom nepažnjom, za štetu zbog smrti, tjelesne ozljede ili oštećenja zdravlja, za odgovornost za neispravan proizvod te u drugim slučajevima u kojima je to propisano prisilnim propisima odgovaramo u punom opsegu.
> (2) U ostalim slučajevima, prema Poslovnim korisnicima naša ukupna odgovornost po svim osnovama u vezi s Uslugom ograničena je na iznos veći od: (a) ukupnih naknada koje je Poslovni korisnik platio za Uslugu u 12 mjeseci prije štetnog događaja ili (b) [X] EUR. Prema Poslovnim korisnicima ne odgovaramo za izmaklu korist, gubitak poslova ili ugovora, troškove ponovne izrade projekta ni za neizravnu štetu, osim u slučajevima iz stavka 1.
> (3) Ništa u ovim Uvjetima ne isključuje niti ograničava prava koja Potrošač ima na temelju prisilnih propisa, osobito prava zbog neusklađenosti digitalne usluge.

**c8. Professional-tool results disclaimer** (only for products whose output users rely on; shown in the T&C, at sign-up, next to each result and on exported reports):
> **Narav rezultata.** [Naziv] je programski alat koji [kratak opis: izrađuje izračune / izvješća / prijedloge dokumenata] prema propisima, normama i pretpostavkama navedenima u dokumentaciji za pojedinu verziju. Usluga ne predstavlja [stručno / pravno / porezno / medicinsko / inženjersko] savjetovanje i ne zamjenjuje prosudbu stručne osobe. Rezultati ovise o ulaznim podacima i pretpostavkama koje unosi korisnik. Korisnik je dužan provjeriti ispravnost ulaznih podataka i rezultata prije njihove uporabe; za dokument u koji su rezultati uključeni odgovara osoba koja ga izrađuje i potpisuje u skladu s propisima. Ako uočimo pogrešku u izračunu, obavijestit ćemo korisnike i objaviti ispravak. Ova odredba ne ograničava našu odgovornost iz članka [Ograničenje odgovornosti], stavaka 1. i 3.

Footer on exported reports:
> "Izrađeno alatom [Naziv] v[x.y] ([datum]) prema [propisi / norme / metodologija]. Rezultate provjerava i za njih odgovara osoba koja potpisuje dokument."

---

## (d) Impressum / footer templates

**d.o.o.** (ZTD 21(4)-(5); ZET 6):
> **[TVRTKA d.o.o.]** za [djelatnost] *(puni naziv kako je upisan u sudski registar)*
> Sjedište: [ulica i broj], [poštanski broj] [grad], Hrvatska
> Upisano u sudski registar Trgovačkog suda u [Zagrebu] pod MBS [xxxxxxxxx]
> OIB: [xxxxxxxxxxx] · PDV ID: HR[xxxxxxxxxxx]
> Temeljni kapital: [2.500,00] EUR, uplaćen u cijelosti
> Član uprave / direktor: [Ime Prezime]
> Poslovni račun: IBAN HR[xx xxxx …] kod [Naziv banke d.d., sjedište]
> Kontakt: [e-adresa] · [telefon]
> [Opći uvjeti] · [Politika privatnosti] · [Pisani prigovori] · [Izvansudsko rješavanje sporova] · **[Raskid ugovora]**

**Obrt** (Zakon o obrtu 19; ZTD 21(4) by analogy; ZET 6):
> **[NAZIV], obrt za [djelatnost], vl. [Ime Prezime], [Mjesto]** *(tvrtka obrta kako je upisana)*
> Sjedište: [ulica i broj], [poštanski broj] [grad], Hrvatska
> Upisan u Obrtni registar pri [Gradski ured / Upravni odjel …], MBO [xxxxxxxx]
> OIB: [xxxxxxxxxxx] · *[ako je u sustavu PDV-a:]* PDV ID: HR[xxxxxxxxxxx] · *[ako nije:]* Obveznik nije u sustavu PDV-a
> Poslovni račun: IBAN HR[…] kod [Naziv banke d.d.]
> Kontakt: [e-adresa] · [telefon]
> [Opći uvjeti] · [Politika privatnosti] · [Pisani prigovori] · [Izvansudsko rješavanje sporova] · **[Raskid ugovora]**

---

## (e) Common mistakes the Državni inspektorat penalises, and fine ranges

The DIRH half-year report (Jan–Jun 2025) gives only aggregate figures: 5,762 market inspections, mostly price-control actions. It has no web-shop breakdown. The list below therefore maps typical online-sales failures to the statutory offences. **VERIFY** practice against DIRH annual reports.

| # | Mistake | Provision / offence | Fine (d.o.o. / director / obrtnik) | Fix-to-avoid-fine allowed? |
|---|---|---|---|---|
| 1 | No or incomplete pre-contract information (esp. withdrawal, ADR, auto-renewal); not in Croatian | ZZP 60, 72; 149(1) items 67, 75 | €1,500–50,000 / €1,500–2,500 / €750–2,500; Art 150 turnover-based if cross-border widespread | Yes, during inspection (Art 148(1)) |
| 2 | Button not labelled "narudžba s obvezom plaćanja"; key terms not shown before ordering | ZZP 74; 149(1) items 77–78 | As above; **plus the contract is void** (74(4)) | Yes |
| 3 | No confirmation on a durable medium (or without the consent record) | ZZP 76; 149(1) item 80 | As above | **No** (148(4)) |
| 4 | **No "Raskid ugovora" function** (new since 19 Jun 2026) | ZZP 81.a; 149(1) item 82 | As above | **No** |
| 5 | Refund not made within 14 days / via a different method | ZZP 83; 149(1) items 83–84 | As above | **No** for item 83 |
| 6 | Treating SaaS withdrawal as fully waived; refusing pro-rata refunds | ZZP 84, 86 | Same Art 149 range; inspector can order a refund (Art 144-type measure) | n/a |
| 7 | No complaint channels or notice on the website; **no reply within 15 days**; no complaint log | ZZP 10; 149(1) items 16, 17, **19**, 20 | As above | **No for item 19** |
| 8 | No ADR information, or no ADR statement in the complaint reply | ZARPS 22; ZZP 60(1)(26) | ZARPS: €265–664 / €133–398 (HRK converted, **VERIFY**) plus ZZP item 67 | Yes |
| 9 | Dead ODR link | Not an offence now; housekeeping | – | – |
| 10 | Missing impressum data (OIB, register, share capital, director, IBAN) | ZET 6; ZTD 21 | ZET: €664–13,272 / €133–1,327 (HRK converted, **VERIFY**); ZTD offences (**VERIFY** article) | – |
| 11 | T&C not downloadable or storable; no input-correction step; no order acknowledgement | ZET 12–14 | ZET 23 range | – |
| 12 | Prices without VAT for consumers; B2B prices not marked "+ PDV"; price list not published | ZZP 7(1),(9); ZET 6(2); 149(1) items 2, 9 | ZZP 149 range | Yes |
| 13 | "Besplatno" trial that silently converts to paid | ZZP 37 item 26 (always misleading); 149(1) item 56 (unfair practice; no-grace list) | ZZP 149, or 150 turnover-based | **No** (item 56 on the 148(4) list) |
| 14 | Charging for payment reminders | ZZP 16(1); 149(1) item 27 | ZZP 149 range | Yes |
| 15 | Unilateral service downgrades without DSD Act Art 20 notice and termination right | DSD Act 20; 25(1)(g) | €1,327–13,272 / €1,327–1,991 / €664–1,991 (HRK converted, **VERIFY**) | – |
| 16 | Using a term already declared unfair by a court | ZZP 55; 149(1) item 66 | ZZP 149/150 | – |

Other enforcement tools: interim measures and **website restriction or domain deletion** for persistent online breaches (ZZP 145–146); collective (class) actions by consumer associations (ZZP Part VI and Zakon o predstavničkim tužbama, **VERIFY**).

---

## Items flagged VERIFY (summary)
1. Exact text of the current Pravilnik on the model withdrawal form under ZZP 81(6) (deliverable (c4) uses the CRD Annex I(B) Croatian wording).
2. Commission CRD Guidance (2021) on when the withdrawal period runs for free trials that convert.
3. Scope of ZZP Art 99(2) (cancellation not harder than signup). It sits in the financial-services chapter.
4. Euro equivalents of HRK-denominated fines in ZARPS, ZET and the DSD Act (fixed rate 7.53450).
5. Whether ZTD 21(4) bank-account disclosure is enforced against an obrt.
6. Characterisation of consumer subscription fees for limitation (226 vs 225).
7. The new ADR-Directive revision and its Croatian transposition.
8. VAT/OSS, the small-business threshold, obrt invoice exemption wording, and fiscalisation of card payments. Consult an accountant.
9. Data Act applicability to your SaaS (likely yes) and the 12 Jan 2027 switching-charge ban.
10. DSA Digital Services Coordinator for Croatia (HAKOM) and its guidance for small hosting services.
11. Whether a regulated sector the product serves imposes specific software requirements (check the competent ministry).

## Primary sources consulted
- ZZP consolidated text (NN 19/22, 59/23, 59/26): https://www.zakon.hr/z/193/zakon-o-zastiti-potrosaca
- NN 59/2026 amending Act (commencement, Arts 81.a, 149, 150): https://narodne-novine.nn.hr/clanci/sluzbeni/2026_06_59_728.html
- SZP summary of NN 59/26: https://www.szp.hr/novosti/u-narodnim-novinama-objavljen-zakon-o-izmjenama-i-dopunama-zakona-o-zastiti-potrosaca-nn-59-26
- Zakon o određenim aspektima ugovora o isporuci digitalnog sadržaja i digitalnih usluga (NN 110/21): https://www.zakon.hr/z/2968/
- Zakon o elektroničkoj trgovini (incl. NN 67/25): https://www.zakon.hr/z/199/zakon-o-elektronickoj-trgovini
- Zakon o trgovačkim društvima Art 21: https://www.zakon.hr/z/546/
- Zakon o obrtu Art 19 (NN 143/13, 127/19, 41/20): https://www.zakon.hr/z/297/zakon-o-obrtu
- ZOO consolidated text (to NN 69/26): https://www.zakon.hr/z/75/zakon-o-obveznim-odnosima
- NN 69/2026 ZOO amendment (PLD transposition, 9 Dec 2026): https://narodne-novine.nn.hr/clanci/sluzbeni/2026_06_69_833.html
- ZARPS (NN 121/16, 32/19): https://www.zakon.hr/z/897/
- Croatian ADR bodies list: https://www.szp.hr/imate-potrosacki-spor/alternativno-izvansudsko-rjesavanje-sporova-adr
- ODR discontinuation: https://consumer-redress.ec.europa.eu/site-relocation_en
- Zakon o hrvatskom jeziku NN 14/2024: https://narodne-novine.nn.hr/clanci/sluzbeni/2024_02_14_252.html
- End of dual price display, 31 Dec 2023: https://mingo.gov.hr/vijesti/zapocelo-obvezno-dvojno-iskazivanje-cijena-u-kuni-i-euru/8927 ; https://hgk.hr/nakon-1-sijecnja-prestaje-obveza-dvojnog-iskazivanja-cijena
- Geo-blocking implementing Act NN 25/2019: https://narodne-novine.nn.hr/clanci/sluzbeni/2019_03_25_492.html
- DIRH half-year report 2025: https://dirh.gov.hr/UserDocsImages/pristup_informacijama_izvjesca/POLUGODISNJI-IZVJESTAJ-O-RADU-SIJECANJ-LIPANJ-2025.pdf
- EU texts from memory, not re-fetched (EUR-Lex blocked automated fetch): Reg. 2018/302 Art 4(1)(b),(2); Rome I Art 6; Brussels Ia Arts 17–19, 25; DSA Arts 3, 4–6, 11–17, 25; Reg. 2019/1150 Art 1–2; Data Act Arts 23–31. Re-check article numbers on EUR-Lex before citing them externally.