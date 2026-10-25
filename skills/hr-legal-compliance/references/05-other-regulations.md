# Other EU and Croatian rules that apply to a small Croatian software business

**Status:** researched 2026-10-05; AI Act timeline, Data Act switching charges and Digital Omnibus status re-checked
2026-10-25. **Scope:** everything except GDPR core, cookies and e-marketing, consumer contract law and tax.
**Method:** primary texts from narodne-novine.nn.hr were downloaded and read where marked "[NN text read]". Law-firm
and secondary sources are marked as such. Anything not confirmed is flagged **VERIFY**. General information, not
legal advice.

**Worked example used in this file.** A fictional micro d.o.o. runs a **B2B SaaS for business users**: a pure browser app, fewer than 10 staff, turnover and balance sheet €2M or less, customers mainly professionals buying for
work, but anyone can sign up; AI features optional; no desktop app distributed. The rules generalise to any SaaS,
web app or content site; adapt each conclusion to the real facts.

---

## 0. Executive summary

**Already in force and applying now:**
- **DSA (Digital Services Act)**, for any service that stores user content (a hosting service):
  - points of contact, T&C content, and a notice-and-action mechanism with reasons for any restriction;
  - notification to HAKOM in the e-Pružatelj DSA system (the general deadline was 29 Oct 2025; registering is not a
    condition for operating, but not notifying is a misdemeanour).
- **AI Act**, if any AI feature ships or AI content is published:
  - Art. 4 AI literacy (softened in July 2026);
  - Art. 50 transparency, applicable since 2 Aug 2026.
- **IP compliance**, mainly open-source licence notices for code shipped to browsers.
- **Misleading and comparative advertising rules** (Zakon o nedopuštenom oglašavanju).
- **Croatian language law** for public and promotional messages.
- **Security obligations** under GDPR Art. 32.

**Applies in principle, but a micro SaaS is likely exempt or out of scope:**
- European Accessibility Act: micro service providers are expressly exempt in Croatia, and B2B-only services fall
  outside "e-commerce services".
- NIS2 / Zakon o kibernetičkoj sigurnosti: micro and small entities are excluded by the size cap.
- Data Act cloud switching: a SaaS whose computing is incidental is likely out of scope (Commission FAQ).
- Cyber Resilience Act: pure SaaS is out of scope.

**Coming soon:**
- **AI Act Art. 50(2) machine-readable marking**: by **2 Dec 2026** for generative systems placed on the market
  before 2 Aug 2026 (re-checked 2026-10-25). New Art. 5 bans on systems generating CSAM or non-consensual intimate
  images also apply from 2 Dec 2026.
- **New product liability rules** (PLD transposed into the ZOO, NN 69/26). They apply to products placed on the
  market from **9 Dec 2026**, and software, including SaaS, counts as a product.
- **Data Act switching charges** must be zero from **12 Jan 2027** (only relevant if the service is in scope).
- **Sector rules** the product implements may change (for example a technical regulation or rulebook that is
  replaced on a fixed date) — see §10.

---

## 1. European Accessibility Act: Directive (EU) 2019/882 and Croatian transposition

### Correct Croatian title (verified)
**Zakon o zahtjevima za pristupačnost proizvoda i usluga**, NN 89/2025. It was adopted 6 Jun 2025 and entered into
force 28 Jun 2025 (Art. 38). The name "Zakon o pristupačnosti proizvoda i usluga" is incorrect. [NN text read]

### Scope
Art. 3(2) lists the covered services. The relevant one is **"usluge e-trgovine"** (e-commerce services). Art. 5(25)
defines these as services provided at a distance, via a website or mobile app, electronically, "at the individual
request of a **consumer** with a view to concluding a **consumer contract**."
- A SaaS or online shop selling to consumers is therefore an e-commerce service.
- Pure B2B sales to professionals acting in a professional capacity fall outside.
- If anyone can sign up and pay without stating a business purpose, consumers can effectively contract. In that case
  the sign-up, checkout, identification and payment flows are in scope; the core tool arguably is not, beyond the
  information duties.

### Microenterprise exemption (verified)
- **Art. 4(2):** "Ovaj se Zakon ne primjenjuje na mikro subjekte malog gospodarstva koji pružaju usluge" (the Act does
  not apply to micro undertakings that provide services).
- **Art. 5(18)** defines a micro undertaking as fewer than 10 employees on annual average **and** annual turnover
  **or** total assets of €2M or less, based on the previous year's financial statements.
- **Conclusion:** while the business stays under those thresholds, the Act does not apply to its services at all.
  Re-test every year from the prior-year financial statements.

### If the exemption is ever lost
- Meet the Annex I service requirements. In practice that means **WCAG 2.1 AA via EN 301 549**, which carries a
  presumption of conformity under Art. 18 once harmonised standards are cited.
- Publish the **Annex V information**: an accessibility statement in the T&Cs or an equivalent place, explaining how
  the service meets the requirements. Art. 36 penalises failing to prepare this information.
- A "disproportionate burden" assessment (Art. 17) is possible. It must be documented, and non-micro undertakings
  must notify the authority (Art. 17(8)).
