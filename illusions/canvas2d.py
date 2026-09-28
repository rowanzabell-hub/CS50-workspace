"""
canvas2d: a small drawing library, built on top of Python's built-in
tkinter, with the same style of functions as dudraw (set_pen_color,
line, filled_circle, etc.) but using plain pixel coordinates instead
of a 0-1 unit square.

You don't need to read or understand this file to do the warm-ups.
Create a canvas, then call its methods:

    canvas = canvas2d.Canvas(512, 512)
    canvas.set_pen_color(canvas.RED)
    canvas.filled_circle(256, 256, 80)
    canvas.wait_for_close()

Coordinates: (0, 0) is the top-left corner of the canvas. x increases
to the right, y increases downward. Both range from 0 up to whatever
size you pass to Canvas(w, h) -- canvas.width and canvas.height hold
those numbers, so you never have to hardcode them.

Angles (for sector / filled_sector): measured in degrees, 0 pointing
right (the positive x direction), increasing counterclockwise. Same
convention you'd see in math class.
"""
import time
import tkinter

BLACK = "black"
WHITE = "white"
RED = "red"
GREEN = "green"
BLUE = "blue"
YELLOW = "yellow"
ORANGE = "orange"
MAGENTA = "magenta"
CYAN = "cyan"
GRAY = "gray"
LIGHT_GRAY = "light gray"
DARK_GRAY = "dim gray"


class Canvas:
    """A drawing window. Call its methods to draw on it, e.g. canvas.line(...)."""

    # Also available as canvas.RED, canvas.BLUE, etc. on any Canvas instance.
    BLACK = BLACK
    WHITE = WHITE
    RED = RED
    GREEN = GREEN
    BLUE = BLUE
    YELLOW = YELLOW
    ORANGE = ORANGE
    MAGENTA = MAGENTA
    CYAN = CYAN
    GRAY = GRAY
    LIGHT_GRAY = LIGHT_GRAY
    DARK_GRAY = DARK_GRAY

    def __init__(self, width, height):
        """Open a drawing window of the given size, in pixels."""
        self.width = width
        self.height = height
        self._root = tkinter.Tk()
        self._root.title("canvas2d")
        self._widget = tkinter.Canvas(self._root, width=width, height=height, highlightthickness=0)
        self._widget.pack()
        self._pen_color = BLACK
        self._pen_width = 1
        self._root.update()
        self._bring_to_front()

    def _bring_to_front(self):
        """Bring this window to the front of the screen.

        Without this, the window can open behind your editor/terminal
        instead of in front of it. Briefly marking it "always on top"
        forces the window manager to raise it above every other
        window (including ones in other apps); we turn that back off
        right after so it doesn't stay stuck above everything.
        """
        self._root.deiconify()
        self._root.lift()
        self._root.focus_force()
        self._root.attributes("-topmost", True)
        self._root.after_idle(self._root.attributes, "-topmost", False)

    def clear(self, color):
        """Fill the whole canvas with a color."""
        self._widget.configure(bg=color)

    def set_pen_color(self, color):
        """Set the color used by shapes drawn after this call, e.g. canvas.RED."""
        self._pen_color = color

    def set_pen_color_rgb(self, r, g, b):
        """Same as set_pen_color, but as three 0-255 numbers instead of a named color."""
        self._pen_color = "#%02x%02x%02x" % (int(r), int(g), int(b))

    def set_pen_width(self, width):
        """Set line thickness, in pixels."""
        self._pen_width = width

    def line(self, x0, y0, x1, y1):
        """Draw a line segment between two points."""
        self._widget.create_line(x0, y0, x1, y1, fill=self._pen_color, width=self._pen_width)

    def circle(self, x, y, r):
        """Draw an outlined circle centered at (x, y) with radius r."""
        self._widget.create_oval(x - r, y - r, x + r, y + r, outline=self._pen_color, width=self._pen_width)

    def filled_circle(self, x, y, r):
        """Draw a filled circle centered at (x, y) with radius r."""
        self._widget.create_oval(x - r, y - r, x + r, y + r, fill=self._pen_color, outline=self._pen_color)

    def rectangle(self, x, y, width, height):
        """Draw an outlined rectangle centered at (x, y) with the given width and height."""
        self._widget.create_rectangle(
            x - width / 2, y - height / 2, x + width / 2, y + height / 2,
            outline=self._pen_color, width=self._pen_width,
        )

    def filled_rectangle(self, x, y, width, height):
        """Draw a filled rectangle centered at (x, y) with the given width and height."""
        self._widget.create_rectangle(
            x - width / 2, y - height / 2, x + width / 2, y + height / 2,
            fill=self._pen_color, outline=self._pen_color,
        )

    def sector(self, x, y, r, angle1, angle2):
        """Draw an outlined "pizza slice" of a circle centered at (x, y) with radius r, from angle1 to angle2 (in degrees)."""
        self._widget.create_arc(
            x - r, y - r, x + r, y + r,
            start=angle1, extent=angle2 - angle1,
            style=tkinter.PIESLICE, outline=self._pen_color, width=self._pen_width,
        )

    def filled_sector(self, x, y, r, angle1, angle2):
        """Draw a filled "pizza slice" of a circle centered at (x, y) with radius r, from angle1 to angle2 (in degrees)."""
        self._widget.create_arc(
            x - r, y - r, x + r, y + r,
            start=angle1, extent=angle2 - angle1,
            style=tkinter.PIESLICE, fill=self._pen_color, outline=self._pen_color,
        )

    def pause(self, msec):
        """Render everything drawn so far, then wait msec milliseconds before returning.

        Handy for watching a loop draw one shape at a time while
        debugging: put this as the last line inside your loop.
        """
        self._widget.update()
        time.sleep(msec / 1000)

    def wait_for_close(self):
        """Render everything drawn so far, then block until you close the window by hand.

        Call this once, as the last line of main(). While the window
        is open, your terminal can't run any other commands, so this
        prints a heads-up before it blocks.
        """
        self._widget.update()
        self._bring_to_front()
        print()
        print("Your program is running. The window will stay open until you close it.")
        print("This terminal is stuck until then -- press Ctrl+C here if you need it back sooner.")
        print()
        self._root.mainloop()
