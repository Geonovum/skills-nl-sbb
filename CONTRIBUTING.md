# Bijdragen aan NL-SBB-skills

Allereerst bedankt dat je wilt bijdragen aan dit project! Zonder jouw input
wordt dit nooit een beter open source project.

## Code of Conduct

Dit project hanteert een [Code of Conduct](CODE_OF_CONDUCT.md). Door bij te
dragen aan dit project ga je akkoord met de voorwaarden hiervan.

## Hoe kan je bijdragen?

Er zijn verschillende manieren om bij te dragen aan dit project:

### Meld een bug

Heb je een bug gevonden? Maak dan een [issue](https://github.com/Geonovum/skills-nl-sbb/issues/new) aan met:

- Een duidelijke en beschrijvende titel
- Stappen om de bug te reproduceren
- Verwacht gedrag vs. daadwerkelijk gedrag
- Foutmeldingen of het rapport dat de skill opleverde (indien van toepassing)
- Welke assistent je gebruikte en, als het om de SHACL-validatie gaat, de versie van pySHACL

### Features voorstellen

Heb je een idee voor een nieuwe feature? Open een issue met:

- Een duidelijke beschrijving van de feature
- Waarom deze feature waardevol zou zijn
- Eventuele voorbeelden, zoals een begrippenkader waarop de skill tekortschiet

### Documentatie verbeteren

Documentatie kan altijd beter! Pull requests voor verbeteringen aan de
documentatie zijn zeer welkom.

### Code bijdragen

Wil je code bijdragen? Volg dan onderstaand proces.

## Ontwikkelproces

### Werkafspraken

- **Taal.** Alles in deze repository is Nederlands: skillteksten, omschrijvingen, commits en documentatie. Engelse vaktermen (skill, SHACL, SKOS) blijven Engels.
- **Branch en pull request.** Wijzigingen gaan via een branch en een pull request met een review. Op `main` commit je niet rechtstreeks.
- **Changeset per wijziging.** Elke pull request die een skill of de repo-opzet wijzigt, voegt met `npx changeset` een changeset toe: `patch` voor een correctie, `minor` voor nieuwe functionaliteit of een nieuwe standaardversie, `major` voor een andere rapportstructuur of ander standaardgedrag. De releaseworkflow bundelt open changesets in een versie-PR; bij merge daarvan volgen tag en GitHub-release. Zie `.changeset/README.md`.
- **Eén bron, gegenereerde afgeleiden.** `.plugin/plugin.json` is het enige manifest dat je bewerkt. De manifesten in de mappen per assistent genereer je met `python3 scripts/generate_plugin.py`; `npm run check` faalt als ze afwijken. Bewerk ze nooit met de hand.
- **Geen productnamen.** Buiten de gegenereerde manifestmappen (de verborgen mappen met de naam van een assistent) komt geen naam van een AI-assistent of model voor, ook niet in de skilltekst of in `allowed-tools`. Beschrijf een handeling, niet het product. Er zijn twee uitzonderingen: `scripts/generate_plugin.py`, dat de mappen per assistent bij naam moet noemen om ze te kunnen schrijven, en de testverslagen in `tests/verslagen/`, die juist moeten vastleggen met welke assistent, welk model en welke versie getest is. Zonder die namen is een test niet na te gaan of te herhalen.

### Een skill wijzigen

- De map heet gelijk aan `name` in de frontmatter en begint met de slug `geonovum-`.
- De frontmatter bevat `name`, `description`, `license` en in `metadata` de `nl.gov.`-sleutels. Datums schrijf je als JJJJ-MM-DD; een sleutel zonder waarde laat je weg.
- Een gepubliceerde skillnaam wijzigt niet meer. Moet het toch, zet dan de oude naam in `nl.gov.previous-name`.
- Een skill is een samenvatting, niet de standaard zelf. Waar de skill afwijkt van of strenger is dan het normatieve SHACL-profiel, leg je dat met de reden vast in `conflicts.md` van die skill.
- `SKILL.md` blijft onder de 500 regels; achtergrond hoort in `reference.md`.
- Bewaak `nl.gov.review-by`: bij een nieuwe versie van NL-SBB of het verstrijken van de datum wordt de skill herzien en krijgt hij een nieuwe release.

### Status van een skill

`nl.gov.status` is een van `concept`, `development`, `beta`, `stable` of `obsolete`. Een status boven `concept` vraagt een expertreview van de inhoud en van wat de skill aanroept, een gepubliceerde reviewprocedure met acceptatiecriteria, en een test met minstens twee assistenten waarvan één open source of Europees. De procedure, de acceptatiecriteria en de verslagen staan in [`tests/`](tests/README.md). De vaststelling als `stable` doet de werkgroep NL-SBB; dan wordt ook `nl.gov.approved-by` ingevuld.

### Lokaal controleren

Nodig: Node.js 22.11 of nieuwer en Python 3.

```bash
npm ci
npm run check
```

Dat controleert of de manifesten per assistent gelijk zijn aan wat `.plugin/plugin.json` oplevert en of de versie in `package.json`, `.plugin/plugin.json` en `publiccode.yml` gelijk is.

### Een skill testen

Wijzig je de werkwijze van een skill, draai dan het ijkpunt en minstens het regressiekader
IMGeo-mini opnieuw, en leg de uitkomst vast in `tests/verslagen/`. Zie [`tests/README.md`](tests/README.md).

```bash
python3 tests/ijkpunt.py tests/fixtures/imgeo-mini/imgeo-mini.ttl
```

## Licentie

Door bij te dragen aan dit project ga je ermee akkoord dat je bijdragen worden
gelicenseerd onder de [EUPL-1.2](LICENSE) licentie. Dit betekent dat:

- Je het auteursrecht behoudt op je bijdragen
- Je bijdragen beschikbaar komen onder dezelfde open source licentie
- De code gebruikt mag worden door andere overheidsorganisaties

---

Bedankt voor je bijdrage!

_Dit project wordt onderhouden door Geonovum en de open source
community._
