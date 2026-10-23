# 2026-10-05 — Vergelijking met de Kwaliteitsregeltaal-validator (MCP)

Vergelijking van de skill met de NL-SBB-regelset van de
[Kwaliteitsregeltaal-validator](https://kwaliteitsregistratie.datastelsel.nl/validator/), via de
MCP-server op `https://kwaliteitsregistratie.datastelsel.nl/validator/mcp` (server `krt` 1.30.0,
tool `validate_nl_sbb`, engine Fuseki, 119 regels). Testmateriaal:
[IMGeo-mini](../fixtures/imgeo-mini/verwacht.md).

**Skillversie:** de interne versie `validatie-nl-sbb` van oktober 2026, met het script
`scripts/inhoudelijke-scan.py` en profiel en extensie samengevoegd tot één shapes-graaf. De
gepubliceerde versie 0.1.0 heeft geen scanscript; zie het
[verslag van 2026-08-28](2026-08-28-portabiliteit-en-lichte-modellen.md#stand-in-de-gepubliceerde-skill).
De skill draaide in Claude Code met Claude Opus 5.5 (`claude-opus-5-5`); SHACL met pySHACL 0.40.1 en
rdflib 7.6.0.

## Uitkomst per aangebrachte fout

| Nr. | Aangebrachte fout | Skill | Kwaliteitsregeltaal |
| --- | --- | --- | --- |
| 1 | Topbegrip met bestaand bovenliggend begrip (`Mast`) | Fout | Gemist |
| 2 | Topbegrip met niet-bestaand bovenliggend begrip (`Bak`, `Begroeidterreindeel`) | Fout en waarschuwing | Alleen waarschuwing ("is geen Concept") |
| 3 | Dubbele voorkeursterm `plus-type` | Waarschuwing | Fout |
| 4 | Drie identieke definities | Waarschuwing | Gemist |
| 5–8, 14 | Termconventies (hoofdletter, leestekens, werkwoord, Engelse CamelCase) | Waarschuwing (scan; het werkwoord vraagt oordeel) | Gemist |
| 9 | Tekstcoderingsfout in definitie | Waarschuwing | Gemist |
| 10 | Circulaire definitie | Waarschuwing | Gemist |
| 11 | Verweesd begrip (`Paal`) | Waarschuwing | Gemist |
| 12 | Collectie zonder `skos:prefLabel` | Waarschuwing | Waarschuwing |
| 13 | Begrippenkader zonder `dct:title` | Waarschuwing | Waarschuwing |

Skill: alle 14 gevonden. Kwaliteitsregeltaal: 4 gevonden, waarvan 1 met een lagere ernst.

## Aantallen

| | Fout | Waarschuwing | Informatief |
| --- | --- | --- | --- |
| Skill (SHACL) | 3 | 17 | 20 |
| Kwaliteitsregeltaal | 21 | 4 | – |

## Oorzaken van de verschillen

**Gemist door de Kwaliteitsregeltaal-regelset:**

- `top_concept_heeft_geen_broader` toetst alleen `skos:broader`. Alle hiërarchie- en lusregels
  zijn SKOS-only en kennen de ISO 25964-relaties niet; daardoor vallen fout 1 en 2 buiten de
  controle.
- `geen_dode_broaderGeneric` vertaalt naar SPARQL met `skos:broaderGeneric` (in plaats van
  `isothes:broaderGeneric`) en `?s skos:x_broaderGeneric` als predicaat, en kan dus nooit afgaan.
  Vermoedelijk geldt dat voor alle `geen_dode_*`-regels voor ISO 25964-relaties.
- Inhoudelijke controles op termen en definities bestaan niet in de regelset.

**Vals positief in de Kwaliteitsregeltaal-regelset:** 18 maal `top_concept_is_inverse` en 1 maal
`schema_moet_top_concept_hebben`, omdat `skos:hasTopConcept` nergens expliciet staat. SKOS
definieert dat als inverse van `skos:topConceptOf`, en het NL-SBB-profiel accepteert
`topConceptOf|^hasTopConcept`. 19 van de 21 fouten komen hieruit voort.

**Vals positief in de skill**, overgenomen van het profiel: `Molgoot` wordt als begrip zonder
relaties gemeld, omdat het profiel 1.0.0 `isothes:broaderGeneric` niet als hiërarchie herkent.

## Uitbreidbaarheid van de Kwaliteitsregeltaal-validator

Getest met de tools `shacl_to_krt`, `check_rule` en `validate`:

- `shacl_to_krt` laat de SHACL-SPARQL-regels van de extensie vallen; alleen de
  eigenschapsregel voor `dct:source` kwam mee.
- De taal kent `UNIEK … PER …`, `KLEINE_LETTERS(…)` en `BEVAT "…"`. Daarmee zijn identieke
  definities, hoofdletters, leestekens en tekstcoderingsfouten uit te drukken. Reguliere
  expressies (`VOLDOET AAN`, `MATCHT`) en vergelijking van twee velden (`BEVAT` met een veld)
  geven een syntaxfout; CamelCase, meervoud en circulariteit zijn dus niet te vangen.
- Eigen regels via `validate` evalueerden op RDF 0 objecten, ook met `skos:`-prefixen: de
  gegenereerde SPARQL zoekt op `ex:Concept`, en hoe dat in te stellen is, is niet gedocumenteerd.

## Conclusie

De twee vullen elkaar aan. De Kwaliteitsregeltaal-validator is deterministisch, koppelt regels aan
kwaliteitsmetrieken en rapporteert in DQV, maar is op deze testset een SKOS-only structuurcheck
met twee defecte regels en een strengere eis voor `hasTopConcept` dan het profiel. De skill vindt
alle aangebrachte fouten, maar neemt een vals positief van het profiel over.

De bevindingen over de regelset zijn bedoeld voor de beheerder van de Kwaliteitsregeltaal-validator.
