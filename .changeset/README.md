# Changesets

Deze map hoort bij [Changesets](https://github.com/changesets/changesets), waarmee versie en CHANGELOG van deze repository worden bijgehouden.

Elke pull request die een skill of de repo-opzet wijzigt, voegt een changeset toe:

```bash
npx changeset
```

Kies `patch` voor een correctie in een bestaande beoordeling, `minor` voor nieuwe functionaliteit of een nieuwe standaardversie in de versietabel, en `major` voor een andere rapportstructuur of ander standaardgedrag. Beschrijf de wijziging in het Nederlands, vanuit de gebruiker van de skill.

Zodra er changesets op `main` staan, opent de workflow in `.github/workflows/release.yml` een pull request "Nieuwe release". Daarin is `npm run version` gedraaid: dat verhoogt de versie in `package.json`, schrijft de CHANGELOG, zet dezelfde versie in `.plugin/plugin.json`, `publiccode.yml` en `nl.gov.version` van elke skill en de datum van die dag in `publiccode.yml`, en genereert de manifesten per assistent opnieuw. Wie die PR merget, geeft de release vrij: de workflow zet dan de tag `v<versie>` en maakt de GitHub-release aan met de CHANGELOG-tekst van die versie. Draai `npm run version` niet zelf op `main`. De releasedatum in `publiccode.yml` is de dag waarop de versie-PR het laatst is bijgewerkt; merge hem op die dag, dan klopt hij met de GitHub-release.

Tot de eerste release staat de versie op 0.0.0 en is er geen CHANGELOG; de eerste changeset (`eerste-release.md`) levert via diezelfde PR versie 0.1.0 op.

Dit pakket wordt niet naar npm gepubliceerd; `package.json` is privaat en bestaat alleen voor Changesets.
