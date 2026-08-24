# Begrippenlijst

Eén begrip, één term. Deze lijst legt vast welke term we gebruiken waar het
materiaal nu nog wisselt, zodat een student niet halverwege de cursus hetzelfde
ding onder een andere naam tegenkomt.

De lijst is normatief: wat hier staat, is de afspraak. Ontbreekt een term die je
vaker gebruikt, voeg hem toe.

Dit document is voor auteurs, niet voor studenten. Het staat bewust buiten
`source/` en maakt geen deel uit van het boek.

## De regel

De schrijfwijzer zegt: gebruik de Engelse vakterm waar die gangbaarder is, en
forceer geen Nederlandse vertaling. Voor dit materiaal werkt dat zo uit:

1. **Is er een Nederlandse term die in het materiaal al domineert, gebruik die.**
   Lijst, lus, klasse en element zijn ingeburgerd; die vertalen we niet terug.
2. **Is er geen Nederlandse term in gebruik, gebruik de Engelse.** Voor string,
   dictionary, integer en float is er geen ingeburgerd Nederlands alternatief.
3. **Bedoel je de taalconstructie zelf, zet die in code-opmaak.** De zin gaat
   over een *lijst*; het type heet `list`. Zo blijft het onderscheid zichtbaar
   tussen het begrip en het Python-woord, en lees je `class` nooit per ongeluk
   als het Nederlandse "klasse".

## Vaste termen

| Begrip | Wij schrijven | Ook aangetroffen | Toelichting |
|---|---|---|---|
| Verzameling waarden op volgorde | **lijst** | list (155×) | Het type heet `list` |
| Reeks tekens | **string** | tekst (197×) | Geen ingeburgerd Nederlands; "tekst" is wat erin staat, niet het type |
| Sleutel-waardepaar-container | **dictionary** | - | Consistent in gebruik |
| Geheel getal | **integer** | geheel getal (3×) | Het type heet `int` |
| Kommagetal | **floating-point getal** | float (9×), kommagetal (4×) | Het type heet `float` |
| Herhaling | **lus** | loop (23×), herhaling (10×) | |
| Bouwsteen van een lijst | **element** | item (2×) | |
| Sjabloon voor objecten | **klasse** | class (145×) | Het sleutelwoord is `class` |
| Functie in een klasse | **methode** | - | |
| Waarde die je meegeeft | **argument** | - | Bij de definitie heet het een **parameter** |
| Resultaat opleveren | **teruggeven** | - | Niet "returnen" |
| Op het scherm tonen | **afdrukken** | printen (12×) | |
| Een programma starten | **uitvoeren** | draaien (5×) | |
| Een functie gebruiken | **aanroepen** | oproepen (1×) | |
| Melding bij een fout | **foutmelding** | error, exception, uitzondering | Voor het Python-mechanisme: `exception` |

## Opgave, opdracht, practicum

Deze drie liepen door elkaar. In koppen komt `Opdracht` 137 keer voor en
`Opgave` 108 keer, verspreid over dezelfde soorten documenten. Voorstel voor een
werkverdeling die aansluit op de structuur die er al is:

| Term | Betekenis |
|---|---|
| **college** | Het materiaal onder `lectures/` |
| **practicum** | Het materiaal onder `practicals/` |
| **opgave** | Een huiswerkitem onder `problems/`, zoals de inhoudsopgave het al noemt |
| **opdracht** | Een genummerde taak *binnen* een document, ongeacht welk soort |

Zo krijgt elk woord één taak: opgave is het artefact, opdracht is de stap erin.
Dit raakt veel koppen en wordt dus niet in één keer doorgevoerd, maar per
document bij de herziening.

## Woorden die geen synoniem zijn

Een paar termen lijken op elkaar maar zijn het niet. Vervang ze niet
automatisch.

- **rij** betekent in dit materiaal meestal *reeks* of *horizontale lijn*, niet
  *lijst*: "drie op een rij", "de Rij van Conway", "de rijen en kolommen van het
  bord". Van de 153 gevallen slaan er 20 op een rij in een tweedimensionale
  structuur en de rest op iets anders. Gebruik **lijst** voor het datatype en
  **rij** alleen waar het echt om een rij gaat.
- **tekst** is wat er in een string staat; **string** is het type.
- **parameter** staat in de functiedefinitie; **argument** is wat je meegeeft
  bij de aanroep.

## Engelse termen die we niet vertalen

`string`, `dictionary`, `integer`, `float`, `list comprehension`, `recursie`,
`debuggen`, `commit`, `branch`, `assertion`, `docstring`, `index`, `slice`.

Introduceer zo'n term bij eerste gebruik kort in het Nederlands. Voor
eerstejaars is die ene toelichting nodig; daarna volstaat de term.
