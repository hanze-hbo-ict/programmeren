# Fibonacci recursief

| Naam         | Beschrijving                                                   |
|--------------|----------------------------------------------------------------|
| Onderwerp    | Een recursieve Fibonacci-reeks in `hmmm`                       |
| Bestandsnaam | `wk7ex6.py`                                                    |
| Inleveren    | Lever jouw bestand met de juiste bestandsnaam in op GradeScope |
| Opmerking    | **Dit is een bonusopgave**                                     |

In de opgave [Feest met Fibonacci](feest_met_fibonacci) heb je een Hmmm-programma geschreven die door middel van een lus de Fibonacci-reeks, 1, 1, 2, 3, 5, 9, 13, 21, ..., afdrukte.

In deze opgave schrijf je deze Fibonacci-generator opnieuw, maar nu *recursief*.

Begin met het maken van een bestand `wk7ex6.hmmm`; je kan hier één van de Hmmmm-programma's van een eerdere opgave voor gebruiken.

We kunnen de Fibonacci-reeks niet alleen sequentieel uitdrukken, maar ook *recursief*, door middel van de volgende wiskundige *recurrente betrekking*:

```python
fib(1) = 1
fib(2) = 1
fib(n) = fib(n-1) + fib(n-2)
```

In deze bonusopgave ga je een functie schrijven die maar **één term** uit de Fibonacci-reeks oplevert, maar dit doet door middel van een **functie** om het *n*-de Fibonacci-getal te berekenen.

## De recursieve Python-code die je gaat nabouwen

Hier is een recursief Python-programma om de *n*-de term uit de Fibonacci-reeks te berekenen:

```python
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
```

Bedenk eerst waarom we hier eigenlijk twee basisgevallen (`if n == 1 or n == 2`) nodig hebben. Wat zou er gebeuren als we alleen het basisgeval `n == 1` gebruiken?

Merk op dat je dit programma ook zonder recursie zou kunnen schrijven, maar we willen hier oefenen met recursie. Wel zie je hieronder een in wat meer detail uitgeschreven versie van het recursieve programma hierboven, waar de stappen opgedeeld zijn in kleinere stappen.
We vragen je **deze uitgebreidere versie** te herschrijven in Hmmm. Probeer het programma zo nauwkeurig mogelijk na te bouwen.

```python
def main():
    r1 = int(input())   # Regel 1, lees invoer van de gebruiker
    r13 = fib(r1)       # Regel 2, roep fib aan met paraemeter r1
    #print(r1)          # (alleen om te debuggen; lever dit niet in) Regel 3, druk r1 af
    print(r13)          # Regel 4, druk het r1-ste Fibonnaci-getal af
    return              # Regel 5, stop het programma

def fib(r1):
    if r1 - 2 <= 0:     # Regel 6, als r1 - 2 <= 0 dan is dit fib(1) of fib(2), en dus is het antwoord 1
        return 1        # Regel 7, dus geef 1 terug
    else:               # Regel 8, anders...
        r13 = fib(r1-1) # Regel 9, bereken fib(r1-1)
        r3 = r13        # Regel 10, sla het resultaat ergens anders op, want r13 is speciaal is special
        r13 = fib(r1-2) # Regel 11, bereken fib(r1-2)
        r13 = r13 + r3  # Regel 12, tel nu de resultaten van fib(r1-1) en fib(r1-2) bij elkaar op...
        return r13      # Regel 13, ...dat is de waarde die teruggegeven wordt in r13
```

Zorg dat je een regel commentaar bij elke regel van je Hmmm-programma zet om aan te geven welke regel van het Python-programma
daar geïmplementeerd wordt.

Soms zullen er meerdere regels Hmmm-code nodig zijn om een enkele regel Python-code te implementeren!

::: {admonition} Belangrijk
:class: warning

