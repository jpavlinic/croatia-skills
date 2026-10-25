# Testing, certificates for test, and error codes

Status: researched 2026-10-25. Sources: Tehnička specifikacija F1 v2.7 (§2.1.5, §2.5, §6, §13),
Pravilnik NN 153/25 Privitci 1–5, Tehnička specifikacija F2 v1.15 (§3.3, §5.7), PU notices.

## 1. F1 test environment

- URL: `https://cistest.apis-it.hr:8449/FiskalizacijaServiceTest` (WSDL package
  `Fiskalizacija-WSDL-EDUC_v1.10.zip`).
- Unavailable: working days 16:00–17:00, Sundays 08:00–12:00.
- Requires a **DEMO** certificate containing an OIB (FINA demo certificates are free, 2 years;
  request via `certifikati-fiskalizacija@fina.hr`). A software house may test with its own demo
  certificate (spec §6). Production certificates are rejected in test and vice versa.
- Since **1.7.2026** test rejects RSA-SHA1 signatures and TLS 1.1 – a good way to prove you are
  ready for the production cut-off on **1.1.2027**.
- Test response-signing certificate *fiskalcistest* was replaced in July 2026; refresh trust
  material when PU announces rotations (porezna.gov.hr → Fiskalizacija u krajnjoj potrošnji →
  Novosti).
- Working-hours methods on test need test premises opened on your demo-cert OIB: ask PU via
  "Pišite nam" (topic *Fiskalizacija u krajnjoj potrošnji (F1)*, subtopic *Tehnička podrška*) with
  the OIB and desired premises labels (spec §2.8).
- Recommended: at least **2 days** of continuous stable operation on test before production, also
  at the customer's site when a software house deploys for many taxpayers (spec §6).
- Technical support: `fiskalizacija.help@apis-it.hr`; legal/business: pisitenam.porezna-uprava.hr,
  0800 1001 (spec §10).

### Smoke-test sequence
1. `EchoRequest` → proves TLS and endpoint (no signature check).
2. `RacunZahtjev` with minimal data (`USustPdv=false`, one total, `NacinPlac=G`) → JIR.
3. Same receipt again with a new `IdPoruke` and `NakDost=true` → check behaviour for re-sends.
4. VAT receipt with 25 % and 5 % rates, a `Naknade` line, negative storno receipt.
5. `PromijeniPodatkeRacunaZahtjev` the same day → `p005`; next day → `s011`.
6. `NapojnicaZahtjev` → `p002`.
7. `ProvjeraZahtjev` (test only) on each → expect `v100`.
8. Fault injection: wrong OIB vs certificate (`s005`), broken signature (`s004`), date in the
   future (`s013` + 177), BrOznRac 0 (178), `T` with buyer OIB (181), VAT rate 10 % (182).
9. Offline: kill network, issue receipts, restore, confirm the backlog drains with `NakDost=true`
   and receipts printed with the `zki=` QR URL.

## 2. F1 error codes

Response `Greske/Greska/{SifraGreske, PorukaGreske}` (lower-case `s`).

| Code | Meaning | Typical fix |
|---|---|---|
| s001 | Message not valid against the XML schema (lists failing elements) | regenerate from XSD; check element order, date formats `dd.mm.yyyyThh:mm:ss`, decimals with `.` |
| s002 | Certificate not from a trust-service provider on the trusted list (eIDAS), expired or revoked | renew; using a demo cert in prod or prod cert in test |
| s003 | Certificate lacks a mandatory attribute (OIB) | certificate profile without OIB / `organizationIdentifier` |
| s004 | Invalid digital signature | XML changed after signing, wrong `Reference URI`, wrong c14n, unsupported algorithm (SHA1 on test since 1.7.2026; prod from 1.1.2027) |
| s005 | OIB in the request ≠ OIB in the certificate | wrong tenant certificate, or `Oib` field wrong |
| s006 | System error | retry with backoff; keep the receipt pending |
| s007 | (payment-method change) issue date ≠ today | after midnight: storno + new receipt |
| s008 | (payment-method change) data differ from the fiscalized receipt / not fiscalized | send the original data exactly |
| s009 | (tip) receipt date more than 2 days ago | – |
| s010 | (tip) data differ from the fiscalized receipt / not fiscalized | – |
| s011 | (change of receipt data) issue date ≠ today | storno + new receipt |
| s012 | (change of receipt data) data differ / not fiscalized | – |
| s013 | Receipt has **restrictive errors** (since 1.1.2026) – rejected, see below | fix data and re-send |

