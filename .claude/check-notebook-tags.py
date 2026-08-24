#!/usr/bin/env python3
"""Controleert de celtags van notebooks onder source/.

De regel is: uitwerkingen draaien, opgaven niet.

Een codecel die `skip-execution` draagt, draait niet bij de build en bereikt de
lezer leeg. Dat is wat een opgave nodig heeft: er valt dan nog iets uit te
voeren. Een uitwerking heeft juist het omgekeerde nodig, want een cel die draait
wordt bij elke build gecontroleerd.

Het venijn zit erin dat celmetadata onzichtbaar is in de gerenderde pagina. Een
vergeten tag levert iets op dat er goed uitziet en toch fout is. Deze controle
maakt dat zichtbaar op het moment dat je het bestand aanraakt.

Zie conventies/technische-conventies.md.
"""

import json
import re
import sys

SKIP = "skip-execution"
RAISES = "raises-exception"

# Constructies die een build laten hangen of falen. Een uitwerking die deze
# bevat, kan onbewaakt niet draaien en mag daarom overgeslagen worden.
NIET_UITVOERBAAR = re.compile(
    r"\binput\s*\(|\bwhile\s+True\b|\bfrom\s+turtle\b|\bimport\s+turtle\b|\bvpython\b"
)


def celtekst(cel: dict) -> str:
    bron = cel.get("source", "")
    return ("".join(bron) if isinstance(bron, list) else bron).strip()


def rubriek(pad: str) -> str | None:
    """Bepaalt op welk soort materiaal een bestand hoort, of None."""
    delen = pad.replace("\\", "/").split("/")
    if "source" not in delen:
        return None
    na_source = delen[delen.index("source") + 1 :]
    return na_source[0] if na_source else None


def controleer(pad: str) -> list[str]:
    with open(pad, encoding="utf-8") as f:
        notebook = json.load(f)

    soort = rubriek(pad)
    problemen = []

    for nummer, cel in enumerate(notebook.get("cells", [])):
        if cel.get("cell_type") != "code":
            continue

        tekst = celtekst(cel)
        tags = cel.get("metadata", {}).get("tags", [])
        overgeslagen = SKIP in tags

        if soort in ("problems", "practicals"):
            if overgeslagen or RAISES in tags:
                continue
            eerste = tekst.splitlines()[0][:50] if tekst else "(lege cel)"
            problemen.append(
                f"Cel {nummer} mist de tag `{SKIP}`: {eerste}\n"
                f"      Een opgave hoort de student leeg te bereiken. Draagt de cel met "
                f"opzet\n      een fout voor, gebruik dan `{RAISES}`."
            )

        elif soort == "solutions":
            if not overgeslagen:
                continue
            if NIET_UITVOERBAAR.search(tekst):
                continue
            eerste = tekst.splitlines()[0][:50] if tekst else "(lege cel)"
            problemen.append(
                f"Cel {nummer} draagt `{SKIP}` maar kan draaien: {eerste}\n"
                f"      Een uitwerking die draait, wordt bij elke build gecontroleerd. "
                f"Haal de\n      tag weg, tenzij de cel invoer vraagt of niet eindigt."
            )

    return problemen


def main(paden: list[str]) -> int:
    fout = False

    for pad in paden:
        if not pad.endswith(".ipynb") or rubriek(pad) is None:
            continue
        try:
            problemen = controleer(pad)
        except json.JSONDecodeError as e:
            print(f"CELCONTROLE {pad}: geen geldig notebook ({e})")
            fout = True
            continue

        naam = pad.split("/")[-1]
        if problemen:
            fout = True
            print(f"CELCONTROLE {naam}: {len(problemen)} probleem/problemen gevonden:")
            for p in problemen:
                print(f"    - {p}")
            print("    Corrigeer deze problemen voordat je verder gaat.")

    return 1 if fout else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
