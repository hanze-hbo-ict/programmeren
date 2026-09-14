# Redactionele verantwoordelijkheid — #214

## Besluit

Op 14 september 2026 keurde de vakdeskundige de aanscherping van de bestaande
ontwerper, auteur en redacteur goed. Aanleiding was zijn ervaring bij de inleiding
van agent-role-loop: de tekst was verbeterd, maar bleef lang en herkenbaar als
AI-uitleg. Dit is een gebruikerswaarneming, geen meting van het Programmerenboek.
Werkitem en overdrachten staan op [#214](https://github.com/hanze-hbo-ict/programmeren/issues/214).

De ontwerper selecteert het doel, de uitleg en de stijlreferenties. De auteur
schrapt overbodige tekst en herstelt redactionele blokkades binnen de afgesproken
inhoudelijke grenzen. De redacteur beoordeelt het gewenste niveau, ook wanneer
de tekst ten opzichte van vroeger verbeterd is. De mens beslist over inhoud,
afbakening en merge. Er komen geen rollen of extra herstelrondes bij.

De schrijfwijzer verduidelijkt selectie naast structuur. Nieuwe werkitems nemen
de gewijzigde procesversie op in C1; lopende routes blijven bij hun vastgelegde
versie. De praktijkproeven van #203 veranderen hierdoor niet.

## Scenarioverificatie

Handmatig getoetst aan de gewijzigde contracten en rollen:

| Situatie | Verwachte route | Vindplaats en resultaat |
| --- | --- | --- |
| Een inleiding legt begrippen uit die pas later nodig zijn | Ontwerper benoemt benodigde begrippen en bestemming van latere uitleg | C2, redactionele uitgangspunten; aanwezig |
| Een regel staat tweemaal in de goedgekeurde sectie | Auteur schrapt herhaling zonder nieuwe poort; noodzakelijke inhoud blijft | Auteur, redactionele verantwoordelijkheid; schrijfwijzer, vorm; toegestaan |
| Het enige noodzakelijke voorbeeld dreigt te verdwijnen | Auteur vraagt een inhoudelijk besluit | Auteur, stopvoorwaarden; loop, Mens; beschermd |
| Een verbeterde passage hindert nog steeds de lezer | Redacteur benoemt passage, criterium/norm en gevolg; auteur herstelt volgens C6 | Beide rollen verwijzen naar bestaande herstelgrens; aanwezig |
| Een reviewer verkiest slechts een ander woord | Geen blokkade op smaak | Redacteur, regels; expliciet uitgesloten |
| Een typefout wordt hersteld | Geen uitgebreid ontwerp of stijldossier | C2 laat relevante afspraak in C0 + C1 volstaan; kleine route blijft |
| Een reviewer start zonder auteursgesprek | C5-kern bevat tekstdoel en vindbare referenties | C5, bij tekstwerk; geen maaktranscript |

Deze controle toont samenhang van instructies. Of de vakdeskundige minder hoeft
te redigeren is nog niet vastgesteld. Noteer bij volgend tekstwerk welke passages
hij alsnog moet aanpassen en waarom: selectie, formulering of inhoudelijk besluit.
Dat kan vervolgverbeteringen onderbouwen; er is nu geen vergelijkbare nulmeting.
