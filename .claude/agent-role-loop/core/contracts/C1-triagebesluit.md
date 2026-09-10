# C1 - Triagebesluit

De orkestrator schrijft dit compacte besluit zelf volgens [loop.md](../loop.md).
Een aparte triage-agent is alleen nodig op verzoek. Invoer: C0 en relevante
staande zaken. Een verantwoordelijkheid hoeft geen aparte agent te zijn.

## Schema

- **Besluit:** `LUS`, `DOORLOPEND` of `AFWIJZEN`.
- **Reden:** hooguit drie zinnen.
- **Omvang:** XS / S / M / L / XL; zegt hoe diep, niet hoeveel agents.
- **Procesversie:** commit van de instructies bij de start. Een lopende route
  verandert niet halverwege.
- **Rollen en uitvoering:** verplicht bij LUS. Noem de verantwoordelijkheden in
  volgorde, de uitvoerende agents, de mens waar nodig en de reden voor extra
  rollen. Benoem een gecombineerde verkenner/ontwerper expliciet.
- **Criteriumtoewijzing:** ieder bekend criterium naar minstens één passende
  beoordelaar. Uitwerkingen nooit bij uitsluitend de eerstejaars. Als C2 nieuwe
  criteria toevoegt, vul dit aan vóór beoordeling. Markeer nog af te leiden
  criteria als zodanig; dat is geen vrijstelling van uiteindelijke dekking.
- **Uitvoeropdracht:** bij de kleine route: doel, bestanden, eindvoorwaarden en
  verificatie uit C0 + C1. Bij een ontwerp: C2 volgt; geen leeg C2 maken.
- **Menselijk besluit:** nodig/vastgelegd/niet nodig, met reden en bron.
- **Herstelstand:** bij start nul per ontwerp en oplevering; volgende rondes en
  besluiten worden op GitHub geregistreerd volgens loop.md.
- **Proefafspraken:** verwijzing indien dit een #203-proef is, anders `<geen>`.
- **Advies:** verplicht bij AFWIJZEN, anders `<geen>`.

DOORLOPEND blijft open als verzamelplek. AFWIJZEN adviseert een kleinere opdracht
of handwerk. Een nieuwe inhoudelijke keuze vraagt de mens, niet automatisch
alle agents. De beslisregels voor extra rollen staan uitsluitend in loop.md.
