#!/usr/bin/env python3
"""Controleert het kopwoord en de niveaunaam van materiaal onder source/.

Twee regels uit `conventies/begrippen.md`, allebei op 8 september 2026
vastgesteld en in één keer doorgevoerd:

1. Een genummerde taak in een kop heet `Opdracht`, niet `Opgave`. *Opgave* is het
   artefact - een bestand onder `problems/` en de rubriek die ernaar verwijst -
   en die twee blijven dus toegestaan: `# Opgaven` en een ongenummerde
   `### Opgave` vallen buiten deze controle.
2. De niveaus heten `opstap`, `basis` en `extra`. Een bestandsnaam met `instap`
   erin is de vierde naam die er niet hoort te zijn.

Zonder deze controle komt `Opgave 1` terug zodra iemand een oude opgave
kopieert, en is de enige borging een meting achteraf die niemand start.

**Wat deze hook wel en niet ziet.** Hij leest koppen, en alleen koppen: een regel
die met `#` begint, buiten een codefence. Een `Opgave`-regel *binnen* een
` ```-blok ` is materiaal en geen kop, en gaat er dus doorheen. In notebooks
leest hij de markdown-cellen, samengevoegd uit de regels waarin de JSON ze
opslaat - een kop die daar per teken is opgeslagen ziet hij net zo goed als een
kop op één regel. Wat hij níet ziet is prozatekst en de nummering zelf; dat blijft
werk voor de beoordeling.

De vier oefententamens zijn uitgezonderd. Die uitsluiting staat in
`conventies/conventies.md` met de grond erbij, en is in
`.pre-commit-config.yaml` een padfilter.
"""

import json
import re
import sys

# Een genummerde werkeenheidkop. De dubbele punt staat er los in, want
# `lectures/9b_recursief.ipynb` schreef zowel `## Opgave: 1` als `## Opgave 2:`.
GENUMMERD = re.compile(r"^#{1,6}\s+Opgave\s*:?\s+\d+\b")
FENCE = re.compile(r"^(`{3,}|~{3,})")
INSTAP = re.compile(r"(^|[/_])instap([_.]|$)", re.IGNORECASE)


def markdownteksten(pad: str):
    """Geeft de markdown van een bestand, per blok, met een aanduiding erbij."""
    if pad.endswith(".ipynb"):
        with open(pad, encoding="utf-8") as f:
            notebook = json.load(f)
        for nummer, cel in enumerate(notebook.get("cells", [])):
            if cel.get("cell_type") == "markdown":
                bron = cel.get("source", "")
                tekst = "".join(bron) if isinstance(bron, list) else bron
                yield f"cel {nummer}", tekst
    else:
        with open(pad, encoding="utf-8") as f:
            yield None, f.read()


def koppen(tekst: str):
    """Geeft de kopregels buiten codefences."""
    fence = None
    for regel in tekst.split("\n"):
        gestript = regel.strip()
        opening = FENCE.match(gestript)
        if opening:
            teken = opening.group(1)[0]
            if fence is None:
                fence = teken
            elif fence == teken:
                fence = None
            continue
        if fence is None and regel.lstrip().startswith("#"):
            yield regel.strip()


def controleer(pad: str) -> list[str]:
    problemen = []
    naam = pad.replace("\\", "/").split("/")[-1]
    if INSTAP.search(naam):
        problemen.append(
            f"De bestandsnaam draagt `instap`: {naam}\n"
            f"      De niveaus heten opstap, basis en extra; zie "
            f"conventies/begrippen.md."
        )
    for waar, tekst in markdownteksten(pad):
        for kop in koppen(tekst):
            if GENUMMERD.match(kop):
                plek = f" ({waar})" if waar else ""
                problemen.append(
                    f"Genummerde `Opgave`-kop{plek}: {kop[:60]}\n"
                    f"      Een genummerde taak heet `Opdracht`; zie "
                    f"conventies/begrippen.md."
                )
    return problemen


def main(paden: list[str]) -> int:
    fout = False
    for pad in paden:
        if not pad.endswith((".md", ".ipynb")):
            continue
        try:
            problemen = controleer(pad)
        except json.JSONDecodeError as e:
            print(f"KOPWOORD {pad}: geen geldig notebook ({e})")
            fout = True
            continue
        if problemen:
            fout = True
            naam = pad.replace("\\", "/").split("/")[-1]
            print(f"KOPWOORD {naam}: {len(problemen)} probleem/problemen gevonden:")
            for p in problemen:
                print(f"    - {p}")
            print("    Corrigeer deze problemen voordat je verder gaat.")
    return 1 if fout else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
