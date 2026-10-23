---
"geonovum-nl-sbb": patch
---

Correcties naar aanleiding van testrondes met verschillende assistenten. De skill meldt de SHACL-validatie als onvolledig als de extensie ontbreekt, in plaats van zonder extensie door te gaan. Aantallen komen uit de ruwe SHACL-uitvoer, met onderscheid tussen resultaten, begrippen, relaties en relatiedoelen. Een begrip dat alleen via ISO 25964-relaties in de hiërarchie hangt, wordt niet meer als verweesd gemeld: dat is een bekende beperking van het profiel. De bronnencontrole behandelt namespaces en begrip-URI's niet meer als bronnen. Collecties zonder `skos:prefLabel`, kaders zonder `dct:title` en tekstcoderingsfouten zijn waarschuwingen. `conflicts.md` beschrijft nu correct wat het profiel wel en niet toetst. De skill heeft een versienummer (`nl.gov.version`) dat in het rapport wordt vermeld.
