"""
Warm-Up 2: Crosshairs

draw_crosshairs() below only draws part of a "+". Finish it.
"""
import canvas2d


def draw_crosshairs(canvas):
    """Draw a red '+' through the center of the canvas.

    Right now this only draws a line from the center to the right
    edge. Two things are missing:
      1. That line should span the FULL canvas, left edge to right edge.
      2. There should also be a vertical line spanning the full canvas.
    """
    canvas.set_pen_color(canvas.RED)

    # BUG: this only reaches from the center to the right edge.
    canvas.line(250, 250, 500, 250)

    # TODO: add another line through the center from top to bottom



def main():
    canvas = canvas2d.Canvas(500, 500)
    canvas.clear(canvas.WHITE)
    canvas.set_pen_width(5)
    draw_crosshairs(canvas)
    canvas.wait_for_close()


if __name__ == "__main__":
    main()
