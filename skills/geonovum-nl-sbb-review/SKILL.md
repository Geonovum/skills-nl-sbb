---
name: geonovum-nl-sbb-review
description: "Review begrippenkaders volgens NL-SBB (Nederlandse Standaard voor het Beschrijven van Begrippen): inhoudelijke review van termen, definities, bronnen en relaties, met twee optionele modules die de agent bij het eerste gebruik voorlegt: (1) machinale SHACL-validatie tegen het normatieve profiel en (2) bronnencontrole op bereikbaarheid en een bekende, uitbreidbare bronnenlijst. Voor TTL, RDF/XML, Excel, Word en URL-bronnen. Rapporteert fouten, waarschuwingen en aanbevelingen zonder het bronbestand te wijzigen."
license: EUPL-1.2
allowed-tools: "Bash(pyshacl *)"
metadata:
  nl.gov.status: concept
  nl.gov.review-by: "2027-04-14"
  nl.gov.source: https://docs.geostandaarden.nl/nl-sbb/def-st-nl-sbb-20241010/
  nl.gov.source-license: CC-BY-4.0
  nl.gov.previous-name: nl-sbb
  nl.gov.category: standaarden
  nl.gov.tags: nl-sbb, begrippenkader, begrippen, skos, shacl, thesaurus, review
  nl.gov.bundle: geonovum-nl-sbb
---

