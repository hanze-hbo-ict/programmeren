"""Opent de pagina's die deze branch wijzigt ten opzichte van master.

Bedoeld voor `make review PR=<nummer>`. De build zelf duurt maar een paar
seconden zolang de notebookcache intact is; het opzoeken van de juiste pagina's
was het bewerkelijke deel.
"""

import subprocess
import sys
import webbrowser
from pathlib import Path

BUILD = Path("build/html")


def gewijzigde_bronbestanden():
    uit = subprocess.run(
        ["git", "diff", "--name-only", "master...HEAD", "--", "source/"],
        capture_output=True, text=True, check=True,
    ).stdout.split()
    return [Path(p) for p in uit if p.endswith((".md", ".ipynb"))]


def naar_pagina(bron):
    """source/lectures/0a_command-line.md -> build/html/lectures/0a_command-line.html"""
    return BUILD / bron.relative_to("source").with_suffix(".html")


def main():
    bronnen = gewijzigde_bronbestanden()
    if not bronnen:
        print("Geen gewijzigde pagina's ten opzichte van master.")
        return 0

    paginas = [p for p in map(naar_pagina, bronnen) if p.exists()]
    ontbreekt = [b for b, p in zip(bronnen, map(naar_pagina, bronnen)) if not p.exists()]

    for p in paginas:
        print(f"  {p}")
        webbrowser.open(p.resolve().as_uri())

    for b in ontbreekt:
        print(f"  {b}: geen gebouwde pagina; staat die in de inhoudsopgave?")

    print(f"\n{len(paginas)} pagina's geopend.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
