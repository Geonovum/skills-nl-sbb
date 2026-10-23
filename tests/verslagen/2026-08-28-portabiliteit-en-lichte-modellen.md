# 2026-08-28 — Portabiliteit en werking op lichtere modellen

Verslag van een testsessie met de skill onder de vorige naam `validatie-nl-sbb` (daarvoor
`nl-sbb`), op NL-SBB 1.0.0. De cijfers zijn in die sessie gemeten, niet geschat. Waar de
gepubliceerde skill inmiddels afwijkt, staat dat onder "Stand in de gepubliceerde skill".

**Testmateriaal:** het IMGeo-begrippenkader (464 begrippen, 57 collecties, 6.102 triples) en het
regressiekader [IMGeo-mini](../fixtures/imgeo-mini/verwacht.md) (20 begrippen, 111 triples,
14 aangebrachte fouttypen).

**Modellen:** Claude Haiku, Claude Sonnet en Claude Opus (versies van augustus 2026). Er is in
deze sessie **geen testrun met een open-source of Europees model** gedaan; deel 1 is een
onderzoek naar de leesbaarheid van de skill in andere omgevingen.

## Deel 1 — Portabiliteit naar andere omgevingen

**Vraag:** is de skill, en in het bijzonder `allowed-tools` in de frontmatter, bruikbaar buiten de
omgeving waarin hij is gemaakt?

**Conclusie:** de body van `SKILL.md` is volledig portabel; de frontmatter gedeeltelijk, en
`allowed-tools` is het zwakste onderdeel.

