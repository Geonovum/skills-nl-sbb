# NL-SBB Review — Achtergrondinfo

Deze pagina bevat de detailregels die niet in de hoofdskill passen: controlelijsten per SKOS-eigenschap, de ISO 25964-relaties, definitietypen, en de meegeleverde SHACL-extensie. De hoofdskill ([`SKILL.md`](SKILL.md)) verwijst hiernaar.

## Ondersteunde talen

De skill ondersteunt Nederlands en Engels. Controleer bij meertalige kaders of taal-tags correct zijn (`@nl`, `@en`), of Nederlandse en Engelse termen en definities consistent zijn, en of vertalingen inhoudelijk overeenkomen. Het ontbreken van Engels is niet automatisch een fout; het ontbreken van Nederlands is in NL-SBB-context meestal een waarschuwing of fout, afhankelijk van de publicatiecontext.

## Controlelijst per SKOS-eigenschap

### Begrippen (`skos:Concept`)

| Eigenschap | Verwachting | Ernst bij ontbreken |
|---|---|---|
| `rdf:type skos:Concept` | Object is als begrip getypeerd | Fout |
| `skos:prefLabel` | Begrip heeft voorkeursterm | Fout of waarschuwing |
| `skos:definition` | Begrip heeft definitie | Fout |
| `skos:inScheme` | Begrip is gekoppeld aan begrippenkader | Fout |

Rapporteer per bevinding de URI, de ontbrekende eigenschap, de ernst, de NL-SBB-uitleg en een advies.

### Begrippenkader (`skos:ConceptScheme`)

Controleer of het kader is gemodelleerd als `skos:ConceptScheme`, een URI/identificatie heeft, een titel of label heeft, topbegrippen heeft via `skos:hasTopConcept` of `skos:topConceptOf`, en vanuit begrippen wordt gebruikt via `skos:inScheme`.

### Collecties (`skos:Collection`)

Controleer of collecties zijn gemodelleerd als `skos:Collection`, een label hebben, leden bevatten via `skos:member`, en niet worden verward met begrippen of begrippenkaders. Signaleer onterechte combinatie van rollen als fout.

## Labels en termen

- `skos:prefLabel` — voorkeursterm; maximaal één per taal.
- `skos:altLabel` — alternatieve termen (synoniemen, afkortingen).
- `skos:hiddenLabel` — zoektermen (spelfouten, zoekvarianten).

Let op dubbele voorkeurstermen binnen hetzelfde kader (meestal waarschuwing, tenzij ontbrekende context publicatie blokkeert), en modelleer specifiekere begrippen niet als alternatieve term.

### Termconventies (Best Practice 1)

De standaard geeft in §5.1.1 conventies voor het beschrijven van termen (voorkeurstermen én alternatieve termen). Toets elke voorkeursterm hieraan; een afwijking is een **waarschuwing** (niet blokkerend, maar relevant voor kwaliteit en consistentie), tenzij de publicatiecontext de conventie verplicht stelt.