Restrictive errors inside `s013`: 176 issue date more than 30 days ago · 177 issue date/time in
the future · 178 BrOznRac is 0 · 179 operator OIB not formally valid · 180 buyer OIB not formally
valid · 181 buyer OIB with payment method `T` · 182 VAT rate not allowed (allowed 0, 5, 13, 25) ·
183 PNP rate < 0 % · 184 PNP rate > 3 %.

Success codes: `p001` payment-method change, `p002` tip, `p003` working hours reported, `p004`
working hours deleted, `p005` receipt data changed.

### Test-only validation codes (`ProvjeraZahtjev`, spec §13)
v100 OK · v101 send time vs receipt time differs > 6 h · v103 device clock wrong (> 6 h ahead) ·
v104 issue time later than send time · v112 VAT base > total · v114 VAT base sign ≠ total sign ·
v152 late 2–5 days · v153 late > 5 days · v160/v161 VAT amount off by > 0.10 € · v162/v163 PNP off
by > 0.10 € · v164 fee > 135 € · v166 total ≠ formula (±0.01 €) · v167 `T`/`O` total beyond
±150,000 € · v174 late 10 min–2 days · v176–v184 as restrictive errors · v185 cash/card total
beyond ±10,000 €. (v106 removed in v2.7.)

## 3. F2 test environment and codes

- Test: `https://cistest.apis-it.hr:8509/FiskalizacijaServiceEprod`; production:
  `https://cis.porezna-uprava.hr:8509/FiskalizacijaService` (spec v1.15 §10.1). Port 8509.
- Pravilnik o eRačunu čl. 2 names a controlled test environment "CIS DEMO" for applications and
  integrations. Intermediaries also provide sandboxes (e.g. FINA e-Račun demo environment) – use
  the intermediary's sandbox for exchange tests and PU test for direct fiscalization.
- Validate UBL with the PU validator (version in use from 15.3.2026) before sending.
- Error codes (upper-case `S`): S001 system error · S002 signature location wrong · S003
  certificate not trusted/expired/revoked · S004 invalid signature · S005 schema / code list ·
  S006 access point not authorised for this OIB (check FiskAplikacija authorisation) · S007 OIB not
  formally valid · S008 eRačun with same identifier already recorded · S009 no recorded eRačun
  (payment/rejection before fiscalization) · S010 rejection already recorded · S012 no original
  for a corrected eRačun. Only the first error is returned, with `redniBrojZapisa`.

## 4. Sample F1 request (spec §9.1, trimmed)

```xml
<!-- TEMPLATE – not legal advice. Spec example values; sign before sending. -->
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
 <soapenv:Body>
  <tns:RacunZahtjev xmlns:tns="http://www.apis-it.hr/fin/2012/types/f73" Id="RacunZahtjev">
   <tns:Zaglavlje>
    <tns:IdPoruke>f81d4fae-7dec-11d0-a765-00a0c91e6bf6</tns:IdPoruke>
    <tns:DatumVrijeme>25.10.2026T14:03:05</tns:DatumVrijeme>
   </tns:Zaglavlje>
   <tns:Racun>
    <tns:Oib>12345678903</tns:Oib>
    <tns:USustPdv>true</tns:USustPdv>
    <tns:DatVrijeme>25.10.2026T14:03:00</tns:DatVrijeme>
    <tns:OznSlijed>P</tns:OznSlijed>
    <tns:BrRac><tns:BrOznRac>15</tns:BrOznRac><tns:OznPosPr>POSL1</tns:OznPosPr><tns:OznNapUr>2</tns:OznNapUr></tns:BrRac>
    <tns:Pdv><tns:Porez><tns:Stopa>25.00</tns:Stopa><tns:Osnovica>116.54</tns:Osnovica><tns:Iznos>29.14</tns:Iznos></tns:Porez></tns:Pdv>
    <tns:IznosUkupno>145.68</tns:IznosUkupno>
    <tns:NacinPlac>K</tns:NacinPlac>
    <tns:OibOper>98765432106</tns:OibOper>
    <tns:ZastKod><!-- 32 hex from zki.py --></tns:ZastKod>
    <tns:NakDost>false</tns:NakDost>
   </tns:Racun>
   <!-- <Signature xmlns="http://www.w3.org/2000/09/xmldsig#"> … enveloped, exc-c14n, rsa-sha256 … </Signature> -->
  </tns:RacunZahtjev>
 </soapenv:Body>
</soapenv:Envelope>
```
OIBs are fictitious, checksum-valid examples. Successful response: `tns:RacunOdgovor` with
`tns:Jir` (UUID).
