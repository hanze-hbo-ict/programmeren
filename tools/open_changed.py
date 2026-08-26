"""Bouwt niets, maar toont de pagina's die deze branch wijzigt ten opzichte van
master.

Serveert `build/html` over HTTP in plaats van de bestanden rechtstreeks te
openen. Dat is nodig: de pagina's laden Mermaid als ES-module vanaf een CDN, en
een browser weigert zo'n import op een `file://`-pagina. Over HTTP werkt het
zoals op de gepubliceerde site.
"""

import functools
import http.server
import socketserver
import subprocess
import sys
import threading
import webbrowser
from pathlib import Path

BUILD = Path("build/html")


def gewijzigde_paginas():
    """De gebouwde pagina's die horen bij de gewijzigde bronbestanden."""
    uit = subprocess.run(
        ["git", "diff", "--name-only", "master...HEAD", "--", "source/"],
        capture_output=True, text=True, check=True,
    ).stdout.split()

    paginas, ontbreekt = [], []
    for pad in uit:
        bron = Path(pad)
        if bron.suffix not in {".md", ".ipynb"}:
            continue
        pagina = bron.relative_to("source").with_suffix(".html")
        (paginas if (BUILD / pagina).exists() else ontbreekt).append(pagina)
    return paginas, ontbreekt


def serveer():
    """Start een server op een vrije poort en geeft die poort terug."""
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(BUILD))
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.TCPServer(("127.0.0.1", 0), handler)
    poort = server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, poort


def main():
    if not BUILD.exists():
        print(f"{BUILD} bestaat niet; draai eerst `make html`.")
        return 1

    paginas, ontbreekt = gewijzigde_paginas()
    if not paginas and not ontbreekt:
        print("Geen gewijzigde pagina's ten opzichte van master.")
        return 0

    server, poort = serveer()
    for pagina in paginas:
        url = f"http://127.0.0.1:{poort}/{pagina.as_posix()}"
        print(f"  {url}")
        webbrowser.open(url)

    for bron in ontbreekt:
        print(f"  {bron}: geen gebouwde pagina; staat die in de inhoudsopgave?")

    print(f"\n{len(paginas)} pagina's geopend. Ctrl+C sluit de server.")
    try:
        threading.Event().wait()
    except KeyboardInterrupt:
        print("\nServer gestopt.")
    finally:
        server.shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(main())
