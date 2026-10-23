# 2026-09-03 — Testrun met Mistral op het volledige IMGeo-kader

Eerste testrun met een Europese assistent. Gescoord op 2026-10-23 tegen het ijkpunt.

| | |
| --- | --- |
| Assistent | Mistral, met internettoegang en Python 3.12.14 *(omgeving en modelversie nog aan te vullen)* |
| Skillversie | `validatie-nl-sbb`, met een scanscript (`scan.py`) en een bestand `shacl.md` *(precieze versie nog aan te vullen)*. Andere indeling dan zowel de versie van augustus als de gepubliceerde 0.1.0 |
| Testkader | IMGeo-begrippenkader, [`https://upload.begrippenxl.nl/storage/imgeo/imgeo.ttl`](https://upload.begrippenxl.nl/storage/imgeo/imgeo.ttl): 6.102 triples, 464 begrippen, 57 collecties, 1 kader. Op 2026-10-23 opnieuw gedownload: zelfde aantal triples, SHA-256 `67c104bf13f56a8ee85418231e1a02c9705b123cc90852bb6da08e770a3ff36e` |
| Verloop | Drie prompts: (1) "valideer deze URL", waarop alleen de basisreview draaide; (2) "voer de SHACL-module en de bronnencontrole uit"; (3) "bied het rapport aan als Markdown" |

## Ijkpunt voor dit kader

```bash
python3 tests/ijkpunt.py imgeo.ttl
```

| | sh:Violation | sh:Warning | sh:Info |
| --- | --- | --- | --- |
| Profiel 1.0.0 + extensie | 48 | 919 | 464 |
| Alleen profiel 1.0.0 | 0 | 351 | 0 |

De 48 violations zijn allemaal `TopConceptWithBroaderShape` (extensie): 39 topbegrippen met in
totaal 48 `isothes:broaderGeneric`-relaties. De 351 waarschuwingen van het profiel bestaan uit
254 meldingen voor dubbele voorkeurstermen (127 begrippen, door twee shapes gemeld), 57 collecties
zonder `skos:prefLabel`, 39 `isothes:broaderGeneric`-relaties naar iets dat geen begrip is, en 1
kader zonder `dct:title`. Ze gaan over 224 verschillende focus nodes.

Overige feiten uit het kader: alle 464 begrippen zijn topbegrip; 425 begrippen hebben geen enkele
semantische relatie; 39 relaties verwijzen naar 14 verschillende doelen die niet in het bestand
staan; geen enkel begrip heeft `dct:source`.

## Score

| Bevinding | Rapport | Werkelijkheid | Oordeel |
| --- | --- | --- | --- |
| Omvang (464 / 57 / 1) | 464 / 57 / 1 | 464 / 57 / 1 | Juist |
| Alle begrippen topbegrip, platte lijst | Gemeld als waarschuwing | 464 van 464 | Juist |
| Topbegrip met bovenliggend begrip | Niet gemeld | 39 begrippen, 48 sh:Violation | **Gemist** (zwaarste fout) |
| Collecties zonder `skos:prefLabel` | 57, als Fout | 57, sh:Warning in het profiel | Juist aantal, ernst te hoog |
| Relaties naar niet-bestaande begrippen | "14 relaties", als Fout | 39 relaties naar 14 doelen | **Telfout** |
| Dubbele voorkeurstermen | Niet gemeld | 127 begrippen | **Gemist** |
| Begrippen zonder semantische relatie | 425 | 425 | Juist |
| Ontbrekende `dct:source` | 464 | 464 | Juist |
| Ontbrekende kadermetadata (`dct:title` e.a.) | Gemeld | Juist | Juist |
| Termconventies, identieke en circulaire definities | Gemeld met aantallen uit het scanscript | Niet afzonderlijk nagerekend | – |
| Ontbrekende definities of voorkeurstermen | 0 | 0 | Juist; geen verzonnen bevindingen |
| SHACL-telling | 0 / 351 / 0 | 0 / 351 / 0 zonder extensie | Juist voor wat er gedraaid is |
| Uitsplitsing van de 351 waarschuwingen | "Alle 351 betreffen `isothes:broaderGeneric` naar niet-begrippen"; "351 begrippen" | 39 daarvan; 224 focus nodes | **Onjuist** |
| Totaaloordeel en publicatieadvies | Voldoet niet, nee | Voldoet niet, nee | Juist, maar op grond van de verkeerde fouten |

## Bevindingen

1. **De extensie is niet meegenomen.** Het rapport zegt zelf: "bestand niet beschikbaar in deze
   omgeving", en adviseert de extensie alsnog toe te voegen. Daardoor ontbreken de 48 harde
   fouten. Dit is dezelfde blinde vlek als het `-e`-defect uit het
   [verslag van 2026-08-28](2026-08-28-portabiliteit-en-lichte-modellen.md), met een andere oorzaak:
   de omgeving gaf geen toegang tot de bestanden naast `SKILL.md`, of de assistent heeft ze niet
   gezocht. De zelfcontrole uit de skill (er moet minstens één shape uit de extensie in de
   resultaten staan) had dit moeten tegenhouden.
2. **De SHACL-uitkomst is verkeerd samengevat.** De telling klopt, maar de toelichting schrijft
   alle 351 waarschuwingen toe aan één oorzaak. Daardoor missen de 127 dubbele voorkeurstermen in
   het rapport, terwijl ze in de ruwe uitvoer stonden.
3. **Telfout bij kapotte relaties.** "14 relaties" zijn 14 doel-URI's; het gaat om 39 relaties.
   Hetzelfde patroon als bij het lichtste model in augustus: het juiste getal is af te leiden uit
   de eigen uitvoer.
4. **De bronnencontrole is verkeerd opgevat.** Het kader heeft geen enkele `dct:source`. De
   assistent controleerde daarom de hosts van namespaces en begrip-URI's (`www.w3.org`,
   `stelselcatalogus.omgevingswet.overheid.nl`) en adviseert die aan de bronnenlijst toe te
   voegen. Dat zijn geen bronnen van definities.
5. **Ernst van collecties zonder `skos:prefLabel`.** Gemeld als Fout; het profiel geeft
   sh:Warning. De skill zegt een advies niet als harde overtreding te presenteren als dat niet uit
   NL-SBB volgt.
6. **Wat goed ging:** alle telbare feiten uit het scanscript zijn juist overgenomen, er zijn geen
   verzonnen bevindingen, en het rapport benoemt welke modules zijn overgeslagen en wat niet is
   gecontroleerd.

## Gevolgen voor de skill

- De zelfcontrole op de extensie moet harder: ontbreekt de extensie, dan is het oordeel over de
  SHACL-validatie "niet volledig uitgevoerd" en niet een telling zonder voorbehoud.
- Leg in de skill vast dat de bronnencontrole zonder `dct:source` uitkomt op "geen bronnen om te
  controleren", en dat namespace-hosts geen bronnen zijn.
- Laat de uitsplitsing van SHACL-resultaten per shape uit de ruwe uitvoer komen, niet uit een
  samenvatting door de assistent.
