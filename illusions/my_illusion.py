
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

    for i in range(48):
        angle = math.radians(i * 7.5)
        x1 = 500 - 700 * math.cos(angle)
        y1 = 500 - 700 * math.sin(angle)
        x2 = 500 + 700 * math.cos(angle)
        y2 = 500 + 700 * math.sin(angle)
        canvas.line(x1, y1, x2, y2)

    # Red vertical parallel lines in front
    canvas.set_pen_color(canvas.RED)
    canvas.set_pen_width(2)

    for i in range(5):
        x = 300 + i * 100
        canvas.line(x, 0, x, 1000)


def main():
    canvas = canvas2d.Canvas(1000, 1000)
    canvas.clear(canvas.WHITE)
    draw_my_illusion(canvas)
    canvas.wait_for_close()


if __name__ == "__main__":
    main()
