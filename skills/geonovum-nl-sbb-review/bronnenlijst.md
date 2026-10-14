# Bekende bronnenlijst (bronnencontrole-module)

Deze lijst hoort bij de **optionele bronnencontrole-module** van de NL-SBB-skill (zie [`SKILL.md`](SKILL.md)). De module vergelijkt de **host** van elke in een begrippenkader gebruikte bron met de hosts hieronder:

- **Host staat op de lijst** → informatief ("bekende bron").
- **Host staat niet op de lijst** → waarschuwing ("onbekende bron; niet op de bekende bronnenlijst"), géén fout.

De lijst is een **hulpmiddel van deze skill**, geen normatieve of uitputtende opsomming van toegestane bronnen. Ontbreken op de lijst betekent niet dat een bron ongeldig is — alleen dat de skill hem (nog) niet kent. De lijst is in dialoog met de gebruiker uit te breiden; zie "Bronnenlijst uitbreiden" in [`SKILL.md`](SKILL.md).

## Officiële NL-SBB / Geonovum-bronnen

| Host | Toelichting |
|------|-------------|
| `register.geostandaarden.nl` | Register met de normatieve SHACL-profielen per versie |
| `docs.geostandaarden.nl` | Publicatie van de NL-SBB-standaard (laatste en vastgestelde versies) |
| `geonovum.github.io` | Werkversies / spiegel van NL-SBB |
| `github.com` | Broncode NL-SBB-profiel (Geonovum/NL-SBB), fallback |
| `raw.githubusercontent.com` | Ruwe bestanden uit de Geonovum/NL-SBB-repository |

## Aanvullende landelijke bronnen

| Host | Toelichting |
|------|-------------|
| `definities.geostandaarden.nl` | Begrippen/definities-service (Skosmos) van Geostandaarden |
| `stelselcatalogus.nl` | Stelselcatalogus Omgevingswet |
| `wetten.overheid.nl` | Officiële publicatie van Nederlandse wet- en regelgeving |
| `noraonline.nl` | Nederlandse Overheid Referentie Architectuur (NORA) |

## Wijzigingslog

| Datum | Host toegevoegd/verwijderd | Grond |
|-------|----------------------------|-------|
| 2026-07-21 | Initiële lijst (bovenstaande hosts) | Officiële NL-SBB/Geonovum-bronnen + door gebruiker aangedragen landelijke bronnen |
| 2026-07-21 | `wetten.overheid.nl` toegevoegd | Op verzoek van de gebruiker; officiële publicatielocatie van Nederlandse wetgeving |
| 2026-07-21 | `wetten.nl` verwijderd | Op verzoek van de gebruiker; vervangen door de officiële host `wetten.overheid.nl` |

> **Noot bij `wetten.overheid.nl`:** dit is de officiële publicatielocatie van Nederlandse wetgeving. Een eerder op verzoek opgenomen `wetten.nl` is verwijderd ten gunste van deze host.
