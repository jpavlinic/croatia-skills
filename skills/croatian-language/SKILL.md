---
name: croatian-language
description: >-
  Croatian (hrvatski) writing, proofreading and style guide based on the IHJJ
  Hrvatski pravopis. Use it ALWAYS whenever Croatian appears: the user writes
  in Croatian; any text you write, translate, review or edit is Croatian (even
  one sentence, a UI string, an e-mail, a commit message or a code comment);
  the project is Croatian (.hr domain, hr locale, hr.json); or Croatian is
  mentioned. Triggers: "Croatian text", "proofread", "translate to Croatian",
  "native Croatian", lektura, lektoriraj, korektura, pravopis, gramatika,
  ispravi tekst, prijevod na hrvatski, zvuči li prirodno, anglicizmi, kalkovi,
  srbizmi, ijekavica, "da li", ne bi/nebi, neću, č/ć, dž/đ, veliko slovo, Vi
  iz poštovanja, zarez, navodnici, crtica, spojnica, brojke, datumi, kratice,
  e-mail i dopisi, UI tekstovi, množina uz brojeve, strojni prijevod, AI tekst.
  Apply proactively and silently to every Croatian output.
---

# Croatian language: writing and proofreading

Write and correct Croatian so it reads like the work of an educated native
speaker: correct by the standard, natural, free of English calques and of
Serbian forms. The norm is the *Hrvatski pravopis* of the Institut za hrvatski
jezik (IHJJ, [pravopis.hr](https://pravopis.hr)). Where the standard allows
variants (e.g. thousands separator, spacing around a range dash), follow the
project's own house style if it has a consistent one (CLAUDE.md, a style
guide, existing content); otherwise use the IHJJ default given here.

Status: researched 2026-10-25.

## How to use

1. Croatian anywhere in input or output → apply this skill without being asked.
2. Work in three layers (below). For short texts you write yourself (an
   e-mail, a UI string) return only the clean text; for proofreading return
   the corrected text plus a short list of changes.
3. Load a reference only when needed:

| Need | Reference | Grep hints |
|---|---|---|
| Commas, dashes, quotes, numbers, dates, units, money, capitals | `references/interpunkcija-i-tipografija.md` | `zarez`, `crtica`, `tisućica`, `datum`, `navodnici` |
| Frequent spelling errors (ne bi, neću, uvijek, č/ć, dž/đ, ije/je, gdje/kamo) | `references/ceste-pogreske.md` | `nebi`, `č / ć`, `pokriveni`, `kamo` |
| Foreign names and words, abbreviations, acronyms, hyphenated compounds | `references/strane-rijeci-kratice-i-spojnica.md` | `sklonidba`, `kratice`, `pokrate`, `e-pošta` |
| Grammar, word order, clitics, conditional, number agreement, style | `references/gramatika-stil-prirodnost.md` | `enklitike`, `bismo`, `koji`, `isti` |
| Anglicisms and better Croatian words | `references/vokabular-i-anglicizmi.md` | `kalk`, `ukoliko`, `kreirati` |
| Serbian forms to avoid | `references/hrvatski-vs-srpski.md` | `ekavica`, `da + prezent`, `tisuća` |
| Machine-translation / AI-text smells | `references/strojni-prijevod-i-ai-tekst.md` | `od strane`, `vršiti`, `Title Case` |
| E-mails, letters, salutations | `references/e-mail-i-dopisi.md` | `Poštovani`, `pozdrav`, `vokativ` |
| UI strings, forms, error messages, i18n plurals, meta texts | `references/web-i-ui-tekstovi.md` | `Spremi`, `plural`, `alt` |
| Fact, number and logic checks | `references/cinjenice-brojke-i-provjera.md` | `zbroj`, `PDV`, `studij` |
| Proofreading a Markdown/MDX article | `references/lektura-blog-workflow.md` | `frontmatter`, `flag` |

Related skills in this plugin: `croatia:hr-localization` (dates, numbers,
plurals, collation, slugs, name declension and vocative, *u/na* with place
names in code and data), `croatia:hr-market-brands` (which brands, shops and
banks really exist in Croatia), `croatia:hr-legal-compliance` (content of
legal pages; this skill covers only their language).

## Three layers of every review

1. **Jezik**: pravopis, gramatika, vokabular, prirodan red riječi, anglicizmi,
   srbizmi, interpunkcija, tipografija.
2. **Logika**: zbrajaju li se brojke, odgovara li „tri razloga” nabrajanju,
   nema li proturječja ni dvostrukoga brojenja.
3. **Činjenice**: podatci, studije, brendovi i njihova dostupnost u Hrvatskoj,
   propisi i iznosi. Ne mijenjaj činjenicu „iz glave”: provjeri je ili je
   označi.

Pravopisno besprijekoran tekst koji je logički ili činjenično pogrešan i dalje
je loš tekst.

## Vrhovno načelo: neka zvuči izvorno hrvatski

- **Prepiši nezgrapnu rečenicu** umjesto da je krpaš; kalk često traži novu
  formulaciju.
- **Čuvaj smisao, brojke, strukturu i ton.** Sloboda je u formulaciji, ne u
  sadržaju. Zadani „ti” i opušten ton ostaju.
- **Ne uvodi nove pogreške.** Bolje ostaviti dvojbeno i označiti nego jednu
  pogrešku zamijeniti drugom.

## Vi iz poštovanja (čvrsto pravilo)

IHJJ: osobna i posvojna zamjenica 2. lica množine pišu se **velikim početnim
slovom kad se u pisanome tekstu obraćamo pojedincu i želimo mu izraziti
poštovanje**, a **malim kad se obraćamo skupini ili ne konkretnomu
pojedincu** ([pravopis.hr, 4.1.3.](https://pravopis.hr/pravilo/rijeci-iz-postovanja-i-pocasti/21/)).

- **Jedna osoba → Vi, Vas, Vam, Vama, Vaš, Vaša, Vaše, Vašeg(a), Vašem(u),
  Vašoj, Vašu, Vašim, Vaših, Vašima** u svim oblicima: „Hvala Vam na
  prijavi.”, „Vaša je adresa potvrđena.”, „Ako niste Vi zatražili promjenu…”
- **Skupina → vi, vas, vaš…**: „Dragi gosti, želimo vam ugodan boravak.”,
  „Poštovani roditelji, pozivamo vas na sastanak.”, „Dragi svi, hvala vam.”
- **Opća uputa koja se ne obraća konkretnomu čitatelju** (natpis, ambalaža,
  upute za uporabu, obavijest javnosti) → malo slovo, kao u primjeru IHJJ-a:
  „Poštovani, molimo vas da prije upotrebe pročitate upute!”
- **Web-stranica, aplikacija, obrazac, transakcijski e-mail** obraćaju se
  pojedinačnomu korisniku koji ih čita kao poruku sebi → **veliko V** („Vaša
  je narudžba poslana.”, „Javit ćemo Vam se.”). To je ustaljena praksa u
  korisničkim tekstovima. Kad nisi siguran obraća li se tekst jednoj osobi,
  piši veliko V.
- Veliko je samo zamjenica; glagoli ostaju mali („Prijavite se”).
- **Slaganje je u množini:** „Vi ste bili u pravu”, „Jeste li zadovoljni?”;
  nikad „Vi ste bila”.
- **Ne pretrpavaj tekst s „Vaš”.** Kad je osoba subjekt, ide povratno
  **svoj**: „Unesite svoju lozinku”, ili bez zamjenice: „Unesite lozinku.”
- Na „ti” piše se malim slovom (veliko „Ti” samo u osobnoj čestitki ili
  posveti). Ne miješaj „Vi” i „ti” u istom tekstu.

Pozdravi, oslovljavanje i potpisi: `references/e-mail-i-dopisi.md`.

## Interpunkcija i tipografija (najčešće)

Sve s izvorima u `references/interpunkcija-i-tipografija.md`.

- **Crtica (–) i spojnica (-) nisu isto.** Spojnica bez razmaka spaja riječi:
  crno-bijeli, e-pošta, sat-dva. Crtica s razmacima je stanka u rečenici:
  „Radi – ali sporo.” Em crta (—) u hrvatskome se ne rabi.
- **Raspon:** IHJJ crticu piše **s razmacima**: „30 – 45 minuta”,
  „2010. – 2012.”, „ponedjeljak – petak” (bez razmaka samo stranice u
  bibliografiji: „str. 145–162”). Raspon bez razmaka („8–12 tjedana”) raširen
  je tipografski običaj i prihvatljiv je kao kućni stil ako je dosljedan.
  Nikad spojnica u rasponu („8-12”) i nikad „od 8 – 12” (piši „od 8 do 12”
  ili „8 – 12”).
- **Navodnici:** „…” ili »…«, polunavodnici ‘…’ za navod u navodu; bez
  razmaka s unutarnje strane. Ravni `"` u kodu, JSON-u i atributima ne diraj.
- **Brojke:** decimalni **zarez** (1,5 kg). Tisućice: IHJJ piše **bjelinu**
  od 10 000 naviše (10 000, 859 343 286), četveroznamenkaste skupa (5331);
  **točka** (10.000) dopuštena je u financijama i raširena je u praksi. Odaberi
  jedno i drži se toga. Godine se nikad ne razdvajaju (2026.).
- **Razmak između broja i znaka:** 30 %, 5 °C, 5 kg, 99,90 €. Bez razmaka:
  45°, +5, 50 m/s, 1/3.
- **Datum:** u prozi „25. listopada 2026.” (mjesec u genitivu); brojčano s
  razmacima „25. 10. 2026.” Redna točka ne udvostručuje se na kraju rečenice.
- **Sat:** „u 18 sati” / „u 18 h”, „18:30” ili „18.30”; nikad „18h”.
- **Zarez:** zavisna rečenica ispred glavne dobiva zarez („Ako dođete, javite
  se.”), iza glavne ne dobiva („Javite se ako dođete.”). Bez zareza iza uvodne
  priložne oznake („Nakon prijave dobit ćete…”) i ispred „i, ili, pa, te, ni”
  u nizanju. Zarez ispred suprotnih „a, ali, nego, no, već”, ali ne ispred
  poredbenoga „nego” („bolje nego jučer”). Bez zareza ispred „itd.” i „i sl.”
- **Veliko slovo:** naslovi, gumbi i izbornici samo s prvim velikim slovom
  („Kako odabrati stan”, ne „Kako Odabrati Stan”). Mjeseci, dani, pridjevi od
  naziva naroda malim slovom (siječanj, ponedjeljak, hrvatski).

## Najčešće pravopisne pogreške (brzi popis)

Detaljno u `references/ceste-pogreske.md`.

| Pogrešno | Ispravno |
|---|---|
| nebi, nebih, nebismo | ne bi, ne bih, ne bismo |
| nemogu, neznam, nežele | ne mogu, ne znam, ne žele |
| ne ću | neću (IHJJ; spojeno i nisam, nemam, nemoj) |
| mi bi htjeli, vi bi mogli | mi bismo htjeli, vi biste mogli |
| uvjek, primjetiti, zamjeniti (glagol) | uvijek, primijetiti, zamijeniti |
| slijedeći tjedan | sljedeći tjedan (slijedeći = koji slijedi koga) |
| preći, pređem | prijeći, prijeđem |
| gdje ideš? | kamo ideš? (gdje = mjesto, kamo = cilj, kuda = smjer) |
| 10-tak, 50-tih | 10-ak, 50-ih |
| menađer, buđet | menadžer, budžet (dž u posuđenicama) |
| svjedođba, narudđba | svjedodžba, narudžba |
| da li ste dobili | jeste li dobili |
| hvala za pomoć | hvala na pomoći |
| stol kojeg sam kupio | stol koji sam kupio (neživo: A = N) |

## Najčešće leksičke zamjene

Potpuna tablica u `references/vokabular-i-anglicizmi.md`, a znakovi strojnoga
i AI teksta u `references/strojni-prijevod-i-ai-tekst.md`.

| Kalk / slabije | Bolje |
|---|---|
| od strane (u pasivu) | aktivna rečenica: „Administrator je odobrio…” |
| isti (umjesto zamjenice) | on, ona, to; ili izostavi |
| vršiti/izvršiti provjeru | provjeriti |
| na dnevnoj bazi | svakodnevno |
| ukoliko (= ako) | ako |
| s obzirom da, obzirom da | s obzirom na to da |
| vezano za | u vezi s |
| biti u mogućnosti | moći |
| kroz dan (vremenski) | tijekom dana |
| zbog (svrha) | radi („radi uštede”); zbog je za uzrok |
| u zadnje vrijeme | u posljednje vrijeme |
| drugačiji | drukčiji (preporučeno) |
| kreirati, aplicirati | izraditi, prijaviti se |
| TL;DR | Ukratko |

## Nikad ne miješati sa srpskim

Detaljno u `references/hrvatski-vs-srpski.md`.

1. **Ijekavica:** mlijeko, vrijeme, dijete, htjeti (ne mleko, vreme).
2. **Infinitiv, ne „da + prezent”:** „moram reći”, „želim probati”.
3. **„Je li”, ne „da li”:** „Je li stiglo?”, „Jeste li sigurni?”
4. **Futur:** „radit ću”, „vidjet ćemo” (ne „radiću”, „ću da radim”).
5. **Vokabular:** tisuća, kruh, tjedan, tko/što, točno, uopće, vlak, kat,
   sveučilište, siječanj (ne januar).
6. **Glagoli na -irati:** organizirati, kontrolirati (ne organizovati).

## Gramatika koja se najčešće krivo napiše

Detaljno u `references/gramatika-stil-prirodnost.md`.

- **Kondicional:** ja bih, ti bi, on bi, mi bismo, vi biste, oni bi.
- **Red enklitika:** iza prve naglašene riječi ili skupine: „Sutra ću Vam
  javiti”, ne „Sutra Vam ću javiti”.
- **Brojevi:** 1, 21, 31 → jednina („21 dan”); 2–4, 22–24 → „dana”, „eura”;
  5–20, 25–30 → genitiv množine („pet dana”, „11 tjedana”). Za i18n vidi
  `references/web-i-ui-tekstovi.md`.
- **s / sa:** „sa” ispred s, z, š, ž, ispred skupina poput ps-, ks-, pš- i
  ispred „mnom” (sa sestrom, sa psom, sa mnom); inače „s” (s kavom, s Vama).
- **Posvojni pridjevi na -ov, -ev, -in** sklanjaju se imenički: „na Markovu
  trgu”, „Anina prijatelja” (oblici „Markovome”, „Aninoga” razgovorni su).

## Stil

- Aktiv umjesto pasiva s „od strane”, glagol umjesto imenice („provjerite”,
  ne „izvršite provjeru”).
- Kraće rečenice, bez lanaca „koji… koji… što…”.
- Bez izmišljenih doslovnih citata stvarnih osoba.
- Rodna dosljednost kroz cijeli tekst; uz Vi glagolski pridjev u množini.
- Bez engleskoga Title Casea, bez em crta i bez engleskih navodnika.

## Činjenice i brojke

Detaljno u `references/cinjenice-brojke-i-provjera.md`.

- Svaki zbroj, množenje, postotak i pretvorbu provjeri doslovno.
- Brojčana tvrdnja mora odgovarati nabrajanju.
- Citat studije (autor, godina, časopis) provjeri prije izmjene.
- Brendovi moraju postojati i biti točni za Hrvatsku (npr. Njuškalo, ne OLX
  kao hrvatski oglasnik); za provjeru vidi `croatia:hr-market-brands`.
- Propisi, stope i iznosi mijenjaju se: navedi godinu i provjeri na službenom
  izvoru.

## Osjetljive teme

Kod zdravstvenih, pravnih, poreznih i financijskih tema jasno odvoji
informaciju od savjeta i uputi na stručnjaka.

## Redoslijed rada

1. Pročitaj cijeli tekst: namjera, ton, čitatelj (jedna osoba ili skupina →
   Vi ili vi; ti ili Vi).
2. Provjeri činjenice i brojke.
3. Prođi logiku.
4. Prođi jezik: srbizmi → anglicizmi i kalkovi → gramatika → pravopis →
   zarez i veliko slovo → tipografija.
5. Vrati ispravljen tekst; kod lekture i sažet popis izmjena po kategorijama,
   s istaknutim činjeničnim i logičkim ispravcima i otvorenim pitanjima.

## Keeping current

- The online IHJJ *Hrvatski pravopis* ([pravopis.hr](https://pravopis.hr)) is
  updated occasionally. Re-check the rules
  quoted here (Vi, crtica, bjelina/točka, neću) before relying on them for a
  publication standard.
- Other normative works (e.g. Matica hrvatska's pravopis, the Babić–Ham–Moguš
  school pravopis) differ in some details (ne ću/neću, pogrješka/pogreška).
  When a client or publisher prescribes one of them, follow it consistently.
- Word recommendations: IHJJ [Jezični savjetnik](https://jezicni-savjetnik.hr),
  [Bolje je hrvatski!](https://bolje.hr), Hrvatski jezični portal
  ([hjp.znanje.hr](https://hjp.znanje.hr)).
- Facts that go stale (VAT rates, fees, brand ownership, institution names)
  are never stored here; check them at the official source each time.
