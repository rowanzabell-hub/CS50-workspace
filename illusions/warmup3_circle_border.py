"""
Warm-Up 3: Circle Border

draw_circle_border() below only draws two of the canvas's four
borders (top and bottom). Finish it.
"""
import canvas2d




def draw_circle_border(canvas):
    """Draw a border of green circles around all four edges of the canvas.

    Right now this only draws circles along the top and bottom edges.
    Missing: circles along the left and right edges, evenly spaced the
    same way. The top/bottom loop below shows the pattern to follow;
    write a second loop that does the same thing for the left and
    right edges.
    """
    canvas.set_pen_color_rgb(111, 194, 118) # Soft green

    # Top and bottom borders
    for i in range(11):
        top_bottom_x = i * 50 # This is a variable!
        canvas.filled_circle(top_bottom_x, 0, 25)
        canvas.filled_circle(top_bottom_x, 500, 25)

    # TODO: write a loop that draws circles down the left and right
    # edges, spaced the same way as the top/bottom loop above.



def main():
    canvas = canvas2d.Canvas(500, 500)
    canvas.clear(canvas.WHITE)
    draw_circle_border(canvas)
    canvas.wait_for_close()


if __name__ == "__main__":
    main()
