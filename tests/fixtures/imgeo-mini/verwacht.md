# IMGeo-mini: gewenste uitkomst

`imgeo-mini.ttl` is een klein regressiekader: 1 begrippenkader, 20 begrippen, 2 collecties,
111 triples. Termen en definities zijn ontleend aan het IMGeo-begrippenkader; de fouten zijn
opzettelijk aangebracht. Elke fout staat in het bestand bij een commentaarregel.

Het kader is klein genoeg om in een paar minuten te draaien. Mist een assistent hier een
bevinding, dan ligt dat aan de skill of het model, niet aan de omvang van het kader (zie
[het verslag van 2026-08-28](../../verslagen/2026-08-28-portabiliteit-en-lichte-modellen.md)).

## SHACL-validatie

Met het profiel 1.0.0 uit het register plus de extensie van de skill, `advanced=True`,
`inference=rdfs`. Samengevoegd tot één shapes-graaf, of als twee aparte runs waarvan de
bevindingen worden opgeteld (zoals de skill voorschrijft): beide geven dezelfde aantallen.

| sh:Violation | sh:Warning | sh:Info |
| --- | --- | --- |
| 3 | 17 | 20 |

De volledige lijst per focus node staat in [`verwacht-shacl.json`](verwacht-shacl.json) en is
te reproduceren met:

```bash
python3 tests/ijkpunt.py tests/fixtures/imgeo-mini/imgeo-mini.ttl
```

Komt er 0 `sh:Violation` uit, dan is de extensie vrijwel zeker niet meegenomen (bijvoorbeeld
door `pyshacl -e`). De drie violations komen alle drie uit de extensie.

## Aangebrachte fouten en wat de skill moet melden

| Nr. | Begrip of onderdeel | Aangebrachte fout | Ernst in het rapport | Gevonden door |
| --- | --- | --- | --- | --- |
| 1 | `Mast` | Topbegrip met een bovenliggend begrip (`isothes:broaderGeneric` naar `Inrichtingselement`) | Fout | Extensie `TopConceptWithBroaderShape` |
| 2 | `Bak`, `Begroeidterreindeel` | Topbegrip met een bovenliggend begrip dat niet in het kader bestaat (`Cityfurniture`, `Plantcover`) | Fout | Extensie `TopConceptWithBroaderShape`; profiel `Concept-broaderGeneric` meldt daarnaast dat het doel geen `skos:Concept` is |
| 3 | `Plustype_wegdeel`, `Plustype_terrein` | Dubbele voorkeursterm `plus-type` | Waarschuwing | Profiel `Concept-UniquePrefLabelWithinSchemeShape` |
| 4 | `NietBgtWegdeel`, `NietBgtTerrein`, `NietBgtWater` | Identieke, niet-onderscheidende definitie | Waarschuwing | Extensie `DuplicateDefinitionWithinSchemeShape` (6 resultaten: één per paar) |
| 5 | `Buurt` | Term met hoofdletter | Waarschuwing | Inhoudelijke review (termconventies) |
| 6 | `Greppel` | Leesteken in de term: `greppel, droge sloot` | Waarschuwing | Inhoudelijke review |
| 7 | `Put` | Leesteken in de term: `inspectie- / rioolput` | Waarschuwing | Inhoudelijke review |
| 8 | `Verhardenwegdeel` | Werkwoord als term: `verharden wegdeel` | Waarschuwing | Inhoudelijke review (oordeel) |
| 9 | `Duiker` | Tekstcoderingsfout in de definitie (`Ã©Ã©n`) | Waarschuwing | Inhoudelijke review |
| 10 | `Overigbouwwerk` | Circulaire definitie: "Een bouwwerk dat een overig bouwwerk is." | Waarschuwing | Inhoudelijke review |
| 11 | `Paal` | Verweesd begrip: geen topbegrip, geen enkele relatie | Waarschuwing | Extensie `OrphanConceptShape` en profiel |
| 12 | Collectie `Functiewegdeel` | Geen `skos:prefLabel`, alleen `rdfs:label` | Waarschuwing | Profiel `Collection-label` |
| 13 | Begrippenkader | Geen `dct:title`, alleen `rdfs:label "Model"`; die titel is ook nietszeggend | Waarschuwing | Profiel `ConceptScheme-label`; inhoudelijke review voor de titel |
| 14 | `Inrichtingselement` | Engelse CamelCase-term met taal-tag `@nl`: `CityFurniture` | Waarschuwing | Inhoudelijke review |

Daarnaast heeft geen enkel begrip een `dct:source`: 20 maal Informatief (extensie
`MissingSourceShape`).

## Controlegroep

`Kolk`, `Watervlakte`, `Goot` en `Molgoot` zijn correct. Behalve de ontbrekende bron hoort de
skill daar niets over te melden.

**Bekend vals positief.** Het profiel 1.0.0 meldt `Molgoot` als begrip zonder relaties
(node shape `Concept`), omdat het `isothes:broaderGeneric` niet als hiërarchische relatie
herkent. `Molgoot` hangt wel degelijk onder `Goot`. De extensie meldt `Molgoot` terecht níet.
Een goed rapport noemt `Molgoot` niet als verweesd, of benoemt de melding expliciet als
beperking van het profiel.

## Oordeel

- **Totaaloordeel:** Voldoet gedeeltelijk aan NL-SBB. "Voldoet niet" is verdedigbaar; "Voldoet
  (grotendeels)" niet, want er zijn harde fouten.
- **Publicatieadvies:** niet geschikt voor publicatie zonder herstel van fout 1 en 2.

## Scoren

Een rapport scoort per aangebrachte fout: gevonden met de juiste ernst, gevonden met een andere
ernst, of gemist. Daarnaast tellen:

- verzonnen bevindingen (een fout die niet in het kader zit);
- telfouten (een aantal dat afwijkt van de werkelijkheid, ook als het in de eigen uitvoer van de
  assistent goed staat);
- of het rapport vermeldt welke controles uitputtend en welke op steekproef zijn gedaan.
