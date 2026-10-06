def draw_my_illusion(canvas):
    # Hering's Illusion

    # Lots of very thin black curved lines
    canvas.set_pen_color(canvas.BLACK)
    canvas.set_pen_width(1)

    for i in range(70):
        offset = i * 14

        canvas.arc(500 - offset, 250, 1000 + offset * 2, 500, 0, 180)
        canvas.arc(500 - offset, 250, 1000 + offset * 2, 500, 180, 180)

    # Two thin red vertical lines in the middle
    canvas.set_pen_color(canvas.RED)
    canvas.set_pen_width(2)

    canvas.line(475, 0, 475, 1000)
    canvas.line(525, 0, 525, 1000)
