# Fiskalizacija 2.0 – eRačun exchange, eRačun fiscalization and eIzvještavanje ("F2")

Status: researched 2026-10-25. Primary sources: Zakon o fiskalizaciji NN 89/25 (Part III,
čl. 33–57), Pravilnik o eRačunu NN 11/26, *Tehnička specifikacija Fiskalizacija eRačuna i
eIzvještavanje* **v1.15 (6.2.2026)** (latest version found; PU updates it without notice – check
the change history), *Specifikacija osnovne uporabe eRačuna s proširenjima* (HR CIUS, version
dated **12.3.2026**), PU validator in use from **15.3.2026**, PU pages "Fiskalizacija eRačuna"
(updated 5.6.2026) and "Popis informacijskih posrednika" (updated 16.10.2026).
Legal scope (who issues/receives, OSS, Art 39 card option, penalties): `croatia:hr-legal-compliance`
reference 04 §1.6–1.8. This file is the technical HOW.

## 1. Three separate flows

| Flow | What | Channel | Deadline |
|---|---|---|---|
| **Exchange** (razmjena) | UBL 2.1 Invoice/CreditNote, EN 16931 + HR CIUS | access point → AMS/MPS lookup → AS4 → receiver's access point | at issue |
| **Fiscalization** (fiskalizacija eRačuna) | extracted data set → PU `EvidentirajERacun` | SOAP web service, signed XAdES-B | issuer: at issue (self-billing: 5 working days); receiver: within **5 working days** of receipt (Zakon čl. 48(3)–(4)) |
| **eIzvještavanje** | payment received (`EvidentirajNaplatu`), rejection (`EvidentirajOdbijanje`), supply without eRačun (`EvidentirajIsporukuZaKojuNijeIzdanERacun`) | SOAP web service, intermediary or FiskAplikacija (čl. 50) | payments and rejections by the **20th of the following month** (čl. 52(1), 53(1)); no-eRačun supplies on the čl. 48(3) timeline (čl. 51(3)) |

Fiscalization runs **separately** from the exchange; PU confirms the fiscalization message but
nothing is written onto the eRačun. An eRačun carries **no JIR, ZKI or QR** (PU Q&A; legal skill).

## 2. Integration options

1. **Use an information intermediary (informacijski posrednik)** – the normal route. The
   intermediary runs the access point, AMS/MPS registration, validation, AS4 exchange and, if
   authorised, the fiscalization and eIzvještavanje messages with its own certificate.
   - PU's list had **37 entries on 16.10.2026** (including Financijska agencija – FINA). Pick from
     the current list only: porezna-uprava.gov.hr → "Popis informacijskih posrednika". The list
     shows per service (eRačun + fiscalization, eIzvještavanje, MPS) what each is certified for.
   - Authorise it in **FiskAplikacija** (reached through ePorezna): receiving and fiscalization are
     separate authorisations. The method `eOvlastenjaFiskalizacije` (spec v1.15) lets software
     query who is authorised for an OIB.
   - Intermediaries expose their own REST/SOAP APIs and formats (UBL upload, JSON). Integration
     effort is in mapping your invoice model to HR CIUS UBL and handling status callbacks.
2. **Own access point** – implement AS4 (eRačun-AS4 profile), MPS/AMS, validation and the PU
   fiscalization service yourself. Intermediary requirements (Zakon čl. 59–62: Croatian OIB,
   ISO/IEC 27001, EU-only processing, PU conformity certificate) apply to anyone offering it as a
   service. **VERIFY** with PU what a taxpayer running an access point only for itself must
   certify. Realistic only for large issuers or software vendors.
3. **MIKROeRAČUN** – free PU app for **non-VAT** taxpayers: receiving (2026) and issuing (from
   1.1.2027). No API for bulk use, and **no B2C**.

Hybrid is common: own UBL generation + intermediary API for transport and fiscalization.

## 3. Exchange: AMS, MPS, AS4 (Pravilnik o eRačunu čl. 6–7; Zakon čl. 37, 44)

1. The sender's access point needs the recipient's identifier (normally the OIB, endpoint scheme
   `9934`).
2. DNS query to **AMS** (Adresar metapodatkovnih servisa) → N-APTR record with the URL of the
   recipient's **MPS** (metapodatkovni servis).
3. REST call to the MPS with the identifier → URL of the recipient's access point.
4. HTTPS + **AS4** per the agreed P-mode; eRačun and attachments in the AS4 message (SBDH header).
   Messages are signed with an application certificate; PU says AS4 is used with signing and
   without message-level encryption.
5. The receiving access point acknowledges, or returns an error if the content is not EN 16931
   compliant (it **must** reject non-compliant eRačuni and non-AS4 deliveries, čl. 7(2)–(3)).

