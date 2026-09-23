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

## Proef 1 vastgelegd: de handleidingen van week 5 en 6 zonder ontwerpstap

Vastgesteld door de vakdeskundige op 21 september 2026, op voorstel van de
orkestrator. Dit is de S/M-proef uit de fasering hierboven.

**De aanleiding is een waarneming en geen theorie.** Bij #256 - week 4 op de norm
brengen - liep een volledige ontwerpstap met een herstelronde, terwijl er al twee
handleidingen op die norm lagen. Wat de ontwerper deed was het model van week 3
nalopen en op week 4 toepassen. De vakdeskundige verwoordde het zo: *"issue 256
leest als overkill (lusresultaten) voor een eenvoudige stap"*. De ontwerpstap is
bij deze vorm van werk het duurste onderdeel en het minst onderscheidende.

**Wat de route wordt.** Voor `handleidingen/week_5.md` en `week_6.md`: C0 en C1,
dan meteen de auteur, dan de poort bij de vakdeskundige, dan één beoordelaar.
Geen `rol-curriculumontwerper`.

De auteur krijgt `handleidingen/week_3.md` en `week_4.md` als model en meet de
blokschema's zelf; hij levert ze als voorstel op, met de herkomstmerken erbij.

**Wat er niet verdwijnt.** De poort en de beoordeling blijven allebei, en dat is
met opzet - het zijn niet de dure stappen, en ze hebben zich in dit werk bewezen.
Bij #256 was het menselijke poortbesluit inhoudelijk beter dan het ontwerpvoorstel
(de oefenmidterm gaat naar het practicum omdat de midterm in week 5 valt), en bij
#237 ving de beoordelaar twee aantoonbare onwaarheden in de opgeleverde tekst.
De eis dat elk tijdsblok zijn herkomst draagt blijft eveneens staan; die ving bij
#237 een telfout die door drie artefacten heen was gelopen.

| Afspraak | Invulling |
|---|---|
| Issue en uitvoerautorisatie | nieuw werkitem onder #95 voor week 5; week 6 volgt als de proef houdt |
| Omvang, bestanden en criteria | M; `handleidingen/week_5.md`, plus `curriculum/uitgangspunten.md` als de poort een afwijking vaststelt; de acht criteria van #256 |
| Route en controledekking | C0 + C1 → auteur → poort → één beoordelaar; toepasselijke pre-commit, geen Sphinx-build zolang `source/` onaangeroerd blijft |
| Historische referentie en motivering | **#256**, dezelfde soort werk op dezelfde norm, met dezelfde criteria en dezelfde controledekking. Te verkiezen boven #237, want #237 moest de norm zelf nog uitvinden |
| Procescommit, model en meetdefinitie | bij start |
| Referentietotaal en 70%-grens | **693.462** agenttokens (#256); de 70%-grens is **485.423** |
| Verantwoordelijke vakdeskundige voor latere lezing/les | de vakdeskundige |

**Wat deze proef kan aantonen, en wat niet.** Zij vergelijkt twee werkitems, geen
twee methoden: week 5 en week 6 zijn andere weken dan week 4, met ander materiaal
en een andere hoeveelheid bron. Een lager totaal bewijst dus niet dat de
ontwerpstap overbodig is, alleen dat deze route voor dit soort werk goedkoper
uitviel. Het omgekeerde is even informatief: komt de beoordelaar met blokkades
waar #256 er geen had, dan heeft de ontwerpstap gedaan waarvoor zij bestond.

### Uitkomst van proef 1, 24 september 2026

| Werkitem | Agenttokens | t.o.v. #256 | Doel (≥ 30% minder) | Beoordeling |
|---|---:|---:|---|---|
| #256, week 4 (referentie, met ontwerpstap) | 693.462 | 100% | - | AKKOORD MET PUNTJES, 0 blokkades |
| #276, week 5 | 502.819 | 72,5% | **niet gehaald** (27,5%) | **BLOKKEER** op 2 fouten; na één herstel AKKOORD |
| #280, week 6 | 470.035 | 67,8% | gehaald (32,2%) | AKKOORD MET PUNTJES, 0 blokkades |

**Bron.** De getallen zijn de cumulatieve `subagent_tokens` uit het
verbruiksrapport dat de orkestrator na elke agentstap krijgt, inclusief herstel-
en naleesronden. De rollen zelf zien hun teller niet en schreven *"niet
beschikbaar"*; de rapportgetallen zijn op 24 september 2026 als aanvulling op
#276 en #280 geplaatst. Orkestratie zit in geen van de drie totalen.

**Drie afwijkingen van wat hier vooraf staat.**
- Het referentietotaal had vóór de start bevestigd moeten zijn; het is achteraf
  ingevuld, uit de meting van #256.
- De budgetreactie is bij #276 niet uitgevoerd. Na het auteursherstel stond de
  stand op 495.117 (71,4%); de herbeoordeling is gestart zonder de vakdeskundige
  te vragen.
- Het totaal van #280 bevat 28.482 beoordelaarstokens voor het nalezen van
  orkestratorcommits. Bij #256 las geen rol de correcties van de orkestrator. De
  twee totalen zijn op dat punt niet gelijk opgebouwd.

**Wat de getallen zeggen.** Beide proeven waren goedkoper dan de referentie;
#280 haalde het doel, #276 niet. De besparing komt uit het weglaten van de
ontwerpstap (215.006 tokens bij #256). De auteur werd daarbij **duurder**: 343.145
bij #276 en 293.226 bij #280, tegen 280.463 bij #256 - hij deed een deel van het
ontwerpwerk zelf.

**Wat de proef vooraf als tegenbewijs aanwees, en wat er gebeurde.** Hierboven
staat: *"komt de beoordelaar met blokkades waar #256 er geen had, dan heeft de
ontwerpstap gedaan waarvoor zij bestond."* Bij #276 gebeurde dat. De twee fouten
waren een voorspelde uitvoer die niet klopte en een telling over te weinig
bestanden; of een ontwerpstap die had voorkomen, laat de proef niet zien. Na de
les daaruit in de opdracht van #280 kwamen ze niet terug.

**De vakdeskundige.** Bij #256 veranderde het poortbesluit de indeling; bij #276
deed een aanvulling van de vakdeskundige tijdens het schrijven dat (de derde
bijeenkomst is het tentamen). Beide keren op grond van informatie die in geen
enkel artefact stond. Bij #280 bevestigde de poort het voorstel.

**Besluit over voortzetting** ligt bij de vakdeskundige. De proef geeft gemengde
uitkomsten: één keer het doel gehaald zonder blokkade, één keer niet gehaald met
een blokkade.

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
