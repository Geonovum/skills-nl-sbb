# NL-SBB Review — Bronbeperkingen en keuzes

Geconstateerd: 2026-07-20

Dit document beschrijft bekende beperkingen van de bronnen en de keuzes die in deze skill zijn gemaakt.

## Bron van waarheid en versiekoppeling

- Deze skill is gemaakt voor **NL-SBB versie 1.0.0** en gebruikt standaard het profiel `https://register.geostandaarden.nl/shacl/nl-sbb/1.0.0/skos-ap-nl.ttl`.
- De **standaard** op https://docs.geostandaarden.nl/nl-sbb/nl-sbb/ verwijst altijd naar de laatste versie en is normatief leidend. Deze pagina wordt alleen geraadpleegd wanneer de gebruiker vraagt of er een nieuwere versie is.
- Het **SHACL-profiel** wordt per versie gepubliceerd in het register: `https://register.geostandaarden.nl/shacl/nl-sbb/<versie>/skos-ap-nl.ttl`, waarbij het versienummer in de URL gelijk is aan dat van de standaard.
- De **GitHub-bron** (`Geonovum/NL-SBB`, map `shacl/1.0.0/`, vastgepind op de commit waarin die map is toegevoegd) is een fallback voor als het register onbereikbaar is. De map `profiles/` in die repository is legacy en wordt niet meer gebruikt. Controleer bij gebruik `owl:versionInfo` in het bestand.

De agent valideert standaard tegen 1.0.0. Een nieuwere versie wordt niet automatisch toegepast: eerst controleren (via de standaard-URL en `owl:versionInfo` in het profiel), de status bepalen (DEF/VV/CV), en pas na expliciete bevestiging van de gebruiker toepassen — met de waarschuwing dat de skill niet alle aspecten van de nieuwe versie noodzakelijk correct controleert. De procedure staat in [`SKILL.md`](SKILL.md) onder "Controleren op een nieuwere versie".

## Status van een versie (DEF/VV/CV)

NL-SBB is een ReSpec-document. De status van een versie is vastgelegd in de persistente URI (statusparameter, bijvoorbeeld een pad- of query-segment) én in tekst in de kop van het document. Mogelijke statussen:

- **Vastgestelde versie (DEF)** — officieel goedgekeurd;
- **Versie ter vaststelling (VV)** — aangeboden voor vaststelling, nog niet definitief;
- **Consultatieversie (CV)** — in openbare consultatie, kan nog wijzigen.

Baseer de statusbepaling op beide bronnen (URI én tekst) en meld waarop de conclusie berust. Is de status niet eenduidig af te lezen, meld dat als onzekerheid.

## Laatst geverifieerde versie

- Op 2026-07-20 was de laatst bekende profielversie **1.0.0** (`owl:versionInfo "1.0.0"`, `rdfs:label "Toepassingsprofiel Nederlandse standaard voor het beschrijven van begrippen in RDF"@nl`), geverifieerd via de GitHub-bron.
- Op 2026-07-21 opnieuw geverifieerd: de laatst gepubliceerde standaard is de **Vastgestelde versie (DEF) van 10 oktober 2024** (persistente URI `docs.geostandaarden.nl/nl-sbb/def-st-nl-sbb-20241010`), en het register meldt nog steeds `owl:versionInfo "1.0.0"`. Geen nieuwere versie beschikbaar.

## SHACL-profiel dekt niet alle regels

Het normatieve profiel meldt sommige NL-SBB-regels niet, of met een andere ernst dan de tekst van de standaard suggereert. Bekend:

| Regel | Standaard/skill | SHACL-profiel v1.0.0 |
|---|---|---|
| Topbegrip met bovenliggend begrip via `isothes:broaderGeneric` | Fout | Niet getoetst |
| Semantische/hiërarchische relatie naar niet-begrip | Fout (skill) | `sh:Warning` |
| Harmonisatierelatie binnen hetzelfde kader | Fout | Niet getoetst |
| Dubbele `skos:notation` binnen één kader | Fout | Niet expliciet getoetst |
| Verweesd begrip | Waarschuwing | Niet getoetst |
| Identieke definities bij meerdere begrippen | Waarschuwing | Niet getoetst |

Hiervoor levert de skill de extensie [`skos-ap-nl-extensie.ttl`](skos-ap-nl-extensie.ttl). **Bij een discrepantie tussen de ernst uit het SHACL-profiel en die uit de standaardtekst is de standaardtekst leidend**; rapporteer beide en licht de keuze toe.

## Netwerktoegang

In sommige uitvoeromgevingen zijn `docs.geostandaarden.nl` en `register.geostandaarden.nl` niet bereikbaar (allowlist). Kan het profiel niet uit het register worden gehaald, gebruik dan de GitHub-fallback en meld dit expliciet in het rapport. Kan de te beoordelen bron zelf niet volledig worden gelezen, gebruik dan het totaaloordeel **Niet volledig te beoordelen**.

## Invoerformaten

Turtle/TTL en RDF/XML zijn direct met rdflib/pySHACL te valideren. Excel en Word vereisen eerst een conversie naar RDF vóór SHACL-validatie; zonder betrouwbare conversie beperkt de review zich tot een inhoudelijke beoordeling en wordt dit als beperking gemeld.
