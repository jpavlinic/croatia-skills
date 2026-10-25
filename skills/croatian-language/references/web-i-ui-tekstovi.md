# Web i UI tekstovi

Za tekstove u sučelju: gumbi, izbornici, obrasci, poruke o pogrešci,
obavijesti, i18n datoteke (`hr.json`, `messages/hr.ts`), meta opisi.

## Osnovna načela

1. **Jedan način obraćanja kroz cijelu aplikaciju.** Ili „Vi” (Pošaljite,
   Vaša narudžba) ili „ti” (Pošalji, tvoja narudžba). Neutralni oblici
   (imenice, infinitiv u naslovu) rade s oba.
2. **Sentence case:** „Zaboravljena lozinka”, ne „Zaboravljena Lozinka”.
3. **Kratko i glagolom:** gumb kaže što se dogodi: „Spremi promjene”, „Pošalji
   upit”, „Preuzmi račun”, ne „OK” ili „Potvrda”.
4. **Gumbi u 2. licu jednine imperativa** („Spremi”, „Odustani”, „Prijavi
   se”) su uvriježeni i u aplikacijama koje inače koriste „Vi”. Ako brend
   dosljedno koristi Vi, može i „Spremite”, „Pošaljite”, ali tada svugdje.
5. **Bez „Vaš” svugdje:** „Unesite e-adresu”, „Potvrdite svoju lozinku”
   (povratno „svoj” kad je korisnik subjekt). „Vaš” ostaje kad je posvojnost
   važna: „Vaša narudžba je poslana.”
6. **Bez nepotrebnog engleskog** gdje postoji ustaljen hrvatski izraz.

## Pojmovnik sučelja

| Engleski | Hrvatski |
|---|---|
| Home | Početna |
| About us | O nama |
| Contact | Kontakt |
| Log in / Sign in | Prijava / Prijavi se |
| Log out | Odjava / Odjavi se |
| Sign up / Register | Registracija / Registriraj se |
| Create account | Izradi račun |
| Forgot password? | Zaboravili ste lozinku? |
| Reset password | Ponovno postavi lozinku / Nova lozinka |
| Password | Lozinka |
| Username | Korisničko ime |
| Email (address) | E-adresa / adresa e-pošte |
| Email (message) | e-poruka / e-mail |
| Profile | Profil |
| Account | Račun / Korisnički račun |
| Settings | Postavke |
| Dashboard | Nadzorna ploča / Pregled |
| Search | Pretraži / Pretraživanje |
| Filter / Sort | Filtriraj / Poredaj |
| Save | Spremi |
| Save changes | Spremi promjene |
| Cancel | Odustani |
| Delete | Izbriši / Obriši |
| Edit | Uredi |
| Add | Dodaj |
| Remove | Ukloni |
| Close | Zatvori |
| Back | Natrag |
| Next / Continue | Dalje / Nastavi |
| Previous | Prethodno |
| Submit | Pošalji |
| Confirm | Potvrdi |
| Upload | Učitaj / Prenesi |
| Download | Preuzmi |
| Share | Podijeli |
| Copy | Kopiraj |
| Learn more / Read more | Saznajte više / Saznaj više; Pročitajte više / Pročitaj više |
| Get started | Započni / Započnite |
| Show more / less | Prikaži više / manje |
| Loading… | Učitavanje… |
| Required field | Obvezno polje |
| Optional | Neobvezno |
| Error | Pogreška |
| Something went wrong | Nešto je pošlo po zlu. / Došlo je do pogreške. |
| Try again | Pokušaj ponovno / Pokušajte ponovno |
| Success | Uspješno |
| Saved | Spremljeno |
| No results | Nema rezultata |
| Page not found (404) | Stranica nije pronađena |
| Cart | Košarica |
| Checkout | Plaćanje / Dovrši narudžbu |
| Order | Narudžba |
| Add to cart | Dodaj u košaricu |
| Shipping | Dostava |
| Invoice | Račun |
| Quote / Offer | Ponuda |
| Subscribe | Pretplati se |
| Unsubscribe | Odjavi se (s popisa) / Otkaži pretplatu |
| Newsletter | Newsletter / Bilten |
| Notifications | Obavijesti |
| Privacy policy | Politika privatnosti / Pravila privatnosti |
| Terms of service | Uvjeti korištenja |
| Cookies | Kolačići |
| Accept all / Reject all | Prihvati sve / Odbij sve |
| Cookie settings | Postavke kolačića |
| Legal notice / Imprint | Impressum / Podaci o tvrtki |
| FAQ | Česta pitanja |
| Blog post | Članak / Objava |
| Link | Poveznica (u prozi može „link”) |
| Website | Web-stranica / mrežna stranica |
| Web page | Stranica |
| App | Aplikacija |
| Feature | Značajka / Mogućnost |
| Update | Ažuriranje / Ažuriraj |
| Online | Online / na mreži |

