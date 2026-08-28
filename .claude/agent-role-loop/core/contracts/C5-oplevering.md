# C5 - Oplevering

## Doel

Het verslag van de auteur over wat er is gemaakt en hoe het is aangetoond, in twee
delen met een verschillend publiek. De **kern** gaat naar elke beoordelaar: net
genoeg om het werk op eigen merites te beoordelen, zonder de geschiedenis van het
maken. Het **uitgebreide** deel gaat alleen naar de hoofdredacteur: het
bewijsspoor, de afwijkingen en de losse eindjes.

Die scheiding is wat de contexten van de beoordelaars schoon houdt. Een
beoordelaar die heeft gezien waar de auteur mee worstelde, beoordeelt de
worsteling mee.

## Voorwaarde vooraf

De mechanische controles zijn groen **voordat** deze oplevering wordt gemaakt:

```sh
uv run pre-commit run --files <gewijzigde bestanden>
uv run make html
```

Die controles zijn een toegangsvoorwaarde tot de beoordeling, geen onderdeel
ervan. Beoordelingsaandacht besteden aan wat een hook al vaststelt, is
verspilling.

## Schema

### Kern (naar alle beoordelaars)

- **Samenvatting** - 2 tot 5 punten over wat er is veranderd.
- **Gewijzigde bestanden** - lijst.
- **Dekking van de acceptatiecriteria** - de genummerde criteria uit het ontwerp,
  elk met waar het is gerealiseerd.
- **Wat dit raakt buiten deze week** - of `<geen>`.

### Uitgebreid (alleen naar de hoofdredacteur)

- **Verificatie** - wat er draait en wat het aantoont, volgens het gekozen model.
- **Bewijs vooraf** - de fout of het gemis zoals vastgesteld vóór de wijziging.
  Bij lesmateriaal is dat vaak de meting uit de bevindingen.
- **Bewijs achteraf** - het commando of de uitvoer die aantoont dat het nu klopt.
- **Afwijkingen van het ontwerp** - of `<geen>`; elk met de reden.
- **Niet gedane vervolgen** - onderweg gevonden en bewust laten liggen, of
  `<geen>`.

## Voorbeeld

```md
## Kern

### Samenvatting
- Basis is nu tekstanalyse met dictionaries, in zes stappen.
- Twee tekstbestanden toegevoegd, één met de hand na te rekenen.
- De Rij van Conway is uit deze week verdwenen.

### Gewijzigde bestanden
- problems/7_basis.ipynb
- solutions/7_basis.ipynb
- problems/assets/teksten/kort.txt, vuurtoren.txt

### Dekking van de acceptatiecriteria
1. Basis opent met een concreet probleem - de context is auteurschap; zie de
   opening van `7_basis`.
2. De opstap dekt wat de basis vraagt - opdracht 10 is het telpatroon uit stap 3.
3. Conventies en schone build - hooks en build groen, zie uitgebreid.

### Wat dit raakt buiten deze week
- PGM2 week 4 verwijst nog naar de Rij van Conway; die blijft bereikbaar als
  losse opgave.

## Uitgebreid

### Verificatie
`assertions-draaien`. De uitwerking draait bij de build; 17 assertions.

### Bewijs vooraf
Basis was 453 woorden en dekte A3 met een getallenpuzzel; dictionaries kwamen er
niet in voor.

### Bewijs achteraf
`uv run make html` bouwt schoon, en de uitvoercel toont:
Woorden: 227 / Verschillende: 134 / Meest gebruikt: een / Eenmalig: 94

### Afwijkingen van het ontwerp
- De opgave heeft zes stappen in plaats van de vijf uit het ontwerp: het
  isoleren van woorden bleek een eigen stap te verdienen.

### Niet gedane vervolgen
- Het practicum heeft nog nul codecellen.
```
