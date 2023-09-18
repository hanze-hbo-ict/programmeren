---
title: LMC Introductie
---

# Little man computer introductie

Deze opgave bestaat uit 5 opdrachten die gemaakt kunnen worden met behulp van het LMC model :https://peterhigginson.co.uk/lmc/


## Opdracht 1

a. Gegeven onderstaande tabel. In de eerste kolom staan de instructies. In de tweede kolom wordt de accumulator bijgehouden. In de derde kolom wordt veranderingen in het geheugen genoteerd. De laatste kolom wordt input en output aangegeven. Maak de tabel af

| instructie | Accumulator | Geheugen | Input/Output |
| ---------- | ----------- | -------- | ------------ |
| inp        | 1           |          | Input is 1   |
| sto 99     | 1           | #99 = 1  |              |
| inp        | 1           |          | input is 1   |
| sto 98     | 1           | #98 = 1  |              |
| add 99     | 1 + 1 = 2   |          |              |
| out        | 2           |          | Output is 2  |
| sto 97     | 2           | #97 = 2  |              |
| add 98     | 2 + 1 = 3   |          |              |
| out        |             |          |              |
| sto 96     |             |          |              |
| add 97     |             |          |              |
| out        |             |          |              |
| sto 95     |             |          |              |
| add 96     |             |          |              |
| out        |             |          |              |
| sto 94     |             |          |              |
| add 95     |             |          |              |
| out        |             |          |              |

b. Wat is de volgende getal in deze reeks?

## Opdracht 2

Als we de reeks langer willen maken gaan we steeds meer geheugen gebruiken op de manier. Dit is niet erg efficiënt. Past het programma zo aan dat enkel en alleen de geheugen plekken 99 en 98 gebruikt worden. Maak een tabel zoals bij opdracht 1 om te laten zien hoe je programma werkt.

## Opdracht 3

Als we de reeks nog langer willen maken gaat het veel instructies kosten terwijl we eigenlijk steeds hetzelfde willen herhalen. Tel de twee voorgaande waardes in de lijst op om de nieuwe waarde uit te rekenen. We hebben dan drie geheugen plaatsen nodig: 97 voor de nieuwe waarde, 98 voor de waarde daarvoor en 99 voor de waarde die daar weer voorzit. Die waardes schuiven steeds door. Zodra er een nieuwe waarde berekend wordt, moet de waarde van 97 naar 98 en die van 98 naar 99. We moeten wel opletten om de volgorde. Als we eerst 97 naar 98 overschrijven kunnen we niet de originele waarde van 98 overschrijven naar 99.

a.	Vul de tabel verder in.

|     | instructie | Accumulator | Geheugen | Input/Output |
| --- | ---------- | ----------- | -------- | ------------ |
| 00  | inp        | 1           |          | Input is 3   |
| 01  | sto 99     | 1           | #99 = 3  |              |
| 02  | inp        | 1           |          | input is 5   |
| 03  | sto 98     | 1           | #98 = 5  |              |
| 04  | add 99     |             |          |              |
| 05  | out        |             |          |              |
| 06  | sto 97     |             |          |              |
| 07  | lda 98     |             |          |              |
| 08  | sto 99     |             |          |              |
| 09  | lda 97     |             |          |              |
| 10  | sto 98     |             |          |              |
| 11  | add 99     |             |          |              |
| 12  | out        |             |          |              |

De volgende stap is om een loop te gaan gebruiken zodat code herhaalt gaat worden. Om dat voor elkaar te krijgen kunnen we gebruik maken van een jump. Dat verteld de computer welke instructie de volgende stap is.

b.	Vul de tabel verder in. Let op de jump opdracht en hoe de instructie nummer daarop reageert.

|        | instructie | Accumulator | Geheugen | Input/Output |
| ------ | ---------- | ----------- | -------- | ------------ |
| 00     | inp        | 1           |          | Input is 3   |
| 01     | sto 99     | 1           | #99 = 3  |              |
| 02     | inp        | 1           |          | input is 5   |
| 03     | sto 98     | 1           | #98 = 5  |              |
| 04     | add 99     |             |          |              |
| 05     | out        |             |          |              |
| 06     | sto 97     |             |          |              |
| 07     | lda 98     |             |          |              |
| 08     | sto 99     |             |          |              |
| 09     | lda 97     |             |          |              |
| 10     | sto 98     |             |          |              |
| 11     | bra **04** |             |          |              |
| **04** | add 99     |             |          |              |
| 05     | out        |             |          |              |
| 06     | sto 97     |             |          |              |
| 07     | lda 98     |             |          |              |
| 08     | sto 99     |             |          |              |
| 09     | lda 97     |             |          |              |
| 10     | sto 98     |             |          |              |
| 11     | bra 04     |             |          |              |

c.	copy & paste de onderstaande code op de website en druk op run om het programma te draaien. Waarom stopt het programma niet uit zichzelf?  (Je kan het programma laten stoppen met ‘STOP’)

inp
sto 99
inp
sto 98
add 99
out
sto 97
lda 98
sto 99
lda 97
sto 98
bra 04
hlt


## Opdracht 4

Ons programma loopt nu nog oneindig door. We moeten aangeven aan de computer wanneer het programma moet stoppen. We hebben al gezien dat we met een BRA XX naar instructie XX kunnen springen. De instructie BRZ XX zal enkel naar een instructie jumpen als de waarde in de ALU gelijk is aan 0. Dat kunnen we gebruiken om naar het einde van het programma te springen als onze counter 0 heeft bereikt.

Gegeven de onderstaande code:


00	inp
01	sto 99
02	inp
03	sto 98
04	out
05	brz 08
06	sub 99
07  bra 04
08  hlt

Maak onderstaande tabel af om te laten zien hoe de code werkt:


|     | instructie | Accumulator | Geheugen | Input/Output |
| --- | ---------- | ----------- | -------- | ------------ |
| 00  | inp        | 1           |          | Input is 1   |
| 01  | sto 99     | 1           | #99 = 1  |              |
| 02  | inp        | 1           |          | input is 3   |
| 03  | sto 98     | 1           | #98 = 3  |              |
| 04  | out        |             |          |              |
| 05  | brz 08     |             |          |              |
| 06  | sub 99     |             |          |              |
| 07  | bra 04     |             |          |              |
| 04  | out        |             |          |              |
|     |            |             |          |              |
|     |            |             |          |              |
|     |            |             |          |              |
| etc | etc        | etc         | etc      | etc          |


## Opdracht 5

We kunnen nu onze fibonaccie reeks programma afmaken.

Schrijf een LMC programma dat vraagt om 4 inputs:
De twee start waardes.
De hoogte van de counter.
De stap grootte van de counter. (standaard is dat 1)

Het programma geeft als ouput de gewenste hoeveel getallen van de fibonaccie reeks, aangegeven via de counter.