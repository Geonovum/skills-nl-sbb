# NL-SBB-skills

Agent-skills van [Geonovum](https://www.geonovum.nl) voor [NL-SBB](https://docs.geostandaarden.nl/nl-sbb/nl-sbb/), de Nederlandse standaard voor het beschrijven van begrippen.

Een agent-skill is een map met een instructiedocument (`SKILL.md`) dat een AI-assistent erbij pakt zodra het onderwerp langskomt. De skills staan in de repository van de standaardbeheerder. De metadata staat in `publiccode.yml` en in de frontmatter van elke skill, en de status per skill staat in `nl.gov.status`.

> **Let op.** De skills zijn hulpmiddelen en maken geen deel uit van de standaard. De publicatie op docs.geostandaarden.nl en het SHACL-profiel in het register zijn leidend. Zie [DISCLAIMER.md](DISCLAIMER.md).

## Skills

| Skill | Status | Doel |
| --- | --- | --- |
| [`geonovum-nl-sbb-review`](skills/geonovum-nl-sbb-review/SKILL.md) | concept | Beoordeelt een begrippenkader (Turtle, RDF/XML, Excel, Word of URL) aan de hand van NL-SBB 1.0.0: inhoudelijke review van termen, definities, bronnen en relaties, met als optionele modules een SHACL-validatie tegen het normatieve profiel en een bronnencontrole. Rapporteert fouten, waarschuwingen en aanbevelingen en wijzigt het bronbestand nooit. |

De status `concept` betekent dat de werkgroep NL-SBB de skill nog niet heeft vastgesteld. Een hogere status vraagt een expertreview, een gepubliceerde reviewprocedure met acceptatiecriteria, en een test met minstens twee assistenten waarvan één open source of Europees.

## Installeren

De skills worden aangeboden via de [skills-marketplace van developer.overheid.nl](https://github.com/developer-overheid-nl/skills-marketplace) als plugin `geonovum-nl-sbb`. De installatie-instructies per assistent staan in de README van die marketplace.

Zonder marketplace: kopieer de map `skills/geonovum-nl-sbb-review/` naar de skillmap van je assistent. Welke map dat is, staat in de documentatie van de assistent.

## Gebruik

Vraag je assistent een begrippenkader te beoordelen volgens NL-SBB en geef het bestand of de URL mee. De skill legt bij het eerste gebruik twee optionele modules voor (SHACL-validatie en bronnencontrole) en levert een rapport met totaaloordeel en publicatieadvies. Voor de SHACL-validatie zijn Python 3 en [pySHACL](https://github.com/RDFLib/pySHACL) nodig; de skill installeert pySHACL zelf als het ontbreekt.

## Relatie tot de standaard

| Bron | Rol |
| --- | --- |
| [NL-SBB, vastgestelde versie 1.0.0](https://docs.geostandaarden.nl/nl-sbb/def-st-nl-sbb-20241010/) | Normatieve tekst waarop de skills zijn gebouwd (`nl.gov.source`, en `supports` in `publiccode.yml`) |
| [NL-SBB, laatste versie](https://docs.geostandaarden.nl/nl-sbb/nl-sbb/) | Startpunt om te controleren of er een nieuwere versie is |
| [SHACL-profiel 1.0.0](https://register.geostandaarden.nl/shacl/nl-sbb/1.0.0/skos-ap-nl.ttl) | Normatief profiel dat de skill tijdens een review ophaalt |
| [Geonovum/NL-SBB](https://github.com/Geonovum/NL-SBB) | Broncode van de standaard; issues over de standaard zelf horen daar |

Regels die de skill wel toetst maar het profiel niet, staan met de reden in [`conflicts.md`](skills/geonovum-nl-sbb-review/conflicts.md) en als SHACL-extensie in [`skos-ap-nl-extensie.ttl`](skills/geonovum-nl-sbb-review/skos-ap-nl-extensie.ttl). Die extensie is een hulpmiddel van de skill, geen onderdeel van het normatieve profiel.

## Bijdragen

Fouten in een skill meld je als [issue](https://github.com/Geonovum/skills-nl-sbb/issues). Fouten in de standaard zelf horen in [Geonovum/NL-SBB](https://github.com/Geonovum/NL-SBB/issues). Werkafspraken voor wijzigingen staan in [CONTRIBUTING.md](CONTRIBUTING.md).

## Licentie

Copyright © 2026 Geonovum. Licensed under the EUPL.

De skills vallen onder de [EUPL-1.2](LICENSE). Alle taalversies van de EUPL zijn gelijkwaardig; de [Nederlandse tekst](https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:32017D0863) staat in het Publicatieblad van de EU. De standaard NL-SBB zelf valt onder CC-BY van Geonovum.