- Every receiver must have published its identifier in AMS before receiving (Zakon čl. 44; done
  by the intermediary/MIKROeRAČUN and confirmed in FiskAplikacija).
- Recipient not found in AMS: the issuer is not liable, may issue a paper invoice and reports the
  data via eIzvještavanje (čl. 40, 51).
- Peppol: Croatia's domestic exchange uses its own eRačun-AS4 profile with AMS/MPS discovery
  (Pravilnik o eRačunu čl. 6–7), not the Peppol SML/SMP network. Some intermediaries on the PU list
  are also Peppol access points. **VERIFY** current interoperability (and whether scheme `9934`
  maps to the Peppol code list entry you expect) before assuming a Peppol AP can deliver to
  Croatian receivers.
- Cross-border B2B (EU or non-EU buyer): no eRačun and no eIzvještavanje obligation; a PDF or any
  agreed format is fine (PU Q&A, see legal skill). Sending UBL via Peppol is optional.

## 4. eRačun document (summary – details in `hr-cius-fields.md`)

- UBL 2.1 `Invoice` or `CreditNote`, EN 16931-1:2017 with HR CIUS and HR extensions (Zakon čl. 36).
- `cbc:CustomizationID` =
  `urn:cen.eu:en16931:2017#compliant#urn:mfin.gov.hr:cius-2025:1.0#conformant#urn:mfin.gov.hr:ext-2025:1.0`
- `cbc:ProfileID` = process type `P1`–`P12` or `P99:<buyer label>`.
- Currency EUR; issue time `cbc:IssueTime` hh:mm:ss; seller and buyer `cbc:EndpointID`;
  operator OIB and label in `cac:SellerContact`; **KPD 2025** code per line (`listID="CG"`) except
  prepayment invoices and credit notes; HR VAT category labels (`HR:PDV25`, `HR:E`, …).
- Invoice number: the Art 9 three-part numbering also applies to eRačuni (Zakon čl. 48(5)); BT-1
  allows separators such as `/`, `-`, `_` but no whitespace (spec v1.15 Table 7; HR-BR-1).
- Corrections that do not affect tax: resend under the same number with **copy indicator**
  (`cbc:CopyIndicator=true`) in the same tax period and fiscalize immediately (čl. 43). A resend
  without the copy indicator is treated as a technical duplicate and not delivered (PU page).
  Anything affecting tax: storno/credit note (381, process P9/P10) and a new invoice.
- PDF: a human-readable visualisation may be attached; **the XML is the invoice**. A PDF by
  e-mail is not an eRačun.

## 5. Fiscalization message: EvidentirajERacun (spec v1.15 §3)

- Service *eFiskalizacija*, namespace `http://www.porezna-uprava.gov.hr/fin/2024/types/eFiskalizacija`.
- `EvidentirajERacunZahtjev` (`Id` attribute) → `Zaglavlje{datumVrijemeSlanja, vrstaERacuna}` +
  1–100 `ERacun` + `Signature`.
  - `datumVrijemeSlanja`: `YYYY-MM-DDTHH:MM:SS.ssss` (**four** fractional digits, regex in spec).
  - `vrstaERacuna`: `I` outgoing (izlazni), `U` incoming (ulazni).
- `ERacun` mirrors the UBL (each field cites its XPath): `brojDokumenta` (BT-1), `datumIzdavanja`
  (BT-2), `vrstaDokumenta` (BT-3), `valutaERacuna` (EUR), `datumDospijecaPlacanja`,
  `vrstaPoslovnogProcesa` (BT-23), `referencaNaUgovor`, `datumIsporuke`, `PrethodniERacun`,
  `Izdavatelj{ime, oibPorezniBroj, oibOperatera (HR-BT-5)}`, `Primatelj`, `PrijenosSredstava`
  (IBAN), `DokumentUkupanIznos`, `RaspodjelaPdv{kategorijaPdv, oporeziviIznos, iznosPoreza, stopa,
  razlogOslobodenja (VATEX), tekstRazlogaOslobodenja, hrOznakaKategorijaPdv}`, `DokumentPopust`,
  `DokumentTrosak`, `StavkaERacuna{…, ArtiklIdentifikatorKlasifikacija (KPD)}`, `indikatorKopije`.
- The legal minimum data set is Zakon čl. 48(1) (dates, number, parties, quantities and KPD,
  delivery date, bases per rate, unit prices, discounts, VAT rate and amount, original invoice
  reference, payee account).
- Checks (spec Table 79): certificate (S003), signature (S002, S004), schema and code lists incl.
  IBAN format and exemption reason for `AE` (S005), OIB format and authorisation (S007, S011),
  access-point authorisation (S006), uniqueness per identifier + direction (S008 – the same number
  may exist once as `I` and once as `U`).