- **Supervisor for e-commerce services:** market inspectors of the **Državni inspektorat** (Art. 25(9)).
- **Penalties for a service provider that is a legal person:** €6,630 to €132,720 (Art. 36). There is an opportunity
  principle (Art. 28): no misdemeanour charge is filed if the defect is fixed during the inspection.

### Public-sector web accessibility
The separate Zakon o pristupačnosti mrežnih stranica i programskih rješenja za pokretne uređaje tijela javnog sektora
(NN 17/19, **VERIFY** the NN number before citing it formally) applies **only to public-sector bodies**. It matters
indirectly when selling to public bodies: procurement specifications must address accessibility (Directive 2014/24
Art. 42), so expect WCAG questions in tenders.

### Practical checklist (voluntary while exempt)
- Keep a record of headcount and turnover in the annual check.
- Do a basic WCAG 2.1 AA pass on the marketing site, sign-up and checkout: contrast, keyboard navigation, labels,
  focus states, alt text.
- Publish a short "Izjava o pristupačnosti" (accessibility statement) as good practice.
- Document known limits (e.g. a complex visual editor that cannot realistically be made fully accessible).

---

## 2. Digital Services Act: Regulation (EU) 2022/2065

### Does a SaaS qualify?
Usually yes, as a hosting service. A "hosting" service stores information provided by, and at the request of, a
recipient (Art. 3(g)(iii)): user projects, uploaded files, generated documents, comments.

### Is it an "online platform"?
Probably not. A platform must disseminate information **to the public** (Art. 3(i), (k)).
- Shared links sent to identified recipients are not "public".
- Blog comments are a "minor and purely ancillary feature", which the Art. 3(i) definition carves out.
- Avoid public, indexable user-content galleries unless intended: they could tip the service into platform status,
  with Art. 20–28 duties. Micro and small enterprises are exempt from most platform duties anyway (Art. 19).
- Marketplaces and public review/listing sites usually **are** online platforms (re-assess fully).

### Obligations for all intermediaries
- **Art. 11:** a single electronic point of contact for authorities. Publish it, with languages, e.g. "dsa@…" in
  Croatian and English.
- **Art. 12:** a single point of contact for users, which must not rely only on automated tools. Publish it.
- **Art. 13:** a legal representative is needed only by providers established outside the EU.
- **Art. 14:** the T&Cs must set out, in clear language, any restrictions on use: content moderation policies and
  procedures (incl. algorithmic tools and human review) and the internal complaint process. Enforcement must be
  diligent and proportionate.
- **Art. 15:** annual transparency reports. **Micro and small enterprises are exempt** (Art. 15(2)) unless a VLOP.

### Obligations for hosting providers (no micro exemption)
- **Art. 16 notice and action:** an easy electronic mechanism to report illegal content, with the required fields
  (reasons, URL, name and e-mail, good-faith statement); acknowledgement; timely, diligent decision; inform the
  notifier. A simple "Prijavi nezakonit sadržaj" form or mailbox with a documented procedure is enough.
- **Art. 17 statement of reasons:** whenever you remove, disable or restrict content, or suspend or terminate an
  account because content is illegal or breaches the T&Cs, give the user a statement of reasons.
- **Art. 18:** notify police or judicial authorities if you become aware of information giving rise to suspicion of
  a criminal offence threatening life or safety.

### Croatian implementation (verified) [NN text read]
- **Implementing act:** Zakon o provedbi Uredbe (EU) 2022/2065 … (Akt o digitalnim uslugama), NN 67/2025, in force
  17 Apr 2025.
- **Digital Services Coordinator:** HAKOM.
- **Art. 23 notification duty:** providers established in Croatia send HAKOM an **"Obavijest o pružanju usluge
  posredovanja"** through the **e-Pružatelj DSA** system. HAKOM set the deadline at 29 Oct 2025. The notice "nije
  uvjet za pružanje usluga", but failing to send it is a misdemeanour (Art. 18(1)(13)). File it if not done.
- **Penalties (Art. 18):** €6,630 to €66,360, or up to 6 % of global annual revenue, whichever is higher; responsible
  person €1,320 to €6,630. They cover DSA Art. 9–17 failures.

### Checklist
1. Notify HAKOM via e-Pružatelj DSA.
2. "DSA / Kontakt" section on the site: authority and user points of contact, languages (hr, en).
3. T&C chapter on acceptable use, moderation, complaints and statements of reasons.
4. A reporting form or mailbox plus an internal procedure that logs every notice and decision.
5. A statement-of-reasons e-mail template for suspensions.

---

## 3. Data Act: Regulation (EU) 2023/2854, applicable from 12 Sep 2025

### Is the SaaS a "data processing service"?
The Art. 2(8) definition requires on-demand, scalable, elastic access to a shared pool of computing resources. The
Commission's Data Act FAQ (as reported by Morrison Foerster, Dec 2025) says a SaaS falls in scope only if the
customer contracts to use configurable, scalable computing resources; it is out of scope where processing is
"incidental or ancillary" to the main functionality.
- A specialised calculation tool sold to professionals is closer to the "functional application" example.
- **Likely out of scope. VERIFY**: treat this as a reasoned position, not settled law. A storage, hosting, database,
  backup or general-purpose platform service is much more likely in scope.

