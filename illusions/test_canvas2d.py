"""
Run this file first, before touching any of the warm-ups, to confirm
canvas2d is working.

    python3 test_canvas2d.py

You should see a window pop up with a red circle in the middle. Close
the window when you're done, it will stay open until you close it.
"""
import canvas2d

canvas = canvas2d.Canvas(400, 400)
canvas.set_pen_color(canvas.RED)
canvas.filled_circle(200, 200, 80)
canvas.wait_for_close()
