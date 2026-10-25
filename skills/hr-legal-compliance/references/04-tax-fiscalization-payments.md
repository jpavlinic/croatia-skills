# Tax, invoicing, fiscalization, record-keeping and payments for a Croatian online business (payment providers such as Stripe)

This file holds the legal "what". For implementing fiscalization and eRačun in code (message formats, signing,
queues, intermediaries) use `croatia:hr-fiscalization-dev`; for choosing obrt vs d.o.o., paušal, VAT registration
and owner contributions use `croatia:hr-business-admin`.

**Status:** researched 2026-10-05; the fiscalization rulebook and NN publications re-checked 2026-10-25 (no further amendment after NN 97/2026 found). Research method: the full text of the new Fiscalization Act (Zakon o fiskalizaciji, NN 89/2025, all 80 articles) was read, together with the Tax Administration's (Porezna uprava, "PU") Q&A document on that Act, its B2C Q&A page (updated 30.1.2026), RRiF, TEB, HOK and several practitioner sites. Items marked **VERIFY** are not confirmed in a primary source, conflict between sources, or may change. Check them with an accountant or porezni savjetnik before going live.

---

## 0. Executive summary

1. **"Fiskalizacija 2.0" is in force.** The new Fiscalization Act (Zakon o fiskalizaciji, NN 89/2025) replaced the old Act on Fiscalization in Cash Transactions (Zakon o fiskalizaciji u prometu gotovinom) on 1.9.2025. Its key parts apply from **1.1.2026**, and the rule that non-VAT payers must *issue* eRačun applies from **1.1.2027**. This is confirmed by the Act itself (Art 80).
2. **Every B2C invoice must be fiscalized, whatever the payment method.** This covers cash, card, Stripe and bank transfer, for every income-tax or profit-tax payer, and **includes paušalni obrt**. Fiscalization means a signed message to PU, which returns a JIR; the invoice must show the JIR, the ZKI and a QR code. There is no turnover or volume exemption (Arts 3 and 2(26); PU Q&A).
3. **Domestic B2B is now eRačun:**
   - **VAT-registered sellers** must issue and receive structured eRačuni (EN 16931 / UBL XML) through an access point or information intermediary (informacijski posrednik), from 1.1.2026.
   - **Non-VAT sellers** (paušalist, small obrt, non-VAT j.d.o.o.) only have to *receive* eRačuni in 2026. They must *issue* eRačuni from **1.1.2027**, for example with PU's free MIKROeRAČUN app.
   - A PDF sent by email is **not** an eRačun.
4. **Domestic B2B paid by card can stay on the B2C route.** Under Art 39 the seller may instead issue a B2C-style fiscalized invoice that includes the buyer's OIB. If it does, it may not also issue an eRačun for the same sale.
5. **Foreign sales:**
   - Cross-border B2B and B2C sales whose place of supply is **outside Croatia** are **not subject to fiscalization**. They get a normal invoice. PU says this explicitly for OSS distance sales and for services to private persons in third countries. **VERIFY** that this applies one-for-one to electronically supplied services sold to non-EU consumers.
   - Watch the €10,000 EU-wide threshold: below it, B2C EU sales are taxed in Croatia and **are** fiscalized.
6. **VAT thresholds and status:**
   - The registration threshold is **€60,000** domestic annual turnover. That is also the paušal limit.
   - Selling services to EU businesses requires a **VAT ID number (PDV-ID)** even for a non-VAT small taxpayer. It also means filing the PDV return and the ZP return.
   - From 1.1.2026 the **PDV, ZP and PDV-S returns are due on the last day of the following month**, not the 20th (NN 151/2025).
7. **Stripe does not fiscalize Croatian invoices.** You need a certified fiscalization solution (own build or third party) driven by Stripe webhooks, plus a separate eRačun intermediary for B2B.
8. **Retention periods:**
   - Bookkeeping documents and ledgers: **11 years** under the Accounting Act (Zakon o računovodstvu).
   - Fiscalized eRačuni: **6 years** under Art 35 of the Fiscalization Act.
   - The General Tax Act (Opći porezni zakon, OPZ) requires **10 years from the start of the limitation period**.

   This is the legal basis for keeping billing data after an account is deleted: GDPR Art 6(1)(c) and Art 17(3)(b).

---

## 1. Fiscalization (Fiskalizacija 2.0)

### 1.1 Legal framework and timeline (verified against NN 89/2025)

| Item | Status |
|---|---|
| Fiscalization Act (Zakon o fiskalizaciji), NN 89/2025 | Passed 6.6.2025. In force **1.9.2025** (Art 80). |
| Old Act on Fiscalization in Cash Transactions (Zakon o fiskalizaciji u prometu gotovinom, NN 133/12 … 114/23) | Repealed on 1.9.2025 (Art 79). |
| From **1.1.2026** | Art 3 extended to bank-transfer payments (transakcijski račun). eRačun Part III applies: Arts 33–43, 45, 47–57. Penalties for eRačun breaches apply. |
| From **1.1.2027** | Art 38(1) points 2–3 apply: **non-VAT income/profit taxpayers and budget users must issue eRačun**. Arts 54–56 apply to *issuing* through MIKROeRAČUN. |
| Implementing rulebook | Rulebook on fiscalization of B2C invoices (Pravilnik o fiskalizaciji računa u krajnjoj potrošnji), NN 153/2025. Amended by **NN 97/2026 (2.9.2026)**; the amendment concerns testing and trust-service certificates (**VERIFY the details**). |

There is **no separate "deadline for non-VAT payers to fiscalize B2C card or bank-transfer invoices"**: they have had to fiscalize all B2C invoices since **1.1.2026**. The 1.1.2027 date applies only to *issuing B2B/B2G eRačun*. Some influencer posts merge the two dates, so treat them with care.

### 1.2 Who must fiscalize B2C invoices (obveznik fiskalizacije računa)

Art 2(21) defines the obligated person as anyone paying income tax on self-employment (obrt of any kind, including paušal) or paying profit tax (d.o.o., j.d.o.o.). VAT status is irrelevant.

Art 2(26) defines "promet u krajnjoj potrošnji" as invoices issued **to citizens / consumers regardless of payment method**.