### If in scope: Chapter VI obligations (Art. 23–31)
- **Contract terms (Art. 25):** switch or port data within 30 days after a notice period of at most 2 months; a list
  of exportable data categories; a minimum 30-day retrieval period; erasure afterwards; disclosure of fees.
- **Interoperability (Art. 30):** export in a structured, commonly used, machine-readable format, plus open
  interfaces.
- **Switching charges (Art. 29):** cost-based only until **12 Jan 2027**, then **zero**, including data egress fees
  (re-checked 2026-10-25 against practitioner sources).
- **Pre-contract information (Art. 26)**, and transparency on jurisdiction and safeguards against government access
  to non-personal data (Art. 28, 32).

### Exemptions
- **Art. 31(1):** services mostly custom-built for an individual customer and not offered at broad commercial scale
  are exempt from Art. 23(d), Art. 29 and Art. 30(1) and (3) only.
- **Art. 31(2):** non-production trial or evaluation versions for a limited period are exempt from the whole chapter.
- There is **no general SME exemption** in Chapter VI. The Digital Omnibus proposes relief for SMEs and legacy
  contracts; the Council agreed its mandate on 21 Oct 2026, the Parliament has not — **not law yet**.

### Practical recommendation
- Build a full "export all my data" feature (JSON/ZIP of user content plus generated documents) anyway. It supports
  GDPR Art. 20 and is cheap insurance.
- Record the out-of-scope reasoning in an internal memo.

---

## 4. AI Act: Regulation (EU) 2024/1689, as amended by the Digital Omnibus on AI

### Omnibus status (re-checked 2026-10-25)
- Adopted as **Regulation (EU) 2026/1744**, published in the OJ on 24 Jul 2026, in force 27 Jul 2026.
- **High-risk obligations deferred** to 2 Dec 2027 (Annex III) and 2 Aug 2028 (Annex I).
- **Article 50 was not delayed:**
  - Art. 50(1) chatbot disclosure and Art. 50(4) deepfake / public-interest text apply since **2 Aug 2026**.
  - **Art. 50(2) machine-readable marking of synthetic content:** systems placed on the market from 2 Aug 2026 must
    comply from launch; systems placed **before 2 Aug 2026** have until **2 Dec 2026** (confirmed by several
    practitioner summaries, Oct 2026).
- **New Art. 5 bans** from 2 Dec 2026: AI systems built to generate child sexual abuse material or non-consensual
  intimate images of identifiable people.
- **Art. 4 AI literacy softened:** providers and deployers must "take measures to support" sufficient AI literacy
  of staff, rather than "ensure" it.
- The Commission's **Art. 50 guidelines** were adopted 20 Jul 2026; the **Code of Practice on transparency of
  AI-generated content** was finalised 10 Jun 2026 (voluntary; signatories are presumed compliant if they follow it).
- **Croatian supervisor for Art. 50:** as of mid-October 2026 Croatia had not designated a general market-surveillance
  authority for the AI Act nor adopted an implementing act (practitioner article, 13 Oct 2026; **VERIFY**). Media
  publishers have separate AI-labelling duties under the Croatian act implementing the European Media Freedom Act,
  supervised by the Agencija za medije (**VERIFY** scope and dates).

### Role analysis (worked example)
- A business that embeds a third-party LLM (via API) into a feature offered under its own name is most likely the
  **provider of an AI system** (Art. 3(3)); the model vendor is a **GPAI model provider**. When it uses AI internally
  (e.g. drafting blog posts) it is a **deployer**.
- **Risk class:** most productivity and calculation assistants are not in Annex III and are not safety components →
  **minimal or limited risk**. Recruitment, credit scoring, education grading, biometrics etc. are different —
  re-assess.

### Obligations
1. **Art. 4 (since 2 Feb 2025, softened):** a short internal AI-use policy; training notes for staff and contractors
   who use or build AI features; records of what was done.
2. **Art. 50(1):** a chat or assistant UI must tell users they are interacting with AI unless obvious. Example: "AI
   asistent — odgovori mogu sadržavati pogreške; provjerite rezultate."
3. **Art. 50(2):** generated text, images, audio, video must be marked in a machine-readable way (metadata,
   watermarks), unless the system performs an **assistive function for standard editing** or does not substantially
   alter the input. **VERIFY** whether AI-written passages in exported reports need marking; practical approach: a
   visible note plus document metadata.
4. **Art. 50(4):** a deployer publishing AI-generated **text to inform the public on matters of public interest**
   must disclose it, unless the text underwent human review or editorial control and someone holds editorial
   responsibility. Keep that review documented (named editor). Realistic AI images/video/audio ("deepfakes") need a
   label that travels with the content.
5. **Penalties (Art. 99):** up to €15M or 3 % of turnover for Art. 50 breaches; for SMEs the **lower** of the two.

### GDPR points when sending user data to AI APIs
- Sign the vendor DPA (Art. 28); check the transfer basis (DPF and/or SCCs).
- Prefer zero data retention / no-training settings and EU data residency.
- Minimise prompts: strip names, addresses and identifiers.
- Update the privacy notice and ROPA; consider a light DPIA if client personal data are included.
- Never feed admin-console customer data into AI tooling without a basis.

