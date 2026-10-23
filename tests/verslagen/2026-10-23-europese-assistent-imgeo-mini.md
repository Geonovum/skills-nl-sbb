# 2026-10-23 — Testrun met Mistral op IMGeo-mini

Tweede testrun met een Europese assistent, nu op het regressiekader. Gescoord tegen
[`verwacht.md`](../fixtures/imgeo-mini/verwacht.md) en het ijkpunt.

| | |
| --- | --- |
| Assistent | Mistral, met de skill uit een workspace-registry via de Mistral-MCP, Python en internettoegang *(omgeving en modelversie nog aan te vullen)* |
| Skillversie | `validatie-nl-sbb` uit de workspace-registry, met `scan.py` en losse moduledocumenten voor SHACL en bronnencontrole. **De extensie `skos-ap-nl-extensie.ttl` zat niet in de skill-assets**; de assistent haalde hem zelf op uit Geonovum/skills-nl-sbb |
| Testkader | `tests/fixtures/imgeo-mini/imgeo-mini.ttl`, geüpload als `.txt` |
| Verloop | Twee prompts: (1) "kan je met de geonovum-nl-sbb skill dit begrippenkader valideren?", waarop de basisreview draaide; (2) "allebei graag", na het aanbod van de SHACL-module en de bronnencontrole |

## Acceptatiecriteria

| Nr. | Criterium | Uitkomst |
| --- | --- | --- |
| 1 | SHACL-telling gelijk aan het ijkpunt (3 / 17 / 20) | ✅ 3 / 17 / 20, extensie samengevoegd (679 → 746 triples) |
| 2 | Fout 1 en 2 als Fout gemeld | ✅ Mast, Bak en Begroeidterreindeel, met de zwevende verwijzingen |
| 3 | Minstens 12 van de 14 fouttypen gevonden | ✅ 14 van 14 |
| 4 | Geen verzonnen bevindingen en geen telfouten | ❌ één verzonnen bevinding en één telfout, zie hieronder |
| 5 | Totaaloordeel "Voldoet gedeeltelijk" of "Voldoet niet", publicatieadvies "nee" | ✅ Voldoet gedeeltelijk; niet geschikt voor publicatie |
| 6 | Bronbestand ongewijzigd | ✅ |

**Uitkomst:** vijf van de zes criteria gehaald. De run haalt de acceptatiecriteria net niet, op
criterium 4.

## Score per aangebrachte fout

| Nr. | Fout | Gevonden | Ernst in het rapport | Verwacht |
| --- | --- | --- | --- | --- |
| 1 | Topbegrip met bovenliggend begrip (`Mast`) | ✅ | Fout | Fout |
| 2 | Topbegrip met niet-bestaand bovenliggend begrip (`Bak`, `Begroeidterreindeel`) | ✅ | Fout | Fout |
| 3 | Dubbele voorkeursterm `plus-type` | ✅ | Waarschuwing | Waarschuwing |
| 4 | Identieke definities (3 niet-bgt-begrippen) | ✅ | Waarschuwing | Waarschuwing |
| 5 | Hoofdletter `Buurt` | ✅ | Waarschuwing | Waarschuwing |
| 6 | Komma in `greppel, droge sloot` | ✅ | Waarschuwing | Waarschuwing |
| 7 | Schuine streep in `inspectie- / rioolput` | ✅ | Waarschuwing | Waarschuwing |
| 8 | Werkwoordsvorm `verharden wegdeel` | ✅ | Waarschuwing, met voorbehoud | Waarschuwing |
| 9 | Tekstcoderingsfout bij `Duiker` | ✅ | **Fout** | Waarschuwing |
| 10 | Circulaire definitie `overig bouwwerk` | ✅ | Waarschuwing | Waarschuwing |
| 11 | Verweesd begrip `Paal` | ✅ | Waarschuwing | Waarschuwing |
| 12 | Collectie zonder `skos:prefLabel` | ✅ | Waarschuwing | Waarschuwing |
| 13 | Kader zonder `dct:title`, titel "Model" nietszeggend | ✅ | **Aanbeveling** | Waarschuwing |
| 14 | Engelse CamelCase `CityFurniture`@nl | ✅ | Waarschuwing | Waarschuwing |

12 van de 14 met de verwachte ernst. Fout 9 is te zwaar gewogen: een tekstcoderingsfout is geen
harde NL-SBB-regel. Fout 13 is te licht gewogen: het profiel geeft hier een sh:Warning.