- Het formaat is een open specificatie ([agentskills.io/specification](https://agentskills.io/specification))
  met zes frontmattervelden: `name`, `description`, `license`, `compatibility`, `metadata` en
  het experimentele `allowed-tools`. Begin 2026 ondersteunden ruim 30 tools het formaat, onder
  meer van OpenAI, Microsoft, Google, JetBrains, AWS, Block en Mistral AI. De installatiepaden
  verschillen per tool.
- `allowed-tools` is volgens de specificatie experimenteel. In de skill stonden drie problemen:
  een YAML-lijst in plaats van één string met spaties; toolnamen (`Bash`, `WebFetch`) die
  andere omgevingen anders noemen (`shell`, `run_shell_command`, `runInTerminal`); en een
  matchsyntax (`Bash(curl -s *)`) die alleen in één omgeving werkt. Een omgeving die het veld
  niet begrijpt, negeert het: de skill werkt dan, maar met goedkeuringsvragen.
- Microsoft Agent Framework leest `SKILL.md`, maar negeert `allowed-tools` bewust en vraagt
  goedkeuring per aanroep. Microsoft 365 Copilot leest geen `SKILL.md`; declarative agents hebben
  geen shell, alleen een Python-codeinterpreter. De SHACL-module kan daar niet draaien, de
  inhoudelijke review wel.
- Een veld `model` in de frontmatter doet niets: het is geen veld uit de specificatie.

**Aangepast:** `allowed-tools` naar de vorm uit de specificatie, een veld `compatibility`, en een
sectie "Benodigde tools en voorbeeldaanroepen" in de body. Omdat `allowed-tools` genegeerd kan
worden, staat wat de skill nodig heeft nu ook in de body.

**Vuistregel:** zet wat een andere omgeving moet weten in de body. Beschrijf tools functioneel
("shell-toegang", "een fetch-tool") en noem in de skill geen modelnamen.

## Deel 2 — De skill werkend krijgen op lichtere modellen

Wat op een modelverschil leek, bleek grotendeels gereedschap dat een verkeerde uitkomst gaf en een
werkwijze die niet schaalde.

### Defect 1: `pyshacl -e` laadt de extensie niet als shapes

De skill schreef `pyshacl -s profiel.ttl -e extensie.ttl` voor. `-e/--ont-graph` voegt het
bestand toe aan de datagraaf, niet aan de shapes-graaf: de extensie werd stilzwijgend nooit
geëvalueerd.

| Aanroep op IMGeo | Resultaat |
| --- | --- |
| Zoals gedocumenteerd (`-e`) | 0 sh:Violation, 351 sh:Warning |
| Profiel en extensie samengevoegd | 48 sh:Violation, 919 sh:Warning, 464 sh:Info |

Alle 48 violations komen uit `TopConceptWithBroaderShape`: precies de zwaarste fout die de
extensie moet vangen. **Correctie:** profiel en extensie eerst samenvoegen, plus een zelfcontrole
(de samengevoegde graaf telt meer triples dan het profiel, 679 → 746, en er moet minstens één
shape uit de extensie in de resultaten staan).

### Defect 2: lezend steekproeven schaalt niet

Na de correctie vonden alle drie de modellen dezelfde 48 / 919 / 464. Het verschil verschoof naar
de inhoudelijke review, en daar bleek de omvang van het kader doorslaggevend, niet het model:

| Inhoudelijke controle | IMGeo, 464 begrippen (Haiku / Sonnet / Opus) | IMGeo-mini, 20 begrippen |
| --- | --- | --- |
| Ontbrekende `dct:title` | – ✓ ✓ | ✓ ✓ ✓ |
| Leestekens in termen | – ✓ ✓ | ✓ ✓ ✓ |
| Engelse CamelCase met `@nl` | – ✓ ✓ | ✓ ✓ ✓ |
| Tekstcoderingsfout in definitie | – ✓ – | ✓ ✓ ✓ |

Ook het zwaarste model miste de tekstcoderingsfout op het grote kader en vond hem op het kleine.
Bij 464 begrippen gaan alle modellen steekproeven nemen; bij 20 leest elk model alles.

**Correctie:** een script `scripts/inhoudelijke-scan.py` dat elke term en elke definitie toetst,
en de instructie om vanaf ongeveer 50 begrippen eerst die scan te draaien en in het rapport te
vermelden welke controles uitputtend en welke op steekproef zijn gedaan.

### Resultaat over drie rondes (lichtste model, volledig IMGeo)

| Ronde | Violations | Publicatieadvies | Verzonnen bevindingen | Inhoudelijke controles |
| --- | --- | --- | --- | --- |
| R1 — skill met `-e`-defect | 0 | "Ja, onder voorwaarden" | 2 | 1 van 7 |
| R2 — SHACL gecorrigeerd | 48 | "Niet verantwoord" | 0 | 1 van 7 |
| R3 — scan toegevoegd | 48 | "Niet verantwoord" | 0 | 6 van 7 |

De verzonnen bevindingen in R1 ("465 begrippen"; "1 begrip zonder definitie, 1 zonder
prefLabel") verdwenen zodra het gereedschap klopte.

### Wat na beide correcties modelafhankelijk blijft

1. **Telnauwkeurigheid.** Haiku schreef viermaal "47 topbegrippen" waar het er 39 zijn, en
   driemaal "126 dubbele voorkeurstermen" waar het er 127 zijn, terwijl de juiste getallen in de
   eigen uitvoer stonden. Sonnet en Opus maakten geen telfouten.
2. **Redeneren over het gereedschap.** Alleen Sonnet en Opus zagen dat het normatieve profiel
   zelf gaten heeft.
3. **Patroonherkenning over het kader.** Opus leidde af dat 39 kapotte relaties op de verkeerde
   sleutel waren gegenereerd: 11 van 14 doel-URI's waren de `skos:prefLabel` van een bestaand
   begrip. Dat veranderde het hersteladvies.

Sonnet vond in beide rondes de tien definities met tekstcoderingsfouten die Opus tweemaal miste:
verschillende blinde vlekken, geen rangorde.

### Kosten per run

| Model | Tokens | Duur |
| --- | --- | --- |
| Haiku | 61–73k | 3–5 min |
| Sonnet | 126–184k | 8–15 min |
| Opus | 112–140k | 8–12 min |

## Deel 3 — Werkwijze

1. **Bepaal eerst zelf een ijkpunt**, zonder assistent: [`tests/ijkpunt.py`](../ijkpunt.py).
   In deze sessie zat de eerste ijkrun zelf nog in de `-e`-val; dat kwam pas uit doordat twee
   modellen het opmerkten.
2. **Per model een aparte run met een identieke prompt**, elk in een eigen werkmap.
3. **Test een gewijzigde skill via het bestandspad**, niet via de geïnstalleerde versie: laat de
   assistent expliciet `<pad>/SKILL.md` lezen.
4. **Gebruik het kleine regressiekader** om te zien of een gemiste bevinding aan het model ligt
   of aan de omvang.

## Deel 4 — Bevindingen buiten de skill

- Zes bevindingen over het SHACL-profiel 1.0.0, als issues voor Geonovum/NL-SBB geformuleerd.
  De twee zwaarste: `skosapnl:TopConceptHavingBroader` toetst alleen `skos:broader` en niet de
  ISO 25964-varianten, en de ernst `sh:Warning` op de node shape `skosapnl:Concept` overschrijft
  de `sh:Violation` van die constraint. Samen melden ze op IMGeo nul violations waar er 48 zijn.
- Een issue voor Imvertor over `Imvert2Skos-BRO.xsl`, dat superklasserelaties wegschrijft naar
  begrippen die niet worden geëxporteerd.
- `conflicts.md` is gecorrigeerd: het beweerde op drie punten dat het profiel iets niet toetst,
  terwijl de shapes wel bestaan.

## Stand in de gepubliceerde skill

Vergeleken met de gepubliceerde versie `geonovum-nl-sbb-review` (0.1.0):

- De correctie van defect 1 staat erin, in een andere vorm: profiel en extensie worden als twee aparte runs gedraaid en de bevindingen opgeteld, in plaats van samengevoegd tot één shapes-graaf. Op IMGeo-mini geeft dat dezelfde uitkomst (profiel 10 sh:Warning; extensie 3 sh:Violation, 7 sh:Warning, 20 sh:Info; samen 3 / 17 / 20), getoetst op 2026-10-23.
- **Het script `scripts/inhoudelijke-scan.py` en de instructie voor grote kaders (defect 2)
  ontbreken.** De resultaten van R3 gelden dus niet voor de gepubliceerde versie.
- `allowed-tools` is teruggebracht tot `Bash(pyshacl *)`.
- Het voorstel voor `compatibility` uit deze sessie is niet overgenomen.