---

## 5. NIS2 (Directive (EU) 2022/2555) and Zakon o kibernetičkoj sigurnosti (NN 14/2024)

### Size-cap rule in the Croatian Act (verified) [NN text read]
- **Art. 9 (essential entities):** Annex I entities that **exceed** medium-enterprise thresholds. Qualified trust
  service providers, TLD registries and DNS providers count "neovisno o veličini".
- **Art. 10 (important entities):** Annex I/II entities that are **medium-sized or larger**.
- **Cloud computing service providers are subject to the size cap** (same as NIS2 Art. 2(2)).
- **Art. 11:** micro and small entities can be designated regardless of size only in special cases (sole provider of
  a critical service, significant impact on public safety or health, systemic risk, special national importance).

**Conclusion:** a micro SaaS is not a key or important entity.

### Special register (Art. 22–23)
The central state body for cybersecurity keeps a register of cloud, data-centre, CDN, MSP/MSSP, marketplace and
similar providers; data must be supplied within **15 days of a request**. Whether it reaches entities below the size
cap is unclear (**VERIFY**). No proactive filing.

### If covered
Risk-management measures (Art. 26), incident reporting, management accountability. Fines: essential entities
€10,000 to €10M or 0.5–2 % of turnover (Art. 101); important entities €5,000 to €7M or 0.2–1.4 % (Art. 102).

### Indirect effect
Customers that are NIS2 entities must manage supply-chain risk: expect security questionnaires and contract clauses.
A short security whitepaper helps.

---

## 6. Cyber Resilience Act: Regulation (EU) 2024/2847

- **Scope:** "products with digital elements". **Pure SaaS is a service and is out of scope**; remote data processing
  is caught only when essential to a product's functions (DLA Piper, Feb 2026; Commission FAQs). Downloadable software
  (desktop app, plugin, CLI, mobile app) is in scope.
