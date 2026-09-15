# Opstap: Mandelbrot rekenen

## Het probleem

Je bouwt stap voor stap een programma dat onderzoekt welke complexe getallen
bij de mandelbrotverzameling horen. Download {download}`mandelbrot.zip
<assets/mandelbrot.zip>` en pak het archief uit. Werk in `mandelbrot.py`.

Installeer Pillow eenmalig als Python meldt dat de module ontbreekt:

```bash
pip install Pillow
```

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


assert in_mset(0 + 0j, 25) is True
assert in_mset(3 + 4j, 25) is False
```

Je hebt nu de rekenkern. In de basislaag gebruik je die kern voor een raster.
