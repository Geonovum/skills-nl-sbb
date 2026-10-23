#!/usr/bin/env python3
"""Onafhankelijk ijkpunt voor de review-skill: SHACL-uitkomst zonder assistent.

Valideert een begrippenkader tegen het normatieve profiel plus de extensie van de
skill, op dezelfde manier als de skill voorschrijft: beide samengevoegd tot één
shapes-graaf (niet via -e), advanced=True, inference=rdfs, geen allow-warnings.
Een rapport van de skill wordt hiertegen gescoord.

Gebruik:
  python3 tests/ijkpunt.py tests/fixtures/imgeo-mini/imgeo-mini.ttl
  python3 tests/ijkpunt.py data.ttl --json > verwacht.json
  python3 tests/ijkpunt.py data.ttl --profiel skos-ap-nl.ttl   # lokaal profiel

Nodig: pip install pyshacl rdflib
"""
import argparse, json, re, sys, time, urllib.request
from collections import Counter
from pathlib import Path

from pyshacl import validate
from rdflib import Graph, Namespace, RDF

PROFIEL_URL = "https://register.geostandaarden.nl/shacl/nl-sbb/1.0.0/skos-ap-nl.ttl"
EXTENSIE = Path(__file__).resolve().parent.parent / "skills/geonovum-nl-sbb-review/skos-ap-nl-extensie.ttl"
SH = Namespace("http://www.w3.org/ns/shacl#")
ERNST = {"Violation": "fout", "Warning": "waarschuwing", "Info": "info"}


def kort(u):
    return re.split(r"[/#]", str(u).rstrip("/"))[-1]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("data")
    ap.add_argument("--profiel", help=f"lokaal profiel; standaard {PROFIEL_URL}")
    ap.add_argument("--json", action="store_true", help="volledige uitkomst als JSON")
    a = ap.parse_args()

    shapes = Graph()
    if a.profiel:
        shapes.parse(a.profiel)
    else:
        with urllib.request.urlopen(PROFIEL_URL, timeout=60) as r:
            shapes.parse(data=r.read().decode("utf-8"), format="turtle")
    n_profiel = len(shapes)
    ext = Graph().parse(EXTENSIE)
    ext_shapes = {kort(s) for s in ext.subjects(RDF.type, SH.NodeShape)} | {kort(s) for s in ext.subjects(RDF.type, SH.PropertyShape)}
    shapes += ext
    if len(shapes) <= n_profiel:
        sys.exit("De extensie is niet aan de shapes-graaf toegevoegd.")

    t0 = time.time()
    data = Graph().parse(a.data)
    _, res, _ = validate(data, shacl_graph=shapes, advanced=True, inference="rdfs",
                         abort_on_first=False, allow_warnings=False, allow_infos=False)
    duur = round(time.time() - t0, 1)

    def sleutel(r):
        shape, pad = res.value(r, SH.sourceShape), res.value(r, SH.resultPath)
        naam = kort(shape) if shape is not None else ""
        if len(naam) >= 30 and not naam[:1].isupper():  # blank node: geen stabiele naam
            naam = "(anoniem)"
        return (ERNST[str(res.value(r, SH.resultSeverity)).split("#")[-1]], naam,
                kort(pad) if pad is not None else "", str(res.value(r, SH.focusNode)))

    # Telling op de ruwe resultaten, zoals de skill voorschrijft: een regel die per paar
    # meldt (zoals identieke definities) telt dus per paar. De lijst is per focus node ontdubbeld.
    ruw = Counter(sleutel(r) for r in res.subjects(RDF.type, SH.ValidationResult))
    rijen = sorted(ruw)
    telling = Counter()
    for (e, *_), n in ruw.items():
        telling[e] += n
    uit = {
        "data": a.data,
        "profiel": a.profiel or PROFIEL_URL,
        "triplesProfiel": n_profiel,
        "triplesProfielPlusExtensie": len(shapes),
        "instellingen": {"advanced": True, "inference": "rdfs", "allow_warnings": False},
        "telling": {k: telling.get(k, 0) for k in ("fout", "waarschuwing", "info")},
        "extensieShapesGeraakt": sorted({s for _, s, _, _ in rijen if s in ext_shapes}),
        "resultaten": [{"ernst": e, "shape": s, "pad": p or None, "focus": f, "aantal": ruw[(e, s, p, f)]} for e, s, p, f in rijen],
    }
    if a.json:
        print(json.dumps(uit, ensure_ascii=False, indent=1))
        return
    t = uit["telling"]
    print(f"Profiel {n_profiel} triples + extensie {len(shapes) - n_profiel} triples · {duur} s")
    print(f"sh:Violation {t['fout']} · sh:Warning {t['waarschuwing']} · sh:Info {t['info']}")
    per_shape = Counter()
    for (e, s, _, _), n in ruw.items():
        per_shape[(e, s)] += n
    for (e, s), n in sorted(per_shape.items(),
                            key=lambda x: (list(ERNST.values()).index(x[0][0]), -x[1])):
        print(f"  {e:<13}{n:>5}  {s}{'  [extensie]' if s in ext_shapes else ''}")


if __name__ == "__main__":
    main()
