---
title: De macht van recursie!
description: Recursieve machtsverheffing in `hmmm`
file: wk7ex4.hmmm
points: 10
---

# De macht van recursie!

In de opgave [De macht van Hmmm!](macht_van_hmmm) heb je een programma geschreven om "`x` tot de macht van `y`" te berekenen via *iteratie*.

In deze opgave ga je een *recursief* programma schrijven om `x` tot de macht `y` te berekenen.

Let op, jouw programma hoeft alleen *niet-negatieve* invoer te kunnen verwerken.

## Voorbeeld in Python

Bekijk het volgende recursieve Python programma, waarin `main()` invoer van de gebruiker krijgt en een recursieve functie `power` aanroept die "`x` tot de macht van `y`" berekent en het resultaat teruggeeft aan `main` om het vervolgens af te drukken.

```python
def main():
    x = int(input())  # we willen de gebruiker vragen
    y = int(input())  # om invoer voor x en y
    print(power(x, y))


def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)
```

### Voorbeelduitvoer

Hier is een voorbeeld van de Hmmm-code die `3 ** 5 == 243` berekent.

Toegegeven, dit is niet zo spannend, maar dat komt omdat alle spannende dingen in het Hmmm-programma gebeuren!

```console
Enter number: 3
Enter number: 5
243
```

(Zorg dat je niet per ongeluk `5 ** 3` berekent, dat is 125.)

## Recursief machtsverheffen

De opgave is om deze recursive machtsverheffingscode in Hmmm-assembly te implementeren.

Je kan beginnen met het gegeven bestand `wk7ex4.hmmm`, uit de map die je gedownload hebt in de opgave [Hmmm... Assembly!](hmmm_assembly).

Verwijder dan het Hmmm-programma dat als voorbeeld in dit bestand staat. Vervang het door het recursieve faculteitsvoorbeeld uit het college, dat hieronder getoond is.

Pas daarna het recursieve faculteitvoorbeeld aan om een zo "getrouw" mogelijke Hmmm-implementatie te maken van de recursieve functie `power` te maken.

Bij "getrouw" bedoelen we dat een deel van je Hmmm-code moet overeenkomen met `main` en een deel moet overeenkomen met `power`. Het `main`-gedeelte leest de invoerwaardes `x` en `y` in van de gebruiker en springt naar `power`. Je `power`-code moet, in het recursieve geval, zichzelf recursief aanroepen met `power(x, y-1)` en dan na de recursie het resultaat
daarvan met `x` vermenigvuldigt en die waarde teruggeeft. Je zult een stack met functieaanroepen nodig hebben, zoals besproken is tijdens het college.

Merk op dat in de Pythoncode `power` niets afdrukt; het geeft het terug aan `main`, die het daadwerkelijke afdrukken regelt. In Hmmm moet je de uitvoer wel afdrukken.

```asm
# Dit is de recursieve faculteit (uit het college):

00 read  r1             # Lees gebruikersinvoer in in r1
01 setn  r15 42         # Initialiseer de stack pointer
02 nop                  # Ruimte voor uitbreiding (zie wk7ex4!)
03 calln r14 7          # Roep de faculteitsfunctie aan (op regel 7)
04 nop                  # Ruimte voor uitbreiding (zie wk7ex4!)
05 write r13            # Druk uitvoer af op het scherm
06 halt                 # Klaar!

# +++ Faculteitsfunctie +++
# Basisgeval (regels 7-10)
07 jnezn r1  11         # de test voor het basisgeval: is de invoer r1 != 0 ?
08 setn  r13 1          # Als r1 0 is, dan is het resultaat, r13, 1
09 nop                  # Ruimte voor uitbreiding (of om iets af te drukken!)
10 jumpr r14            # Geef het resultaat, r13, terug aan het regelnummer in r14

# Recursief geval (regels 11-20)
11 pushr r1  r15        # Bewaar (push) r1 op de stack (op positie r15)
12 pushr r14 r15        # Bewaar (push) r14 op de stack
13 addn  r1 -1          # Bepaal N-1 en zet het in r1
14 nop                  # Ruimte voor uitbreiding (of om iets af te drukken!)
15 calln r14 7          # Vraag nu de faculteit van N-1  (Wow!)
16 nop                  # Ruimte voor uitbreiding (of om iets af te drukken!)
17 popr  r14 r15        # Verkrijg (pop) r14 van de stack
18 popr  r1  r15        # Verkrijg (pop) r1 van de stack
19 mul   r13 r1 r13     # Bereken r13 = N * fac(N-1)   (Wow!)
20 jumpr r14            # Klaar! Geef r13 terug naar de aanroeper in r14
```

::: {admonition} Maak gebruik van het faculteitsprogramma
:class: notice

Faculteit en machtsverheffen lijken HEEL erg op elkaar! Je hoeft maar een paar regels aan te passen (misschien zelfs verbazingwekkend weinig) om je recursieve machtsverheffunctie te maken als je met bovenstaande code begint.
:::

::: {admonition} Sla het grondtal op in `r2`
:class: tip

Overweeg om van de eerste regel

```asm
00 read r2
```

te maken en dan verder te gaan met de faculteitscode. Hierdoor kan het grondtal in `r2` blijven en (nadat de andere regels doorgenummerd zijn) kan de macht in `r1` staan. Dit is handig!

Als je dit doet hoef je bovendien de rest van de code niet te hernummeren dankzij de `nop`!
:::

### Testen en inleveren

Zoals bij elke Hmmm-opgave moet je elke regel, of bijna elke regel, van commentaar voorzien, zoals in het voorbeeld hierboven. Test je code bovendien grondig!