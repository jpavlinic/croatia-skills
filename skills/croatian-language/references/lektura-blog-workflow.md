# Radni proces za lekturu Markdown/MDX članaka

Checklist za lekturu članka, bloga, dokumentacije ili opisa u Markdownu ili
MDX-u. Cilj: prirodan hrvatski uz logičku i činjeničnu točnost, a tehnička
struktura ostaje netaknuta.

## Što ostaviti netaknuto

Mijenjaj **samo tekst koji čovjek čita**. Ne diraj:

- **YAML frontmatter strukturu** (`title`, `description`, `date`, `tags`,
  `excerpt`, `cover`, `keywords`, `faq`…). Tekstualne vrijednosti (naslov,
  opis, sažetak, odgovori u FAQ-u) lektoriraš, ali ključeve, datume, putanje
  i redoslijed ne mijenjaš.
- **Ciljane ključne riječi** (`keywords` i slično): to su tražilične fraze,
  ne stilske pogreške. Ne „ispravljaj” ih bez dogovora.
- **HTML i MDX komponente:** oznake, `class`, `href`, `id`, propsi,
  ikone. Mijenjaj samo vidljivi tekst unutar njih.
- **Poveznice, putanje, slike, sidra** (`#naslov`), blokove koda i
  vrijednosti unutar koda.

## Što ispraviti

1. **Jezik, logiku i činjenice** – sva tri sloja (SKILL.md i ostale
   reference).
2. **Usiljene lokalne kvalifikatore u prozi.** „Hrvatski”, „domaći”,
   „lokalni” ubačeni ondje gdje ništa ne dodaju („s hrvatskim primjerima” uz
   posve opće primjere) makni. Zadrži stvaran lokalni sadržaj: hrvatski
   propisi, institucije, klima, cijene, običaji, mjesta.
   - **Test:** ako rečenica jednako dobro stoji bez kvalifikatora, makni ga;
     ako gubi konkretno značenje, zadrži ga.
3. **„TL;DR” → „Ukratko”.**
4. **Napomenu na kraju** dodaj ako je nema, a tema je traži (zdravlje, pravo,
   porezi, financije): kratko i informativno, npr. *„Tekst je informativan i
   ne zamjenjuje savjet liječnika.”* ili *„Tekst je informativan i ne
   zamjenjuje pravni savjet.”* Prilagodi obraćanju (ti / Vi).
5. **Vi / ti:** ako se članak obraća čitatelju s „Vi”, piši Vi, Vas, Vaš
   velikim slovom kroz cijeli tekst; ako se obraća s „ti”, ostani na „ti”.
6. **Naslovi H1–H3** samo s prvim velikim slovom.
7. **Dosljednost kroz cijeli tekst:** separator tisućica, raspon (crtica s
   razmacima ili bez), navodnici, oblik sata, nazivi.

## Što istaknuti korisniku (ne ispravljaj tiho)

- **Izmišljena „stvarna” svjedočanstva:** imenovane osobe s konkretnim
  rezultatima čitaju se kao stvarni klijenti. Omekšaj naslov koji implicira
  stvarnost („Stvaran primjer” → „Primjer”) i predloži da se primjeri označe
  kao ilustrativni ako nisu dokumentirani.
- **Krive ili neprovjerene citacije studija** (vidi
  `cinjenice-brojke-i-provjera.md`).
- **Brojke koje se ne zbrajaju** ili proturječe drugim dijelovima teksta ili
  drugim člancima istoga projekta.
- **Zastarjele podatke** (stope, iznosi, nazivi ustanova) bez godine.

## Osjetljive teme

- **Zdravlje:** napomena neka upućuje na liječnika ili drugoga stručnjaka. Ne
  navodi linije podrške koje nisi provjerio da još rade.
- **Pravo, porezi, financije:** odvoji informaciju od savjeta i navedi godinu
  na koju se podatci odnose.
- **Ne pojačavaj** samokritiku, strah ni krivnju čitatelja.

## Format isporuke

1. Vrati ispravljenu datoteku (ista struktura, ispravljen tekst).
2. Daj **sažet popis izmjena** grupiran po kategorijama:
   - **Činjenice i logika** – najprije i najistaknutije;
   - **Brendovi i nazivi** – što je promijenjeno i zašto;
   - **Jezik i tipografija** – zbirno (zamjene, crtice, separatori);
   - **Namjerno zadržano** – što izgleda kao pogreška, a nije (npr. ključne
     riječi, lokalni kontekst);
   - **Za provjeru** – neprovjerene tvrdnje, ilustrativni primjeri.
3. Budi konkretan i kratak; ne objašnjavaj očito.

## Tipičan redoslijed

1. Pročitaj izvornik; uoči temu, ton i čitatelja.
2. Provjeri brojke i činjenice.
3. Provjeri logiku i unutarnju dosljednost.
4. Lektoriraj jezik (srbizmi → anglicizmi → gramatika → pravopis →
   interpunkcija → tipografija).
5. Sačuvaj strukturu, dodaj napomenu ako treba, vrati datoteku i popis
   izmjena.