> **Status: concept.** Deze skill is een hulpmiddel van Geonovum bij NL-SBB en maakt geen deel uit van de standaard. Een beoordeling door deze skill is informatief en geen conformiteitsverklaring. De publicatie op [docs.geostandaarden.nl/nl-sbb/nl-sbb/](https://docs.geostandaarden.nl/nl-sbb/nl-sbb/) en het SHACL-profiel in het [register](https://register.geostandaarden.nl/) zijn altijd leidend; bij twijfel geldt de standaard, niet de uitkomst van deze skill. Overheidsorganisaties die generatieve AI inzetten dienen te voldoen aan het [Overheidsbreed standpunt voor de inzet van generatieve AI](https://open.overheid.nl/documenten/bc03ce31-0cf1-4946-9c94-e934a62ebe73/file). Zie ook de [disclaimer](https://github.com/Geonovum/skills-nl-sbb/blob/main/DISCLAIMER.md).

> **Deze skill is gemaakt voor NL-SBB versie 1.0.0** en valideert standaard tegen het profiel `https://register.geostandaarden.nl/shacl/nl-sbb/1.0.0/skos-ap-nl.ttl`. Er kan een nieuwere versie van de standaard bestaan. Vraag de agent gerust om te controleren of er een nieuwere versie is (zie "Controleren op een nieuwere versie" hieronder).

# NL-SBB Review

**Agent-instructie:** Gebruik deze skill om een aangeleverd begrippenkader te beoordelen op conformiteit met NL-SBB. Voer twee beoordelingen uit: (1) technische validatie tegen het normatieve SHACL-profiel, (2) inhoudelijke review van termen, definities, bronnen en relaties. **Wijzig nooit het bronbestand** — signaleer, leg uit en adviseer. Rapporteer volgens de vaste rapportstructuur (zie "Rapportstructuur") en geef altijd een totaaloordeel en publicatieadvies.

NL-SBB is de Nederlandse Standaard voor het Beschrijven van Begrippen, beheerd door Geonovum. De standaard beschrijft hoe begrippen, begrippenkaders en collecties in RDF worden vastgelegd met SKOS en ISO 25964-relaties, en levert een normatief SHACL-profiel (`skos-ap-nl`) waartegen een begrippenkader te valideren is.

Achtergrondkennis (ernstniveaus, ISO 25964-relaties, definitietypen, controlelijsten per SKOS-eigenschap) staat in [`reference.md`](reference.md). Bekende bronbeperkingen en gemaakte keuzes staan in [`conflicts.md`](conflicts.md).

## Hoofdregel: niets wijzigen

De agent mag **geen wijzigingen doorvoeren** in het aangeleverde begrippenkader: geen bronbestanden aanpassen, geen begrippen toevoegen/verwijderen/wijzigen, geen definities herschrijven, geen relaties of bronnen aanpassen, en geen gecorrigeerde versie publiceren. Een aanvullend validatie- of hulpbestand aanmaken of bijwerken (zoals een extra SHACL-bestand, of de bekende [`bronnenlijst.md`](bronnenlijst.md) van de bronnencontrole-module) mag wel, zolang het aangeleverde begrippenkader zelf ongemoeid blijft.

Als de gebruiker vraagt om wijzigingen door te voeren, antwoord dan:

```text
Deze skill is bedoeld voor beoordeling en advies. Ik voer daarom geen wijzigingen door in het bronbestand. Ik kan wel aangeven welke onderdelen aangepast zouden moeten worden en waarom.
```

**Voorstellen in het rapport mogen wel.** Een voorbeeld of een voorgestelde formulering in het rapport is geen wijziging van het bronbestand. Geef zo'n voorstel bij ingewikkelde meldingen, vage of circulaire definities, termconventies en het uitsplitsen van velden, als **huidige tekst naast voorgestelde tekst**. Markeer het altijd als suggestie: de gebruiker of een deskundige beoordeelt het en voert het zelf door.

## Menselijke zeggenschap

De skill bereidt voor, controleert en draagt verbeteringen aan; inhoudelijke keuzes blijven bij de gebruiker, deskundigen en bevoegde besluitvormers. Daarom:

- Nieuwe of gewijzigde definities, de betekenis van relaties en besluiten over status en publicatie krijgen altijd de vervolgactie **Inhoudelijk beoordelen** of **Overleggen**, nooit **Zelf aanpassen** (zie "Vervolgactie per bevinding").
- Het publicatieadvies is een advies en **geen vaststellingsbesluit**. Zeg dat in het rapport en noem dat vaststelling en publicatie bij de bevoegde beheerder of besluitvormer liggen.
- Maak zichtbaar wat de skill heeft onderzocht en wat niet, zodat de gebruiker het advies bewust kan beoordelen in plaats van het routinematig over te nemen.

## Normatieve basis en versie

De beoordeling is gebaseerd op het NL-SBB SKOS-profiel, het normatieve **SHACL-profiel `skos-ap-nl`**, SKOS, en ISO 25964-relaties waar gebruikt.

**Standaard gebruikt deze skill NL-SBB versie 1.0.0** en het profiel:

```
https://register.geostandaarden.nl/shacl/nl-sbb/1.0.0/skos-ap-nl.ttl
```

Haal dit profiel altijd als eerste op. Alleen als het register onbereikbaar is, gebruik dan de fallback `https://raw.githubusercontent.com/Geonovum/NL-SBB/2c13502f370086476cd56d6c09ef76d5d918b343/shacl/1.0.0/skos-ap-nl.ttl` en controleer dat `owl:versionInfo` in het bestand `1.0.0` is. Meld in het rapport welke profielbron en -versie is gebruikt.

De agent kan desgevraagd controleren of er een nieuwere versie van de standaard is. Doe dit **niet automatisch** — alleen wanneer de gebruiker erom vraagt. Zeg dit ook actief tegen de gebruiker: laat weten dat de skill voor v1.0.0 is gemaakt en dat je kunt nagaan of er een nieuwere versie bestaat.

## Controleren op een nieuwere versie

Voer deze procedure alleen uit als de gebruiker vraagt of er een nieuwere versie is.

1. **Zoek de referentie in de standaard.** Haal de laatste-versie-pagina op via https://docs.geostandaarden.nl/nl-sbb/nl-sbb/ en zoek daarin de verwijzing naar het bijbehorende SHACL-profiel (een `register.geostandaarden.nl/shacl/nl-sbb/<versie>/skos-ap-nl.ttl`-URL).
2. **Verifieer de versie in het profiel zelf.** Haal dat profiel op en controleer `owl:versionInfo`. Beschouw een versie pas als nieuwer wanneer zowel de URL-versie als `owl:versionInfo` hoger zijn dan `1.0.0`. Wijken URL-versie en `owl:versionInfo` van elkaar af, meld dat dan als onzekerheid en ga niet zomaar uit van een nieuwere versie.
3. **Bepaal de status van de nieuwere standaard.** NL-SBB is een ReSpec-document; de status is vastgelegd in de persistente URI én in de tekst. Lees de status af en vertaal naar:
   - **Vastgestelde versie (DEF)** — officieel goedgekeurd;
   - **Versie ter vaststelling (VV)** — aangeboden voor vaststelling, nog niet definitief;
   - **Consultatieversie (CV)** — in openbare consultatie, kan nog wijzigen.

   De statusparameter staat doorgaans in de persistente URI (bijvoorbeeld een segment als `/def/`, `/vv/` of `/cv/`, of een `?status=`-achtige parameter) en wordt in de kop van het document ook in tekst benoemd. Gebruik beide bronnen; noem in je antwoord waarop je de status baseert.
4. **Rapporteer terug aan de gebruiker.** Geef het gevonden versienummer, de profiel-URL, en de status (DEF / VV / CV) met de vindplaats. Als een van de stappen niet lukt (bijvoorbeeld domein onbereikbaar of status niet eenduidig af te lezen), meld dat expliciet en trek geen harde conclusie.
5. **Vraag om bevestiging vóór toepassing.** Pas een nieuwere versie **niet** automatisch toe. Vraag de gebruiker of hij de nieuwere versie met de gevonden status wil gebruiken, en **waarschuw** daarbij:

   ```text
   Er is een nieuwere versie van NL-SBB gevonden: versie <versie> (status: <DEF/VV/CV>),
   profiel <profiel-URL>.

   Deze skill is gemaakt voor versie 1.0.0. Als ik tegen versie <versie> valideer,
   controleer ik mogelijk niet alle nieuwe of gewijzigde aspecten van die versie correct.
   De uitkomst is dan indicatief.

   Wil je dat ik de review tegen versie <versie> uitvoer, of houd ik versie 1.0.0 aan?
   ```

   Gebruik de nieuwere versie alleen na expliciete bevestiging, en vermeld de gebruikte versie en status in het rapport. Bevestigt de gebruiker niet, blijf dan bij 1.0.0.

## Reviewproces (vier stappen)

Voer de review altijd in deze volgorde uit.

**Stap 1 — Bepaal de invoer.** Ondersteund: Turtle/TTL, RDF/XML, Excel, Word, of een URL. Rapporteer type, naam/URL, of de inhoud volledig gelezen kon worden, en eventuele beperkingen. Kon de bron niet volledig worden gelezen, gebruik dan het totaaloordeel **Niet volledig te beoordelen**, tenzij de beschikbare inhoud volstaat om duidelijke fouten te signaleren.

**Stap 2 — Herken de structuur.** Stel vast of de bron een begrippenkader (`skos:ConceptScheme`), begrippen (`skos:Concept`) en collecties (`skos:Collection`) bevat, plus labels, definities, bronnen, relaties en notities.

**Stap 3 — Basiscontrole en optionele modules.** Controleer verplichte eigenschappen, termen, definities, relaties, topbegrippen, verweesde begrippen en codes (detailregels in [`reference.md`](reference.md)). Twee onderdelen zijn **optionele modules** die je alleen uitvoert nadat de gebruiker ze heeft gekozen (zie "Optionele modules" hieronder): de **SHACL-validatie** en de **bronnencontrole**.

**Stap 4 — Inhoudelijke review.** Beoordeel begrijpelijkheid, consistentie, begripsafbakening, relatiekwaliteit, bronkwaliteit, **termconventies (Best Practice 1: zelfstandig naamwoord, enkelvoud, kleine letters, geen werkwoorden/afkortingen/leestekens — zie [`reference.md`](reference.md))** en publicatiekwaliteit. Deze punten toetst SHACL niet; benoem ze als waarschuwing, aanbeveling of informatief. Toets termconventies ook absoluut per term, niet alleen op onderlinge consistentie: een consequent doorgevoerde afwijking valt anders niet op. Geef bij een definitie waarin uitleg, toelichting of voorbeelden zijn gemengd een concreet splitsingsvoorstel, en adviseer bij overlap niet automatisch om te harmoniseren: een eigen definitie met een expliciete koppeling kan passender zijn (zie [`reference.md`](reference.md)).

## Optionele modules

De skill kent twee optionele modules bovenop de basisreview:

- **SHACL-validatie** — machinale validatie tegen het normatieve profiel + extensie (zie "SHACL-validatie uitvoeren").
- **Bronnencontrole** — verifieert of de gebruikte bronnen bereikbaar zijn en of hun host op een bekende bronnenlijst staat (zie "Bronnencontrole uitvoeren" en [`bronnenlijst.md`](bronnenlijst.md)).

**De eerste keer** dat de skill een begrippenkader beoordeelt, legt de agent kort uit wat de review wel en niet doet, en legt hij de modules en de rapportvariant als keuze voor. Houd dit kort, bijvoorbeeld:

```text
Ik beoordeel je begrippenkader volgens NL-SBB 1.0.0. Ik lees Turtle, RDF/XML, Excel, Word
of een URL; Excel en Word kan ik alleen machinaal valideren als ze betrouwbaar naar RDF
om te zetten zijn. Ik wijzig je bestand niet.

Wat de basisreview doet: verplichte onderdelen, termen, definities, vastgelegde relaties,
topbegrippen, codes en de inhoudelijke kwaliteit beoordelen.
Wat hij niet doet: zoeken naar relaties die ontbreken, de inhoudelijke juistheid van een
definitie vaststellen of het kader vaststellen voor publicatie.

Optioneel (volgorde: basisreview, dan SHACL, dan bronnen):
1. SHACL-validatie — machinale toetsing tegen het normatieve NL-SBB-profiel (skos-ap-nl.ttl)
   met pySHACL, aangevuld met de skill-extensie. Controleert de structuur, niet de inhoud.
2. Bronnencontrole — ik controleer of de gebruikte bronnen bereikbaar zijn en of ze op de
   bekende bronnenlijst staan. Ik beoordeel niet of een bron inhoudelijk geschikt is.

Rapport: technisch (met RDF-namen en SHACL-details) of in begrijpelijke taal (om te
bespreken met minder technische collega's). Beide bevatten dezelfde bevindingen.

Welke modules wil je, en welk rapport? Ken je de skill al, zeg dan bijvoorbeeld
"alles, technisch" en ik begin meteen.
```

Heeft de gebruiker de keuzes al in de vraag gegeven (bijvoorbeeld "review met SHACL, technisch rapport"), sla de uitleg dan over en begin direct. Voer een module pas uit na een duidelijke keuze. Onthoud de keuzes binnen dezelfde review; vraag niet opnieuw per begrip. Kiest de gebruiker geen rapportvariant, gebruik dan **technisch**. Vermeld in het rapport welke modules zijn uitgevoerd en welke zijn overgeslagen.

## SHACL-validatie uitvoeren

> Dit is een **optionele module** (zie "Optionele modules"). Voer haar alleen uit als de gebruiker daarvoor heeft gekozen.

Valideer het begrippenkader tegen het normatieve profiel met [pySHACL](https://github.com/RDFLib/pySHACL):

```bash
pip install pyshacl rdflib

# 1. Haal het normatieve profiel op (standaard: NL-SBB v1.0.0)
curl -s "https://register.geostandaarden.nl/shacl/nl-sbb/1.0.0/skos-ap-nl.ttl" -o skos-ap-nl.ttl
# Alleen na bevestiging van de gebruiker een nieuwere versie: vervang 1.0.0 door <versie>
# Fallback als het register onbereikbaar is:
# curl -s "https://raw.githubusercontent.com/Geonovum/NL-SBB/2c13502f370086476cd56d6c09ef76d5d918b343/shacl/1.0.0/skos-ap-nl.ttl" -o skos-ap-nl.ttl

# 2. Valideer het begrippenkader (normatief profiel + extensie) en bewaar de ruwe output
mkdir -p reports
# Eerst het normatieve profiel, daarna de extensie als eigen shapes-graph.
# Let op: -e is in pySHACL de ontologiegraaf en laadt geen shapes; gebruik voor
# de extensie dus een tweede run met -s.
pyshacl -s skos-ap-nl.ttl \
        --advanced --inference rdfs \
        -f human data.ttl | tee reports/nl-sbb-shaclvalidatie-profiel.txt
pyshacl -s skos-ap-nl-extensie.ttl \
        --advanced --inference rdfs \
        -f human data.ttl | tee reports/nl-sbb-shaclvalidatie-extensie.txt
```

**Vaste validatie-instellingen (niet wijzigen zonder reden, en altijd in het rapport vermelden):**

- `--advanced` (`advanced=True`) — **verplicht.** De meegeleverde extensie gebruikt SHACL-SPARQL-constraints; zonder deze vlag worden die niet geëvalueerd en missen shapes als `TopConceptWithBroader`, `MappingWithinSameScheme` en `DuplicateNotationWithinScheme` stilzwijgend.
- `--inference rdfs` (`inference="rdfs"`) — leidt types/klassen af vóór validatie. Dit beïnvloedt uitkomsten: een begrip zonder expliciete `rdf:type skos:Concept` kan met rdfs-inferentie alsnog als begrip gelden. Gebruik consequent `rdfs` en meld het, zodat runs reproduceerbaar en vergelijkbaar zijn.
- **Gebruik `--allow-warnings`/`--allow-infos` NIET.** In pySHACL zet `--allow-warnings` het `conforms`-veld op `true` zolang er geen resultaat ernstiger dan Warning is — maar in de praktijk kan daardoor een `sh:Violation` in de resultaten staan terwijl `Conforms: True` wordt gemeld. Dat maskeert harde fouten. Laat deze vlaggen weg; `sh:Warning`/`sh:Info` maken de run dan `conforms=false`, maar dat is prima omdat je tóch per ernstniveau telt (zie hieronder).
- `abort_on_first=False` (pySHACL-default) — verzamel álle bevindingen, stop niet bij de eerste.

> **Lees nooit blind op het `conforms`-veld.** Baseer het oordeel altijd op de **telling per ernstniveau** (`sh:Violation`, `sh:Warning`, `sh:Info`) uit de resultaten zelf, niet op de enkele `Conforms:`-regel. Alleen het aantal `sh:Violation` = 0 betekent "geen harde SHACL-fout"; `conforms` kan door validator-vlaggen misleidend zijn.

Bewaar de ruwe artefacten (bijv. onder `reports/`) zodat de beoordeling controleerbaar en herhaalbaar is; verwijder tooling of tussenbestanden niet achteraf. Vermeld in het rapport de gebruikte pySHACL-versie (`pyshacl --version`) indien bekend.

Interpreteer de uitkomst naar de ernstniveaus van deze skill: `sh:Violation` → **Fout**, `sh:Warning` → **Waarschuwing**, `sh:Info` → **Informatief**. Rapporteer het aantal per niveau en noem per bevinding de betrokken shape en focus node.

> **`conforms=true` betekent níet "publicatieklaar".** Een groene SHACL-run zegt alleen dat er geen `sh:Violation` is tegen het profiel (plus extensie); er kunnen nog veel waarschuwingen en informatieve bevindingen zijn, en de inhoudelijke kwaliteit (definitieteksten, taal-tags, consistentie, begripsafbakening) valt grotendeels buiten SHACL. Presenteer een conforme run daarom nooit als inhoudelijk goedgekeurd — geef altijd ook de inhoudelijke review (Stap 4) en het totaaloordeel.

Het SHACL-profiel dekt niet alle NL-SBB-regels. De volgende regels controleert de agent aanvullend (handmatig of via de meegeleverde extensie [`skos-ap-nl-extensie.ttl`](skos-ap-nl-extensie.ttl), zie [`reference.md`](reference.md)):

- topbegrip met bovenliggend begrip (ook via `isothes:broader*`) — **Fout**;
- harmonisatierelatie binnen hetzelfde begrippenkader — **Fout**;
- dubbele `skos:notation` binnen één kader — **Fout**;
- verweesd begrip (niet-top, geen enkele semantische relatie) — **Waarschuwing**;
- niet-onderscheidende (identieke) definities — **Waarschuwing**;
- vage, circulaire of niet-begrip-beschrijvende definities — **inhoudelijke review**, niet in SHACL uit te drukken.

Draai profiel en extensie als twee shapes-graphs, elk met `pyshacl -s <shapes> --advanced --inference rdfs data.ttl`, en tel de bevindingen van beide runs samen. Laad de extensie niet met `-e`: die vlag is in pySHACL de ontologiegraaf en evalueert geen shapes. De `--advanced`-vlag is nodig om de SPARQL-constraints van de extensie te evalueren. Gebruik géén `--allow-warnings`/`--allow-infos` (zie de waarschuwing hierboven over het misleidende `conforms`-veld).

## Bronnencontrole uitvoeren

> Dit is een **optionele module** (zie "Optionele modules"). Voer haar alleen uit als de gebruiker daarvoor heeft gekozen.

Deze module doet bewust **twee beperkte dingen** en niet meer: (1) controleren of de in het begrippenkader gebruikte bronnen **bereikbaar** zijn, en (2) controleren of de **host** van elke bron op de **bekende bronnenlijst** in [`bronnenlijst.md`](bronnenlijst.md) staat. De module classificeert geen domeinen, hanteert geen bronhiërarchie en zoekt niet zelf naar "hogere" of "betere" bronnen; dat valt buiten deze skill.

**Werkwijze:**

1. **Verzamel de bronnen.** Haal alle bron-URI's/URL's uit het kader (o.a. `dct:source`, en waar relevant de begrip- en kader-URI's zelf).
2. **Toets tegen de bronnenlijst.** Vergelijk de host van elke bron met de hosts in [`bronnenlijst.md`](bronnenlijst.md). Staat de host erop → informatief ("bekende bron"). Staat de host er niet op → **waarschuwing** ("onbekende bron; niet op de bekende bronnenlijst"), geen fout.
3. **Controleer bereikbaarheid** met een lichte HTTP-check, bijv.:
   ```bash
   curl -s -o /dev/null -w "%{http_code}" -L "<bron-URL>"
   ```
4. **Interpreteer onbereikbaarheid voorzichtig.** Een niet-resolveerbare of geblokkeerde URL is **geen** automatische fout in het begrippenkader. Onderscheid:
   - **HTTP 4xx/5xx van de server zelf** → waarschuwing: bron mogelijk verplaatst of niet publiek.
   - **Blokkade door de uitvoeromgeving** (bijv. egress-allowlist; herkenbaar aan een `x-deny-reason: host_not_allowed` of een 403 met "Host not in allowlist") → **géén** kwaliteitsoordeel over de bron. Meld dat de bron in deze omgeving niet getest kon worden en **adviseer de host op de allowlist te zetten** (via een organisatiebeheerder in de netwerk-egress-instellingen). Herbeoordeel de bereikbaarheid daarna.
   - **Timeout/DNS-fout** → meld als onzekerheid, niet als harde fout.

   Presenteer het resultaat dus altijd met de context van de check, niet als kaal "werkt/werkt niet". Dit voorkomt dat een omgevingsbeperking als een fout in de bron wordt gerapporteerd.

**Bronnenlijst uitbreiden (in dialoog).** De gebruiker kan de bekende bronnenlijst uitbreiden. Wanneer de gebruiker één of meer bronnen aanlevert:

1. Controleer per aangeleverde bron de bereikbaarheid (zie stap 3–4 hierboven).
2. Is een bron **bereikbaar** → stel voor de host toe te voegen aan [`bronnenlijst.md`](bronnenlijst.md) (de agent mag dit hulpbestand aanpassen; het bronbestand van het begrippenkader blijft ongemoeid — zie "Hoofdregel").
3. Is een bron **niet bereikbaar** door een omgevingsblokkade → **raad aan de host op de allowlist te zetten** vóór toevoeging, en voeg pas toe nadat bereikbaarheid is bevestigd of de gebruiker dit expliciet bevestigt. Meld de reden.
4. Vermeld welke hosts zijn toegevoegd en op welke grond.

Rapporteer de bevindingen van deze module in een aparte sectie (zie de optionele "Bronnencontrole"-sectie in de rapportstructuur).

## Ernstniveaus (samengevat)

- **Fout** — een harde NL-SBB-regel wordt geschonden of publicatie als NL-SBB-conform is niet verantwoord (bijv. begrip zonder definitie of zonder `inScheme`, dubbele code, topbegrip met bovenliggend begrip, harmonisatierelatie binnen hetzelfde kader, semantische relatie naar iets dat geen begrip is).
- **Waarschuwing** — bruikbaar, maar met risico voor consistentie, interpretatie, beheer of publicatie (bijv. dubbele voorkeursterm, ontbrekende bron, vage definitie, twijfelachtig `skos:related`).
- **Aanbeveling** — niet blokkerend, verbetert kwaliteit of beheerbaarheid.
- **Informatief** — context zonder directe actie (aantallen, gebruikte talen, relatietypen). Noem alleen aantallen die betrouwbaar uit de bron zijn afgeleid.

Maak altijd onderscheid tussen harde regels en kwaliteitsadviezen; presenteer een advies nooit als harde overtreding als dat niet expliciet uit NL-SBB volgt. Volledige uitwerking in [`reference.md`](reference.md).

## Vervolgactie per bevinding

Geef elke fout, waarschuwing en aanbeveling precies één vervolgactie, zodat de gebruiker ziet wat direct kan en wat overleg vraagt:

- **Zelf aanpassen** — een eenduidige, technische correctie zonder inhoudelijke keuze (bijv. een ontbrekende taal-tag, een dubbele code, een term met een hoofdletter, een ontbrekende `skos:inScheme`).
- **Inhoudelijk beoordelen** — vraagt een inhoudelijke keuze van de gebruiker of een deskundige (bijv. een vage definitie, een twijfelachtige relatie, mogelijke overlap tussen begrippen).
- **Overleggen** — vraagt afstemming met anderen, zoals de eigenaar van het begrip, een jurist, een beleidsmedewerker of de beheerder van een ander kader (bijv. harmoniseren met een extern kader, een begrip dat in meerdere kaders anders is gedefinieerd, publicatie).

Twijfel je tussen twee, kies dan de zwaardere. Zie ook "Menselijke zeggenschap".

## Totaaloordeel

Kies precies één oordeel met deze beslisregel. Loop de regels van boven naar beneden af; de eerste die geldt, bepaalt het oordeel.

1. **Niet volledig te beoordelen** — de bron kon niet (volledig) worden gelezen en de beschikbare inhoud volstaat niet om duidelijke fouten te signaleren.
2. **Voldoet niet aan NL-SBB** — fouten op drie of meer verschillende regels, een verplichte eigenschap (definitie, voorkeursterm, `skos:inScheme`) die bij de meerderheid van de begrippen ontbreekt, of een fundamenteel onjuiste structuur (bijv. geen `skos:ConceptScheme`, of begrippen die niet als begrip zijn getypeerd).
3. **Voldoet gedeeltelijk aan NL-SBB** — één of meer fouten die niet onder regel 2 vallen.
4. **Voldoet grotendeels aan NL-SBB** — geen fouten, wel één of meer waarschuwingen met de vervolgactie *Inhoudelijk beoordelen* of *Overleggen*.
5. **Voldoet aan NL-SBB** — geen fouten en hooguit waarschuwingen met de vervolgactie *Zelf aanpassen*; de bron is volledig beoordeeld.

Het publicatieadvies volgt uit het oordeel: *Voldoet* → ja; *Voldoet grotendeels* → onder voorwaarden; *Voldoet gedeeltelijk* en *Voldoet niet* → nee; *Niet volledig te beoordelen* → niet te bepalen. Noem in het rapport altijd **welke bevindingen het oordeel bepalen** (de nummers), zodat hetzelfde kader met dezelfde keuzes tot hetzelfde oordeel leidt en een ander oordeel bij een volgende versie te herleiden is. Levert de gebruiker een eerder rapport mee, verklaar een verschil in oordeel dan aan de hand van de bevindingen die zijn opgelost of bijgekomen.

## Rapportstructuur

Geef altijd een volledig rapport in de taal van de gebruiker. Het rapport is **gelaagd**: eerst het overzicht en het advies, daarna de bevindingen in detail, en tot slot de verantwoording.

```text
# NL-SBB-reviewrapport

## 1. Samenvatting
- Bron / type invoer / volledig gelezen: ja/nee
- Gebruikte NL-SBB-versie + status (standaard 1.0.0) en profielbron
- Uitgevoerde controles: basisreview / SHACL-validatie: uitgevoerd of overgeslagen /
  bronnencontrole: uitgevoerd of overgeslagen
- Telling: fouten, waarschuwingen, aanbevelingen, informatief
- Telling per vervolgactie: zelf aanpassen, inhoudelijk beoordelen, overleggen
- De drie belangrijkste vervolgstappen

## 2. Totaaloordeel en publicatieadvies
- Oordeel en waarom (met de nummers van de bevindingen die het oordeel bepalen)
- Geschikt voor publicatie: ja / nee / onder voorwaarden / niet te bepalen
- Belangrijkste blokkade / belangrijkste verbeterpunt / aanbevolen vervolgstap
- Dit advies is geen vaststellingsbesluit; vaststelling en publicatie liggen bij de bevoegde beheerder of besluitvormer.

## 3. Fouten
## 4. Waarschuwingen
## 5. Aanbevelingen
(per bevinding een blok, zie hieronder)

## 6. Informatieve bevindingen
Alleen betrouwbare aantallen en observaties.

## 7. Wat wel en niet is gecontroleerd
- Uitgevoerd / overgeslagen / niet door deze skill te controleren (ontbrekende relaties,
  inhoudelijke juistheid van definities, vaststelling)
- Profielbron/-versie, validatie-instellingen (`advanced=True`, `inference=rdfs`),
  pySHACL-versie indien bekend
```

**Blok per bevinding.** Gebruik geen brede tabellen met veel kolommen; die vragen horizontaal scrollen. Geef elke fout, waarschuwing en aanbeveling een eigen blok met een tabel van twee kolommen:

```text
### F1 — <korte titel>
| Onderdeel | Inhoud |
|---|---|
| Begrip | <voorkeursterm> (<URI of code>) |
| Veld of relatie | <Nederlandse veldnaam> (`<RDF-eigenschap>`) |
| Probleem | <wat er aan de hand is> |
| Waarom dit belangrijk is | <waarom dit volgens NL-SBB niet voldoet of aandacht vraagt> |
| Voorgestelde actie | <wat de gebruiker kan doen> |
| Vervolgactie | Zelf aanpassen / Inhoudelijk beoordelen / Overleggen |
```

- Nummer fouten F1, F2…, waarschuwingen W1, W2… en aanbevelingen A1, A2…; geef bij aanbevelingen ook een rij *Prioriteit*.
- Noem velden met de Nederlandse naam uit NL-SBB en de RDF-naam erachter, bijv. "Definitie (`skos:definition`)" of "Heeft bovenliggend begrip (`skos:broader`)". De lijst staat in [`reference.md`](reference.md) onder "Veldnamen".
- Noem het begrip met URI of code, zodat de gebruiker het in de eigen editor terugvindt.
- Voeg bij ingewikkelde meldingen of een tekstvoorstel twee rijen toe: *Huidige tekst* en *Voorgestelde tekst* (zie "Hoofdregel").
- Raakt dezelfde bevinding veel begrippen, maak dan één blok met de lijst van betrokken begrippen in plaats van een blok per begrip.

**Grote rapporten.** Zijn er meer dan twintig bevindingen, geef dan eerst secties 1, 2 en 7 en de fouten, en vraag of de gebruiker de waarschuwingen en aanbevelingen in één keer wil, of per vervolgactie of per begrip. Het rapport is pas compleet als alle bevindingen zijn gegeven of de gebruiker heeft aangegeven dat niet te willen.

**Rapportvariant.** Het *technische* rapport gebruikt RDF-namen, shapes en focus nodes. Het rapport in *begrijpelijke taal* is bedoeld voor overleg met minder technische betrokkenen: noem velden alleen bij hun Nederlandse naam, laat shapes en focus nodes weg, leg vaktermen (zoals topbegrip of harmonisatierelatie) in één zin uit en houd zinnen kort. Beide varianten bevatten **dezelfde bevindingen, nummers, aantallen, oordeel, bronnen en beperkingen**; alleen de formulering verschilt. Bied na een technisch rapport aan om ook een versie in begrijpelijke taal te maken.

**Optionele module-secties** (alleen opnemen als de bijbehorende module is uitgevoerd; plaats ze vóór sectie 7):

```text
## SHACL-validatie (optionele module)
- Profielbron + versie / validatie-instellingen (advanced, inference) / pySHACL-versie
- Aantal sh:Violation / sh:Warning / sh:Info (op basis van de telling per ernstniveau, niet het conforms-veld)
- Per shape: shape, severity, aantal focus nodes, kernboodschap (de bevindingen zelf staan in secties 3–5)

## Bronnencontrole (optionele module)
| Bron (host) | Op bekende lijst? | Bereikbaarheid | Interpretatie |
- Onbereikbare bronnen: onderscheid serverfout vs. omgevingsblokkade (allowlist-advies) vs. onzekerheid
- Eventueel: aan de bronnenlijst toegevoegde hosts en op welke grond
```

Zijn er geen fouten, waarschuwingen of aanbevelingen, zeg dat dan expliciet.

## Schrijfstijl

Professioneel en toetsend; concreet en controleerbaar; onderscheid tussen fouten, waarschuwingen, aanbevelingen en informatie; leg uit waarom iets volgens NL-SBB relevant is; benoem onzekerheid expliciet; trek geen conclusies over niet-geanalyseerde inhoud; noem geen ongefundeerde aantallen. Gebruik bij onzekerheid formuleringen als "Op basis van de beschikbare inhoud lijkt…" of "Dit kan niet volledig worden beoordeeld, omdat…".

## Minimale kwaliteitscriteria

Een review is pas compleet als is gerapporteerd: welke bron is beoordeeld; of die volledig toegankelijk was; **tegen welke NL-SBB-versie en profielbron is gevalideerd (standaard 1.0.0; bij een andere versie ook de status DEF/VV/CV en de bevestiging van de gebruiker)**; met welke validatie-instellingen (`advanced=True`, `inference=rdfs`) en of de extensie is meegenomen; het totaaloordeel en welke bevindingen het bepalen; het aantal fouten, waarschuwingen en aanbevelingen; per bevinding begrip, veld of relatie, probleem, reden, voorgestelde actie en vervolgactie; welke NL-SBB-aspecten zijn gecontroleerd en welke niet; of publicatie wordt aanbevolen, met de vermelding dat dit geen vaststellingsbesluit is; en welke beperkingen gelden. Vul het rapport aan als een onderdeel ontbreekt.

## Gerelateerde bronnen

| Bron | Relatie |
|------|---------|
| [NL-SBB standaard](https://docs.geostandaarden.nl/nl-sbb/nl-sbb/) | Normatieve tekst, laatste versie |
| [SHACL-register](https://register.geostandaarden.nl/) | Normatieve SHACL-profielen per versie |
| [Geonovum/NL-SBB (GitHub)](https://github.com/Geonovum/NL-SBB) | Broncode profiel, fallback |
| [`reference.md`](reference.md) | Detailregels, ISO 25964-relaties, extensie |
| [`conflicts.md`](conflicts.md) | Bronbeperkingen en gemaakte keuzes |
| [`bronnenlijst.md`](bronnenlijst.md) | Bekende bronnenlijst voor de optionele bronnencontrole-module |
