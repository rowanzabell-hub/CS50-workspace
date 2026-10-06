import canvas2d
import math


def draw_my_illusion(canvas):
    # Black lines
    canvas.set_pen_color(canvas.BLACK)
    canvas.set_pen_width(1)

    for i in range(100):
        angle = math.radians(i * 3.6)

        x1 = 500 - 700 * math.cos(angle)
        y1 = 500 - 700 * math.sin(angle)
        x2 = 500 + 700 * math.cos(angle)
        y2 = 500 + 700 * math.sin(angle)

        canvas.line(x1, y1, x2, y2)

    # Two thin red vertical lines
    canvas.set_pen_color(canvas.RED)
    canvas.set_pen_width(2)

    canvas.line(475, 0, 475, 1000)
    canvas.line(525, 0, 525, 1000)


def main():
    canvas = canvas2d.Canvas(1000, 1000)
    canvas.clear(canvas.WHITE)
    draw_my_illusion(canvas)
    canvas.wait_for_close()


if __name__ == "__main__":





    main()
