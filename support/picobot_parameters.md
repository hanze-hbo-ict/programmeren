# Picobot-parameters

Zelfs als alles goed geïmplementeerd is, is het nog een soort van kunst om te zorgen dat genetische algoritmes een oplossing voor een bepaald probleem goed evolueren. (Als dit makkelijk zou zijn, zouden alle oplosbare problemen al opgelost zijn!)

Voor Picobot vind je hier een aantal strategieën die handig kunnen zijn; dit is geen garantie dat ze voor jou werken, maar ze zijn het overwegen waard!

## Aantal overlevende programma's

Neem altijd de beste 10% van je populatie mee in de volgende generatie: op deze manier kan de maximale fitness niet zoveel afnemen; het kan een beetje afnemen doordat de posities waarmee getest wordt willekeurig zijn, maar dat kan nooit veel zijn. Het kan meer afnemen als je deze "oude" programma's ook laat muteren, dat mag je zelf bepalen.

Vul de andere 90% met kinderen van willekeurig gekozen ouders vanuit de top 10%. Je kan er ook voor kiezen om een meer kandidaat-ouders te gebruiken, die dus zelf niet overleven.

!!! notice "Dezelfde ouders"
    Als je willekeurig ouders kiest kan het gebeuren dat een bepaald kind twee keer dezelfde ouder heeft; dat is best. Crossover zal hier geen verandering geven, maar dat betekent alleen maar dat er twee kopieën van de ouder in de nieuwe generatie zitten, maar dat kan geen kwaad. Als er dan mutatie optreedt, dan is het resultaat een variatie van de oorspronkelijke ouder, en dat is ook best.
    
## Mutaties

Muteer bijvoorbeeld een derde van de populate die je op deze manier maakt (op maar één regel, en alleen met een geldige nieuwe verplaatsing en misschien een nieuwe toestand). De *meeste* mutaties zijn fataal voor de programma's die ze krijgen, maar dit is niet altijd zo. Zonder mutaties is er geen manier om iets beters te krijgen dan wat er aanwezig was in de oorspronkelijke genenpoel.


## Toestanden

Als je vast zit op 12% of 17%, kan het zijn dat je een fout hebt waardoor de toestand nooit wijzigt. Probeer eens alle toestanden die tijdens een test langskomen af te drukken...

## Het doolhof

Het is moeilijk, tot zelfs onmogelijk, om een programma te evolueren die het doolhof oplost. Er is eenvoudigweg niet genoeg ruimte om de zoektocht te laten werken: er is steeds maar één "goede" verplaatsing en de rest zijn "fout". Evolutie gaat deze vermoedelijk niet vinden, aangezien je niet kan zeggen dat de oplossing "steeds een beetje beter" wordt...

In ruimtes met veel open ruimte is het wel mogelijk om geleidelijke aanpassingen te maken die naar een bijna volledige oplossing leiden. Volledige oplossingen zijn zeldzaam, maar het is goed mogelijk om de 80% voorbij te gaan en zelfs boven de 90% kan voorkomen.

Succes met je Picobot-populaties!