Napomena: IHJJ preporučuje **obvezno** (od „obveza”); „obavezno” je raširenije
i nije pogrešno, ali drži jedan oblik u cijelom projektu.

## Poruke o pogrešci i obavijesti

- Reci što se dogodilo i što korisnik može napraviti, bez krivnje:
  - „Lozinka mora imati najmanje 8 znakova.”
  - „E-adresa nije ispravna. Provjerite je li upisana bez razmaka.”
  - „Ova e-adresa je već registrirana. Želite li se prijaviti?”
  - „Veza s poslužiteljem nije uspjela. Pokušajte ponovno za nekoliko
    trenutaka.”
- Ne: ~~„Greška 500!!!”~~, ~~„Neispravan input”~~, ~~„Invalid email”~~.
- „Pogreška” je normativno preporučeno, „greška” je razgovorno i prihvatljivo u
  opuštenom tonu.
- Potvrde: „Promjene su spremljene.”, „Poruka je poslana. Javit ćemo Vam se u
  roku od jednog radnog dana.”
- Prazna stanja: „Još nemate narudžbi.”, „Ovdje će se pojaviti Vaše
  obavijesti.”

## Obrasci

- Oznake polja kao imenice: „Ime i prezime”, „E-adresa”, „Broj telefona”,
  „Poruka”, „OIB”, „Adresa”, „Poštanski broj”, „Mjesto”.
- Placeholderi kao primjer, ne kao uputa: „npr. ana.horvat@primjer.hr”.
- Privola: „Slažem se s [Uvjetima korištenja] i [Politikom privatnosti].” –
  pazi na padež u poveznici (instrumental iza „s”).
- Gumb ispod obrasca: „Pošalji upit”, „Zatraži ponudu”, „Rezerviraj termin”.

## Množina uz brojeve (i18n)

Hrvatski ima tri oblika (CLDR kategorije `one`, `few`, `other`):

| Kategorija | Brojevi | Primjer |
|---|---|---|
| `one` | završava na 1, ali ne na 11 (1, 21, 31, 101) | 1 proizvod, 21 dan |
| `few` | završava na 2–4, ali ne na 12–14 (2, 3, 22, 34) | 2 proizvoda, 3 dana |
| `other` | sve ostalo (0, 5–20, 25, 100, 111–114) | 5 proizvoda, 12 dana |

Primjer ICU poruke:

```
{count, plural,
  one {# proizvod}
  few {# proizvoda}
  other {# proizvoda}
}
```

```
{count, plural,
  one {Imate # novu poruku}
  few {Imate # nove poruke}
  other {Imate # novih poruka}
}
```

- Ne lijepi „proizvod(a)”; koristi pravu sklonidbu.
- Kod decimalnih brojeva kategorija ovisi o decimalama (1,5 → `other`, 1,1 →
  `one`); kad je važno, provjeri s `Intl.PluralRules`.
- U JS-u: `new Intl.PluralRules('hr').select(n)` vraća `one` / `few` / `other`.
- Datumi i brojevi: `new Intl.NumberFormat('hr-HR')` daje točku za tisućice i
  zarez za decimale; `Intl.DateTimeFormat('hr-HR', { dateStyle: 'long' })` daje
  „21. listopada 2026.”. Valuta: `{ style: 'currency', currency: 'EUR' }` →
  „99,90 €”.
- Točka koju daje `Intl` dopuštena je, ali IHJJ kao osnovno piše bjelinu
  (10 000); ako proza i sučelje moraju izgledati jednako, uskladi ih (vidi
  `interpunkcija-i-tipografija.md` i `croatia:hr-localization`).

## SEO tekstovi (title, meta description, alt)

- **Title:** prirodna fraza sentence caseom, ključna riječ naprijed, naziv
  brenda iza crte: „Najam stanova u Splitu – cijene i uvjeti | Primjer d.o.o.”.
- **Meta opis:** jedna do dvije rečenice, Vi ili ti prema tonu stranice, s
  pozivom na radnju („Zatražite besplatnu ponudu.”).
- **Alt tekst:** opis slike na hrvatskom, bez „slika” na početku: „Ulaz u
  stambenu zgradu s biciklističkim parkiralištem”.
- **URL slugovi:** malim slovima, sa spojnicama, obično bez dijakritika:
  `/blog/kako-odabrati-stan`. Pravila transliteracije (č, ć → c; đ → d ili
  dj; š → s; ž → z) i kod: `croatia:hr-localization`.

## Pravni i regulatorni nazivi

- „Politika privatnosti”, „Uvjeti korištenja”, „Uvjeti prodaje”, „Pravo na
  jednostrani raskid ugovora” (pravo na odustanak), „Obrazac za jednostrani
  raskid”, „Podaci o trgovcu”, „Kolačići”.
- Sadržaj pravnih stranica: `croatia:hr-legal-compliance`; ovaj skill pokriva
  samo jezik.
