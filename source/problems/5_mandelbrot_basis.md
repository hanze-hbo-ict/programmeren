# Basis: Mandelbrot op een raster

## Van pixel naar complex getal

Neem je functies uit de opstap over in `mandelbrot.py`. Een afbeelding heeft
kolommen en rijen als gehele getallen. De mandelbrotberekening gebruikt
complexe getallen. De functie `scale` vertaalt een pixelnummer naar een waarde
in een gekozen bereik.

## Stap 1: schalen

Schrijf `scale(pix, pix_max, value_min, value_max)`. De eerste pixel hoort bij
`value_min` en de laatste pixel ligt aan de andere kant van het bereik.

```python
def scale(pix, pix_max, value_min, value_max):
    """Vertaalt pix naar het bereik value_min tot value_max."""
    ...


assert scale(100, 200, -2.0, 1.0) == -0.5
assert scale(100, 200, -1.5, 1.5) == 0.0
```

## Stap 2: een raster doorlopen

Schrijf `count_inside(width, height, n)`. Doorloop alle kolommen en rijen met
geneste lussen. Gebruik `scale` om `c = x + y * 1j` te maken en tel hoeveel
punten `in_mset(c, n)` oplevert.

```python
def count_inside(width, height, n):
    """Telt rasterpunten die na n updates binnen blijven."""
    ...


assert count_inside(1, 1, 25) == 0
```

De exacte waarde verandert als je het raster of het aantal iteraties verandert;
de assertion maakt het kleinste geval controleerbaar. In de extra laag gebruik
je hetzelfde raster om een PNG-afbeelding te schrijven.
