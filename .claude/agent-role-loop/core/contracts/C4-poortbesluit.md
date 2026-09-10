# C4 - Poortbesluit

Het expliciete besluit van de mens. Een agent mag het registreren, niet verzinnen.
Invoer is C2 met eventueel C3, of een concrete uitvoeropdracht in C0 + C1 wanneer
een kleine wijziging een inhoudelijk besluit vraagt zonder ontwerp nodig te hebben.
Zie [loop.md](../loop.md) voor wanneer de poort nodig is.

## Schema

- **Besluit:** AKKOORD / HERZIEN / STOP.
- **Reden:** één korte alinea; registreer wat de mens heeft gezegd, geen nieuwe
  inhoudelijke rechtvaardiging namens hem.
- **Bron en opdrachtversie:** exact akkoord en het artefact waarop het slaat.
- **Vereiste wijzigingen:** verplicht bij HERZIEN, anders `<geen>`.
- **Genomen beslissingen:** antwoorden en gekozen afbakening.
- **Uitgestelde vragen:** expliciet veilig uitgesteld, of `<geen>`.
- **Waar vastgelegd:** inhoudelijke besluiten in `curriculum/` of `conventies/`,
  procesbesluiten in `onderzoek/`. Noem wat nog in de uitvoerings-PR wordt
  vastgelegd; het GitHub-besluit is de bron, geen vervanging van die registratie.
- **Vervolggrens:** bij hervatten na de rondelimiet: welke concrete vervolgopdracht
  en hoeveel extra rondes zijn toegestaan. Anders geldt de grens in loop.md.

## Checklist

Is het doel juist, de afbakening aanvaardbaar, het eindpunt toetsbaar en het
verificatieplan geloofwaardig? Zijn gevolgen buiten het werkitem benoemd, open
vragen beantwoord of veilig uitgesteld, en kan de auteur werken zonder nieuwe
eisen te verzinnen? Wordt materiaal verwijderd, is dat dan expliciet bedoeld?

Een reeds gegeven expliciet akkoord wordt vastgelegd; vraag het niet opnieuw.
Nieuwe inhoudelijke keuzes en werk buiten de goedgekeurde grens vragen wel een
nieuw besluit. De mens beslist over merge.