- **Timeline:** reporting obligations (Art. 14) from **11 Sep 2026** (actively exploited vulnerabilities and severe
  incidents: 24 h early warning, 72 h notification, final report via ENISA's Single Reporting Platform); full
  application from **11 Dec 2027** (essential requirements, conformity assessment, CE marking, support period).
- **For a browser-only SaaS:** not applicable. If a plugin, desktop exporter or app is released, the reporting duty
  applies at once and full requirements for units placed on the market from 11 Dec 2027. Plan secure-by-design, an
  SBOM and vulnerability handling. Microenterprises get some penalty relief for missed 24 h deadlines (**VERIFY**
  Art. 64(10)).

---

## 7. New Product Liability Directive (EU) 2024/2853 (PLD)

### Croatian transposition (verified) [NN text read]
- **Zakon o izmjenama i dopunama Zakona o obveznim odnosima, NN 69/2026**, adopted 19 Jun 2026.
- The product-liability articles **enter into force on 9 Dec 2026** and **do not apply to products placed on the
  market or put into service before 9 Dec 2026** (Art. 21(2) of the amending act).
- Definition: "proizvod je bilo koja pokretnina … uključujući … **softver**". New concepts: "povezana usluga"
  (related service) and "kontrola proizvođača" (manufacturer's control), which covers software updates.

### Effect on SaaS
- PLD Recital 13 treats software as a product **irrespective of mode of supply, including SaaS**.
- Strict liability for **death or personal injury (incl. medically recognised psychological harm)**, damage to
  **property** and **destruction or corruption of data**. **Property and data used exclusively for professional
  purposes are excluded.** Pure economic loss is not covered.
- A B2B tool therefore has limited direct exposure, but some remains: an error that leads to physical or health harm
  to a consumer, or a vulnerability that corrupts a consumer user's private data.
- Liability towards the injured person **cannot be excluded or limited by contract** (PLD Art. 15; ZOO čl. 1079).
- Presumptions of defectiveness ease the claimant's burden in technically complex cases; failing to supply security
  updates can make a product defective; a substantial modification can reset timelines.

### Checklist
- Versioned release notes and validation evidence (test cases against known worked examples).
- A vulnerability-patching record.
- Product liability insurance or a professional indemnity extension covering software (**VERIFY** with an insurer).
- Keep B2B limitation clauses for contract claims within ZOO limits (no exclusion for intent or gross negligence,
  ZOO čl. 345).
- For a continuously updated SaaS the "placed on the market" date is fuzzy, so assume the new regime.

---

## 8. Croatian language law

### Correct title (verified)
**Zakon o hrvatskom jeziku**, NN 14/2024 (not "hrvatskome"). In force 8 days after 7 Feb 2024. [NN text read]

### What binds a private business
- **Art. 11(1):** "public use" covers any oral or written notice in a space intended for the public, **including
  electronically**.
- **Art. 11(3):** Croatian is the means of informing the public and **consumers about products and services on the
  Croatian market**.
- **Art. 11(4):** **public notices and promotional messages** are made **in Croatian**.
- **Art. 11(5):** in multilingual notices and promotions, **Croatian comes first**.
- **Art. 15(2):** names of professional events and conferences are displayed in Croatian (Croatian first if
  translated).
- **Art. 6(2):** the Act does not regulate private communication.

### Enforcement
The Act has **no penalty provisions**; the Vijeće za hrvatski jezik (Art. 17–18) is advisory. Real sanctions come
from other laws: consumer law requires pre-contract information and contracts in Croatian (ZZP čl. 60(9)); company
law governs the company name (ZTD čl. 21); the EAA Croatian law covers product instructions.

### Must be in Croatian on the Croatian market
Marketing site and landing pages; ads and e-mail campaigns; pricing; T&Cs and privacy notice; DSA notices; in-app
UI for Croatian users; exported document templates used in Croatian procedures; support communication. A Croatian
brand name avoids the question; foreign-language feature names and taglines should appear with Croatian first on
Croatian-market pages.

---

## 9. Intellectual property

### Copyright: Zakon o autorskom pravu i srodnim pravima (ZASP), NN 111/2021 [NN text read]
- **Software is protected** as a literary work.
- **Employees, Art. 100(6):** for a computer program created by an employee performing duties under an employment
  contract, **the employer holds all exclusive exploitation rights**, unless the contract says otherwise. Art. 101
  allows special remuneration if provided for.
- **Commissioned works, Art. 96(3):** the commissioner is *presumed* to acquire exclusive rights only "to the extent
  necessary for its business activity". With freelancers, designers and agencies, use a **written contract with an
  explicit, broad assignment or exclusive licence** (all forms of use, modification, sublicensing, worldwide,
  unlimited in time) and consent to modification (moral rights are not transferable). **VERIFY** the written-form
  requirement.
- **Text and data mining, Art. 188:** commercial TDM is allowed on lawfully accessible works unless the rightsholder
  opted out; for online content only a **machine-readable** opt-out counts (Art. 188(5)). Keep robots.txt, TDM
  reservations and T&C consistent; check opt-outs of sources you mine yourself.
- **Trade secrets:** protected under the Zakon o zaštiti neobjavljenih informacija s tržišnom vrijednošću (NN 30/18,
  **VERIFY**) only if "reasonable steps" keep them secret: NDAs, access control.

### Images, fonts and other assets
- **Free stock licences** (e.g. Unsplash): commercial use usually allowed without attribution, but no resale of
  unaltered photos, and **people, trademarks and buildings are not cleared**. Keep a log of image URL and download
  date.
- **Paid stock:** keep licence certificates; respect editorial-only restrictions.
- **AI-generated images:** uncertain copyright; AI Act labelling if realistic.
- **Fonts:** most Google Fonts use the SIL OFL (fine for web and PDF embedding); **self-host** rather than hot-link
  (LG München I, Jan 2022). Commercial fonts need web and PDF embedding licences.

### Open-source compliance
Run a licence report for every repository's production dependencies (e.g. `license-checker`, `mvn
license:aggregate-third-party-report`, `pip-licenses`). Typical findings:
- **MPL-2.0 code shipped to browsers:** frontend JavaScript is *distributed*, so MPL applies to those files: keep
  notices and tell recipients where the source of MPL-covered files is (link to upstream repo and version on a
  "Third-party notices" page); publish modifications to MPL files under MPL; your own files stay proprietary.
- **CC-BY data packages** (e.g. browser-compatibility datasets): attribution on the notices page.
- **LGPL native libraries used server-side or at build time:** server-side SaaS use is not "distribution"; do not
  distribute the backend (e.g. on-prem edition) without LGPL compliance.
- **AGPL:** its network clause *does* bite in SaaS (classic case: some PDF libraries). Add a CI licence gate that
  fails on AGPL/GPL/SSPL unless approved.
- **Apache-2.0:** keep LICENSE and NOTICE. **MIT/BSD/ISC:** reproduce copyright and licence text.
- Practical approach: an automatically generated `/third-party-notices` page, linked from the app footer (and from
  exported documents if fonts or libraries are embedded).

### Trademarks
- Register the product name (word mark, ideally also the logo) before scaling the brand; run a clearance search first
  (TMview, DZIV database).
- **Classes:** usually 9 (downloadable software), 42 (SaaS), possibly 41 (training, webinars).
- **Routes:** **DZIV** (Državni zavod za intelektualno vlasništvo), national; **EUIPO** EU trade mark (about €850 for
  one class online, +€50 for the second, +€150 per further class; **VERIFY** current fees). National law: Zakon o
  žigu (NN 14/2019, **VERIFY**).

### Domains (.hr)
- The .hr registry is CARNET (Pravilnik o ustrojstvu i upravljanju vršnom nacionalnom internetskom domenom).
- Free second-level .hr domains for legal persons must match the registered company name or abbreviation (per
  domene.hr); paid .hr domains (any name) are available to EU-established persons. Keep registrant data current.
- Consider defensive registrations of obvious typos and .eu / .com.

---

## 10. Sector-specific regulation

Many products implement rules from a regulated sector (construction, energy, tax, health, finance, tourism). The
general pattern:

1. **Identify the rules the product implements** and record the exact version (NN number, edition of standards).
2. **Track pending changes** (e-Savjetovanja, ministry pages) — a replaced regulation can make the product's output
   wrong overnight and makes "usklađeno s propisima" claims misleading.
3. **Check whether software approval is required.** It usually is not; then never imply one ("certificiran",
   "odobren od Ministarstva", "službeni").
4. **Identify who is legally responsible** for the final document (a licensed professional, an authorised person,
   the taxpayer) and reflect that in the T&C and the in-tool disclaimer (`03` §6).

**Typical outcome (VERIFY for the actual sector before relying on it):**
- Official documents in regulated sectors (certificates, design documentation, tax returns, medical records) are
  usually signed by a licensed professional or authorised person, or issued through a state information system. The
  software vendor is not a regulated party: its liability is contractual and, from 9 Dec 2026, product liability (§7).
- Where no approval regime exists, confirm that with the competent ministry before making any marketing claim.
- **Safe claims:** "izračun prema [norma, izdanje]" if implemented and validated against worked examples; "provjera
  zahtjeva iz [propis, NN]" as a factual statement of what is checked. **Avoid unless provably true:** "certificiran",
  "verificiran od Ministarstva", "odobren", "službeni", "zamjena za [službeni dokument / stručnu osobu]", "100 %
  točno", "jamčimo da će dokument biti prihvaćen".

---

## 11. Advertising and claims (B2B), comparative advertising, competitor names

### Statute
**Zakon o nedopuštenom oglašavanju**, NN 43/2009 [NN text read]. Protects **traders** (B2B) from misleading
advertising and sets the conditions for comparative advertising; B2C is covered by ZZP unfair-practice rules.
- **Art. 3:** misleading advertising is any advertising that misleads, or is likely to mislead, and is likely to
  affect economic behaviour or injure competitors.
- **Art. 5:** the assessment covers claims about characteristics, fitness for purpose, **expected results**, **test
  results**, price, and the advertiser's qualifications and awards.
- **Art. 6:** comparative advertising is lawful only if it is not misleading; compares goods or services meeting the
  same needs; **objectively compares material, relevant, verifiable and representative features**; creates no
  confusion; does not **denigrate** the competitor or its marks; takes no unfair advantage of a mark's reputation;
  does not present the product as an imitation.
- **Enforcement:** action before the **commercial court** (Art. 7–9). **Reversed burden of proof**: the court can
  require the advertiser to prove factual claims; unproven claims are deemed inaccurate (Art. 10(3)–(4)). Interim
  measures and publication of the judgment at the advertiser's cost (Art. 11, 14). Competitors can also sue under
  unfair-competition and trademark law.

### Using competitor names
- "Product vs Competitor" or "alternative to Competitor" pages are **comparative advertising**: permissible if facts
  are accurate, verifiable, current and dated, with no disparagement and no logo use. Reflect competitors' real prices
  (including free tiers) accurately.
- Keyword ads on competitor marks are generally lawful if the ad clearly identifies the advertiser (CJEU C-236/08
  *Google France*, C-323/09 *Interflora*).
- Referential use of the word mark is fine; the competitor's **logo** or trade dress is not.
- Keep a dated evidence file for every comparative claim: screenshots, version numbers, prices.

---

## 12. Reviews, testimonials and client logos

- **Consumer-facing reviews:** ZZP čl. 36(5) t. 3 and čl. 37 t. 31–32 (from the Omnibus Directive 2019/2161): say
  whether and how you verify reviews; fake or undisclosed incentivised reviews are blacklisted.
- **B2B:** the same principle via misleading advertising (Art. 5): testimonials must be genuine, typical (or labelled
  as not typical), with incentives disclosed.
- **Client logos:** get **written permission** (trademark; implied endorsement).
- **Named testimonials with photos:** consent of the person (GDPR); keep records and allow withdrawal.

---

## 13. Employment and contractors (flag only)

Detail lives in `croatia:hr-payroll-employment`.
- **Zakon o radu:** written employment contract or written confirmation before work starts; working-time records;
  internal work rules (pravilnik o radu) from 20 employees.
- **Zakon o zaštiti na radu:** risk assessment (procjena rizika) from the first employee; health and safety training.
- **Contractors:** disguised-employment risk; explicit IP assignment (ZASP Art. 96); NDA and trade-secret clauses;
  local law and tax for foreign contractors.
- **Employee monitoring:** GDPR and Zakon o radu limits.

---

## 14. Web security baseline

### Legal anchors
- **GDPR Art. 32** (appropriate measures) and **Art. 33–34** (breach notification to AZOP within 72 h).
- **DSA** has no security mandate. **NIS2** does not apply directly to a micro SaaS, but its Art. 21 list is the de
  facto benchmark customers ask about.

### Practical baseline
- HTTPS everywhere with HSTS; security headers (CSP, frame-ancestors, Referrer-Policy).
- OWASP Top 10 / ASVS L1–L2 for the app and **admin console**: MFA for admins, IP allow-listing or separate auth,
  audit log.
- **File upload hardening:** size limits, parsers sandboxed with timeouts, no XXE or zip bombs.
- Dependencies patched with automated alerts; encrypted backups, restore tests, documented backup policy.
- **Logging and monitoring vendors:** DPAs; EU regions; **mask personal data before sending** — shipping appenders
  often serialise events themselves and bypass the framework's pattern-based masking, so masking must happen in the
  appender or shipper itself (test it); retention limits.
- **Vulnerability disclosure:** publish **`/.well-known/security.txt`** (RFC 9116: Contact, Expires, Policy,
  Preferred-Languages: hr, en) and a short coordinated disclosure policy with a safe-harbour statement. Croatia's CVD
  coordinator for private entities: national CSIRT (**VERIFY** whether CERT.hr or the NCSC under SOA).
- **Incident runbook:** who decides, AZOP 72 h, customer notification, DSA Art. 18 if a life or safety threat is
  detected.

---

## 15. Hosting and data localisation

- **No data-localisation requirement** in Croatian or EU law for ordinary SaaS; Regulation 2018/1807 prohibits
  unjustified localisation requirements for non-personal data.
- **Personal data** may be hosted outside the EU only with a GDPR Chapter V transfer basis.
- **Recommendation:** primary hosting, backups, logs and AI-API regions in the EU/EEA. This simplifies GDPR,
  public-sector sales, NIS2-regulated customers and Data Act Art. 32 (if ever in scope).

---

## 16. AZOP registration or database notification

- **No general registration or notification duty** under the GDPR; the old central register under the repealed
  Zakon o zaštiti osobnih podataka no longer exists, and ZPDZ (NN 42/2018) has none.
- **Remaining duties:** if a DPO is designated, **send AZOP the DPO contact details** (GDPR Art. 37(7); AZOP form);
  prior consultation only if a DPIA shows high residual risk (Art. 36).
- **Company impresum** on the website: ZET Art. 6 plus ZTD Art. 21 (see `03` §4).

---

## Summary table

| Regulation | Applies to a micro SaaS? | Why | Key obligations | Deadline / status | Penalty |
|---|---|---|---|---|---|
| EAA: Zakon o zahtjevima za pristupačnost proizvoda i usluga (NN 89/25) | **No, while micro** (services) | Art. 4(2) exempts micro service providers; B2B-only is outside "e-commerce" | If exemption lost: WCAG 2.1 AA / EN 301 549, Annex V statement | In force 28 Jun 2025; re-test thresholds annually | €6,630–132,720 (Art. 36) |
| Public-sector web accessibility (NN 17/19, **VERIFY**) | No | Public bodies only | Indirect: tender WCAG requirements | — | — |
| DSA 2022/2065 + NN 67/25 | **Yes** (hosting service) | Stores user content | Art. 11–12 contact points; Art. 14 T&Cs; Art. 16 notice and action; Art. 17 reasons; Art. 18; **HAKOM notification**; Art. 15 reports exempt for micro/small | In force; HAKOM deadline 29 Oct 2025 (file now) | €6,630–66,360 or up to 6 % of turnover |
| Data Act 2023/2854, Ch. VI | **Likely no** for specialised tools (VERIFY) | Commission FAQ: SaaS out if computing is incidental | If in scope: switching terms, export, zero switching charges | Applicable 12 Sep 2025; charges zero from 12 Jan 2027 | Set nationally (VERIFY HR act) |
| AI Act 2024/1689 as amended by Reg. 2026/1744 | **Yes, if AI features or AI content** | Provider of an AI feature; deployer for AI content | Art. 4 AI literacy support; Art. 50(1) disclosure; 50(2) marking; 50(4) public-interest text and deepfakes | Art. 50 since 2 Aug 2026; marking for pre-Aug-2026 systems by 2 Dec 2026 | Up to €15M or 3 %; SMEs the lower; HR authority not yet designated (VERIFY) |
| NIS2 / Zakon o kibernetičkoj sigurnosti (NN 14/24) | **No** | Size cap | Indirect: supply-chain clauses; possible register request | In force | Up to €10M / 2 % (essential) |
| CRA 2024/2847 | **No** for pure SaaS; **yes** for downloadable apps/plugins | Products with digital elements only | Art. 14 reporting; later essential requirements, CE | Reporting 11 Sep 2026; full 11 Dec 2027 | Up to €15M / 2.5 % |
| PLD 2024/2853 → ZOO NN 69/26 | **Yes** (software is a product) | Strict liability for injury, consumer property and data | No exclusion; validation records, patching, insurance | Products placed from 9 Dec 2026 | Civil damages |
| Zakon o hrvatskom jeziku (NN 14/24) | **Yes** | Public and promotional content on the HR market | Croatian; Croatian first when multilingual | In force | No sanctions in the Act |
| ZASP (NN 111/21) + OSS licences | **Yes** | Own software, contractor work, assets, OSS | Contractor IP assignment; notices page; asset log; TDM stance | Ongoing | Damages, injunctions |
| Trademarks (DZIV / EUIPO) | Optional but advised | Protect the brand | Clearance + filing | — | — |
| Sector rules the product implements | **Indirectly** | Define what the product must compute or produce | Accurate claims; track pending changes | Varies | Misleading advertising, contract, PLD |
| Zakon o nedopuštenom oglašavanju (NN 43/09) | **Yes** | B2B advertising, comparisons | Verifiable claims, no disparagement, no logos | In force | Injunction, publication, reversed burden |
| Reviews and testimonials (ZZP) | Yes for B2C; principle B2B | Fake or undisclosed reviews banned | Disclose verification; written logo consent | In force | ZZP fines |
| GDPR Art. 32 security | **Yes** | Personal data | TLS, OWASP, MFA, log masking, security.txt, CVD | In force | Up to €10M / 2 % |
| Data localisation | **No** | None in HR/EU law | EU hosting recommended | — | — |
| AZOP registration | **No** | Abolished with GDPR | DPO contact only if a DPO is appointed | — | — |

---

## Prioritised action list (typical micro SaaS)

### Now
1. **Notify HAKOM** in e-Pružatelj DSA if the service stores user content.
2. **DSA website and T&Cs:** contact points, moderation and acceptable-use chapter, reporting form and procedure,
   statement-of-reasons template.
3. **AI Act (if any AI feature or AI content):** in-UI disclosure; internal AI-use and literacy note; vendor DPA,
   no-training / zero-retention settings, EU region, privacy-notice update; documented human editorial review for
   AI-assisted public content; labels for realistic AI media; machine-readable marking by **2 Dec 2026** for
   generative features launched before 2 Aug 2026.
4. **Open-source compliance:** generated `/third-party-notices` page; CI licence gate.
5. **Log masking** on every shipping appender; DPAs and EU regions for monitoring vendors.
6. **Audit marketing claims:** remove or qualify "certificiran / verificiran / službeni"; state implemented rule and
   standard versions; dated evidence file for every comparative claim; no competitor logos.
7. **security.txt and a CVD policy**; MFA on the admin console.

### Before 9 Dec 2026
8. **PLD readiness:** validation dossier, release notes, patching log, insurance check, review of B2B limitation
   clauses.
9. **Contractor and IP hygiene:** written IP assignment and NDA with every contractor (retroactive where possible);
   asset licence log; self-hosted fonts.
10. **Trademark:** clearance search, then filing.
11. **Croatian-first check** on all public and promotional surfaces.
12. **Data portability:** full export feature; memo on Data Act scope.

### Watch list (2027)
13. Pending changes to the sector rules the product implements.
14. **Digital Omnibus** (GDPR, cookies, Data Act strand): Council mandate 21 Oct 2026; Parliament and trilogues next.
15. **CRA** if any downloadable component is planned.
16. **EAA thresholds:** re-check annually.
17. **Public-sector sales:** WCAG and security documentation for tenders.

---

## Key sources
- NN 89/2025, Zakon o zahtjevima za pristupačnost proizvoda i usluga: https://narodne-novine.nn.hr/clanci/sluzbeni/2025_06_89_1231.html
- NN 67/2025, Croatian DSA implementing act: https://narodne-novine.nn.hr/clanci/sluzbeni/2025_04_67_857.html
- HAKOM DSA notification: https://www.hakom.hr/hr/informacija-o-nacinu-podnosenja-obavijesti-o-pruzanju-usluga-posredovanja/12197
- NN 14/2024, Zakon o kibernetičkoj sigurnosti: https://narodne-novine.nn.hr/clanci/sluzbeni/2024_02_14_254.html
- NN 14/2024, Zakon o hrvatskom jeziku: https://narodne-novine.nn.hr/clanci/sluzbeni/2024_02_14_252.html
- NN 69/2026, ZOO amendments (PLD transposition): https://narodne-novine.nn.hr/clanci/sluzbeni/2026_06_69_833.html
- NN 111/2021, ZASP (Art. 96, 100, 188): https://narodne-novine.nn.hr/clanci/sluzbeni/2021_10_111_1941.html
- NN 43/2009, Zakon o nedopuštenom oglašavanju: https://narodne-novine.nn.hr/clanci/sluzbeni/2009_04_43_984.html
- AI Omnibus (Reg. 2026/1744): White & Case https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act ; deadline summary (Oct 2026) https://www.technology.org/2026/10/13/eu-ai-act-deadlines-after-the-digital-omnibus-what-applies-from-december-2026-to-august-2028/
- Croatian AI Act supervision gap (practitioner article, 13 Oct 2026): https://womeninadria.com/kazne-do-15-milijuna-eura-tko-ce-u-hrvatskoj-nadzirati-transparentnost-po-ai-aktu/
- Data Act Art. 31: https://www.eu-data-act.com/Data_Act_Article_31.html ; MoFo FAQ analysis https://www.mofo.com/resources/insights/251222-top-10-questions-about-the-eu-data-act
- CRA and SaaS: DLA Piper https://www.dlapiper.com/en/insights/publications/2026/02/cyber-resilience-act-the-fine-line-between-saas-and-digital-products
- Digital Omnibus Council mandate (21 Oct 2026): https://dig.watch/updates/eu-council-agrees-digital-rulebook-changes
- .hr domains: https://domene.hr/portal/register

**Limitations.** Secondary-source points (law-firm summaries of the Omnibus, the Data Act FAQ, deadline trackers) were
not cross-checked against EUR-Lex consolidated texts. Fee amounts (DZIV, EUIPO) and several NN numbers for ancillary
acts are marked VERIFY.
