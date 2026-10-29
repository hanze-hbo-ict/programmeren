# Opstap: Mandelbrot rekenen

## Het probleem

Je bouwt stap voor stap een programma dat onderzoekt welke complexe getallen
bij de mandelbrotverzameling horen. Download {download}`mandelbrot.zip
<assets/mandelbrot.zip>` en pak het archief uit. Werk in `mandelbrot.py`.

Installeer Pillow eenmalig als Python meldt dat de module ontbreekt; je krijgt dan een `ModuleNotFoundError`.

`````{tab-set}

````{tab-item} Windows
Installeer Pillow voor de Python van Scoop:

```console
python3 -m pip install Pillow
```
````

````{tab-item} macOS
Installeer Pillow met Homebrew, net als Python zelf:

```console
brew install pillow
```
````

````{tab-item} Linux
Op Linux installeer je Pillow voor de Python van je distributie.

Controleer op openSUSE eerst met `python3 --version` of je Python 3.13 gebruikt; bij een andere versie heb je een ander Pillow-pakket nodig. Vraag dan je docent om hulp, net als bij een distributie die niet in de tabel staat.

Gebruik de regel voor jouw systeem:

| Distributie | Commando's |
| --- | --- |
| Ubuntu, Debian, Linux Mint, Pop!_OS, Zorin OS | Eerst `sudo apt update`, daarna `sudo apt install python3-pil` |
| Fedora | `sudo dnf install python3-pillow` |
| Arch Linux | `sudo pacman -Syu python-pillow` |
| openSUSE Leap 16.0 of Tumbleweed met Python 3.13 | `sudo zypper install python313-Pillow` |

De Linux-commando's vragen beheerdersrechten. Het Arch-commando werkt ook je systeem bij.
````

`````

Controleer op elk besturingssysteem of Pillow bij dezelfde Python beschikbaar is:

```console
python3 -c "from PIL import Image"
```

Keert de prompt terug zonder foutmelding, dan is Pillow beschikbaar. Krijg je een foutmelding, ook bij een bestaande Python-installatie, vraag dan je docent om hulp.

De afbeelding-API komt later; in deze opstap werk je alleen met waarden en
lussen.

## Stap 1: herhaald optellen

Schrijf `mult(c, n)`. Tel `c` precies `n` keer op bij een resultaat dat met nul
begint. Gebruik een `for`-lus en geef het resultaat terug.

```python
def mult(c, n):
    """Geeft c maal de positieve integer n terug met optellen."""
    ...


assert mult(3, 5) == 15
assert mult(1.5, 28) == 42.0
```

## Stap 2: de update

Schrijf `update(c, n)`. Begin met `z = 0` en voer `z = z**2 + c` precies `n`
keer uit.

```python
def update(c, n):
    """Voert n updates uit en geeft de laatste z terug."""
    ...


assert update(1, 3) == 5
assert update(-1, 10) == 0
```

## Stap 3: binnen of buiten

Schrijf `in_mset(c, n)`. Geef tijdens de lus meteen `False` terug zodra
`abs(z) > 2`. Als de lus klaar is zonder zo'n waarde, geef je `True` terug.

```python
def in_mset(c, n):
    """Test c gedurende hoogstens n updates."""
    ...


assert in_mset(0 + 0j, 25) == True
assert in_mset(3 + 4j, 25) == False
```

Je hebt nu de rekenkern. In de basislaag gebruik je die kern voor een raster.