- Response `EvidentirajERacunOdgovor`: `Odgovor{idZahtjeva, prihvacenZahtjev true/false,
  greska{sifra, redniBrojZapisa, opis}}` – only the **first** error is returned.

## 6. eIzvještavanje (spec v1.15 §4–5)

Namespace `http://www.porezna-uprava.gov.hr/fin/2024/types/eIzvjestavanje`.

| Method | Key fields | Notes |
|---|---|---|
| `EvidentirajNaplatu` | `brojDokumenta, datumIzdavanja, oibPorezniBrojIzdavatelja, oibPorezniBrojPrimatelja, datumNaplate, naplaceniIznos, nacinPlacanja` (`T` transakcijski račun, `O` obračunsko plaćanje, `Z` ostalo) | requires a fiscalized outgoing eRačun (S009); several partial payments allowed; to correct, resend with negative amounts |
| `EvidentirajOdbijanje` | identifiers + `datumOdbijanja`, `vrstaRazlogaOdbijanja` (`N` mismatch not affecting tax, `U` affecting tax, `O` other), reason text | requires a fiscalized incoming eRačun (S009); duplicate → S010; reporting a rejection = statement that no input VAT is claimed (Zakon čl. 52(3)); the law sets no deadline for rejecting itself (PU page) |
| `EvidentirajIsporukuZaKojuNijeIzdanERacun` | `vrstaRacuna = IR` + čl. 48(1) data | for čl. 40 cases (recipient not in AMS) |
| `eOvlastenjaFiskalizacije` | OIB → list of authorised OIBs | since spec v1.15 |

Error code list (spec §5.7.1.2.1): S001 system error, S002 signature location wrong, S003
certificate not from trusted list/expired/revoked, S004 invalid signature, S005 schema, S006 access
point not authorised, S007 OIB not formally valid, S008 eRačun with same identifier already
recorded, S009 no recorded eRačun, S010 rejection already recorded, S012 no original eRačun for the
corrected one. (Upper-case `S`; different meanings from the F1 lower-case `s0xx` codes.)

## 7. Transport and signature (spec v1.15 §7–11)

| Environment | URL |
|---|---|
| Test | `https://cistest.apis-it.hr:8509/FiskalizacijaServiceEprod` |
| Production | `https://cis.porezna-uprava.hr:8509/FiskalizacijaService` |

- TCP port **8509**; SOAP 1.1 document-literal, UTF-8, 1-way TLS. The spec text still lists
  "TLS v1.1 i v1.2" (Table 128) while the F1 service drops TLS 1.1 on 1.1.2027 – use TLS 1.2+.
- The spec names the test server certificate `cistest.porezna-uprava.hr` but the URL uses
  `cistest.apis-it.hr` – **VERIFY** against the current WSDL before configuring TLS checks.
- Signature: **XAdES-B** (ETSI EN 319 132-1) enveloped in the root element; two `Reference`s (root
  by `Id` with enveloped-signature + exc-c14n transforms; `SignedProperties` with exc-c14n);
  SHA-256 digests; `rsa-sha256` in the spec examples; `KeyInfo/X509Data/X509Certificate`;
  `xades:SigningTime`, `SigningCertificateV2`. The spec includes a Java example using the EU DSS
  library; ETSI's signature conformance checker can validate.
- Certificate: application certificate with the OIB in the DN, from a trust-service provider; PU
  says there are no separate "Fiskal 1"/"Fiskal 2" certificate types. Test messages must use demo
  certificates.
- Recommended: 2 days of stable running on test before production (spec §10).

## 8. Archiving

- Keep issued and received fiscalized eRačuni in **original (XML) form for 6 years** from the end of
  the year of issue (Zakon čl. 35); the Accounting Act generally requires 11 years for invoices –
  see `croatia:hr-legal-compliance`. Practical rule: keep the signed XML, attachments, AS4
  receipts, fiscalization and eIzvještavanje request/response XML for 11 years, immutable
  (WORM/object-lock), with an index by OIB + number + date + direction.
- PU keeps the fiscal data after that (čl. 35(2)); taxpayers can see their data in FiskAplikacija
  (Pravilnik o eRačunu čl. 4(5)).

## 9. Timelines for code (Zakon čl. 80)

- 1.1.2026: VAT payers issue and receive eRačuni; everyone in scope (including non-VAT and
  paušalisti) must be able to **receive** and be in AMS.
- 1.1.2027: non-VAT taxpayers and budget users must **issue** eRačuni (MIKROeRAČUN or an
  intermediary); KPD and eIzvještavanje duties follow.
- Check the legal skill for the exact scope; this file does not decide who is obliged.
