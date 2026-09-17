# Uitwerking opstap: Mandelbrot rekenen

```python
def mult(c, n):
    """Geeft c maal n terug met herhaald optellen."""
    result = 0  # verzamelvariabele
    for _ in range(n):
        result += c
    return result


def update(c, n):
    """Voert n keer z = z**2 + c uit."""
    z = 0  # verzamelvariabele voor de tussenstand
    for _ in range(n):
        z = z**2 + c
    return z


def in_mset(c, n):
    """Geeft False terug zodra de reeks buiten de grens komt."""
    z = 0  # verzamelvariabele voor de opeenvolgende waarden van z
    for _ in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False  # verlaat de functie; dit is niet het einde van de lus
    return True


assert mult(3, 5) == 15
assert update(1, 3) == 5
assert update(-1, 10) == 0
assert in_mset(0 + 0j, 25) is True
assert in_mset(3 + 4j, 25) is False
```
