# Extra: van tekst naar beeld

Uitwerking van [de extra-opgave](/problems/6_extra). `save_rgb` komt uit de
`png.py` van het [practicum](/practicals/6b_images); die module zit in
{download}`fraaie_plaatjes.zip <../problems/assets/fraaie_plaatjes.zip>`. Pak
die zip uit en zet dit programma in dezelfde directory, dan slaagt de import.

Het pad `../problems/assets/patroon.txt` hieronder loopt van deze uitwerking
naar de asset in de repository. Draai je het programma zelf, dan wijs je naar
het `patroon.txt` dat je bij de opgave hebt gedownload.

```python
def read_raster(filename):
    """Lees een niet-leeg rechthoekig raster met . en #."""
    with open(filename) as bestand:
        raster = []
        for regel in bestand:
            raster = raster + [regel[:-1]]
    return raster
```

```python
def raster_to_pixels(raster):
    """Zet . en # om in witte en zwarte RGB-lijsten."""
    pixels = []
    for regel in raster:
        pixelregel = []
        for teken in regel:
            if teken == ".":
                pixelregel = pixelregel + [[255, 255, 255]]
            else:
                pixelregel = pixelregel + [[0, 0, 0]]
        pixels = pixels + [pixelregel]
    return pixels
```

```python
def scale_pixels(pixels):
    """Maak van iedere pixel een blok van 8 bij 8 pixels."""
    geschaald = []
    for regel in pixels:
        brede_regel = []
        for pixel in regel:
            for _ in range(8):
                brede_regel = brede_regel + [pixel[:]]
        for _ in range(8):
            kopie_regel = []
            for pixel in brede_regel:
                kopie_regel = kopie_regel + [pixel[:]]
            geschaald = geschaald + [kopie_regel]
    return geschaald
```

```python
from png import save_rgb


def write_pattern_image(pixels):
    """Schrijf de geschaalde pixels als patroon.png."""
    save_rgb(pixels, "patroon.png")
```

Daarmee is het programma compleet. Het blok hieronder controleert de vier
functies op de meegeleverde asset en schrijft `patroon.png` weg. De assertions
staan hier en niet in de functies zelf: zo testen ze wat er uit een functie
komt, en dat is wat je wilt weten.

```python
raster = read_raster("../problems/assets/patroon.txt")
assert len(raster) == 16
assert len(raster[0]) == 16
for regel in raster:
    assert len(regel) == 16
    for teken in regel:
        assert teken == "." or teken == "#"
pixels = raster_to_pixels(raster)
assert len(pixels) == 16
assert len(pixels[0]) == 16
assert pixels[0][0] == [255, 255, 255]
assert pixels[2][4] == [0, 0, 0]
assert pixels[6][8] == [0, 0, 0]
klein = raster_to_pixels([".#"])
assert klein == [[[255, 255, 255], [0, 0, 0]]]
geschaald = scale_pixels(pixels)
assert len(geschaald) == 128
assert len(geschaald[0]) == 128
for regel in geschaald:
    assert len(regel) == 128
assert geschaald[16][32] == [0, 0, 0]
assert geschaald[0][0] == [255, 255, 255]

zwarte_bron = 0
for regel in raster:
    for teken in regel:
        if teken == "#":
            zwarte_bron = zwarte_bron + 1
zwarte_geschaald = 0
for regel in geschaald:
    for pixel in regel:
        if pixel == [0, 0, 0]:
            zwarte_geschaald = zwarte_geschaald + 1
assert zwarte_geschaald == zwarte_bron * 64
for bron_rij in range(16):
    for bron_kolom in range(16):
        kleur = pixels[bron_rij][bron_kolom]
        for rij in range(bron_rij * 8, (bron_rij + 1) * 8):
            for kolom in range(bron_kolom * 8, (bron_kolom + 1) * 8):
                assert geschaald[rij][kolom] == kleur
write_pattern_image(geschaald)
```
