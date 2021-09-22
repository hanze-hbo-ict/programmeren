# Een voorbeeld van een Picobot-programma met 5 toestanden

Dit is één voorbeeld van een Picobot-programma met 5 toestanden en 9 regels
per toestand die met `__repr__` is afgedrukt.

Je kan als voorbeeld gebruiken om te zorgen dat je methode `__repr__` uitvoer geeft die
rechtstreeks gekopieerd en geplakt kan worden in de [Picobot-simulator](../assets/picobot.html).

```
0 NExx -> W 2
0 NxWx -> E 0
0 Nxxx -> E 2
0 xExS -> W 4
0 xExx -> W 4
0 xxWS -> N 3
0 xxWx -> N 4
0 xxxS -> E 3
0 xxxx -> N 0

1 NExx -> S 0
1 NxWx -> E 2
1 Nxxx -> S 2
1 xExS -> N 4
1 xExx -> S 0
1 xxWS -> E 2
1 xxWx -> S 2
1 xxxS -> N 4
1 xxxx -> S 3

2 NExx -> W 2
2 NxWx -> E 4
2 Nxxx -> W 3
2 xExS -> N 0
2 xExx -> N 2
2 xxWS -> E 0
2 xxWx -> S 1
2 xxxS -> N 3
2 xxxx -> E 0

3 NExx -> S 0
3 NxWx -> E 1
3 Nxxx -> E 4
3 xExS -> W 0
3 xExx -> N 4
3 xxWS -> N 3
3 xxWx -> E 1
3 xxxS -> N 2
3 xxxx -> W 1

4 NExx -> S 1
4 NxWx -> E 2
4 Nxxx -> E 0
4 xExS -> N 4
4 xExx -> W 2
4 xxWS -> N 1
4 xxWx -> N 2
4 xxxS -> E 3
4 xxxx -> S 0
```
