from png import *


def change(p):
    """Change takes in a pixel (an [R,G,B] list)
    and returns a new pixel to take its place!
    """
    red = p[0]
    green = p[1]
    blue = p[2]
    return [255 - red, 255 - green, 255 - blue]


def invert():
    """Run this function to read in the in.png image,
    change it, and write out the result to out.png
    """
    im_pix = get_rgb("in.png")  # lees het bestand in.png in

    print("De eerste twee pixels van de eerste rij zijn", im_pix[0][0:2])

    # Onthoud dat im_pix een lijst (de afbeelding) van
    # lijsten (elke rij) van lijsten (elke pixel is [R,G,B]) is

    new_pix = []

    for row in im_pix:
        new_row = []

        for pixel in row:
            new_pixel = change(pixel)
            new_row += [new_pixel]

        new_pix += [new_row]

    # sla nu het bestand 'out.png' op
    save_rgb(new_pix, "out.png")


# uitproberen!
invert()
