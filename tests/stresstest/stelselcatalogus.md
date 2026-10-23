# Stresstest: export van de stelselcatalogus

De volledige Turtle-export van de [stelselcatalogus](https://stelselcatalogus.nl) is een
realistisch groot kader om te testen of de skill (en tools die dezelfde validatie draaien)
het volhouden: looptijd, geheugen, en of alle bevindingen worden geteld in plaats van
gesampled.

## Bestand ophalen

Het bestand staat niet in deze repository: het is ruim 22 MB, het verandert bij elke nieuwe
export, en het bevat begrippenkaders van tientallen beheerders.

Download het via [stelselcatalogus.nl/downloads](https://stelselcatalogus.nl/downloads), met de
downloadknop bij de Turtle-export. Die pagina is de stabiele verwijzing. De directe link naar het
bestand bevat een code die bij elke upload verandert (op 2026-10-23 was dat
`https://stelselcatalogus.nl/cms/uploads/Stelselcatalogus_734c5a31a9.ttl`).

Controleer na het downloaden welke versie je hebt:

```bash
sha256sum Stelselcatalogus.ttl
```

## Geteste versie

| | Export getest op 2026-10-07 | Export op de site op 2026-10-23 |
| --- | --- | --- |
| Grootte | 22.438.861 bytes | 22.603.674 bytes |
| SHA-256 | `fa32a6c5fbca5b99a0ae76d2ca89a10ce48c18aae931142fab469fe401b0a012` | `71f42e88c82c0d56a9432367a5dea75acf691135b5cbf96514fc4d10b8fdddd4` |
| Triples | 271.875 | 273.369 |
| Begrippenkaders | 49 | 50 |
| Begrippen | 1.665 | 1.728 |
| Collecties | 134 | 134 |

De referentie-uitkomst hieronder geldt alleen voor de export van 2026-10-07. Bij een andere
export is de test bedoeld om te zien of de validatie standhoudt, niet om exacte aantallen te
vergelijken.

## Kenmerken van de export van 2026-10-07

- 49 begrippenkaders van verschillende beheerders. Het grootste is het IMGeo-kader (464
  begrippen); daarnaast onder meer TOOI-waardelijsten, het MIM-begrippenkader, Warmtenetten,
  Verkeersstatistiek Mobiliteit en EU-lijsten (Frequency, Access right). Eén kader is leeg.
- 106 begrippen zonder `skos:inScheme`; 14 begrippen in meer dan één kader.
- 700 topbegrippen.
- Taal-tags door elkaar: `nl-NL` (3.998), `nl` (1.274) en 2.869 labels zonder taal-tag.
- Bij het inlezen meldt rdflib een `xsd:date` met een maand buiten 1–12: een fout in de data.

## Referentie-uitkomst (export van 2026-10-07)

Profiel 1.0.0 uit het register plus de extensie van de skill, samengevoegd tot één shapes-graaf,
`advanced=True`, `inference=rdfs`, pySHACL 0.40.1 en rdflib 7.6.0, op een laptop met Windows 11:

| Stap | Duur |
| --- | --- |
| Inlezen | 26 s |
| SHACL-validatie | 191 s |
| Inhoudelijke scan van termen en definities | 2 s |
| Totaal | 3 min 44 s |

| sh:Violation | sh:Warning | sh:Info |
| --- | --- | --- |
| 599 | 2.033 | 1.701 |

De violations:

| Aantal | Shape | Bevinding |
| --- | --- | --- |
| 518 | `Concept-definition` | Begrip zonder `skos:definition` (512 begrippen met expliciet `rdf:type skos:Concept`; 6 meer door rdfs-inferentie) |
| 52 | `TopConceptWithBroaderShape` (extensie) | Topbegrip met een bovenliggend begrip |
| 29 | `Concept-closeMatch` | Ongeldige `skos:closeMatch` |

De grootste groepen waarschuwingen: 576 identieke definities (extensie; één resultaat per paar,
samen 112 begrippen), 383 en 313 begrippen zonder relaties (profiel en extensie), 2 × 135
dubbele voorkeurstermen (profiel), 214 bronverwijzingen die niet aan het profiel voldoen.

De inhoudelijke scan van alle termen en definities vond onder meer 495 termen met een
hoofdletter, 80 in CamelCase, 63 met een leesteken, 22 met een afkorting, 261 definities die de
eigen term bevatten (te beoordelen), 4 definities met stuurtekens en geen tekstcoderingsfouten.

## Wat de test liet zien

1. **De validatie zelf kost de tijd.** De SPARQL-regels die alle begrippen met elkaar
   vergelijken, zoals die voor identieke definities, wegen het zwaarst. pySHACL parseert
   bovendien per focus node dezelfde SPARQL-query opnieuw; een cache op de parser maakte de
   validatie in een andere test ongeveer 7 keer sneller met dezelfde uitkomst.
2. **Identieke definities worden per paar geteld.** 576 meldingen over 112 begrippen: bij grote
   kaders is dat lastig te lezen.
3. **Eén rapport voor 49 kaders is weinig bruikbaar.** Elke beheerder is verantwoordelijk voor het
   eigen kader; een rapport hoort per begrippenkader uitgesplitst te kunnen worden.
4. **Een validatie in de browser** (Python via WebAssembly) is naar verwachting 2 à 4 keer trager
   dan de commandoregel; of het werkgeheugen van de browser volstaat, is nog niet vastgesteld.
