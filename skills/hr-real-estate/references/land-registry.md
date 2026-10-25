# Land registry (zemljišna knjiga) and cadastre (katastar)

Status: researched 2026-10-25. Not legal advice.

Law: Zakon o zemljišnim knjigama (ZZK), NN 63/19, 128/22, 155/23, 127/24.
Registers are kept by the land-registry departments of municipal courts (općinski sudovi);
the cadastre by Državna geodetska uprava (DGU, dgu.gov.hr). Both are joined in the
**Zajednički informacijski sustav zemljišnih knjiga i katastra (ZIS)**: oss.uredjenazemlja.hr.

## Two registers, two purposes

| | Zemljišna knjiga (ZK) | Katastar |
|---|---|---|
| Kept by | municipal court, ZK department | DGU (područni uredi / ispostave) |
| Shows | **legal** status: ownership, mortgages, easements, rights | **physical** status: plots (čestice), area, buildings, use |
| Legal effect | ownership is acquired by registration; trust principle (ZZK čl. 8) | evidential; feeds the ZK |
| Extract | ZK izvadak | posjedovni list, kopija katastarskog plana |

**Mismatches are common** (old surveys, unregistered buildings, different areas or holders).
A mismatch is not fatal but must be understood before buying: whose name is in the cadastre,
is the house drawn on the plot, does the area differ, is there a newer survey (nova izmjera)
in progress. Fixing it may need a geodetic report (geodetski elaborat) and a court procedure.

## Reading a ZK izvadak

A ZK uložak (folio) has three parts (ZZK čl. 20(1)):

| List | Name | Contains | What to check |
|---|---|---|---|
| **A** | posjedovnica | the land: čestica numbers, culture/use, area, buildings; A2: rights belonging to the land (e.g. easement over a neighbour) | correct plot and building; matches cadastre |
| **B** | vlastovnica | owners and shares (suvlasnički dijelovi), with restrictions on them | seller(s) registered, shares add up to 1/1, no restrictions (e.g. minor owner, ban on sale) |
| **C** | teretovnica | encumbrances: mortgages (založno pravo / hipoteka), easements (služnosti), usufruct (plodouživanje), pre-emption, lease, enforcement (ovrha), lawsuit notes | everything here must be either acceptable to you or deleted at closing |

- **KPU** (knjiga položenih ugovora) sub-folios exist for flats in buildings where etažiranje
  was not done in the main book (ZZK čl. 20(2)). A flat registered only in KPU gives weaker
  certainty; ask the notary how it will be handled.
- **Etažiranje**: a flat must be a separate unit (posebni dio, etaža) linked to a co-ownership
  share of the whole building. If not, you are buying an ideal share of the building and the
  right to use a flat is only contractual.

## Kinds of entries (ZZK čl. 34)

| Entry | Meaning |
|---|---|
| **Uknjižba** | final (unconditional) acquisition, transfer, restriction or deletion of a right |
| **Predbilježba** | conditional entry, valid if later justified (opravdanje); used when the document lacks something (e.g. no clausula yet) |
| **Zabilježba** | notes a fact relevant to the property: lawsuit, enforcement, minor's status, pre-emption, start of a legal procedure, priority reservation |

**Plomba** (ZZK čl. 108): entered as soon as a filing arrives, with date, time and case number;
removed when the entry is decided. A plomba on the seller's folio means something is pending:
ask what it is before paying.

**Priority** (prvenstveni red) is fixed by the moment the filing reaches the court
(ZZK čl. 50(1)). This is why buyers and banks e-file immediately after signing.

**Trust principle** (ZZK čl. 8): the register is presumed true and complete; a good-faith buyer
who relied on it is protected, unless they knew or had reason to doubt (čl. 8(3)). Not checking
the off-register situation is not bad faith in itself, but if you see a different occupant,
an unregistered spouse or building, ask questions: a court may find you "had reason to doubt".

## Documents for registration (uknjižba)

- Private document (contract) with **notarised signatures** (ZZK čl. 57(1)).
- The **explicit consent** of the registered owner "da pristaje na uknjižbu" (clausula
  intabulandi / tabularna isprava), in the contract or a separate document (ZZK čl. 59(1)(b)).
- Signatures by an attorney: notarised, plus a special power of attorney or a general one not
  older than one year (ZZK čl. 58).
- Proof of citizenship of the buyer (domovnica, ID or passport); for third-country buyers the
  ministry's consent (see `foreigners.md`).
- Proof of court-fee payment or exemption (gov.hr, *Upis prava vlasništva*).

## Fees 2026 (court fees, Uredba o Tarifi sudskih pristojbi NN 37/23)

| Item | Amount |
|---|---|
| Application (prijedlog) for registration | 6.64 € (gov.hr shows 6.50 €; sudovi.hr shows 6.64 €; **VERIFY** current tariff) |
| Decision on uknjižba/predbilježba of ownership or other real right | 26.54 € per right |
| E-filing (via notary, lawyer, e-Građani) | filing fee reduced by 50 % |
| Filed more than 60 days after conditions were met | 5× the fee |
| ZK izvadak online (oss.uredjenazemlja.hr / e-Građani) | free to view; e-izvadak with legal force free via e-Građani (**VERIFY** for non-residents without NIAS login) |
| Certified extract at a court / notary | small fee plus notary tariff |

## Practical online checks

1. oss.uredjenazemlja.hr → *Pregled zemljišnoknjižnih izvadaka*: search by katastarska općina
   and čestica, or ZK uložak / KPU poduložak.
2. Same portal → cadastre data (posjedovni list, plan) and the status of pending filings by case
   number.
3. Compare: owner in list B vs. seller's ID; area in list A vs. cadastre and the ad; buildings
   drawn vs. reality (satellite view, site visit).
4. Repeat the check on the day of signing and right before paying.

## Common problems and fixes

| Problem | Typical fix |
|---|---|
| Seller not registered (inherited, bought decades ago) | first register the inheritance decision / old contract (chain of titles), then sell |
| Building not drawn in cadastre / ZK | geodetski elaborat + uporabna dozvola or rješenje o izvedenom stanju, then registration |
| Old mortgage of a repaid loan in list C | bank's brisovno očitovanje (deletion consent), filed at closing |
| Several co-owners, one refuses | sale of a share only, or court partition (razvrgnuće) – slow |
| KPU only / no etažiranje | etažiranje by all co-owners (elaborat + agreement), or buy with legal advice |
| Area differs between ZK and cadastre | survey (nova izmjera) or individual correction; price on actual area |
