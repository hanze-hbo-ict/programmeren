# Proef: efficiëntere rollenlus (#203)

## Besluit en status

De vakdeskundige heeft op 10 september 2026 expliciet **akkoord** gegeven op het
[besluitpakket](https://github.com/hanze-hbo-ict/programmeren/issues/203#issuecomment-5625179565).
Het [C4](https://github.com/hanze-hbo-ict/programmeren/issues/203#issuecomment-5625217193)
registreert dat akkoord. Het voorafgaande ontwerp kreeg een onafhankelijke
[C3 AKKOORD](https://github.com/hanze-hbo-ict/programmeren/issues/203#issuecomment-5625173128).

**Goedgekeurd:** kleinere routes, gerichte besluit-/bewijsoverdracht en herstel,
maximaal één automatische herstelronde per ontwerp en oplevering, het proefdoel
van 30% minder tokens en de budgetreactie hieronder. De gedeelde uitvoerregels
staan in [loop.md](../.claude/agent-role-loop/core/loop.md).

**Nog niet uitgevoerd:** merge van de instructies, de twee praktijkproeven en
het evaluatiebesluit. De instructie-PR verwijst naar #203 en sluit het niet.
Een wijziging in instructies is geen bewijs dat kosten of kwaliteit verbeterden.

## Fasering

Eerst worden besluit-/bewijsoverdracht en gericht herstel aangepast; vervolgens
wordt de kleinere route beproefd op twee nieuw gestarte werkitems, één S/M en één
L. Binnen de proeven geldt het hele gewijzigde proces. Met twee proeven valt het
effect van individuele maatregelen niet te isoleren.

Kies geen lopende route. Haar startcommit en C1 blijven leidend. De proefissues
en hun materiaalwerk vragen eigen autorisatie. #203 is geen opdracht om alvast
een lesweek te wijzigen. Modelkeuze verandert niet als onderdeel van deze proef.

## Vooraf vastleggen per proef

De orkestrator stelt voor, de vakdeskundige bevestigt vóór de start:

| Afspraak | Proef S/M | Proef L |
|---|---|---|
| Issue en uitvoerautorisatie | nog te kiezen | nog te kiezen |
| Omvang, bestanden en criteria | nog vast te stellen | nog vast te stellen |
| Route en controledekking | nog vast te stellen | nog vast te stellen |
| Historische referentie en motivering | nog te kiezen | nog te kiezen |
| Procescommit, model en meetdefinitie | bij start | bij start |
| Referentietotaal en 70%-grens | niet vastgesteld | niet vastgesteld |
| Verantwoordelijke vakdeskundige voor latere lezing/les | vóór start aanwijzen | vóór start aanwijzen |

Kies geen referentie alleen omdat zij duur is. Vergelijk omvang, verantwoordelijkheden,
geleverde artefacten en controledekking. Een onvolledig beoordeelde historische
run is geen referentie voor dezelfde kwaliteit zonder dat verschil te benoemen.

## Meten en reageren

De orkestrator registreert na iedere agentstap de beschikbare tokens, duur,
uitkomst, herstelstand en cumulatieve stand op GitHub. Tel in beide totalen
intake, eventuele leesronde, ontwerp, uitvoering, beoordeling en herstel mee.
Afgebroken runs meetellen voor zover beschikbaar; onbekend blijft onbekend.

Houd eenmalige invoeringskosten van #203 apart van de proefwerkitems en rapporteer
ze wel. Orkestratietokens worden apart gerapporteerd indien beschikbaar; bij
vergelijking alleen meenemen als beide zijden ze bevatten. Agentminuten zijn
geen doorlooptijd; beoordelingen kunnen parallel lopen. Menselijke leestijd
alleen als gemeten, anders niet beschikbaar. Invoer, uitvoer en cachegebruik
alleen onderscheiden als de bron die gegevens geeft. Geen factuurclaims.

**Doel:** per proefwerkitem ten minste 30% minder vergelijkbaar geregistreerde
agenttokens dan de vooraf bevestigde referentie. Een verschillende meetdefinitie
bij Claude en Codex maakt een percentage ongeldig: noteer niet vast te stellen.

**Budgetreactie:** controleer na iedere agentstap of het cumulatieve meetbare
gebruik meer dan 70% van de referentie bedraagt. Zo ja: leg de stand vast en
vraag vóór een volgende agentstart een keuze van de mens: gericht doorgaan met
een herziene grens, scope splitsen of stoppen. Breek geen lopende stap af en
negeer geen kwaliteitsblokkade. De herziene grens en opdracht staan op GitHub.
Bij ontbrekende of onvergelijkbare metingen is deze tokencontrole niet uitvoerbaar;
de rondelimiet blijft gelden en er is geen vastgesteld besparingspercentage.

De rondelimiet geldt volgens loop.md, onafhankelijk van de tokenmeting. Een
nieuwe sessie of agent zet de teller niet terug. Een overschrijding maakt een
onvoltooide taak niet voltooid.

## Kwaliteit en evaluatie

Registreer per proef terechte blokkades, unieke bevindingen per beoordelaar,
herstelwerk en later ontdekte defecten. De vakdeskundige organiseert de
waarneming bij de eerstvolgende reguliere lezing of les; de orkestrator neemt
de uitkomst met bron over. Geen afzonderlijke volledige schaduwrollenlus.

Evalueer uiterlijk twee weken na de tweede proefoplevering. Was er nog geen
praktijkwaarneming, noteer dat als ontbrekende kwaliteitstoets, niet als nul
fouten. Een gemiste blokkerende fout die samenhangt met een vervallen
verantwoordelijkheid leidt tot terugzetten van die verantwoordelijkheid vóór
verdere toepassing.

De vakdeskundige neemt één afsluitend besluit: invoeren, gericht bijstellen of
terugvallen. Leg bij bijstellen een eindige wijzigingslijst vast. Geen automatische
extra proefreeks of procesrondes. Twee proeven bewijzen geen gelijkblijvende
kwaliteit. De issue sluit pas als dit besluit en de vereiste vervolghandelingen
zijn afgerond.

## Uitgangsmeting

Onderstaande samenvatting is als
[C1b](https://github.com/hanze-hbo-ict/programmeren/issues/203#issuecomment-5625172571)
gepubliceerd. Rijsommen uit `onderzoek/metingen.md`, op 10 september 2026 met een
Python-berekening: per tabel de numerieke tokenkolom lezen, punten verwijderen en
per fase optellen. Niet-numerieke waarden zijn niet als nul behandeld.

| Werkitem | Triage | Verkenner | Ontwerp/verheldering | Auteur | Beoordeling/samenvoeging | Bekende som |
|---|---|---|---|---|---|---|
| #103 | 12.611 | 157.971 | 719.262 | 342.577 | overgeslagen | 1.232.421 |
| #134 | 42.380 | 141.279 | 788.388 | 390.309 | 1.301.354 | 2.663.710 |
| #146 | 29.310 | 200.139 | 248.455 | 195.211 | 452.919 | 1.126.034 |
| #178 | 40.544 | 103.214 | 365.148 | 1.256.891 | 1.206.774 | 2.972.571 |

- #103: vier ontwerp-/verhelderaarrondes, twee afgebroken runs zonder tokenmeting,
  eindbeoordeling overgeslagen. Geen volledige kwaliteitsbaseline.
- #134: vier ontwerprondes, twee auteursrondes en twee beoordelingsrondes. De mens
  wijzigde ook inhoudelijke uitgangspunten; niet alle herhaling is procesverlies.
- #146: drie van negen ontworpen onderdelen opgeleverd. Voorafgaande leesronde
  van 194.900 tokens niet opgenomen in deze tabel.
- #178: twee ontwerp-/verhelderaarrondes, vier auteursrondes en twee beoordelingen;
  gestopt zonder laatste beoordeling. Tien materiaalcriteria waren volgens de
  registratie na auteursronde twee gehaald; vervolgrondes betroffen de normtekst.

De lopende tekst noemt bij #103 circa 1,13M en 718k waar de rijsommen 1.232.421 en
719.262 geven. Bij #146 noemt zij 453.919 voor de reviewers, waar de rijen 452.919
geven. Bij #134 is ronde twee 668.887 voor de reviewers en 686.492 inclusief
hoofdredacteur. Historische tekst is niet stilzwijgend herschreven.

Volgens de registratie vond bij #146 alleen de eerstejaars de omgekeerde uitleg
van `while`. Bij #134 bevestigt het oorspronkelijke
[C4](https://github.com/hanze-hbo-ict/programmeren/issues/134#issuecomment-5496335568)
de bewuste afhankelijkheid van #102; die beslissing ontbrak bij de reviewers.
Er waren ook twee terechte blokkades, dus de gehele tweede ronde is geen bewezen
vermijdbare kostenpost. Bij #178 ondersteunen het
[C7 van ronde twee](https://github.com/hanze-hbo-ict/programmeren/issues/178#issuecomment-5605471805)
en het [afsluitbericht](https://github.com/hanze-hbo-ict/programmeren/issues/178#issuecomment-5606430813)
de analyse van doorgroeiend herstel rond normtekst. De lus vond ook terechte
fouten, waaronder twintig labels in codecommentaar die de hook miste.

Niet vastgesteld: volledige unieke opbrengst per reviewer, tokenverdeling naar
cache/invoer/uitvoer, factuurkosten, menselijke leestijd en systematische latere
defecten. De oorspronkelijke issues #134/#178 zijn gericht geraadpleegd; niet
iedere historische tokenregel is zelfstandig geverifieerd. Dit is een
reproduceerbare samenvatting van de registratie, geen nieuwe meting van die runs.
