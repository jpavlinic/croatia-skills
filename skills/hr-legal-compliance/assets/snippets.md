PREDLOŽAK – nije pravni savjet. Prilagodite ga svom slučaju i dajte ga na provjeru stručnjaku.

# Ready-to-use snippets (Croatian) + implementation patterns

Every snippet you hand to a user as a document or published text keeps the line above at its top until a
professional has reviewed it. Address one reader with the polite capital Vi/Vaš/Vam.

Cross-references: cookie banner / cookie table / newsletter checkbox / marketing footer / soft-opt-in notice /
B2B cold email / "can I send this email?" decision tree → `references/02-cookies-marketing-contacting.md` §7.
Impressum (d.o.o. + obrt) → `references/03-consumer-contracts-terms.md` deliverable (d).
Invoice layout → `references/04-tax-fiscalization-payments.md` §10.

---

## 1. Registration form (B2B service that may also reach consumers)

```
[ Ime i prezime ] [ E-adresa ] [ Naziv tvrtke (opcionalno) ] [ Lozinka ]

Voditelj obrade je [Tvrtka], OIB [..]. Podatke obrađujemo radi izvršenja ugovora o korištenju usluge.
Više o obradi, rokovima čuvanja i Vašim pravima: [Politika privatnosti].

☐ Prihvaćam [Opće uvjete korištenja] i potvrđujem da imam najmanje 16 godina.        (obvezno, NEoznačeno)

Povremeno ćemo Vam e-poštom slati savjete i ponude za [Naziv]. Od tih se poruka
možete odjaviti jednim klikom u svakoj poruci.
☐ Ne želim primati savjete i ponude e-poštom.                                         (soft opt-in, ZEK čl. 50. st. 2.)
   — ILI, sigurnije —
☐ Želim primati savjete, novosti i ponude e-poštom.                                    (privola, NEoznačeno)

[ Izradi račun ]
```

Store on submit (table `consents` or columns): `user_id, kind (TERMS|PRIVACY_NOTICE|MARKETING), granted bool,
document_version, text_hash, created_at, ip (truncated), user_agent, source (signup|google|settings|checkout)`, `withdrawn_at`.
Google one-tap sign-up must go through the same acceptance step before the account is created.

## 2. Checkout block for consumers (ZZP čl. 74, 77; see references/03 §1.4–1.6)

```
Plan PRO – 29,00 EUR mjesečno (uključen PDV 25 %) za 1 korisnika; svaki dodatni korisnik [X] EUR mjesečno.
Pretplata se automatski produljuje svaki mjesec dok je ne otkažete. Otkazati možete u svakom trenutku u
postavkama računa, s učinkom na kraju tekućeg razdoblja. Nema minimalnog trajanja.

☐ Izričito zahtijevam da pružanje Usluge započne odmah, prije isteka roka od 14 dana za jednostrani raskid
  ugovora. Upoznat/a sam s time da ću, ako jednostrano raskinem ugovor u tom roku, biti dužan/dužna platiti
  razmjerni dio cijene za razdoblje do raskida te da ću izgubiti pravo na jednostrani raskid ugovora kada
  Usluga bude u potpunosti ispunjena.

[ Naruči s obvezom plaćanja ]
```
Business buyers: radio "Kupujem kao: ○ fizička osoba (potrošač) ○ poslovni subjekt (OIB / PDV ID)".
With a hosted checkout (e.g. Stripe Checkout): `consent_collection.terms_of_service=required` + `custom_text.terms_of_service_acceptance`
+ `custom_text.submit` for the payment-obligation wording; the provider's own localized button text (e.g. "Pretplati se" / "Plati") – verify
that it is unambiguous ("Plati" / "Pretplati se" are commonly treated as a "sličan nedvojben izraz", **VERIFY**;
keep the above summary text directly above it).

## 3. "Raskid ugovora" withdrawal function (ZZP čl. 81.a – in force 19 June 2026)

- Link **„Raskid ugovora”** in the site footer AND in Account → Billing, available during the 14-day period.
- Step 1 form: „Ime i prezime”, „E-adresa računa / broj narudžbe”, „E-adresa za potvrdu”.
- Step 2 button: **„Potvrditi raskid ugovora”**.
- Immediately send: „Zaprimili smo Vašu izjavu o jednostranom raskidu ugovora o pružanju usluge [Naziv], podnesenu
  [DD. MM. GGGG.] u [hh:mm]. Sadržaj izjave: [..]. Povrat iznosa od [X] EUR izvršit ćemo najkasnije u roku od 14 dana
  na isto sredstvo plaćanja. Svoje podatke možete izvesti do [datum].”
- Backend: record request (timestamp), cancel the subscription at the payment provider, compute pro-rata, refund to
  the same payment method, fiscalize a storno invoice (references/04 §1.4; implementation: `croatia:hr-fiscalization-dev`),
  keep the record ≥ limitation period.

## 4. Model withdrawal form (Prilog 1)
See `references/03-consumer-contracts-terms.md` deliverable (c4).

## 5. Email footers

