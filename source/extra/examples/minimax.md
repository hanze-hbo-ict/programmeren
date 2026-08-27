# Minimax

## Het Minimax Algoritme Uitgelegd

Het minimax algoritme wordt vooral gebruikt in spellen waar twee spelers tegen elkaar spelen, zoals schaak of boter-kaas-en-eieren. Het idee is dat één speler probeert te winnen (maximaliseren) terwijl de andere speler probeert te voorkomen dat dit gebeurt (minimaliseren).

Stel je voor dat je schaakt. Bij elke beurt:

1. Kijk je naar alle mogelijke zetten die je kunt doen
2. Voor elke zet kijk je naar alle mogelijke tegenzetten van je tegenstander
3. Dit ga je een aantal stappen diep door
4. Aan het einde geef je elke situatie een score
5. Je kiest de zet die uiteindelijk tot de beste score leidt

Laten we dit visualiseren met een eenvoudig voorbeeld:

```{md-mermaid}
graph TD
    A[A: MAX] --> B[B: MIN]
    A --> C[C: MIN]
    B --> D[D: MAX<br/>Score: 3]
    B --> E[E: MAX<br/>Score: 5]
    C --> F[F: MAX<br/>Score: 2]
    C --> G[G: MAX<br/>Score: 8]

    %% propagatie van waarden
    D -- "3" --> B
    E -- "5" --> B
    F -- "2" --> C
    G -- "8" --> C
    B -- "3" --> A
    C -- "2" --> A

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#dfd,stroke:#333,stroke-width:2px
    style E fill:#dfd,stroke:#333,stroke-width:2px
    style F fill:#dfd,stroke:#333,stroke-width:2px
    style G fill:#dfd,stroke:#333,stroke-width:2px
```

In dit voorbeeld:

- De MAX speler (bijvoorbeeld jij) begint bovenaan
- De MIN speler (je tegenstander) is het niveau eronder
- De getallen onderaan zijn de scores van elke eindpositie
- Bij MAX-nodes kies je het hoogste getal
- Bij MIN-nodes kiest je tegenstander het laagste getal

## Alpha-Beta Pruning

Nu komt het slimme deel: alpha-beta pruning. Dit is een techniek om veel sneller tot dezelfde beslissing te komen, door takken van de boom te "snoeien" die we toch nooit zullen kiezen.

Laten we dit visualiseren:

```{md-mermaid}
graph TD
    A[A: MAX<br/>α=-∞ β=∞] --> B[B: MIN<br/>α=3 β=∞]
    A --> C[C: MIN<br/>α=3 β=∞]
    B --> D[D: MAX<br/>Score: 3]
    B --> E[E: MAX<br/>Score: 5]
    C --> F[F: MAX<br/>Score: 2]
    C --> G[G: MAX<br/>❌ Gesnoeid]

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#dfd,stroke:#333,stroke-width:2px
    style E fill:#dfd,stroke:#333,stroke-width:2px
    style F fill:#dfd,stroke:#333,stroke-width:2px
    style G fill:#fdd,stroke:#333,stroke-width:2px

```

Hoe werkt alpha-beta pruning?

- Alpha (α) is de beste score die MAX tot nu toe heeft gevonden
- Beta (β) is de beste score die MIN tot nu toe heeft gevonden
- Als we een tak tegenkomen die nooit gekozen zal worden (omdat er al een betere optie is), dan kunnen we die tak "snoeien"

In het voorbeeld hierboven:

1. We beginnen bij A met α=-∞ en β=∞
2. We verkennen tak B:
   - D geeft score 3
   - E geeft score 5
   - B kiest dus 5 (MIN kiest altijd het laagste)
3. We gaan naar tak C:
   - F geeft score 2
   - We weten dat MIN bij B al 5 heeft gekozen
   - Als we nu een score > 5 vinden bij G, zal MIN deze tak toch nooit kiezen
   - Dus kunnen we G overslaan (snoeien)