## Bevindingen

1. **Verzonnen bevinding over `Molgoot`.** Het rapport neemt de profielmelding over (waarschuwing 12)
   en verklaart die met "de spiegelende broaderGeneric op Molgoot ontbreekt". Dat is onjuist:
   `Molgoot` heeft al `isothes:broaderGeneric Goot`. De melding is het bekende vals positief van
   het profiel 1.0.0, dat `isothes:broaderGeneric` niet als hiërarchie herkent. De extensie meldt
   `Molgoot` terecht niet. Het advies om een relatie toe te voegen die er al staat, is fout.
2. **Telfout over de extensie.** "13 ext:-resultaten in het ruwe rapport"; het zijn er 30 (10
   zonder de Info-meldingen). Het rapport schrijft daarnaast `Concept-UniquePrefLabelWithinSchemeShape`
   toe aan de extensie; die shape komt uit het profiel. De conclusie dat de extensie meedoet, klopt
   wel.
3. **Tegenstrijdigheid in de eerste ronde.** Het telblok zegt "geen dubbele prefLabel per taal",
   terwijl waarschuwing 3 de dubbele voorkeursterm `plus-type` noemt.
4. **De extensie ontbrak in de skill.** De assistent merkte dat zelf op en haalde het bestand op uit
   de repository. Dat verklaart waarschijnlijk ook de misser van
   [2026-09-03](2026-09-03-europese-assistent-imgeo-volledig.md), waar de extensie "niet beschikbaar"
   was. De oorzaak zit in de verpakking van de skill voor de workspace-registry, niet in het model.
5. **Gereedschap aangepast.** De assistent schreef `scan.py` naar een tijdelijke map en verbeterde
   daar "een tikfout in een melding". Het bronbestand bleef ongewijzigd, maar een aangepast script
   maakt de run minder goed herhaalbaar.
6. **Bronnencontrole goed opgevat**, anders dan op 2026-09-03: het rapport stelt vast dat er geen
   `dct:source` is, test daarna de begrip- en kader-URI's (HTTP 404 op een bereikbare host) en
   stelt geen hosts voor de bronnenlijst voor.
7. **Wat verder goed ging:** de SHACL-telling komt uit de resultaten en niet uit het
   `conforms`-veld; de assistent herstelde zelf een fout in zijn telscript (`sh:severity` in plaats
   van `sh:resultSeverity`); alle telbare structuurfeiten kloppen (18 topbegrippen, 14 begrippen
   zonder relatie, 2 zwevende doelen); het rapport vermeldt wat uitputtend en wat oordelend is
   gedaan.

## Vergelijking met 2026-09-03

| | 2026-09-03 (volledig IMGeo) | 2026-10-23 (IMGeo-mini) |
| --- | --- | --- |
| Extensie meegenomen | Nee | Ja, zelf opgehaald |
| Harde fouten gevonden | 0 van 48 | 3 van 3 |
| Verzonnen bevindingen | 0 | 1 (`Molgoot`) |
| Telfouten | 1 (14 relaties i.p.v. 39) | 1 (13 extensieresultaten i.p.v. 30) |
| Bronnencontrole | Verkeerd opgevat | Goed opgevat |

Het verschil in omvang (464 tegen 20 begrippen) maakt de twee runs niet direct vergelijkbaar.
Een run op het volledige IMGeo-kader mét extensie staat nog open.

## Gevolgen voor de skill

- **Lever de extensie mee in elke verpakking** van de skill, ook in de workspace-registry. Laat de
  skill stoppen of expliciet "SHACL-validatie onvolledig" melden als het bestand ontbreekt, in
  plaats van zonder extensie door te gaan.
- **Neem het bekende vals positief op in de skill**: een begrip dat via `isothes:broader*` onder een
  ander begrip hangt en toch door het profiel als "zonder relaties" wordt gemeld, is een beperking
  van het profiel en geen fout in het kader. Dat staat nu alleen in `verwacht.md`. `conflicts.md`
  zegt bovendien dat het profiel verweesde begrippen "niet toetst"; het profiel doet dat wel, maar
  alleen met de SKOS-relaties. Die onjuiste uitleg maakt het voor een assistent lastig om de melding
  bij `Molgoot` te herkennen als beperking van het profiel.
- **Tekstcoderingsfouten zijn een waarschuwing**, geen fout. Leg dat vast bij de ernstniveaus.