**Service/transactional email** (no unsubscribe required, but identity is good practice and ZET čl. 6):
```
—
[Naziv] · [Tvrtka d.o.o.], [ulica i broj], [grad] · OIB [..]
Ovu poruku primate jer imate korisnički račun na [Naziv]. Riječ je o obavijesti vezanoj uz Vaš račun.
```

**Marketing / promotional email** (trial offers, discounts, newsletters, "upgrade" nudges):
```
—
Ovu poruku šalje [Tvrtka d.o.o.], [adresa], OIB [..], upisan u sudski registar Trgovačkog suda u [..], MBS [..].
Primate je jer ste [koristili probno razdoblje usluge [Naziv] / se prijavili na novosti].
[Odjava jednim klikom] · [Postavke obavijesti]
```
Headers (RFC 8058; also required by Gmail/Yahoo for bulk senders):
```
List-Unsubscribe: <https://app.example.hr/u/{signedToken}>, <mailto:unsubscribe@example.hr?subject=unsub-{token}>
List-Unsubscribe-Post: List-Unsubscribe=One-Click
```
Implementation: signed, non-expiring token per user+category; POST endpoint flips `marketing_opt_out=true`
without login; suppression check in the send path (`if (!user.marketingAllowed()) skip`), not only a global flag.

Classify each template (references/02 §4.4): neutral "trial ends on X / what happens next" = service;
anything with a discount, coupon, "upgrade now" CTA or win-back = marketing.

## 6. Contact form notice
```
Podatke iz obrasca koristimo isključivo kako bismo odgovorili na Vaš upit (čl. 6. st. 1. t. b) i f) GDPR-a)
i čuvamo ih [3 godine]. Obrazac obrađuje [pružatelj, lokacija]. Više u [Politici privatnosti].
```
Phone field optional unless genuinely needed.

## 7. Results footer for exported reports (professional tools only; see references/03 §6)
```
Izrađeno alatom [Naziv] v[x.y] ([datum]) prema [propis / norma / metodologija, verzija].
Rezultate provjerava i za njih odgovara osoba koja potpisuje dokument.
```

## 8. Art 28 DPA (Ugovor o obradi podataka) — skeleton for a SaaS offering it to B2B customers
1. Predmet, trajanje, narav i svrha obrade (Prilog A: kategorije podataka – npr. imena i kontaktni podaci klijenata
   korisnika, sadržaj koji korisnik unosi; kategorije ispitanika – klijenti, zaposlenici ili partneri korisnika).
2. Obrada samo prema dokumentiranim uputama (ugovor + konfiguracija usluge = upute); obavijest ako je uputa protupropisna.
3. Povjerljivost osoba ovlaštenih za obradu.
4. Tehničke i organizacijske mjere (Prilog B: TLS, šifriranje kopija, MFA, pristup po ulogama, revizijski zapis,
   maskiranje dnevnika, testovi povrata).
5. Podizvršitelji: opće pisano ovlaštenje, javni popis [URL], obavijest 30 dana unaprijed, pravo prigovora,
   prijenos istih obveza; Prilog C popis (hosting, e-pošta, dnevnici, CDN).
6. Pomoć pri ostvarivanju prava ispitanika (izvoz, brisanje).
7. Povrede: obavijest voditelju bez odgađanja, najkasnije u roku od [48] sati od saznanja.
8. Pomoć pri DPIA i prethodnom savjetovanju.
9. Brisanje ili vraćanje podataka po prestanku ugovora ([30] dana izvoz, zatim brisanje; kopije za [35] dana).
10. Revizije i informacije (upitnik/izvješće; pregled na licu mjesta uz najavu 30 dana, o trošku voditelja).
11. Prijenosi izvan EGP-a (DPF / SKK modul 3) i TIA.
12. Odgovornost, mjerodavno pravo (RH), prednost DPA pred Uvjetima u pitanjima zaštite podataka.
Optional base: EU Commission SCCs for Art 28 (Implementing Decision (EU) 2021/915).

## 9. Retention schedule (machine-checkable starting point)
```yaml
account_and_projects:       { keep: "contract + 30d", then: hard_delete, job: daily }
unconverted_trial:          { keep: "trial_end + 12mo inactivity", warn: [30d, 7d], then: hard_delete }
trial_abuse_email_hash:     { keep: "24mo", then: delete }        # document LIA; not "forever"
invoices_and_billing_ledger:{ keep: "11y from end of FY (eRačun 6y)", basis: "ZoR čl. 10; ZoF čl. 35; OPZ čl. 66" }
terms_acceptance_records:   { keep: "contract end + 5y (B2B 3y)", basis: "ZOO čl. 225, 228" }
marketing_consent_proof:    { keep: "while used + 4y", basis: "ZEK čl. 174 zastara" }
suppression_list:           { keep: "while marketing is sent", store: email_hash }
consumer_complaints:        { keep: "1y", basis: "ZZP čl. 10. st. 7." }
app_logs_raw:               { keep: "30d" }
security_audit_logs:        { keep: "12mo" }
backups:                    { keep: "≤35d rolling", encrypted: true, offsite: true }
auth_tokens:                { keep: "until expiry", then: purge_daily }   # incl. refresh tokens
```