Het voordeel van alpha-beta pruning is dat je veel minder posities hoeft te evalueren, terwijl je exact dezelfde beslissing neemt. In grote spellen zoals schaak kan dit het verschil zijn tussen secondes of uren rekentijd!

## Boter-kaas-en-eieren

```{md-mermaid}
graph TD
    A["Start<br/>□ □ □<br/>□ X □<br/>□ □ □<br/>[MAX]"] --> B["□ □ O<br/>□ X □<br/>□ □ □<br/>[MIN]"]
    A --> C["□ □ □<br/>□ X □<br/>□ □ O<br/>[MIN]"]

    B --> D["□ □ O<br/>□ X □<br/>X □ □<br/>[MAX]"]
    B --> E["□ □ O<br/>□ X □<br/>□ X □<br/>[MAX]"]

    C --> F["X □ □<br/>□ X □<br/>□ □ O<br/>[MAX]"]
    C --> G["□ □ X<br/>□ X □<br/>□ □ O<br/>[MAX]"]

    D --> H["□ □ O<br/>□ X O<br/>X □ □<br/>Score: -1"]
    D --> I["O □ O<br/>□ X □<br/>X □ □<br/>Score: 0"]

    E --> J["□ □ O<br/>O X □<br/>□ X □<br/>Score: 1"]

    F --> K["X □ O<br/>□ X □<br/>□ □ O<br/>Score: 1"]

    G --> L["□ □ X<br/>□ X O<br/>□ □ O<br/>Score: 0"]

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#f9f,stroke:#333,stroke-width:2px
    style F fill:#f9f,stroke:#333,stroke-width:2px
    style G fill:#f9f,stroke:#333,stroke-width:2px
    style H fill:#dfd,stroke:#333,stroke-width:2px
    style I fill:#dfd,stroke:#333,stroke-width:2px
    style J fill:#dfd,stroke:#333,stroke-width:2px
    style K fill:#dfd,stroke:#333,stroke-width:2px
    style L fill:#dfd,stroke:#333,stroke-width:2px

```

Laten we dit voorbeeld stap voor stap doornemen:

1. **Uitgangssituatie**
   - We beginnen met een X in het midden (speler MAX)
   - O is aan zet (speler MIN)
   - De lege vakjes zijn aangegeven met □

2. **Scores**
   - +1: Als MAX (X) wint
   - -1: Als MIN (O) wint
   - 0: Bij gelijkspel of tussenposities

3. **Hoe werkt het proces?**
   - MIN (O) heeft in dit voorbeeld twee logische eerste zetten: rechtsboven of rechtsonder
   - Voor elke zet van MIN kijkt MAX naar zijn mogelijke tegenzetten
   - Dit proces gaat door tot we een eindsituatie bereiken

Laten we nu zien hoe alpha-beta pruning hier kan helpen:

```{md-mermaid}
graph TD
    A["Start<br/>□ □ □<br/>□ X □<br/>□ □ □<br/>α=-∞ β=∞"] --> B["□ □ O<br/>□ X □<br/>□ □ □<br/>α=-∞ β=1"]
    A --> C["□ □ □<br/>□ X □<br/>□ □ O<br/>❌ Gesnoeid"]

    B --> D["□ □ O<br/>□ X □<br/>X □ □<br/>α=0 β=1"]
    B --> E["□ □ O<br/>□ X □<br/>□ X □<br/>α=1 β=1"]

    D --> H["□ □ O<br/>□ X O<br/>X □ □<br/>Score: -1"]
    D --> I["O □ O<br/>□ X □<br/>X □ □<br/>Score: 0"]

    E --> J["□ □ O<br/>O X □<br/>□ X □<br/>Score: 1"]

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#fdd,stroke:#333,stroke-width:2px
    style D fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#f9f,stroke:#333,stroke-width:2px
    style H fill:#dfd,stroke:#333,stroke-width:2px
    style I fill:#dfd,stroke:#333,stroke-width:2px
    style J fill:#dfd,stroke:#333,stroke-width:2px

```

