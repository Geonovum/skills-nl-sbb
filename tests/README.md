# Tests

Testmateriaal, referentie-uitkomsten en verslagen voor de skill `geonovum-nl-sbb-review`. Deze map
gaat niet mee met de plugin: alleen `skills/` wordt geïnstalleerd.

Een status boven `concept` vraagt volgens [CONTRIBUTING.md](../CONTRIBUTING.md#status-van-een-skill)
een gepubliceerde reviewprocedure met acceptatiecriteria en een test met minstens twee
assistenten, waarvan één open source of Europees. Deze map is die procedure.

## Inhoud

| Pad | Inhoud |
| --- | --- |
| [`evals.json`](evals.json) | Testgevallen: prompt, invoerbestanden en verwachte bevindingen per geval. Het formaat (prompt, bestanden, verwachtingen) is het gangbare formaat voor evals van skills, zodat de tests met elke assistent opnieuw te draaien zijn |
| [`ijkpunt.py`](ijkpunt.py) | Onafhankelijke SHACL-referentie, zonder assistent. Rapporten van de skill worden hiertegen gescoord |
| [`fixtures/imgeo-mini/`](fixtures/imgeo-mini/verwacht.md) | Regressiekader van 20 begrippen met 14 aangebrachte fouttypen, de gewenste uitkomst en de SHACL-referentie |
| [`stresstest/stelselcatalogus.md`](stresstest/stelselcatalogus.md) | De volledige export van de stelselcatalogus (ruim 22 MB, circa 50 begrippenkaders) als stresstest: bron, controlegetal en referentie-uitkomst. Het bestand zelf staat niet in de repository |
| [`verslagen/`](verslagen/) | Verslagen van testrondes, met datum, skillversie en de gebruikte assistent en het model. Alleen hier mogen namen van assistenten en modellen staan (zie CONTRIBUTING.md) |

## Procedure

1. **Bepaal eerst het ijkpunt**, zonder assistent:
   ```bash
   pip install pyshacl rdflib
   python3 tests/ijkpunt.py tests/fixtures/imgeo-mini/imgeo-mini.ttl
   ```
   Wijkt de uitkomst af van [`verwacht.md`](fixtures/imgeo-mini/verwacht.md), zoek dan eerst de
   oorzaak (nieuwe versie van het profiel, de extensie of pySHACL) voordat je assistenten test.
2. **Test de skill via het bestandspad**, niet via een geïnstalleerde versie. Instrueer de
   assistent expliciet om `skills/geonovum-nl-sbb-review/SKILL.md` uit de werkkopie te lezen en
   te volgen; anders test je de vorige versie.
3. **Draai elk testgeval uit `evals.json` per assistent**, met een identieke prompt en elk in een
   eigen werkmap, zodat runs elkaars bestanden niet overschrijven.
4. **Scoor elk rapport** tegen de `expectations` van het testgeval en tegen het ijkpunt: per
   aangebrachte fout gevonden met de juiste ernst, gevonden met een andere ernst, of gemist;
   daarnaast verzonnen bevindingen en telfouten.
5. **Leg de ronde vast** in `verslagen/JJJJ-MM-DD-<onderwerp>.md`: skillversie of commit,
   assistent, model en versie, omgeving (met of zonder shell), per testgeval de score, tokens en
   duur waar bekend, en wat er naar aanleiding van de ronde is aangepast.

Het kleine kader is bedoeld om snel te zien of een gemiste bevinding aan de skill of het model
ligt. De stresstest laat zien of de werkwijze schaalt: bij honderden begrippen gaan assistenten
steekproeven nemen in plaats van alles te lezen.

## Acceptatiecriteria

Voorstel; de vaststelling doet de werkgroep NL-SBB.

Op IMGeo-mini, per assistent:

1. De SHACL-telling is gelijk aan het ijkpunt: 3 sh:Violation, 17 sh:Warning, 20 sh:Info.
2. Alle drie de fouten (aangebrachte fout 1 en 2) worden als Fout gemeld.
3. Minstens 12 van de 14 aangebrachte fouttypen worden gevonden.
4. Geen verzonnen bevindingen en geen telfouten.
5. Totaaloordeel "Voldoet gedeeltelijk" of "Voldoet niet", publicatieadvies "nee".
6. Het bronbestand is ongewijzigd.

Over de assistenten heen: de criteria worden gehaald met minstens twee assistenten, waarvan één
open source of Europees. Bij een assistent zonder shell vervalt criterium 1; het rapport moet dan
vermelden dat de SHACL-validatie is overgeslagen.

Op de stresstest: de validatie loopt tot het eind en het rapport vermeldt welke controles
uitputtend en welke op steekproef zijn gedaan.

## Testrondes

| Datum | Onderwerp | Assistenten | Verslag |
| --- | --- | --- | --- |
| 2026-08-28 | Portabiliteit van de skill en werking op lichtere modellen | 3 modellen van één aanbieder | [verslag](verslagen/2026-08-28-portabiliteit-en-lichte-modellen.md) |
| 2026-10-05 | Vergelijking met de Kwaliteitsregeltaal-validator via MCP | 1 model | [verslag](verslagen/2026-10-05-vergelijking-kwaliteitsregeltaal-mcp.md) |
| 2026-10-07 | Stresstest met de export van de stelselcatalogus (zonder assistent) | – | [stresstest](stresstest/stelselcatalogus.md) |

**Nog open:** een testronde met een open-source of Europese assistent, en met een lokaal
draaiende assistent. Het verslag van 2026-08-28 onderzoekt alleen of de skill in andere
omgevingen leesbaar is; de skill is daar niet in gedraaid.
