"""
Warm-Up 4: Piano Pattern

draw_piano_pattern() below draws the white piano keys but is missing
the black keys. Finish it.
"""
import canvas2d




def draw_piano_pattern(canvas):
    """Draw a row of piano keys: white key outlines plus black filled keys.

    Right now this only draws the white key outlines. Missing: a
    filled black rectangle for the black key that sits between each
    pair of white keys.
    """
    canvas.set_pen_color(canvas.BLACK)
    for i in range(6):
        key_x = 50 + i * 60 # More variables! Don't change this one though
        canvas.rectangle(key_x, 250, 60, 350) # Don't change this line either

        # TODO: add a filled black rectangle for the black key here
        

    # Draws the extra white key at the end. Leave this alone!
    canvas.rectangle(410, 250, 60, 350)


def main():
    canvas = canvas2d.Canvas(500, 500)
    canvas.clear(canvas.WHITE)
    canvas.set_pen_width(3)
    draw_piano_pattern(canvas)
    canvas.wait_for_close()


if __name__ == "__main__":
    main()
