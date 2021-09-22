# Vpython-voorbeeld van elastische botsingen tussen twee bollen

Het volgende codefragment laat zien hoe je elastische botsingen tussen twee bewegende bollen kan berekenen. Deze code werkt voor elk aantal bollen als ze maar in de lijst `sphere_list` staan.

* In deze code zijn de bewegingen *niet* precies symmetrisch; je ziet dit bij de botsing.
* Een belangrijk onderdeel is dat je *de bollen een tijdstap terug verplaatst als ze botsen*: Dit voorkomt dat de bollen over elkaar heen liggen zodat het minder waarschijnlijk is dat ze tegen elkaar blijven "plakken" doordat ze steeds botsen omdat de bollen heel vaak van richting veranderen.
* Je kan de bollen natuurlijk vervangen door alle objecten met instantievariabelen `pos` en `vel`!

```python
s0 = sphere(pos=vector(0, 0, 5),
            color=vector(1, 1, 1),
            radius=1)
s0.vel = vector(0, 0, 0)

s1 = sphere(pos=vector(6, 0, 0),
            color=vector(1, 1, 0),
            radius=1)
s1.vel = vector(0, 0, 0)


# lijst van bollen; PAS DIT AAN WAAR NODIG
sphere_list = [s0, s1]

# controle op botsingen en snelheidsverandering: elastische botsingen
for i in range(len(sphere_list)):
    for j in range(i + 1, len(sphere_list)):
        if collide(sphere_list[i], sphere_list[j]):
            # diff = de vector tussen de twee bollen
            diff = sphere_list[i].pos - sphere_list[j].pos
            dtan = rotate(diff, radians(90), vector(0, 1, 0))

            # neem de twee snelheden
            vi = sphere_list[i].vel
            vj = sphere_list[j].vel
            # draai de laatste tijdstap terug
            sphere_list[i].pos -= sphere_list[i].vel * dt
            sphere_list[j].pos -= sphere_list[j].vel * dt
            # haal de lood- en raaklijnen op
            vi_rad = proj(vi, diff)
            vi_tan = proj(vi, dtan)
            vj_rad = proj(vj, -diff)
            vj_tan = proj(vj, dtan)
            # draai de loodlijnen om en bewaar de raaklijnen
            sphere_list[i].vel = vj_rad + vi_tan
            sphere_list[j].vel = vi_rad + vj_tan
```

Bovenstaande code heeft een functie `collide` nodig. Hier is een simpel voorbeeld dat voor bollen werkt:

```python
def collide(a, b):
    diff = a.pos - b.pos
    if mag(diff) < a.radius + b.radius:
        return True
    else:
        return False
```

We zeggen hier dat er een botsing is als de afstand (`mag`) tussen de bollen kleiner is dan de som van de stralen.