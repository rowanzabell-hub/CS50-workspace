
"""
The Assignment: Your Illusion

Pick one of the five optical illusions described in the README and
recreate it here with canvas2d. Then modify it in some way (colors,
number of shapes, line thickness, or anything else) so your version
is distinct from the original, without breaking the illusion.
"""
import canvas2d
import math


def draw_my_illusion(canvas):
    """Draw your chosen illusion."""
    # Hering's Illusion

    # Black radiating lines in the background
    canvas.set_pen_color(canvas.BLACK)
    canvas.set_pen_width(2)

    for i in range(24):
        angle = math.radians(i * 15)
        x = 500 + 700 * math.cos(angle)
        y = 500 + 700 * math.sin(angle)
        canvas.line(500 - 700 * math.cos(angle),
                    500 - 700 * math.sin(angle), x, y)

    # Red vertical parallel lines in front
    canvas.set_pen_color(canvas.RED)
    canvas.set_pen_width(5)

    for i in range(5):
        x = 300 + i * 100
        canvas.line(x, 100, x, 900)


def main():
    canvas = canvas2d.Canvas(1000, 1000)
    canvas.clear(canvas.WHITE)
    draw_my_illusion(canvas)
    canvas.wait_for_close()


if __name__ == "__main__":
    main()