Art 3 says the obligated person fiscalizes invoices "naplaćenog gotovinom, karticama, transakcijskim računom i na ostale načine", that is, paid in cash, by card, by bank transfer or otherwise. Stripe card payments are "kartica", and other methods are "ostalo".

PU's Q&A has no minimum: an obrt with only a few B2C bank-transfer invoices must still fiscalize. PU Q&A no. 34 says a paušalni obrt must, from 1.1.2026, have a "prilagođeni naplatni uređaj s programskim rješenjem", meaning fiscalization-capable invoicing software. MIKROeRAČUN **cannot** issue B2C invoices.

### 1.3 What changed compared with the old cash-transactions Act

| Topic | Old Act (to 31.12.2025) | Fiskalizacija 2.0 |
|---|---|---|
| B2C payment methods fiscalized | Cash and cards (plus cheques and "other") | **All methods, including bank transfer** (from 1.1.2026) |
| Paušalist selling online with Stripe card payments | Already fiscalizable as card payments | Same, plus bank-transfer B2C invoices |
| B2B domestic | Paper or PDF invoices; eRačun mandatory only for B2G | Mandatory eRačun with fiscalization by both issuer and recipient. VAT payers from 2026; non-VAT issuers from 2027. |
| Reporting | — | **eIzvještavanje** (e-reporting): payment data, rejections, and supplies where no eRačun could be sent |
| Classification code | — | **KPD 2025** code (six digits) required on every eRačun line (Art 42) |
| Certificate | FINA fiscal certificate only | Any certificate from a qualified trust service provider that contains the OIB (Art 10; Q&A 23) |
| VAT ledgers | U-RA form and PPO form | Abolished from 2026 because PU now gets the data from fiscalization (NN 151/2025) |

### 1.4 Mechanics of a fiscalized B2C invoice

The process (Art 15) is:
1. The invoicing software signs the invoice elements.
2. It sends them to the Fiscalization System (Sustav za fiskalizaciju).
3. PU returns the **JIR** (unique invoice identifier).
4. The invoice is issued showing the JIR.

**Elements sent to PU** (Art 2(7)): the issuer's OIB, date and time, invoice number, a flag for whether the issuer is in the VAT system, amounts by VAT rate (including exempt amounts), payment method, the operator's OIB and the ZKI.

**Extra mandatory content on the invoice** (Art 7):
- time of issue (hour and minute);
- operator code;
- payment method (novčanice / kartica / transakcijski račun / ostalo);
- JIR;
- ZKI (issuer protection code);
- QR code. Its content is set by the rulebook, roughly JIR or ZKI, date-time and amount (**VERIFY the exact QR payload in NN 153/2025**).

**Numbering** (Art 9): numeric part / business premises code / device code, for example `154/WEB1/1`. The sequence must be unbroken, per premises or per device. It may restart each year from any number, as set out in the internal act. PU allows a separate device code for cashless invoices (Q&A 22).

**Internal act (interni akt)** (Art 9(3)): a written decision that sets the numbering rules, lists premises and device codes, links operator codes to OIBs (Art 8) and sets the cash limit (blagajnički maksimum). Someone with an internal act under the old law need not adopt a new one unless the data changed (Art 75).

**Software** (Art 14): the software must make it impossible to edit an invoice after it is issued. Both the taxpayer and the software vendor are liable. You must report the software maker's or maintainer's OIB to PU (Art 17).

**Connectivity outage** (Art 21): you may issue the invoice without a JIR and send it within **2 working days**.

**Cancellations and refunds** (Art 24): a storno invoice, or an invoice with a negative amount, is fiscalized under the same rules. This covers refunds and chargebacks.