| Conventie | Toets | Voorbeeld fout → goed |
|---|---|---|
| Zelfstandig naamwoord (evt. + bijvoeglijk naamwoord) | Term is een znw., geen werkwoord/bijwoord | "bakken" → "het bakken" |
| Geen werkwoorden | Term is geen (infinitief-)werkwoord | "koken" → "het koken" |
| Geen bijwoorden, lidwoorden, voorzetsels | Term bevat geen "de/het/een", "in", "snel" | "de fiets" → "fiets" |
| Geen dubbele adjectieven | Hoogstens één bijvoeglijk naamwoord | "grote zware last" → "zware last" |
| Geen afkortingen | Term voluit (afkortingen horen in `skos:altLabel`) | "EV-object" → "externe veiligheidsobject" |
| Kleine letters, behalve eigennamen | Term in kleine letters "zoals in een zin" | "Fiets" → "fiets"; "Amsterdam" blijft |
| Latijnse karakters (UTF-8) | Geen niet-Latijns schrift | — |
| Geen leestekens (streepjes, punten, komma's) | Term zonder interpunctie | "auto-band" → "autoband" |
| Enkelvoud (NL/DE/FR, niet EN) | Term is enkelvoud | "kookhandelingen" → "kookhandeling" |
| Standaardspelling (Groene Boekje) | Correct gespeld | — |

**Belangrijke beperkingen bij deze check:**
- Woordsoort (werkwoord vs. zelfstandig naamwoord) en getal (enkelvoud/meervoud) zijn niet altijd betrouwbaar automatisch te bepalen; sommige vormen zijn dubbelzinnig (bijv. een gesubstantiveerd werkwoord). Meld twijfel expliciet ("lijkt een werkwoordsvorm") en presenteer het als aandachtspunt, niet als harde overtreding.
- Deze conventies gelden voor termen (`prefLabel`/`altLabel`), niet voor `rdfs:label` of definitieteksten.
- Een consequent doorgevoerde afwijking (bijv. álle termen in meervoud) valt niet op als *inconsistentie*; toets daarom elke term ook absoluut tegen de conventie, niet alleen onderling.
- Deze regels zijn niet in SHACL uit te drukken (geen woordsoort-/getalanalyse in het profiel of de extensie) en horen daarom in de inhoudelijke review.

## Definities en notities

Controleer per `skos:definition`: is de definitie aanwezig, beschrijft ze het begrip (niet alleen de term), is ze onderscheidend, niet circulair, niet te vaag, niet slechts een voorbeeld, en past ze bij bovenliggende/onderliggende begrippen?

Definitietypen (beoordeel waar mogelijk): (1) typering / genus-differentia, (2) samenstelling / geheel-deel, (3) onderdeel, (4) relatie, (5) kenmerk.

Onderscheid tussen: `skos:definition` (precieze betekenis), `rdfs:comment` (eenvoudige uitleg), `skos:scopeNote` (gebruik, grens, reikwijdte), `skos:example` (voorbeelden). Signaleer als waarschuwing wanneer uitleg, voorbeelden of toelichtingen de definitie vervangen of tegenspreken.

## Bronnen

Controleer `dct:source`: hebben begrippen waar relevant een bron, is die specifiek genoeg, vindbaar/herleidbaar, en heeft het brondocument een titel, URL of bibliografische verwijzing? Een ontbrekende bron is niet automatisch een fout, tenzij de toepassingscontext dit verplicht stelt.

## Relaties

### Semantische relaties

`skos:broader` (algemener), `skos:narrower` (specifieker), `skos:related` (associatief). Signaleer als **fout** wanneer een semantische relatie naar iets verwijst dat geen begrip is. Signaleer als **waarschuwing** wanneer `related` eigenlijk hiërarchisch lijkt, `broader`/`narrower` eigenlijk associatief lijkt, relaties onvoldoende betekenisvol zijn, of een belangrijk begrip geïsoleerd is.

### ISO 25964-relaties

| Relatie | Betekenis |
|---|---|
| `isothes:broaderGeneric` | is specialisatie van |
| `isothes:narrowerGeneric` | is generalisatie van |
| `isothes:broaderPartitive` | is onderdeel van |
| `isothes:narrowerPartitive` | omvat |
| `isothes:broaderInstantial` | is exemplaar van |
| `isothes:narrowerInstantial` | is categorie van |

Waarschuw bij twijfelachtig gebruik, bijvoorbeeld een partitieve relatie voor delen die tot meerdere gehelen kunnen behoren.

### Harmonisatierelaties

`skos:exactMatch` (betekenis gelijk), `skos:closeMatch` (ongeveer gelijk), `skos:broadMatch` (extern algemener), `skos:narrowMatch` (extern specifieker), `skos:relatedMatch` (extern verwant). Deze zijn bedoeld voor begrippen uit **verschillende** kaders. Signaleer als **fout** wanneer ze binnen hetzelfde begrippenkader worden gebruikt.

## Topbegrippen, verweesde begrippen en codes

- **Topbegrippen** — aangeduid via `skos:hasTopConcept` of `skos:topConceptOf`, gekoppeld aan het juiste kader, en **zonder** bovenliggend begrip. Een topbegrip met een bovenliggend begrip is een **fout**.
- **Verweesde begrippen** — niet-topbegrippen horen minimaal één semantische verbinding te hebben (`broader`, `narrower`, `related` of ISO-thes). Ontbreekt die, dan is dat een **waarschuwing**.
- **Codes** — `skos:notation` moet uniek zijn binnen hetzelfde kader; dubbele codes zijn een **fout**, inconsistente codes een **waarschuwing**.

## Inhoudelijke kwaliteitsreview

- **Begrijpelijkheid** — begrijpelijke voorkeurstermen, compacte en onderscheidende definities, verhelderende toelichtingen, passende voorbeelden.
- **Consistentie** — vergelijkbare definitiepatronen, spelling, hoofdletters, enkelvoud/meervoud, taal-tags, consequent relatiegebruik.
- **Begripsafbakening** — wat binnen/buiten het begrip valt, logische boven-/onderliggende begrippen, overlap met verwante begrippen, definities die relaties ondersteunen.
- **Publicatiekwaliteit** — blokkeren fouten de publicatie, moeten waarschuwingen vóór publicatie worden opgelost, kunnen aanbevelingen later, en is het oordeel begrijpelijk voor interne én externe gebruikers?

## SHACL-extensie voor niet-getoetste regels

Het normatieve profiel `skos-ap-nl.ttl` toetst niet alle NL-SBB-regels. De meegeleverde extensie [`skos-ap-nl-extensie.ttl`](skos-ap-nl-extensie.ttl) vult dit aan met zes shapes (gebaseerd op SPARQL-constraints):

| Shape | Regel | Ernst |
|---|---|---|
| `TopConceptWithBroaderShape` | Topbegrip met bovenliggend begrip (incl. `isothes:broader*`) | Violation |
| `MappingWithinSameSchemeShape` | Harmonisatierelatie binnen hetzelfde kader | Violation |
| `DuplicateNotationWithinSchemeShape` | Dubbele `skos:notation` binnen één kader | Violation |
| `OrphanConceptShape` | Verweesd begrip (niet-top, geen semantische relatie) | Warning |
| `DuplicateDefinitionWithinSchemeShape` | Identieke definitie bij meerdere begrippen | Warning |
| `MissingSourceShape` | Ontbrekende `dct:source` | Info |

Gebruik naast het normatieve profiel:

```bash
pyshacl -s skos-ap-nl.ttl --advanced --inference rdfs -f human data.ttl
pyshacl -s skos-ap-nl-extensie.ttl --advanced --inference rdfs -f human data.ttl
```

De extensie is een hulpmiddel van deze skill, geen onderdeel van de normatieve standaard. Twee regels blijven buiten SHACL en horen in de inhoudelijke review: het geheel-patroon "alle begrippen zijn topbegrip" en vage/circulaire definities.

## Gerelateerde bronnen

| Bron | Relatie |
|------|---------|
| [`SKILL.md`](SKILL.md) | Hoofdskill: proces, ernstniveaus, rapportstructuur |
| [`conflicts.md`](conflicts.md) | Bronbeperkingen en gemaakte keuzes |
| [NL-SBB standaard](https://docs.geostandaarden.nl/nl-sbb/nl-sbb/) | Normatieve tekst |