In dit voorbeeld van alpha-beta pruning:

1. Na het verkennen van tak B vinden we dat MIN daar maximaal een score van 1 kan behalen
2. Als we dan bij tak C beginnen, weten we dat:
   - MAX al een pad heeft gevonden dat minstens 1 oplevert
   - Als MIN slim speelt, zal deze tak nooit gekozen worden
3. Daarom kunnen we de hele tak C (en alle onderliggende posities) overslaan

Praktische voordelen voor boter-kaas-en-eieren:

- In een echt spel zijn er ongeveer 255.168 mogelijke spelposities
- Met alpha-beta pruning hoef je maar een fractie hiervan te evalueren
- Dit maakt het mogelijk om in milliseconden de beste zet te bepalen

Dit voorbeeld laat ook zien waarom een X in het midden een sterke openingszet is: het geeft MAX (X) de meeste mogelijkheden om later drie-op-een-rij te maken, terwijl het MIN (O) dwingt om defensief te spelen.

Wil je dat ik nog dieper inga op bepaalde aspecten van het algoritme of heb je interesse in hoe dit zou werken voor andere spellen?

## Genetisch algoritme

```{md-mermaid}
flowchart TD
    A[Initiële Populatie] -->|Genereer willekeurig| B[Evaluatie]
    B --> C{Fitness Check}
    C -->|Goede dekking| D[Selectie]
    C -->|Slechte dekking| E[Eliminatie]
    D --> F[Crossover]
    D --> G[Mutatie]
    F --> H[Nieuwe Generatie]
    G --> H
    H --> B
```

1. **Wat is een genetisch algoritme?**
   Het is een programmeertechniek die geïnspireerd is door natuurlijke evolutie. Net zoals in de natuur organismen evolueren om beter aangepast te raken aan hun omgeving, kunnen we computerprogramma's laten "evolueren" om beter te worden in een taak.

2. **Toepassing op Picobot:**
   - Een "individu" is een complete verzameling regels
   - Elke regel heeft het format: `huidige_staat omgeving -> nieuwe_staat beweging`
   - Een "populatie" is een verzameling van verschillende reeksen regels

3. **Het evolutieproces:**
   - **Initiële populatie**: We beginnen met willekeurig gegenereerde verzamelingen regels
   - **Evaluatie**: We testen elke verzameling:
     - Hoeveel % van de ruimte wordt bezocht?
     - Hoeveel stappen zijn nodig?
     - Hoe efficiënt zijn de regels?

4. **Evolutionaire operatoren:**
   - **Selectie**: De beste verzamelingen regels krijgen een hogere kans om "ouder" te worden
   - **Crossover**: We combineren regels van twee goede verzamelingen
     - Bijvoorbeeld: de eerste helft van verzameling A met de tweede helft van verzameling B
   - **Mutatie**: We maken kleine willekeurige aanpassingen
     - Bijvoorbeeld: een bewegingsrichting veranderen van N naar O

5. **Optimalisatieproces:**
   - Dit proces herhaalt zich voor meerdere generaties
   - Elke generatie wordt gemiddeld beter dan de vorige
   - Uiteindelijk vinden we verzamelingen regels die de ruimte efficiënt kunnen verkennen

Waarom is een een genetisch algoritme interessant?

- Dit is een voorbeeld van hoe we natuurlijke processen kunnen gebruiken als inspiratie voor probleemoplossing
- Het laat zien dat computers zelf oplossingen kunnen vinden zonder dat wij expliciet programmeren wat ze moeten doen
- Het demonstreert hoe kleine, willekeurige veranderingen gecombineerd met selectie kunnen leiden tot complexe, effectieve oplossingen

Zou je geïnteresseerd zijn in meer details over een specifiek aspect van dit proces? Bijvoorbeeld hoe we precies de fitness berekenen of hoe we crossover implementeren?
