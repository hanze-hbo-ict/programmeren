# Feest met Fibonacci

| Naam         | Beschrijving                                                   |
|--------------|----------------------------------------------------------------|
| Onderwerp    | Een Fibonacci-reeks in `hmmm`                                  |
| Bestandsnaam | `wk7ex3.hmmm`                                                  |
| Inleveren    | Lever jouw bestand met de juiste bestandsnaam in op GradeScope |

De [Fibonacci-reeks](https://en.wikipedia.org/wiki/Fibonacci_number) is een van de meest bekende reeksen getallen in de wiskunde. Het eerste Fibonacci-getal is 1, het tweede Fibonacci-getal is 1, en in het algemeen is het volgende Fibonacci-getal in de reeks de som van de vorige twee. De eerste paar getallen in de reeks zijn 1, 1, 2, 3, 5, 8, 13, 21.

De opgave is om een programma in Hmmm-assembly te schrijven die een enkel getal van de gebruiker ontvangt, zeg `n`, en de eerste `n` Fibonacci-getallen afdrukt. Het is het makkelijst om het bestand `wk7ex3.hmmm` te gebruiken uit de map die je bij de opgave [Hmmm... Assembly!](hmmm_assembly) hebt gedownload.

::: {admonition} Een register kopiëren
:class: tip
Het zal waarschijnlijk nodig blijken om de inhoud van een register `rX` in een ander register `rY` kopieëren tijdens dit programma. Bekijk de Hmmm [documentatie](/support/hmmm); het commando om `r1` naar `r2` te kopiëren, dat wil zeggen, `r2 = r1` in Python, is

```asm
copy r2 r1
```

Merk op dat deze instructie gegevens van rechts naar links verplaatst; dit lijkt op het toekenningsstatement in Python, immers, `y = x` kent de waarde van `x` toe aan `y`.
:::

Bij deze opgave mag je ervanuit gaan dat de invoer `n` altijd minimaal 2 is. Hier is een voorbeeld van invoer en uitvoer:

```console
Enter number: 10
1
1
2
3
5
8
13
21
34
55
```

Onthoud dat je bij elke regel code commentaar moet schrijven. Test bovendien je programma zorgvuldig, te beginnen met `n == 2`.