Bedenk goed welke "belangrijke gegevens" je op de stack moet zetten om ze te bewaren. De functie `main` heeft maar één belangrijk gegeven als `fib` aangeroepen wordt, de waarde van `r1`. Bedenk dat `r1` gebruikt wordt door deze af te drukken nadat de aanroep naar `fib` geweest is, dus het is belangrijk dat deze opgeslagen wordt voor de functieaanroep. De recursieve aanroep van regel 9 heeft twee belangrijke gegevens, welke zijn dat? De recursieve aanroep op regel 11 heeft zelfs **drie** belangrijke gegevens!
:::

## Stappenplan voor dit (lastige) probleem

Dit is zeker een uitdaging, maar als het je lukt, kan je wel zeggen dat je recursieve functies geschreven hebt in assembly! Tja 🙃

Hier is een overzicht van hoe je oplossing zou kunnen werken.

Het idee is om de *uitgebreide* versie van het programma hierboven om te zetten in Hmmm-assembly. Hier heb je functieaanroepen en recursie voor nodig. Een goed voorbeeld om te bekijken is het recursieve faculteitsprogramma dat tijdens het college is langsgekomen, waarbij je dit kan vergelijken met de Python-versie van datzelfde programma.

Het belangrijkste is om eerst een overzicht te krijgen van de onderdelen van het programma; daarna kan je de onderdelen makkelijker bouwen. Je vindt hier de onderdelen die je nodig hebt. De regelnummers zijn vermoedelijk erg ruim, maar je kan altijd `nop`s gebruiken!

* **Regels 0-10: implementeer de functie `main`**: invoer, de positie van de stack instellen (`setn r15 60`; zorg dat deze waarde hoger is dan de laatste regel code), de aanroep naar de Fibonacci-functie op regel 11, en daarna het resultaat afdrukken.
* **Regel 11: dit is het begin van de Fibonacci-functie**: alle `call`s gaan naar deze regel, bijvoorbeeld `calln r14 11`.
* **Regels 11-16: het basisgeval**: deze lijkt op het basisgeval van facuilteit; alleen de details zijn anders, niet de structuur
* **Regel 17: het begin van het recursieve geval**: spring hier naar toe als het basisgeval niet van toepassing is
* **Regels 17-20: push waardes op de stack**: om de recursieve aanroep `fib(r1-1)` te kunnen doen, moet je `r1` en `r14` op de stack zetten.
  * Dit is dezelfde code als de twee push-regels bij het voorbeeld met de faculteit
* **Regels 21-25: voorbereiden en aanroepen van `fib(r1-1)`**: de aanroep zelf is `calln r14 11`; je hebt hier misschien minder dan vijf regels voor nodig.
* **Regels 26-29: pop waardes van de stack**: `r13` is nu het `r1-1`-ste Fibonacci-getal, en nu moeten `r14` en `r1` teruggezet worden van de stack zodat we door kunnen gaan waar we waren
  * Dit is dezelfde code als de twee pop-regels bij het voorbeeld met de faculteit
* **Regel 30:** `copy r3 13`. Dit is de implementatie van regel 10 uit de Python-code
* **Regels 31-36: push waardes op de stack**: dit moet opnieuw, nu voor de aanroep `fib(r1-2)`
  * Je moet nu ook `r3` pushen, omdat we deze hierna weer nodig hebben (net als `r1` en `r14`, maar die zijn altijd belangrijk)
  * Je hebt nu dus *drie* regels nodig!
* **Regels 37-41: voorbereiden en aanroepen van `fib(r1-2)`** opnieuw met `calln r14 11`; maar ook hier heb je misschien geen vijf regels nodig.
* **Regels 42-47: pop waardes van de stack voor de tweede aanroep**: ook hier zijn *drie* regels nodig!
* **Regel 48: implementeer regel 12** van de Python-code; dit kan met één instructie
* **Regel 48: implementeer regel 13** van de Python-code; dit kan met één instructie

Dat is een fors stuk code! Je kan wel zien waarom dit soort omzetting niet (meer...) door mensen wordt gedaan, maar door computers. We kijken hier deze week zo uitgebreid naar om echt goed in te zien wat programmeertalen doen: ze vertalen een "natuurlijke" syntax naar assembly.

Veel succes met dit (*bijzonder*) uitdagend probleem!