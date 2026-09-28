"""
Warm-Up 1: Circle and Square

There's a bug in draw_circle_and_square() below: the circle is too
big for the square. Find and fix it.
"""
import canvas2d


def draw_circle_and_square(canvas):
    """Draw a square with a circle inscribed exactly inside it.

    The circle should touch all four sides of the square, right in the
    middle, with no gap and no overlap. Run this once first and look
    at how far the circle pokes out past the square's edges.
    """
    canvas.set_pen_color(canvas.BLUE)
    canvas.rectangle(250, 250, 300, 300)

    canvas.set_pen_color(canvas.RED)
    # BUG: This circle's numbers (aka arguments) are all wrong!
    # Change the arguments so the circle neatly fills the square
    canvas.circle(100, 100, 100)



def main():
    canvas = canvas2d.Canvas(500, 500)
    canvas.clear(canvas.WHITE)
    canvas.set_pen_width(5)
    draw_circle_and_square(canvas)
    canvas.wait_for_close()


if __name__ == "__main__":
    main()
