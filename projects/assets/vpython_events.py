from visual import *

scene.range = 8  # vaste grootte, geen automatisch zoomen

arr = arrow(pos=(2, 0, 0), axis=(0, 5, 0))  # maak een pijl met de naam arr
by = 0.5  # je moet zo dicht bij de punt of staart klikken
drag = None  # nog geen punt of staart van de pijl geselecteerd

while True:

    #
    # DE PIJL LATEN BEWEGEN
    #
    rate(100)
    arr.pos.x += 0.01
    if arr.pos.x > 5:
        arr.pos.x = -5  # om de rand wrappen...

    #
    # TOETSAASLAGEN AFHANDELEN
    #
    if scene.kb.keys:  # is er nog een toetsaanslag die afgehandeld moet worden?
        s = scene.kb.getkey()  # haal informatie van het toetsenbord
        if len(s) > 0:
            print("Toetsaanslag", s)
            if s == 'up':
                print("That was the up arrow!")

    #
    # MUISEVENTS AFHANDELEN
    #
    if scene.mouse.events:  # zijn er muisevents?

        m1 = scene.mouse.getevent()  # event ophalen

        if m1.press:  # is het een muisklik?

            if mag(arr.pos - m1.pos) <= by:  # zijn we bij de staart?
                drag = 'tail'  # bij de staart van de pijl
            elif mag((arr.pos + arr.axis) - m1.pos) <= by:  # of bij de punt?
                drag = 'tip'  # bij de punt van de pijl

            drag_pos = m1.pos  # sla de locatie van de klik op in drag_pos

        elif m1.drop:  # losgelaten na het slepen
            drag = None  # stoppen met slepen

    #
    # DE PIJL VERPLAATSEN
    #
    if drag is not None:  # het kan 'tail', 'tip' of None zijn

        new_pos = scene.mouse.pos  # haal de huidige muispositie op

        if new_pos != drag_pos:  # als de muis bewogen heeft

            displace = new_pos - drag_pos  # de muis heeft zo ver bewogen
            drag_pos = new_pos  # pas de sleeppositie aan

            if drag == 'tail':
                arr.pos += displace  # verplaats de staart
            else:
                arr.axis += displace  # verplaats de punt