**"OVO NIJE FISKALIZIRANI RAČUN"** (Art 29): any document showing payment details issued *before* the invoice, such as a pre-payment pro-forma, must carry this text. Breaking this rule is a "most serious" offence. **For SaaS: checkout pages and Stripe-hosted invoice or receipt emails that show payment data before the fiscalized invoice exists can trigger this.** Configure Stripe receipts accordingly, or switch them off and send your own fiscalized invoice (**VERIFY with an adviser how PU views Stripe's automatic receipt email**).

**Customer notice in premises** (Art 25): applies only to closed (physical) premises, so it is not needed for a web shop.

**Customer verification** (Art 28): the buyer can check the invoice for 30 days, for example at provjeri-racun.hr.

### 1.5 Business premises (poslovni prostor) for an online business (Art 16)

You must register **every premises where B2C invoices are issued** through ePorezna (FiskAplikacija) **before issuing the first invoice**. The data are:
- OIB;
- premises code;
- address, chosen from the spatial-units register (Registar prostornih jedinica);
- type, which must be stated as **"internetska trgovina"** (online store) for online business (Art 16(4));
- activity, as an NKD code;
- working hours and days;
- opening date;
- closing date (when it closes);
- status.

In practice, use the registered seat address, type "internetska trgovina", code e.g. `WEB1`, and hours 00–24 every day. PU says the taxpayer is free to decide what counts as its premises (Q&A on B2C no. 6). Report changes before they apply (Art 16(10)). Premises registered under the old Act do not need to be re-registered (Art 75(2)).

### 1.6 eRačun (B2B / B2G) – Part III of the Act

- **Who issues:** Croatian-established VAT payers (from 2026). Non-VAT income-tax and profit-tax payers and budget users from 1.1.2027 (Art 38(1)).
- **Who receives:** the same groups. **All of them have had to be able to receive eRačuni since 1.1.2026, including paušalists** (Art 2(24), Art 41). Each must publish its receiving address in the AMS address register through an intermediary or MIKROeRAČUN (Art 44).
- **Scope:** only **"tuzemne transakcije"** (Art 2(34)), meaning a supply subject to Croatian VAT (taxable or exempt) where **both parties are Croatian-established taxpayers** (Art 33(3)).
  - Sales to EU or non-EU businesses need **no eRačun and no e-reporting**; any "suitable form", such as a PDF, is enough (PU Q&A eRačun nos. 12–13).
  - Consumers are never eRačun recipients.
- **Format:** EN 16931-1:2017 with the Croatian CIUS extensions (Art 36). Exchange goes through access points (Art 37). The Q&A states expressly that email and PDF are not eRačun.
- **KPD code:** each line needs a six-digit KPD 2025 code (Art 42). **VERIFY the right code for SaaS** using PU's KPD browser. A likely candidate is 58.29.xx (software publishing, online software) or 63.10.xx (hosting and data processing); there is no official mapping.
- **eRačun fiscalization** (Arts 47–48): the issuer sends the fiscal data at issue and the recipient sends them within 5 working days of receipt. The intermediary usually does this under an authorisation given in FiskAplikacija. **An eRačun carries no JIR, ZKI or QR code** (Q&A 20). The Art 9 numbering rules still apply to eRačuni (Art 48(5)).
- **e-reporting (eIzvještavanje):**
  - **Payment data** for each eRačun: by the **20th of the following month** (Art 53).
  - **Rejections** by the recipient: by the 20th (Art 52).
  - Supplies where the buyer's AMS address was missing: report them (Art 51) and issue a paper invoice instead (Art 40).
- **Art 39 card/cash option:** a B2B sale paid by card or cash may be fiscalized as a B2C invoice that includes the buyer's OIB. PU confirms the issuer chooses (Q&A nos. 32 and 49–51), but then no eRačun may be issued. For a VAT-registered SaaS selling to a Croatian company by Stripe card, this is the simplest path: one fiscalization pipeline. However, many corporate customers want an eRačun in their accounts-payable system.
- **MIKROeRAČUN:** a free PU app for **non-VAT** taxpayers that are not public contracting authorities. It covers receiving (2026) and issuing (from 2027) eRačuni, but **not B2C**.
- **Intermediary requirements** (Arts 59–62): a Croatian OIB, ISO/IEC 27001 certification, EU-only data processing and a PU conformity certificate. PU publishes the "Popis informacijskih posrednika" (list of approved intermediaries). Foreign companies with a Croatian OIB may qualify (Q&A 79).
- **Retention:** fiscalized eRačuni must be kept **6 years** (Art 35).

### 1.7 Which sales are fiscalized (key for a SaaS)

| Sale | Place of supply (VAT) | B2C fiscalization (F1) | eRačun (F2) | Notes |
|---|---|---|---|---|
| Croatian consumer, Stripe card | HR | **Yes**, payment method "kartica" | No | JIR, ZKI and QR on the invoice, delivered by email or download |
| Croatian consumer paying by bank transfer | HR | **Yes**, method "transakcijski račun" | No | New since 1.1.2026 |
| Croatian business, VAT-registered seller | HR | Only if you choose the Art 39 route for a card payment | **Yes, unless Art 39 is used** | Buyer OIB required |
| Croatian business, **non-VAT seller** (paušal) | HR (exempt under Art 90) | Only if paid by card and Art 39 is used (**VERIFY whether Art 39 is useful for a non-VAT issuer in 2026, when it has no eRačun duty anyway**) | **Not before 1.1.2027.** From then: eRačun (MIKROeRAČUN or intermediary) | In 2026, an ordinary PDF invoice to businesses is fine (HOK leaflet; PU Q&A eRačun no. 6) |
| EU business with a valid VAT ID | Customer's member state (Art 17(1) ZPDV / Art 44 VAT Directive), reverse charge | No | No | Ordinary invoice with "prijenos porezne obveze / reverse charge" |
| EU consumer, while EU-wide B2C e-services are **≤ €10,000** | **HR** (Art 26a ZPDV) | **Yes**, it is a Croatian-taxed B2C sale | No | VAT payer: HR 25%. Paušalist: exempt under Art 90 |
| EU consumer, **above €10,000** (or after opting in) | Customer's member state, through OSS | **No.** PU Q&A B2C no. 8: OSS B2C sales "ne podliježu fiskalizaciji". You may fiscalize voluntarily. | No | Ordinary invoice with the customer-country VAT rate |
| Non-EU consumer | Customer's country (Art 26 ZPDV / Art 58 VAT Directive) | **No**, by analogy to PU's statement for services to private persons in third countries: "ne postoji obveza Fiskalizacije 1.0… jer se ne obračunava hrvatski PDV s obzirom na mjesto oporezivanja". **VERIFY** | No | Check the foreign VAT/GST rules; the UK, Norway, Switzerland, Australia and others tax digital services with low or no thresholds |
| Non-EU business | Customer's country (Art 17(1)) | No | No | Ordinary invoice. Report it in the PDV return. |

**Conflicting source to flag:** the HOK (Croatian Chamber of Trades) leaflet for paušalists says invoices to "fizičke osobe, stranci… preko raznih platformi" (foreign individuals paying through platforms) need ZKI, JIR and QR. That fits services whose place of supply stays in Croatia, which is the general Art 17(2) rule for a non-VAT seller and covers e-services under the €10k threshold. It does **not** fit OSS or non-EU e-services, which PU's own Q&A excludes. Fiskalopedija admits there are "razna mišljenja" (various opinions). **VERIFY. The safest practice is to fiscalize every sale whose place of supply is Croatia.** For a small SaaS under €10k in EU B2C, that means fiscalizing all EU consumer sales. Fiscalizing voluntarily is permitted (PU Q&A B2C no. 8).

### 1.8 Practical implementation with a payment provider (Stripe as the example)

Outline only; the code-level "how" is in `croatia:hr-fiscalization-dev`.

Stripe confirms on its support page "Invoice fiscalization in Croatia" that it provides **no** Croatian fiscalization. Third-party tools exist, such as e-racuni.hr's Stripe integration and fiskalio.net. Alternatively you build the integration yourself against PU's fiscalization web service using a qualified certificate.

1. **Trigger:** `invoice.paid` (subscriptions) or `checkout.session.completed` / `charge.succeeded`. Fiscalize **at the moment the invoice is issued**; for card payments that is immediately after payment succeeds (Fiskalopedija; Art 15).
2. **Classify the customer:** B2C or B2B; country; VAT ID valid in VIES; Croatian OIB present. Then choose the path from the table in 1.7.
3. **Create the invoice number** `n/WEB1/1` from your own gap-free sequence. Do not use Stripe's invoice number as the legal number unless you can guarantee the Art 9 format and no gaps. Stripe numbers can be voided or skipped.
4. **Fiscalize:** sign, send, receive the JIR. Render the PDF with JIR, ZKI, QR, time, operator and payment method "kartica". Email it.
5. **Refunds and chargebacks:** fiscalize a storno or negative invoice that references the original (Art 24). For an eRačun, issue a credit note through the intermediary.
6. **Outages:** queue and retry within 2 working days (Art 21).
7. **B2B domestic:** send the eRačun through the intermediary, or use the Art 39 card route. Report payment data by the 20th of the next month (Art 53); Stripe payouts give you the payment date.
8. **Suppress or relabel Stripe's own receipts**, or make sure they are clearly not invoices (see the Art 29 risk in 1.4).
9. **Keep audit logs:** request and response XML, JIR, timestamps.

---

## 2. Invoice content (ZPDV Art 79; OPZ; Fiscalization Act Art 7)

### 2.1 VAT Act (ZPDV) Art 79(1): mandatory elements
1. Invoice number and date of issue.
2. Seller's name, address and OIB or VAT ID.
3. Buyer's name, address and OIB or VAT ID.
4. Quantity and description of goods, or type and extent of services.
5. Date of supply or of advance payment, if different from the issue date. For subscriptions, state the service period.
6. Unit price excluding VAT, by rate.
7. Discounts, if not included in the price.
8. VAT rate.
9. VAT amount by rate.
10. Total (net plus VAT).

**Required notes:**
- Art 79(2): the OIB must be shown. For intra-EU transactions the **VAT ID** must be shown.
- Art 79(3): exempt supplies must cite the legal basis. For a paušalist / small taxpayer: *"Oslobođeno PDV-a temeljem čl. 90. st. 1. Zakona o PDV-u"*. VAT rate and VAT amount must then **not** appear.
- Art 79(7): reverse-charge supplies must say *"prijenos porezne obveze"* or *"reverse charge"*, citing Art 17(1) ZPDV.
- Paušalist to an EU business: cite Art 17(1) and "reverse charge". Do **not** combine this with the Art 90 note (Fiskalopedija/RRiF reasoning: these are two different grounds).
- Small taxpayers may issue simplified invoices (Art 79(12)), but **not** for supplies taxable in another member state (RRiF).

### 2.2 Other content requirements
- **Fiscalized B2C invoice:** add time, operator, payment method, JIR, ZKI and QR (Art 7).
- **Business form:**
  - d.o.o. / j.d.o.o.: the Companies Act (Zakon o trgovačkim društvima, ZTD) requires company name, seat, registry court and MBS number, bank and IBAN, share capital and how much is paid in, and the board members' names (Raverus summary; **VERIFY the ZTD article, roughly Art 21**).
  - Obrt: trade name, seat and owner's name (Pravilnik o porezu na dohodak; Zakon o obrtu).
- **Currency:** amounts in **EUR**. Other currencies may be shown as well, but the **VAT amount must be in EUR** at the Croatian National Bank (HNB) middle rate on the day the VAT obligation arises (Raverus summary of ZPDV and the rulebook; **VERIFY the article**). If you price in USD on Stripe for non-EU customers, still keep EUR equivalents for bookkeeping and for the €10k and €60k thresholds.
- **Language:** no rule found that makes a Croatian-language invoice compulsory for VAT purposes. PU may ask for a translation in an audit (OPZ procedural rules). Bilingual HR/EN invoices are common and safe (**VERIFY**).
- **R1/R2:** these labels come from the pre-2013 rulebook (R-1 meant an invoice giving the right to deduct input VAT). They no longer exist as legal categories. In practice "R1 račun" still means an invoice made out to a business with its OIB. For B2C nothing extra is needed.
- **Buyer's OIB for B2B:** mandatory for domestic B2B. It is also the eRačun identifier and the Art 15(6) field for Art 39 receipts. For consumers, OIB is not needed; name alone is enough per Fiskalopedija. For B2C online sales an email or name is normal.
- **Advance payments:** from 2026, practitioners say advance netting must be split into three documents: advance invoice, storno of the advance, final invoice (Finacro on NN 151/2025; **VERIFY**). This matters for annual SaaS prepayments that you invoice as advances; usually you avoid this by invoicing the service period at payment.

---

## 3. VAT (PDV)

### 3.1 Thresholds and status
- **Domestic registration threshold:** €60,000 annual turnover (ZPDV Art 90(1), from 1.1.2025; TEB, RRiF, HOK). Only supplies with a **Croatian place of supply** count. Services taxed in another country, such as B2B EU reverse charge or OSS B2C, **do not count** (RRiF 1.2).
  - Once the threshold is crossed you are registered **from the day after**.
  - You must file the P-PDV registration form within 8 days.
  - You cannot return to the exempt scheme the following year.
  - Voluntary registration commits you for the current year and the next.
- **Paušal limit:** €60,000 receipts a year, and the obrtnik must not be in the VAT system. Paušal tax brackets for 2026 run from €203.40 to €1,080 a year (Liber; **VERIFY with PU**). The government plans changes from 1.1.2027 for the brackets above €40k; the paušal limit is reportedly unchanged (Poslovni.hr, Dnevnik.hr, Aug–Sep 2026; **VERIFY final law**).
- **Cross-border SME scheme** (from 2025, Directive 2020/285): a Croatian small taxpayer can extend the exemption to other member states if EU-wide turnover is ≤ €100,000. It requires a prior notification to PU (an "EX" number) and quarterly reports (RRiF 2). This can be combined with OSS but not with IOSS.
- **Standard rate:** 25%, which applies to SaaS.

### 3.2 B2B to EU businesses (reverse charge)
- Place of supply is the customer's member state (ZPDV Art 17(1) = Directive Art 44). The **customer self-assesses** VAT under Directive Art 196.
- **Check the VAT ID in VIES** and keep the result: timestamp and consultation number. If the ID is invalid, treat the sale as B2C.
- **A non-VAT small taxpayer must still get a PDV-ID number** before supplying services to EU businesses (ZPDV Art 77; Pravilnik o PDV-u Art 154; RRiF 1.3). This is **not** joining the VAT system. Practitioners say apply about 15 days ahead (Luppis).
- It must then file **Obrazac PDV and Obrazac ZP** for each period in which it made such supplies, now due on the **last day of the following month** (NN 151/2025).
- Selling only to non-EU businesses does **not** require a PDV-ID, but those sales still go on the PDV return (RRiF 1.3, 1.6).

### 3.3 Services you **receive** from abroad: the Stripe fee issue
Stripe Payments Europe Ltd (Ireland) bills its fees cross-border. For a business customer, any **taxable** foreign service is reverse-charged in Croatia:
- **A paušalist must self-assess 25% Croatian VAT with no deduction.** It reports this on Obrazac PDV and **PDV-S** and needs a PDV-ID (RRiF 1.4.4, 1.6).
- Card-processing fees are usually exempt payment services. **Stripe Billing, Tax, Radar and similar product fees are likely taxable** (**VERIFY on your Stripe tax invoices**).
- The same applies to AWS, Google, OpenAI and other SaaS inputs. For a non-VAT business these make a cost about 25% higher, which is often overlooked.

### 3.4 B2C to EU consumers (electronically supplied services)
- **Rule:** e-services to non-taxable persons are taxed where the customer lives (ZPDV Art 26 = Directive Art 58).
- **€10,000 EU-wide threshold** (ZPDV Art 26a): this combines TBE (telecom, broadcasting, e-services) and intra-EU distance sales of goods, in the current or previous year. Below it, place of supply is Croatia: Croatian VAT for a VAT payer, Art 90 exemption for a small taxpayer. You may opt to apply destination VAT from the first euro.
- **Form "e-trgovina":** file by 20 January each year, or within 8 days of crossing the threshold (PU OSS page).
- **Above €10k:** charge the customer-country rate and declare it quarterly through **OSS (Union scheme)**, registered in Croatia. OSS returns are due by the last day of the month after the quarter (EU rule). OSS can be used by a small taxpayer while it keeps its domestic exemption (RRiF), so a paušalist with large EU B2C sales has to deal with foreign VAT through OSS. **VERIFY whether OSS registration has knock-on effects for paušal status**; it should not, because foreign-place supplies do not count toward the €60k.
- **Evidence of customer location** (Implementing Regulation 282/2011 Arts 24a–24f): keep **two non-contradictory pieces**, such as billing address, IP geolocation, card BIN country, bank country or SIM country.
  - Where your cross-border TBE supplies are ≤ €100,000 a year, **one** piece from a third party involved in the payment (e.g. the PSP or card-issuer country) can be enough (Art 24b(d)) (**VERIFY the current text**).
  - Stripe gives card country and billing address; you add your own IP geolocation.
- **Stripe Tax:** calculates rates, validates VAT IDs and records location evidence. It does **not** fiscalize. OSS filing support depends on Stripe's filing partners (**VERIFY**).

### 3.5 Non-EU customers
- B2B: place of supply is the customer's country. Show "PDV nije obračunat – čl. 17. st. 1. Zakona o PDV-u (reverse charge)". Report in the PDV return.
- B2C: outside the scope of EU VAT. **Check destination-country digital-services VAT/GST rules.** The UK has no threshold for non-UK sellers of digital services to consumers; Norway, Switzerland, Australia, some US states and others have their own regimes (**VERIFY per market as you grow**).

### 3.6 Price display to consumers
- B2C prices must be shown **final, including VAT and all taxes, in EUR** under the Consumer Protection Act (Zakon o zaštiti potrošača) price-indication rules and the euro-introduction framework. Dual HRK/EUR display ended in 2023 (**VERIFY article numbers**).
- Pricing pages for consumers: tax-inclusive, with the country-specific VAT once you are above €10k. Stripe's `tax_behavior: inclusive` supports this.
- Pricing for businesses may be net, labelled "+ PDV".

---

## 4. Accounting records and retention

| Source | Rule |
|---|---|
| Accounting Act (Zakon o računovodstvu), applies to d.o.o. / j.d.o.o. and other profit-tax payers | Documents behind journal and general-ledger entries, and subsidiary ledgers: **≥ 11 years**. Journal and general ledger: **≥ 11 years**, counted from the last day of the business year. Annual financial statements and payroll analytics: **permanent**. Payslips: 6 years. An electronic general ledger must be locked and e-signed, or printed and bound (TEB, March 2026). |
| Fiscalization Act Art 35 | Issued and received fiscalized **eRačuni**: **6 years** from the end of the year of issue. After that, PU keeps the fiscal data. TEB reads this as: eRačun 6 years; paper/PDF invoices and other bookkeeping documents 11 years. |
| General Tax Act (OPZ) | Business books, bookkeeping documents and records are kept **10 years from the start of the limitation period**, unless a special law sets longer (TEB). The limitation period starts after the end of the year the tax return was due (**VERIFY article numbers**; relative limitation 3 years, absolute 6 years). |
| VAT Act (ZPDV) | Invoices may be kept on paper or electronically, for the OPZ periods. Real-estate VAT documents: 10 years. |
| Paušalni obrt | Keeps only the **turnover book (Knjiga prometa, KPR)**: receipts entered daily, cash and cashless. Files the PO-SD form by 15 January. Keep the KPR and invoices for the OPZ period (≈ 10 years from the start of limitation, so effectively 11–12 calendar years). The Accounting Act's 11-year rule does not apply directly to obrt on income tax, but OPZ produces a similar period. |
| Obrt na dohodak | Income-tax books: KPI (income and expenditure book), DI (fixed-asset register), and others. OPZ retention applies. |

**GDPR link:** customer billing data (name, address, OIB or VAT ID, invoice lines, payment method, location evidence for OSS) may be kept **after the account is deleted**:
- legal basis: Art 6(1)(c), legal obligation;
- exemption from erasure: Art 17(3)(b) (and (e) for legal claims).

Recommended practice:
- Separate the "billing ledger" from the product account.
- Delete or anonymise product data when the account is deleted.
- Keep invoice and fiscal records for **11 full years after the year of the invoice**. Also keep OSS records 10 years, per Directive Art 369 (**VERIFY**).
- Say this in the privacy notice.

---

## 5. Payments (payment providers; Stripe as the example)

**Payment-method discounts and surcharges.** Zakon o platnom prometu (ZPP) (NN 66/18, 114/22, 136/24)
čl. 32(5): the payee may not charge any fee for using a particular payment instrument — a total ban, wider than
PSD2 Art 62(4), so it also covers commercial/B2B cards. čl. 32(4) allows discounts; čl. 15(1) requires disclosing
the discount before the payment is initiated. Word "card price = list − 5 %", never "+5 % for bank transfer"; the VAT
base is the discounted amount (ZPDV čl. 33). VERIFY article numbering against the consolidated text.

- **PSD2 SCA:** the EU card issuer requires strong customer authentication. Stripe Checkout, Elements and Billing handle 3-D Secure. After SCA on the first payment, recurring subscription charges are merchant-initiated transactions (MIT) outside SCA. Use `setup_future_usage=off_session` and handle `invoice.payment_action_required`.
- **PCI DSS:** with Stripe Checkout or Payment Element, card data never touches your servers, so you are usually eligible for **SAQ A**. PCI DSS v4.0.1 changed SAQ A eligibility: script-integrity requirements 6.4.3/11.6.1 were removed and replaced by a criterion that your site is protected against script attacks (**VERIFY with Stripe's annual PCI attestation in the dashboard**). Never log or store the full card number or CVC. Stripe tokens and the last four digits are fine.
- **Stripe's GDPR role:** Stripe's DPA (updated 18.11.2025) says Stripe acts as **processor** for the processing it does on your instructions. It acts as **independent controller** for its own purposes: choosing banks and payment-method providers, fraud monitoring and prevention, and legal and regulatory compliance such as AML/KYC. EU accounts contract with Stripe Payments Europe Ltd (Ireland). List Stripe in your privacy notice as both. Transfers to the US rely on the Stripe DPA, standard contractual clauses and the Data Privacy Framework (**VERIFY the current DPA text**).
- **Chargebacks:** respond in the Stripe dashboard with evidence: ToS acceptance, login and usage logs, cancellation policy. When a dispute is lost, issue a **fiscalized storno** (B2C) or a credit note (B2B eRačun) so that revenue and VAT are corrected.
- **Customer portal:**
  - Lets customers update billing address, VAT ID and payment method.
  - Make sure changes **do not rewrite issued invoices**. Fiscalized invoices are immutable (Art 14(2)); corrections need a storno and a new invoice.
  - For eRačun, a copy-indicator re-send is allowed only for corrections that do not affect tax (Art 43).
- **Billing data to store:** legal name, address, country, OIB (Croatian B2B), VAT ID with VIES proof (EU B2B), email, two pieces of location evidence (EU B2C), Stripe customer, payment intent and charge IDs, invoice number, JIR/ZKI or eRačun ID, and payment date (for eIzvještavanje).
- **AML (ZSPNFT):** a SaaS seller is not an obliged entity under the AML/CFT Act. Practical exposure is limited to the cash rules:
  - between obligated fiscalization payers, cash is capped at **€700 per invoice** (Fiscalization Act Art 30(3)); cash above the cash limit must be banked the same or next working day (Art 30(6));
  - the general AML ban on accepting cash of €10,000 or more (**VERIFY the amount in the current ZSPNFT**).
  
  Stripe performs KYC on *you*.

---

## 6. Business form and registration for online selling

- **Forms:**
  - obrt: e-Obrt / the trades register (obrtni registar);
  - paušal: choose the scheme at registration;
  - j.d.o.o. / d.o.o.: court register, through START or a notary. Initial capital is €2,500 for d.o.o., and ≥ €1 for j.d.o.o. with mandatory profit reserves (**VERIFY**).
- **Activity codes (NKD 2025** has been in force since 1.1.2025, NN 47/2024, aligned with NACE Rev 2.1):
  - **62.10** computer programming (replaces 62.01);
  - **58.29** other software publishing;
  - **63.10** computing infrastructure, data processing, hosting (replaces 63.11).
  
  Several codes may be registered. Use the one that matches the premises' activity when registering business premises.
- **Web shop registration:** no special licence or Državni inspektorat (State Inspectorate) notification was found for selling services online. The usual information duties under the E-Commerce Act (Zakon o elektroničkoj trgovini) and consumer law apply: identity, OIB, registry data, contact details, prices and terms. **VERIFY there is no new notification duty.** The EU ODR platform was shut down in July 2025 under Regulation (EU) 2024/3228, so ODR links are no longer required (**VERIFY**).
- **Prices:** shown in EUR, including VAT for consumers (see 3.6).
- **Tax registrations:**
  - PU registration (RPO); this is automatic with registration.
  - **PDV-ID** if you sell B2B to the EU or buy services from abroad.
  - **OSS** when you pass €10k in EU B2C, or voluntarily.
  - **Fiscalization:** certificate, internal act, premises registration in FiskAplikacija, software maker's OIB, eRačun receiving address in AMS (mandatory since 2026, even for paušalists), and authorisations for the intermediary.

---

## 7. Mandatory notifications to PU (summary)

1. Register business premises ("internetska trgovina") **before the first B2C invoice**, and report every change before it applies (Art 16).
2. Report the software maker's or maintainer's OIB (Art 17).
3. Get a fiscalization certificate (Art 10).
4. Register the eRačun receiving identifier in AMS (Art 44). Penalties for failing to do so have applied since 2026 (Art 73(1)(19)).
5. Authorise the intermediary in FiskAplikacija (eOvlaštenja).
6. P-PDV form within 8 days of passing €60,000.
7. PDV-ID application before the first EU B2B supply or foreign service purchase.
8. Form e-trgovina by 20.1, or within 8 days of passing €10k. OSS registration if applicable.
9. Monthly e-reporting of eRačun payments by the 20th (Art 53).
10. PDV / ZP / PDV-S returns by the **last day of the following month** (from 2026).

---

## 8. Income tax of the business and its owner (brief; VERIFY all figures; detail in `croatia:hr-business-admin`)

- **Paušalni obrt:** fixed tax by bracket, €203.40–€1,080 a year in 2026, paid quarterly. Contributions about €290.98 a month in 2026 on a base of €797.20 (Liber). Expenses are not recognised. Changes are planned from 2027 for brackets above €40k.
- **Obrt na dohodak:** taxed on actual profit at the local lower and higher rates (municipal ranges from the 2024 reform, roughly 15–23% / 25–33%, with the higher rate above about €60k a year) (**VERIFY**). Contributions about €472.84 a month in 2026 on a minimum base of €1,295.45 (Zakon o doprinosima čl. 66; NN 150/2025).
- **d.o.o. / j.d.o.o.:** profit tax 10% up to €1M revenue, 18% above. Dividends taxed at 12% (ZPD čl. 70 st. 19, since 2024). A director who is not employed elsewhere owes contributions (2026 base €1,993.00) even without a salary.

---

## 9. Practical "what to do" by business form

| Obligation | Paušalni obrt (non-VAT) | Obrt na dohodak / j.d.o.o., non-VAT | d.o.o. VAT payer |
|---|---|---|---|
| B2C fiscalization (all payment methods) | **Yes, since 1.1.2026** | Yes | Yes |
| Fiscal certificate, internal act, premises "internetska trgovina", software OIB | Yes | Yes | Yes |
| Croatian VAT on Croatian B2C | No: "oslobođeno čl. 90 st. 1" | No | 25% |
| Receive eRačun (AMS address) | **Yes, since 2026** (MIKROeRAČUN allowed) | Yes (MIKROeRAČUN allowed) | Yes (intermediary or own access point) |
| Issue eRačun to Croatian businesses | **From 1.1.2027.** PDF until then | From 1.1.2027 | **Since 1.1.2026**, or use the Art 39 card route |
| e-reporting of payments and rejections | From when eRačun duties start; rejections already for incoming eRačuni | Same | Yes |
| KPD codes on eRačun lines | From 2027 | From 2027 | Yes |
| PDV-ID for EU B2B or foreign services | **Yes**, required before the first such transaction | Yes | Already has one (HR + OIB) |
| PDV / ZP / PDV-S returns | Only for months with EU B2B supplies or reverse-charged purchases | Same | Monthly or quarterly as normal |
| EU B2C e-services | ≤ €10k: Croatian place of supply, exempt, **fiscalize**. > €10k: OSS with foreign VAT; cross-border SME "EX" scheme possible | Same | ≤ €10k: Croatian 25% and fiscalize. > €10k: OSS and no fiscalization |
| Input VAT deduction | None, and self-assessed reverse charge is a cost | None | Yes |
| Books | KPR and PO-SD | KPI/DI (obrt) or double entry (j.d.o.o.) | Double entry, annual financial statements (GFI) |
| Retention | OPZ ≈ 10 years from limitation start; eRačun 6 years | Same; Accounting Act 11 years for j.d.o.o. | 11 years (Accounting Act); eRačun 6 years; statements permanently |
| €60k limit | Passing it ends paušal status and triggers VAT registration | Triggers VAT registration | — |

---

## 10. Sample compliant B2C invoice (VAT-payer d.o.o., Croatian consumer, card payment) — fictitious example data

```
PRIMJER d.o.o. za računalne usluge
Ulica 1, 10000 Zagreb · OIB: 12345678901 · PDV ID: HR12345678901
Upisano u sudski registar Trgovačkog suda u Zagrebu, MBS: 0812345678
Temeljni kapital: 2.500,00 EUR, uplaćen u cijelosti · Uprava: Ivan Horvat
IBAN: HR12 2340 0091 1100 0000 1 (Banka d.d.)

RAČUN br.: 154/WEB1/1
Datum i vrijeme izdavanja: 05.10.2026. 14:32
Datum isporuke / razdoblje usluge: 05.10.2026. – 04.11.2026.
Mjesto izdavanja: Zagreb (internetska trgovina)

Kupac: Ana Anić, Ulica 2, 21000 Split, Hrvatska   [OIB not required for consumers]

| Opis                               | Kol. | Jed. cijena bez PDV-a | Stopa | Iznos bez PDV-a |
| Pretplata "Pro" – mjesečna (SaaS)  | 1    | 16,00 EUR             | 25 %  | 16,00 EUR       |

Osnovica 25 %: 16,00 EUR · PDV 25 %: 4,00 EUR · UKUPNO ZA PLATITI: 20,00 EUR
Način plaćanja: Kartica (online, Stripe)
Oznaka operatera: WEB (OIB operatera povezan internim aktom)
ZKI: 1a2b3c4d5e6f…   JIR: 9f8e7d6c-…-…
[QR kod]
Račun je izdan elektroničkim putem i valjan je bez potpisa i pečata.
```

**Variants:**
- **Paušalist:** drop the PDV-ID, rate and VAT lines. Add "Obveznik nije u sustavu PDV-a; oslobođeno PDV-a temeljem čl. 90. st. 1. Zakona o PDV-u." Show the obrt name, owner and address instead of the court-registry data.
- **EU B2B:** buyer's VAT ID, both VAT IDs shown, "Prijenos porezne obveze / reverse charge – čl. 17. st. 1. Zakona o PDV-u (čl. 196. Direktive 2006/112/EZ)". No JIR, no QR.
- **OSS B2C:** customer-country VAT rate and amount. No JIR is needed; issuing one voluntarily is allowed.

---

## 11. Common mistakes and penalties (Fiscalization Act Arts 71–73, verified)

| Offence | Legal entity | Responsible person | Obrtnik / self-employed |
|---|---|---|---|
| **Most serious (Art 71):** pre-invoice document without "OVO NIJE FISKALIZIRANI RAČUN"; not issuing, receiving or fiscalizing eRačun; software that allows evasion | €3,980 – €66,360 | €660 – €6,630 | €3,980 – €39,810 |
| **Serious (Art 72):** not fiscalizing all activities; invoices missing Art 7 data (JIR, ZKI, QR, payment method, time); no certificate; no electronic device; not depositing cash; not fiscalizing eRačun on time | €2,650 – €66,360 (repeat €3,500 – €80,000) | €390 – €6,630 (repeat €500 – €8,000) | €1,320 – €39,810 (repeat €2,000 – €45,000) |
| **Minor (Art 73):** wrong numbering; no internal act; buyer OIB missing in Art 39 receipts; premises not reported or incomplete; software OIB not reported; outage invoices not sent within 2 days; storno not done properly; eRačun not kept 6 years; wrong KPD; AMS identifier not registered; e-reporting late | €1,320 – €26,540 (repeat €2,500 – €35,000) | €260 – €2,650 | €660 – €13,270 for points 1–5 and 7–14 (repeat €1,000 – €20,000) |
| Buyer not keeping the invoice (Art 73(5)) | — | — | Buyer: €30 – €260 |

On top of fines, PU may **seal the business for up to 8 days** if B2C fiscalization is not carried out (Art 66).

**Typical mistakes for an online SaaS:**
1. A paušalist assumes card or bank-transfer B2C sales need no fiscalization, or that MIKROeRAČUN covers B2C. Neither is true.
2. Stripe invoice numbers used as the legal number: wrong format, gaps from voided drafts.
3. No premises registered before the first sale.
4. Stripe receipts or "paid" invoices sent before the fiscalized invoice exists, without the Art 29 text.
5. Selling to EU businesses without a PDV-ID or without ZP/PDV returns.
6. Ignoring the reverse charge on taxable foreign SaaS inputs (paušalist).
7. Not tracking the €10k EU B2C threshold and €60k domestic threshold in EUR.
8. Refunds and chargebacks without a fiscalized storno.
9. No AMS receiving address (mandatory since 2026, even for paušalists).
10. Deleting invoice data on GDPR erasure requests.

**VERIFY:** separate VAT/invoice penalties (for example failing to issue an invoice, or wrong content) are in OPZ's misdemeanour provisions; exact ranges were not confirmed.

---

## 12. Open items to verify with an accountant / PU (pisitenam.porezna-uprava.hr)
1. Whether B2C e-services to **non-EU consumers** are outside fiscalization. PU's legal-services Q&A supports this; the HOK leaflet suggests otherwise.
2. Correct **KPD 2025** code for SaaS subscriptions.
3. Exact **QR content** and any rulebook changes in **NN 97/2026**.
4. How PU treats Stripe's automatic receipts and hosted invoices under Art 29.
5. Which Stripe fees are taxable, and the reverse-charge mechanics for a paušalist.
6. Final 2027 paušal and income-tax changes (draft bills reported Jul–Sep 2026).
7. OPZ article numbers for retention and limitation; ZTD article for company-letter and invoice data.
8. Price-display articles in the Consumer Protection Act; status of the ODR link duty.

---

## Sources
- Zakon o fiskalizaciji, NN 89/2025 (full text, read in full): https://narodne-novine.nn.hr/clanci/sluzbeni/2025_06_89_1233.html ; https://www.zakon.hr/z/3960/zakon-o-fiskalizaciji
- PU, "Pitanja i odgovori vezani uz Zakon o fiskalizaciji" (PDF): https://porezna-uprava.gov.hr/UserDocsImages/Fiskalizacija/Fiskalizacija_eRacun/Pitanja%20i%20odgovori%20vezani%20uz%20Zakon%20o%20fiskalizaciji.pdf
- PU, B2C Q&A page (updated 30.1.2026): https://porezna-uprava.gov.hr/hr/fiskalizacija-racuna-u-krajnjoj-potrosnji-b2c-poslovanje/8033
- PU, eRačun fiscalization Q&A (updated 5.6.2026): https://porezna-uprava.gov.hr/hr/fiskalizacija-eracuna-azurirano-17-4-2026/8049
- Pravilnik o fiskalizaciji računa u krajnjoj potrošnji, NN 153/2025: https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_153_2278.html ; amendment NN 97/2026: https://www.zakon.hr/c/podzakonski-propis/1420916/
- HOK leaflet "Paušalni obrtnici i fiskalizacija od 1.1.2026.": https://www.hok.hr/sites/default/files/page-docs/2025-12/LETAK%20-%20Pau%C5%A1alni%20obrtnici%20i%20Fiskalizacija%202.0.pdf
- Fiskalopedija, paušalni obrt and Fiskalizacija 2.0: https://fiskalopedija.hr/baza-znanja/fiskalizacija-20-pausalni-obrt ; EU invoicing: https://fiskalopedija.hr/baza-znanja/izdavanje-racuna-inozemstvo-unutar-eu
- RRiF, "Posebni postupak oporezivanja za male porezne obveznike od 1.1.2025.": https://www.rrif.hr/posebni_postupak_oporezivanja_za_male_porezne_obve-4114-misljenje/
- RRiF, NN 151/2025 summary: https://www.rrif.hr/zakon_o_izmjenama_i_dopunama_zakona_o_porezu_na_do-6494-propis/ ; Finacro summary: https://finacro.hr/good-to-know/kljucne-izmjene-zakona-o-pdv-u-od-01-01-2026/
- TEB, Ulazak u sustav PDV-a 2025: https://www.teb.hr/novosti/2025/ulazak-u-sustav-pdv-a-u-2025/ ; PDV na elektronički obavljene usluge: https://www.teb.hr/novosti/2024/pdv-na-elektronicki-obavljene-usluge/ ; Čuvanje računa (2026): https://www.teb.hr/novosti/2026/cuvanje-racuna-i-knjigovodstvene-dokumentacije/
- PU OSS page: https://porezna-uprava.gov.hr/hr/pdvoss/4693
- ZPDV Art 79 text: https://www.pdvaktualno.hr/33/clanak-79-obvezni-sadrzaj-racuna-uniqueidmRRWSbk196E4DjKFq6pChG6vuuclhFodw1yePAXzd-yiKebrrbyYXg/ ; Raverus summary: https://www.raverus.hr/DobroJeZnati/RacunSadrzaj
- NKD 2025 (DZS): https://web.dzs.hr/App/NKD_Browser/assets/docs/NKD_2025_struktura.pdf ; NN 47/2024
- PU KPD 2025: https://porezna-uprava.gov.hr/hr/klasifikacija-proizvoda-kpd-2025/7718
- Paušal 2026 figures (commercial source, VERIFY): https://www.knjigovodstvo-liber.com/clanci/pausalni-obrt ; 2027 reform news: https://www.poslovni.hr/hrvatska/od-1-sijecnja-2027-mijenjaju-porezi-i-doprinosi-za-dio-obrtnika-vazna-vijest-za-one-ciji-su-primici-do-40-000-eura-4550528
- Stripe, Croatian fiscalization support note: https://support.stripe.com/questions/invoice-fiscalization-in-croatia ; Stripe DPA: https://stripe.com/legal/dpa
- Third-party Stripe fiscalization tools (not endorsements): https://e-racuni.hr/hrracuni/stripe-invoicing/ ; https://fiskalio.net/