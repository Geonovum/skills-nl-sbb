# geonovum-nl-sbb

## 1.0.0

### Major Changes

- adb157c: Rapport en begeleiding van `geonovum-nl-sbb-review` aangepast op basis van het gebruikersonderzoek naar de AI-assistent voor begrippenkaders (enquête en vijf gebruikerstesten, november 2026). Het rapport is gelaagd: eerst samenvatting, oordeel en publicatieadvies, daarna per bevinding een blok met begrip, veld of relatie (met Nederlandse veldnaam), probleem, reden, voorgestelde actie en een vervolgactie (zelf aanpassen, inhoudelijk beoordelen of overleggen). Het totaaloordeel volgt een vaste beslisregel en noemt de bevindingen die het bepalen. De skill legt bij de start uit wat wel en niet wordt gecontroleerd, biedt een rapport in begrijpelijke taal naast het technische rapport, mag in het rapport tekstvoorstellen geven (huidige naast voorgestelde tekst), geeft een splitsingsvoorstel voor gemengde beschrijvingen en adviseert bij overlap niet automatisch om te harmoniseren. Het publicatieadvies vermeldt dat het geen vaststellingsbesluit is.

## 0.1.0

### Minor Changes

- 3d5ed58: Eerste release. Skill `geonovum-nl-sbb-review` (eerder `nl-sbb`): review van begrippenkaders volgens NL-SBB 1.0.0, met optionele SHACL-validatie en bronnencontrole, status `concept`.
