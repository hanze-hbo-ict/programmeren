# Geheugenproblemen

| Naam         | Beschrijving                                                                                          |
|--------------|-------------------------------------------------------------------------------------------------------|
| Onderwerp    | Geheugen met schakelingen                                                                             |
| Bestandsnaam | `wk6ex1-4.circ`                                                                                       |
| Inleveren    | Lever jouw bestand met de juiste bestandsnaam in op GradeScope                                        |
| Opmerking    | Dit is hetzelfde bestand dat je hebt gebruikt bij het [practicum](/problems/optellingen_schakelen.md) |
|              | **Dit is een bonusopgave**                                                                            |

Deze opgave wordt een nieuwe schakeling in het bestand `wk6ex1-4.circ`.

Als je graag nog meer schakelingen wilt ontwerpen, is hier een leuke en uitdagende opgave. Tijdens het college is besproken hoe een random-access memory (RAM) met vier 3-bit "words" werkt. Hier gaan we eerst de onderliggende schakelingen bouwen waarmee dit soort geheugen werkt (je krijgt hiervoor 3 bonuspunten), en daarna bouwen we de 12 bits geheugen zelf (je krijgt hier 12 extra bonuspunten voor).

## De 2-bit decoder

**1 bonuspunt**

Een 2-bit decoder is een schakeling die twee bits als invoer heeft en vier uitvoerpins. De invoerbits heten `Input0` en `Input1`, en de uitvoerbits heten `Output0`, `Output1`, `Output2` en `Output3`. Als de twee invoerbits `00` (in volgorde: `Input1` en `Input0`) zijn dan wordt `Output0` een `1` en de andere drie uitvoerbits `0`. Als de twee invoerbits `01` zijn dan wordt `Output1` een `1` en de andere drie uitvoerbits `0`. Als de twee invoerbits `10` zijn dan wordt `Output2` een `1` en de andere drie uitvoerbits `0`. Als ten slotte de twee invoerbits `11` zijn dan wordt `Output3` een `1` en de andere drie uitvoerbits `0`.

**Maak gebruik van het minterm-expansieprincipe** om een 2-bit decoder te bouwen in Logisim Evolution. Je mag alleen `AND`-, `OR`- en `NOT`-poorten gebruiken om de schakeling te maken, en deze moeten afgeleid zijn van het minterm-expansieprincipe. Er is al een deelschakeling genaamd `Een_2bit_decoder` aanwezig in het bestand `wk6evolution.circ` die je hebt gebruikt voor het practicum. Gebruik die voor het maken van je schakeling, en zorg dat je dezelfde namen voor de invoer- en uitvoerpins gebruikt die we hier beschreven hebben.

## De SR-latch

**1 bonuspunt**

Je kan een nieuwe schakeling maken via "Project" en "Add circuit" in het menu. Noem je schakeling "SR_Latch".

Maak een nieuwe schakeling en implementeer een SR-latch in Logisim Evolution door gebruik te maken van NOR-gates. Dit is de schakeling met twee NOR-poorten waarbij de uitvoer van beide de invoer van de andere is.

Het is de schakeling met de invoerpins "S" en "R" uit het college...

## De flip-flop

**1 bonuspunt**

Gebruik vervolgens je SR-latch om een D-latch of flip-flop te bouwen, zoals getoond op het college. Noem deze deelschakeling "Flip-flop".

## 12nGbits geheugen!

**12 bonuspunten** ... maar je krijgt niet direct één punt per bit!

Gebruik ten slotte je flip-flopschakeling om een compleet 4x3 == 12-bit RAM te maken. Het bestaat uit 4 adresseerbare geheugenlocaties met ieder drie bits.

Het RAM moet 2 bits invoer hebben om de 4 unieke geheugenlocaties aan te wijzen (gebruik hiervoor je 2-bit decoder!). Het moet 3 bits input voor de data, een 1-bit "read"-vlag en een 1-bit "write"-vlag. Ook moet je RAM 3 bits uitvoerdata hebben. Noem je deelschakeling "Een_12_nGb_geheugen" (12 nano-gigabits geheugen) in het bestand `wk6evolution.circ`. Die deelschakeling zou er al moeten zijn.

Denk erom dat je duidelijke namen gebruikt voor je invoer en uitvoer!

<!-- Als een richtlijn voor hoe je de schakeling zou kunnen indelen (en om je geheugen even te stimuleren!) zijn hier de afbeeldingen uit het college. De eerste toont hoe gegevens worden ***weggeschreven***, of opgeslagen, in het geheugen. De tweede toont hoe gegevens worden ***gelezen***, of geladen, uit het geheugen. Er staan ook een paar vragen bij die je misschien de goede weg op kunnen wijzen:

![Writing](TODO)

![Reading](TODO) -->
