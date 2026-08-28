# C7 - Eindoordeel

## Doel

De samengevoegde uitkomst van de beoordelingsronde, gemaakt door de
hoofdredacteur uit de vier onafhankelijke oordelen (C6) en de volledige
oplevering (C5). Het ontdubbelt bevindingen, lost tegenspraak expliciet op, en
zegt de auteur wat er nu gebeurt.

Vaste prioriteitsregel: **juistheid en dekking eerst, dan begrijpelijkheid voor de
student, dan onderhoudbaarheid, dan afwerking.**

## Schema

Alle velden van C6, met bevindingen ontdubbeld en geordend volgens de
prioriteitsregel, plus:

- **Tegenspraak tussen beoordelaars** - elk meningsverschil met de oplossing en de
  redenering; of `<geen>`.
- **Volgende stap voor de auteur** - één concrete instructie: mergen, de
  moet-lijst herstellen en opnieuw indienen, of terug naar de vakdeskundige.

## Regels

- Lever één samengevoegd oordeel, kort genoeg om naar te handelen.
- Je bent geen vijfde beoordelaar die opnieuw begint. Je ontdubbelt, prioriteert
  en beslist.
- Voeg geen eigen bevindingen toe, behalve waar het uitgebreide deel een aanname
  van een beoordelaar tegenspreekt.
- Los elke tegenspraak expliciet op. Middel nooit twee oordelen tot vaagheid.
- Een criterium is pas `gehaald` als geen enkele beoordelaar het geloofwaardig
  heeft afgekeurd.

## Voorbeeld

```md
Oordeel: AKKOORD MET PUNTJES

Moet veranderen: <geen>

Zou moeten veranderen:
- Leg in de uitwerking uit dat `>` en `>=` bij gelijkspel een ander woord
  opleveren (onderwijskundige en eerstejaars, samengevoegd).

Puntjes:
- De kop in de inhoudsopgave zegt alleen "Basis" (redacteur).

Dekking van de acceptatiecriteria:
- AC1: gehaald - door alle vier bevestigd.
- AC2: gehaald.
- AC3: gehaald - het uitgebreide deel toont de uitvoer van de build.

Tegenspraak tussen beoordelaars:
- De eerstejaars blokkeerde op stap 2, omdat leestekens verwijderen nergens is
  voorgedaan. Het uitgebreide deel laat zien dat de hint dat wél doet. Opgelost
  naar "zou moeten veranderen": de hint mag explicieter.

Volgende stap voor de auteur:
- Verwerk het punt over gelijkspel, dan mergen. De puntjes worden een werkitem.
```
