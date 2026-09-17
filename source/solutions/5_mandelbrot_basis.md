# Uitwerking basis: Mandelbrot op een raster

```python
def scale(pix, pix_max, value_min, value_max):
    """Vertaalt pix naar een waarde in het gekozen bereik."""
    return value_min + pix / pix_max * (value_max - value_min)


def count_inside(width, height, n):
    """Telt de rasterpunten die binnen blijven."""
    count = 0  # verzamelvariabele voor de punten die binnen blijven
    for col in range(width):
        for row in range(height):
            x = scale(col, width, -2.0, 1.0)
            y = scale(row, height, -1.0, 1.0)
            if in_mset(x + y * 1j, n):
                count += 1
    return count


assert scale(100, 200, -2.0, 1.0) == -0.5
assert count_inside(1, 1, 25) == 0
```
