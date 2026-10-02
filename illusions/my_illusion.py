"""
The Assignment: Your Illusion

Pick one of the five optical illusions described in the README and
recreate it here with canvas2d. Then modify it in some way (colors,
number of shapes, line thickness, or anything else) so your version
is distinct from the original, without breaking the illusion.
"""
import canvas2d


def draw_my_illusion(canvas):
    """Draw your chosen illusion."""
    # Hering's Illusion

    canvas.set_pen_color(canvas.RED)
    canvas.set_pen_width(4)

    for i in range(15):
        y = 100 + i * 60
        canvas.line(100, y, 900, y)

    canvas.set_pen_color(canvas.BLACK)
    canvas.set_pen_width(3)

    for i in range(13):
        x = 200 + i * 50
        canvas.line(500, 500, x, 100)

    for i in range(13):
        x = 200 + i * 50
        canvas.line(500, 500, x, 900)


def main():
    canvas = canvas2d.Canvas(1000, 1000)
    canvas.clear(canvas.WHITE)
    draw_my_illusion(canvas)
    canvas.wait_for_close()


if __name__ == "__main__":
    main()
